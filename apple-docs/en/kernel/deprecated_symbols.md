---
title: Deprecated Symbols
framework: Kernel
symbol_kind: symbol
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/kernel/deprecated_symbols
source_url: 'https://developer.apple.com/documentation/kernel/deprecated_symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/kernel/deprecated_symbols.json'
content_hash: 'sha256:a98982cc526675f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Kernel](../kernel.md)

# Deprecated Symbols

<sub>API Collection</sub>

Review unsupported symbols and their replacements.

## Topics

### Functions

- [IOFreeContiguous](1575295-iofreecontiguous.md) — Deprecated - use IOBufferMemoryDescriptor. Frees memory allocated with IOMallocContiguous. _(deprecated)_
- [IOMallocContiguous](1575289-iomalloccontiguous.md) — Deprecated - use IOBufferMemoryDescriptor. Allocates wired memory in the kernel map, with an alignment restriction and physically contiguous. _(deprecated)_
- [strcat](1579328-strcat.md) _(deprecated)_
- [strcpy](1579337-strcpy.md) _(deprecated)_
- [roundtol](1557345-roundtol.md) _(deprecated)_
- [rinttol](1557213-rinttol.md) _(deprecated)_
- [sysctl_register_fixed](1404259-sysctl_register_fixed.md) _(deprecated)_
- [mbuf_getcluster](1535695-mbuf_getcluster.md) _(deprecated)_
- [mbuf_adj](1535755-mbuf_adj.md) _(deprecated)_
- [mbuf_adjustlen](1535669-mbuf_adjustlen.md) _(deprecated)_
- [mbuf_align_32](1535692-mbuf_align_32.md) _(deprecated)_
- [mbuf_alloccluster](1535679-mbuf_alloccluster.md) _(deprecated)_
- [mbuf_allocpacket](1535712-mbuf_allocpacket.md) _(deprecated)_
- [mbuf_allocpacket_list](1535681-mbuf_allocpacket_list.md) _(deprecated)_
- [mbuf_attachcluster](1535766-mbuf_attachcluster.md) _(deprecated)_
- [mbuf_clear_csum_performed](1535748-mbuf_clear_csum_performed.md) _(deprecated)_
- [mbuf_clear_csum_requested](1535735-mbuf_clear_csum_requested.md) _(deprecated)_
- [mbuf_clear_vlan_tag](1535696-mbuf_clear_vlan_tag.md) _(deprecated)_
- [mbuf_concatenate](1535716-mbuf_concatenate.md) _(deprecated)_
- [mbuf_copy_pkthdr](1535645-mbuf_copy_pkthdr.md) _(deprecated)_
- [mbuf_copyback](1535623-mbuf_copyback.md) _(deprecated)_
- [mbuf_copydata](1535784-mbuf_copydata.md) _(deprecated)_
- [mbuf_copym](1535750-mbuf_copym.md) _(deprecated)_
- [mbuf_data](1535644-mbuf_data.md) _(deprecated)_
- [mbuf_data_to_physical](1535757-mbuf_data_to_physical.md) _(deprecated)_
- [mbuf_datastart](1535666-mbuf_datastart.md) _(deprecated)_
- [mbuf_dup](1535619-mbuf_dup.md) _(deprecated)_
- [mbuf_flags](1535785-mbuf_flags.md) _(deprecated)_
- [mbuf_free](1535684-mbuf_free.md) _(deprecated)_
- [mbuf_freecluster](1535768-mbuf_freecluster.md) _(deprecated)_
- [mbuf_freem](1535714-mbuf_freem.md) _(deprecated)_
- [mbuf_freem_list](1535787-mbuf_freem_list.md) _(deprecated)_
- [mbuf_get](1535751-mbuf_get.md) _(deprecated)_
- [mbuf_get_csum_requested](1535698-mbuf_get_csum_requested.md) _(deprecated)_
- [mbuf_get_mhlen](1535687-mbuf_get_mhlen.md) _(deprecated)_
- [mbuf_get_minclsize](1535737-mbuf_get_minclsize.md) _(deprecated)_
- [mbuf_get_mlen](1535699-mbuf_get_mlen.md) _(deprecated)_
- [mbuf_get_traffic_class](1535745-mbuf_get_traffic_class.md) _(deprecated)_
- [mbuf_get_tso_requested](1535781-mbuf_get_tso_requested.md) _(deprecated)_
- [mbuf_get_vlan_tag](1535803-mbuf_get_vlan_tag.md) _(deprecated)_
- [mbuf_gethdr](1535722-mbuf_gethdr.md) _(deprecated)_
- [mbuf_getpacket](1535724-mbuf_getpacket.md) _(deprecated)_
- [mbuf_inbound_modified](1535780-mbuf_inbound_modified.md) _(deprecated)_
- [mbuf_inet6_cksum](1535764-mbuf_inet6_cksum.md) _(deprecated)_
- [mbuf_inet_cksum](1535734-mbuf_inet_cksum.md) _(deprecated)_
- [mbuf_is_traffic_class_privileged](1535772-mbuf_is_traffic_class_privileged.md) _(deprecated)_
- [mbuf_leadingspace](1535767-mbuf_leadingspace.md) _(deprecated)_
- [mbuf_len](1535650-mbuf_len.md) _(deprecated)_
- [mbuf_maxlen](1535774-mbuf_maxlen.md) _(deprecated)_
- [mbuf_mclget](1535664-mbuf_mclget.md) _(deprecated)_
- [mbuf_mclhasreference](1535799-mbuf_mclhasreference.md) _(deprecated)_
- [mbuf_next](1535627-mbuf_next.md) _(deprecated)_
- [mbuf_nextpkt](1535633-mbuf_nextpkt.md) _(deprecated)_
- [mbuf_outbound_finalize](1535731-mbuf_outbound_finalize.md) _(deprecated)_
- [mbuf_pkthdr_adjustlen](1535682-mbuf_pkthdr_adjustlen.md) _(deprecated)_
- [mbuf_pkthdr_header](1535662-mbuf_pkthdr_header.md) _(deprecated)_
- [mbuf_pkthdr_len](1535742-mbuf_pkthdr_len.md) _(deprecated)_
- [mbuf_pkthdr_rcvif](1535717-mbuf_pkthdr_rcvif.md) _(deprecated)_
- [mbuf_pkthdr_setheader](1535690-mbuf_pkthdr_setheader.md) _(deprecated)_
- [mbuf_pkthdr_setlen](1535646-mbuf_pkthdr_setlen.md) _(deprecated)_
- [mbuf_pkthdr_setrcvif](1535657-mbuf_pkthdr_setrcvif.md) _(deprecated)_
- [mbuf_prepend](1535660-mbuf_prepend.md) _(deprecated)_
- [mbuf_pulldown](1535617-mbuf_pulldown.md) _(deprecated)_
- [mbuf_pullup](1535805-mbuf_pullup.md) _(deprecated)_
- [mbuf_set_csum_performed](1535789-mbuf_set_csum_performed.md) _(deprecated)_
- [mbuf_set_traffic_class](1535642-mbuf_set_traffic_class.md) _(deprecated)_
- [mbuf_set_vlan_tag](1535628-mbuf_set_vlan_tag.md) _(deprecated)_
- [mbuf_setdata](1535656-mbuf_setdata.md) _(deprecated)_
- [mbuf_setflags](1535683-mbuf_setflags.md) _(deprecated)_
- [mbuf_setflags_mask](1535686-mbuf_setflags_mask.md) _(deprecated)_
- [mbuf_setlen](1535776-mbuf_setlen.md) _(deprecated)_
- [mbuf_setnext](1535672-mbuf_setnext.md) _(deprecated)_
- [mbuf_setnextpkt](1535738-mbuf_setnextpkt.md) _(deprecated)_
- [mbuf_settype](1535744-mbuf_settype.md) _(deprecated)_
- [mbuf_split](1535762-mbuf_split.md) _(deprecated)_
- [mbuf_stats](1535710-mbuf_stats.md) _(deprecated)_
- [mbuf_tag_allocate](1535756-mbuf_tag_allocate.md) _(deprecated)_
- [mbuf_tag_find](1535711-mbuf_tag_find.md) _(deprecated)_
- [mbuf_tag_free](1535728-mbuf_tag_free.md) _(deprecated)_
- [mbuf_tag_id_find](1535795-mbuf_tag_id_find.md) _(deprecated)_
- [mbuf_trailingspace](1535759-mbuf_trailingspace.md) _(deprecated)_
- [mbuf_type](1535806-mbuf_type.md) _(deprecated)_
- [kcdata_iter_unsafe](1644335-kcdata_iter_unsafe.md) _(deprecated)_
- [KUNCUserNotificationDisplayAlert](1434506-kuncusernotificationdisplayalert.md) _(deprecated)_
- [KUNCUserNotificationDisplayFromBundle](1434508-kuncusernotificationdisplayfromb.md) _(deprecated)_
- [KUNCUserNotificationDisplayNotice](1434502-kuncusernotificationdisplaynotic.md) _(deprecated)_
- [KUNCExecute](1434510-kuncexecute.md) _(deprecated)_
- [KUNCGetNotificationID](1434512-kuncgetnotificationid.md) _(deprecated)_
- [finite](1557318-finite.md) _(deprecated)_
- [IOExitThread](1575306-ioexitthread.md) — Deprecated function - use thread_terminate(). Terminate execution of current thread. _(deprecated)_
- [IOCreateThread](1575312-iocreatethread.md) — Deprecated function - use kernel_thread_start(). Create a kernel thread. _(deprecated)_
- [IOSetProcessorCacheMode](1575314-iosetprocessorcachemode.md) _(deprecated)_

