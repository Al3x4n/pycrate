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
# * File Name : pycrate_csn1dir/si2quater_rest_octets.py
# * Created : 2018-10-08
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.33b SI 2quater Rest Octets
# top-level object: SI2quater Rest Octets

# external references
from pycrate_csn1dir.pcid_group_ie import pcid_group_ie
from pycrate_csn1dir.enhanced_cell_reselection_parameters_ie import enhanced_cell_reselection_parameters_ie
from pycrate_csn1dir.psc_group_ie import psc_group_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_bit = CSN1Bit(name='spare_bit')
Spare_bit = spare_bit
Spare_Bit = spare_bit

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

extended_earfcns_description_for_csg_cells_struct = CSN1List(name='extended_earfcns_description_for_csg_cells_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='csg_earfcn_extended', bit=18)]),
  CSN1Val(name='', val='0')])

measurement_parameters_description_struct = CSN1List(name='measurement_parameters_description_struct', list=[
  CSN1Bit(name='report_type'),
  CSN1Bit(name='serving_band_reporting', bit=2)])

gprs_report_priority_description_struct = CSN1List(name='gprs_report_priority_description_struct', list=[
  CSN1Bit(name='number_cells', bit=7),
  CSN1Bit(name='rep_priority', num=([0], lambda x: x))])

extended_earfcns_description_struct = CSN1List(name='extended_earfcns_description_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='earfcn_extended', bit=18)]),
  CSN1Val(name='', val='0')])

repeated_utran_tdd_neighbour_cells_struct = CSN1List(name='repeated_utran_tdd_neighbour_cells_struct', list=[
  CSN1Val(name='', val='0'),
  CSN1Bit(name='tdd_arfcn', bit=14),
  CSN1Bit(name='tdd_indic0'),
  CSN1Bit(name='nr_of_tdd_cells', bit=5),
  CSN1Bit(name='tdd_cell_information_field', bit=('# unprocessed: (q(NR_OF_TDD_CELLS))', lambda: 0))])

utran_tdd_description_struct = CSN1List(name='utran_tdd_description_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='bandwidth_tdd', bit=3)])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='repeated_utran_tdd_neighbour_cells', obj=repeated_utran_tdd_neighbour_cells_struct)]),
  CSN1Val(name='', val='0')])

repeated_utran_fdd_neighbour_cells_struct = CSN1List(name='repeated_utran_fdd_neighbour_cells_struct', list=[
  CSN1Val(name='', val='0'),
  CSN1Bit(name='fdd_arfcn', bit=14),
  CSN1Bit(name='fdd_indic0'),
  CSN1Bit(name='nr_of_fdd_cells', bit=5),
  CSN1Bit(name='fdd_cell_information_field', bit=('# unprocessed: (p(NR_OF_FDD_CELLS))', lambda: 0))])

e_utran_csg_cells_reporting_description_struct = CSN1List(name='e_utran_csg_cells_reporting_description_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='e_utran_csg_fdd_reporting_threshold', bit=3),
    CSN1Bit(name='e_utran_csg_fdd_reporting_threshold_2', bit=6)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='e_utran_csg_tdd_reporting_threshold', bit=3),
    CSN1Bit(name='e_utran_csg_fdd_reporting_threshold_2', bit=6)])})])

ccn_support_description_struct = CSN1List(name='ccn_support_description_struct', list=[
  CSN1Bit(name='number_cells', bit=7),
  CSN1Bit(name='ccn_supported', num=([0], lambda x: x))])

utran_csg_cells_reporting_description_struct = CSN1List(name='utran_csg_cells_reporting_description_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='utran_csg_fdd_reporting_threshold', bit=3),
    CSN1Bit(name='utran_csg_fdd_reporting_threshold_2', bit=6)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='utran_csg_tdd_reporting_threshold', bit=3)])})])

