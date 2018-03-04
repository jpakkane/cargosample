#!/usr/bin/env python3

# Copyright 2018 Jussi Pakkanen

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import subprocess, sys, os
import pathlib

header_templ = '''project('%s', 'rust', version : '%s')

'''

target_templ = '''%s_lib = static_library('%s',
  '%s')

'''

dep_templ = '''%s_dep = declare_dependency(link_with : %s_lib)\n'''

def get_crate_repo_url(crate_name, crate_version):
    # Crates.io does not seem to provide a query API
    # and the web site is 100% javascript so web scraping
    # is impossible. Thanks.
    if crate_name != 'itoa':
        sys.exit('This demo script only supports the itoa crate.')
    if crate_version != '0.3.4':
        sys.exit('This demo script only supports version 0.3.4.')
    return 'https://github.com/dtolnay/itoa.git'

def create_checkout(crate_name, crate_version):
    spdir = pathlib.Path('subprojects')
    outdir = spdir / ('%s-%s' % (crate_name, crate_version))
    if outdir.exists():
        print('Output path %s already exists, not doing a checkout.' % outdir)
        return outdir
    crate_url = get_crate_repo_url(crate_name, crate_version)
    subprocess.check_call(['git', 'clone', crate_url, str(outdir)])
    subprocess.check_call(['git', 'checkout', crate_version], cwd=outdir)
    return outdir

def create_mesonfiles(crate_name, crate_version, outdir):
    mfile = outdir / 'meson.build'
    with mfile.open('w') as ofile:
        ofile.write(header_templ % (crate_name, crate_version))
        ofile.write(target_templ % (crate_name,
                                    crate_name,
                                    'src/lib.rs'))
        ofile.write(dep_templ % (crate_name, crate_name))

def convert_single(crate_name, crate_version):
    outdir = create_checkout(crate_name, crate_version)
    create_mesonfiles(crate_name, crate_version, outdir)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(sys.argv[0] + ' <name of dependency> <version of dependency>')
    (name, version) = sys.argv[1:]
    if not os.path.exists('subprojects'):
        sys.exit('Subprojects directory does not exist.')
    convert_single(name, version)
