"""
>>> calcular_telefone('1-HOME-SWEET-HOME')
'1-4663-79338-4663 '
>>> calcular_telefone('MY-MISERABLE-JOB')
'69-647372253-562'
>>> calcular_telefone('6Y-MISERABLE-JOB')
'69-647372253-562'
>>> calcular_telefone('69-MISERABLE-JOB')
'69-647372253-562'
>>> calcular_telefone('6Y-M4SERABLE-JOB')
'69-647372253-562'
>>> calcular_telefone('6Y-M47ERABLE-JOB')
'69-647372253-562'
>>> calcular_telefone('6Y-M473RABLE-JOB')
'69-647372253-562'
>>> calcular_telefone('6Y-M473R2BLE-JOB')
'69-647372253-562'
"""
# http://dojopuzzles.com/problemas/exibe/encontre-o-telefone/
import string

string.ascii_uppercase

# ABC    ->  2
# DEF    ->  3
# GHI    ->  4
# JKL    ->  5
# MNO    ->  6
# PQRS    ->  7
# TUV    ->  8
# WXYZ   ->  9
