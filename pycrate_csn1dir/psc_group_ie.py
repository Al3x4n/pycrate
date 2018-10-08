# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.3
# *
# * Copyright 2018. Benoit Michau. ANSSI.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_csn1dir/psc_group_ie.py
# * Created : 2018-10-08
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 12.58 PSC Group
# top-level object: PSC Group IE



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

psc_group_ie = CSN1List(name='psc_group_ie', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='psc', bit=9)]),
  CSN1Val(name='', val='0'),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='psc_pattern_length', bit=3),
    CSN1Bit(name='psc_pattern', bit=([1], lambda x: x + 1)),
    CSN1Bit(name='psc_pattern_sense')]),
  CSN1Val(name='', val='0')])

