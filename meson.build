project('cargosample', 'rust')

itoa_sp = subproject('itoa-0.3.4')
itoa_dep = itoa_sp.get_variable('itoa_dep')

executable('prog', 'prog.rs',
  dependencies : itoa_dep)