gprs_3g_measurement_parameters_description_struct = CSN1List(name='gprs_3g_measurement_parameters_description_struct', list=[
  CSN1Bit(name='qsearch_p', bit=4),
  CSN1Val(name='', val='1'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='fdd_rep_quant'),
    CSN1Bit(name='fdd_multirat_reporting', bit=2)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='fdd_reporting_offset', bit=3),
    CSN1Bit(name='fdd_reporting_threshold', bit=3)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='tdd_multirat_reporting', bit=2)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='tdd_reporting_offset', bit=3),
    CSN1Bit(name='tdd_reporting_threshold', bit=3)])})])

_3g_measurement_parameters_description_struct = CSN1List(name='_3g_measurement_parameters_description_struct', list=[
  CSN1Bit(name='qsearch_i', bit=4),
  CSN1Bit(name='qsearch_c_initial'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='fdd_qoffset', bit=4),
    CSN1Bit(name='fdd_rep_quant'),
    CSN1Bit(name='fdd_multirat_reporting', bit=2),
    CSN1Bit(name='fdd_qmin', bit=3)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='tdd_qoffset', bit=4),
    CSN1Bit(name='tdd_multirat_reporting', bit=2)])})])

rtd6_struct = CSN1List(name='rtd6_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='0'),
    CSN1Bit(name='rtd', bit=6)]),
  CSN1Val(name='', val='1')])

_3g_additional_measurement_parameters_description_2_struct = CSN1Alt(name='_3g_additional_measurement_parameters_description_2_struct', alt={
  '0': ('', []),
  '1': ('', [
  CSN1Bit(name='fdd_reporting_threshold_2', bit=6)])})

csg_cells_reporting_description_struct = CSN1List(name='csg_cells_reporting_description_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='utran_csg_cells_reporting_description', obj=utran_csg_cells_reporting_description_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='e_utran_csg_cells_reporting_description', obj=e_utran_csg_cells_reporting_description_struct)])})])

gprs_e_utran_measurement_parameters_description_struct = CSN1List(name='gprs_e_utran_measurement_parameters_description_struct', list=[
  CSN1Bit(name='qsearch_p_e_utran', bit=4),
  CSN1Bit(name='e_utran_rep_quant'),
  CSN1Bit(name='e_utran_multirat_reporting', bit=2),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='e_utran_fdd_reporting_threshold', bit=3),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='e_utran_fdd_reporting_threshold_2', bit=6)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='e_utran_fdd_reporting_offset', bit=3)])})])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='e_utran_tdd_reporting_threshold', bit=3),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='e_utran_tdd_reporting_threshold_2', bit=6)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='e_utran_tdd_reporting_offset', bit=3)])})])})])

repeated_utran_priority_parameters_struct = CSN1List(name='repeated_utran_priority_parameters_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='utran_frequency_index', bit=5)]),
  CSN1Val(name='', val='0'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='utran_priority', bit=3)])}),
  CSN1Bit(name='thresh_utran_high', bit=5),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='thresh_utran_low', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='utran_qrxlevmin', bit=5)])})])

_3g_additional_measurement_parameters_description_struct = CSN1List(name='_3g_additional_measurement_parameters_description_struct', list=[
  CSN1Bit(name='fdd_qmin_offset', bit=3),
  CSN1Bit(name='fdd_rscpmin', bit=4)])

si2q_extension_information = CSN1List(name='si2q_extension_information', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='ccn_support_description', obj=ccn_support_description_struct)])}),
  CSN1Ref(obj=spare_bit, num=-1)])

