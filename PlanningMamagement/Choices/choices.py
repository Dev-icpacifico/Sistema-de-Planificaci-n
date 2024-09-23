trabajado = 'Trabajado'
no_trabajado = 'No Trabajado'
pendiente = 'Pendiente'

WORKED_DAY_CHOICES = [(trabajado, 'Trabajado'),
                      (no_trabajado, 'No Trabajado'),
                      (pendiente, 'Pendiente'), ]

programada = 'Programada'
reserva = 'Reserva'
pendiente = 'Pendiente'
retrabajo = 'ReTrabajo'
ejecutada_no_planificada = 'Ejec/No Plan'

ACTIV_TYPE_CHOICES = [(programada, 'Programada'),
                      (reserva, 'Reserva'),
                      (pendiente, 'Pendiente'),
                      (retrabajo, 'ReTrabajo'),
                      (ejecutada_no_planificada, 'Ejec/No Plan'), ]

obra_gruesa = 'Obra Gruesa'
terminaciones = 'Terminaciones'
obras_exteriores = 'Obras Exteriores'

FRENTES_CHOICES = [(obra_gruesa, 'Obra Gruesa'),
                  (terminaciones, 'Terminaciones'),
                  (obras_exteriores, 'Obras Exteriores'), ]