### Network Kernel Extensions

- [sock_accept](1396149-sock_accept.md) _(deprecated)_
- [sock_bind](1396145-sock_bind.md) _(deprecated)_
- [sock_close](1396134-sock_close.md) _(deprecated)_
- [sock_connect](1396120-sock_connect.md) _(deprecated)_
- [sock_getpeername](1396137-sock_getpeername.md) _(deprecated)_
- [sock_getsockname](1396141-sock_getsockname.md) _(deprecated)_
- [sock_getsockopt](1396136-sock_getsockopt.md) _(deprecated)_
- [sock_gettype](1396147-sock_gettype.md) _(deprecated)_
- [sock_inject_data_in](1433192-sock_inject_data_in.md) _(deprecated)_
- [sock_inject_data_out](1433162-sock_inject_data_out.md) _(deprecated)_
- [sock_ioctl](1396118-sock_ioctl.md) _(deprecated)_
- [sock_isconnected](1396130-sock_isconnected.md) _(deprecated)_
- [sock_isnonblocking](1396116-sock_isnonblocking.md) _(deprecated)_
- [sock_listen](1396139-sock_listen.md) _(deprecated)_
- [sock_receive](1396126-sock_receive.md) _(deprecated)_
- [sock_receivembuf](1396114-sock_receivembuf.md) _(deprecated)_
- [sock_send](1396143-sock_send.md) _(deprecated)_
- [sock_sendmbuf](1396128-sock_sendmbuf.md) _(deprecated)_
- [sock_setpriv](1396124-sock_setpriv.md) _(deprecated)_
- [sock_setsockopt](1396148-sock_setsockopt.md) _(deprecated)_
- [sock_shutdown](1396150-sock_shutdown.md) _(deprecated)_
- [sock_socket](1396122-sock_socket.md) _(deprecated)_
- [sockopt_copyin](1433166-sockopt_copyin.md) _(deprecated)_
- [sockopt_copyout](1433176-sockopt_copyout.md) _(deprecated)_
- [sockopt_direction](1433253-sockopt_direction.md) _(deprecated)_
- [sockopt_level](1433193-sockopt_level.md) _(deprecated)_
- [sockopt_name](1433249-sockopt_name.md) _(deprecated)_
- [sockopt_valsize](1433272-sockopt_valsize.md) _(deprecated)_
- [ifaddr_address](1525073-ifaddr_address.md) _(deprecated)_
- [ifaddr_address_family](1524915-ifaddr_address_family.md) _(deprecated)_
- [ifaddr_dstaddress](1525058-ifaddr_dstaddress.md) _(deprecated)_
- [ifaddr_findbestforaddr](1525009-ifaddr_findbestforaddr.md) _(deprecated)_
- [ifaddr_ifnet](1524949-ifaddr_ifnet.md) _(deprecated)_
- [ifaddr_netmask](1525132-ifaddr_netmask.md) _(deprecated)_
- [ifaddr_reference](1525060-ifaddr_reference.md) _(deprecated)_
- [ifaddr_release](1524928-ifaddr_release.md) _(deprecated)_
- [ifaddr_withaddr](1524859-ifaddr_withaddr.md) _(deprecated)_
- [ifaddr_withdstaddr](1525107-ifaddr_withdstaddr.md) _(deprecated)_
- [ifaddr_withnet](1524842-ifaddr_withnet.md) _(deprecated)_
- [ifaddr_withroute](1524963-ifaddr_withroute.md) _(deprecated)_
- [iflt_attach](1589956-iflt_attach.md) _(deprecated)_
- [iflt_detach](1589950-iflt_detach.md) _(deprecated)_
- [ifmaddr_address](1524853-ifmaddr_address.md) _(deprecated)_
- [ifmaddr_ifnet](1525101-ifmaddr_ifnet.md) _(deprecated)_
- [ifmaddr_lladdress](1525091-ifmaddr_lladdress.md) _(deprecated)_
- [ifmaddr_reference](1524890-ifmaddr_reference.md) _(deprecated)_
- [ifmaddr_release](1525024-ifmaddr_release.md) _(deprecated)_
- [ifnet_add_multicast](1524976-ifnet_add_multicast.md) _(deprecated)_
- [ifnet_addrlen](1524855-ifnet_addrlen.md) _(deprecated)_
- [ifnet_allocate](1525028-ifnet_allocate.md) _(deprecated)_
- [ifnet_attach](1524922-ifnet_attach.md) _(deprecated)_
- [ifnet_attach_protocol](1525004-ifnet_attach_protocol.md) _(deprecated)_
- [ifnet_attach_protocol_v2](1525131-ifnet_attach_protocol_v2.md) _(deprecated)_
- [ifnet_baudrate](1524866-ifnet_baudrate.md) _(deprecated)_
- [ifnet_capabilities_enabled](1525016-ifnet_capabilities_enabled.md) _(deprecated)_
- [ifnet_capabilities_supported](1524931-ifnet_capabilities_supported.md) _(deprecated)_
- [ifnet_detach](1524903-ifnet_detach.md) _(deprecated)_
- [ifnet_detach_protocol](1525007-ifnet_detach_protocol.md) _(deprecated)_
- [ifnet_event](1524986-ifnet_event.md) _(deprecated)_
- [ifnet_family](1524921-ifnet_family.md) _(deprecated)_
- [ifnet_find_by_name](1525072-ifnet_find_by_name.md) _(deprecated)_
- [ifnet_flags](1525111-ifnet_flags.md) _(deprecated)_
- [ifnet_free_address_list](1524991-ifnet_free_address_list.md) _(deprecated)_
- [ifnet_free_multicast_list](1524898-ifnet_free_multicast_list.md) _(deprecated)_
- [ifnet_get_address_list](1525146-ifnet_get_address_list.md) _(deprecated)_
- [ifnet_get_address_list_family](1525142-ifnet_get_address_list_family.md) _(deprecated)_
- [ifnet_get_link_mib_data](1524988-ifnet_get_link_mib_data.md) _(deprecated)_
- [ifnet_get_link_mib_data_length](1524864-ifnet_get_link_mib_data_length.md) _(deprecated)_
- [ifnet_get_multicast_list](1525020-ifnet_get_multicast_list.md) _(deprecated)_
- [ifnet_get_tso_mtu](1524965-ifnet_get_tso_mtu.md) _(deprecated)_
- [ifnet_get_wake_flags](1524907-ifnet_get_wake_flags.md) _(deprecated)_
- [ifnet_hdrlen](1524895-ifnet_hdrlen.md) _(deprecated)_
- [ifnet_index](1525041-ifnet_index.md) _(deprecated)_
- [ifnet_input](1525087-ifnet_input.md) _(deprecated)_
- [ifnet_interface_family_find](1524844-ifnet_interface_family_find.md) _(deprecated)_
- [ifnet_ioctl](1525082-ifnet_ioctl.md) _(deprecated)_
- [ifnet_lastchange](1525140-ifnet_lastchange.md) _(deprecated)_
- [ifnet_list_free](1524868-ifnet_list_free.md) _(deprecated)_
- [ifnet_list_get](1524913-ifnet_list_get.md) _(deprecated)_
- [ifnet_lladdr_copy_bytes](1525069-ifnet_lladdr_copy_bytes.md) _(deprecated)_
- [ifnet_llbroadcast_copy_bytes](1525030-ifnet_llbroadcast_copy_bytes.md) _(deprecated)_
- [ifnet_metric](1524964-ifnet_metric.md) _(deprecated)_
- [ifnet_mtu](1524959-ifnet_mtu.md) _(deprecated)_
- [ifnet_name](1524885-ifnet_name.md) _(deprecated)_
- [ifnet_offload](1524854-ifnet_offload.md) _(deprecated)_
- [ifnet_output](1525046-ifnet_output.md) _(deprecated)_
- [ifnet_output_raw](1525049-ifnet_output_raw.md) _(deprecated)_
- [ifnet_reference](1524857-ifnet_reference.md) _(deprecated)_
- [ifnet_release](1525052-ifnet_release.md) _(deprecated)_
- [ifnet_remove_multicast](1524982-ifnet_remove_multicast.md) _(deprecated)_
- [ifnet_resolve_multicast](1525080-ifnet_resolve_multicast.md) _(deprecated)_
- [ifnet_set_addrlen](1524861-ifnet_set_addrlen.md) _(deprecated)_
- [ifnet_set_baudrate](1525090-ifnet_set_baudrate.md) _(deprecated)_
- [ifnet_set_capabilities_enabled](1524938-ifnet_set_capabilities_enabled.md) _(deprecated)_
- [ifnet_set_capabilities_supported](1525144-ifnet_set_capabilities_supported.md) _(deprecated)_
- [ifnet_set_flags](1524996-ifnet_set_flags.md) _(deprecated)_
- [ifnet_set_hdrlen](1525097-ifnet_set_hdrlen.md) _(deprecated)_
- [ifnet_set_link_mib_data](1525120-ifnet_set_link_mib_data.md) _(deprecated)_
- [ifnet_set_lladdr](1524891-ifnet_set_lladdr.md) _(deprecated)_
- [ifnet_set_metric](1524932-ifnet_set_metric.md) _(deprecated)_
- [ifnet_set_mtu](1524919-ifnet_set_mtu.md) _(deprecated)_
- [ifnet_set_offload](1524961-ifnet_set_offload.md) _(deprecated)_
- [ifnet_set_promiscuous](1524973-ifnet_set_promiscuous.md) _(deprecated)_
- [ifnet_set_stat](1524994-ifnet_set_stat.md) _(deprecated)_
- [ifnet_set_tso_mtu](1525098-ifnet_set_tso_mtu.md) _(deprecated)_
- [ifnet_set_wake_flags](1525070-ifnet_set_wake_flags.md) _(deprecated)_
- [ifnet_softc](1524952-ifnet_softc.md) _(deprecated)_
- [ifnet_stat](1525068-ifnet_stat.md) _(deprecated)_
- [ifnet_stat_increment](1525065-ifnet_stat_increment.md) _(deprecated)_
- [ifnet_stat_increment_in](1525002-ifnet_stat_increment_in.md) _(deprecated)_
- [ifnet_stat_increment_out](1525085-ifnet_stat_increment_out.md) _(deprecated)_
- [ifnet_touch_lastchange](1524957-ifnet_touch_lastchange.md) _(deprecated)_
- [ifnet_type](1524954-ifnet_type.md) _(deprecated)_
- [ifnet_unit](1525055-ifnet_unit.md) _(deprecated)_

