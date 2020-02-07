# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.4
# *
# * Copyright 2016. Benoit Michau. ANSSI.
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
# * File Name : test/test_ether.py
# * Created : 2016-04-28
# * Authors : Benoit Michau 
# *--------------------------------------------------------
#*/

from timeit   import timeit
from binascii import unhexlify

from pycrate_ether.Ethernet import *
from pycrate_ether.ARP      import *
from pycrate_ether.IP       import *
from pycrate_ether.PCAP     import *

# enable TCP / UDP checksum calculation
TCP._CS_OFF = False
UDP._CS_OFF = False

# Some examples of Ethernet / ARP or IPv4 packets
eth_arp             = unhexlify(b'22334455667700112233445508060001080006040002001122334455c0a8000a223344556677c0a80001')
#
eth_ipv4_udp_dns    = unhexlify(b'0011223344552233445566770800450000469f4900003f115b02c0a80001c0a8000a0035cac100325d3f9ccd818000010001000000000469657466036f72670000010001c00c00010001000006f40004041fc62c')
eth_ipv4_tcp        = unhexlify(b'8c1645d7cd67fcecda022e37080045000034ce6600007606ea81acd912ceac1b201901bbde4058e3443e62715904801001be295b00000101080a464a8cef0764ac97')
eth_ipv4_tcp_http   = unhexlify(b'2233445566770011223344550800450001de94f4400040061928c0a8000a041fc62ccd460050418754bcd7b1410e8018001c929e00000101080a017ec07206520e5d474554202f20485454502f312e310d0a486f73743a20696574662e6f72670d0a557365722d4167656e743a204d6f7a696c6c612f352e3020285831313b205562756e74753b204c696e7578207838365f36343b2072763a34362e3029204765636b6f2f32303130303130312046697265666f782f34362e300d0a4163636570743a20746578742f68746d6c2c6170706c69636174696f6e2f7868746d6c2b786d6c2c6170706c69636174696f6e2f786d6c3b713d302e392c2a2f2a3b713d302e380d0a4163636570742d4c616e67756167653a20656e2d55532c656e3b713d302e350d0a4163636570742d456e636f64696e673a20677a69702c206465666c6174650d0a436f6f6b69653a207374796c6553686565743d310d0a436f6e6e656374696f6e3a206b6565702d616c6976650d0a49662d4d6f6469666965642d53696e63653a204d6f6e2c2032352041707220323031362032303a32323a353620474d540d0a49662d4e6f6e652d4d617463683a2022343736372d353331353466313233393865632d677a6970220d0a43616368652d436f6e74726f6c3a206d61782d6167653d300d0a0d0a')
eth_ipv4_sctp_data  = unhexlify(b'a44bb2d9e3cef60babc3b51408004500038000c700004084dcfeb8de2670bbb6fe2f0ded0ded818195460ed7d1440003011de57876220001af940000000501000b010000010d006a88d8003ec34c00836daf93280981030e190b12080012044366905824560b1208001104638313686909d96281d648043d0176f06b1a2818060700118605010101a00d600ba1090607040000010019026c81b1a181ae02010002012e3081a5800831389689465127f08407911501574210f304818f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000300dfe57876230001af950000000501000b01000000cf006a88d8003ec34d00836daf93c80981030e190b12070012045507842350430b12060011044340005450479b658198480410272e8c4904081608e46b262824060700118605010101a0196117a109060704000001000e03a203020100a305a1030201006c62a260020100305b020138a356a15430520410606161283ac926eb256cf41bfede584c04086013e4bb46cd1f0e04106aed5f0c8f12d661dbfae475c9fa767f04106207f65ace3942d0a3b041e81207bf520410ebba4f51ea7100000ec0abef5c71764700000300b0e57876240001af960000000501000b01000000a0006a88d8003ec34e00836daf93480981030e190b12950012044040051283600b12060011042602701363916c646a4904010404566c62a26002012c305b020138a356a1543052041013588fe881c390ec61a92684b5972bbc0408d54677a5743501ec041011bd061bcff52e3cba73751230c91d4504101eddca8180c13db4db57c62bf42e41680410dc5d88445f590000f9fa2c7e74fd0b25000300b0e57876250001af970000000501000b01000000a0006a88d8003ec34f00836daf93a80981030e190b12950012046647117122140b12060011049735408513006c646a4904010600c06c62a2600201b4305b020138a356a15430520410a0e24e93fc8e35bc37d4e75bf9c0fbe404085e8086949058e4c804106b92a335cf544b1c8009fa04f8bf26ad0410e0ecc07807abed861ac686cca2baf93b041023ab83c76f260000107d95c528097891')
eth_ipv4_sctp_sack  = unhexlify(b'a44bb2d9e3cef60babc3b51408004500022000cb00004084de5ab8de2670bbb6fe2f0ded0ded81819546ad72d90d03000010971c9c00000249f00000000000030124e57876260001af980000000501000b0100000114006a88db003ec35000836daf93280981030e190b12950012044304813588140b1206001104260270136391e06581dd480420254c6b490400d103306b262824060700118605010101a0196117a109060704000001002003a203020100a305a1030201006c81a6a181a30201a502010730819a8107912207134841f7830100b07d0500a179302a0201019002f12192031b921f940ca3eeb2df367f09bd3d6f33ee8009017396d4fe44810101820300640030220201039002f12192031b921f9404146bb4fc8009017396d4fe44810101820300640030270201089002f12192031b921f94092cd4737dd45da74e6e8009017396d4fe448101018203006400980100bf1f098607915461490007f9000300cce57876270001af990000000501000b01000000bc006a88db003ec35100836daf93880981030e190b12070012041895158224480b12060011043485864244118865818548041023536e4904d98e0cf66c77a175020102020107306da74da01504012b301030068301108401043006820110840104a015040121301030068301108401043006820110840104a11d0401923018300683011084010530068301208401043006820110840104ad1ca01a301530130a010202021b588007915531123384f8810100800101')
eth_ipv4_sctp_init  = unhexlify(b'0000000000000000000000000800450200440000400040843c327f0000017f0000012712271100000000ff16659a010000240ae91d2f0001a000000300034cc692eb000c00060005000080000004c0000004')
eth_ipv4_sctp_shut  = unhexlify(b'0000000000000000000000000800450200240003400040843c4f7f0000017f0000012712271129eadab86b6737600e000004')
#
eth_ipv6_mdns       = unhexlify(b'3333000000fbe86a64e8da5a86dd600eac14003511fffe80000000000000dac6d10f0a1eb230ff0200000000000000000000000000fb14e914e900356d93000000000002000000000000055f69707073045f746370056c6f63616c00000c0001045f697070c012000c0001')
eth_ipv6_icmp6      = unhexlify(b'3333ff00000054ab3a1bf16886dd6000000000203afffe80000000000000f667d256c7dda12cff0200000000000000000001ff0000008700c9250000000000000000000000000000000000000000010154ab3a1bf168')
eth_ipv6_hopopt     = unhexlify(b'333300000016ac88fd3a993886dd6000000000240001fe8000000000000010e8019ca4d1f03dff0200000000000000000000000000163a000100050200008f00c77c0000000104000000ff0200000000000000000000000000fb')
#
eth_frames = (
    eth_arp,
    eth_ipv4_udp_dns,
    eth_ipv4_tcp,
    eth_ipv4_tcp_http,
    eth_ipv4_sctp_data,
    eth_ipv4_sctp_sack,
    eth_ipv4_sctp_init,
    eth_ipv4_sctp_shut,
    eth_ipv6_mdns,
    eth_ipv6_icmp6,
    eth_ipv6_hopopt
    )


def test_ether(eth_frames=eth_frames):
    for f in eth_frames:
        pkt = EthernetPacket()
        pkt.from_bytes(f)
        v = pkt.get_val()
        pkt.reautomate()
        assert( pkt.get_val() == v )
        assert( pkt.to_bytes() == f )


def test_perf_ether(eth_frames=eth_frames):
    
    print('[+] decoding and re-encoding Ethernet / IP frames')
    Ta = timeit(test_ether, number=100)
    print('test_ether: {0:.4f}'.format(Ta))


if __name__ == '__main__':
    test_perf_ether()

