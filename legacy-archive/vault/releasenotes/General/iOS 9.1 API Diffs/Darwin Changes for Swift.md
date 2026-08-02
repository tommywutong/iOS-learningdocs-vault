---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/Darwin.html
archived_at: '2026-07-18T02:57:07.836386Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# Darwin Changes for Swift

### Darwin

Added mach_msg_descriptor_t.init(ool_ports: mach_msg_ool_ports_descriptor_t)Added mach_msg_descriptor_t.init(out_of_line: mach_msg_ool_descriptor_t)Added mach_msg_descriptor_t.init(port: mach_msg_port_descriptor_t)Added mach_msg_descriptor_t.init(type: mach_msg_type_descriptor_t)Added mach_msg_descriptor_t.ool_portsAdded mach_msg_descriptor_t.out_of_lineAdded mach_msg_descriptor_t.portAdded mach_msg_descriptor_t.typeAdded mach_msg_empty_t.init(rcv: mach_msg_empty_rcv_t)Added mach_msg_empty_t.init(send: mach_msg_empty_send_t)Added mach_msg_empty_t.rcvAdded mach_msg_empty_t.sendAdded mach_msg_ool_descriptor32_t.copyAdded mach_msg_ool_descriptor32_t.deallocateAdded mach_msg_ool_descriptor32_t.init(address: UInt32, size: mach_msg_size_t, deallocate: boolean_t, copy: mach_msg_copy_options_t, pad1: UInt32, type: mach_msg_descriptor_type_t)Added mach_msg_ool_descriptor32_t.pad1Added mach_msg_ool_descriptor32_t.typeAdded mach_msg_ool_descriptor64_t.copyAdded mach_msg_ool_descriptor64_t.deallocateAdded mach_msg_ool_descriptor64_t.init(address: UInt64, deallocate: boolean_t, copy: mach_msg_copy_options_t, pad1: UInt32, type: mach_msg_descriptor_type_t, size: mach_msg_size_t)Added mach_msg_ool_descriptor64_t.pad1Added mach_msg_ool_descriptor64_t.typeAdded mach_msg_ool_descriptor_t.copyAdded mach_msg_ool_descriptor_t.deallocateAdded mach_msg_ool_descriptor_t.init(address: UnsafeMutablePointer<Void>, size: mach_msg_size_t, deallocate: boolean_t, copy: mach_msg_copy_options_t, pad1: UInt32, type: mach_msg_descriptor_type_t)Added mach_msg_ool_descriptor_t.pad1Added mach_msg_ool_descriptor_t.typeAdded mach_msg_ool_ports_descriptor32_t.copyAdded mach_msg_ool_ports_descriptor32_t.deallocateAdded mach_msg_ool_ports_descriptor32_t.dispositionAdded mach_msg_ool_ports_descriptor32_t.init(address: UInt32, count: mach_msg_size_t, deallocate: boolean_t, copy: mach_msg_copy_options_t, disposition: mach_msg_type_name_t, type: mach_msg_descriptor_type_t)Added mach_msg_ool_ports_descriptor32_t.typeAdded mach_msg_ool_ports_descriptor64_t.copyAdded mach_msg_ool_ports_descriptor64_t.deallocateAdded mach_msg_ool_ports_descriptor64_t.dispositionAdded mach_msg_ool_ports_descriptor64_t.init(address: UInt64, deallocate: boolean_t, copy: mach_msg_copy_options_t, disposition: mach_msg_type_name_t, type: mach_msg_descriptor_type_t, count: mach_msg_size_t)Added mach_msg_ool_ports_descriptor64_t.typeAdded mach_msg_ool_ports_descriptor_t.copyAdded mach_msg_ool_ports_descriptor_t.deallocateAdded mach_msg_ool_ports_descriptor_t.dispositionAdded mach_msg_ool_ports_descriptor_t.init(address: UnsafeMutablePointer<Void>, count: mach_msg_size_t, deallocate: boolean_t, copy: mach_msg_copy_options_t, disposition: mach_msg_type_name_t, type: mach_msg_descriptor_type_t)Added mach_msg_ool_ports_descriptor_t.typeAdded mach_msg_port_descriptor_t.dispositionAdded mach_msg_port_descriptor_t.init(name: mach_port_t, pad1: mach_msg_size_t, pad2: UInt32, disposition: mach_msg_type_name_t, type: mach_msg_descriptor_type_t)Added mach_msg_port_descriptor_t.pad2Added mach_msg_port_descriptor_t.typeAdded mach_msg_type_descriptor_t.init(pad1: natural_t, pad2: mach_msg_size_t, pad3: UInt32, type: mach_msg_descriptor_type_t)Added mach_msg_type_descriptor_t.pad3Added mach_msg_type_descriptor_t.typeAdded mach_port_qos.init(name: UInt32, prealloc: UInt32, pad1: boolean_t, len: natural_t)Added mach_port_qos.nameAdded mach_port_qos.pad1Added mach_port_qos.preallocAdded POSIXError.ELASTAdded POSIXError.EWOULDBLOCKAdded semun.arrayAdded semun.bufAdded semun.init(array: UnsafeMutablePointer<UInt16>)Added semun.init(buf: UnsafeMutablePointer<__semid_ds_new>)Added semun.init(val: Int32)Added semun.valAdded sigval.init(sival_int: Int32)Added sigval.init(sival_ptr: UnsafeMutablePointer<Void>)Added sigval.sival_intAdded sigval.sival_ptrAdded tcp_connection_info.init(tcpi_state: UInt8, tcpi_snd_wscale: UInt8, tcpi_rcv_wscale: UInt8, __pad1: UInt8, tcpi_options: UInt32, tcpi_flags: UInt32, tcpi_rto: UInt32, tcpi_maxseg: UInt32, tcpi_snd_ssthresh: UInt32, tcpi_snd_cwnd: UInt32, tcpi_snd_wnd: UInt32, tcpi_snd_sbbytes: UInt32, tcpi_rcv_wnd: UInt32, tcpi_rttcur: UInt32, tcpi_srtt: UInt32, tcpi_rttvar: UInt32, tcpi_tfo_cookie_req: UInt32, tcpi_tfo_cookie_rcv: UInt32, tcpi_tfo_syn_loss: UInt32, tcpi_tfo_syn_data_sent: UInt32, tcpi_tfo_syn_data_acked: UInt32, tcpi_tfo_syn_data_rcv: UInt32, tcpi_tfo_cookie_req_rcv: UInt32, tcpi_tfo_cookie_sent: UInt32, tcpi_tfo_cookie_invalid: UInt32, __pad2: UInt32, tcpi_txpackets: UInt64, tcpi_txbytes: UInt64, tcpi_txretransmitbytes: UInt64, tcpi_rxpackets: UInt64, tcpi_rxbytes: UInt64, tcpi_rxoutoforderbytes: UInt64)Added tcp_connection_info.tcpi_tfo_cookie_invalidAdded tcp_connection_info.tcpi_tfo_cookie_rcvAdded tcp_connection_info.tcpi_tfo_cookie_reqAdded tcp_connection_info.tcpi_tfo_cookie_req_rcvAdded tcp_connection_info.tcpi_tfo_cookie_sentAdded tcp_connection_info.tcpi_tfo_syn_data_ackedAdded tcp_connection_info.tcpi_tfo_syn_data_rcvAdded tcp_connection_info.tcpi_tfo_syn_data_sentAdded tcp_connection_info.tcpi_tfo_syn_lossAdded tcphdr.init(th_sport: UInt16, th_dport: UInt16, th_seq: tcp_seq, th_ack: tcp_seq, th_x2: UInt32, th_off: UInt32, th_flags: UInt8, th_win: UInt16, th_sum: UInt16, th_urp: UInt16)Added tcphdr.th_offAdded tcphdr.th_x2Added wait.init(w_status: Int32)Added wait.w_statusAdded CPUFAMILY_INTEL_SKYLAKEAdded KERN_INSUFFICIENT_BUFFER_SIZEAdded SEM_FAILEDAdded sem_open(_: UnsafePointer<CChar>, _: CInt) -> UnsafeMutablePointer<sem_t>Added sem_open(_: UnsafePointer<CChar>, _: CInt, _: mode_t, _: CUnsignedInt) -> UnsafeMutablePointer<sem_t>Added TARGET_OS_TVModified acl_entry_id_t [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct acl_entry_id_t : RawRepresentable {     init(_ rawValue: Int32)     init(rawValue rawValue: Int32)     var rawValue: Int32 } ``` | RawRepresentable |
| To | ``` struct acl_entry_id_t : RawRepresentable, Equatable {     init(_ rawValue: Int32)     init(rawValue rawValue: Int32)     var rawValue: Int32 } ``` | Equatable, RawRepresentable |

Modified acl_flag_t [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct acl_flag_t : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct acl_flag_t : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified acl_perm_t [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct acl_perm_t : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct acl_perm_t : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified acl_tag_t [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct acl_tag_t : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct acl_tag_t : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified acl_type_t [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct acl_type_t : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct acl_type_t : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified ACTION [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ACTION : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct ACTION : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified filesec_property_t [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct filesec_property_t : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct filesec_property_t : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified idtype_t [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct idtype_t : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct idtype_t : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified mach_msg_descriptor_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_descriptor_t {     init() } ``` |
| To | ``` struct mach_msg_descriptor_t {     var port: mach_msg_port_descriptor_t     var out_of_line: mach_msg_ool_descriptor_t     var ool_ports: mach_msg_ool_ports_descriptor_t     var type: mach_msg_type_descriptor_t     init(port port: mach_msg_port_descriptor_t)     init(out_of_line out_of_line: mach_msg_ool_descriptor_t)     init(ool_ports ool_ports: mach_msg_ool_ports_descriptor_t)     init(type type: mach_msg_type_descriptor_t)     init() } ``` |

Modified mach_msg_empty_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_empty_t {     init() } ``` |
| To | ``` struct mach_msg_empty_t {     var send: mach_msg_empty_send_t     var rcv: mach_msg_empty_rcv_t     init(send send: mach_msg_empty_send_t)     init(rcv rcv: mach_msg_empty_rcv_t)     init() } ``` |

Modified mach_msg_ool_descriptor32_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_ool_descriptor32_t {     var address: UInt32     var size: mach_msg_size_t     init() } ``` |
| To | ``` struct mach_msg_ool_descriptor32_t {     var address: UInt32     var size: mach_msg_size_t     var deallocate: boolean_t     var copy: mach_msg_copy_options_t     var pad1: UInt32     var type: mach_msg_descriptor_type_t     init()     init(address address: UInt32, size size: mach_msg_size_t, deallocate deallocate: boolean_t, copy copy: mach_msg_copy_options_t, pad1 pad1: UInt32, type type: mach_msg_descriptor_type_t) } ``` |

Modified mach_msg_ool_descriptor64_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_ool_descriptor64_t {     var address: UInt64     var size: mach_msg_size_t     init() } ``` |
| To | ``` struct mach_msg_ool_descriptor64_t {     var address: UInt64     var deallocate: boolean_t     var copy: mach_msg_copy_options_t     var pad1: UInt32     var type: mach_msg_descriptor_type_t     var size: mach_msg_size_t     init()     init(address address: UInt64, deallocate deallocate: boolean_t, copy copy: mach_msg_copy_options_t, pad1 pad1: UInt32, type type: mach_msg_descriptor_type_t, size size: mach_msg_size_t) } ``` |

Modified mach_msg_ool_descriptor_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_ool_descriptor_t {     var address: UnsafeMutablePointer<Void>     var size: mach_msg_size_t     init() } ``` |
| To | ``` struct mach_msg_ool_descriptor_t {     var address: UnsafeMutablePointer<Void>     var size: mach_msg_size_t     var deallocate: boolean_t     var copy: mach_msg_copy_options_t     var pad1: UInt32     var type: mach_msg_descriptor_type_t     init()     init(address address: UnsafeMutablePointer<Void>, size size: mach_msg_size_t, deallocate deallocate: boolean_t, copy copy: mach_msg_copy_options_t, pad1 pad1: UInt32, type type: mach_msg_descriptor_type_t) } ``` |

Modified mach_msg_ool_ports_descriptor32_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_ool_ports_descriptor32_t {     var address: UInt32     var count: mach_msg_size_t     init() } ``` |
| To | ``` struct mach_msg_ool_ports_descriptor32_t {     var address: UInt32     var count: mach_msg_size_t     var deallocate: boolean_t     var copy: mach_msg_copy_options_t     var disposition: mach_msg_type_name_t     var type: mach_msg_descriptor_type_t     init()     init(address address: UInt32, count count: mach_msg_size_t, deallocate deallocate: boolean_t, copy copy: mach_msg_copy_options_t, disposition disposition: mach_msg_type_name_t, type type: mach_msg_descriptor_type_t) } ``` |

Modified mach_msg_ool_ports_descriptor64_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_ool_ports_descriptor64_t {     var address: UInt64     var count: mach_msg_size_t     init() } ``` |
| To | ``` struct mach_msg_ool_ports_descriptor64_t {     var address: UInt64     var deallocate: boolean_t     var copy: mach_msg_copy_options_t     var disposition: mach_msg_type_name_t     var type: mach_msg_descriptor_type_t     var count: mach_msg_size_t     init()     init(address address: UInt64, deallocate deallocate: boolean_t, copy copy: mach_msg_copy_options_t, disposition disposition: mach_msg_type_name_t, type type: mach_msg_descriptor_type_t, count count: mach_msg_size_t) } ``` |

Modified mach_msg_ool_ports_descriptor_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_ool_ports_descriptor_t {     var address: UnsafeMutablePointer<Void>     var count: mach_msg_size_t     init() } ``` |
| To | ``` struct mach_msg_ool_ports_descriptor_t {     var address: UnsafeMutablePointer<Void>     var count: mach_msg_size_t     var deallocate: boolean_t     var copy: mach_msg_copy_options_t     var disposition: mach_msg_type_name_t     var type: mach_msg_descriptor_type_t     init()     init(address address: UnsafeMutablePointer<Void>, count count: mach_msg_size_t, deallocate deallocate: boolean_t, copy copy: mach_msg_copy_options_t, disposition disposition: mach_msg_type_name_t, type type: mach_msg_descriptor_type_t) } ``` |

Modified mach_msg_port_descriptor_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_port_descriptor_t {     var name: mach_port_t     var pad1: mach_msg_size_t     init() } ``` |
| To | ``` struct mach_msg_port_descriptor_t {     var name: mach_port_t     var pad1: mach_msg_size_t     var pad2: UInt32     var disposition: mach_msg_type_name_t     var type: mach_msg_descriptor_type_t     init()     init(name name: mach_port_t, pad1 pad1: mach_msg_size_t, pad2 pad2: UInt32, disposition disposition: mach_msg_type_name_t, type type: mach_msg_descriptor_type_t) } ``` |

Modified mach_msg_type_descriptor_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_type_descriptor_t {     var pad1: natural_t     var pad2: mach_msg_size_t     init() } ``` |
| To | ``` struct mach_msg_type_descriptor_t {     var pad1: natural_t     var pad2: mach_msg_size_t     var pad3: UInt32     var type: mach_msg_descriptor_type_t     init()     init(pad1 pad1: natural_t, pad2 pad2: mach_msg_size_t, pad3 pad3: UInt32, type type: mach_msg_descriptor_type_t) } ``` |

Modified mach_port_guard_exception_codes [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct mach_port_guard_exception_codes : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct mach_port_guard_exception_codes : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified mach_port_qos [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_port_qos {     var len: natural_t     init() } ``` |
| To | ``` struct mach_port_qos {     var name: UInt32     var prealloc: UInt32     var pad1: boolean_t     var len: natural_t     init()     init(name name: UInt32, prealloc prealloc: UInt32, pad1 pad1: boolean_t, len len: natural_t) } ``` |

Modified MachError [enum]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` @objc enum MachError : CInt {     case KERN_SUCCESS     case KERN_INVALID_ADDRESS     case KERN_PROTECTION_FAILURE     case KERN_NO_SPACE     case KERN_INVALID_ARGUMENT     case KERN_FAILURE     case KERN_RESOURCE_SHORTAGE     case KERN_NOT_RECEIVER     case KERN_NO_ACCESS     case KERN_MEMORY_FAILURE     case KERN_MEMORY_ERROR     case KERN_ALREADY_IN_SET     case KERN_NOT_IN_SET     case KERN_NAME_EXISTS     case KERN_ABORTED     case KERN_INVALID_NAME     case KERN_INVALID_TASK     case KERN_INVALID_RIGHT     case KERN_INVALID_VALUE     case KERN_UREFS_OVERFLOW     case KERN_INVALID_CAPABILITY     case KERN_RIGHT_EXISTS     case KERN_INVALID_HOST     case KERN_MEMORY_PRESENT     case KERN_MEMORY_DATA_MOVED     case KERN_MEMORY_RESTART_COPY     case KERN_INVALID_PROCESSOR_SET     case KERN_POLICY_LIMIT     case KERN_INVALID_POLICY     case KERN_INVALID_OBJECT     case KERN_ALREADY_WAITING     case KERN_DEFAULT_SET     case KERN_EXCEPTION_PROTECTED     case KERN_INVALID_LEDGER     case KERN_INVALID_MEMORY_CONTROL     case KERN_INVALID_SECURITY     case KERN_NOT_DEPRESSED     case KERN_TERMINATED     case KERN_LOCK_SET_DESTROYED     case KERN_LOCK_UNSTABLE     case KERN_LOCK_OWNED     case KERN_LOCK_OWNED_SELF     case KERN_SEMAPHORE_DESTROYED     case KERN_RPC_SERVER_TERMINATED     case KERN_RPC_TERMINATE_ORPHAN     case KERN_RPC_CONTINUE_ORPHAN     case KERN_NOT_SUPPORTED     case KERN_NODE_DOWN     case KERN_NOT_WAITING     case KERN_OPERATION_TIMED_OUT     case KERN_CODESIGN_ERROR     case KERN_POLICY_STATIC } extension MachError : _BridgedNSError, _ObjectiveCBridgeableErrorType, ErrorType, __BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` @objc enum MachError : CInt {     case KERN_SUCCESS     case KERN_INVALID_ADDRESS     case KERN_PROTECTION_FAILURE     case KERN_NO_SPACE     case KERN_INVALID_ARGUMENT     case KERN_FAILURE     case KERN_RESOURCE_SHORTAGE     case KERN_NOT_RECEIVER     case KERN_NO_ACCESS     case KERN_MEMORY_FAILURE     case KERN_MEMORY_ERROR     case KERN_ALREADY_IN_SET     case KERN_NOT_IN_SET     case KERN_NAME_EXISTS     case KERN_ABORTED     case KERN_INVALID_NAME     case KERN_INVALID_TASK     case KERN_INVALID_RIGHT     case KERN_INVALID_VALUE     case KERN_UREFS_OVERFLOW     case KERN_INVALID_CAPABILITY     case KERN_RIGHT_EXISTS     case KERN_INVALID_HOST     case KERN_MEMORY_PRESENT     case KERN_MEMORY_DATA_MOVED     case KERN_MEMORY_RESTART_COPY     case KERN_INVALID_PROCESSOR_SET     case KERN_POLICY_LIMIT     case KERN_INVALID_POLICY     case KERN_INVALID_OBJECT     case KERN_ALREADY_WAITING     case KERN_DEFAULT_SET     case KERN_EXCEPTION_PROTECTED     case KERN_INVALID_LEDGER     case KERN_INVALID_MEMORY_CONTROL     case KERN_INVALID_SECURITY     case KERN_NOT_DEPRESSED     case KERN_TERMINATED     case KERN_LOCK_SET_DESTROYED     case KERN_LOCK_UNSTABLE     case KERN_LOCK_OWNED     case KERN_LOCK_OWNED_SELF     case KERN_SEMAPHORE_DESTROYED     case KERN_RPC_SERVER_TERMINATED     case KERN_RPC_TERMINATE_ORPHAN     case KERN_RPC_CONTINUE_ORPHAN     case KERN_NOT_SUPPORTED     case KERN_NODE_DOWN     case KERN_NOT_WAITING     case KERN_OPERATION_TIMED_OUT     case KERN_CODESIGN_ERROR     case KERN_POLICY_STATIC } extension MachError : _BridgedNSError { } ``` | -- |

Modified NXByteOrder [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NXByteOrder : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct NXByteOrder : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified POSIXError [enum]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` @objc enum POSIXError : CInt {     case EPERM     case ENOENT     case ESRCH     case EINTR     case EIO     case ENXIO     case E2BIG     case ENOEXEC     case EBADF     case ECHILD     case EDEADLK     case ENOMEM     case EACCES     case EFAULT     case ENOTBLK     case EBUSY     case EEXIST     case EXDEV     case ENODEV     case ENOTDIR     case EISDIR     case EINVAL     case ENFILE     case EMFILE     case ENOTTY     case ETXTBSY     case EFBIG     case ENOSPC     case ESPIPE     case EROFS     case EMLINK     case EPIPE     case EDOM     case ERANGE     case EAGAIN     case EINPROGRESS     case EALREADY     case ENOTSOCK     case EDESTADDRREQ     case EMSGSIZE     case EPROTOTYPE     case ENOPROTOOPT     case EPROTONOSUPPORT     case ESOCKTNOSUPPORT     case ENOTSUP     case EPFNOSUPPORT     case EAFNOSUPPORT     case EADDRINUSE     case EADDRNOTAVAIL     case ENETDOWN     case ENETUNREACH     case ENETRESET     case ECONNABORTED     case ECONNRESET     case ENOBUFS     case EISCONN     case ENOTCONN     case ESHUTDOWN     case ETOOMANYREFS     case ETIMEDOUT     case ECONNREFUSED     case ELOOP     case ENAMETOOLONG     case EHOSTDOWN     case EHOSTUNREACH     case ENOTEMPTY     case EPROCLIM     case EUSERS     case EDQUOT     case ESTALE     case EREMOTE     case EBADRPC     case ERPCMISMATCH     case EPROGUNAVAIL     case EPROGMISMATCH     case EPROCUNAVAIL     case ENOLCK     case ENOSYS     case EFTYPE     case EAUTH     case ENEEDAUTH     case EPWROFF     case EDEVERR     case EOVERFLOW     case EBADEXEC     case EBADARCH     case ESHLIBVERS     case EBADMACHO     case ECANCELED     case EIDRM     case ENOMSG     case EILSEQ     case ENOATTR     case EBADMSG     case EMULTIHOP     case ENODATA     case ENOLINK     case ENOSR     case ENOSTR     case EPROTO     case ETIME     case ENOPOLICY     case ENOTRECOVERABLE     case EOWNERDEAD     case EQFULL } extension POSIXError : _BridgedNSError, _ObjectiveCBridgeableErrorType, ErrorType, __BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` @objc enum POSIXError : CInt {     case EPERM     case ENOENT     case ESRCH     case EINTR     case EIO     case ENXIO     case E2BIG     case ENOEXEC     case EBADF     case ECHILD     case EDEADLK     case ENOMEM     case EACCES     case EFAULT     case ENOTBLK     case EBUSY     case EEXIST     case EXDEV     case ENODEV     case ENOTDIR     case EISDIR     case EINVAL     case ENFILE     case EMFILE     case ENOTTY     case ETXTBSY     case EFBIG     case ENOSPC     case ESPIPE     case EROFS     case EMLINK     case EPIPE     case EDOM     case ERANGE     case EAGAIN     static var EWOULDBLOCK: POSIXError { get }     case EINPROGRESS     case EALREADY     case ENOTSOCK     case EDESTADDRREQ     case EMSGSIZE     case EPROTOTYPE     case ENOPROTOOPT     case EPROTONOSUPPORT     case ESOCKTNOSUPPORT     case ENOTSUP     case EPFNOSUPPORT     case EAFNOSUPPORT     case EADDRINUSE     case EADDRNOTAVAIL     case ENETDOWN     case ENETUNREACH     case ENETRESET     case ECONNABORTED     case ECONNRESET     case ENOBUFS     case EISCONN     case ENOTCONN     case ESHUTDOWN     case ETOOMANYREFS     case ETIMEDOUT     case ECONNREFUSED     case ELOOP     case ENAMETOOLONG     case EHOSTDOWN     case EHOSTUNREACH     case ENOTEMPTY     case EPROCLIM     case EUSERS     case EDQUOT     case ESTALE     case EREMOTE     case EBADRPC     case ERPCMISMATCH     case EPROGUNAVAIL     case EPROGMISMATCH     case EPROCUNAVAIL     case ENOLCK     case ENOSYS     case EFTYPE     case EAUTH     case ENEEDAUTH     case EPWROFF     case EDEVERR     case EOVERFLOW     case EBADEXEC     case EBADARCH     case ESHLIBVERS     case EBADMACHO     case ECANCELED     case EIDRM     case ENOMSG     case EILSEQ     case ENOATTR     case EBADMSG     case EMULTIHOP     case ENODATA     case ENOLINK     case ENOSR     case ENOSTR     case EPROTO     case ETIME     case ENOPOLICY     case ENOTRECOVERABLE     case EOWNERDEAD     case EQFULL     static var ELAST: POSIXError { get } } extension POSIXError : _BridgedNSError { } ``` | -- |

Modified qos_class_t [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct qos_class_t : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct qos_class_t : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified semun [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct semun {     init() } ``` |
| To | ``` struct semun {     var val: Int32     var buf: UnsafeMutablePointer<__semid_ds_new>     var array: UnsafeMutablePointer<UInt16>     init(val val: Int32)     init(buf buf: UnsafeMutablePointer<__semid_ds_new>)     init(array array: UnsafeMutablePointer<UInt16>)     init() } ``` |

Modified sigval [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sigval {     init() } ``` |
| To | ``` struct sigval {     var sival_int: Int32     var sival_ptr: UnsafeMutablePointer<Void>     init(sival_int sival_int: Int32)     init(sival_ptr sival_ptr: UnsafeMutablePointer<Void>)     init() } ``` |

Modified task_latency_qos [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct task_latency_qos : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct task_latency_qos : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified task_role [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct task_role : RawRepresentable {     init(_ rawValue: Int32)     init(rawValue rawValue: Int32)     var rawValue: Int32 } ``` | RawRepresentable |
| To | ``` struct task_role : RawRepresentable, Equatable {     init(_ rawValue: Int32)     init(rawValue rawValue: Int32)     var rawValue: Int32 } ``` | Equatable, RawRepresentable |

Modified task_throughput_qos [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct task_throughput_qos : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct task_throughput_qos : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified tcp_connection_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tcp_connection_info {     var tcpi_state: UInt8     var tcpi_snd_wscale: UInt8     var tcpi_rcv_wscale: UInt8     var __pad1: UInt8     var tcpi_options: UInt32     var tcpi_flags: UInt32     var tcpi_rto: UInt32     var tcpi_maxseg: UInt32     var tcpi_snd_ssthresh: UInt32     var tcpi_snd_cwnd: UInt32     var tcpi_snd_wnd: UInt32     var tcpi_snd_sbbytes: UInt32     var tcpi_rcv_wnd: UInt32     var tcpi_rttcur: UInt32     var tcpi_srtt: UInt32     var tcpi_rttvar: UInt32     var tcpi_txpackets: UInt64     var tcpi_txbytes: UInt64     var tcpi_txretransmitbytes: UInt64     var tcpi_rxpackets: UInt64     var tcpi_rxbytes: UInt64     var tcpi_rxoutoforderbytes: UInt64     init() } ``` |
| To | ``` struct tcp_connection_info {     var tcpi_state: UInt8     var tcpi_snd_wscale: UInt8     var tcpi_rcv_wscale: UInt8     var __pad1: UInt8     var tcpi_options: UInt32     var tcpi_flags: UInt32     var tcpi_rto: UInt32     var tcpi_maxseg: UInt32     var tcpi_snd_ssthresh: UInt32     var tcpi_snd_cwnd: UInt32     var tcpi_snd_wnd: UInt32     var tcpi_snd_sbbytes: UInt32     var tcpi_rcv_wnd: UInt32     var tcpi_rttcur: UInt32     var tcpi_srtt: UInt32     var tcpi_rttvar: UInt32     var tcpi_tfo_cookie_req: UInt32     var tcpi_tfo_cookie_rcv: UInt32     var tcpi_tfo_syn_loss: UInt32     var tcpi_tfo_syn_data_sent: UInt32     var tcpi_tfo_syn_data_acked: UInt32     var tcpi_tfo_syn_data_rcv: UInt32     var tcpi_tfo_cookie_req_rcv: UInt32     var tcpi_tfo_cookie_sent: UInt32     var tcpi_tfo_cookie_invalid: UInt32     var __pad2: UInt32     var tcpi_txpackets: UInt64     var tcpi_txbytes: UInt64     var tcpi_txretransmitbytes: UInt64     var tcpi_rxpackets: UInt64     var tcpi_rxbytes: UInt64     var tcpi_rxoutoforderbytes: UInt64     init()     init(tcpi_state tcpi_state: UInt8, tcpi_snd_wscale tcpi_snd_wscale: UInt8, tcpi_rcv_wscale tcpi_rcv_wscale: UInt8, __pad1 __pad1: UInt8, tcpi_options tcpi_options: UInt32, tcpi_flags tcpi_flags: UInt32, tcpi_rto tcpi_rto: UInt32, tcpi_maxseg tcpi_maxseg: UInt32, tcpi_snd_ssthresh tcpi_snd_ssthresh: UInt32, tcpi_snd_cwnd tcpi_snd_cwnd: UInt32, tcpi_snd_wnd tcpi_snd_wnd: UInt32, tcpi_snd_sbbytes tcpi_snd_sbbytes: UInt32, tcpi_rcv_wnd tcpi_rcv_wnd: UInt32, tcpi_rttcur tcpi_rttcur: UInt32, tcpi_srtt tcpi_srtt: UInt32, tcpi_rttvar tcpi_rttvar: UInt32, tcpi_tfo_cookie_req tcpi_tfo_cookie_req: UInt32, tcpi_tfo_cookie_rcv tcpi_tfo_cookie_rcv: UInt32, tcpi_tfo_syn_loss tcpi_tfo_syn_loss: UInt32, tcpi_tfo_syn_data_sent tcpi_tfo_syn_data_sent: UInt32, tcpi_tfo_syn_data_acked tcpi_tfo_syn_data_acked: UInt32, tcpi_tfo_syn_data_rcv tcpi_tfo_syn_data_rcv: UInt32, tcpi_tfo_cookie_req_rcv tcpi_tfo_cookie_req_rcv: UInt32, tcpi_tfo_cookie_sent tcpi_tfo_cookie_sent: UInt32, tcpi_tfo_cookie_invalid tcpi_tfo_cookie_invalid: UInt32, __pad2 __pad2: UInt32, tcpi_txpackets tcpi_txpackets: UInt64, tcpi_txbytes tcpi_txbytes: UInt64, tcpi_txretransmitbytes tcpi_txretransmitbytes: UInt64, tcpi_rxpackets tcpi_rxpackets: UInt64, tcpi_rxbytes tcpi_rxbytes: UInt64, tcpi_rxoutoforderbytes tcpi_rxoutoforderbytes: UInt64) } ``` |

Modified tcphdr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tcphdr {     var th_sport: UInt16     var th_dport: UInt16     var th_seq: tcp_seq     var th_ack: tcp_seq     var th_flags: UInt8     var th_win: UInt16     var th_sum: UInt16     var th_urp: UInt16     init() } ``` |
| To | ``` struct tcphdr {     var th_sport: UInt16     var th_dport: UInt16     var th_seq: tcp_seq     var th_ack: tcp_seq     var th_x2: UInt32     var th_off: UInt32     var th_flags: UInt8     var th_win: UInt16     var th_sum: UInt16     var th_urp: UInt16     init()     init(th_sport th_sport: UInt16, th_dport th_dport: UInt16, th_seq th_seq: tcp_seq, th_ack th_ack: tcp_seq, th_x2 th_x2: UInt32, th_off th_off: UInt32, th_flags th_flags: UInt8, th_win th_win: UInt16, th_sum th_sum: UInt16, th_urp th_urp: UInt16) } ``` |

Modified uio_rw [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct uio_rw : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct uio_rw : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified VISIT [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct VISIT : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct VISIT : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified wait [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct wait {     init() } ``` |
| To | ``` struct wait {     var w_status: Int32     init(w_status w_status: Int32)     init() } ``` |

Modified noErr

|  | Declaration |
| --- | --- |
| From | ``` let noErr: OSStatus ``` |
| To | ``` var noErr: OSStatus { get } ``` |

Modified S_IEXEC

|  | Declaration |
| --- | --- |
| From | ``` let S_IEXEC: mode_t ``` |
| To | ``` var S_IEXEC: mode_t { get } ``` |

Modified S_IFBLK

|  | Declaration |
| --- | --- |
| From | ``` let S_IFBLK: mode_t ``` |
| To | ``` var S_IFBLK: mode_t { get } ``` |

Modified S_IFCHR

|  | Declaration |
| --- | --- |
| From | ``` let S_IFCHR: mode_t ``` |
| To | ``` var S_IFCHR: mode_t { get } ``` |

Modified S_IFDIR

|  | Declaration |
| --- | --- |
| From | ``` let S_IFDIR: mode_t ``` |
| To | ``` var S_IFDIR: mode_t { get } ``` |

Modified S_IFIFO

|  | Declaration |
| --- | --- |
| From | ``` let S_IFIFO: mode_t ``` |
| To | ``` var S_IFIFO: mode_t { get } ``` |

Modified S_IFLNK

|  | Declaration |
| --- | --- |
| From | ``` let S_IFLNK: mode_t ``` |
| To | ``` var S_IFLNK: mode_t { get } ``` |

Modified S_IFMT

|  | Declaration |
| --- | --- |
| From | ``` let S_IFMT: mode_t ``` |
| To | ``` var S_IFMT: mode_t { get } ``` |

Modified S_IFREG

|  | Declaration |
| --- | --- |
| From | ``` let S_IFREG: mode_t ``` |
| To | ``` var S_IFREG: mode_t { get } ``` |

Modified S_IFSOCK

|  | Declaration |
| --- | --- |
| From | ``` let S_IFSOCK: mode_t ``` |
| To | ``` var S_IFSOCK: mode_t { get } ``` |

Modified S_IFWHT

|  | Declaration |
| --- | --- |
| From | ``` let S_IFWHT: mode_t ``` |
| To | ``` var S_IFWHT: mode_t { get } ``` |

Modified S_IREAD

|  | Declaration |
| --- | --- |
| From | ``` let S_IREAD: mode_t ``` |
| To | ``` var S_IREAD: mode_t { get } ``` |

Modified S_IRGRP

|  | Declaration |
| --- | --- |
| From | ``` let S_IRGRP: mode_t ``` |
| To | ``` var S_IRGRP: mode_t { get } ``` |

Modified S_IROTH

|  | Declaration |
| --- | --- |
| From | ``` let S_IROTH: mode_t ``` |
| To | ``` var S_IROTH: mode_t { get } ``` |

Modified S_IRUSR

|  | Declaration |
| --- | --- |
| From | ``` let S_IRUSR: mode_t ``` |
| To | ``` var S_IRUSR: mode_t { get } ``` |

Modified S_IRWXG

|  | Declaration |
| --- | --- |
| From | ``` let S_IRWXG: mode_t ``` |
| To | ``` var S_IRWXG: mode_t { get } ``` |

Modified S_IRWXO

|  | Declaration |
| --- | --- |
| From | ``` let S_IRWXO: mode_t ``` |
| To | ``` var S_IRWXO: mode_t { get } ``` |

Modified S_IRWXU

|  | Declaration |
| --- | --- |
| From | ``` let S_IRWXU: mode_t ``` |
| To | ``` var S_IRWXU: mode_t { get } ``` |

Modified S_ISGID

|  | Declaration |
| --- | --- |
| From | ``` let S_ISGID: mode_t ``` |
| To | ``` var S_ISGID: mode_t { get } ``` |

Modified S_ISTXT

|  | Declaration |
| --- | --- |
| From | ``` let S_ISTXT: mode_t ``` |
| To | ``` var S_ISTXT: mode_t { get } ``` |

Modified S_ISUID

|  | Declaration |
| --- | --- |
| From | ``` let S_ISUID: mode_t ``` |
| To | ``` var S_ISUID: mode_t { get } ``` |

Modified S_ISVTX

|  | Declaration |
| --- | --- |
| From | ``` let S_ISVTX: mode_t ``` |
| To | ``` var S_ISVTX: mode_t { get } ``` |

Modified S_IWGRP

|  | Declaration |
| --- | --- |
| From | ``` let S_IWGRP: mode_t ``` |
| To | ``` var S_IWGRP: mode_t { get } ``` |

Modified S_IWOTH

|  | Declaration |
| --- | --- |
| From | ``` let S_IWOTH: mode_t ``` |
| To | ``` var S_IWOTH: mode_t { get } ``` |

Modified S_IWRITE

|  | Declaration |
| --- | --- |
| From | ``` let S_IWRITE: mode_t ``` |
| To | ``` var S_IWRITE: mode_t { get } ``` |

Modified S_IWUSR

|  | Declaration |
| --- | --- |
| From | ``` let S_IWUSR: mode_t ``` |
| To | ``` var S_IWUSR: mode_t { get } ``` |

Modified S_IXGRP

|  | Declaration |
| --- | --- |
| From | ``` let S_IXGRP: mode_t ``` |
| To | ``` var S_IXGRP: mode_t { get } ``` |

Modified S_IXOTH

|  | Declaration |
| --- | --- |
| From | ``` let S_IXOTH: mode_t ``` |
| To | ``` var S_IXOTH: mode_t { get } ``` |

Modified S_IXUSR

|  | Declaration |
| --- | --- |
| From | ``` let S_IXUSR: mode_t ``` |
| To | ``` var S_IXUSR: mode_t { get } ``` |

Modified SIG_DFL

|  | Declaration |
| --- | --- |
| From | ``` let SIG_DFL: sig_t? ``` |
| To | ``` var SIG_DFL: sig_t? { get } ``` |

Modified SIG_ERR

|  | Declaration |
| --- | --- |
| From | ``` let SIG_ERR: sig_t ``` |
| To | ``` var SIG_ERR: sig_t { get } ``` |

Modified SIG_HOLD

|  | Declaration |
| --- | --- |
| From | ``` let SIG_HOLD: sig_t ``` |
| To | ``` var SIG_HOLD: sig_t { get } ``` |

Modified SIG_IGN

|  | Declaration |
| --- | --- |
| From | ``` let SIG_IGN: sig_t ``` |
| To | ``` var SIG_IGN: sig_t { get } ``` |

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