e_utran_measurement_parameters_description_struct = CSN1List(name='e_utran_measurement_parameters_description_struct', list=[
  CSN1Bit(name='qsearch_c_e_utran_initial', bit=4),
  CSN1Bit(name='e_utran_rep_quant'),
  CSN1Bit(name='e_utran_multirat_reporting', bit=2),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='e_utran_fdd_reporting_threshold', bit=3),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='e_utran_fdd_reporting_threshold_2', bit=6)])}),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='e_utran_fdd_reporting_offset', bit=3)])})])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='e_utran_tdd_reporting_threshold', bit=3),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='e_utran_tdd_reporting_threshold_2', bit=6)])}),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='e_utran_tdd_reporting_offset', bit=3)])})])})]),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='e_utran_fdd_measurement_report_offset', bit=6),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='e_utran_fdd_reporting_threshold_2', bit=6)])}),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='e_utran_fdd_reporting_offset', bit=3)])})])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='e_utran_tdd_measurement_report_offset', bit=6),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='e_utran_tdd_reporting_threshold_2', bit=6)])}),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='e_utran_tdd_reporting_offset', bit=3)])})])}),
    CSN1Bit(name='reporting_granularity')])})])

repeated_e_utran_not_allowed_cells_struct = CSN1List(name='repeated_e_utran_not_allowed_cells_struct', list=[
  CSN1Ref(name='not_allowed_cells', obj=pcid_group_ie),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='e_utran_frequency_index', bit=3)]),
  CSN1Val(name='', val='0')])

gprs_bsic_description_struct = CSN1List(name='gprs_bsic_description_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='ba_index_start_bsic', bit=5)])}),
  CSN1Bit(name='bsic', bit=6),
  CSN1Bit(name='number_remaining_bsic', bit=7),
  CSN1List(num=([2], lambda x: x), list=[
    CSN1Bit(name='frequency_scrolling'),
    CSN1Bit(name='bsic', bit=6)])])

e_utran_csg_description_struct = CSN1List(name='e_utran_csg_description_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='csg_pci_split', obj=pcid_group_ie),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Bit(name='e_utran_frequency_index', bit=3)]),
    CSN1Val(name='', val='0')]),
  CSN1Val(name='', val='0'),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='csg_earfcn', bit=16)]),
  CSN1Val(name='', val='0')])

repeated_e_utran_pcid_to_ta_mapping_struct = CSN1List(name='repeated_e_utran_pcid_to_ta_mapping_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='pcid_to_ta_mapping', obj=pcid_group_ie)]),
  CSN1Val(name='', val='0'),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='e_utran_frequency_index', bit=3)]),
  CSN1Val(name='', val='0')])

rtd12_struct = CSN1List(name='rtd12_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='0'),
    CSN1Bit(name='rtd', bit=12)]),
  CSN1Val(name='', val='1')])

serving_cell_priority_parameters_description_struct = CSN1List(name='serving_cell_priority_parameters_description_struct', list=[
  CSN1Bit(name='geran_priority', bit=3),
  CSN1Bit(name='thresh_priority_search', bit=4),
  CSN1Bit(name='thresh_gsm_low', bit=4),
  CSN1Bit(name='h_prio', bit=2),
  CSN1Bit(name='t_reselection', bit=2)])

nc_measurement_parameters_struct = CSN1List(name='nc_measurement_parameters_struct', list=[
  CSN1Bit(name='network_control_order', bit=2),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='nc__non_drx_period', bit=3),
    CSN1Bit(name='nc_reporting_period_i', bit=3),
    CSN1Bit(name='nc_reporting_period_t', bit=3)])})])

gprs_measurement_parameters_description_struct = CSN1List(name='gprs_measurement_parameters_description_struct', list=[
  CSN1Bit(name='report_type'),
  CSN1Bit(name='reporting_rate'),
  CSN1Bit(name='invalid_bsic_reporting'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='multiband_reporting', bit=2)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='serving_band_reporting', bit=2)])}),
  CSN1Bit(name='scale_ord', bit=2),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='_900_reporting_offset', bit=3),
    CSN1Bit(name='_900_reporting_threshold', bit=3)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='_1800_reporting_offset', bit=3),
    CSN1Bit(name='_1800_reporting_threshold', bit=3)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='_400_reporting_offset', bit=3),
    CSN1Bit(name='_400_reporting_threshold', bit=3)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='_1900_reporting_offset', bit=3),
    CSN1Bit(name='_1900_reporting_threshold', bit=3)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='_850_reporting_offset', bit=3),
    CSN1Bit(name='_850_reporting_threshold', bit=3)])})])

