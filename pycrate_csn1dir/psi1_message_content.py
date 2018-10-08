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
# * File Name : pycrate_csn1dir/psi1_message_content.py
# * Created : 2018-10-08
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.18 Packet System Information Type 1
# top-level object: PSI1 message content

# external references
from pycrate_csn1dir.pccch_organization_parameters_ie import pccch_organization_parameters_ie
from pycrate_csn1dir.padding_bits import padding_bits
from pycrate_csn1dir.global_power_control_parameters_ie import global_power_control_parameters_ie
from pycrate_csn1dir.gprs_cell_options_ie import gprs_cell_options_ie
from pycrate_csn1dir.prach_control_parameters_ie import prach_control_parameters_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

psi1_message_content = CSN1List(name='psi1_message_content', list=[
  CSN1Bit(name='page_mode', bit=2),
  CSN1Bit(name='pbcch_change_mark', bit=3),
  CSN1Bit(name='psi_change_field', bit=4),
  CSN1Bit(name='psi1_repeat_period', bit=4),
  CSN1Bit(name='psi_count_lr', bit=6),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='psi_count_hr', bit=4)])}),
  CSN1Bit(name='measurement_order'),
  CSN1Ref(name='gprs_cell_options', obj=gprs_cell_options_ie),
  CSN1Ref(name='prach_control_parameters', obj=prach_control_parameters_ie),
  CSN1Ref(name='pccch_organization_parameters', obj=pccch_organization_parameters_ie),
  CSN1Ref(name='global_power_control_parameters', obj=global_power_control_parameters_ie),
  CSN1Bit(name='psi_status_ind'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='mscr'),
    CSN1Bit(name='sgsnr'),
    CSN1Bit(name='band_indicator'),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='lb_ms_txpwr_max_cch', bit=5)])}),
      CSN1Ref(obj=padding_bits)]),
      None: ('', [])})]),
    None: ('', [])})])

