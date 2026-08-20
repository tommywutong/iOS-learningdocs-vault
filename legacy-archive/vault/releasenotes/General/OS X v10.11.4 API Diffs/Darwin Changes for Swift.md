---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/Darwin.html
archived_at: '2026-07-18T02:53:51.056105Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# Darwin Changes for Swift

### Darwin

Removed P_RESV10Removed VQ_FLAG1000Added eproc [struct]Added eproc.e_flagAdded eproc.e_jobcAdded eproc.e_loginAdded eproc.e_paddrAdded eproc.e_pcredAdded eproc.e_pgidAdded eproc.e_ppidAdded eproc.e_sessAdded eproc.e_spareAdded eproc.e_tdevAdded eproc.e_tpgidAdded eproc.e_tsessAdded eproc.e_ucredAdded eproc.e_vmAdded eproc.e_wmesgAdded eproc.e_xccountAdded eproc.e_xrssizeAdded eproc.e_xsizeAdded eproc.e_xswrssAdded eproc.init()Added eproc.init(e_paddr: COpaquePointer, e_sess: COpaquePointer, e_pcred: _pcred, e_ucred: _ucred, e_vm: vmspace, e_ppid: pid_t, e_pgid: pid_t, e_jobc: Int16, e_tdev: dev_t, e_tpgid: pid_t, e_tsess: COpaquePointer, e_wmesg: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), e_xsize: segsz_t, e_xrssize: Int16, e_xccount: Int16, e_xswrss: Int16, e_flag: Int32, e_login: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), e_spare: (Int32, Int32, Int32, Int32))Added extern_proc.p_unAdded FndrDirInfo.frLocationAdded FndrDirInfo.frRectAdded FndrDirInfo.init(frRect: FndrDirInfo.__Unnamed_struct_frRect, frFlags: UInt16, frLocation: FndrDirInfo.__Unnamed_struct_frLocation, opaque: Int16)Added FndrFileInfo.fdLocationAdded FndrFileInfo.init(fdType: UInt32, fdCreator: UInt32, fdFlags: UInt16, fdLocation: FndrFileInfo.__Unnamed_struct_fdLocation, opaque: Int16)Added HFSPlusBSDInfo.init(ownerID: UInt32, groupID: UInt32, adminFlags: UInt8, ownerFlags: UInt8, fileMode: UInt16, special: HFSPlusBSDInfo.__Unnamed_union_special)Added HFSPlusBSDInfo.specialAdded ifconf.ifc_ifcuAdded ifconf.init(ifc_len: Int32, ifc_ifcu: ifconf.__Unnamed_union_ifc_ifcu)Added ifkpi.ifk_dataAdded ifkpi.init(ifk_module_id: UInt32, ifk_type: UInt32, ifk_data: ifkpi.__Unnamed_union_ifk_data)Added ifreq.ifr_ifruAdded ifreq.init(ifr_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifr_ifru: ifreq.__Unnamed_union_ifr_ifru)Added in6_addr.init(__u6_addr: in6_addr.__Unnamed_union___u6_addr)Added in_sockinfo.init(insi_fport: Int32, insi_lport: Int32, insi_gencnt: UInt64, insi_flags: UInt32, insi_flow: UInt32, insi_vflag: UInt8, insi_ip_ttl: UInt8, rfu_1: UInt32, insi_faddr: in_sockinfo.__Unnamed_union_insi_faddr, insi_laddr: in_sockinfo.__Unnamed_union_insi_laddr, insi_v4: in_sockinfo.__Unnamed_struct_insi_v4, insi_v6: in_sockinfo.__Unnamed_struct_insi_v6)Added in_sockinfo.insi_faddrAdded in_sockinfo.insi_laddrAdded in_sockinfo.insi_v4Added in_sockinfo.insi_v6Added posix_cred [struct]Added posix_cred.cr_flagsAdded posix_cred.cr_gmuidAdded posix_cred.cr_groupsAdded posix_cred.cr_ngroupsAdded posix_cred.cr_rgidAdded posix_cred.cr_ruidAdded posix_cred.cr_svgidAdded posix_cred.cr_svuidAdded posix_cred.cr_uidAdded posix_cred.init()Added posix_cred.init(cr_uid: uid_t, cr_ruid: uid_t, cr_svuid: uid_t, cr_ngroups: Int16, cr_groups: (gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t), cr_rgid: gid_t, cr_svgid: gid_t, cr_gmuid: uid_t, cr_flags: Int32)Added socket_info.init(soi_stat: vinfo_stat, soi_so: UInt64, soi_pcb: UInt64, soi_type: Int32, soi_protocol: Int32, soi_family: Int32, soi_options: Int16, soi_linger: Int16, soi_state: Int16, soi_qlen: Int16, soi_incqlen: Int16, soi_qlimit: Int16, soi_timeo: Int16, soi_error: u_short, soi_oobmark: UInt32, soi_rcv: sockbuf_info, soi_snd: sockbuf_info, soi_kind: Int32, rfu_1: UInt32, soi_proto: socket_info.__Unnamed_union_soi_proto)Added socket_info.soi_protoAdded tokenstr.init(id: u_char, data: UnsafeMutablePointer<u_char>, len: Int, tt: tokenstr.__Unnamed_union_tt)Added tokenstr.ttAdded ucred.cr_linkAdded ucred.init(cr_link: ucred.__Unnamed_struct_cr_link, cr_ref: u_long, cr_posix: posix_cred, cr_label: COpaquePointer, cr_audit: au_session)Added un_sockinfo.init(unsi_conn_so: UInt64, unsi_conn_pcb: UInt64, unsi_addr: un_sockinfo.__Unnamed_union_unsi_addr, unsi_caddr: un_sockinfo.__Unnamed_union_unsi_caddr)Added un_sockinfo.unsi_addrAdded un_sockinfo.unsi_caddrAdded uprof [struct]Added uprof.init()Added uprof.init(pr_next: UnsafeMutablePointer<uprof>, pr_base: caddr_t, pr_size: UInt32, pr_off: UInt32, pr_scale: UInt32, pr_addr: UInt32, pr_ticks: UInt32)Added uprof.pr_addrAdded uprof.pr_baseAdded uprof.pr_nextAdded uprof.pr_offAdded uprof.pr_scaleAdded uprof.pr_sizeAdded uprof.pr_ticksAdded wait.init(w_S: wait.__Unnamed_struct_w_S)Added wait.init(w_T: wait.__Unnamed_struct_w_T)Added wait.w_SAdded wait.w_TAdded x86_avx_state.init(ash: x86_state_hdr_t, ufs: x86_avx_state.__Unnamed_union_ufs)Added x86_avx_state.ufsAdded x86_debug_state.init(dsh: x86_state_hdr_t, uds: x86_debug_state.__Unnamed_union_uds)Added x86_debug_state.udsAdded x86_exception_state.init(esh: x86_state_hdr_t, ues: x86_exception_state.__Unnamed_union_ues)Added x86_exception_state.uesAdded x86_float_state.init(fsh: x86_state_hdr_t, ufs: x86_float_state.__Unnamed_union_ufs)Added x86_float_state.ufsAdded x86_thread_state.init(tsh: x86_state_hdr_t, uts: x86_thread_state.__Unnamed_union_uts)Added x86_thread_state.utsAdded arc4random() -> UInt32Added arc4random_uniform(_: UInt32) -> UInt32Added close(_: Int32) -> Int32Added fcntl(_: CInt, _: CInt) -> CIntAdded fcntl(_: CInt, _: CInt, _: CInt) -> CIntAdded fcntl(_: CInt, _: CInt, _: UnsafeMutablePointer<Void>) -> CIntAdded free(_: UnsafeMutablePointer<Void>)Added host_check_multiuser_mode(_: host_t, _: UnsafeMutablePointer<UInt32>) -> kern_return_tAdded host_get_multiuser_config_flags(_: host_t, _: UnsafeMutablePointer<UInt32>) -> kern_return_tAdded host_set_multiuser_config_flags(_: host_priv_t, _: UInt32) -> kern_return_tAdded MAC_OS_X_VERSION_10_11_3Added MAC_OS_X_VERSION_10_11_4Added mach_voucher_attr_value_flags_tAdded memcmp(_: UnsafePointer<Void>, _: UnsafePointer<Void>, _: Int) -> Int32Added P_ADOPTPERSONAAdded putchar(_: Int32) -> Int32Added read(_: Int32, _: UnsafeMutablePointer<Void>, _: Int) -> IntAdded strcmp(_: UnsafePointer<Int8>, _: UnsafePointer<Int8>) -> Int32Added strcpy(_: UnsafeMutablePointer<Int8>, _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8>Added strlen(_: UnsafePointer<Int8>) -> UIntAdded strtod(_: UnsafePointer<Int8>, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> DoubleAdded strtof(_: UnsafePointer<Int8>, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> FloatAdded SYS_personaAdded SYS_usrctlAdded usrctl(_: UInt32) -> Int32Added VQ_QUOTAAdded write(_: Int32, _: UnsafePointer<Void>, _: Int) -> IntModified extern_proc [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct extern_proc {     var p_vmspace: UnsafeMutablePointer<vmspace>     var p_sigacts: COpaquePointer     var p_flag: Int32     var p_stat: Int8     var p_pid: pid_t     var p_oppid: pid_t     var p_dupfd: Int32     var user_stack: caddr_t     var exit_thread: UnsafeMutablePointer<Void>     var p_debugger: Int32     var sigwait: boolean_t     var p_estcpu: u_int     var p_cpticks: Int32     var p_pctcpu: fixpt_t     var p_wchan: UnsafeMutablePointer<Void>     var p_wmesg: UnsafeMutablePointer<Int8>     var p_swtime: u_int     var p_slptime: u_int     var p_realtimer: itimerval     var p_rtime: timeval     var p_uticks: u_quad_t     var p_sticks: u_quad_t     var p_iticks: u_quad_t     var p_traceflag: Int32     var p_tracep: COpaquePointer     var p_siglist: Int32     var p_textvp: COpaquePointer     var p_holdcnt: Int32     var p_sigmask: sigset_t     var p_sigignore: sigset_t     var p_sigcatch: sigset_t     var p_priority: u_char     var p_usrpri: u_char     var p_nice: Int8     var p_comm: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var p_pgrp: COpaquePointer     var p_addr: UnsafeMutablePointer<user>     var p_xstat: u_short     var p_acflag: u_short     var p_ru: UnsafeMutablePointer<rusage>     init() } ``` |
| To | ``` struct extern_proc {     struct __Unnamed_union_p_un {         struct __Unnamed_struct_p_st1 {             var __p_forw: COpaquePointer             var __p_back: COpaquePointer             init()             init(__p_forw __p_forw: COpaquePointer, __p_back __p_back: COpaquePointer)         }         var p_st1: extern_proc.__Unnamed_union_p_un.__Unnamed_struct_p_st1         var __p_starttime: timeval         init(p_st1 p_st1: extern_proc.__Unnamed_union_p_un.__Unnamed_struct_p_st1)         init(__p_starttime __p_starttime: timeval)         init()     }     var p_un: extern_proc.__Unnamed_union_p_un     var p_vmspace: UnsafeMutablePointer<vmspace>     var p_sigacts: COpaquePointer     var p_flag: Int32     var p_stat: Int8     var p_pid: pid_t     var p_oppid: pid_t     var p_dupfd: Int32     var user_stack: caddr_t     var exit_thread: UnsafeMutablePointer<Void>     var p_debugger: Int32     var sigwait: boolean_t     var p_estcpu: u_int     var p_cpticks: Int32     var p_pctcpu: fixpt_t     var p_wchan: UnsafeMutablePointer<Void>     var p_wmesg: UnsafeMutablePointer<Int8>     var p_swtime: u_int     var p_slptime: u_int     var p_realtimer: itimerval     var p_rtime: timeval     var p_uticks: u_quad_t     var p_sticks: u_quad_t     var p_iticks: u_quad_t     var p_traceflag: Int32     var p_tracep: COpaquePointer     var p_siglist: Int32     var p_textvp: COpaquePointer     var p_holdcnt: Int32     var p_sigmask: sigset_t     var p_sigignore: sigset_t     var p_sigcatch: sigset_t     var p_priority: u_char     var p_usrpri: u_char     var p_nice: Int8     var p_comm: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var p_pgrp: COpaquePointer     var p_addr: UnsafeMutablePointer<user>     var p_xstat: u_short     var p_acflag: u_short     var p_ru: UnsafeMutablePointer<rusage>     init() } ``` |

Modified FndrDirInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FndrDirInfo {     var frFlags: UInt16     var opaque: Int16     init() } ``` |
| To | ``` struct FndrDirInfo {     struct __Unnamed_struct_frRect {         var top: Int16         var left: Int16         var bottom: Int16         var right: Int16         init()         init(top top: Int16, left left: Int16, bottom bottom: Int16, right right: Int16)     }     struct __Unnamed_struct_frLocation {         var v: UInt16         var h: UInt16         init()         init(v v: UInt16, h h: UInt16)     }     var frRect: FndrDirInfo.__Unnamed_struct_frRect     var frFlags: UInt16     var frLocation: FndrDirInfo.__Unnamed_struct_frLocation     var opaque: Int16     init()     init(frRect frRect: FndrDirInfo.__Unnamed_struct_frRect, frFlags frFlags: UInt16, frLocation frLocation: FndrDirInfo.__Unnamed_struct_frLocation, opaque opaque: Int16) } ``` |

Modified FndrFileInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FndrFileInfo {     var fdType: UInt32     var fdCreator: UInt32     var fdFlags: UInt16     var opaque: Int16     init() } ``` |
| To | ``` struct FndrFileInfo {     struct __Unnamed_struct_fdLocation {         var v: Int16         var h: Int16         init()         init(v v: Int16, h h: Int16)     }     var fdType: UInt32     var fdCreator: UInt32     var fdFlags: UInt16     var fdLocation: FndrFileInfo.__Unnamed_struct_fdLocation     var opaque: Int16     init()     init(fdType fdType: UInt32, fdCreator fdCreator: UInt32, fdFlags fdFlags: UInt16, fdLocation fdLocation: FndrFileInfo.__Unnamed_struct_fdLocation, opaque opaque: Int16) } ``` |

Modified HFSPlusBSDInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HFSPlusBSDInfo {     var ownerID: UInt32     var groupID: UInt32     var adminFlags: UInt8     var ownerFlags: UInt8     var fileMode: UInt16     init() } ``` |
| To | ``` struct HFSPlusBSDInfo {     struct __Unnamed_union_special {         var iNodeNum: UInt32         var linkCount: UInt32         var rawDevice: UInt32         init(iNodeNum iNodeNum: UInt32)         init(linkCount linkCount: UInt32)         init(rawDevice rawDevice: UInt32)         init()     }     var ownerID: UInt32     var groupID: UInt32     var adminFlags: UInt8     var ownerFlags: UInt8     var fileMode: UInt16     var special: HFSPlusBSDInfo.__Unnamed_union_special     init()     init(ownerID ownerID: UInt32, groupID groupID: UInt32, adminFlags adminFlags: UInt8, ownerFlags ownerFlags: UInt8, fileMode fileMode: UInt16, special special: HFSPlusBSDInfo.__Unnamed_union_special) } ``` |

Modified ifconf [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifconf {     var ifc_len: Int32     init() } ``` |
| To | ``` struct ifconf {     struct __Unnamed_union_ifc_ifcu {         var ifcu_buf: caddr_t         var ifcu_req: UnsafeMutablePointer<ifreq>         init(ifcu_buf ifcu_buf: caddr_t)         init(ifcu_req ifcu_req: UnsafeMutablePointer<ifreq>)         init()     }     var ifc_len: Int32     var ifc_ifcu: ifconf.__Unnamed_union_ifc_ifcu     init()     init(ifc_len ifc_len: Int32, ifc_ifcu ifc_ifcu: ifconf.__Unnamed_union_ifc_ifcu) } ``` |

Modified ifkpi [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifkpi {     var ifk_module_id: UInt32     var ifk_type: UInt32     init() } ``` |
| To | ``` struct ifkpi {     struct __Unnamed_union_ifk_data {         var ifk_ptr: UnsafeMutablePointer<Void>         var ifk_value: Int32         init(ifk_ptr ifk_ptr: UnsafeMutablePointer<Void>)         init(ifk_value ifk_value: Int32)         init()     }     var ifk_module_id: UInt32     var ifk_type: UInt32     var ifk_data: ifkpi.__Unnamed_union_ifk_data     init()     init(ifk_module_id ifk_module_id: UInt32, ifk_type ifk_type: UInt32, ifk_data ifk_data: ifkpi.__Unnamed_union_ifk_data) } ``` |

Modified ifreq [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifreq {     var ifr_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init() } ``` |
| To | ``` struct ifreq {     struct __Unnamed_union_ifr_ifru {         var ifru_addr: sockaddr         var ifru_dstaddr: sockaddr         var ifru_broadaddr: sockaddr         var ifru_flags: Int16         var ifru_metric: Int32         var ifru_mtu: Int32         var ifru_phys: Int32         var ifru_media: Int32         var ifru_intval: Int32         var ifru_data: caddr_t         var ifru_devmtu: ifdevmtu         var ifru_kpi: ifkpi         var ifru_wake_flags: UInt32         var ifru_route_refcnt: UInt32         var ifru_cap: (Int32, Int32)         init(ifru_addr ifru_addr: sockaddr)         init(ifru_dstaddr ifru_dstaddr: sockaddr)         init(ifru_broadaddr ifru_broadaddr: sockaddr)         init(ifru_flags ifru_flags: Int16)         init(ifru_metric ifru_metric: Int32)         init(ifru_mtu ifru_mtu: Int32)         init(ifru_phys ifru_phys: Int32)         init(ifru_media ifru_media: Int32)         init(ifru_intval ifru_intval: Int32)         init(ifru_data ifru_data: caddr_t)         init(ifru_devmtu ifru_devmtu: ifdevmtu)         init(ifru_kpi ifru_kpi: ifkpi)         init(ifru_wake_flags ifru_wake_flags: UInt32)         init(ifru_route_refcnt ifru_route_refcnt: UInt32)         init(ifru_cap ifru_cap: (Int32, Int32))         init()     }     var ifr_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ifr_ifru: ifreq.__Unnamed_union_ifr_ifru     init()     init(ifr_name ifr_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifr_ifru ifr_ifru: ifreq.__Unnamed_union_ifr_ifru) } ``` |

Modified in6_addr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct in6_addr {     init() } ``` |
| To | ``` struct in6_addr {     struct __Unnamed_union___u6_addr {         var __u6_addr8: (__uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t)         var __u6_addr16: (__uint16_t, __uint16_t, __uint16_t, __uint16_t, __uint16_t, __uint16_t, __uint16_t, __uint16_t)         var __u6_addr32: (__uint32_t, __uint32_t, __uint32_t, __uint32_t)         init(__u6_addr8 __u6_addr8: (__uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t, __uint8_t))         init(__u6_addr16 __u6_addr16: (__uint16_t, __uint16_t, __uint16_t, __uint16_t, __uint16_t, __uint16_t, __uint16_t, __uint16_t))         init(__u6_addr32 __u6_addr32: (__uint32_t, __uint32_t, __uint32_t, __uint32_t))         init()     }     var __u6_addr: in6_addr.__Unnamed_union___u6_addr     init()     init(__u6_addr __u6_addr: in6_addr.__Unnamed_union___u6_addr) } ``` |

Modified in_sockinfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct in_sockinfo {     var insi_fport: Int32     var insi_lport: Int32     var insi_gencnt: UInt64     var insi_flags: UInt32     var insi_flow: UInt32     var insi_vflag: UInt8     var insi_ip_ttl: UInt8     var rfu_1: UInt32     init() } ``` |
| To | ``` struct in_sockinfo {     struct __Unnamed_union_insi_faddr {         var ina_46: in4in6_addr         var ina_6: in6_addr         init(ina_46 ina_46: in4in6_addr)         init(ina_6 ina_6: in6_addr)         init()     }     struct __Unnamed_union_insi_laddr {         var ina_46: in4in6_addr         var ina_6: in6_addr         init(ina_46 ina_46: in4in6_addr)         init(ina_6 ina_6: in6_addr)         init()     }     struct __Unnamed_struct_insi_v4 {         var in4_tos: u_char         init()         init(in4_tos in4_tos: u_char)     }     struct __Unnamed_struct_insi_v6 {         var in6_hlim: UInt8         var in6_cksum: Int32         var in6_ifindex: u_short         var in6_hops: Int16         init()         init(in6_hlim in6_hlim: UInt8, in6_cksum in6_cksum: Int32, in6_ifindex in6_ifindex: u_short, in6_hops in6_hops: Int16)     }     var insi_fport: Int32     var insi_lport: Int32     var insi_gencnt: UInt64     var insi_flags: UInt32     var insi_flow: UInt32     var insi_vflag: UInt8     var insi_ip_ttl: UInt8     var rfu_1: UInt32     var insi_faddr: in_sockinfo.__Unnamed_union_insi_faddr     var insi_laddr: in_sockinfo.__Unnamed_union_insi_laddr     var insi_v4: in_sockinfo.__Unnamed_struct_insi_v4     var insi_v6: in_sockinfo.__Unnamed_struct_insi_v6     init()     init(insi_fport insi_fport: Int32, insi_lport insi_lport: Int32, insi_gencnt insi_gencnt: UInt64, insi_flags insi_flags: UInt32, insi_flow insi_flow: UInt32, insi_vflag insi_vflag: UInt8, insi_ip_ttl insi_ip_ttl: UInt8, rfu_1 rfu_1: UInt32, insi_faddr insi_faddr: in_sockinfo.__Unnamed_union_insi_faddr, insi_laddr insi_laddr: in_sockinfo.__Unnamed_union_insi_laddr, insi_v4 insi_v4: in_sockinfo.__Unnamed_struct_insi_v4, insi_v6 insi_v6: in_sockinfo.__Unnamed_struct_insi_v6) } ``` |

Modified pipebuf [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct pipebuf {     var cnt: u_int     var `in`: u_int     var out: u_int     var size: u_int     var buffer: caddr_t     init()     init(cnt cnt: u_int, `in` `in`: u_int, out out: u_int, size size: u_int, buffer buffer: caddr_t) } ``` |
| To | ``` struct pipebuf {     var cnt: u_int     var `in`: u_int     var out: u_int     var size: u_int     var buffer: caddr_t     init()     init(cnt cnt: u_int, in in: u_int, out out: u_int, size size: u_int, buffer buffer: caddr_t) } ``` |

Modified pipebuf.init(cnt: u_int, in: u_int, out: u_int, size: u_int, buffer: caddr_t)

|  | Declaration |
| --- | --- |
| From | ``` init(cnt cnt: u_int, `in` `in`: u_int, out out: u_int, size size: u_int, buffer buffer: caddr_t) ``` |
| To | ``` init(cnt cnt: u_int, in in: u_int, out out: u_int, size size: u_int, buffer buffer: caddr_t) ``` |

Modified socket_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct socket_info {     var soi_stat: vinfo_stat     var soi_so: UInt64     var soi_pcb: UInt64     var soi_type: Int32     var soi_protocol: Int32     var soi_family: Int32     var soi_options: Int16     var soi_linger: Int16     var soi_state: Int16     var soi_qlen: Int16     var soi_incqlen: Int16     var soi_qlimit: Int16     var soi_timeo: Int16     var soi_error: u_short     var soi_oobmark: UInt32     var soi_rcv: sockbuf_info     var soi_snd: sockbuf_info     var soi_kind: Int32     var rfu_1: UInt32     init() } ``` |
| To | ``` struct socket_info {     struct __Unnamed_union_soi_proto {         var pri_in: in_sockinfo         var pri_tcp: tcp_sockinfo         var pri_un: un_sockinfo         var pri_ndrv: ndrv_info         var pri_kern_event: kern_event_info         var pri_kern_ctl: kern_ctl_info         init(pri_in pri_in: in_sockinfo)         init(pri_tcp pri_tcp: tcp_sockinfo)         init(pri_un pri_un: un_sockinfo)         init(pri_ndrv pri_ndrv: ndrv_info)         init(pri_kern_event pri_kern_event: kern_event_info)         init(pri_kern_ctl pri_kern_ctl: kern_ctl_info)         init()     }     var soi_stat: vinfo_stat     var soi_so: UInt64     var soi_pcb: UInt64     var soi_type: Int32     var soi_protocol: Int32     var soi_family: Int32     var soi_options: Int16     var soi_linger: Int16     var soi_state: Int16     var soi_qlen: Int16     var soi_incqlen: Int16     var soi_qlimit: Int16     var soi_timeo: Int16     var soi_error: u_short     var soi_oobmark: UInt32     var soi_rcv: sockbuf_info     var soi_snd: sockbuf_info     var soi_kind: Int32     var rfu_1: UInt32     var soi_proto: socket_info.__Unnamed_union_soi_proto     init()     init(soi_stat soi_stat: vinfo_stat, soi_so soi_so: UInt64, soi_pcb soi_pcb: UInt64, soi_type soi_type: Int32, soi_protocol soi_protocol: Int32, soi_family soi_family: Int32, soi_options soi_options: Int16, soi_linger soi_linger: Int16, soi_state soi_state: Int16, soi_qlen soi_qlen: Int16, soi_incqlen soi_incqlen: Int16, soi_qlimit soi_qlimit: Int16, soi_timeo soi_timeo: Int16, soi_error soi_error: u_short, soi_oobmark soi_oobmark: UInt32, soi_rcv soi_rcv: sockbuf_info, soi_snd soi_snd: sockbuf_info, soi_kind soi_kind: Int32, rfu_1 rfu_1: UInt32, soi_proto soi_proto: socket_info.__Unnamed_union_soi_proto) } ``` |

Modified task_vm_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_vm_info {     var virtual_size: mach_vm_size_t     var region_count: integer_t     var page_size: integer_t     var resident_size: mach_vm_size_t     var resident_size_peak: mach_vm_size_t     var device: mach_vm_size_t     var device_peak: mach_vm_size_t     var `internal`: mach_vm_size_t     var internal_peak: mach_vm_size_t     var external: mach_vm_size_t     var external_peak: mach_vm_size_t     var reusable: mach_vm_size_t     var reusable_peak: mach_vm_size_t     var purgeable_volatile_pmap: mach_vm_size_t     var purgeable_volatile_resident: mach_vm_size_t     var purgeable_volatile_virtual: mach_vm_size_t     var compressed: mach_vm_size_t     var compressed_peak: mach_vm_size_t     var compressed_lifetime: mach_vm_size_t     var phys_footprint: mach_vm_size_t     init()     init(virtual_size virtual_size: mach_vm_size_t, region_count region_count: integer_t, page_size page_size: integer_t, resident_size resident_size: mach_vm_size_t, resident_size_peak resident_size_peak: mach_vm_size_t, device device: mach_vm_size_t, device_peak device_peak: mach_vm_size_t, `internal` `internal`: mach_vm_size_t, internal_peak internal_peak: mach_vm_size_t, external external: mach_vm_size_t, external_peak external_peak: mach_vm_size_t, reusable reusable: mach_vm_size_t, reusable_peak reusable_peak: mach_vm_size_t, purgeable_volatile_pmap purgeable_volatile_pmap: mach_vm_size_t, purgeable_volatile_resident purgeable_volatile_resident: mach_vm_size_t, purgeable_volatile_virtual purgeable_volatile_virtual: mach_vm_size_t, compressed compressed: mach_vm_size_t, compressed_peak compressed_peak: mach_vm_size_t, compressed_lifetime compressed_lifetime: mach_vm_size_t, phys_footprint phys_footprint: mach_vm_size_t) } ``` |
| To | ``` struct task_vm_info {     var virtual_size: mach_vm_size_t     var region_count: integer_t     var page_size: integer_t     var resident_size: mach_vm_size_t     var resident_size_peak: mach_vm_size_t     var device: mach_vm_size_t     var device_peak: mach_vm_size_t     var `internal`: mach_vm_size_t     var internal_peak: mach_vm_size_t     var external: mach_vm_size_t     var external_peak: mach_vm_size_t     var reusable: mach_vm_size_t     var reusable_peak: mach_vm_size_t     var purgeable_volatile_pmap: mach_vm_size_t     var purgeable_volatile_resident: mach_vm_size_t     var purgeable_volatile_virtual: mach_vm_size_t     var compressed: mach_vm_size_t     var compressed_peak: mach_vm_size_t     var compressed_lifetime: mach_vm_size_t     var phys_footprint: mach_vm_size_t     init()     init(virtual_size virtual_size: mach_vm_size_t, region_count region_count: integer_t, page_size page_size: integer_t, resident_size resident_size: mach_vm_size_t, resident_size_peak resident_size_peak: mach_vm_size_t, device device: mach_vm_size_t, device_peak device_peak: mach_vm_size_t, internal internal: mach_vm_size_t, internal_peak internal_peak: mach_vm_size_t, external external: mach_vm_size_t, external_peak external_peak: mach_vm_size_t, reusable reusable: mach_vm_size_t, reusable_peak reusable_peak: mach_vm_size_t, purgeable_volatile_pmap purgeable_volatile_pmap: mach_vm_size_t, purgeable_volatile_resident purgeable_volatile_resident: mach_vm_size_t, purgeable_volatile_virtual purgeable_volatile_virtual: mach_vm_size_t, compressed compressed: mach_vm_size_t, compressed_peak compressed_peak: mach_vm_size_t, compressed_lifetime compressed_lifetime: mach_vm_size_t, phys_footprint phys_footprint: mach_vm_size_t) } ``` |

Modified task_vm_info.init(virtual_size: mach_vm_size_t, region_count: integer_t, page_size: integer_t, resident_size: mach_vm_size_t, resident_size_peak: mach_vm_size_t, device: mach_vm_size_t, device_peak: mach_vm_size_t, internal: mach_vm_size_t, internal_peak: mach_vm_size_t, external: mach_vm_size_t, external_peak: mach_vm_size_t, reusable: mach_vm_size_t, reusable_peak: mach_vm_size_t, purgeable_volatile_pmap: mach_vm_size_t, purgeable_volatile_resident: mach_vm_size_t, purgeable_volatile_virtual: mach_vm_size_t, compressed: mach_vm_size_t, compressed_peak: mach_vm_size_t, compressed_lifetime: mach_vm_size_t, phys_footprint: mach_vm_size_t)

|  | Declaration |
| --- | --- |
| From | ``` init(virtual_size virtual_size: mach_vm_size_t, region_count region_count: integer_t, page_size page_size: integer_t, resident_size resident_size: mach_vm_size_t, resident_size_peak resident_size_peak: mach_vm_size_t, device device: mach_vm_size_t, device_peak device_peak: mach_vm_size_t, `internal` `internal`: mach_vm_size_t, internal_peak internal_peak: mach_vm_size_t, external external: mach_vm_size_t, external_peak external_peak: mach_vm_size_t, reusable reusable: mach_vm_size_t, reusable_peak reusable_peak: mach_vm_size_t, purgeable_volatile_pmap purgeable_volatile_pmap: mach_vm_size_t, purgeable_volatile_resident purgeable_volatile_resident: mach_vm_size_t, purgeable_volatile_virtual purgeable_volatile_virtual: mach_vm_size_t, compressed compressed: mach_vm_size_t, compressed_peak compressed_peak: mach_vm_size_t, compressed_lifetime compressed_lifetime: mach_vm_size_t, phys_footprint phys_footprint: mach_vm_size_t) ``` |
| To | ``` init(virtual_size virtual_size: mach_vm_size_t, region_count region_count: integer_t, page_size page_size: integer_t, resident_size resident_size: mach_vm_size_t, resident_size_peak resident_size_peak: mach_vm_size_t, device device: mach_vm_size_t, device_peak device_peak: mach_vm_size_t, internal internal: mach_vm_size_t, internal_peak internal_peak: mach_vm_size_t, external external: mach_vm_size_t, external_peak external_peak: mach_vm_size_t, reusable reusable: mach_vm_size_t, reusable_peak reusable_peak: mach_vm_size_t, purgeable_volatile_pmap purgeable_volatile_pmap: mach_vm_size_t, purgeable_volatile_resident purgeable_volatile_resident: mach_vm_size_t, purgeable_volatile_virtual purgeable_volatile_virtual: mach_vm_size_t, compressed compressed: mach_vm_size_t, compressed_peak compressed_peak: mach_vm_size_t, compressed_lifetime compressed_lifetime: mach_vm_size_t, phys_footprint phys_footprint: mach_vm_size_t) ``` |

Modified tokenstr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tokenstr {     var id: u_char     var data: UnsafeMutablePointer<u_char>     var len: Int     init() } ``` |
| To | ``` struct tokenstr {     struct __Unnamed_union_tt {         var arg32: au_arg32_t         var arg64: au_arg64_t         var arb: au_arb_t         var attr32: au_attr32_t         var attr64: au_attr64_t         var execarg: au_execarg_t         var execenv: au_execenv_t         var exit: au_exit_t         var file: au_file_t         var grps: au_groups_t         var hdr32: au_header32_t         var hdr32_ex: au_header32_ex_t         var hdr64: au_header64_t         var hdr64_ex: au_header64_ex_t         var inaddr: au_inaddr_t         var inaddr_ex: au_inaddr_ex_t         var ip: au_ip_t         var ipc: au_ipc_t         var ipcperm: au_ipcperm_t         var iport: au_iport_t         var opaque: au_opaque_t         var path: au_path_t         var proc32: au_proc32_t         var proc32_ex: au_proc32ex_t         var proc64: au_proc64_t         var proc64_ex: au_proc64ex_t         var ret32: au_ret32_t         var ret64: au_ret64_t         var seq: au_seq_t         var socket: au_socket_t         var socket_ex32: au_socket_ex32_t         var sockinet_ex32: au_socketinet_ex32_t         var sockunix: au_socketunix_t         var subj32: au_subject32_t         var subj32_ex: au_subject32ex_t         var subj64: au_subject64_t         var subj64_ex: au_subject64ex_t         var text: au_text_t         var kevent: au_kevent_t         var invalid: au_invalid_t         var trail: au_trailer_t         var zonename: au_zonename_t         init(arg32 arg32: au_arg32_t)         init(arg64 arg64: au_arg64_t)         init(arb arb: au_arb_t)         init(attr32 attr32: au_attr32_t)         init(attr64 attr64: au_attr64_t)         init(execarg execarg: au_execarg_t)         init(execenv execenv: au_execenv_t)         init(exit exit: au_exit_t)         init(file file: au_file_t)         init(grps grps: au_groups_t)         init(hdr32 hdr32: au_header32_t)         init(hdr32_ex hdr32_ex: au_header32_ex_t)         init(hdr64 hdr64: au_header64_t)         init(hdr64_ex hdr64_ex: au_header64_ex_t)         init(inaddr inaddr: au_inaddr_t)         init(inaddr_ex inaddr_ex: au_inaddr_ex_t)         init(ip ip: au_ip_t)         init(ipc ipc: au_ipc_t)         init(ipcperm ipcperm: au_ipcperm_t)         init(iport iport: au_iport_t)         init(opaque opaque: au_opaque_t)         init(path path: au_path_t)         init(proc32 proc32: au_proc32_t)         init(proc32_ex proc32_ex: au_proc32ex_t)         init(proc64 proc64: au_proc64_t)         init(proc64_ex proc64_ex: au_proc64ex_t)         init(ret32 ret32: au_ret32_t)         init(ret64 ret64: au_ret64_t)         init(seq seq: au_seq_t)         init(socket socket: au_socket_t)         init(socket_ex32 socket_ex32: au_socket_ex32_t)         init(sockinet_ex32 sockinet_ex32: au_socketinet_ex32_t)         init(sockunix sockunix: au_socketunix_t)         init(subj32 subj32: au_subject32_t)         init(subj32_ex subj32_ex: au_subject32ex_t)         init(subj64 subj64: au_subject64_t)         init(subj64_ex subj64_ex: au_subject64ex_t)         init(text text: au_text_t)         init(kevent kevent: au_kevent_t)         init(invalid invalid: au_invalid_t)         init(trail trail: au_trailer_t)         init(zonename zonename: au_zonename_t)         init()     }     var id: u_char     var data: UnsafeMutablePointer<u_char>     var len: Int     var tt: tokenstr.__Unnamed_union_tt     init()     init(id id: u_char, data data: UnsafeMutablePointer<u_char>, len len: Int, tt tt: tokenstr.__Unnamed_union_tt) } ``` |

Modified ucred [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ucred {     var cr_ref: u_long     var cr_posix: posix_cred     var cr_label: COpaquePointer     var cr_audit: au_session     init() } ``` |
| To | ``` struct ucred {     struct __Unnamed_struct_cr_link {         var tqe_next: UnsafeMutablePointer<ucred>         var tqe_prev: UnsafeMutablePointer<UnsafeMutablePointer<ucred>>         init()         init(tqe_next tqe_next: UnsafeMutablePointer<ucred>, tqe_prev tqe_prev: UnsafeMutablePointer<UnsafeMutablePointer<ucred>>)     }     var cr_link: ucred.__Unnamed_struct_cr_link     var cr_ref: u_long     var cr_posix: posix_cred     var cr_label: COpaquePointer     var cr_audit: au_session     init()     init(cr_link cr_link: ucred.__Unnamed_struct_cr_link, cr_ref cr_ref: u_long, cr_posix cr_posix: posix_cred, cr_label cr_label: COpaquePointer, cr_audit cr_audit: au_session) } ``` |

Modified un_sockinfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct un_sockinfo {     var unsi_conn_so: UInt64     var unsi_conn_pcb: UInt64     init() } ``` |
| To | ``` struct un_sockinfo {     struct __Unnamed_union_unsi_addr {         var ua_sun: sockaddr_un         var ua_dummy: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)         init(ua_sun ua_sun: sockaddr_un)         init(ua_dummy ua_dummy: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))         init()     }     struct __Unnamed_union_unsi_caddr {         var ua_sun: sockaddr_un         var ua_dummy: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)         init(ua_sun ua_sun: sockaddr_un)         init(ua_dummy ua_dummy: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))         init()     }     var unsi_conn_so: UInt64     var unsi_conn_pcb: UInt64     var unsi_addr: un_sockinfo.__Unnamed_union_unsi_addr     var unsi_caddr: un_sockinfo.__Unnamed_union_unsi_caddr     init()     init(unsi_conn_so unsi_conn_so: UInt64, unsi_conn_pcb unsi_conn_pcb: UInt64, unsi_addr unsi_addr: un_sockinfo.__Unnamed_union_unsi_addr, unsi_caddr unsi_caddr: un_sockinfo.__Unnamed_union_unsi_caddr) } ``` |

Modified wait [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct wait {     var w_status: Int32     init(w_status w_status: Int32)     init() } ``` |
| To | ``` struct wait {     struct __Unnamed_struct_w_T {         var w_Termsig: UInt32         var w_Coredump: UInt32         var w_Retcode: UInt32         var w_Filler: UInt32         init()         init(w_Termsig w_Termsig: UInt32, w_Coredump w_Coredump: UInt32, w_Retcode w_Retcode: UInt32, w_Filler w_Filler: UInt32)     }     struct __Unnamed_struct_w_S {         var w_Stopval: UInt32         var w_Stopsig: UInt32         var w_Filler: UInt32         init()         init(w_Stopval w_Stopval: UInt32, w_Stopsig w_Stopsig: UInt32, w_Filler w_Filler: UInt32)     }     var w_status: Int32     var w_T: wait.__Unnamed_struct_w_T     var w_S: wait.__Unnamed_struct_w_S     init(w_status w_status: Int32)     init(w_T w_T: wait.__Unnamed_struct_w_T)     init(w_S w_S: wait.__Unnamed_struct_w_S)     init() } ``` |

Modified x86_avx_state [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct x86_avx_state {     var ash: x86_state_hdr_t     init() } ``` |
| To | ``` struct x86_avx_state {     struct __Unnamed_union_ufs {         var as32: x86_avx_state32_t         var as64: x86_avx_state64_t         init(as32 as32: x86_avx_state32_t)         init(as64 as64: x86_avx_state64_t)         init()     }     var ash: x86_state_hdr_t     var ufs: x86_avx_state.__Unnamed_union_ufs     init()     init(ash ash: x86_state_hdr_t, ufs ufs: x86_avx_state.__Unnamed_union_ufs) } ``` |

Modified x86_debug_state [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct x86_debug_state {     var dsh: x86_state_hdr_t     init() } ``` |
| To | ``` struct x86_debug_state {     struct __Unnamed_union_uds {         var ds32: x86_debug_state32_t         var ds64: x86_debug_state64_t         init(ds32 ds32: x86_debug_state32_t)         init(ds64 ds64: x86_debug_state64_t)         init()     }     var dsh: x86_state_hdr_t     var uds: x86_debug_state.__Unnamed_union_uds     init()     init(dsh dsh: x86_state_hdr_t, uds uds: x86_debug_state.__Unnamed_union_uds) } ``` |

Modified x86_exception_state [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct x86_exception_state {     var esh: x86_state_hdr_t     init() } ``` |
| To | ``` struct x86_exception_state {     struct __Unnamed_union_ues {         var es32: x86_exception_state32_t         var es64: x86_exception_state64_t         init(es32 es32: x86_exception_state32_t)         init(es64 es64: x86_exception_state64_t)         init()     }     var esh: x86_state_hdr_t     var ues: x86_exception_state.__Unnamed_union_ues     init()     init(esh esh: x86_state_hdr_t, ues ues: x86_exception_state.__Unnamed_union_ues) } ``` |

Modified x86_float_state [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct x86_float_state {     var fsh: x86_state_hdr_t     init() } ``` |
| To | ``` struct x86_float_state {     struct __Unnamed_union_ufs {         var fs32: x86_float_state32_t         var fs64: x86_float_state64_t         init(fs32 fs32: x86_float_state32_t)         init(fs64 fs64: x86_float_state64_t)         init()     }     var fsh: x86_state_hdr_t     var ufs: x86_float_state.__Unnamed_union_ufs     init()     init(fsh fsh: x86_state_hdr_t, ufs ufs: x86_float_state.__Unnamed_union_ufs) } ``` |

Modified x86_thread_state [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct x86_thread_state {     var tsh: x86_state_hdr_t     init() } ``` |
| To | ``` struct x86_thread_state {     struct __Unnamed_union_uts {         var ts32: x86_thread_state32_t         var ts64: x86_thread_state64_t         init(ts32 ts32: x86_thread_state32_t)         init(ts64 ts64: x86_thread_state64_t)         init()     }     var tsh: x86_state_hdr_t     var uts: x86_thread_state.__Unnamed_union_uts     init()     init(tsh tsh: x86_state_hdr_t, uts uts: x86_thread_state.__Unnamed_union_uts) } ``` |

Modified mach_memory_object_memory_entry(_: host_t, _: boolean_t, _: vm_size_t, _: vm_prot_t, _: memory_object_t, _: UnsafeMutablePointer<mach_port_t>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_memory_object_memory_entry(_ host: host_t, _ `internal`: boolean_t, _ size: vm_size_t, _ permission: vm_prot_t, _ pager: memory_object_t, _ entry_handle: UnsafeMutablePointer<mach_port_t>) -> kern_return_t ``` |
| To | ``` func mach_memory_object_memory_entry(_ host: host_t, _ internal: boolean_t, _ size: vm_size_t, _ permission: vm_prot_t, _ pager: memory_object_t, _ entry_handle: UnsafeMutablePointer<mach_port_t>) -> kern_return_t ``` |

Modified mach_memory_object_memory_entry_64(_: host_t, _: boolean_t, _: memory_object_size_t, _: vm_prot_t, _: memory_object_t, _: UnsafeMutablePointer<mach_port_t>) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_memory_object_memory_entry_64(_ host: host_t, _ `internal`: boolean_t, _ size: memory_object_size_t, _ permission: vm_prot_t, _ pager: memory_object_t, _ entry_handle: UnsafeMutablePointer<mach_port_t>) -> kern_return_t ``` |
| To | ``` func mach_memory_object_memory_entry_64(_ host: host_t, _ internal: boolean_t, _ size: memory_object_size_t, _ permission: vm_prot_t, _ pager: memory_object_t, _ entry_handle: UnsafeMutablePointer<mach_port_t>) -> kern_return_t ``` |

Modified mach_port_destruct(_: ipc_space_t, _: mach_port_name_t, _: mach_port_delta_t, _: mach_port_context_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_destruct(_ task: ipc_space_t, _ name: mach_port_name_t, _ srdelta: mach_port_delta_t, _ `guard`: mach_port_context_t) -> kern_return_t ``` |
| To | ``` func mach_port_destruct(_ task: ipc_space_t, _ name: mach_port_name_t, _ srdelta: mach_port_delta_t, _ guard: mach_port_context_t) -> kern_return_t ``` |

Modified mach_port_guard(_: ipc_space_t, _: mach_port_name_t, _: mach_port_context_t, _: boolean_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_guard(_ task: ipc_space_t, _ name: mach_port_name_t, _ `guard`: mach_port_context_t, _ strict: boolean_t) -> kern_return_t ``` |
| To | ``` func mach_port_guard(_ task: ipc_space_t, _ name: mach_port_name_t, _ guard: mach_port_context_t, _ strict: boolean_t) -> kern_return_t ``` |

Modified mach_port_unguard(_: ipc_space_t, _: mach_port_name_t, _: mach_port_context_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_unguard(_ task: ipc_space_t, _ name: mach_port_name_t, _ `guard`: mach_port_context_t) -> kern_return_t ``` |
| To | ``` func mach_port_unguard(_ task: ipc_space_t, _ name: mach_port_name_t, _ guard: mach_port_context_t) -> kern_return_t ``` |

Modified uuid_parse(_: UnsafePointer<Int8>, _: UnsafeMutablePointer<UInt8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func uuid_parse(_ `in`: UnsafePointer<Int8>, _ uu: UnsafeMutablePointer<UInt8>) -> Int32 ``` |
| To | ``` func uuid_parse(_ in: UnsafePointer<Int8>, _ uu: UnsafeMutablePointer<UInt8>) -> Int32 ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