_3g_csg_description_struct = CSN1List(name='_3g_csg_description_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='csg_psc_split', obj=psc_group_ie),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Bit(name='utran_frequency_index', bit=5)]),
    CSN1Val(name='', val='0')]),
  CSN1Val(name='', val='0'),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Alt(alt={
      '0': ('', [
      CSN1Bit(name='csg_fdd_uarfcn', bit=14)]),
      '1': ('', [
      CSN1Bit(name='csg_tdd_uarfcn', bit=14)])})]),
  CSN1Val(name='', val='0')])

repeated_e_utran_neighbour_cells_struct = CSN1List(name='repeated_e_utran_neighbour_cells_struct', list=[
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='earfcn', bit=16),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='measurement_bandwidth', bit=3)])})]),
  CSN1Val(name='', val='0'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='e_utran_priority', bit=3)])}),
  CSN1Bit(name='thresh_e_utran_high', bit=5),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='thresh_e_utran_low', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='e_utran_qrxlevmin', bit=5)])})])

utran_fdd_description_struct = CSN1List(name='utran_fdd_description_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='bandwidth_fdd', bit=3)])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='repeated_utran_fdd_neighbour_cells', obj=repeated_utran_fdd_neighbour_cells_struct)]),
  CSN1Val(name='', val='0')])

gprs_real_time_difference_description_struct = CSN1List(name='gprs_real_time_difference_description_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='ba_index_start_rtd', bit=5)])}),
    CSN1Ref(name='rtd', obj=rtd6_struct),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='0'),
      CSN1Ref(name='rtd', obj=rtd6_struct)]),
    CSN1Val(name='', val='1')])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='ba_index_start_rtd', bit=5)])}),
    CSN1Ref(name='rtd', obj=rtd12_struct),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='0'),
      CSN1Ref(name='rtd', obj=rtd12_struct)]),
    CSN1Val(name='', val='1')])})])

e_utran_parameters_description_struct = CSN1List(name='e_utran_parameters_description_struct', list=[
  CSN1Bit(name='e_utran_ccn_active'),
  CSN1Bit(name='e_utran_start'),
  CSN1Bit(name='e_utran_stop'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='e_utran_measurement_parameters_description', obj=e_utran_measurement_parameters_description_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='gprs_e_utran_measurement_parameters_description', obj=gprs_e_utran_measurement_parameters_description_struct)])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='repeated_e_utran_neighbour_cells', obj=repeated_e_utran_neighbour_cells_struct)]),
  CSN1Val(name='', val='0'),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='repeated_e_utran_not_allowed_cells', obj=repeated_e_utran_not_allowed_cells_struct)]),
  CSN1Val(name='', val='0'),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='repeated_e_utran_pcid_to_ta_mapping', obj=repeated_e_utran_pcid_to_ta_mapping_struct)]),
  CSN1Val(name='', val='0')])

_3g_priority_parameters_description_struct = CSN1List(name='_3g_priority_parameters_description_struct', list=[
  CSN1Bit(name='utran_start'),
  CSN1Bit(name='utran_stop'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='default_utran_priority', bit=3),
    CSN1Bit(name='default_thresh_utran', bit=5),
    CSN1Bit(name='default_utran_qrxlevmin', bit=5)])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='repeated_utran_priority_parameters', obj=repeated_utran_priority_parameters_struct)]),
  CSN1Val(name='', val='0')])

