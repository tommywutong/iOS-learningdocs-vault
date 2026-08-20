---
title: tvOS 9.2 API Diffs
apple_id: TP40016673
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS92APIDiffs/Swift/Darwin.html
archived_at: '2026-07-18T02:58:05.687818Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 9.2 API Diffs](tvOS%209.1%20to%209.2%20API%20Differences.md)


# Darwin Changes for Swift

### Darwin

Removed P_RESV10Removed VQ_FLAG1000Added arm_unified_thread_state.init(ash: arm_state_hdr_t, uts: arm_unified_thread_state.__Unnamed_union_uts)Added arm_unified_thread_state.utsAdded eproc [struct]Added eproc.e_flagAdded eproc.e_jobcAdded eproc.e_loginAdded eproc.e_paddrAdded eproc.e_pcredAdded eproc.e_pgidAdded eproc.e_ppidAdded eproc.e_sessAdded eproc.e_spareAdded eproc.e_tdevAdded eproc.e_tpgidAdded eproc.e_tsessAdded eproc.e_ucredAdded eproc.e_vmAdded eproc.e_wmesgAdded eproc.e_xccountAdded eproc.e_xrssizeAdded eproc.e_xsizeAdded eproc.e_xswrssAdded eproc.init()Added eproc.init(e_paddr: COpaquePointer, e_sess: COpaquePointer, e_pcred: _pcred, e_ucred: _ucred, e_vm: vmspace, e_ppid: pid_t, e_pgid: pid_t, e_jobc: Int16, e_tdev: dev_t, e_tpgid: pid_t, e_tsess: COpaquePointer, e_wmesg: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), e_xsize: segsz_t, e_xrssize: Int16, e_xccount: Int16, e_xswrss: Int16, e_flag: Int32, e_login: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), e_spare: (Int32, Int32, Int32, Int32))Added extern_proc.p_unAdded ifconf.ifc_ifcuAdded ifconf.init(ifc_len: Int32, ifc_ifcu: ifconf.__Unnamed_union_ifc_ifcu)Added ifkpi.ifk_dataAdded ifkpi.init(ifk_module_id: UInt32, ifk_type: UInt32, ifk_data: ifkpi.__Unnamed_union_ifk_data)Added ifreq.ifr_ifruAdded ifreq.init(ifr_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifr_ifru: ifreq.__Unnamed_union_ifr_ifru)Added in6_addr.init(__u6_addr: in6_addr.__Unnamed_union___u6_addr)Added posix_cred [struct]Added posix_cred.cr_flagsAdded posix_cred.cr_gmuidAdded posix_cred.cr_groupsAdded posix_cred.cr_ngroupsAdded posix_cred.cr_rgidAdded posix_cred.cr_ruidAdded posix_cred.cr_svgidAdded posix_cred.cr_svuidAdded posix_cred.cr_uidAdded posix_cred.init()Added posix_cred.init(cr_uid: uid_t, cr_ruid: uid_t, cr_svuid: uid_t, cr_ngroups: Int16, cr_groups: (gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t), cr_rgid: gid_t, cr_svgid: gid_t, cr_gmuid: uid_t, cr_flags: Int32)Added ucred.cr_linkAdded ucred.init(cr_link: ucred.__Unnamed_struct_cr_link, cr_ref: u_long, cr_posix: posix_cred, cr_label: COpaquePointer, cr_audit: au_session)Added wait.init(w_S: wait.__Unnamed_struct_w_S)Added wait.init(w_T: wait.__Unnamed_struct_w_T)Added wait.w_SAdded wait.w_TAdded arc4random() -> UInt32Added arc4random_uniform(_: UInt32) -> UInt32Added close(_: Int32) -> Int32Added fcntl(_: CInt, _: CInt) -> CIntAdded fcntl(_: CInt, _: CInt, _: UnsafeMutablePointer<Void>) -> CIntAdded fcntl(_: CInt, _: CInt, _: CInt) -> CIntAdded free(_: UnsafeMutablePointer<Void>)Added host_check_multiuser_mode(_: host_t, _: UnsafeMutablePointer<UInt32>) -> kern_return_tAdded host_get_multiuser_config_flags(_: host_t, _: UnsafeMutablePointer<UInt32>) -> kern_return_tAdded host_set_multiuser_config_flags(_: host_priv_t, _: UInt32) -> kern_return_tAdded MAC_OS_X_VERSION_10_11_3Added MAC_OS_X_VERSION_10_11_4Added mach_voucher_attr_value_flags_tAdded memcmp(_: UnsafePointer<Void>, _: UnsafePointer<Void>, _: Int) -> Int32Added P_ADOPTPERSONAAdded putchar(_: Int32) -> Int32Added read(_: Int32, _: UnsafeMutablePointer<Void>, _: Int) -> IntAdded strcmp(_: UnsafePointer<Int8>, _: UnsafePointer<Int8>) -> Int32Added strcpy(_: UnsafeMutablePointer<Int8>, _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8>Added strlen(_: UnsafePointer<Int8>) -> UIntAdded strtod(_: UnsafePointer<Int8>, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> DoubleAdded strtof(_: UnsafePointer<Int8>, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> FloatAdded SYS_personaAdded SYS_usrctlAdded VQ_QUOTAAdded write(_: Int32, _: UnsafePointer<Void>, _: Int) -> IntModified arm_unified_thread_state [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct arm_unified_thread_state {     var ash: arm_state_hdr_t     init() } ``` |
| To | ``` struct arm_unified_thread_state {     struct __Unnamed_union_uts {         var ts_32: arm_thread_state32_t         var ts_64: arm_thread_state64_t         init(ts_32 ts_32: arm_thread_state32_t)         init(ts_64 ts_64: arm_thread_state64_t)         init()     }     var ash: arm_state_hdr_t     var uts: arm_unified_thread_state.__Unnamed_union_uts     init()     init(ash ash: arm_state_hdr_t, uts uts: arm_unified_thread_state.__Unnamed_union_uts) } ``` |

Modified extern_proc [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct extern_proc {     var p_vmspace: UnsafeMutablePointer<vmspace>     var p_sigacts: COpaquePointer     var p_flag: Int32     var p_stat: Int8     var p_pid: pid_t     var p_oppid: pid_t     var p_dupfd: Int32     var user_stack: caddr_t     var exit_thread: UnsafeMutablePointer<Void>     var p_debugger: Int32     var sigwait: boolean_t     var p_estcpu: u_int     var p_cpticks: Int32     var p_pctcpu: fixpt_t     var p_wchan: UnsafeMutablePointer<Void>     var p_wmesg: UnsafeMutablePointer<Int8>     var p_swtime: u_int     var p_slptime: u_int     var p_realtimer: itimerval     var p_rtime: timeval     var p_uticks: u_quad_t     var p_sticks: u_quad_t     var p_iticks: u_quad_t     var p_traceflag: Int32     var p_tracep: COpaquePointer     var p_siglist: Int32     var p_textvp: COpaquePointer     var p_holdcnt: Int32     var p_sigmask: sigset_t     var p_sigignore: sigset_t     var p_sigcatch: sigset_t     var p_priority: u_char     var p_usrpri: u_char     var p_nice: Int8     var p_comm: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var p_pgrp: COpaquePointer     var p_addr: COpaquePointer     var p_xstat: u_short     var p_acflag: u_short     var p_ru: UnsafeMutablePointer<rusage>     init() } ``` |
| To | ``` struct extern_proc {     struct __Unnamed_union_p_un {         struct __Unnamed_struct_p_st1 {             var __p_forw: COpaquePointer             var __p_back: COpaquePointer             init()             init(__p_forw __p_forw: COpaquePointer, __p_back __p_back: COpaquePointer)         }         var p_st1: extern_proc.__Unnamed_union_p_un.__Unnamed_struct_p_st1         var __p_starttime: timeval         init(p_st1 p_st1: extern_proc.__Unnamed_union_p_un.__Unnamed_struct_p_st1)         init(__p_starttime __p_starttime: timeval)         init()     }     var p_un: extern_proc.__Unnamed_union_p_un     var p_vmspace: UnsafeMutablePointer<vmspace>     var p_sigacts: COpaquePointer     var p_flag: Int32     var p_stat: Int8     var p_pid: pid_t     var p_oppid: pid_t     var p_dupfd: Int32     var user_stack: caddr_t     var exit_thread: UnsafeMutablePointer<Void>     var p_debugger: Int32     var sigwait: boolean_t     var p_estcpu: u_int     var p_cpticks: Int32     var p_pctcpu: fixpt_t     var p_wchan: UnsafeMutablePointer<Void>     var p_wmesg: UnsafeMutablePointer<Int8>     var p_swtime: u_int     var p_slptime: u_int     var p_realtimer: itimerval     var p_rtime: timeval     var p_uticks: u_quad_t     var p_sticks: u_quad_t     var p_iticks: u_quad_t     var p_traceflag: Int32     var p_tracep: COpaquePointer     var p_siglist: Int32     var p_textvp: COpaquePointer     var p_holdcnt: Int32     var p_sigmask: sigset_t     var p_sigignore: sigset_t     var p_sigcatch: sigset_t     var p_priority: u_char     var p_usrpri: u_char     var p_nice: Int8     var p_comm: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var p_pgrp: COpaquePointer     var p_addr: COpaquePointer     var p_xstat: u_short     var p_acflag: u_short     var p_ru: UnsafeMutablePointer<rusage>     init() } ``` |

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

Modified ucred [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ucred {     var cr_ref: u_long     var cr_posix: posix_cred     var cr_label: COpaquePointer     var cr_audit: au_session     init() } ``` |
| To | ``` struct ucred {     struct __Unnamed_struct_cr_link {         var tqe_next: UnsafeMutablePointer<ucred>         var tqe_prev: UnsafeMutablePointer<UnsafeMutablePointer<ucred>>         init()         init(tqe_next tqe_next: UnsafeMutablePointer<ucred>, tqe_prev tqe_prev: UnsafeMutablePointer<UnsafeMutablePointer<ucred>>)     }     var cr_link: ucred.__Unnamed_struct_cr_link     var cr_ref: u_long     var cr_posix: posix_cred     var cr_label: COpaquePointer     var cr_audit: au_session     init()     init(cr_link cr_link: ucred.__Unnamed_struct_cr_link, cr_ref cr_ref: u_long, cr_posix cr_posix: posix_cred, cr_label cr_label: COpaquePointer, cr_audit cr_audit: au_session) } ``` |

Modified wait [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct wait {     var w_status: Int32     init(w_status w_status: Int32)     init() } ``` |
| To | ``` struct wait {     struct __Unnamed_struct_w_T {         var w_Termsig: UInt32         var w_Coredump: UInt32         var w_Retcode: UInt32         var w_Filler: UInt32         init()         init(w_Termsig w_Termsig: UInt32, w_Coredump w_Coredump: UInt32, w_Retcode w_Retcode: UInt32, w_Filler w_Filler: UInt32)     }     struct __Unnamed_struct_w_S {         var w_Stopval: UInt32         var w_Stopsig: UInt32         var w_Filler: UInt32         init()         init(w_Stopval w_Stopval: UInt32, w_Stopsig w_Stopsig: UInt32, w_Filler w_Filler: UInt32)     }     var w_status: Int32     var w_T: wait.__Unnamed_struct_w_T     var w_S: wait.__Unnamed_struct_w_S     init(w_status w_status: Int32)     init(w_T w_T: wait.__Unnamed_struct_w_T)     init(w_S w_S: wait.__Unnamed_struct_w_S)     init() } ``` |

Modified CPUFAMILY_ARM_TWISTER

|  | Introduction |
| --- | --- |
| From | tvOS 9.1 |
| To | tvOS 9.0 |

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
