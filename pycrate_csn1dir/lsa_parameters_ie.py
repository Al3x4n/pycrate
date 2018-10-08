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
# * File Name : pycrate_csn1dir/lsa_parameters_ie.py
# * Created : 2018-10-08
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 12.28 LSA Parameters
# top-level object: LSA Parameters IE



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

lsa_id_information_struct = CSN1List(name='lsa_id_information_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Alt(alt={
      '0': ('', [
      CSN1Bit(name='lsa_id', bit=24)]),
      '1': ('', [
      CSN1Bit(name='shortlsa_id', bit=10)])})]),
  CSN1Val(name='', val='0')])

lsa_parameters_ie = CSN1List(name='lsa_parameters_ie', list=[
  CSN1Bit(name='nr_of_freq_or_cells', bit=5),
  CSN1Ref(name='lsa_id_information', obj=lsa_id_information_struct, num=([0], lambda x: x))])