### IOKit

- [IOUSBDevice](iousbdevice.md) — An input/output service object that represents a device on the USB bus. _(deprecated)_
- [IOUSBInterface](iousbinterface.md) — An object that represents an interface of a device on the USB bus. _(deprecated)_
- [IOOFPathMatching](1575304-ioofpathmatching.md) _(deprecated)_
- [IOUSBHostInterface](iousbhostinterface.md) _(deprecated)_
- [IOUSBHostDevice](iousbhostdevice.md) _(deprecated)_
- [IOUSBHostPipe](iousbhostpipe.md) _(deprecated)_
- [IOUSBHostIOSource](iousbhostiosource.md) _(deprecated)_
- [IOUSBHostStream](iousbhoststream.md) _(deprecated)_
- [IOHIDEventDriver](iohideventdriver.md) _(deprecated)_
- [IOHIDEventService](iohideventservice.md) — IOService represents an device or OS service in IOKit and DriverKit. _(deprecated)_
- [IOHIDInterface](iohidinterface.md) — IOService represents an device or OS service in IOKit and DriverKit. _(deprecated)_
- [IOHIDSystem](iohidsystem.md) _(deprecated)_
- [IOHIKeyboardMapper](iohikeyboardmapper.md) _(deprecated)_
- [IOHIKeyboard](iohikeyboard.md) _(deprecated)_
- [IOHIPointing](iohipointing.md) _(deprecated)_
- [IOHIDevice](iohidevice.md) _(deprecated)_
- [IOHIDElement](iohidelement.md) _(deprecated)_
- [IOHIDWorkLoop](iohidworkloop.md) _(deprecated)_
- [IOEthernetInterface](ioethernetinterface.md) — The Ethernet interface object. _(deprecated)_
- [IOEthernetController](ioethernetcontroller.md) — Abstract superclass for Ethernet controllers. _(deprecated)_