priority_and_e_utran_parameters_description_struct = CSN1List(name='priority_and_e_utran_parameters_description_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='serving_cell_priority_parameters_description', obj=serving_cell_priority_parameters_description_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='_3g_priority_parameters_description', obj=_3g_priority_parameters_description_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='e_utran_parameters_description', obj=e_utran_parameters_description_struct)])})])

_3g_neighbour_cell_description_struct = CSN1List(name='_3g_neighbour_cell_description_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='index_start_3g', bit=7)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='absolute_index_start_emr', bit=7)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='utran_fdd_description', obj=utran_fdd_description_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='utran_tdd_description', obj=utran_tdd_description_struct)])})])

si2quater_rest_octets = CSN1List(name='si2quater_rest_octets', list=[
  CSN1Bit(name='ba_ind'),
  CSN1Bit(name='_3g_ba_ind'),
  CSN1Bit(name='mp_change_mark'),
  CSN1Bit(name='si2quater_index', bit=4),
  CSN1Bit(name='si2quater_count', bit=4),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='measurement_parameters_description', obj=measurement_parameters_description_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='gprs_real_time_difference_description', obj=gprs_real_time_difference_description_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='gprs_bsic_description', obj=gprs_bsic_description_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='gprs_report_priority_description', obj=gprs_report_priority_description_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='gprs_measurement_parameters_description', obj=gprs_measurement_parameters_description_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='nc_measurement_parameters', obj=nc_measurement_parameters_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='extension_length', bit=8),
    CSN1Ref(obj=si2q_extension_information, lref=([1], lambda x: x + 1))])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='_3g_neighbour_cell_description', obj=_3g_neighbour_cell_description_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='_3g_measurement_parameters_description', obj=_3g_measurement_parameters_description_struct)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='gprs_3g_measurement_parameters_description', obj=gprs_3g_measurement_parameters_description_struct)])}),
  CSN1Alt(alt={
    'H': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='_3g_additional_measurement_parameters_description', obj=_3g_additional_measurement_parameters_description_struct)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='_3g_additional_measurement_parameters_description_2', obj=_3g_additional_measurement_parameters_description_2_struct)])}),
    CSN1Alt(alt={
      'H': ('', [
      CSN1Bit(name='_3g_ccn_active'),
      CSN1Alt(alt={
        'H': ('', [
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Bit(name='_700_reporting_offset', bit=3),
          CSN1Bit(name='_700_reporting_threshold', bit=3)])}),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Bit(name='_810_reporting_offset', bit=3),
          CSN1Bit(name='_810_reporting_threshold', bit=3)])}),
        CSN1Alt(alt={
          'H': ('', [
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Ref(name='priority_and_e_utran_parameters_description', obj=priority_and_e_utran_parameters_description_struct)])}),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Ref(name='_3g_csg_description', obj=_3g_csg_description_struct)])}),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Ref(name='e_utran_csg_description', obj=e_utran_csg_description_struct)])}),
          CSN1Alt(alt={
            'H': ('', [
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Ref(name='enhanced_cell_reselection_parameters_description', obj=enhanced_cell_reselection_parameters_ie)])}),
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Ref(name='csg_cells_reporting_description', obj=csg_cells_reporting_description_struct)])}),
            CSN1Alt(alt={
              'H': ('', [
              CSN1Alt(alt={
                '0': ('', []),
                '1': ('', [
                CSN1Bit(name='init_pwr_red')])}),
              CSN1Bit(name='nc2_csg_pccn_permitted')]),
              'L': ('', []),
              None: ('', [])}),
            CSN1Alt(alt={
              'H': ('', [
              CSN1Alt(alt={
                '0': ('', []),
                '1': ('', [
                CSN1Ref(name='extended_earfcns_description', obj=extended_earfcns_description_struct)])}),
              CSN1Alt(alt={
                '0': ('', []),
                '1': ('', [
                CSN1Ref(name='extended_earfcns_description_for_csg_cells', obj=extended_earfcns_description_for_csg_cells_struct)])})]),
              'L': ('', []),
              None: ('', [])})]),
            'L': ('', []),
            None: ('', [])})]),
          'L': ('', []),
          None: ('', [])})]),
        'L': ('', []),
        None: ('', [])})]),
      'L': ('', []),
      None: ('', [])})]),
    'L': ('', []),
    None: ('', [])}),
  CSN1Ref(obj=spare_padding)])

