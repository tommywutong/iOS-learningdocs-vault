---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/Darwin.html
archived_at: '2026-07-18T02:55:17.455552Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# Darwin Changes for Swift

### Darwin

Removed addrinfo.init(ai_flags: Int32, ai_family: Int32, ai_socktype: Int32, ai_protocol: Int32, ai_addrlen: socklen_t, ai_canonname: UnsafeMutablePointer<Int8>, ai_addr: UnsafeMutablePointer<sockaddr>, ai_next: UnsafeMutablePointer<addrinfo>)Removed aiocb.init(aio_fildes: Int32, aio_offset: off_t, aio_buf: UnsafeMutablePointer<Void>, aio_nbytes: Int, aio_reqprio: Int32, aio_sigevent: sigevent, aio_lio_opcode: Int32)Removed au_session.init(as_aia_p: UnsafeMutablePointer<auditinfo_addr_t>, as_mask: au_mask_t)Removed ctlname.init(ctl_name: UnsafeMutablePointer<Int8>, ctl_type: Int32)Removed datum.init(dptr: UnsafeMutablePointer<Void>, dsize: Int)Removed DBM.init(__opaque: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Removed DIR.init(__dd_fd: Int32, __dd_loc: Int, __dd_size: Int, __dd_buf: UnsafeMutablePointer<Int8>, __dd_len: Int32, __dd_seek: Int, __dd_rewind: Int, __dd_flags: Int32, __dd_lock: __darwin_pthread_mutex_t, __dd_td: COpaquePointer)Removed dl_info.init(dli_fname: UnsafePointer<Int8>, dli_fbase: UnsafeMutablePointer<Void>, dli_sname: UnsafePointer<Int8>, dli_saddr: UnsafeMutablePointer<Void>)Removed entry.init(key: UnsafeMutablePointer<Int8>, data: UnsafeMutablePointer<Void>)Removed eproc.init(e_paddr: COpaquePointer, e_sess: COpaquePointer, e_pcred: _pcred, e_ucred: _ucred, e_vm: vmspace, e_ppid: pid_t, e_pgid: pid_t, e_jobc: Int16, e_tdev: dev_t, e_tpgid: pid_t, e_tsess: COpaquePointer, e_wmesg: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), e_xsize: segsz_t, e_xrssize: Int16, e_xccount: Int16, e_xswrss: Int16, e_flag: Int32, e_login: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), e_spare: (Int32, Int32, Int32, Int32))Removed exception.init(type: Int32, name: UnsafeMutablePointer<Int8>, arg1: Double, arg2: Double, retval: Double)Removed fbootstraptransfer.init(fbt_offset: off_t, fbt_length: Int, fbt_buffer: UnsafeMutablePointer<Void>)Removed fcodeblobs.init(f_cd_hash: UnsafeMutablePointer<Void>, f_hash_size: Int, f_cd_buffer: UnsafeMutablePointer<Void>, f_cd_size: Int, f_out_size: UnsafeMutablePointer<UInt32>, f_arch: Int32, __padding: Int32)Removed fenv_t.init(__fpscr: UInt32, __reserved0: UInt32, __reserved1: UInt32, __reserved2: UInt32)Removed fsignatures.init(fs_file_start: off_t, fs_blob_start: UnsafeMutablePointer<Void>, fs_blob_size: Int)Removed fssearchblock.init(returnattrs: UnsafeMutablePointer<attrlist>, returnbuffer: UnsafeMutablePointer<Void>, returnbuffersize: Int, maxmatches: u_long, timelimit: timeval, searchparams1: UnsafeMutablePointer<Void>, sizeofsearchparams1: Int, searchparams2: UnsafeMutablePointer<Void>, sizeofsearchparams2: Int, searchattrs: attrlist)Removed group.init(gr_name: UnsafeMutablePointer<Int8>, gr_passwd: UnsafeMutablePointer<Int8>, gr_gid: gid_t, gr_mem: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>)Removed hostent.init(h_name: UnsafeMutablePointer<Int8>, h_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, h_addrtype: Int32, h_length: Int32, h_addr_list: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>)Removed iconv_fallbacks.init(mb_to_uc_fallback: iconv_unicode_mb_to_uc_fallback!, uc_to_mb_fallback: iconv_unicode_uc_to_mb_fallback!, mb_to_wc_fallback: iconv_wchar_mb_to_wc_fallback!, wc_to_mb_fallback: iconv_wchar_wc_to_mb_fallback!, data: UnsafeMutablePointer<Void>)Removed iconv_hooks.init(uc_hook: iconv_unicode_char_hook!, wc_hook: iconv_wide_char_hook!, data: UnsafeMutablePointer<Void>)Removed if_clonereq.init(ifcr_total: Int32, ifcr_count: Int32, ifcr_buffer: UnsafeMutablePointer<Int8>)Removed if_data.init(ifi_type: u_char, ifi_typelen: u_char, ifi_physical: u_char, ifi_addrlen: u_char, ifi_hdrlen: u_char, ifi_recvquota: u_char, ifi_xmitquota: u_char, ifi_unused1: u_char, ifi_mtu: UInt32, ifi_metric: UInt32, ifi_baudrate: UInt32, ifi_ipackets: UInt32, ifi_ierrors: UInt32, ifi_opackets: UInt32, ifi_oerrors: UInt32, ifi_collisions: UInt32, ifi_ibytes: UInt32, ifi_obytes: UInt32, ifi_imcasts: UInt32, ifi_omcasts: UInt32, ifi_iqdrops: UInt32, ifi_noproto: UInt32, ifi_recvtiming: UInt32, ifi_xmittiming: UInt32, ifi_lastchange: timeval, ifi_unused2: UInt32, ifi_hwassist: UInt32, ifi_reserved1: UInt32, ifi_reserved2: UInt32)Removed if_data64.init(ifi_type: u_char, ifi_typelen: u_char, ifi_physical: u_char, ifi_addrlen: u_char, ifi_hdrlen: u_char, ifi_recvquota: u_char, ifi_xmitquota: u_char, ifi_unused1: u_char, ifi_mtu: UInt32, ifi_metric: UInt32, ifi_baudrate: UInt64, ifi_ipackets: UInt64, ifi_ierrors: UInt64, ifi_opackets: UInt64, ifi_oerrors: UInt64, ifi_collisions: UInt64, ifi_ibytes: UInt64, ifi_obytes: UInt64, ifi_imcasts: UInt64, ifi_omcasts: UInt64, ifi_iqdrops: UInt64, ifi_noproto: UInt64, ifi_recvtiming: UInt32, ifi_xmittiming: UInt32, ifi_lastchange: timeval)Removed if_nameindex.init(if_index: UInt32, if_name: UnsafeMutablePointer<Int8>)Removed ifdrv.init(ifd_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifd_cmd: UInt, ifd_len: Int, ifd_data: UnsafeMutablePointer<Void>)Removed ifmediareq.init(ifm_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifm_current: Int32, ifm_mask: Int32, ifm_status: Int32, ifm_active: Int32, ifm_count: Int32, ifm_ulist: UnsafeMutablePointer<Int32>)Removed ifqueue.init(ifq_head: UnsafeMutablePointer<Void>, ifq_tail: UnsafeMutablePointer<Void>, ifq_len: Int32, ifq_maxlen: Int32, ifq_drops: Int32)Removed iovec.init(iov_base: UnsafeMutablePointer<Void>, iov_len: Int)Removed kevent.init(ident: UInt, filter: Int16, flags: UInt16, fflags: UInt32, data: Int, udata: UnsafeMutablePointer<Void>)Removed klist.init(slh_first: COpaquePointer)Removed kmod_info.init(next: UnsafeMutablePointer<kmod_info>, info_version: Int32, id: UInt32, name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), version: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), reference_count: Int32, reference_list: UnsafeMutablePointer<kmod_reference_t>, address: vm_address_t, size: vm_size_t, hdr_size: vm_size_t, start: ((UnsafeMutablePointer<kmod_info>, UnsafeMutablePointer<Void>) -> kern_return_t)!, stop: ((UnsafeMutablePointer<kmod_info>, UnsafeMutablePointer<Void>) -> kern_return_t)!)Removed kmod_reference.init(next: UnsafeMutablePointer<kmod_reference>, info: UnsafeMutablePointer<kmod_info>)Removed lconv.init(decimal_point: UnsafeMutablePointer<Int8>, thousands_sep: UnsafeMutablePointer<Int8>, grouping: UnsafeMutablePointer<Int8>, int_curr_symbol: UnsafeMutablePointer<Int8>, currency_symbol: UnsafeMutablePointer<Int8>, mon_decimal_point: UnsafeMutablePointer<Int8>, mon_thousands_sep: UnsafeMutablePointer<Int8>, mon_grouping: UnsafeMutablePointer<Int8>, positive_sign: UnsafeMutablePointer<Int8>, negative_sign: UnsafeMutablePointer<Int8>, int_frac_digits: Int8, frac_digits: Int8, p_cs_precedes: Int8, p_sep_by_space: Int8, n_cs_precedes: Int8, n_sep_by_space: Int8, p_sign_posn: Int8, n_sign_posn: Int8, int_p_cs_precedes: Int8, int_n_cs_precedes: Int8, int_p_sep_by_space: Int8, int_n_sep_by_space: Int8, int_p_sign_posn: Int8, int_n_sign_posn: Int8)Removed mach_memory_info.init(flags: UInt64, site: UInt64, size: UInt64, free: UInt64, largest: UInt64, _resv: (UInt64, UInt64, UInt64))Removed mach_msg_ool_descriptor_t.init(address: UnsafeMutablePointer<Void>, size: mach_msg_size_t, deallocate: boolean_t, copy: mach_msg_copy_options_t, pad1: UInt32, type: mach_msg_descriptor_type_t)Removed mach_msg_ool_ports_descriptor_t.init(address: UnsafeMutablePointer<Void>, count: mach_msg_size_t, deallocate: boolean_t, copy: mach_msg_copy_options_t, disposition: mach_msg_type_name_t, type: mach_msg_descriptor_type_t)Removed MachError [enum]Removed MachError.KERN_ABORTEDRemoved MachError.KERN_ALREADY_IN_SETRemoved MachError.KERN_ALREADY_WAITINGRemoved MachError.KERN_CODESIGN_ERRORRemoved MachError.KERN_DEFAULT_SETRemoved MachError.KERN_EXCEPTION_PROTECTEDRemoved MachError.KERN_FAILURERemoved MachError.KERN_INVALID_ADDRESSRemoved MachError.KERN_INVALID_ARGUMENTRemoved MachError.KERN_INVALID_CAPABILITYRemoved MachError.KERN_INVALID_HOSTRemoved MachError.KERN_INVALID_LEDGERRemoved MachError.KERN_INVALID_MEMORY_CONTROLRemoved MachError.KERN_INVALID_NAMERemoved MachError.KERN_INVALID_OBJECTRemoved MachError.KERN_INVALID_POLICYRemoved MachError.KERN_INVALID_PROCESSOR_SETRemoved MachError.KERN_INVALID_RIGHTRemoved MachError.KERN_INVALID_SECURITYRemoved MachError.KERN_INVALID_TASKRemoved MachError.KERN_INVALID_VALUERemoved MachError.KERN_LOCK_OWNEDRemoved MachError.KERN_LOCK_OWNED_SELFRemoved MachError.KERN_LOCK_SET_DESTROYEDRemoved MachError.KERN_LOCK_UNSTABLERemoved MachError.KERN_MEMORY_DATA_MOVEDRemoved MachError.KERN_MEMORY_ERRORRemoved MachError.KERN_MEMORY_FAILURERemoved MachError.KERN_MEMORY_PRESENTRemoved MachError.KERN_MEMORY_RESTART_COPYRemoved MachError.KERN_NAME_EXISTSRemoved MachError.KERN_NO_ACCESSRemoved MachError.KERN_NO_SPACERemoved MachError.KERN_NODE_DOWNRemoved MachError.KERN_NOT_DEPRESSEDRemoved MachError.KERN_NOT_IN_SETRemoved MachError.KERN_NOT_RECEIVERRemoved MachError.KERN_NOT_SUPPORTEDRemoved MachError.KERN_NOT_WAITINGRemoved MachError.KERN_OPERATION_TIMED_OUTRemoved MachError.KERN_POLICY_LIMITRemoved MachError.KERN_POLICY_STATICRemoved MachError.KERN_PROTECTION_FAILURERemoved MachError.KERN_RESOURCE_SHORTAGERemoved MachError.KERN_RIGHT_EXISTSRemoved MachError.KERN_RPC_CONTINUE_ORPHANRemoved MachError.KERN_RPC_SERVER_TERMINATEDRemoved MachError.KERN_RPC_TERMINATE_ORPHANRemoved MachError.KERN_SEMAPHORE_DESTROYEDRemoved MachError.KERN_SUCCESSRemoved MachError.KERN_TERMINATEDRemoved MachError.KERN_UREFS_OVERFLOWRemoved malloc_introspection_t.init(enumerator: ((task_t, UnsafeMutablePointer<Void>, UInt32, vm_address_t, ((task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> kern_return_t)!, ((task_t, UnsafeMutablePointer<Void>, UInt32, UnsafeMutablePointer<vm_range_t>, UInt32) -> Void)!) -> kern_return_t)!, good_size: ((UnsafeMutablePointer<malloc_zone_t>, Int) -> Int)!, check: ((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)!, print: ((UnsafeMutablePointer<malloc_zone_t>, boolean_t) -> Void)!, log: ((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>) -> Void)!, force_lock: ((UnsafeMutablePointer<malloc_zone_t>) -> Void)!, force_unlock: ((UnsafeMutablePointer<malloc_zone_t>) -> Void)!, statistics: ((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<malloc_statistics_t>) -> Void)!, zone_locked: ((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)!, enable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)!, disable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>) -> Void)!, discharge: ((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>) -> Void)!, enumerate_discharged_pointers: ((UnsafeMutablePointer<malloc_zone_t>, ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)!) -> Void)!)Removed mig_subsystem.init(server: mig_server_routine_t!, start: mach_msg_id_t, end: mach_msg_id_t, maxsize: mach_msg_size_t, reserved: vm_address_t, routine: (mig_routine_descriptor))Removed mig_symtab.init(ms_routine_name: UnsafeMutablePointer<Int8>, ms_routine_number: Int32, ms_routine: (() -> Void)!)Removed msghdr.init(msg_name: UnsafeMutablePointer<Void>, msg_namelen: socklen_t, msg_iov: UnsafeMutablePointer<iovec>, msg_iovlen: Int32, msg_control: UnsafeMutablePointer<Void>, msg_controllen: socklen_t, msg_flags: Int32)Removed netent.init(n_name: UnsafeMutablePointer<Int8>, n_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, n_addrtype: Int32, n_net: UInt32)Removed option.init(name: UnsafePointer<Int8>, has_arg: Int32, flag: UnsafeMutablePointer<Int32>, val: Int32)Removed passwd.init(pw_name: UnsafeMutablePointer<Int8>, pw_passwd: UnsafeMutablePointer<Int8>, pw_uid: uid_t, pw_gid: gid_t, pw_change: __darwin_time_t, pw_class: UnsafeMutablePointer<Int8>, pw_gecos: UnsafeMutablePointer<Int8>, pw_dir: UnsafeMutablePointer<Int8>, pw_shell: UnsafeMutablePointer<Int8>, pw_expire: __darwin_time_t)Removed port_obj_tentry.init(pos_value: UnsafeMutablePointer<Void>, pos_type: Int32)Removed POSIXError [enum]Removed POSIXError.E2BIGRemoved POSIXError.EACCESRemoved POSIXError.EADDRINUSERemoved POSIXError.EADDRNOTAVAILRemoved POSIXError.EAFNOSUPPORTRemoved POSIXError.EAGAINRemoved POSIXError.EALREADYRemoved POSIXError.EAUTHRemoved POSIXError.EBADARCHRemoved POSIXError.EBADEXECRemoved POSIXError.EBADFRemoved POSIXError.EBADMACHORemoved POSIXError.EBADMSGRemoved POSIXError.EBADRPCRemoved POSIXError.EBUSYRemoved POSIXError.ECANCELEDRemoved POSIXError.ECHILDRemoved POSIXError.ECONNABORTEDRemoved POSIXError.ECONNREFUSEDRemoved POSIXError.ECONNRESETRemoved POSIXError.EDEADLKRemoved POSIXError.EDESTADDRREQRemoved POSIXError.EDEVERRRemoved POSIXError.EDOMRemoved POSIXError.EDQUOTRemoved POSIXError.EEXISTRemoved POSIXError.EFAULTRemoved POSIXError.EFBIGRemoved POSIXError.EFTYPERemoved POSIXError.EHOSTDOWNRemoved POSIXError.EHOSTUNREACHRemoved POSIXError.EIDRMRemoved POSIXError.EILSEQRemoved POSIXError.EINPROGRESSRemoved POSIXError.EINTRRemoved POSIXError.EINVALRemoved POSIXError.EIORemoved POSIXError.EISCONNRemoved POSIXError.EISDIRRemoved POSIXError.ELASTRemoved POSIXError.ELOOPRemoved POSIXError.EMFILERemoved POSIXError.EMLINKRemoved POSIXError.EMSGSIZERemoved POSIXError.EMULTIHOPRemoved POSIXError.ENAMETOOLONGRemoved POSIXError.ENEEDAUTHRemoved POSIXError.ENETDOWNRemoved POSIXError.ENETRESETRemoved POSIXError.ENETUNREACHRemoved POSIXError.ENFILERemoved POSIXError.ENOATTRRemoved POSIXError.ENOBUFSRemoved POSIXError.ENODATARemoved POSIXError.ENODEVRemoved POSIXError.ENOENTRemoved POSIXError.ENOEXECRemoved POSIXError.ENOLCKRemoved POSIXError.ENOLINKRemoved POSIXError.ENOMEMRemoved POSIXError.ENOMSGRemoved POSIXError.ENOPOLICYRemoved POSIXError.ENOPROTOOPTRemoved POSIXError.ENOSPCRemoved POSIXError.ENOSRRemoved POSIXError.ENOSTRRemoved POSIXError.ENOSYSRemoved POSIXError.ENOTBLKRemoved POSIXError.ENOTCONNRemoved POSIXError.ENOTDIRRemoved POSIXError.ENOTEMPTYRemoved POSIXError.ENOTRECOVERABLERemoved POSIXError.ENOTSOCKRemoved POSIXError.ENOTSUPRemoved POSIXError.ENOTTYRemoved POSIXError.ENXIORemoved POSIXError.EOVERFLOWRemoved POSIXError.EOWNERDEADRemoved POSIXError.EPERMRemoved POSIXError.EPFNOSUPPORTRemoved POSIXError.EPIPERemoved POSIXError.EPROCLIMRemoved POSIXError.EPROCUNAVAILRemoved POSIXError.EPROGMISMATCHRemoved POSIXError.EPROGUNAVAILRemoved POSIXError.EPROTORemoved POSIXError.EPROTONOSUPPORTRemoved POSIXError.EPROTOTYPERemoved POSIXError.EPWROFFRemoved POSIXError.EQFULLRemoved POSIXError.ERANGERemoved POSIXError.EREMOTERemoved POSIXError.EROFSRemoved POSIXError.ERPCMISMATCHRemoved POSIXError.ESHLIBVERSRemoved POSIXError.ESHUTDOWNRemoved POSIXError.ESOCKTNOSUPPORTRemoved POSIXError.ESPIPERemoved POSIXError.ESRCHRemoved POSIXError.ESTALERemoved POSIXError.ETIMERemoved POSIXError.ETIMEDOUTRemoved POSIXError.ETOOMANYREFSRemoved POSIXError.ETXTBSYRemoved POSIXError.EUSERSRemoved POSIXError.EWOULDBLOCKRemoved POSIXError.EXDEVRemoved protoent.init(p_name: UnsafeMutablePointer<Int8>, p_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, p_proto: Int32)Removed rb_node.init(opaque: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>))Removed rb_tree.init(opaque: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>))Removed rb_tree_ops_t.init(rbto_compare_nodes: rbto_compare_nodes_fn!, rbto_compare_key: rbto_compare_key_fn!, rbto_node_offset: Int, rbto_context: UnsafeMutablePointer<Void>)Removed routine_descriptor.init(impl_routine: mig_impl_routine_t!, stub_routine: mig_stub_routine_t!, argc: UInt32, descr_count: UInt32, arg_descr: routine_arg_descriptor_t, max_reply_msg: UInt32)Removed rpc_routine_descriptor.init(impl_routine: mig_impl_routine_t!, stub_routine: mig_stub_routine_t!, argc: UInt32, descr_count: UInt32, arg_descr: rpc_routine_arg_descriptor_t, max_reply_msg: UInt32)Removed rpc_subsystem.init(reserved: UnsafeMutablePointer<Void>, start: mach_msg_id_t, end: mach_msg_id_t, maxsize: UInt32, base_addr: vm_address_t, routine: (rpc_routine_descriptor), arg_descriptor: (rpc_routine_arg_descriptor))Removed rpcent.init(r_name: UnsafeMutablePointer<Int8>, r_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, r_number: Int32)Removed rslvmulti_req.init(sa: UnsafeMutablePointer<sockaddr>, llsa: UnsafeMutablePointer<UnsafeMutablePointer<sockaddr>>)Removed sa_endpoints.init(sae_srcif: UInt32, sae_srcaddr: UnsafeMutablePointer<sockaddr>, sae_srcaddrlen: socklen_t, sae_dstaddr: UnsafeMutablePointer<sockaddr>, sae_dstaddrlen: socklen_t)Removed semun.init(array: UnsafeMutablePointer<UInt16>)Removed semun.init(buf: UnsafeMutablePointer<__semid_ds_new>)Removed servent.init(s_name: UnsafeMutablePointer<Int8>, s_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, s_port: Int32, s_proto: UnsafeMutablePointer<Int8>)Removed sf_hdtr.init(headers: UnsafeMutablePointer<iovec>, hdr_cnt: Int32, trailers: UnsafeMutablePointer<iovec>, trl_cnt: Int32)Removed sigevent.init(sigev_notify: Int32, sigev_signo: Int32, sigev_value: sigval, sigev_notify_function: ((sigval) -> Void)!, sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t>)Removed sigstack.init(ss_sp: UnsafeMutablePointer<Int8>, ss_onstack: Int32)Removed sigval.init(sival_ptr: UnsafeMutablePointer<Void>)Removed task_power_info_v2.init(cpu_energy: task_power_info_data_t, gpu_energy: gpu_energy_data)Removed task_vm_info.init(virtual_size: mach_vm_size_t, region_count: integer_t, page_size: integer_t, resident_size: mach_vm_size_t, resident_size_peak: mach_vm_size_t, device: mach_vm_size_t, device_peak: mach_vm_size_t, internal: mach_vm_size_t, internal_peak: mach_vm_size_t, external: mach_vm_size_t, external_peak: mach_vm_size_t, reusable: mach_vm_size_t, reusable_peak: mach_vm_size_t, purgeable_volatile_pmap: mach_vm_size_t, purgeable_volatile_resident: mach_vm_size_t, purgeable_volatile_virtual: mach_vm_size_t, compressed: mach_vm_size_t, compressed_peak: mach_vm_size_t, compressed_lifetime: mach_vm_size_t, phys_footprint: mach_vm_size_t)Removed tcp_connection_info.init(tcpi_state: UInt8, tcpi_snd_wscale: UInt8, tcpi_rcv_wscale: UInt8, __pad1: UInt8, tcpi_options: UInt32, tcpi_flags: UInt32, tcpi_rto: UInt32, tcpi_maxseg: UInt32, tcpi_snd_ssthresh: UInt32, tcpi_snd_cwnd: UInt32, tcpi_snd_wnd: UInt32, tcpi_snd_sbbytes: UInt32, tcpi_rcv_wnd: UInt32, tcpi_rttcur: UInt32, tcpi_srtt: UInt32, tcpi_rttvar: UInt32, tcpi_tfo_cookie_req: UInt32, tcpi_tfo_cookie_rcv: UInt32, tcpi_tfo_syn_loss: UInt32, tcpi_tfo_syn_data_sent: UInt32, tcpi_tfo_syn_data_acked: UInt32, tcpi_tfo_syn_data_rcv: UInt32, tcpi_tfo_cookie_req_rcv: UInt32, tcpi_tfo_cookie_sent: UInt32, tcpi_tfo_cookie_invalid: UInt32, __pad2: UInt32, tcpi_txpackets: UInt64, tcpi_txbytes: UInt64, tcpi_txretransmitbytes: UInt64, tcpi_rxpackets: UInt64, tcpi_rxbytes: UInt64, tcpi_rxoutoforderbytes: UInt64)Removed tm.init(tm_sec: Int32, tm_min: Int32, tm_hour: Int32, tm_mday: Int32, tm_mon: Int32, tm_year: Int32, tm_wday: Int32, tm_yday: Int32, tm_isdst: Int32, tm_gmtoff: Int, tm_zone: UnsafeMutablePointer<Int8>)Removed ucred.init(cr_link: ucred.__Unnamed_struct_cr_link, cr_ref: u_long, cr_posix: posix_cred, cr_label: COpaquePointer, cr_audit: au_session)Removed vfsidctl.init(vc_vers: Int32, vc_fsid: fsid_t, vc_ptr: UnsafeMutablePointer<Void>, vc_len: Int, vc_spare: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32))Removed vfsstatfs.init(f_bsize: UInt32, f_iosize: Int, f_blocks: UInt64, f_bfree: UInt64, f_bavail: UInt64, f_bused: UInt64, f_files: UInt64, f_ffree: UInt64, f_fsid: fsid_t, f_owner: uid_t, f_flags: UInt64, f_fstypename: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), f_mntonname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), f_mntfromname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), f_fssubtype: UInt32, f_reserved: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>))Removed vmspace.init(dummy: Int32, dummy2: caddr_t, dummy3: (Int32, Int32, Int32, Int32, Int32), dummy4: (caddr_t, caddr_t, caddr_t))Removed wordexp_t.init(we_wordc: Int, we_wordv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, we_offs: Int)Removed &&(_: T, _: () -> DarwinBoolean) -> BoolRemoved ceil(_: Float) -> FloatRemoved ceil(_: Double) -> DoubleRemoved CPUFAMILY_INTEL_6_14Removed CPUFAMILY_INTEL_6_15Removed CPUFAMILY_INTEL_CORERemoved CPUFAMILY_INTEL_CORE2Removed CPUFAMILY_INTEL_MEROMRemoved CPUFAMILY_INTEL_YONAHRemoved fabs(_: Double) -> DoubleRemoved fabs(_: Float) -> FloatRemoved fcntl(_: CInt, _: CInt, _: UnsafeMutablePointer<Void>) -> CIntRemoved floor(_: Float) -> FloatRemoved floor(_: Double) -> DoubleRemoved fma(_: Float, _: Float, _: Float) -> FloatRemoved fmod(_: Float, _: Float) -> FloatRemoved isfinite(_: Float) -> BoolRemoved isfinite(_: Double) -> BoolRemoved isinf(_: Float) -> BoolRemoved isinf(_: Double) -> BoolRemoved isnan(_: Float) -> BoolRemoved isnan(_: Double) -> BoolRemoved isnormal(_: Double) -> BoolRemoved isnormal(_: Float) -> BoolRemoved jrand48(_: UnsafeMutablePointer<UInt16>) -> IntRemoved KERN_KDDISABLE_BG_TRACERemoved KERN_KDENABLE_BG_TRACERemoved KERN_KDSET_BG_TYPEFILTERRemoved KERN_KDWAIT_BG_TRACE_RESETRemoved lrand48() -> IntRemoved mrand48() -> IntRemoved nrand48(_: UnsafeMutablePointer<UInt16>) -> IntRemoved P_DIRTY_DEFER_IN_PROGRESSRemoved pclose(_: UnsafeMutablePointer<FILE>) -> Int32Removed popen(_: UnsafePointer<Int8>, _: UnsafePointer<Int8>) -> UnsafeMutablePointer<FILE>Removed pthread_once(_: UnsafeMutablePointer<pthread_once_t>, _: (() -> Void)!) -> Int32Removed rand() -> Int32Removed rand_r(_: UnsafeMutablePointer<UInt32>) -> Int32Removed random() -> IntRemoved remainder(_: Float, _: Float) -> FloatRemoved round(_: Float) -> FloatRemoved round(_: Double) -> DoubleRemoved sem_open(_: UnsafePointer<CChar>, _: CInt) -> UnsafeMutablePointer<sem_t>Removed sem_open(_: UnsafePointer<CChar>, _: CInt, _: mode_t, _: CUnsignedInt) -> UnsafeMutablePointer<sem_t>Removed signbit(_: Double) -> IntRemoved signbit(_: Float) -> IntRemoved sqrt(_: Float) -> FloatRemoved srand(_: UInt32)Removed SYS_chudRemoved SYS_rename_extRemoved SYS_stack_snapshotRemoved system(_: UnsafePointer<Int8>) -> Int32Removed tempnam(_: UnsafePointer<Int8>, _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8>Removed tmpnam(_: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8>Removed trunc(_: Float) -> FloatRemoved trunc(_: Double) -> DoubleRemoved vsprintf(_: UnsafeMutablePointer<Int8>, _: UnsafePointer<Int8>, _: CVaListPointer) -> Int32Removed vsprintf_l(_: UnsafeMutablePointer<Int8>, _: locale_t, _: UnsafePointer<Int8>, _: CVaListPointer) -> Int32Removed ||(_: T, _: () -> DarwinBoolean) -> BoolAdded addrinfo.init(ai_flags: Int32, ai_family: Int32, ai_socktype: Int32, ai_protocol: Int32, ai_addrlen: socklen_t, ai_canonname: UnsafeMutablePointer<Int8>!, ai_addr: UnsafeMutablePointer<sockaddr>!, ai_next: UnsafeMutablePointer<addrinfo>!)Added aiocb.init(aio_fildes: Int32, aio_offset: off_t, aio_buf: UnsafeMutableRawPointer!, aio_nbytes: Int, aio_reqprio: Int32, aio_sigevent: sigevent, aio_lio_opcode: Int32)Added arm_legacy_debug_state [struct]Added arm_legacy_debug_state.init()Added arm_legacy_debug_state.init(__bvr: (__uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t), __bcr: (__uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t), __wvr: (__uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t), __wcr: (__uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t))Added atomic_flag [struct]Added atomic_flag.init()Added au_session.init(as_aia_p: UnsafeMutablePointer<auditinfo_addr_t>!, as_mask: au_mask_t)Added clockid_t [struct]Added clockid_t.init(_: UInt32)Added clockid_t.init(rawValue: UInt32)Added clockid_t.rawValueAdded ctlname.init(ctl_name: UnsafeMutablePointer<Int8>!, ctl_type: Int32)Added DarwinBoolean.customMirrorAdded datum.init(dptr: UnsafeMutableRawPointer!, dsize: Int)Added DBM.init(__opaque: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added DIR.init(__dd_fd: Int32, __dd_loc: Int, __dd_size: Int, __dd_buf: UnsafeMutablePointer<Int8>!, __dd_len: Int32, __dd_seek: Int, __dd_rewind: Int, __dd_flags: Int32, __dd_lock: __darwin_pthread_mutex_t, __dd_td: OpaquePointer!)Added dl_info.init(dli_fname: UnsafePointer<Int8>!, dli_fbase: UnsafeMutableRawPointer!, dli_sname: UnsafePointer<Int8>!, dli_saddr: UnsafeMutableRawPointer!)Added dyld_kernel_image_info [struct]Added dyld_kernel_image_info.fsidAdded dyld_kernel_image_info.fsobjidAdded dyld_kernel_image_info.init()Added dyld_kernel_image_info.init(uuid: Darwin.uuid_t, fsobjid: fsobj_id_t, fsid: fsid_t, load_addr: UInt64)Added dyld_kernel_image_info.load_addrAdded dyld_kernel_image_info.uuidAdded dyld_kernel_process_info [struct]Added dyld_kernel_process_info.cache_image_infoAdded dyld_kernel_process_info.dyldStateAdded dyld_kernel_process_info.imageCountAdded dyld_kernel_process_info.init()Added dyld_kernel_process_info.init(cache_image_info: dyld_kernel_image_info, timestamp: UInt64, imageCount: UInt32, initialImageCount: UInt32, dyldState: UInt8, no_cache: boolean_t, private_cache: boolean_t)Added dyld_kernel_process_info.initialImageCountAdded dyld_kernel_process_info.no_cacheAdded dyld_kernel_process_info.private_cacheAdded dyld_kernel_process_info.timestampAdded entry.init(key: UnsafeMutablePointer<Int8>!, data: UnsafeMutableRawPointer!)Added eproc.init(e_paddr: OpaquePointer!, e_sess: OpaquePointer!, e_pcred: _pcred, e_ucred: _ucred, e_vm: vmspace, e_ppid: pid_t, e_pgid: pid_t, e_jobc: Int16, e_tdev: dev_t, e_tpgid: pid_t, e_tsess: OpaquePointer!, e_wmesg: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), e_xsize: segsz_t, e_xrssize: Int16, e_xccount: Int16, e_xswrss: Int16, e_flag: Int32, e_login: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), e_spare: (Int32, Int32, Int32, Int32))Added exception.init(type: Int32, name: UnsafeMutablePointer<Int8>!, arg1: Double, arg2: Double, retval: Double)Added fbootstraptransfer.init(fbt_offset: off_t, fbt_length: Int, fbt_buffer: UnsafeMutableRawPointer!)Added fchecklv [struct]Added fchecklv.init()Added fchecklv.init(lv_file_start: off_t, lv_error_message_size: Int, lv_error_message: UnsafeMutableRawPointer!)Added fchecklv.lv_error_messageAdded fchecklv.lv_error_message_sizeAdded fchecklv.lv_file_startAdded fcodeblobs.init(f_cd_hash: UnsafeMutableRawPointer!, f_hash_size: Int, f_cd_buffer: UnsafeMutableRawPointer!, f_cd_size: Int, f_out_size: UnsafeMutablePointer<UInt32>!, f_arch: Int32, __padding: Int32)Added fenv_t.init(__fpsr: UInt64, __fpcr: UInt64)Added fsignatures.init(fs_file_start: off_t, fs_blob_start: UnsafeMutableRawPointer!, fs_blob_size: Int)Added fssearchblock.init(returnattrs: UnsafeMutablePointer<attrlist>!, returnbuffer: UnsafeMutableRawPointer!, returnbuffersize: Int, maxmatches: u_long, timelimit: timeval, searchparams1: UnsafeMutableRawPointer!, sizeofsearchparams1: Int, searchparams2: UnsafeMutableRawPointer!, sizeofsearchparams2: Int, searchattrs: attrlist)Added group.init(gr_name: UnsafeMutablePointer<Int8>!, gr_passwd: UnsafeMutablePointer<Int8>!, gr_gid: gid_t, gr_mem: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!)Added host_can_has_debugger_info [struct]Added host_can_has_debugger_info.can_has_debuggerAdded host_can_has_debugger_info.init()Added host_can_has_debugger_info.init(can_has_debugger: boolean_t)Added hostent.init(h_name: UnsafeMutablePointer<Int8>!, h_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, h_addrtype: Int32, h_length: Int32, h_addr_list: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!)Added iconv_fallbacks.init(mb_to_uc_fallback: Darwin.iconv_unicode_mb_to_uc_fallback!, uc_to_mb_fallback: Darwin.iconv_unicode_uc_to_mb_fallback!, mb_to_wc_fallback: Darwin.iconv_wchar_mb_to_wc_fallback!, wc_to_mb_fallback: Darwin.iconv_wchar_wc_to_mb_fallback!, data: UnsafeMutableRawPointer!)Added iconv_hooks.init(uc_hook: Darwin.iconv_unicode_char_hook!, wc_hook: Darwin.iconv_wide_char_hook!, data: UnsafeMutableRawPointer!)Added if_clonereq.init(ifcr_total: Int32, ifcr_count: Int32, ifcr_buffer: UnsafeMutablePointer<Int8>!)Added if_data.init(ifi_type: u_char, ifi_typelen: u_char, ifi_physical: u_char, ifi_addrlen: u_char, ifi_hdrlen: u_char, ifi_recvquota: u_char, ifi_xmitquota: u_char, ifi_unused1: u_char, ifi_mtu: UInt32, ifi_metric: UInt32, ifi_baudrate: UInt32, ifi_ipackets: UInt32, ifi_ierrors: UInt32, ifi_opackets: UInt32, ifi_oerrors: UInt32, ifi_collisions: UInt32, ifi_ibytes: UInt32, ifi_obytes: UInt32, ifi_imcasts: UInt32, ifi_omcasts: UInt32, ifi_iqdrops: UInt32, ifi_noproto: UInt32, ifi_recvtiming: UInt32, ifi_xmittiming: UInt32, ifi_lastchange: timeval32, ifi_unused2: UInt32, ifi_hwassist: UInt32, ifi_reserved1: UInt32, ifi_reserved2: UInt32)Added if_data64.init(ifi_type: u_char, ifi_typelen: u_char, ifi_physical: u_char, ifi_addrlen: u_char, ifi_hdrlen: u_char, ifi_recvquota: u_char, ifi_xmitquota: u_char, ifi_unused1: u_char, ifi_mtu: UInt32, ifi_metric: UInt32, ifi_baudrate: UInt64, ifi_ipackets: UInt64, ifi_ierrors: UInt64, ifi_opackets: UInt64, ifi_oerrors: UInt64, ifi_collisions: UInt64, ifi_ibytes: UInt64, ifi_obytes: UInt64, ifi_imcasts: UInt64, ifi_omcasts: UInt64, ifi_iqdrops: UInt64, ifi_noproto: UInt64, ifi_recvtiming: UInt32, ifi_xmittiming: UInt32, ifi_lastchange: timeval32)Added if_nameindex.init(if_index: UInt32, if_name: UnsafeMutablePointer<Int8>!)Added ifdrv.init(ifd_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifd_cmd: UInt, ifd_len: Int, ifd_data: UnsafeMutableRawPointer!)Added ifmediareq.init(ifm_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifm_current: Int32, ifm_mask: Int32, ifm_status: Int32, ifm_active: Int32, ifm_count: Int32, ifm_ulist: UnsafeMutablePointer<Int32>!)Added ifqueue.init(ifq_head: UnsafeMutableRawPointer!, ifq_tail: UnsafeMutableRawPointer!, ifq_len: Int32, ifq_maxlen: Int32, ifq_drops: Int32)Added iovec.init(iov_base: UnsafeMutableRawPointer!, iov_len: Int)Added kevent.init(ident: UInt, filter: Int16, flags: UInt16, fflags: UInt32, data: Int, udata: UnsafeMutableRawPointer!)Added klist.init(slh_first: OpaquePointer!)Added kmod_info.init(next: UnsafeMutablePointer<kmod_info>!, info_version: Int32, id: UInt32, name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), version: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), reference_count: Int32, reference_list: UnsafeMutablePointer<kmod_reference_t>!, address: vm_address_t, size: vm_size_t, hdr_size: vm_size_t, start: ( (UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!, stop: ( (UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!)Added kmod_reference.init(next: UnsafeMutablePointer<kmod_reference>!, info: UnsafeMutablePointer<kmod_info>!)Added lconv.init(decimal_point: UnsafeMutablePointer<Int8>!, thousands_sep: UnsafeMutablePointer<Int8>!, grouping: UnsafeMutablePointer<Int8>!, int_curr_symbol: UnsafeMutablePointer<Int8>!, currency_symbol: UnsafeMutablePointer<Int8>!, mon_decimal_point: UnsafeMutablePointer<Int8>!, mon_thousands_sep: UnsafeMutablePointer<Int8>!, mon_grouping: UnsafeMutablePointer<Int8>!, positive_sign: UnsafeMutablePointer<Int8>!, negative_sign: UnsafeMutablePointer<Int8>!, int_frac_digits: Int8, frac_digits: Int8, p_cs_precedes: Int8, p_sep_by_space: Int8, n_cs_precedes: Int8, n_sep_by_space: Int8, p_sign_posn: Int8, n_sign_posn: Int8, int_p_cs_precedes: Int8, int_n_cs_precedes: Int8, int_p_sep_by_space: Int8, int_n_sep_by_space: Int8, int_p_sign_posn: Int8, int_n_sign_posn: Int8)Added mach_memory_info.collectable_bytesAdded mach_memory_info.init(flags: UInt64, site: UInt64, size: UInt64, free: UInt64, largest: UInt64, collectable_bytes: UInt64, _resv: (UInt64, UInt64))Added mach_msg_ool_descriptor_t.init(address: UnsafeMutableRawPointer!, deallocate: boolean_t, copy: mach_msg_copy_options_t, pad1: UInt32, type: mach_msg_descriptor_type_t, size: mach_msg_size_t)Added mach_msg_ool_ports_descriptor_t.init(address: UnsafeMutableRawPointer!, deallocate: boolean_t, copy: mach_msg_copy_options_t, disposition: mach_msg_type_name_t, type: mach_msg_descriptor_type_t, count: mach_msg_size_t)Added MachErrorCode [enum]Added MachErrorCode.abortedAdded MachErrorCode.alreadyInSetAdded MachErrorCode.alreadyWaitingAdded MachErrorCode.codesignErrorAdded MachErrorCode.defaultSetAdded MachErrorCode.exceptionProtectedAdded MachErrorCode.failureAdded MachErrorCode.invalidAddressAdded MachErrorCode.invalidArgumentAdded MachErrorCode.invalidCapabilityAdded MachErrorCode.invalidHostAdded MachErrorCode.invalidLedgerAdded MachErrorCode.invalidMemoryControlAdded MachErrorCode.invalidNameAdded MachErrorCode.invalidObjectAdded MachErrorCode.invalidPolicyAdded MachErrorCode.invalidProcessorSetAdded MachErrorCode.invalidRightAdded MachErrorCode.invalidSecurityAdded MachErrorCode.invalidTaskAdded MachErrorCode.invalidValueAdded MachErrorCode.lockOwnedAdded MachErrorCode.lockOwnedSelfAdded MachErrorCode.lockSetDestroyedAdded MachErrorCode.lockUnstableAdded MachErrorCode.memoryDataMovedAdded MachErrorCode.memoryErrorAdded MachErrorCode.memoryFailureAdded MachErrorCode.memoryPresentAdded MachErrorCode.memoryRestartCopyAdded MachErrorCode.nameExistsAdded MachErrorCode.noAccessAdded MachErrorCode.nodeDownAdded MachErrorCode.noSpaceAdded MachErrorCode.notDepressedAdded MachErrorCode.notInSetAdded MachErrorCode.notReceiverAdded MachErrorCode.notSupportedAdded MachErrorCode.notWaitingAdded MachErrorCode.operationTimedOutAdded MachErrorCode.policyLimitAdded MachErrorCode.policyStaticAdded MachErrorCode.protectionFailureAdded MachErrorCode.resourceShortageAdded MachErrorCode.rightExistsAdded MachErrorCode.rpcContinueOrphanAdded MachErrorCode.rpcServerTerminatedAdded MachErrorCode.rpcTerminateOrphanAdded MachErrorCode.semaphoreDestroyedAdded MachErrorCode.successAdded MachErrorCode.terminatedAdded MachErrorCode.userReferencesOverflowAdded malloc_introspection_t.init(enumerator: ( (task_t, UnsafeMutableRawPointer?, UInt32, vm_address_t, ( (task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)?, ( (task_t, UnsafeMutableRawPointer?, UInt32, UnsafeMutablePointer<vm_range_t>?, UInt32) -> Swift.Void)?) -> kern_return_t)!, good_size: ( (UnsafeMutablePointer<malloc_zone_t>?, Int) -> Int)!, check: ( (UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, print: ( (UnsafeMutablePointer<malloc_zone_t>?, boolean_t) -> Swift.Void)!, log: ( (UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!, force_lock: ( (UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, force_unlock: ( (UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, statistics: ( (UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutablePointer<malloc_statistics_t>?) -> Swift.Void)!, zone_locked: ( (UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, enable_discharge_checking: ( (UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, disable_discharge_checking: ( (UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, discharge: ( (UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!, enumerate_discharged_pointers: ( (UnsafeMutablePointer<malloc_zone_t>?, ( (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)?) -> Swift.Void)!, reinit_lock: ( (UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!)Added malloc_introspection_t.reinit_lockAdded memory_order [struct]Added memory_order.init(_: UInt32)Added memory_order.init(rawValue: UInt32)Added memory_order.rawValueAdded mig_subsystem.init(server: Darwin.mig_server_routine_t!, start: mach_msg_id_t, end: mach_msg_id_t, maxsize: mach_msg_size_t, reserved: vm_address_t, routine: (mig_routine_descriptor))Added mig_symtab.init(ms_routine_name: UnsafeMutablePointer<Int8>!, ms_routine_number: Int32, ms_routine: ( () -> Swift.Void)!)Added msghdr.init(msg_name: UnsafeMutableRawPointer!, msg_namelen: socklen_t, msg_iov: UnsafeMutablePointer<iovec>!, msg_iovlen: Int32, msg_control: UnsafeMutableRawPointer!, msg_controllen: socklen_t, msg_flags: Int32)Added netent.init(n_name: UnsafeMutablePointer<Int8>!, n_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, n_addrtype: Int32, n_net: UInt32)Added option.init(name: UnsafePointer<Int8>!, has_arg: Int32, flag: UnsafeMutablePointer<Int32>!, val: Int32)Added os_unfair_lock_s [struct]Added os_unfair_lock_s.init()Added os_unfair_lock_s.init(_os_unfair_lock_opaque: UInt32)Added passwd.init(pw_name: UnsafeMutablePointer<Int8>!, pw_passwd: UnsafeMutablePointer<Int8>!, pw_uid: uid_t, pw_gid: gid_t, pw_change: __darwin_time_t, pw_class: UnsafeMutablePointer<Int8>!, pw_gecos: UnsafeMutablePointer<Int8>!, pw_dir: UnsafeMutablePointer<Int8>!, pw_shell: UnsafeMutablePointer<Int8>!, pw_expire: __darwin_time_t)Added port_obj_tentry.init(pos_value: UnsafeMutableRawPointer!, pos_type: Int32)Added POSIXErrorCode [enum]Added POSIXErrorCode.E2BIGAdded POSIXErrorCode.EACCESAdded POSIXErrorCode.EADDRINUSEAdded POSIXErrorCode.EADDRNOTAVAILAdded POSIXErrorCode.EAFNOSUPPORTAdded POSIXErrorCode.EAGAINAdded POSIXErrorCode.EALREADYAdded POSIXErrorCode.EAUTHAdded POSIXErrorCode.EBADARCHAdded POSIXErrorCode.EBADEXECAdded POSIXErrorCode.EBADFAdded POSIXErrorCode.EBADMACHOAdded POSIXErrorCode.EBADMSGAdded POSIXErrorCode.EBADRPCAdded POSIXErrorCode.EBUSYAdded POSIXErrorCode.ECANCELEDAdded POSIXErrorCode.ECHILDAdded POSIXErrorCode.ECONNABORTEDAdded POSIXErrorCode.ECONNREFUSEDAdded POSIXErrorCode.ECONNRESETAdded POSIXErrorCode.EDEADLKAdded POSIXErrorCode.EDESTADDRREQAdded POSIXErrorCode.EDEVERRAdded POSIXErrorCode.EDOMAdded POSIXErrorCode.EDQUOTAdded POSIXErrorCode.EEXISTAdded POSIXErrorCode.EFAULTAdded POSIXErrorCode.EFBIGAdded POSIXErrorCode.EFTYPEAdded POSIXErrorCode.EHOSTDOWNAdded POSIXErrorCode.EHOSTUNREACHAdded POSIXErrorCode.EIDRMAdded POSIXErrorCode.EILSEQAdded POSIXErrorCode.EINPROGRESSAdded POSIXErrorCode.EINTRAdded POSIXErrorCode.EINVALAdded POSIXErrorCode.EIOAdded POSIXErrorCode.EISCONNAdded POSIXErrorCode.EISDIRAdded POSIXErrorCode.ELASTAdded POSIXErrorCode.ELOOPAdded POSIXErrorCode.EMFILEAdded POSIXErrorCode.EMLINKAdded POSIXErrorCode.EMSGSIZEAdded POSIXErrorCode.EMULTIHOPAdded POSIXErrorCode.ENAMETOOLONGAdded POSIXErrorCode.ENEEDAUTHAdded POSIXErrorCode.ENETDOWNAdded POSIXErrorCode.ENETRESETAdded POSIXErrorCode.ENETUNREACHAdded POSIXErrorCode.ENFILEAdded POSIXErrorCode.ENOATTRAdded POSIXErrorCode.ENOBUFSAdded POSIXErrorCode.ENODATAAdded POSIXErrorCode.ENODEVAdded POSIXErrorCode.ENOENTAdded POSIXErrorCode.ENOEXECAdded POSIXErrorCode.ENOLCKAdded POSIXErrorCode.ENOLINKAdded POSIXErrorCode.ENOMEMAdded POSIXErrorCode.ENOMSGAdded POSIXErrorCode.ENOPOLICYAdded POSIXErrorCode.ENOPROTOOPTAdded POSIXErrorCode.ENOSPCAdded POSIXErrorCode.ENOSRAdded POSIXErrorCode.ENOSTRAdded POSIXErrorCode.ENOSYSAdded POSIXErrorCode.ENOTBLKAdded POSIXErrorCode.ENOTCONNAdded POSIXErrorCode.ENOTDIRAdded POSIXErrorCode.ENOTEMPTYAdded POSIXErrorCode.ENOTRECOVERABLEAdded POSIXErrorCode.ENOTSOCKAdded POSIXErrorCode.ENOTSUPAdded POSIXErrorCode.ENOTTYAdded POSIXErrorCode.ENXIOAdded POSIXErrorCode.EOVERFLOWAdded POSIXErrorCode.EOWNERDEADAdded POSIXErrorCode.EPERMAdded POSIXErrorCode.EPFNOSUPPORTAdded POSIXErrorCode.EPIPEAdded POSIXErrorCode.EPROCLIMAdded POSIXErrorCode.EPROCUNAVAILAdded POSIXErrorCode.EPROGMISMATCHAdded POSIXErrorCode.EPROGUNAVAILAdded POSIXErrorCode.EPROTOAdded POSIXErrorCode.EPROTONOSUPPORTAdded POSIXErrorCode.EPROTOTYPEAdded POSIXErrorCode.EPWROFFAdded POSIXErrorCode.EQFULLAdded POSIXErrorCode.ERANGEAdded POSIXErrorCode.EREMOTEAdded POSIXErrorCode.EROFSAdded POSIXErrorCode.ERPCMISMATCHAdded POSIXErrorCode.ESHLIBVERSAdded POSIXErrorCode.ESHUTDOWNAdded POSIXErrorCode.ESOCKTNOSUPPORTAdded POSIXErrorCode.ESPIPEAdded POSIXErrorCode.ESRCHAdded POSIXErrorCode.ESTALEAdded POSIXErrorCode.ETIMEAdded POSIXErrorCode.ETIMEDOUTAdded POSIXErrorCode.ETOOMANYREFSAdded POSIXErrorCode.ETXTBSYAdded POSIXErrorCode.EUSERSAdded POSIXErrorCode.EWOULDBLOCKAdded POSIXErrorCode.EXDEVAdded protoent.init(p_name: UnsafeMutablePointer<Int8>!, p_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, p_proto: Int32)Added rb_node.init(opaque: (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?))Added rb_tree.init(opaque: (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?))Added rb_tree_ops_t.init(rbto_compare_nodes: Darwin.rbto_compare_nodes_fn!, rbto_compare_key: Darwin.rbto_compare_key_fn!, rbto_node_offset: Int, rbto_context: UnsafeMutableRawPointer!)Added routine_descriptor.init(impl_routine: Darwin.mig_impl_routine_t!, stub_routine: Darwin.mig_stub_routine_t!, argc: UInt32, descr_count: UInt32, arg_descr: routine_arg_descriptor_t!, max_reply_msg: UInt32)Added rpc_routine_descriptor.init(impl_routine: Darwin.mig_impl_routine_t!, stub_routine: Darwin.mig_stub_routine_t!, argc: UInt32, descr_count: UInt32, arg_descr: rpc_routine_arg_descriptor_t!, max_reply_msg: UInt32)Added rpc_subsystem.init(reserved: UnsafeMutableRawPointer!, start: mach_msg_id_t, end: mach_msg_id_t, maxsize: UInt32, base_addr: vm_address_t, routine: (rpc_routine_descriptor), arg_descriptor: (rpc_routine_arg_descriptor))Added rpcent.init(r_name: UnsafeMutablePointer<Int8>!, r_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, r_number: Int32)Added rslvmulti_req.init(sa: UnsafeMutablePointer<sockaddr>!, llsa: UnsafeMutablePointer<UnsafeMutablePointer<sockaddr>?>!)Added sa_endpoints.init(sae_srcif: UInt32, sae_srcaddr: UnsafePointer<sockaddr>!, sae_srcaddrlen: socklen_t, sae_dstaddr: UnsafePointer<sockaddr>!, sae_dstaddrlen: socklen_t)Added semun.init(array: UnsafeMutablePointer<UInt16>!)Added semun.init(buf: UnsafeMutablePointer<__semid_ds_new>!)Added servent.init(s_name: UnsafeMutablePointer<Int8>!, s_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, s_port: Int32, s_proto: UnsafeMutablePointer<Int8>!)Added sf_hdtr.init(headers: UnsafeMutablePointer<iovec>!, hdr_cnt: Int32, trailers: UnsafeMutablePointer<iovec>!, trl_cnt: Int32)Added sigevent.init(sigev_notify: Int32, sigev_signo: Int32, sigev_value: sigval, sigev_notify_function: ( (sigval) -> Swift.Void)!, sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t>!)Added sigstack.init(ss_sp: UnsafeMutablePointer<Int8>!, ss_onstack: Int32)Added sigval.init(sival_ptr: UnsafeMutableRawPointer!)Added task_power_info_v2.init(cpu_energy: task_power_info_data_t, gpu_energy: gpu_energy_data, task_energy: UInt64)Added task_power_info_v2.task_energyAdded task_vm_info.init(virtual_size: mach_vm_size_t, region_count: integer_t, page_size: integer_t, resident_size: mach_vm_size_t, resident_size_peak: mach_vm_size_t, device: mach_vm_size_t, device_peak: mach_vm_size_t, internal: mach_vm_size_t, internal_peak: mach_vm_size_t, external: mach_vm_size_t, external_peak: mach_vm_size_t, reusable: mach_vm_size_t, reusable_peak: mach_vm_size_t, purgeable_volatile_pmap: mach_vm_size_t, purgeable_volatile_resident: mach_vm_size_t, purgeable_volatile_virtual: mach_vm_size_t, compressed: mach_vm_size_t, compressed_peak: mach_vm_size_t, compressed_lifetime: mach_vm_size_t, phys_footprint: mach_vm_size_t, min_address: mach_vm_address_t, max_address: mach_vm_address_t)Added task_vm_info.max_addressAdded task_vm_info.min_addressAdded tcp_connection_info.init(tcpi_state: UInt8, tcpi_snd_wscale: UInt8, tcpi_rcv_wscale: UInt8, __pad1: UInt8, tcpi_options: UInt32, tcpi_flags: UInt32, tcpi_rto: UInt32, tcpi_maxseg: UInt32, tcpi_snd_ssthresh: UInt32, tcpi_snd_cwnd: UInt32, tcpi_snd_wnd: UInt32, tcpi_snd_sbbytes: UInt32, tcpi_rcv_wnd: UInt32, tcpi_rttcur: UInt32, tcpi_srtt: UInt32, tcpi_rttvar: UInt32, tcpi_tfo_cookie_req: UInt32, tcpi_tfo_cookie_rcv: UInt32, tcpi_tfo_syn_loss: UInt32, tcpi_tfo_syn_data_sent: UInt32, tcpi_tfo_syn_data_acked: UInt32, tcpi_tfo_syn_data_rcv: UInt32, tcpi_tfo_cookie_req_rcv: UInt32, tcpi_tfo_cookie_sent: UInt32, tcpi_tfo_cookie_invalid: UInt32, tcpi_tfo_cookie_wrong: UInt32, tcpi_tfo_no_cookie_rcv: UInt32, tcpi_tfo_heuristics_disable: UInt32, tcpi_tfo_send_blackhole: UInt32, tcpi_tfo_recv_blackhole: UInt32, __pad2: UInt32, tcpi_txpackets: UInt64, tcpi_txbytes: UInt64, tcpi_txretransmitbytes: UInt64, tcpi_rxpackets: UInt64, tcpi_rxbytes: UInt64, tcpi_rxoutoforderbytes: UInt64)Added tcp_connection_info.tcpi_tfo_cookie_wrongAdded tcp_connection_info.tcpi_tfo_heuristics_disableAdded tcp_connection_info.tcpi_tfo_no_cookie_rcvAdded tcp_connection_info.tcpi_tfo_recv_blackholeAdded tcp_connection_info.tcpi_tfo_send_blackholeAdded tm.init(tm_sec: Int32, tm_min: Int32, tm_hour: Int32, tm_mday: Int32, tm_mon: Int32, tm_year: Int32, tm_wday: Int32, tm_yday: Int32, tm_isdst: Int32, tm_gmtoff: Int, tm_zone: UnsafeMutablePointer<Int8>!)Added ucred.init(cr_link: ucred.__Unnamed_struct_cr_link, cr_ref: u_long, cr_posix: posix_cred, cr_label: OpaquePointer!, cr_audit: au_session)Added vfsidctl.init(vc_vers: Int32, vc_fsid: fsid_t, vc_ptr: UnsafeMutableRawPointer!, vc_len: Int, vc_spare: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32))Added vfsstatfs.init(f_bsize: UInt32, f_iosize: Int, f_blocks: UInt64, f_bfree: UInt64, f_bavail: UInt64, f_bused: UInt64, f_files: UInt64, f_ffree: UInt64, f_fsid: fsid_t, f_owner: uid_t, f_flags: UInt64, f_fstypename: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), f_mntonname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), f_mntfromname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), f_fssubtype: UInt32, f_reserved: (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?))Added vmspace.init(dummy: Int32, dummy2: caddr_t!, dummy3: (Int32, Int32, Int32, Int32, Int32), dummy4: (caddr_t?, caddr_t?, caddr_t?))Added wordexp_t.init(we_wordc: Int, we_wordv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, we_offs: Int)Added ALARM_NULLAdded AT_IPC_MSGAdded AT_IPC_SEMAdded AT_IPC_SHMAdded ATOMIC_BOOL_LOCK_FREEAdded ATOMIC_CHAR16_T_LOCK_FREEAdded ATOMIC_CHAR32_T_LOCK_FREEAdded ATOMIC_CHAR_LOCK_FREEAdded atomic_flag_clear(_: UnsafeMutablePointer<atomic_flag>!)Added atomic_flag_clear_explicit(_: UnsafeMutablePointer<atomic_flag>!, _: memory_order)Added atomic_flag_test_and_set(_: UnsafeMutablePointer<atomic_flag>!) -> BoolAdded atomic_flag_test_and_set_explicit(_: UnsafeMutablePointer<atomic_flag>!, _: memory_order) -> BoolAdded atomic_signal_fence(_: memory_order)Added atomic_thread_fence(_: memory_order)Added ATOMIC_WCHAR_T_LOCK_FREEAdded basename_r(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>!Added ceil<T : FloatingPoint>(_: T) -> TAdded clock_getres(_: clockid_t, _: UnsafeMutablePointer<timespec>!) -> Int32Added clock_gettime(_: clockid_t, _: UnsafeMutablePointer<timespec>!) -> Int32Added clock_gettime_nsec_np(_: clockid_t) -> __uint64_tAdded CLOCK_NULLAdded COALITION_NULLAdded COPYFILE_CLONEAdded COPYFILE_CLONE_FORCEAdded COPYFILE_RUN_IN_PLACEAdded COPYFILE_STATE_WAS_CLONEDAdded CPU_SUBTYPE_ARM64_ALLAdded CPU_SUBTYPE_ARM64_V8Added CPU_SUBTYPE_ARM_ALLAdded CPU_SUBTYPE_ARM_V4TAdded CPU_SUBTYPE_ARM_V5TEJAdded CPU_SUBTYPE_ARM_V6Added CPU_SUBTYPE_ARM_V6MAdded CPU_SUBTYPE_ARM_V7Added CPU_SUBTYPE_ARM_V7EMAdded CPU_SUBTYPE_ARM_V7FAdded CPU_SUBTYPE_ARM_V7KAdded CPU_SUBTYPE_ARM_V7MAdded CPU_SUBTYPE_ARM_V7SAdded CPU_SUBTYPE_ARM_V8Added CPU_SUBTYPE_ARM_XSCALEAdded CPU_SUBTYPE_BIG_ENDIANAdded CPU_SUBTYPE_HPPA_7100Added CPU_SUBTYPE_HPPA_7100LCAdded CPU_SUBTYPE_HPPA_ALLAdded CPU_SUBTYPE_I860_860Added CPU_SUBTYPE_I860_ALLAdded CPU_SUBTYPE_LITTLE_ENDIANAdded CPU_SUBTYPE_MC68030Added CPU_SUBTYPE_MC68030_ONLYAdded CPU_SUBTYPE_MC68040Added CPU_SUBTYPE_MC680x0_ALLAdded CPU_SUBTYPE_MC88000_ALLAdded CPU_SUBTYPE_MC88100Added CPU_SUBTYPE_MC88110Added CPU_SUBTYPE_MC98000_ALLAdded CPU_SUBTYPE_MC98601Added CPU_SUBTYPE_MIPS_ALLAdded CPU_SUBTYPE_MIPS_R2000Added CPU_SUBTYPE_MIPS_R2000aAdded CPU_SUBTYPE_MIPS_R2300Added CPU_SUBTYPE_MIPS_R2600Added CPU_SUBTYPE_MIPS_R2800Added CPU_SUBTYPE_MIPS_R3000Added CPU_SUBTYPE_MIPS_R3000aAdded CPU_SUBTYPE_MULTIPLEAdded CPU_SUBTYPE_POWERPC_601Added CPU_SUBTYPE_POWERPC_602Added CPU_SUBTYPE_POWERPC_603Added CPU_SUBTYPE_POWERPC_603eAdded CPU_SUBTYPE_POWERPC_603evAdded CPU_SUBTYPE_POWERPC_604Added CPU_SUBTYPE_POWERPC_604eAdded CPU_SUBTYPE_POWERPC_620Added CPU_SUBTYPE_POWERPC_7400Added CPU_SUBTYPE_POWERPC_7450Added CPU_SUBTYPE_POWERPC_750Added CPU_SUBTYPE_POWERPC_970Added CPU_SUBTYPE_POWERPC_ALLAdded CPU_SUBTYPE_SPARC_ALLAdded CPU_SUBTYPE_UVAXIAdded CPU_SUBTYPE_UVAXIIAdded CPU_SUBTYPE_UVAXIIIAdded CPU_SUBTYPE_VAX730Added CPU_SUBTYPE_VAX750Added CPU_SUBTYPE_VAX780Added CPU_SUBTYPE_VAX785Added CPU_SUBTYPE_VAX8200Added CPU_SUBTYPE_VAX8500Added CPU_SUBTYPE_VAX8600Added CPU_SUBTYPE_VAX8650Added CPU_SUBTYPE_VAX8800Added CPU_SUBTYPE_VAX_ALLAdded CPU_SUBTYPE_X86_64_ALLAdded CPU_SUBTYPE_X86_64_HAdded CPU_SUBTYPE_X86_ALLAdded CPU_SUBTYPE_X86_ARCH1Added CPU_THREADTYPE_INTEL_HTTAdded CPU_THREADTYPE_NONEAdded CPU_TYPE_ANYAdded CPU_TYPE_ARMAdded CPU_TYPE_HPPAAdded CPU_TYPE_I386Added CPU_TYPE_I860Added CPU_TYPE_MC680x0Added CPU_TYPE_MC88000Added CPU_TYPE_MC98000Added CPU_TYPE_POWERPCAdded CPU_TYPE_SPARCAdded CPU_TYPE_VAXAdded CPU_TYPE_X86Added CPUFAMILY_ARM_HURRICANEAdded dirname_r(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>!Added dprintf(_: Int, _: UnsafePointer<Int8>, _: CVarArg) -> Int32Added dyld_kernel_image_info_array_tAdded dyld_kernel_image_info_tAdded dyld_kernel_process_info_tAdded err_noneAdded ERR_SUCCESSAdded EV_VANISHEDAdded EVFILT_EXCEPTAdded F_CHECK_LVAdded fabs<T : FloatingPoint>(_: T) -> TAdded fchecklv_tAdded fcntl(_: Int32, _: Int32, _: UnsafeMutableRawPointer) -> Int32Added FFDSYNCAdded FFSYNCAdded floor<T : FloatingPoint>(_: T) -> TAdded fma<T : FloatingPoint>(_: T, _: T, _: T) -> TAdded fmod<T : FloatingPoint>(_: T, _: T) -> TAdded HOST_CALENDAR_SET_REPLYIDAdded HOST_CAN_HAS_DEBUGGERAdded host_can_has_debugger_info_data_tAdded host_can_has_debugger_info_tAdded host_create_mach_voucher_trap(_: mach_port_name_t, _: mach_voucher_attr_raw_recipe_array_t!, _: Int32, _: UnsafeMutablePointer<mach_port_name_t>!) -> kern_return_tAdded HOST_NOTIFY_CALENDAR_SETAdded HOST_NULLAdded HOST_PRIV_NULLAdded HOST_SECURITY_NULLAdded IFCAP_HW_TIMESTAMPAdded IFCAP_SKYWALKAdded IFCAP_SW_TIMESTAMPAdded IN_LINKLOCALNETNUMAdded INADDR_ALLHOSTS_GROUPAdded INADDR_ALLMDNS_GROUPAdded INADDR_ALLRPTS_GROUPAdded INADDR_ALLRTRS_GROUPAdded INADDR_ANYAdded INADDR_BROADCASTAdded INADDR_CARP_GROUPAdded INADDR_LOOPBACKAdded INADDR_MAX_LOCAL_GROUPAdded INADDR_PFSYNC_GROUPAdded INADDR_UNSPEC_GROUPAdded IOC_DIRMASKAdded IOC_INAdded IOC_OUTAdded IOC_VOIDAdded ioctl(_: CInt, _: UInt) -> CIntAdded ioctl(_: CInt, _: UInt, _: CInt) -> CIntAdded ioctl(_: CInt, _: UInt, _: UnsafeMutableRawPointer) -> CIntAdded IPC_PRIVATEAdded IPC_SPACE_NULLAdded IPC_VOUCHER_ATTR_CONTROL_NULLAdded IPC_VOUCHER_ATTR_MANAGER_NULLAdded IPC_VOUCHER_NULLAdded kdebug_signpost(_: UInt32, _: UInt, _: UInt, _: UInt, _: UInt) -> Int32Added kdebug_signpost_end(_: UInt32, _: UInt, _: UInt, _: UInt, _: UInt) -> Int32Added kdebug_signpost_start(_: UInt32, _: UInt, _: UInt, _: UInt, _: UInt) -> Int32Added KERN_KDTESTAdded KEV_DL_QOS_MODE_CHANGEDAdded KEV_INET6_ADDR_DELETEDAdded KEV_INET6_CHANGED_ADDRAdded KEV_INET6_DEFROUTERAdded KEV_INET6_NEW_LL_ADDRAdded KEV_INET6_NEW_RTADV_ADDRAdded KEV_INET6_NEW_USER_ADDRAdded KEV_INET6_SUBCLASSAdded KEV_INET_ADDR_DELETEDAdded KEV_INET_ARPCOLLISIONAdded KEV_INET_ARPRTRALIVEAdded KEV_INET_ARPRTRFAILUREAdded KEV_INET_CHANGED_ADDRAdded KEV_INET_NEW_ADDRAdded KEV_INET_PORTINUSEAdded KEV_INET_SIFBRDADDRAdded KEV_INET_SIFDSTADDRAdded KEV_INET_SIFNETMASKAdded KEV_INET_SUBCLASSAdded LEDGER_NULLAdded LOCK_SET_NULLAdded MAC_OS_X_VERSION_10_12Added MACH_ACTIVITY_ID_COUNT_MAXAdded mach_continuous_approximate_time() -> UInt64Added mach_continuous_time() -> UInt64Added mach_generate_activity_id(_: mach_port_name_t, _: Int32, _: UnsafeMutablePointer<UInt64>!) -> kern_return_tAdded mach_msg_priority_tAdded MACH_MSG_PRIORITY_UNSPECIFIEDAdded MACH_MSG_SIZE_MAXAdded MACH_MSG_TIMEOUT_NONEAdded MACH_MSG_TYPE_POLYMORPHICAdded MACH_PORT_DEADAdded MACH_PORT_RIGHT_DEAD_NAMEAdded MACH_PORT_RIGHT_LABELHAdded MACH_PORT_RIGHT_NUMBERAdded MACH_PORT_RIGHT_PORT_SETAdded MACH_PORT_RIGHT_RECEIVEAdded MACH_PORT_RIGHT_SENDAdded MACH_PORT_RIGHT_SEND_ONCEAdded MACH_PORT_TYPE_NONEAdded MACH_SEND_OVERRIDEAdded MACH_VM_MAX_ADDRESSAdded MACH_VM_MIN_ADDRESSAdded MACH_VOUCHER_ATTR_AUTO_REDEEMAdded MACH_VOUCHER_ATTR_BITS_STOREAdded MACH_VOUCHER_ATTR_CONTROL_FLAGS_NONEAdded MACH_VOUCHER_ATTR_CONTROL_NULLAdded MACH_VOUCHER_ATTR_COPYAdded MACH_VOUCHER_ATTR_IMPORTANCE_SELFAdded MACH_VOUCHER_ATTR_KEY_ALLAdded MACH_VOUCHER_ATTR_KEY_ATMAdded MACH_VOUCHER_ATTR_KEY_BANKAdded MACH_VOUCHER_ATTR_KEY_BITSAdded MACH_VOUCHER_ATTR_KEY_IMPORTANCEAdded MACH_VOUCHER_ATTR_KEY_NONEAdded MACH_VOUCHER_ATTR_KEY_NUM_WELL_KNOWNAdded MACH_VOUCHER_ATTR_KEY_PTHPRIORITYAdded MACH_VOUCHER_ATTR_KEY_TESTAdded MACH_VOUCHER_ATTR_KEY_USER_DATAAdded MACH_VOUCHER_ATTR_MANAGER_NULLAdded MACH_VOUCHER_ATTR_MAX_RAW_RECIPE_ARRAY_SIZEAdded MACH_VOUCHER_ATTR_NOOPAdded MACH_VOUCHER_ATTR_REDEEMAdded MACH_VOUCHER_ATTR_REMOVEAdded MACH_VOUCHER_ATTR_SEND_PREPROCESSAdded MACH_VOUCHER_ATTR_SET_VALUE_HANDLEAdded MACH_VOUCHER_ATTR_TEST_STOREAdded MACH_VOUCHER_ATTR_USER_DATA_STOREAdded MACH_VOUCHER_ATTR_VALUE_FLAGS_NONEAdded MACH_VOUCHER_ATTR_VALUE_FLAGS_PERSISTAdded MACH_VOUCHER_ATTR_VALUE_MAX_NESTEDAdded mach_voucher_extract_attr_recipe_trap(_: mach_port_name_t, _: mach_voucher_attr_key_t, _: mach_voucher_attr_raw_recipe_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_tAdded MACH_VOUCHER_NAME_NULLAdded MACH_VOUCHER_NULLAdded MACH_VOUCHER_SELECTOR_CURRENTAdded MACH_VOUCHER_SELECTOR_EFFECTIVEAdded MACH_VOUCHER_TRAP_STACK_LIMITAdded MAP_MEM_GRAB_SECLUDEDAdded MEMORY_OBJECT_CONTROL_NULLAdded MEMORY_OBJECT_DEFAULT_NULLAdded MEMORY_OBJECT_NAME_NULLAdded MEMORY_OBJECT_NULLAdded memory_order_acq_relAdded memory_order_acquireAdded memory_order_consumeAdded memory_order_relaxedAdded memory_order_releaseAdded memory_order_seq_cstAdded mig_strncpy_zerofill(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int32) -> Int32Added mkostemp(_: UnsafeMutablePointer<Int8>!, _: Int32) -> Int32Added mkostemps(_: UnsafeMutablePointer<Int8>!, _: Int32, _: Int32) -> Int32Added mkpathat_np(_: Int32, _: UnsafePointer<Int8>!, _: mode_t) -> Int32Added mkstemp_dprotected_np(_: UnsafeMutablePointer<Int8>!, _: Int32, _: Int32) -> Int32Added NET_SERVICE_TYPE_AVAdded NET_SERVICE_TYPE_BEAdded NET_SERVICE_TYPE_BKAdded NET_SERVICE_TYPE_OAMAdded NET_SERVICE_TYPE_RDAdded NET_SERVICE_TYPE_RVAdded NET_SERVICE_TYPE_SIGAdded NET_SERVICE_TYPE_VIAdded NET_SERVICE_TYPE_VOAdded NETSVC_MRKNG_LVL_L2Added NETSVC_MRKNG_LVL_L3L2_ALLAdded NETSVC_MRKNG_LVL_L3L2_BKAdded NETSVC_MRKNG_UNKNOWNAdded NOTE_FUNLOCKAdded NOTE_MACH_CONTINUOUS_TIMEAdded NOTE_OOBAdded O_FSYNCAdded os_block_tAdded os_function_tAdded OS_LOCK_API_VERSIONAdded os_unfair_lockAdded os_unfair_lock_lock(_: os_unfair_lock_t)Added os_unfair_lock_tAdded os_unfair_lock_trylock(_: os_unfair_lock_t) -> BoolAdded os_unfair_lock_unlock(_: os_unfair_lock_t)Added OSATOMIC_DEPRECATEDAdded OSAtomic_int64_aligned64_tAdded OSSPINLOCK_DEPRECATEDAdded P_DIRTY_AGING_IN_PROGRESSAdded PF_BONDAdded PF_VLANAdded PROCESSOR_NULLAdded PROCESSOR_SET_NULLAdded pthread_create_from_mach_thread(_: UnsafeMutablePointer<pthread_t?>!, _: UnsafePointer<pthread_attr_t>?, _: (UnsafeMutableRawPointer) -> UnsafeMutableRawPointer?, _: UnsafeMutableRawPointer?) -> Int32Added remainder<T : FloatingPoint>(_: T, _: T) -> TAdded RENAME_EXCLAdded RENAME_SECLUDEAdded RENAME_SWAPAdded renameatx_np(_: Int32, _: UnsafePointer<Int8>!, _: Int32, _: UnsafePointer<Int8>!, _: UInt32) -> Int32Added renamex_np(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UInt32) -> Int32Added round<T : FloatingPoint>(_: T) -> TAdded RPP_STDINAdded sem_open(_: UnsafePointer<CChar>, _: Int32) -> UnsafeMutablePointer<sem_t>?Added sem_open(_: UnsafePointer<CChar>, _: Int32, _: mode_t, _: CUnsignedInt) -> UnsafeMutablePointer<sem_t>?Added SEMAPHORE_NULLAdded snprintf(ptr: UnsafeMutablePointer<Int8>, _: Int, _: UnsafePointer<Int8>, _: CVarArg) -> Int32Added SO_NET_SERVICE_TYPEAdded SO_NETSVC_MARKING_LEVELAdded sqrt<T : FloatingPoint>(_: T) -> TAdded SYS___channel_get_infoAdded SYS___channel_get_optAdded SYS___channel_openAdded SYS___channel_set_optAdded SYS___channel_syncAdded SYS___nexus_createAdded SYS___nexus_deregisterAdded SYS___nexus_destroyAdded SYS___nexus_get_optAdded SYS___nexus_openAdded SYS___nexus_registerAdded SYS___nexus_set_optAdded SYS_abort_with_payloadAdded SYS_clonefileatAdded SYS_fclonefileatAdded SYS_fs_snapshotAdded SYS_getentropyAdded SYS_invalidAdded SYS_kdebug_typefilterAdded SYS_necp_client_actionAdded SYS_necp_openAdded SYS_renameatx_npAdded SYS_terminate_with_payloadAdded SYS_ulock_waitAdded SYS_ulock_wakeAdded TARGET_OS_BRIDGEAdded TARGET_OS_OSXAdded task_generate_corpse(_: task_t, _: UnsafeMutablePointer<mach_port_t>!) -> kern_return_tAdded task_get_dyld_image_infos(_: task_t, _: UnsafeMutablePointer<dyld_kernel_image_info_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_tAdded task_map_corpse_info(_: task_t, _: task_t, _: UnsafeMutablePointer<vm_address_t>!, _: UnsafeMutablePointer<UInt32>!) -> kern_return_tAdded task_map_corpse_info_64(_: task_t, _: task_t, _: UnsafeMutablePointer<mach_vm_address_t>!, _: UnsafeMutablePointer<mach_vm_size_t>!) -> kern_return_tAdded TASK_NAME_NULLAdded TASK_NULLAdded task_register_dyld_get_process_state(_: task_t, _: UnsafeMutablePointer<dyld_kernel_process_info_t>!) -> kern_return_tAdded task_register_dyld_image_infos(_: task_t, _: dyld_kernel_image_info_array_t!, _: mach_msg_type_number_t) -> kern_return_tAdded task_register_dyld_set_dyld_state(_: task_t, _: UInt8) -> kern_return_tAdded task_register_dyld_shared_cache_image_info(_: task_t, _: dyld_kernel_image_info_t, _: boolean_t, _: boolean_t) -> kern_return_tAdded TASK_RESOURCE_NOTIFY_PORTAdded task_unregister_dyld_image_infos(_: task_t, _: dyld_kernel_image_info_array_t!, _: mach_msg_type_number_t) -> kern_return_tAdded THR_ACT_NULLAdded THREAD_BACKGROUND_POLICY_DARWIN_BGAdded THREAD_NULLAdded TID_NULLAdded TIOCCBRKAdded TIOCCDTRAdded TIOCCONSAdded TIOCDCDTIMESTAMPAdded TIOCDRAINAdded TIOCDSIMICROCODEAdded TIOCEXCLAdded TIOCEXTAdded TIOCFLUSHAdded TIOCGDRAINWAITAdded TIOCGETAAdded TIOCGETCAdded TIOCGETDAdded TIOCGETPAdded TIOCGLTCAdded TIOCGPGRPAdded TIOCGWINSZAdded TIOCHPCLAdded TIOCIXOFFAdded TIOCIXONAdded TIOCLBICAdded TIOCLBISAdded TIOCLGETAdded TIOCLSETAdded TIOCMBICAdded TIOCMBISAdded TIOCMGDTRWAITAdded TIOCMGETAdded TIOCMODGAdded TIOCMODSAdded TIOCMSDTRWAITAdded TIOCMSETAdded TIOCNOTTYAdded TIOCNXCLAdded TIOCOUTQAdded TIOCPKTAdded TIOCPTYGNAMEAdded TIOCPTYGRANTAdded TIOCPTYUNLKAdded TIOCREMOTEAdded TIOCSBRKAdded TIOCSCONSAdded TIOCSCTTYAdded TIOCSDRAINWAITAdded TIOCSDTRAdded TIOCSETAAdded TIOCSETAFAdded TIOCSETAWAdded TIOCSETCAdded TIOCSETDAdded TIOCSETNAdded TIOCSETPAdded TIOCSIGAdded TIOCSLTCAdded TIOCSPGRPAdded TIOCSTARTAdded TIOCSTATAdded TIOCSTIAdded TIOCSTOPAdded TIOCSWINSZAdded TIOCTIMESTAMPAdded TIOCUCNTLAdded trunc<T : FloatingPoint>(_: T) -> TAdded UND_SERVER_NULLAdded UPL_NULLAdded USER_ADDR_NULLAdded UUID_NULLAdded VM_BEHAVIOR_CAN_REUSEAdded VM_BEHAVIOR_DEFAULTAdded VM_BEHAVIOR_DONTNEEDAdded VM_BEHAVIOR_FREEAdded VM_BEHAVIOR_PAGEOUTAdded VM_BEHAVIOR_RANDOMAdded VM_BEHAVIOR_REUSABLEAdded VM_BEHAVIOR_REUSEAdded VM_BEHAVIOR_RSEQNTLAdded VM_BEHAVIOR_SEQUENTIALAdded VM_BEHAVIOR_WILLNEEDAdded VM_BEHAVIOR_ZERO_WIRED_PAGESAdded VM_FLAGS_RANDOM_ADDRAdded VM_INHERIT_COPYAdded VM_INHERIT_DEFAULTAdded VM_INHERIT_DONATE_COPYAdded VM_INHERIT_LAST_VALIDAdded VM_INHERIT_NONEAdded VM_INHERIT_SHAREAdded VM_MAP_MAX_ADDRESSAdded VM_MAP_MIN_ADDRESSAdded VM_MAP_NULLAdded VM_MAX_ADDRESSAdded VM_MEMORY_COREGRAPHICS_XALLOCAdded VM_MEMORY_DHMMAdded VM_MEMORY_SCENEKITAdded VM_MEMORY_SKYWALKAdded VM_MEMORY_SWIFT_METADATAAdded VM_MEMORY_SWIFT_RUNTIMEAdded VM_MIN_ADDRESSAdded VM_NAMED_ENTRY_NULLAdded VM_PROT_COPYAdded VM_PROT_EXECUTEAdded VM_PROT_IS_MASKAdded VM_PROT_NO_CHANGEAdded VM_PROT_NONEAdded VM_PROT_READAdded VM_PROT_STRIP_READAdded VM_PROT_WANTS_COPYAdded VM_PROT_WRITEAdded VM_PURGABLE_GET_STATEAdded VM_PURGABLE_PURGE_ALLAdded VM_PURGABLE_SET_STATEAdded VM_SYNC_ASYNCHRONOUSAdded VM_SYNC_CONTIGUOUSAdded VM_SYNC_DEACTIVATEAdded VM_SYNC_INVALIDATEAdded VM_SYNC_KILLPAGESAdded VM_SYNC_REUSABLEPAGESAdded VM_SYNC_SYNCHRONOUSAdded VOL_CAP_FMT_DIR_HARDLINKSAdded VOL_CAP_FMT_DOCUMENT_IDAdded VOL_CAP_FMT_WRITE_GENERATION_COUNTAdded VOL_CAP_INT_CLONEAdded VOL_CAP_INT_RENAME_EXCLAdded VOL_CAP_INT_RENAME_SWAPAdded WEOFAdded XATTR_FLAG_CONTENT_DEPENDENTAdded XATTR_FLAG_NEVER_PRESERVEAdded XATTR_FLAG_NO_EXPORTAdded XATTR_FLAG_SYNCABLEModified addrinfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct addrinfo {     var ai_flags: Int32     var ai_family: Int32     var ai_socktype: Int32     var ai_protocol: Int32     var ai_addrlen: socklen_t     var ai_canonname: UnsafeMutablePointer<Int8>     var ai_addr: UnsafeMutablePointer<sockaddr>     var ai_next: UnsafeMutablePointer<addrinfo>     init()     init(ai_flags ai_flags: Int32, ai_family ai_family: Int32, ai_socktype ai_socktype: Int32, ai_protocol ai_protocol: Int32, ai_addrlen ai_addrlen: socklen_t, ai_canonname ai_canonname: UnsafeMutablePointer<Int8>, ai_addr ai_addr: UnsafeMutablePointer<sockaddr>, ai_next ai_next: UnsafeMutablePointer<addrinfo>) } ``` |
| To | ``` struct addrinfo {     var ai_flags: Int32     var ai_family: Int32     var ai_socktype: Int32     var ai_protocol: Int32     var ai_addrlen: socklen_t     var ai_canonname: UnsafeMutablePointer<Int8>!     var ai_addr: UnsafeMutablePointer<sockaddr>!     var ai_next: UnsafeMutablePointer<addrinfo>!     init()     init(ai_flags ai_flags: Int32, ai_family ai_family: Int32, ai_socktype ai_socktype: Int32, ai_protocol ai_protocol: Int32, ai_addrlen ai_addrlen: socklen_t, ai_canonname ai_canonname: UnsafeMutablePointer<Int8>!, ai_addr ai_addr: UnsafeMutablePointer<sockaddr>!, ai_next ai_next: UnsafeMutablePointer<addrinfo>!) } ``` |

Modified addrinfo.ai_addr

|  | Declaration |
| --- | --- |
| From | ``` var ai_addr: UnsafeMutablePointer<sockaddr> ``` |
| To | ``` var ai_addr: UnsafeMutablePointer<sockaddr>! ``` |

Modified addrinfo.ai_canonname

|  | Declaration |
| --- | --- |
| From | ``` var ai_canonname: UnsafeMutablePointer<Int8> ``` |
| To | ``` var ai_canonname: UnsafeMutablePointer<Int8>! ``` |

Modified addrinfo.ai_next

|  | Declaration |
| --- | --- |
| From | ``` var ai_next: UnsafeMutablePointer<addrinfo> ``` |
| To | ``` var ai_next: UnsafeMutablePointer<addrinfo>! ``` |

Modified aiocb [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct aiocb {     var aio_fildes: Int32     var aio_offset: off_t     var aio_buf: UnsafeMutablePointer<Void>     var aio_nbytes: Int     var aio_reqprio: Int32     var aio_sigevent: sigevent     var aio_lio_opcode: Int32     init()     init(aio_fildes aio_fildes: Int32, aio_offset aio_offset: off_t, aio_buf aio_buf: UnsafeMutablePointer<Void>, aio_nbytes aio_nbytes: Int, aio_reqprio aio_reqprio: Int32, aio_sigevent aio_sigevent: sigevent, aio_lio_opcode aio_lio_opcode: Int32) } ``` |
| To | ``` struct aiocb {     var aio_fildes: Int32     var aio_offset: off_t     var aio_buf: UnsafeMutableRawPointer!     var aio_nbytes: Int     var aio_reqprio: Int32     var aio_sigevent: sigevent     var aio_lio_opcode: Int32     init()     init(aio_fildes aio_fildes: Int32, aio_offset aio_offset: off_t, aio_buf aio_buf: UnsafeMutableRawPointer!, aio_nbytes aio_nbytes: Int, aio_reqprio aio_reqprio: Int32, aio_sigevent aio_sigevent: sigevent, aio_lio_opcode aio_lio_opcode: Int32) } ``` |

Modified aiocb.aio_buf

|  | Declaration |
| --- | --- |
| From | ``` var aio_buf: UnsafeMutablePointer<Void> ``` |
| To | ``` var aio_buf: UnsafeMutableRawPointer! ``` |

Modified au_session [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct au_session {     var as_aia_p: UnsafeMutablePointer<auditinfo_addr_t>     var as_mask: au_mask_t     init()     init(as_aia_p as_aia_p: UnsafeMutablePointer<auditinfo_addr_t>, as_mask as_mask: au_mask_t) } ``` |
| To | ``` struct au_session {     var as_aia_p: UnsafeMutablePointer<auditinfo_addr_t>!     var as_mask: au_mask_t     init()     init(as_aia_p as_aia_p: UnsafeMutablePointer<auditinfo_addr_t>!, as_mask as_mask: au_mask_t) } ``` |

Modified au_session.as_aia_p

|  | Declaration |
| --- | --- |
| From | ``` var as_aia_p: UnsafeMutablePointer<auditinfo_addr_t> ``` |
| To | ``` var as_aia_p: UnsafeMutablePointer<auditinfo_addr_t>! ``` |

Modified ctlname [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ctlname {     var ctl_name: UnsafeMutablePointer<Int8>     var ctl_type: Int32     init()     init(ctl_name ctl_name: UnsafeMutablePointer<Int8>, ctl_type ctl_type: Int32) } ``` |
| To | ``` struct ctlname {     var ctl_name: UnsafeMutablePointer<Int8>!     var ctl_type: Int32     init()     init(ctl_name ctl_name: UnsafeMutablePointer<Int8>!, ctl_type ctl_type: Int32) } ``` |

Modified ctlname.ctl_name

|  | Declaration |
| --- | --- |
| From | ``` var ctl_name: UnsafeMutablePointer<Int8> ``` |
| To | ``` var ctl_name: UnsafeMutablePointer<Int8>! ``` |

Modified DarwinBoolean [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct DarwinBoolean : BooleanType, BooleanLiteralConvertible {     init(_ value: Bool)     var boolValue: Bool { get }     init(booleanLiteral value: Bool) } extension DarwinBoolean : _Reflectable { } extension DarwinBoolean : CustomStringConvertible {     var description: String { get } } extension DarwinBoolean : Equatable { } ``` | BooleanLiteralConvertible, BooleanType, CustomStringConvertible, Equatable |
| To | ``` struct DarwinBoolean : ExpressibleByBooleanLiteral {     init(_ value: Bool)     var boolValue: Bool { get }     init(booleanLiteral value: Bool) } extension DarwinBoolean : CustomReflectable {     var customMirror: Mirror { get } } extension DarwinBoolean : CustomStringConvertible {     var description: String { get } } ``` | CustomReflectable, CustomStringConvertible, ExpressibleByBooleanLiteral |

Modified datum [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct datum {     var dptr: UnsafeMutablePointer<Void>     var dsize: Int     init()     init(dptr dptr: UnsafeMutablePointer<Void>, dsize dsize: Int) } ``` |
| To | ``` struct datum {     var dptr: UnsafeMutableRawPointer!     var dsize: Int     init()     init(dptr dptr: UnsafeMutableRawPointer!, dsize dsize: Int) } ``` |

Modified datum.dptr

|  | Declaration |
| --- | --- |
| From | ``` var dptr: UnsafeMutablePointer<Void> ``` |
| To | ``` var dptr: UnsafeMutableRawPointer! ``` |

Modified DBM [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DBM {     var __opaque: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(__opaque __opaque: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |
| To | ``` struct DBM {     var __opaque: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(__opaque __opaque: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified DIR [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DIR {     var __dd_fd: Int32     var __dd_loc: Int     var __dd_size: Int     var __dd_buf: UnsafeMutablePointer<Int8>     var __dd_len: Int32     var __dd_seek: Int     var __dd_rewind: Int     var __dd_flags: Int32     var __dd_lock: __darwin_pthread_mutex_t     var __dd_td: COpaquePointer     init()     init(__dd_fd __dd_fd: Int32, __dd_loc __dd_loc: Int, __dd_size __dd_size: Int, __dd_buf __dd_buf: UnsafeMutablePointer<Int8>, __dd_len __dd_len: Int32, __dd_seek __dd_seek: Int, __dd_rewind __dd_rewind: Int, __dd_flags __dd_flags: Int32, __dd_lock __dd_lock: __darwin_pthread_mutex_t, __dd_td __dd_td: COpaquePointer) } ``` |
| To | ``` struct DIR {     var __dd_fd: Int32     var __dd_loc: Int     var __dd_size: Int     var __dd_buf: UnsafeMutablePointer<Int8>!     var __dd_len: Int32     var __dd_seek: Int     var __dd_rewind: Int     var __dd_flags: Int32     var __dd_lock: __darwin_pthread_mutex_t     var __dd_td: OpaquePointer!     init()     init(__dd_fd __dd_fd: Int32, __dd_loc __dd_loc: Int, __dd_size __dd_size: Int, __dd_buf __dd_buf: UnsafeMutablePointer<Int8>!, __dd_len __dd_len: Int32, __dd_seek __dd_seek: Int, __dd_rewind __dd_rewind: Int, __dd_flags __dd_flags: Int32, __dd_lock __dd_lock: __darwin_pthread_mutex_t, __dd_td __dd_td: OpaquePointer!) } ``` |

Modified dl_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dl_info {     var dli_fname: UnsafePointer<Int8>     var dli_fbase: UnsafeMutablePointer<Void>     var dli_sname: UnsafePointer<Int8>     var dli_saddr: UnsafeMutablePointer<Void>     init()     init(dli_fname dli_fname: UnsafePointer<Int8>, dli_fbase dli_fbase: UnsafeMutablePointer<Void>, dli_sname dli_sname: UnsafePointer<Int8>, dli_saddr dli_saddr: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct dl_info {     var dli_fname: UnsafePointer<Int8>!     var dli_fbase: UnsafeMutableRawPointer!     var dli_sname: UnsafePointer<Int8>!     var dli_saddr: UnsafeMutableRawPointer!     init()     init(dli_fname dli_fname: UnsafePointer<Int8>!, dli_fbase dli_fbase: UnsafeMutableRawPointer!, dli_sname dli_sname: UnsafePointer<Int8>!, dli_saddr dli_saddr: UnsafeMutableRawPointer!) } ``` |

Modified dl_info.dli_fbase

|  | Declaration |
| --- | --- |
| From | ``` var dli_fbase: UnsafeMutablePointer<Void> ``` |
| To | ``` var dli_fbase: UnsafeMutableRawPointer! ``` |

Modified dl_info.dli_fname

|  | Declaration |
| --- | --- |
| From | ``` var dli_fname: UnsafePointer<Int8> ``` |
| To | ``` var dli_fname: UnsafePointer<Int8>! ``` |

Modified dl_info.dli_saddr

|  | Declaration |
| --- | --- |
| From | ``` var dli_saddr: UnsafeMutablePointer<Void> ``` |
| To | ``` var dli_saddr: UnsafeMutableRawPointer! ``` |

Modified dl_info.dli_sname

|  | Declaration |
| --- | --- |
| From | ``` var dli_sname: UnsafePointer<Int8> ``` |
| To | ``` var dli_sname: UnsafePointer<Int8>! ``` |

Modified entry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct entry {     var key: UnsafeMutablePointer<Int8>     var data: UnsafeMutablePointer<Void>     init()     init(key key: UnsafeMutablePointer<Int8>, data data: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct entry {     var key: UnsafeMutablePointer<Int8>!     var data: UnsafeMutableRawPointer!     init()     init(key key: UnsafeMutablePointer<Int8>!, data data: UnsafeMutableRawPointer!) } ``` |

Modified entry.data

|  | Declaration |
| --- | --- |
| From | ``` var data: UnsafeMutablePointer<Void> ``` |
| To | ``` var data: UnsafeMutableRawPointer! ``` |

Modified entry.key

|  | Declaration |
| --- | --- |
| From | ``` var key: UnsafeMutablePointer<Int8> ``` |
| To | ``` var key: UnsafeMutablePointer<Int8>! ``` |

Modified eproc [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct eproc {     var e_paddr: COpaquePointer     var e_sess: COpaquePointer     var e_pcred: _pcred     var e_ucred: _ucred     var e_vm: vmspace     var e_ppid: pid_t     var e_pgid: pid_t     var e_jobc: Int16     var e_tdev: dev_t     var e_tpgid: pid_t     var e_tsess: COpaquePointer     var e_wmesg: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var e_xsize: segsz_t     var e_xrssize: Int16     var e_xccount: Int16     var e_xswrss: Int16     var e_flag: Int32     var e_login: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var e_spare: (Int32, Int32, Int32, Int32)     init()     init(e_paddr e_paddr: COpaquePointer, e_sess e_sess: COpaquePointer, e_pcred e_pcred: _pcred, e_ucred e_ucred: _ucred, e_vm e_vm: vmspace, e_ppid e_ppid: pid_t, e_pgid e_pgid: pid_t, e_jobc e_jobc: Int16, e_tdev e_tdev: dev_t, e_tpgid e_tpgid: pid_t, e_tsess e_tsess: COpaquePointer, e_wmesg e_wmesg: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), e_xsize e_xsize: segsz_t, e_xrssize e_xrssize: Int16, e_xccount e_xccount: Int16, e_xswrss e_xswrss: Int16, e_flag e_flag: Int32, e_login e_login: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), e_spare e_spare: (Int32, Int32, Int32, Int32)) } ``` |
| To | ``` struct eproc {     var e_paddr: OpaquePointer!     var e_sess: OpaquePointer!     var e_pcred: _pcred     var e_ucred: _ucred     var e_vm: vmspace     var e_ppid: pid_t     var e_pgid: pid_t     var e_jobc: Int16     var e_tdev: dev_t     var e_tpgid: pid_t     var e_tsess: OpaquePointer!     var e_wmesg: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var e_xsize: segsz_t     var e_xrssize: Int16     var e_xccount: Int16     var e_xswrss: Int16     var e_flag: Int32     var e_login: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var e_spare: (Int32, Int32, Int32, Int32)     init()     init(e_paddr e_paddr: OpaquePointer!, e_sess e_sess: OpaquePointer!, e_pcred e_pcred: _pcred, e_ucred e_ucred: _ucred, e_vm e_vm: vmspace, e_ppid e_ppid: pid_t, e_pgid e_pgid: pid_t, e_jobc e_jobc: Int16, e_tdev e_tdev: dev_t, e_tpgid e_tpgid: pid_t, e_tsess e_tsess: OpaquePointer!, e_wmesg e_wmesg: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), e_xsize e_xsize: segsz_t, e_xrssize e_xrssize: Int16, e_xccount e_xccount: Int16, e_xswrss e_xswrss: Int16, e_flag e_flag: Int32, e_login e_login: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), e_spare e_spare: (Int32, Int32, Int32, Int32)) } ``` |

Modified eproc.e_paddr

|  | Declaration |
| --- | --- |
| From | ``` var e_paddr: COpaquePointer ``` |
| To | ``` var e_paddr: OpaquePointer! ``` |

Modified eproc.e_sess

|  | Declaration |
| --- | --- |
| From | ``` var e_sess: COpaquePointer ``` |
| To | ``` var e_sess: OpaquePointer! ``` |

Modified eproc.e_tsess

|  | Declaration |
| --- | --- |
| From | ``` var e_tsess: COpaquePointer ``` |
| To | ``` var e_tsess: OpaquePointer! ``` |

Modified exception [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct exception {     var type: Int32     var name: UnsafeMutablePointer<Int8>     var arg1: Double     var arg2: Double     var retval: Double     init()     init(type type: Int32, name name: UnsafeMutablePointer<Int8>, arg1 arg1: Double, arg2 arg2: Double, retval retval: Double) } ``` |
| To | ``` struct exception {     var type: Int32     var name: UnsafeMutablePointer<Int8>!     var arg1: Double     var arg2: Double     var retval: Double     init()     init(type type: Int32, name name: UnsafeMutablePointer<Int8>!, arg1 arg1: Double, arg2 arg2: Double, retval retval: Double) } ``` |

Modified exception.name

|  | Declaration |
| --- | --- |
| From | ``` var name: UnsafeMutablePointer<Int8> ``` |
| To | ``` var name: UnsafeMutablePointer<Int8>! ``` |

Modified extern_proc [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct extern_proc {     struct __Unnamed_union_p_un {         struct __Unnamed_struct_p_st1 {             var __p_forw: COpaquePointer             var __p_back: COpaquePointer             init()             init(__p_forw __p_forw: COpaquePointer, __p_back __p_back: COpaquePointer)         }         var p_st1: extern_proc.__Unnamed_union_p_un.__Unnamed_struct_p_st1         var __p_starttime: timeval         init(p_st1 p_st1: extern_proc.__Unnamed_union_p_un.__Unnamed_struct_p_st1)         init(__p_starttime __p_starttime: timeval)         init()     }     var p_un: extern_proc.__Unnamed_union_p_un     var p_vmspace: UnsafeMutablePointer<vmspace>     var p_sigacts: COpaquePointer     var p_flag: Int32     var p_stat: Int8     var p_pid: pid_t     var p_oppid: pid_t     var p_dupfd: Int32     var user_stack: caddr_t     var exit_thread: UnsafeMutablePointer<Void>     var p_debugger: Int32     var sigwait: boolean_t     var p_estcpu: u_int     var p_cpticks: Int32     var p_pctcpu: fixpt_t     var p_wchan: UnsafeMutablePointer<Void>     var p_wmesg: UnsafeMutablePointer<Int8>     var p_swtime: u_int     var p_slptime: u_int     var p_realtimer: itimerval     var p_rtime: timeval     var p_uticks: u_quad_t     var p_sticks: u_quad_t     var p_iticks: u_quad_t     var p_traceflag: Int32     var p_tracep: COpaquePointer     var p_siglist: Int32     var p_textvp: COpaquePointer     var p_holdcnt: Int32     var p_sigmask: sigset_t     var p_sigignore: sigset_t     var p_sigcatch: sigset_t     var p_priority: u_char     var p_usrpri: u_char     var p_nice: Int8     var p_comm: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var p_pgrp: COpaquePointer     var p_addr: COpaquePointer     var p_xstat: u_short     var p_acflag: u_short     var p_ru: UnsafeMutablePointer<rusage>     init() } ``` |
| To | ``` struct extern_proc {     struct __Unnamed_union_p_un {         struct __Unnamed_struct_p_st1 {             var __p_forw: OpaquePointer!             var __p_back: OpaquePointer!             init()             init(__p_forw __p_forw: OpaquePointer!, __p_back __p_back: OpaquePointer!)         }         var p_st1: extern_proc.__Unnamed_union_p_un.__Unnamed_struct_p_st1         var __p_starttime: timeval         init(p_st1 p_st1: extern_proc.__Unnamed_union_p_un.__Unnamed_struct_p_st1)         init(__p_starttime __p_starttime: timeval)         init()     }     var p_un: extern_proc.__Unnamed_union_p_un     var p_vmspace: UnsafeMutablePointer<vmspace>!     var p_sigacts: OpaquePointer!     var p_flag: Int32     var p_stat: Int8     var p_pid: pid_t     var p_oppid: pid_t     var p_dupfd: Int32     var user_stack: caddr_t!     var exit_thread: UnsafeMutableRawPointer!     var p_debugger: Int32     var sigwait: boolean_t     var p_estcpu: u_int     var p_cpticks: Int32     var p_pctcpu: fixpt_t     var p_wchan: UnsafeMutableRawPointer!     var p_wmesg: UnsafeMutablePointer<Int8>!     var p_swtime: u_int     var p_slptime: u_int     var p_realtimer: itimerval     var p_rtime: timeval     var p_uticks: u_quad_t     var p_sticks: u_quad_t     var p_iticks: u_quad_t     var p_traceflag: Int32     var p_tracep: OpaquePointer!     var p_siglist: Int32     var p_textvp: OpaquePointer!     var p_holdcnt: Int32     var p_sigmask: sigset_t     var p_sigignore: sigset_t     var p_sigcatch: sigset_t     var p_priority: u_char     var p_usrpri: u_char     var p_nice: Int8     var p_comm: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var p_pgrp: OpaquePointer!     var p_addr: OpaquePointer!     var p_xstat: u_short     var p_acflag: u_short     var p_ru: UnsafeMutablePointer<rusage>!     init() } ``` |

Modified extern_proc.exit_thread

|  | Declaration |
| --- | --- |
| From | ``` var exit_thread: UnsafeMutablePointer<Void> ``` |
| To | ``` var exit_thread: UnsafeMutableRawPointer! ``` |

Modified extern_proc.p_addr

|  | Declaration |
| --- | --- |
| From | ``` var p_addr: COpaquePointer ``` |
| To | ``` var p_addr: OpaquePointer! ``` |

Modified extern_proc.p_pgrp

|  | Declaration |
| --- | --- |
| From | ``` var p_pgrp: COpaquePointer ``` |
| To | ``` var p_pgrp: OpaquePointer! ``` |

Modified extern_proc.p_ru

|  | Declaration |
| --- | --- |
| From | ``` var p_ru: UnsafeMutablePointer<rusage> ``` |
| To | ``` var p_ru: UnsafeMutablePointer<rusage>! ``` |

Modified extern_proc.p_sigacts

|  | Declaration |
| --- | --- |
| From | ``` var p_sigacts: COpaquePointer ``` |
| To | ``` var p_sigacts: OpaquePointer! ``` |

Modified extern_proc.p_textvp

|  | Declaration |
| --- | --- |
| From | ``` var p_textvp: COpaquePointer ``` |
| To | ``` var p_textvp: OpaquePointer! ``` |

Modified extern_proc.p_tracep

|  | Declaration |
| --- | --- |
| From | ``` var p_tracep: COpaquePointer ``` |
| To | ``` var p_tracep: OpaquePointer! ``` |

Modified extern_proc.p_vmspace

|  | Declaration |
| --- | --- |
| From | ``` var p_vmspace: UnsafeMutablePointer<vmspace> ``` |
| To | ``` var p_vmspace: UnsafeMutablePointer<vmspace>! ``` |

Modified extern_proc.p_wchan

|  | Declaration |
| --- | --- |
| From | ``` var p_wchan: UnsafeMutablePointer<Void> ``` |
| To | ``` var p_wchan: UnsafeMutableRawPointer! ``` |

Modified extern_proc.p_wmesg

|  | Declaration |
| --- | --- |
| From | ``` var p_wmesg: UnsafeMutablePointer<Int8> ``` |
| To | ``` var p_wmesg: UnsafeMutablePointer<Int8>! ``` |

Modified extern_proc.user_stack

|  | Declaration |
| --- | --- |
| From | ``` var user_stack: caddr_t ``` |
| To | ``` var user_stack: caddr_t! ``` |

Modified fbootstraptransfer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fbootstraptransfer {     var fbt_offset: off_t     var fbt_length: Int     var fbt_buffer: UnsafeMutablePointer<Void>     init()     init(fbt_offset fbt_offset: off_t, fbt_length fbt_length: Int, fbt_buffer fbt_buffer: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct fbootstraptransfer {     var fbt_offset: off_t     var fbt_length: Int     var fbt_buffer: UnsafeMutableRawPointer!     init()     init(fbt_offset fbt_offset: off_t, fbt_length fbt_length: Int, fbt_buffer fbt_buffer: UnsafeMutableRawPointer!) } ``` |

Modified fbootstraptransfer.fbt_buffer

|  | Declaration |
| --- | --- |
| From | ``` var fbt_buffer: UnsafeMutablePointer<Void> ``` |
| To | ``` var fbt_buffer: UnsafeMutableRawPointer! ``` |

Modified fcodeblobs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fcodeblobs {     var f_cd_hash: UnsafeMutablePointer<Void>     var f_hash_size: Int     var f_cd_buffer: UnsafeMutablePointer<Void>     var f_cd_size: Int     var f_out_size: UnsafeMutablePointer<UInt32>     var f_arch: Int32     var __padding: Int32     init()     init(f_cd_hash f_cd_hash: UnsafeMutablePointer<Void>, f_hash_size f_hash_size: Int, f_cd_buffer f_cd_buffer: UnsafeMutablePointer<Void>, f_cd_size f_cd_size: Int, f_out_size f_out_size: UnsafeMutablePointer<UInt32>, f_arch f_arch: Int32, __padding __padding: Int32) } ``` |
| To | ``` struct fcodeblobs {     var f_cd_hash: UnsafeMutableRawPointer!     var f_hash_size: Int     var f_cd_buffer: UnsafeMutableRawPointer!     var f_cd_size: Int     var f_out_size: UnsafeMutablePointer<UInt32>!     var f_arch: Int32     var __padding: Int32     init()     init(f_cd_hash f_cd_hash: UnsafeMutableRawPointer!, f_hash_size f_hash_size: Int, f_cd_buffer f_cd_buffer: UnsafeMutableRawPointer!, f_cd_size f_cd_size: Int, f_out_size f_out_size: UnsafeMutablePointer<UInt32>!, f_arch f_arch: Int32, __padding __padding: Int32) } ``` |

Modified fcodeblobs.f_cd_buffer

|  | Declaration |
| --- | --- |
| From | ``` var f_cd_buffer: UnsafeMutablePointer<Void> ``` |
| To | ``` var f_cd_buffer: UnsafeMutableRawPointer! ``` |

Modified fcodeblobs.f_cd_hash

|  | Declaration |
| --- | --- |
| From | ``` var f_cd_hash: UnsafeMutablePointer<Void> ``` |
| To | ``` var f_cd_hash: UnsafeMutableRawPointer! ``` |

Modified fcodeblobs.f_out_size

|  | Declaration |
| --- | --- |
| From | ``` var f_out_size: UnsafeMutablePointer<UInt32> ``` |
| To | ``` var f_out_size: UnsafeMutablePointer<UInt32>! ``` |

Modified fenv_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fenv_t {     var __fpscr: UInt32     var __reserved0: UInt32     var __reserved1: UInt32     var __reserved2: UInt32     init()     init(__fpscr __fpscr: UInt32, __reserved0 __reserved0: UInt32, __reserved1 __reserved1: UInt32, __reserved2 __reserved2: UInt32) } ``` |
| To | ``` struct fenv_t {     var __fpsr: UInt64     var __fpcr: UInt64     init()     init(__fpsr __fpsr: UInt64, __fpcr __fpcr: UInt64) } ``` |

Modified fsignatures [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fsignatures {     var fs_file_start: off_t     var fs_blob_start: UnsafeMutablePointer<Void>     var fs_blob_size: Int     init()     init(fs_file_start fs_file_start: off_t, fs_blob_start fs_blob_start: UnsafeMutablePointer<Void>, fs_blob_size fs_blob_size: Int) } ``` |
| To | ``` struct fsignatures {     var fs_file_start: off_t     var fs_blob_start: UnsafeMutableRawPointer!     var fs_blob_size: Int     init()     init(fs_file_start fs_file_start: off_t, fs_blob_start fs_blob_start: UnsafeMutableRawPointer!, fs_blob_size fs_blob_size: Int) } ``` |

Modified fsignatures.fs_blob_start

|  | Declaration |
| --- | --- |
| From | ``` var fs_blob_start: UnsafeMutablePointer<Void> ``` |
| To | ``` var fs_blob_start: UnsafeMutableRawPointer! ``` |

Modified fssearchblock [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fssearchblock {     var returnattrs: UnsafeMutablePointer<attrlist>     var returnbuffer: UnsafeMutablePointer<Void>     var returnbuffersize: Int     var maxmatches: u_long     var timelimit: timeval     var searchparams1: UnsafeMutablePointer<Void>     var sizeofsearchparams1: Int     var searchparams2: UnsafeMutablePointer<Void>     var sizeofsearchparams2: Int     var searchattrs: attrlist     init()     init(returnattrs returnattrs: UnsafeMutablePointer<attrlist>, returnbuffer returnbuffer: UnsafeMutablePointer<Void>, returnbuffersize returnbuffersize: Int, maxmatches maxmatches: u_long, timelimit timelimit: timeval, searchparams1 searchparams1: UnsafeMutablePointer<Void>, sizeofsearchparams1 sizeofsearchparams1: Int, searchparams2 searchparams2: UnsafeMutablePointer<Void>, sizeofsearchparams2 sizeofsearchparams2: Int, searchattrs searchattrs: attrlist) } ``` |
| To | ``` struct fssearchblock {     var returnattrs: UnsafeMutablePointer<attrlist>!     var returnbuffer: UnsafeMutableRawPointer!     var returnbuffersize: Int     var maxmatches: u_long     var timelimit: timeval     var searchparams1: UnsafeMutableRawPointer!     var sizeofsearchparams1: Int     var searchparams2: UnsafeMutableRawPointer!     var sizeofsearchparams2: Int     var searchattrs: attrlist     init()     init(returnattrs returnattrs: UnsafeMutablePointer<attrlist>!, returnbuffer returnbuffer: UnsafeMutableRawPointer!, returnbuffersize returnbuffersize: Int, maxmatches maxmatches: u_long, timelimit timelimit: timeval, searchparams1 searchparams1: UnsafeMutableRawPointer!, sizeofsearchparams1 sizeofsearchparams1: Int, searchparams2 searchparams2: UnsafeMutableRawPointer!, sizeofsearchparams2 sizeofsearchparams2: Int, searchattrs searchattrs: attrlist) } ``` |

Modified fssearchblock.returnattrs

|  | Declaration |
| --- | --- |
| From | ``` var returnattrs: UnsafeMutablePointer<attrlist> ``` |
| To | ``` var returnattrs: UnsafeMutablePointer<attrlist>! ``` |

Modified fssearchblock.returnbuffer

|  | Declaration |
| --- | --- |
| From | ``` var returnbuffer: UnsafeMutablePointer<Void> ``` |
| To | ``` var returnbuffer: UnsafeMutableRawPointer! ``` |

Modified fssearchblock.searchparams1

|  | Declaration |
| --- | --- |
| From | ``` var searchparams1: UnsafeMutablePointer<Void> ``` |
| To | ``` var searchparams1: UnsafeMutableRawPointer! ``` |

Modified fssearchblock.searchparams2

|  | Declaration |
| --- | --- |
| From | ``` var searchparams2: UnsafeMutablePointer<Void> ``` |
| To | ``` var searchparams2: UnsafeMutableRawPointer! ``` |

Modified glob_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct glob_t {     var gl_pathc: Int     var gl_matchc: Int32     var gl_offs: Int     var gl_flags: Int32     var gl_pathv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var gl_closedir: ((UnsafeMutablePointer<Void>) -> Void)!     var gl_readdir: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<dirent>)!     var gl_opendir: ((UnsafePointer<Int8>) -> UnsafeMutablePointer<Void>)!     var gl_lstat: ((UnsafePointer<Int8>, UnsafeMutablePointer<stat>) -> Int32)!     var gl_stat: ((UnsafePointer<Int8>, UnsafeMutablePointer<stat>) -> Int32)!     init() } ``` |
| To | ``` struct glob_t {     var gl_pathc: Int     var gl_matchc: Int32     var gl_offs: Int     var gl_flags: Int32     var gl_pathv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!     var gl_closedir: ((UnsafeMutableRawPointer?) -> Swift.Void)!     var gl_readdir: ((UnsafeMutableRawPointer?) -> UnsafeMutablePointer<dirent>?)!     var gl_opendir: ((UnsafePointer<Int8>?) -> UnsafeMutableRawPointer?)!     var gl_lstat: ((UnsafePointer<Int8>?, UnsafeMutablePointer<stat>?) -> Int32)!     var gl_stat: ((UnsafePointer<Int8>?, UnsafeMutablePointer<stat>?) -> Int32)!     init() } ``` |

Modified glob_t.gl_closedir

|  | Declaration |
| --- | --- |
| From | ``` var gl_closedir: ((UnsafeMutablePointer<Void>) -> Void)! ``` |
| To | ``` var gl_closedir: ((UnsafeMutableRawPointer?) -> Swift.Void)! ``` |

Modified glob_t.gl_lstat

|  | Declaration |
| --- | --- |
| From | ``` var gl_lstat: ((UnsafePointer<Int8>, UnsafeMutablePointer<stat>) -> Int32)! ``` |
| To | ``` var gl_lstat: ((UnsafePointer<Int8>?, UnsafeMutablePointer<stat>?) -> Int32)! ``` |

Modified glob_t.gl_opendir

|  | Declaration |
| --- | --- |
| From | ``` var gl_opendir: ((UnsafePointer<Int8>) -> UnsafeMutablePointer<Void>)! ``` |
| To | ``` var gl_opendir: ((UnsafePointer<Int8>?) -> UnsafeMutableRawPointer?)! ``` |

Modified glob_t.gl_pathv

|  | Declaration |
| --- | --- |
| From | ``` var gl_pathv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>> ``` |
| To | ``` var gl_pathv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>! ``` |

Modified glob_t.gl_readdir

|  | Declaration |
| --- | --- |
| From | ``` var gl_readdir: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<dirent>)! ``` |
| To | ``` var gl_readdir: ((UnsafeMutableRawPointer?) -> UnsafeMutablePointer<dirent>?)! ``` |

Modified glob_t.gl_stat

|  | Declaration |
| --- | --- |
| From | ``` var gl_stat: ((UnsafePointer<Int8>, UnsafeMutablePointer<stat>) -> Int32)! ``` |
| To | ``` var gl_stat: ((UnsafePointer<Int8>?, UnsafeMutablePointer<stat>?) -> Int32)! ``` |

Modified group [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct group {     var gr_name: UnsafeMutablePointer<Int8>     var gr_passwd: UnsafeMutablePointer<Int8>     var gr_gid: gid_t     var gr_mem: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     init()     init(gr_name gr_name: UnsafeMutablePointer<Int8>, gr_passwd gr_passwd: UnsafeMutablePointer<Int8>, gr_gid gr_gid: gid_t, gr_mem gr_mem: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) } ``` |
| To | ``` struct group {     var gr_name: UnsafeMutablePointer<Int8>!     var gr_passwd: UnsafeMutablePointer<Int8>!     var gr_gid: gid_t     var gr_mem: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!     init()     init(gr_name gr_name: UnsafeMutablePointer<Int8>!, gr_passwd gr_passwd: UnsafeMutablePointer<Int8>!, gr_gid gr_gid: gid_t, gr_mem gr_mem: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) } ``` |

Modified group.gr_mem

|  | Declaration |
| --- | --- |
| From | ``` var gr_mem: UnsafeMutablePointer<UnsafeMutablePointer<Int8>> ``` |
| To | ``` var gr_mem: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>! ``` |

Modified group.gr_name

|  | Declaration |
| --- | --- |
| From | ``` var gr_name: UnsafeMutablePointer<Int8> ``` |
| To | ``` var gr_name: UnsafeMutablePointer<Int8>! ``` |

Modified group.gr_passwd

|  | Declaration |
| --- | --- |
| From | ``` var gr_passwd: UnsafeMutablePointer<Int8> ``` |
| To | ``` var gr_passwd: UnsafeMutablePointer<Int8>! ``` |

Modified hostent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct hostent {     var h_name: UnsafeMutablePointer<Int8>     var h_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var h_addrtype: Int32     var h_length: Int32     var h_addr_list: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     init()     init(h_name h_name: UnsafeMutablePointer<Int8>, h_aliases h_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, h_addrtype h_addrtype: Int32, h_length h_length: Int32, h_addr_list h_addr_list: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) } ``` |
| To | ``` struct hostent {     var h_name: UnsafeMutablePointer<Int8>!     var h_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!     var h_addrtype: Int32     var h_length: Int32     var h_addr_list: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!     init()     init(h_name h_name: UnsafeMutablePointer<Int8>!, h_aliases h_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, h_addrtype h_addrtype: Int32, h_length h_length: Int32, h_addr_list h_addr_list: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) } ``` |

Modified hostent.h_addr_list

|  | Declaration |
| --- | --- |
| From | ``` var h_addr_list: UnsafeMutablePointer<UnsafeMutablePointer<Int8>> ``` |
| To | ``` var h_addr_list: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>! ``` |

Modified hostent.h_aliases

|  | Declaration |
| --- | --- |
| From | ``` var h_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>> ``` |
| To | ``` var h_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>! ``` |

Modified hostent.h_name

|  | Declaration |
| --- | --- |
| From | ``` var h_name: UnsafeMutablePointer<Int8> ``` |
| To | ``` var h_name: UnsafeMutablePointer<Int8>! ``` |

Modified iconv_fallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct iconv_fallbacks {     var mb_to_uc_fallback: iconv_unicode_mb_to_uc_fallback!     var uc_to_mb_fallback: iconv_unicode_uc_to_mb_fallback!     var mb_to_wc_fallback: iconv_wchar_mb_to_wc_fallback!     var wc_to_mb_fallback: iconv_wchar_wc_to_mb_fallback!     var data: UnsafeMutablePointer<Void>     init()     init(mb_to_uc_fallback mb_to_uc_fallback: iconv_unicode_mb_to_uc_fallback!, uc_to_mb_fallback uc_to_mb_fallback: iconv_unicode_uc_to_mb_fallback!, mb_to_wc_fallback mb_to_wc_fallback: iconv_wchar_mb_to_wc_fallback!, wc_to_mb_fallback wc_to_mb_fallback: iconv_wchar_wc_to_mb_fallback!, data data: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct iconv_fallbacks {     var mb_to_uc_fallback: Darwin.iconv_unicode_mb_to_uc_fallback!     var uc_to_mb_fallback: Darwin.iconv_unicode_uc_to_mb_fallback!     var mb_to_wc_fallback: Darwin.iconv_wchar_mb_to_wc_fallback!     var wc_to_mb_fallback: Darwin.iconv_wchar_wc_to_mb_fallback!     var data: UnsafeMutableRawPointer!     init()     init(mb_to_uc_fallback mb_to_uc_fallback: Darwin.iconv_unicode_mb_to_uc_fallback!, uc_to_mb_fallback uc_to_mb_fallback: Darwin.iconv_unicode_uc_to_mb_fallback!, mb_to_wc_fallback mb_to_wc_fallback: Darwin.iconv_wchar_mb_to_wc_fallback!, wc_to_mb_fallback wc_to_mb_fallback: Darwin.iconv_wchar_wc_to_mb_fallback!, data data: UnsafeMutableRawPointer!) } ``` |

Modified iconv_fallbacks.data

|  | Declaration |
| --- | --- |
| From | ``` var data: UnsafeMutablePointer<Void> ``` |
| To | ``` var data: UnsafeMutableRawPointer! ``` |

Modified iconv_fallbacks.mb_to_uc_fallback

|  | Declaration |
| --- | --- |
| From | ``` var mb_to_uc_fallback: iconv_unicode_mb_to_uc_fallback! ``` |
| To | ``` var mb_to_uc_fallback: Darwin.iconv_unicode_mb_to_uc_fallback! ``` |

Modified iconv_fallbacks.mb_to_wc_fallback

|  | Declaration |
| --- | --- |
| From | ``` var mb_to_wc_fallback: iconv_wchar_mb_to_wc_fallback! ``` |
| To | ``` var mb_to_wc_fallback: Darwin.iconv_wchar_mb_to_wc_fallback! ``` |

Modified iconv_fallbacks.uc_to_mb_fallback

|  | Declaration |
| --- | --- |
| From | ``` var uc_to_mb_fallback: iconv_unicode_uc_to_mb_fallback! ``` |
| To | ``` var uc_to_mb_fallback: Darwin.iconv_unicode_uc_to_mb_fallback! ``` |

Modified iconv_fallbacks.wc_to_mb_fallback

|  | Declaration |
| --- | --- |
| From | ``` var wc_to_mb_fallback: iconv_wchar_wc_to_mb_fallback! ``` |
| To | ``` var wc_to_mb_fallback: Darwin.iconv_wchar_wc_to_mb_fallback! ``` |

Modified iconv_hooks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct iconv_hooks {     var uc_hook: iconv_unicode_char_hook!     var wc_hook: iconv_wide_char_hook!     var data: UnsafeMutablePointer<Void>     init()     init(uc_hook uc_hook: iconv_unicode_char_hook!, wc_hook wc_hook: iconv_wide_char_hook!, data data: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct iconv_hooks {     var uc_hook: Darwin.iconv_unicode_char_hook!     var wc_hook: Darwin.iconv_wide_char_hook!     var data: UnsafeMutableRawPointer!     init()     init(uc_hook uc_hook: Darwin.iconv_unicode_char_hook!, wc_hook wc_hook: Darwin.iconv_wide_char_hook!, data data: UnsafeMutableRawPointer!) } ``` |

Modified iconv_hooks.data

|  | Declaration |
| --- | --- |
| From | ``` var data: UnsafeMutablePointer<Void> ``` |
| To | ``` var data: UnsafeMutableRawPointer! ``` |

Modified iconv_hooks.uc_hook

|  | Declaration |
| --- | --- |
| From | ``` var uc_hook: iconv_unicode_char_hook! ``` |
| To | ``` var uc_hook: Darwin.iconv_unicode_char_hook! ``` |

Modified iconv_hooks.wc_hook

|  | Declaration |
| --- | --- |
| From | ``` var wc_hook: iconv_wide_char_hook! ``` |
| To | ``` var wc_hook: Darwin.iconv_wide_char_hook! ``` |

Modified if_clonereq [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct if_clonereq {     var ifcr_total: Int32     var ifcr_count: Int32     var ifcr_buffer: UnsafeMutablePointer<Int8>     init()     init(ifcr_total ifcr_total: Int32, ifcr_count ifcr_count: Int32, ifcr_buffer ifcr_buffer: UnsafeMutablePointer<Int8>) } ``` |
| To | ``` struct if_clonereq {     var ifcr_total: Int32     var ifcr_count: Int32     var ifcr_buffer: UnsafeMutablePointer<Int8>!     init()     init(ifcr_total ifcr_total: Int32, ifcr_count ifcr_count: Int32, ifcr_buffer ifcr_buffer: UnsafeMutablePointer<Int8>!) } ``` |

Modified if_clonereq.ifcr_buffer

|  | Declaration |
| --- | --- |
| From | ``` var ifcr_buffer: UnsafeMutablePointer<Int8> ``` |
| To | ``` var ifcr_buffer: UnsafeMutablePointer<Int8>! ``` |

Modified if_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct if_data {     var ifi_type: u_char     var ifi_typelen: u_char     var ifi_physical: u_char     var ifi_addrlen: u_char     var ifi_hdrlen: u_char     var ifi_recvquota: u_char     var ifi_xmitquota: u_char     var ifi_unused1: u_char     var ifi_mtu: UInt32     var ifi_metric: UInt32     var ifi_baudrate: UInt32     var ifi_ipackets: UInt32     var ifi_ierrors: UInt32     var ifi_opackets: UInt32     var ifi_oerrors: UInt32     var ifi_collisions: UInt32     var ifi_ibytes: UInt32     var ifi_obytes: UInt32     var ifi_imcasts: UInt32     var ifi_omcasts: UInt32     var ifi_iqdrops: UInt32     var ifi_noproto: UInt32     var ifi_recvtiming: UInt32     var ifi_xmittiming: UInt32     var ifi_lastchange: timeval     var ifi_unused2: UInt32     var ifi_hwassist: UInt32     var ifi_reserved1: UInt32     var ifi_reserved2: UInt32     init()     init(ifi_type ifi_type: u_char, ifi_typelen ifi_typelen: u_char, ifi_physical ifi_physical: u_char, ifi_addrlen ifi_addrlen: u_char, ifi_hdrlen ifi_hdrlen: u_char, ifi_recvquota ifi_recvquota: u_char, ifi_xmitquota ifi_xmitquota: u_char, ifi_unused1 ifi_unused1: u_char, ifi_mtu ifi_mtu: UInt32, ifi_metric ifi_metric: UInt32, ifi_baudrate ifi_baudrate: UInt32, ifi_ipackets ifi_ipackets: UInt32, ifi_ierrors ifi_ierrors: UInt32, ifi_opackets ifi_opackets: UInt32, ifi_oerrors ifi_oerrors: UInt32, ifi_collisions ifi_collisions: UInt32, ifi_ibytes ifi_ibytes: UInt32, ifi_obytes ifi_obytes: UInt32, ifi_imcasts ifi_imcasts: UInt32, ifi_omcasts ifi_omcasts: UInt32, ifi_iqdrops ifi_iqdrops: UInt32, ifi_noproto ifi_noproto: UInt32, ifi_recvtiming ifi_recvtiming: UInt32, ifi_xmittiming ifi_xmittiming: UInt32, ifi_lastchange ifi_lastchange: timeval, ifi_unused2 ifi_unused2: UInt32, ifi_hwassist ifi_hwassist: UInt32, ifi_reserved1 ifi_reserved1: UInt32, ifi_reserved2 ifi_reserved2: UInt32) } ``` |
| To | ``` struct if_data {     var ifi_type: u_char     var ifi_typelen: u_char     var ifi_physical: u_char     var ifi_addrlen: u_char     var ifi_hdrlen: u_char     var ifi_recvquota: u_char     var ifi_xmitquota: u_char     var ifi_unused1: u_char     var ifi_mtu: UInt32     var ifi_metric: UInt32     var ifi_baudrate: UInt32     var ifi_ipackets: UInt32     var ifi_ierrors: UInt32     var ifi_opackets: UInt32     var ifi_oerrors: UInt32     var ifi_collisions: UInt32     var ifi_ibytes: UInt32     var ifi_obytes: UInt32     var ifi_imcasts: UInt32     var ifi_omcasts: UInt32     var ifi_iqdrops: UInt32     var ifi_noproto: UInt32     var ifi_recvtiming: UInt32     var ifi_xmittiming: UInt32     var ifi_lastchange: timeval32     var ifi_unused2: UInt32     var ifi_hwassist: UInt32     var ifi_reserved1: UInt32     var ifi_reserved2: UInt32     init()     init(ifi_type ifi_type: u_char, ifi_typelen ifi_typelen: u_char, ifi_physical ifi_physical: u_char, ifi_addrlen ifi_addrlen: u_char, ifi_hdrlen ifi_hdrlen: u_char, ifi_recvquota ifi_recvquota: u_char, ifi_xmitquota ifi_xmitquota: u_char, ifi_unused1 ifi_unused1: u_char, ifi_mtu ifi_mtu: UInt32, ifi_metric ifi_metric: UInt32, ifi_baudrate ifi_baudrate: UInt32, ifi_ipackets ifi_ipackets: UInt32, ifi_ierrors ifi_ierrors: UInt32, ifi_opackets ifi_opackets: UInt32, ifi_oerrors ifi_oerrors: UInt32, ifi_collisions ifi_collisions: UInt32, ifi_ibytes ifi_ibytes: UInt32, ifi_obytes ifi_obytes: UInt32, ifi_imcasts ifi_imcasts: UInt32, ifi_omcasts ifi_omcasts: UInt32, ifi_iqdrops ifi_iqdrops: UInt32, ifi_noproto ifi_noproto: UInt32, ifi_recvtiming ifi_recvtiming: UInt32, ifi_xmittiming ifi_xmittiming: UInt32, ifi_lastchange ifi_lastchange: timeval32, ifi_unused2 ifi_unused2: UInt32, ifi_hwassist ifi_hwassist: UInt32, ifi_reserved1 ifi_reserved1: UInt32, ifi_reserved2 ifi_reserved2: UInt32) } ``` |

Modified if_data.ifi_lastchange

|  | Declaration |
| --- | --- |
| From | ``` var ifi_lastchange: timeval ``` |
| To | ``` var ifi_lastchange: timeval32 ``` |

Modified if_data64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct if_data64 {     var ifi_type: u_char     var ifi_typelen: u_char     var ifi_physical: u_char     var ifi_addrlen: u_char     var ifi_hdrlen: u_char     var ifi_recvquota: u_char     var ifi_xmitquota: u_char     var ifi_unused1: u_char     var ifi_mtu: UInt32     var ifi_metric: UInt32     var ifi_baudrate: UInt64     var ifi_ipackets: UInt64     var ifi_ierrors: UInt64     var ifi_opackets: UInt64     var ifi_oerrors: UInt64     var ifi_collisions: UInt64     var ifi_ibytes: UInt64     var ifi_obytes: UInt64     var ifi_imcasts: UInt64     var ifi_omcasts: UInt64     var ifi_iqdrops: UInt64     var ifi_noproto: UInt64     var ifi_recvtiming: UInt32     var ifi_xmittiming: UInt32     var ifi_lastchange: timeval     init()     init(ifi_type ifi_type: u_char, ifi_typelen ifi_typelen: u_char, ifi_physical ifi_physical: u_char, ifi_addrlen ifi_addrlen: u_char, ifi_hdrlen ifi_hdrlen: u_char, ifi_recvquota ifi_recvquota: u_char, ifi_xmitquota ifi_xmitquota: u_char, ifi_unused1 ifi_unused1: u_char, ifi_mtu ifi_mtu: UInt32, ifi_metric ifi_metric: UInt32, ifi_baudrate ifi_baudrate: UInt64, ifi_ipackets ifi_ipackets: UInt64, ifi_ierrors ifi_ierrors: UInt64, ifi_opackets ifi_opackets: UInt64, ifi_oerrors ifi_oerrors: UInt64, ifi_collisions ifi_collisions: UInt64, ifi_ibytes ifi_ibytes: UInt64, ifi_obytes ifi_obytes: UInt64, ifi_imcasts ifi_imcasts: UInt64, ifi_omcasts ifi_omcasts: UInt64, ifi_iqdrops ifi_iqdrops: UInt64, ifi_noproto ifi_noproto: UInt64, ifi_recvtiming ifi_recvtiming: UInt32, ifi_xmittiming ifi_xmittiming: UInt32, ifi_lastchange ifi_lastchange: timeval) } ``` |
| To | ``` struct if_data64 {     var ifi_type: u_char     var ifi_typelen: u_char     var ifi_physical: u_char     var ifi_addrlen: u_char     var ifi_hdrlen: u_char     var ifi_recvquota: u_char     var ifi_xmitquota: u_char     var ifi_unused1: u_char     var ifi_mtu: UInt32     var ifi_metric: UInt32     var ifi_baudrate: UInt64     var ifi_ipackets: UInt64     var ifi_ierrors: UInt64     var ifi_opackets: UInt64     var ifi_oerrors: UInt64     var ifi_collisions: UInt64     var ifi_ibytes: UInt64     var ifi_obytes: UInt64     var ifi_imcasts: UInt64     var ifi_omcasts: UInt64     var ifi_iqdrops: UInt64     var ifi_noproto: UInt64     var ifi_recvtiming: UInt32     var ifi_xmittiming: UInt32     var ifi_lastchange: timeval32     init()     init(ifi_type ifi_type: u_char, ifi_typelen ifi_typelen: u_char, ifi_physical ifi_physical: u_char, ifi_addrlen ifi_addrlen: u_char, ifi_hdrlen ifi_hdrlen: u_char, ifi_recvquota ifi_recvquota: u_char, ifi_xmitquota ifi_xmitquota: u_char, ifi_unused1 ifi_unused1: u_char, ifi_mtu ifi_mtu: UInt32, ifi_metric ifi_metric: UInt32, ifi_baudrate ifi_baudrate: UInt64, ifi_ipackets ifi_ipackets: UInt64, ifi_ierrors ifi_ierrors: UInt64, ifi_opackets ifi_opackets: UInt64, ifi_oerrors ifi_oerrors: UInt64, ifi_collisions ifi_collisions: UInt64, ifi_ibytes ifi_ibytes: UInt64, ifi_obytes ifi_obytes: UInt64, ifi_imcasts ifi_imcasts: UInt64, ifi_omcasts ifi_omcasts: UInt64, ifi_iqdrops ifi_iqdrops: UInt64, ifi_noproto ifi_noproto: UInt64, ifi_recvtiming ifi_recvtiming: UInt32, ifi_xmittiming ifi_xmittiming: UInt32, ifi_lastchange ifi_lastchange: timeval32) } ``` |

Modified if_data64.ifi_lastchange

|  | Declaration |
| --- | --- |
| From | ``` var ifi_lastchange: timeval ``` |
| To | ``` var ifi_lastchange: timeval32 ``` |

Modified if_nameindex [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct if_nameindex {     var if_index: UInt32     var if_name: UnsafeMutablePointer<Int8>     init()     init(if_index if_index: UInt32, if_name if_name: UnsafeMutablePointer<Int8>) } ``` |
| To | ``` struct if_nameindex {     var if_index: UInt32     var if_name: UnsafeMutablePointer<Int8>!     init()     init(if_index if_index: UInt32, if_name if_name: UnsafeMutablePointer<Int8>!) } ``` |

Modified if_nameindex.if_name

|  | Declaration |
| --- | --- |
| From | ``` var if_name: UnsafeMutablePointer<Int8> ``` |
| To | ``` var if_name: UnsafeMutablePointer<Int8>! ``` |

Modified ifconf [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifconf {     struct __Unnamed_union_ifc_ifcu {         var ifcu_buf: caddr_t         var ifcu_req: UnsafeMutablePointer<ifreq>         init(ifcu_buf ifcu_buf: caddr_t)         init(ifcu_req ifcu_req: UnsafeMutablePointer<ifreq>)         init()     }     var ifc_len: Int32     var ifc_ifcu: ifconf.__Unnamed_union_ifc_ifcu     init()     init(ifc_len ifc_len: Int32, ifc_ifcu ifc_ifcu: ifconf.__Unnamed_union_ifc_ifcu) } ``` |
| To | ``` struct ifconf {     struct __Unnamed_union_ifc_ifcu {         var ifcu_buf: caddr_t!         var ifcu_req: UnsafeMutablePointer<ifreq>!         init(ifcu_buf ifcu_buf: caddr_t!)         init(ifcu_req ifcu_req: UnsafeMutablePointer<ifreq>!)         init()     }     var ifc_len: Int32     var ifc_ifcu: ifconf.__Unnamed_union_ifc_ifcu     init()     init(ifc_len ifc_len: Int32, ifc_ifcu ifc_ifcu: ifconf.__Unnamed_union_ifc_ifcu) } ``` |

Modified ifdrv [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifdrv {     var ifd_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ifd_cmd: UInt     var ifd_len: Int     var ifd_data: UnsafeMutablePointer<Void>     init()     init(ifd_name ifd_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifd_cmd ifd_cmd: UInt, ifd_len ifd_len: Int, ifd_data ifd_data: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct ifdrv {     var ifd_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ifd_cmd: UInt     var ifd_len: Int     var ifd_data: UnsafeMutableRawPointer!     init()     init(ifd_name ifd_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifd_cmd ifd_cmd: UInt, ifd_len ifd_len: Int, ifd_data ifd_data: UnsafeMutableRawPointer!) } ``` |

Modified ifdrv.ifd_data

|  | Declaration |
| --- | --- |
| From | ``` var ifd_data: UnsafeMutablePointer<Void> ``` |
| To | ``` var ifd_data: UnsafeMutableRawPointer! ``` |

Modified ifkpi [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifkpi {     struct __Unnamed_union_ifk_data {         var ifk_ptr: UnsafeMutablePointer<Void>         var ifk_value: Int32         init(ifk_ptr ifk_ptr: UnsafeMutablePointer<Void>)         init(ifk_value ifk_value: Int32)         init()     }     var ifk_module_id: UInt32     var ifk_type: UInt32     var ifk_data: ifkpi.__Unnamed_union_ifk_data     init()     init(ifk_module_id ifk_module_id: UInt32, ifk_type ifk_type: UInt32, ifk_data ifk_data: ifkpi.__Unnamed_union_ifk_data) } ``` |
| To | ``` struct ifkpi {     struct __Unnamed_union_ifk_data {         var ifk_ptr: UnsafeMutableRawPointer!         var ifk_value: Int32         init(ifk_ptr ifk_ptr: UnsafeMutableRawPointer!)         init(ifk_value ifk_value: Int32)         init()     }     var ifk_module_id: UInt32     var ifk_type: UInt32     var ifk_data: ifkpi.__Unnamed_union_ifk_data     init()     init(ifk_module_id ifk_module_id: UInt32, ifk_type ifk_type: UInt32, ifk_data ifk_data: ifkpi.__Unnamed_union_ifk_data) } ``` |

Modified ifmediareq [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifmediareq {     var ifm_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ifm_current: Int32     var ifm_mask: Int32     var ifm_status: Int32     var ifm_active: Int32     var ifm_count: Int32     var ifm_ulist: UnsafeMutablePointer<Int32>     init()     init(ifm_name ifm_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifm_current ifm_current: Int32, ifm_mask ifm_mask: Int32, ifm_status ifm_status: Int32, ifm_active ifm_active: Int32, ifm_count ifm_count: Int32, ifm_ulist ifm_ulist: UnsafeMutablePointer<Int32>) } ``` |
| To | ``` struct ifmediareq {     var ifm_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ifm_current: Int32     var ifm_mask: Int32     var ifm_status: Int32     var ifm_active: Int32     var ifm_count: Int32     var ifm_ulist: UnsafeMutablePointer<Int32>!     init()     init(ifm_name ifm_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifm_current ifm_current: Int32, ifm_mask ifm_mask: Int32, ifm_status ifm_status: Int32, ifm_active ifm_active: Int32, ifm_count ifm_count: Int32, ifm_ulist ifm_ulist: UnsafeMutablePointer<Int32>!) } ``` |

Modified ifmediareq.ifm_ulist

|  | Declaration |
| --- | --- |
| From | ``` var ifm_ulist: UnsafeMutablePointer<Int32> ``` |
| To | ``` var ifm_ulist: UnsafeMutablePointer<Int32>! ``` |

Modified ifqueue [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifqueue {     var ifq_head: UnsafeMutablePointer<Void>     var ifq_tail: UnsafeMutablePointer<Void>     var ifq_len: Int32     var ifq_maxlen: Int32     var ifq_drops: Int32     init()     init(ifq_head ifq_head: UnsafeMutablePointer<Void>, ifq_tail ifq_tail: UnsafeMutablePointer<Void>, ifq_len ifq_len: Int32, ifq_maxlen ifq_maxlen: Int32, ifq_drops ifq_drops: Int32) } ``` |
| To | ``` struct ifqueue {     var ifq_head: UnsafeMutableRawPointer!     var ifq_tail: UnsafeMutableRawPointer!     var ifq_len: Int32     var ifq_maxlen: Int32     var ifq_drops: Int32     init()     init(ifq_head ifq_head: UnsafeMutableRawPointer!, ifq_tail ifq_tail: UnsafeMutableRawPointer!, ifq_len ifq_len: Int32, ifq_maxlen ifq_maxlen: Int32, ifq_drops ifq_drops: Int32) } ``` |

Modified ifqueue.ifq_head

|  | Declaration |
| --- | --- |
| From | ``` var ifq_head: UnsafeMutablePointer<Void> ``` |
| To | ``` var ifq_head: UnsafeMutableRawPointer! ``` |

Modified ifqueue.ifq_tail

|  | Declaration |
| --- | --- |
| From | ``` var ifq_tail: UnsafeMutablePointer<Void> ``` |
| To | ``` var ifq_tail: UnsafeMutableRawPointer! ``` |

Modified ifreq [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifreq {     struct __Unnamed_union_ifr_ifru {         var ifru_addr: sockaddr         var ifru_dstaddr: sockaddr         var ifru_broadaddr: sockaddr         var ifru_flags: Int16         var ifru_metric: Int32         var ifru_mtu: Int32         var ifru_phys: Int32         var ifru_media: Int32         var ifru_intval: Int32         var ifru_data: caddr_t         var ifru_devmtu: ifdevmtu         var ifru_kpi: ifkpi         var ifru_wake_flags: UInt32         var ifru_route_refcnt: UInt32         var ifru_cap: (Int32, Int32)         init(ifru_addr ifru_addr: sockaddr)         init(ifru_dstaddr ifru_dstaddr: sockaddr)         init(ifru_broadaddr ifru_broadaddr: sockaddr)         init(ifru_flags ifru_flags: Int16)         init(ifru_metric ifru_metric: Int32)         init(ifru_mtu ifru_mtu: Int32)         init(ifru_phys ifru_phys: Int32)         init(ifru_media ifru_media: Int32)         init(ifru_intval ifru_intval: Int32)         init(ifru_data ifru_data: caddr_t)         init(ifru_devmtu ifru_devmtu: ifdevmtu)         init(ifru_kpi ifru_kpi: ifkpi)         init(ifru_wake_flags ifru_wake_flags: UInt32)         init(ifru_route_refcnt ifru_route_refcnt: UInt32)         init(ifru_cap ifru_cap: (Int32, Int32))         init()     }     var ifr_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ifr_ifru: ifreq.__Unnamed_union_ifr_ifru     init()     init(ifr_name ifr_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifr_ifru ifr_ifru: ifreq.__Unnamed_union_ifr_ifru) } ``` |
| To | ``` struct ifreq {     struct __Unnamed_union_ifr_ifru {         var ifru_addr: sockaddr         var ifru_dstaddr: sockaddr         var ifru_broadaddr: sockaddr         var ifru_flags: Int16         var ifru_metric: Int32         var ifru_mtu: Int32         var ifru_phys: Int32         var ifru_media: Int32         var ifru_intval: Int32         var ifru_data: caddr_t!         var ifru_devmtu: ifdevmtu         var ifru_kpi: ifkpi         var ifru_wake_flags: UInt32         var ifru_route_refcnt: UInt32         var ifru_cap: (Int32, Int32)         init(ifru_addr ifru_addr: sockaddr)         init(ifru_dstaddr ifru_dstaddr: sockaddr)         init(ifru_broadaddr ifru_broadaddr: sockaddr)         init(ifru_flags ifru_flags: Int16)         init(ifru_metric ifru_metric: Int32)         init(ifru_mtu ifru_mtu: Int32)         init(ifru_phys ifru_phys: Int32)         init(ifru_media ifru_media: Int32)         init(ifru_intval ifru_intval: Int32)         init(ifru_data ifru_data: caddr_t!)         init(ifru_devmtu ifru_devmtu: ifdevmtu)         init(ifru_kpi ifru_kpi: ifkpi)         init(ifru_wake_flags ifru_wake_flags: UInt32)         init(ifru_route_refcnt ifru_route_refcnt: UInt32)         init(ifru_cap ifru_cap: (Int32, Int32))         init()     }     var ifr_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ifr_ifru: ifreq.__Unnamed_union_ifr_ifru     init()     init(ifr_name ifr_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifr_ifru ifr_ifru: ifreq.__Unnamed_union_ifr_ifru) } ``` |

Modified imaxdiv_t.init(quot: intmax_t, rem: intmax_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.3 |

Modified iovec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct iovec {     var iov_base: UnsafeMutablePointer<Void>     var iov_len: Int     init()     init(iov_base iov_base: UnsafeMutablePointer<Void>, iov_len iov_len: Int) } ``` |
| To | ``` struct iovec {     var iov_base: UnsafeMutableRawPointer!     var iov_len: Int     init()     init(iov_base iov_base: UnsafeMutableRawPointer!, iov_len iov_len: Int) } ``` |

Modified iovec.iov_base

|  | Declaration |
| --- | --- |
| From | ``` var iov_base: UnsafeMutablePointer<Void> ``` |
| To | ``` var iov_base: UnsafeMutableRawPointer! ``` |

Modified kevent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kevent {     var ident: UInt     var filter: Int16     var flags: UInt16     var fflags: UInt32     var data: Int     var udata: UnsafeMutablePointer<Void>     init()     init(ident ident: UInt, filter filter: Int16, flags flags: UInt16, fflags fflags: UInt32, data data: Int, udata udata: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct kevent {     var ident: UInt     var filter: Int16     var flags: UInt16     var fflags: UInt32     var data: Int     var udata: UnsafeMutableRawPointer!     init()     init(ident ident: UInt, filter filter: Int16, flags flags: UInt16, fflags fflags: UInt32, data data: Int, udata udata: UnsafeMutableRawPointer!) } ``` |

Modified kevent.udata

|  | Declaration |
| --- | --- |
| From | ``` var udata: UnsafeMutablePointer<Void> ``` |
| To | ``` var udata: UnsafeMutableRawPointer! ``` |

Modified klist [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct klist {     var slh_first: COpaquePointer     init()     init(slh_first slh_first: COpaquePointer) } ``` |
| To | ``` struct klist {     var slh_first: OpaquePointer!     init()     init(slh_first slh_first: OpaquePointer!) } ``` |

Modified klist.slh_first

|  | Declaration |
| --- | --- |
| From | ``` var slh_first: COpaquePointer ``` |
| To | ``` var slh_first: OpaquePointer! ``` |

Modified kmod_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kmod_info {     var next: UnsafeMutablePointer<kmod_info>     var info_version: Int32     var id: UInt32     var name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var version: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var reference_count: Int32     var reference_list: UnsafeMutablePointer<kmod_reference_t>     var address: vm_address_t     var size: vm_size_t     var hdr_size: vm_size_t     var start: ((UnsafeMutablePointer<kmod_info>, UnsafeMutablePointer<Void>) -> kern_return_t)!     var stop: ((UnsafeMutablePointer<kmod_info>, UnsafeMutablePointer<Void>) -> kern_return_t)!     init()     init(next next: UnsafeMutablePointer<kmod_info>, info_version info_version: Int32, id id: UInt32, name name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), version version: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), reference_count reference_count: Int32, reference_list reference_list: UnsafeMutablePointer<kmod_reference_t>, address address: vm_address_t, size size: vm_size_t, hdr_size hdr_size: vm_size_t, start start: ((UnsafeMutablePointer<kmod_info>, UnsafeMutablePointer<Void>) -> kern_return_t)!, stop stop: ((UnsafeMutablePointer<kmod_info>, UnsafeMutablePointer<Void>) -> kern_return_t)!) } ``` |
| To | ``` struct kmod_info {     var next: UnsafeMutablePointer<kmod_info>!     var info_version: Int32     var id: UInt32     var name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var version: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var reference_count: Int32     var reference_list: UnsafeMutablePointer<kmod_reference_t>!     var address: vm_address_t     var size: vm_size_t     var hdr_size: vm_size_t     var start: ((UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!     var stop: ((UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!     init()     init(next next: UnsafeMutablePointer<kmod_info>!, info_version info_version: Int32, id id: UInt32, name name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), version version: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), reference_count reference_count: Int32, reference_list reference_list: UnsafeMutablePointer<kmod_reference_t>!, address address: vm_address_t, size size: vm_size_t, hdr_size hdr_size: vm_size_t, start start: (@escaping (UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!, stop stop: (@escaping (UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!) } ``` |

Modified kmod_info.next

|  | Declaration |
| --- | --- |
| From | ``` var next: UnsafeMutablePointer<kmod_info> ``` |
| To | ``` var next: UnsafeMutablePointer<kmod_info>! ``` |

Modified kmod_info.reference_list

|  | Declaration |
| --- | --- |
| From | ``` var reference_list: UnsafeMutablePointer<kmod_reference_t> ``` |
| To | ``` var reference_list: UnsafeMutablePointer<kmod_reference_t>! ``` |

Modified kmod_info.start

|  | Declaration |
| --- | --- |
| From | ``` var start: ((UnsafeMutablePointer<kmod_info>, UnsafeMutablePointer<Void>) -> kern_return_t)! ``` |
| To | ``` var start: ((UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)! ``` |

Modified kmod_info.stop

|  | Declaration |
| --- | --- |
| From | ``` var stop: ((UnsafeMutablePointer<kmod_info>, UnsafeMutablePointer<Void>) -> kern_return_t)! ``` |
| To | ``` var stop: ((UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)! ``` |

Modified kmod_reference [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kmod_reference {     var next: UnsafeMutablePointer<kmod_reference>     var info: UnsafeMutablePointer<kmod_info>     init()     init(next next: UnsafeMutablePointer<kmod_reference>, info info: UnsafeMutablePointer<kmod_info>) } ``` |
| To | ``` struct kmod_reference {     var next: UnsafeMutablePointer<kmod_reference>!     var info: UnsafeMutablePointer<kmod_info>!     init()     init(next next: UnsafeMutablePointer<kmod_reference>!, info info: UnsafeMutablePointer<kmod_info>!) } ``` |

Modified kmod_reference.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafeMutablePointer<kmod_info> ``` |
| To | ``` var info: UnsafeMutablePointer<kmod_info>! ``` |

Modified kmod_reference.next

|  | Declaration |
| --- | --- |
| From | ``` var next: UnsafeMutablePointer<kmod_reference> ``` |
| To | ``` var next: UnsafeMutablePointer<kmod_reference>! ``` |

Modified lconv [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct lconv {     var decimal_point: UnsafeMutablePointer<Int8>     var thousands_sep: UnsafeMutablePointer<Int8>     var grouping: UnsafeMutablePointer<Int8>     var int_curr_symbol: UnsafeMutablePointer<Int8>     var currency_symbol: UnsafeMutablePointer<Int8>     var mon_decimal_point: UnsafeMutablePointer<Int8>     var mon_thousands_sep: UnsafeMutablePointer<Int8>     var mon_grouping: UnsafeMutablePointer<Int8>     var positive_sign: UnsafeMutablePointer<Int8>     var negative_sign: UnsafeMutablePointer<Int8>     var int_frac_digits: Int8     var frac_digits: Int8     var p_cs_precedes: Int8     var p_sep_by_space: Int8     var n_cs_precedes: Int8     var n_sep_by_space: Int8     var p_sign_posn: Int8     var n_sign_posn: Int8     var int_p_cs_precedes: Int8     var int_n_cs_precedes: Int8     var int_p_sep_by_space: Int8     var int_n_sep_by_space: Int8     var int_p_sign_posn: Int8     var int_n_sign_posn: Int8     init()     init(decimal_point decimal_point: UnsafeMutablePointer<Int8>, thousands_sep thousands_sep: UnsafeMutablePointer<Int8>, grouping grouping: UnsafeMutablePointer<Int8>, int_curr_symbol int_curr_symbol: UnsafeMutablePointer<Int8>, currency_symbol currency_symbol: UnsafeMutablePointer<Int8>, mon_decimal_point mon_decimal_point: UnsafeMutablePointer<Int8>, mon_thousands_sep mon_thousands_sep: UnsafeMutablePointer<Int8>, mon_grouping mon_grouping: UnsafeMutablePointer<Int8>, positive_sign positive_sign: UnsafeMutablePointer<Int8>, negative_sign negative_sign: UnsafeMutablePointer<Int8>, int_frac_digits int_frac_digits: Int8, frac_digits frac_digits: Int8, p_cs_precedes p_cs_precedes: Int8, p_sep_by_space p_sep_by_space: Int8, n_cs_precedes n_cs_precedes: Int8, n_sep_by_space n_sep_by_space: Int8, p_sign_posn p_sign_posn: Int8, n_sign_posn n_sign_posn: Int8, int_p_cs_precedes int_p_cs_precedes: Int8, int_n_cs_precedes int_n_cs_precedes: Int8, int_p_sep_by_space int_p_sep_by_space: Int8, int_n_sep_by_space int_n_sep_by_space: Int8, int_p_sign_posn int_p_sign_posn: Int8, int_n_sign_posn int_n_sign_posn: Int8) } ``` |
| To | ``` struct lconv {     var decimal_point: UnsafeMutablePointer<Int8>!     var thousands_sep: UnsafeMutablePointer<Int8>!     var grouping: UnsafeMutablePointer<Int8>!     var int_curr_symbol: UnsafeMutablePointer<Int8>!     var currency_symbol: UnsafeMutablePointer<Int8>!     var mon_decimal_point: UnsafeMutablePointer<Int8>!     var mon_thousands_sep: UnsafeMutablePointer<Int8>!     var mon_grouping: UnsafeMutablePointer<Int8>!     var positive_sign: UnsafeMutablePointer<Int8>!     var negative_sign: UnsafeMutablePointer<Int8>!     var int_frac_digits: Int8     var frac_digits: Int8     var p_cs_precedes: Int8     var p_sep_by_space: Int8     var n_cs_precedes: Int8     var n_sep_by_space: Int8     var p_sign_posn: Int8     var n_sign_posn: Int8     var int_p_cs_precedes: Int8     var int_n_cs_precedes: Int8     var int_p_sep_by_space: Int8     var int_n_sep_by_space: Int8     var int_p_sign_posn: Int8     var int_n_sign_posn: Int8     init()     init(decimal_point decimal_point: UnsafeMutablePointer<Int8>!, thousands_sep thousands_sep: UnsafeMutablePointer<Int8>!, grouping grouping: UnsafeMutablePointer<Int8>!, int_curr_symbol int_curr_symbol: UnsafeMutablePointer<Int8>!, currency_symbol currency_symbol: UnsafeMutablePointer<Int8>!, mon_decimal_point mon_decimal_point: UnsafeMutablePointer<Int8>!, mon_thousands_sep mon_thousands_sep: UnsafeMutablePointer<Int8>!, mon_grouping mon_grouping: UnsafeMutablePointer<Int8>!, positive_sign positive_sign: UnsafeMutablePointer<Int8>!, negative_sign negative_sign: UnsafeMutablePointer<Int8>!, int_frac_digits int_frac_digits: Int8, frac_digits frac_digits: Int8, p_cs_precedes p_cs_precedes: Int8, p_sep_by_space p_sep_by_space: Int8, n_cs_precedes n_cs_precedes: Int8, n_sep_by_space n_sep_by_space: Int8, p_sign_posn p_sign_posn: Int8, n_sign_posn n_sign_posn: Int8, int_p_cs_precedes int_p_cs_precedes: Int8, int_n_cs_precedes int_n_cs_precedes: Int8, int_p_sep_by_space int_p_sep_by_space: Int8, int_n_sep_by_space int_n_sep_by_space: Int8, int_p_sign_posn int_p_sign_posn: Int8, int_n_sign_posn int_n_sign_posn: Int8) } ``` |

Modified lconv.currency_symbol

|  | Declaration |
| --- | --- |
| From | ``` var currency_symbol: UnsafeMutablePointer<Int8> ``` |
| To | ``` var currency_symbol: UnsafeMutablePointer<Int8>! ``` |

Modified lconv.decimal_point

|  | Declaration |
| --- | --- |
| From | ``` var decimal_point: UnsafeMutablePointer<Int8> ``` |
| To | ``` var decimal_point: UnsafeMutablePointer<Int8>! ``` |

Modified lconv.grouping

|  | Declaration |
| --- | --- |
| From | ``` var grouping: UnsafeMutablePointer<Int8> ``` |
| To | ``` var grouping: UnsafeMutablePointer<Int8>! ``` |

Modified lconv.int_curr_symbol

|  | Declaration |
| --- | --- |
| From | ``` var int_curr_symbol: UnsafeMutablePointer<Int8> ``` |
| To | ``` var int_curr_symbol: UnsafeMutablePointer<Int8>! ``` |

Modified lconv.mon_decimal_point

|  | Declaration |
| --- | --- |
| From | ``` var mon_decimal_point: UnsafeMutablePointer<Int8> ``` |
| To | ``` var mon_decimal_point: UnsafeMutablePointer<Int8>! ``` |

Modified lconv.mon_grouping

|  | Declaration |
| --- | --- |
| From | ``` var mon_grouping: UnsafeMutablePointer<Int8> ``` |
| To | ``` var mon_grouping: UnsafeMutablePointer<Int8>! ``` |

Modified lconv.mon_thousands_sep

|  | Declaration |
| --- | --- |
| From | ``` var mon_thousands_sep: UnsafeMutablePointer<Int8> ``` |
| To | ``` var mon_thousands_sep: UnsafeMutablePointer<Int8>! ``` |

Modified lconv.negative_sign

|  | Declaration |
| --- | --- |
| From | ``` var negative_sign: UnsafeMutablePointer<Int8> ``` |
| To | ``` var negative_sign: UnsafeMutablePointer<Int8>! ``` |

Modified lconv.positive_sign

|  | Declaration |
| --- | --- |
| From | ``` var positive_sign: UnsafeMutablePointer<Int8> ``` |
| To | ``` var positive_sign: UnsafeMutablePointer<Int8>! ``` |

Modified lconv.thousands_sep

|  | Declaration |
| --- | --- |
| From | ``` var thousands_sep: UnsafeMutablePointer<Int8> ``` |
| To | ``` var thousands_sep: UnsafeMutablePointer<Int8>! ``` |

Modified mach_memory_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_memory_info {     var flags: UInt64     var site: UInt64     var size: UInt64     var free: UInt64     var largest: UInt64     var _resv: (UInt64, UInt64, UInt64)     init()     init(flags flags: UInt64, site site: UInt64, size size: UInt64, free free: UInt64, largest largest: UInt64, _resv _resv: (UInt64, UInt64, UInt64)) } ``` |
| To | ``` struct mach_memory_info {     var flags: UInt64     var site: UInt64     var size: UInt64     var free: UInt64     var largest: UInt64     var collectable_bytes: UInt64     var _resv: (UInt64, UInt64)     init()     init(flags flags: UInt64, site site: UInt64, size size: UInt64, free free: UInt64, largest largest: UInt64, collectable_bytes collectable_bytes: UInt64, _resv _resv: (UInt64, UInt64)) } ``` |

Modified mach_msg_context_trailer_t.init(msgh_trailer_type: mach_msg_trailer_type_t, msgh_trailer_size: mach_msg_trailer_size_t, msgh_seqno: mach_port_seqno_t, msgh_sender: security_token_t, msgh_audit: audit_token_t, msgh_context: mach_port_context_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.3 |

Modified mach_msg_mac_trailer_t.init(msgh_trailer_type: mach_msg_trailer_type_t, msgh_trailer_size: mach_msg_trailer_size_t, msgh_seqno: mach_port_seqno_t, msgh_sender: security_token_t, msgh_audit: audit_token_t, msgh_context: mach_port_context_t, msgh_ad: Int32, msgh_labels: msg_labels_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.3 |

Modified mach_msg_ool_descriptor_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_ool_descriptor_t {     var address: UnsafeMutablePointer<Void>     var size: mach_msg_size_t     var deallocate: boolean_t     var copy: mach_msg_copy_options_t     var pad1: UInt32     var type: mach_msg_descriptor_type_t     init()     init(address address: UnsafeMutablePointer<Void>, size size: mach_msg_size_t, deallocate deallocate: boolean_t, copy copy: mach_msg_copy_options_t, pad1 pad1: UInt32, type type: mach_msg_descriptor_type_t) } ``` |
| To | ``` struct mach_msg_ool_descriptor_t {     var address: UnsafeMutableRawPointer!     var deallocate: boolean_t     var copy: mach_msg_copy_options_t     var pad1: UInt32     var type: mach_msg_descriptor_type_t     var size: mach_msg_size_t     init()     init(address address: UnsafeMutableRawPointer!, deallocate deallocate: boolean_t, copy copy: mach_msg_copy_options_t, pad1 pad1: UInt32, type type: mach_msg_descriptor_type_t, size size: mach_msg_size_t) } ``` |

Modified mach_msg_ool_descriptor_t.address

|  | Declaration |
| --- | --- |
| From | ``` var address: UnsafeMutablePointer<Void> ``` |
| To | ``` var address: UnsafeMutableRawPointer! ``` |

Modified mach_msg_ool_ports_descriptor_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_ool_ports_descriptor_t {     var address: UnsafeMutablePointer<Void>     var count: mach_msg_size_t     var deallocate: boolean_t     var copy: mach_msg_copy_options_t     var disposition: mach_msg_type_name_t     var type: mach_msg_descriptor_type_t     init()     init(address address: UnsafeMutablePointer<Void>, count count: mach_msg_size_t, deallocate deallocate: boolean_t, copy copy: mach_msg_copy_options_t, disposition disposition: mach_msg_type_name_t, type type: mach_msg_descriptor_type_t) } ``` |
| To | ``` struct mach_msg_ool_ports_descriptor_t {     var address: UnsafeMutableRawPointer!     var deallocate: boolean_t     var copy: mach_msg_copy_options_t     var disposition: mach_msg_type_name_t     var type: mach_msg_descriptor_type_t     var count: mach_msg_size_t     init()     init(address address: UnsafeMutableRawPointer!, deallocate deallocate: boolean_t, copy copy: mach_msg_copy_options_t, disposition disposition: mach_msg_type_name_t, type type: mach_msg_descriptor_type_t, count count: mach_msg_size_t) } ``` |

Modified mach_msg_ool_ports_descriptor_t.address

|  | Declaration |
| --- | --- |
| From | ``` var address: UnsafeMutablePointer<Void> ``` |
| To | ``` var address: UnsafeMutableRawPointer! ``` |

Modified malloc_introspection_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct malloc_introspection_t {     var enumerator: ((task_t, UnsafeMutablePointer<Void>, UInt32, vm_address_t, ((task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> kern_return_t)!, ((task_t, UnsafeMutablePointer<Void>, UInt32, UnsafeMutablePointer<vm_range_t>, UInt32) -> Void)!) -> kern_return_t)!     var good_size: ((UnsafeMutablePointer<malloc_zone_t>, Int) -> Int)!     var check: ((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)!     var print: ((UnsafeMutablePointer<malloc_zone_t>, boolean_t) -> Void)!     var log: ((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>) -> Void)!     var force_lock: ((UnsafeMutablePointer<malloc_zone_t>) -> Void)!     var force_unlock: ((UnsafeMutablePointer<malloc_zone_t>) -> Void)!     var statistics: ((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<malloc_statistics_t>) -> Void)!     var zone_locked: ((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)!     var enable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)!     var disable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>) -> Void)!     var discharge: ((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>) -> Void)!     var enumerate_discharged_pointers: ((UnsafeMutablePointer<malloc_zone_t>, ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)!) -> Void)!     init()     init(enumerator enumerator: ((task_t, UnsafeMutablePointer<Void>, UInt32, vm_address_t, ((task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> kern_return_t)!, ((task_t, UnsafeMutablePointer<Void>, UInt32, UnsafeMutablePointer<vm_range_t>, UInt32) -> Void)!) -> kern_return_t)!, good_size good_size: ((UnsafeMutablePointer<malloc_zone_t>, Int) -> Int)!, check check: ((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)!, print print: ((UnsafeMutablePointer<malloc_zone_t>, boolean_t) -> Void)!, log log: ((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>) -> Void)!, force_lock force_lock: ((UnsafeMutablePointer<malloc_zone_t>) -> Void)!, force_unlock force_unlock: ((UnsafeMutablePointer<malloc_zone_t>) -> Void)!, statistics statistics: ((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<malloc_statistics_t>) -> Void)!, zone_locked zone_locked: ((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)!, enable_discharge_checking enable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)!, disable_discharge_checking disable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>) -> Void)!, discharge discharge: ((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>) -> Void)!, enumerate_discharged_pointers enumerate_discharged_pointers: ((UnsafeMutablePointer<malloc_zone_t>, ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)!) -> Void)!) } ``` |
| To | ``` struct malloc_introspection_t {     var enumerator: ((task_t, UnsafeMutableRawPointer?, UInt32, vm_address_t, (@escaping (task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)?, (@escaping (task_t, UnsafeMutableRawPointer?, UInt32, UnsafeMutablePointer<vm_range_t>?, UInt32) -> Swift.Void)?) -> kern_return_t)!     var good_size: ((UnsafeMutablePointer<malloc_zone_t>?, Int) -> Int)!     var check: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!     var print: ((UnsafeMutablePointer<malloc_zone_t>?, boolean_t) -> Swift.Void)!     var log: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!     var force_lock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!     var force_unlock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!     var statistics: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutablePointer<malloc_statistics_t>?) -> Swift.Void)!     var zone_locked: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!     var enable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!     var disable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!     var discharge: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!     var enumerate_discharged_pointers: ((UnsafeMutablePointer<malloc_zone_t>?, (@escaping (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)?) -> Swift.Void)!     var reinit_lock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!     init()     init(enumerator enumerator: (@escaping (task_t, UnsafeMutableRawPointer?, UInt32, vm_address_t, (@escaping (task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)?, (@escaping (task_t, UnsafeMutableRawPointer?, UInt32, UnsafeMutablePointer<vm_range_t>?, UInt32) -> Swift.Void)?) -> kern_return_t)!, good_size good_size: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, Int) -> Int)!, check check: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, print print: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, boolean_t) -> Swift.Void)!, log log: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!, force_lock force_lock: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, force_unlock force_unlock: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, statistics statistics: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutablePointer<malloc_statistics_t>?) -> Swift.Void)!, zone_locked zone_locked: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, enable_discharge_checking enable_discharge_checking: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, disable_discharge_checking disable_discharge_checking: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, discharge discharge: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!, enumerate_discharged_pointers enumerate_discharged_pointers: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, (@escaping (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)?) -> Swift.Void)!, reinit_lock reinit_lock: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!) } ``` |

Modified malloc_introspection_t.check

|  | Declaration |
| --- | --- |
| From | ``` var check: ((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)! ``` |
| To | ``` var check: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)! ``` |

Modified malloc_introspection_t.disable_discharge_checking

|  | Declaration |
| --- | --- |
| From | ``` var disable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>) -> Void)! ``` |
| To | ``` var disable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)! ``` |

Modified malloc_introspection_t.discharge

|  | Declaration |
| --- | --- |
| From | ``` var discharge: ((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>) -> Void)! ``` |
| To | ``` var discharge: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)! ``` |

Modified malloc_introspection_t.enable_discharge_checking

|  | Declaration |
| --- | --- |
| From | ``` var enable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)! ``` |
| To | ``` var enable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)! ``` |

Modified malloc_introspection_t.enumerate_discharged_pointers

|  | Declaration |
| --- | --- |
| From | ``` var enumerate_discharged_pointers: ((UnsafeMutablePointer<malloc_zone_t>, ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)!) -> Void)! ``` |
| To | ``` var enumerate_discharged_pointers: ((UnsafeMutablePointer<malloc_zone_t>?, (@escaping (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)?) -> Swift.Void)! ``` |

Modified malloc_introspection_t.enumerator

|  | Declaration |
| --- | --- |
| From | ``` var enumerator: ((task_t, UnsafeMutablePointer<Void>, UInt32, vm_address_t, ((task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> kern_return_t)!, ((task_t, UnsafeMutablePointer<Void>, UInt32, UnsafeMutablePointer<vm_range_t>, UInt32) -> Void)!) -> kern_return_t)! ``` |
| To | ``` var enumerator: ((task_t, UnsafeMutableRawPointer?, UInt32, vm_address_t, (@escaping (task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)?, (@escaping (task_t, UnsafeMutableRawPointer?, UInt32, UnsafeMutablePointer<vm_range_t>?, UInt32) -> Swift.Void)?) -> kern_return_t)! ``` |

Modified malloc_introspection_t.force_lock

|  | Declaration |
| --- | --- |
| From | ``` var force_lock: ((UnsafeMutablePointer<malloc_zone_t>) -> Void)! ``` |
| To | ``` var force_lock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)! ``` |

Modified malloc_introspection_t.force_unlock

|  | Declaration |
| --- | --- |
| From | ``` var force_unlock: ((UnsafeMutablePointer<malloc_zone_t>) -> Void)! ``` |
| To | ``` var force_unlock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)! ``` |

Modified malloc_introspection_t.good_size

|  | Declaration |
| --- | --- |
| From | ``` var good_size: ((UnsafeMutablePointer<malloc_zone_t>, Int) -> Int)! ``` |
| To | ``` var good_size: ((UnsafeMutablePointer<malloc_zone_t>?, Int) -> Int)! ``` |

Modified malloc_introspection_t.log

|  | Declaration |
| --- | --- |
| From | ``` var log: ((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>) -> Void)! ``` |
| To | ``` var log: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)! ``` |

Modified malloc_introspection_t.print

|  | Declaration |
| --- | --- |
| From | ``` var print: ((UnsafeMutablePointer<malloc_zone_t>, boolean_t) -> Void)! ``` |
| To | ``` var print: ((UnsafeMutablePointer<malloc_zone_t>?, boolean_t) -> Swift.Void)! ``` |

Modified malloc_introspection_t.statistics

|  | Declaration |
| --- | --- |
| From | ``` var statistics: ((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<malloc_statistics_t>) -> Void)! ``` |
| To | ``` var statistics: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutablePointer<malloc_statistics_t>?) -> Swift.Void)! ``` |

Modified malloc_introspection_t.zone_locked

|  | Declaration |
| --- | --- |
| From | ``` var zone_locked: ((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)! ``` |
| To | ``` var zone_locked: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)! ``` |

Modified mig_subsystem [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mig_subsystem {     var server: mig_server_routine_t!     var start: mach_msg_id_t     var end: mach_msg_id_t     var maxsize: mach_msg_size_t     var reserved: vm_address_t     var routine: (mig_routine_descriptor)     init()     init(server server: mig_server_routine_t!, start start: mach_msg_id_t, end end: mach_msg_id_t, maxsize maxsize: mach_msg_size_t, reserved reserved: vm_address_t, routine routine: (mig_routine_descriptor)) } ``` |
| To | ``` struct mig_subsystem {     var server: Darwin.mig_server_routine_t!     var start: mach_msg_id_t     var end: mach_msg_id_t     var maxsize: mach_msg_size_t     var reserved: vm_address_t     var routine: (mig_routine_descriptor)     init()     init(server server: Darwin.mig_server_routine_t!, start start: mach_msg_id_t, end end: mach_msg_id_t, maxsize maxsize: mach_msg_size_t, reserved reserved: vm_address_t, routine routine: (mig_routine_descriptor)) } ``` |

Modified mig_subsystem.server

|  | Declaration |
| --- | --- |
| From | ``` var server: mig_server_routine_t! ``` |
| To | ``` var server: Darwin.mig_server_routine_t! ``` |

Modified mig_symtab [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mig_symtab {     var ms_routine_name: UnsafeMutablePointer<Int8>     var ms_routine_number: Int32     var ms_routine: (() -> Void)!     init()     init(ms_routine_name ms_routine_name: UnsafeMutablePointer<Int8>, ms_routine_number ms_routine_number: Int32, ms_routine ms_routine: (() -> Void)!) } ``` |
| To | ``` struct mig_symtab {     var ms_routine_name: UnsafeMutablePointer<Int8>!     var ms_routine_number: Int32     var ms_routine: (() -> Swift.Void)!     init()     init(ms_routine_name ms_routine_name: UnsafeMutablePointer<Int8>!, ms_routine_number ms_routine_number: Int32, ms_routine ms_routine: (@escaping () -> Swift.Void)!) } ``` |

Modified mig_symtab.ms_routine

|  | Declaration |
| --- | --- |
| From | ``` var ms_routine: (() -> Void)! ``` |
| To | ``` var ms_routine: (() -> Swift.Void)! ``` |

Modified mig_symtab.ms_routine_name

|  | Declaration |
| --- | --- |
| From | ``` var ms_routine_name: UnsafeMutablePointer<Int8> ``` |
| To | ``` var ms_routine_name: UnsafeMutablePointer<Int8>! ``` |

Modified msg [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct msg {     var msg_next: UnsafeMutablePointer<msg>     var msg_type: Int     var msg_ts: UInt16     var msg_spot: Int16     var label: COpaquePointer     init() } ``` |
| To | ``` struct msg {     var msg_next: UnsafeMutablePointer<msg>!     var msg_type: Int     var msg_ts: UInt16     var msg_spot: Int16     var label: OpaquePointer!     init() } ``` |

Modified msg.label

|  | Declaration |
| --- | --- |
| From | ``` var label: COpaquePointer ``` |
| To | ``` var label: OpaquePointer! ``` |

Modified msg.msg_next

|  | Declaration |
| --- | --- |
| From | ``` var msg_next: UnsafeMutablePointer<msg> ``` |
| To | ``` var msg_next: UnsafeMutablePointer<msg>! ``` |

Modified msghdr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct msghdr {     var msg_name: UnsafeMutablePointer<Void>     var msg_namelen: socklen_t     var msg_iov: UnsafeMutablePointer<iovec>     var msg_iovlen: Int32     var msg_control: UnsafeMutablePointer<Void>     var msg_controllen: socklen_t     var msg_flags: Int32     init()     init(msg_name msg_name: UnsafeMutablePointer<Void>, msg_namelen msg_namelen: socklen_t, msg_iov msg_iov: UnsafeMutablePointer<iovec>, msg_iovlen msg_iovlen: Int32, msg_control msg_control: UnsafeMutablePointer<Void>, msg_controllen msg_controllen: socklen_t, msg_flags msg_flags: Int32) } ``` |
| To | ``` struct msghdr {     var msg_name: UnsafeMutableRawPointer!     var msg_namelen: socklen_t     var msg_iov: UnsafeMutablePointer<iovec>!     var msg_iovlen: Int32     var msg_control: UnsafeMutableRawPointer!     var msg_controllen: socklen_t     var msg_flags: Int32     init()     init(msg_name msg_name: UnsafeMutableRawPointer!, msg_namelen msg_namelen: socklen_t, msg_iov msg_iov: UnsafeMutablePointer<iovec>!, msg_iovlen msg_iovlen: Int32, msg_control msg_control: UnsafeMutableRawPointer!, msg_controllen msg_controllen: socklen_t, msg_flags msg_flags: Int32) } ``` |

Modified msghdr.msg_control

|  | Declaration |
| --- | --- |
| From | ``` var msg_control: UnsafeMutablePointer<Void> ``` |
| To | ``` var msg_control: UnsafeMutableRawPointer! ``` |

Modified msghdr.msg_iov

|  | Declaration |
| --- | --- |
| From | ``` var msg_iov: UnsafeMutablePointer<iovec> ``` |
| To | ``` var msg_iov: UnsafeMutablePointer<iovec>! ``` |

Modified msghdr.msg_name

|  | Declaration |
| --- | --- |
| From | ``` var msg_name: UnsafeMutablePointer<Void> ``` |
| To | ``` var msg_name: UnsafeMutableRawPointer! ``` |

Modified netent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct netent {     var n_name: UnsafeMutablePointer<Int8>     var n_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var n_addrtype: Int32     var n_net: UInt32     init()     init(n_name n_name: UnsafeMutablePointer<Int8>, n_aliases n_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, n_addrtype n_addrtype: Int32, n_net n_net: UInt32) } ``` |
| To | ``` struct netent {     var n_name: UnsafeMutablePointer<Int8>!     var n_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!     var n_addrtype: Int32     var n_net: UInt32     init()     init(n_name n_name: UnsafeMutablePointer<Int8>!, n_aliases n_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, n_addrtype n_addrtype: Int32, n_net n_net: UInt32) } ``` |

Modified netent.n_aliases

|  | Declaration |
| --- | --- |
| From | ``` var n_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>> ``` |
| To | ``` var n_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>! ``` |

Modified netent.n_name

|  | Declaration |
| --- | --- |
| From | ``` var n_name: UnsafeMutablePointer<Int8> ``` |
| To | ``` var n_name: UnsafeMutablePointer<Int8>! ``` |

Modified option [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct option {     var name: UnsafePointer<Int8>     var has_arg: Int32     var flag: UnsafeMutablePointer<Int32>     var val: Int32     init()     init(name name: UnsafePointer<Int8>, has_arg has_arg: Int32, flag flag: UnsafeMutablePointer<Int32>, val val: Int32) } ``` |
| To | ``` struct option {     var name: UnsafePointer<Int8>!     var has_arg: Int32     var flag: UnsafeMutablePointer<Int32>!     var val: Int32     init()     init(name name: UnsafePointer<Int8>!, has_arg has_arg: Int32, flag flag: UnsafeMutablePointer<Int32>!, val val: Int32) } ``` |

Modified option.flag

|  | Declaration |
| --- | --- |
| From | ``` var flag: UnsafeMutablePointer<Int32> ``` |
| To | ``` var flag: UnsafeMutablePointer<Int32>! ``` |

Modified option.name

|  | Declaration |
| --- | --- |
| From | ``` var name: UnsafePointer<Int8> ``` |
| To | ``` var name: UnsafePointer<Int8>! ``` |

Modified passwd [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct passwd {     var pw_name: UnsafeMutablePointer<Int8>     var pw_passwd: UnsafeMutablePointer<Int8>     var pw_uid: uid_t     var pw_gid: gid_t     var pw_change: __darwin_time_t     var pw_class: UnsafeMutablePointer<Int8>     var pw_gecos: UnsafeMutablePointer<Int8>     var pw_dir: UnsafeMutablePointer<Int8>     var pw_shell: UnsafeMutablePointer<Int8>     var pw_expire: __darwin_time_t     init()     init(pw_name pw_name: UnsafeMutablePointer<Int8>, pw_passwd pw_passwd: UnsafeMutablePointer<Int8>, pw_uid pw_uid: uid_t, pw_gid pw_gid: gid_t, pw_change pw_change: __darwin_time_t, pw_class pw_class: UnsafeMutablePointer<Int8>, pw_gecos pw_gecos: UnsafeMutablePointer<Int8>, pw_dir pw_dir: UnsafeMutablePointer<Int8>, pw_shell pw_shell: UnsafeMutablePointer<Int8>, pw_expire pw_expire: __darwin_time_t) } ``` |
| To | ``` struct passwd {     var pw_name: UnsafeMutablePointer<Int8>!     var pw_passwd: UnsafeMutablePointer<Int8>!     var pw_uid: uid_t     var pw_gid: gid_t     var pw_change: __darwin_time_t     var pw_class: UnsafeMutablePointer<Int8>!     var pw_gecos: UnsafeMutablePointer<Int8>!     var pw_dir: UnsafeMutablePointer<Int8>!     var pw_shell: UnsafeMutablePointer<Int8>!     var pw_expire: __darwin_time_t     init()     init(pw_name pw_name: UnsafeMutablePointer<Int8>!, pw_passwd pw_passwd: UnsafeMutablePointer<Int8>!, pw_uid pw_uid: uid_t, pw_gid pw_gid: gid_t, pw_change pw_change: __darwin_time_t, pw_class pw_class: UnsafeMutablePointer<Int8>!, pw_gecos pw_gecos: UnsafeMutablePointer<Int8>!, pw_dir pw_dir: UnsafeMutablePointer<Int8>!, pw_shell pw_shell: UnsafeMutablePointer<Int8>!, pw_expire pw_expire: __darwin_time_t) } ``` |

Modified passwd.pw_class

|  | Declaration |
| --- | --- |
| From | ``` var pw_class: UnsafeMutablePointer<Int8> ``` |
| To | ``` var pw_class: UnsafeMutablePointer<Int8>! ``` |

Modified passwd.pw_dir

|  | Declaration |
| --- | --- |
| From | ``` var pw_dir: UnsafeMutablePointer<Int8> ``` |
| To | ``` var pw_dir: UnsafeMutablePointer<Int8>! ``` |

Modified passwd.pw_gecos

|  | Declaration |
| --- | --- |
| From | ``` var pw_gecos: UnsafeMutablePointer<Int8> ``` |
| To | ``` var pw_gecos: UnsafeMutablePointer<Int8>! ``` |

Modified passwd.pw_name

|  | Declaration |
| --- | --- |
| From | ``` var pw_name: UnsafeMutablePointer<Int8> ``` |
| To | ``` var pw_name: UnsafeMutablePointer<Int8>! ``` |

Modified passwd.pw_passwd

|  | Declaration |
| --- | --- |
| From | ``` var pw_passwd: UnsafeMutablePointer<Int8> ``` |
| To | ``` var pw_passwd: UnsafeMutablePointer<Int8>! ``` |

Modified passwd.pw_shell

|  | Declaration |
| --- | --- |
| From | ``` var pw_shell: UnsafeMutablePointer<Int8> ``` |
| To | ``` var pw_shell: UnsafeMutablePointer<Int8>! ``` |

Modified port_obj_tentry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct port_obj_tentry {     var pos_value: UnsafeMutablePointer<Void>     var pos_type: Int32     init()     init(pos_value pos_value: UnsafeMutablePointer<Void>, pos_type pos_type: Int32) } ``` |
| To | ``` struct port_obj_tentry {     var pos_value: UnsafeMutableRawPointer!     var pos_type: Int32     init()     init(pos_value pos_value: UnsafeMutableRawPointer!, pos_type pos_type: Int32) } ``` |

Modified port_obj_tentry.pos_value

|  | Declaration |
| --- | --- |
| From | ``` var pos_value: UnsafeMutablePointer<Void> ``` |
| To | ``` var pos_value: UnsafeMutableRawPointer! ``` |

Modified protoent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct protoent {     var p_name: UnsafeMutablePointer<Int8>     var p_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var p_proto: Int32     init()     init(p_name p_name: UnsafeMutablePointer<Int8>, p_aliases p_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, p_proto p_proto: Int32) } ``` |
| To | ``` struct protoent {     var p_name: UnsafeMutablePointer<Int8>!     var p_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!     var p_proto: Int32     init()     init(p_name p_name: UnsafeMutablePointer<Int8>!, p_aliases p_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, p_proto p_proto: Int32) } ``` |

Modified protoent.p_aliases

|  | Declaration |
| --- | --- |
| From | ``` var p_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>> ``` |
| To | ``` var p_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>! ``` |

Modified protoent.p_name

|  | Declaration |
| --- | --- |
| From | ``` var p_name: UnsafeMutablePointer<Int8> ``` |
| To | ``` var p_name: UnsafeMutablePointer<Int8>! ``` |

Modified rb_node [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rb_node {     var opaque: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)     init()     init(opaque opaque: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)) } ``` |
| To | ``` struct rb_node {     var opaque: (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?)     init()     init(opaque opaque: (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?)) } ``` |

Modified rb_node.opaque

|  | Declaration |
| --- | --- |
| From | ``` var opaque: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) ``` |
| To | ``` var opaque: (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) ``` |

Modified rb_tree [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rb_tree {     var opaque: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)     init()     init(opaque opaque: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)) } ``` |
| To | ``` struct rb_tree {     var opaque: (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?)     init()     init(opaque opaque: (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?)) } ``` |

Modified rb_tree.opaque

|  | Declaration |
| --- | --- |
| From | ``` var opaque: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) ``` |
| To | ``` var opaque: (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) ``` |

Modified rb_tree_ops_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rb_tree_ops_t {     var rbto_compare_nodes: rbto_compare_nodes_fn!     var rbto_compare_key: rbto_compare_key_fn!     var rbto_node_offset: Int     var rbto_context: UnsafeMutablePointer<Void>     init()     init(rbto_compare_nodes rbto_compare_nodes: rbto_compare_nodes_fn!, rbto_compare_key rbto_compare_key: rbto_compare_key_fn!, rbto_node_offset rbto_node_offset: Int, rbto_context rbto_context: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct rb_tree_ops_t {     var rbto_compare_nodes: Darwin.rbto_compare_nodes_fn!     var rbto_compare_key: Darwin.rbto_compare_key_fn!     var rbto_node_offset: Int     var rbto_context: UnsafeMutableRawPointer!     init()     init(rbto_compare_nodes rbto_compare_nodes: Darwin.rbto_compare_nodes_fn!, rbto_compare_key rbto_compare_key: Darwin.rbto_compare_key_fn!, rbto_node_offset rbto_node_offset: Int, rbto_context rbto_context: UnsafeMutableRawPointer!) } ``` |

Modified rb_tree_ops_t.rbto_compare_key

|  | Declaration |
| --- | --- |
| From | ``` var rbto_compare_key: rbto_compare_key_fn! ``` |
| To | ``` var rbto_compare_key: Darwin.rbto_compare_key_fn! ``` |

Modified rb_tree_ops_t.rbto_compare_nodes

|  | Declaration |
| --- | --- |
| From | ``` var rbto_compare_nodes: rbto_compare_nodes_fn! ``` |
| To | ``` var rbto_compare_nodes: Darwin.rbto_compare_nodes_fn! ``` |

Modified rb_tree_ops_t.rbto_context

|  | Declaration |
| --- | --- |
| From | ``` var rbto_context: UnsafeMutablePointer<Void> ``` |
| To | ``` var rbto_context: UnsafeMutableRawPointer! ``` |

Modified regex_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct regex_t {     var re_magic: Int32     var re_nsub: Int     var re_endp: UnsafePointer<Int8>     var re_g: COpaquePointer     init() } ``` |
| To | ``` struct regex_t {     var re_magic: Int32     var re_nsub: Int     var re_endp: UnsafePointer<Int8>!     var re_g: OpaquePointer!     init() } ``` |

Modified regex_t.re_endp

|  | Declaration |
| --- | --- |
| From | ``` var re_endp: UnsafePointer<Int8> ``` |
| To | ``` var re_endp: UnsafePointer<Int8>! ``` |

Modified regex_t.re_g

|  | Declaration |
| --- | --- |
| From | ``` var re_g: COpaquePointer ``` |
| To | ``` var re_g: OpaquePointer! ``` |

Modified routine_descriptor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct routine_descriptor {     var impl_routine: mig_impl_routine_t!     var stub_routine: mig_stub_routine_t!     var argc: UInt32     var descr_count: UInt32     var arg_descr: routine_arg_descriptor_t     var max_reply_msg: UInt32     init()     init(impl_routine impl_routine: mig_impl_routine_t!, stub_routine stub_routine: mig_stub_routine_t!, argc argc: UInt32, descr_count descr_count: UInt32, arg_descr arg_descr: routine_arg_descriptor_t, max_reply_msg max_reply_msg: UInt32) } ``` |
| To | ``` struct routine_descriptor {     var impl_routine: Darwin.mig_impl_routine_t!     var stub_routine: Darwin.mig_stub_routine_t!     var argc: UInt32     var descr_count: UInt32     var arg_descr: routine_arg_descriptor_t!     var max_reply_msg: UInt32     init()     init(impl_routine impl_routine: Darwin.mig_impl_routine_t!, stub_routine stub_routine: Darwin.mig_stub_routine_t!, argc argc: UInt32, descr_count descr_count: UInt32, arg_descr arg_descr: routine_arg_descriptor_t!, max_reply_msg max_reply_msg: UInt32) } ``` |

Modified routine_descriptor.arg_descr

|  | Declaration |
| --- | --- |
| From | ``` var arg_descr: routine_arg_descriptor_t ``` |
| To | ``` var arg_descr: routine_arg_descriptor_t! ``` |

Modified routine_descriptor.impl_routine

|  | Declaration |
| --- | --- |
| From | ``` var impl_routine: mig_impl_routine_t! ``` |
| To | ``` var impl_routine: Darwin.mig_impl_routine_t! ``` |

Modified routine_descriptor.stub_routine

|  | Declaration |
| --- | --- |
| From | ``` var stub_routine: mig_stub_routine_t! ``` |
| To | ``` var stub_routine: Darwin.mig_stub_routine_t! ``` |

Modified rpc_routine_descriptor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rpc_routine_descriptor {     var impl_routine: mig_impl_routine_t!     var stub_routine: mig_stub_routine_t!     var argc: UInt32     var descr_count: UInt32     var arg_descr: rpc_routine_arg_descriptor_t     var max_reply_msg: UInt32     init()     init(impl_routine impl_routine: mig_impl_routine_t!, stub_routine stub_routine: mig_stub_routine_t!, argc argc: UInt32, descr_count descr_count: UInt32, arg_descr arg_descr: rpc_routine_arg_descriptor_t, max_reply_msg max_reply_msg: UInt32) } ``` |
| To | ``` struct rpc_routine_descriptor {     var impl_routine: Darwin.mig_impl_routine_t!     var stub_routine: Darwin.mig_stub_routine_t!     var argc: UInt32     var descr_count: UInt32     var arg_descr: rpc_routine_arg_descriptor_t!     var max_reply_msg: UInt32     init()     init(impl_routine impl_routine: Darwin.mig_impl_routine_t!, stub_routine stub_routine: Darwin.mig_stub_routine_t!, argc argc: UInt32, descr_count descr_count: UInt32, arg_descr arg_descr: rpc_routine_arg_descriptor_t!, max_reply_msg max_reply_msg: UInt32) } ``` |

Modified rpc_routine_descriptor.arg_descr

|  | Declaration |
| --- | --- |
| From | ``` var arg_descr: rpc_routine_arg_descriptor_t ``` |
| To | ``` var arg_descr: rpc_routine_arg_descriptor_t! ``` |

Modified rpc_routine_descriptor.impl_routine

|  | Declaration |
| --- | --- |
| From | ``` var impl_routine: mig_impl_routine_t! ``` |
| To | ``` var impl_routine: Darwin.mig_impl_routine_t! ``` |

Modified rpc_routine_descriptor.stub_routine

|  | Declaration |
| --- | --- |
| From | ``` var stub_routine: mig_stub_routine_t! ``` |
| To | ``` var stub_routine: Darwin.mig_stub_routine_t! ``` |

Modified rpc_subsystem [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rpc_subsystem {     var reserved: UnsafeMutablePointer<Void>     var start: mach_msg_id_t     var end: mach_msg_id_t     var maxsize: UInt32     var base_addr: vm_address_t     var routine: (rpc_routine_descriptor)     var arg_descriptor: (rpc_routine_arg_descriptor)     init()     init(reserved reserved: UnsafeMutablePointer<Void>, start start: mach_msg_id_t, end end: mach_msg_id_t, maxsize maxsize: UInt32, base_addr base_addr: vm_address_t, routine routine: (rpc_routine_descriptor), arg_descriptor arg_descriptor: (rpc_routine_arg_descriptor)) } ``` |
| To | ``` struct rpc_subsystem {     var reserved: UnsafeMutableRawPointer!     var start: mach_msg_id_t     var end: mach_msg_id_t     var maxsize: UInt32     var base_addr: vm_address_t     var routine: (rpc_routine_descriptor)     var arg_descriptor: (rpc_routine_arg_descriptor)     init()     init(reserved reserved: UnsafeMutableRawPointer!, start start: mach_msg_id_t, end end: mach_msg_id_t, maxsize maxsize: UInt32, base_addr base_addr: vm_address_t, routine routine: (rpc_routine_descriptor), arg_descriptor arg_descriptor: (rpc_routine_arg_descriptor)) } ``` |

Modified rpc_subsystem.reserved

|  | Declaration |
| --- | --- |
| From | ``` var reserved: UnsafeMutablePointer<Void> ``` |
| To | ``` var reserved: UnsafeMutableRawPointer! ``` |

Modified rpcent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rpcent {     var r_name: UnsafeMutablePointer<Int8>     var r_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var r_number: Int32     init()     init(r_name r_name: UnsafeMutablePointer<Int8>, r_aliases r_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, r_number r_number: Int32) } ``` |
| To | ``` struct rpcent {     var r_name: UnsafeMutablePointer<Int8>!     var r_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!     var r_number: Int32     init()     init(r_name r_name: UnsafeMutablePointer<Int8>!, r_aliases r_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, r_number r_number: Int32) } ``` |

Modified rpcent.r_aliases

|  | Declaration |
| --- | --- |
| From | ``` var r_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>> ``` |
| To | ``` var r_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>! ``` |

Modified rpcent.r_name

|  | Declaration |
| --- | --- |
| From | ``` var r_name: UnsafeMutablePointer<Int8> ``` |
| To | ``` var r_name: UnsafeMutablePointer<Int8>! ``` |

Modified rslvmulti_req [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rslvmulti_req {     var sa: UnsafeMutablePointer<sockaddr>     var llsa: UnsafeMutablePointer<UnsafeMutablePointer<sockaddr>>     init()     init(sa sa: UnsafeMutablePointer<sockaddr>, llsa llsa: UnsafeMutablePointer<UnsafeMutablePointer<sockaddr>>) } ``` |
| To | ``` struct rslvmulti_req {     var sa: UnsafeMutablePointer<sockaddr>!     var llsa: UnsafeMutablePointer<UnsafeMutablePointer<sockaddr>?>!     init()     init(sa sa: UnsafeMutablePointer<sockaddr>!, llsa llsa: UnsafeMutablePointer<UnsafeMutablePointer<sockaddr>?>!) } ``` |

Modified rslvmulti_req.llsa

|  | Declaration |
| --- | --- |
| From | ``` var llsa: UnsafeMutablePointer<UnsafeMutablePointer<sockaddr>> ``` |
| To | ``` var llsa: UnsafeMutablePointer<UnsafeMutablePointer<sockaddr>?>! ``` |

Modified rslvmulti_req.sa

|  | Declaration |
| --- | --- |
| From | ``` var sa: UnsafeMutablePointer<sockaddr> ``` |
| To | ``` var sa: UnsafeMutablePointer<sockaddr>! ``` |

Modified sa_endpoints [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sa_endpoints {     var sae_srcif: UInt32     var sae_srcaddr: UnsafeMutablePointer<sockaddr>     var sae_srcaddrlen: socklen_t     var sae_dstaddr: UnsafeMutablePointer<sockaddr>     var sae_dstaddrlen: socklen_t     init()     init(sae_srcif sae_srcif: UInt32, sae_srcaddr sae_srcaddr: UnsafeMutablePointer<sockaddr>, sae_srcaddrlen sae_srcaddrlen: socklen_t, sae_dstaddr sae_dstaddr: UnsafeMutablePointer<sockaddr>, sae_dstaddrlen sae_dstaddrlen: socklen_t) } ``` |
| To | ``` struct sa_endpoints {     var sae_srcif: UInt32     var sae_srcaddr: UnsafePointer<sockaddr>!     var sae_srcaddrlen: socklen_t     var sae_dstaddr: UnsafePointer<sockaddr>!     var sae_dstaddrlen: socklen_t     init()     init(sae_srcif sae_srcif: UInt32, sae_srcaddr sae_srcaddr: UnsafePointer<sockaddr>!, sae_srcaddrlen sae_srcaddrlen: socklen_t, sae_dstaddr sae_dstaddr: UnsafePointer<sockaddr>!, sae_dstaddrlen sae_dstaddrlen: socklen_t) } ``` |

Modified sa_endpoints.sae_dstaddr

|  | Declaration |
| --- | --- |
| From | ``` var sae_dstaddr: UnsafeMutablePointer<sockaddr> ``` |
| To | ``` var sae_dstaddr: UnsafePointer<sockaddr>! ``` |

Modified sa_endpoints.sae_srcaddr

|  | Declaration |
| --- | --- |
| From | ``` var sae_srcaddr: UnsafeMutablePointer<sockaddr> ``` |
| To | ``` var sae_srcaddr: UnsafePointer<sockaddr>! ``` |

Modified semun [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct semun {     var val: Int32     var buf: UnsafeMutablePointer<__semid_ds_new>     var array: UnsafeMutablePointer<UInt16>     init(val val: Int32)     init(buf buf: UnsafeMutablePointer<__semid_ds_new>)     init(array array: UnsafeMutablePointer<UInt16>)     init() } ``` |
| To | ``` struct semun {     var val: Int32     var buf: UnsafeMutablePointer<__semid_ds_new>!     var array: UnsafeMutablePointer<UInt16>!     init(val val: Int32)     init(buf buf: UnsafeMutablePointer<__semid_ds_new>!)     init(array array: UnsafeMutablePointer<UInt16>!)     init() } ``` |

Modified semun.array

|  | Declaration |
| --- | --- |
| From | ``` var array: UnsafeMutablePointer<UInt16> ``` |
| To | ``` var array: UnsafeMutablePointer<UInt16>! ``` |

Modified semun.buf

|  | Declaration |
| --- | --- |
| From | ``` var buf: UnsafeMutablePointer<__semid_ds_new> ``` |
| To | ``` var buf: UnsafeMutablePointer<__semid_ds_new>! ``` |

Modified servent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct servent {     var s_name: UnsafeMutablePointer<Int8>     var s_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var s_port: Int32     var s_proto: UnsafeMutablePointer<Int8>     init()     init(s_name s_name: UnsafeMutablePointer<Int8>, s_aliases s_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, s_port s_port: Int32, s_proto s_proto: UnsafeMutablePointer<Int8>) } ``` |
| To | ``` struct servent {     var s_name: UnsafeMutablePointer<Int8>!     var s_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!     var s_port: Int32     var s_proto: UnsafeMutablePointer<Int8>!     init()     init(s_name s_name: UnsafeMutablePointer<Int8>!, s_aliases s_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, s_port s_port: Int32, s_proto s_proto: UnsafeMutablePointer<Int8>!) } ``` |

Modified servent.s_aliases

|  | Declaration |
| --- | --- |
| From | ``` var s_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>> ``` |
| To | ``` var s_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>! ``` |

Modified servent.s_name

|  | Declaration |
| --- | --- |
| From | ``` var s_name: UnsafeMutablePointer<Int8> ``` |
| To | ``` var s_name: UnsafeMutablePointer<Int8>! ``` |

Modified servent.s_proto

|  | Declaration |
| --- | --- |
| From | ``` var s_proto: UnsafeMutablePointer<Int8> ``` |
| To | ``` var s_proto: UnsafeMutablePointer<Int8>! ``` |

Modified sf_hdtr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sf_hdtr {     var headers: UnsafeMutablePointer<iovec>     var hdr_cnt: Int32     var trailers: UnsafeMutablePointer<iovec>     var trl_cnt: Int32     init()     init(headers headers: UnsafeMutablePointer<iovec>, hdr_cnt hdr_cnt: Int32, trailers trailers: UnsafeMutablePointer<iovec>, trl_cnt trl_cnt: Int32) } ``` |
| To | ``` struct sf_hdtr {     var headers: UnsafeMutablePointer<iovec>!     var hdr_cnt: Int32     var trailers: UnsafeMutablePointer<iovec>!     var trl_cnt: Int32     init()     init(headers headers: UnsafeMutablePointer<iovec>!, hdr_cnt hdr_cnt: Int32, trailers trailers: UnsafeMutablePointer<iovec>!, trl_cnt trl_cnt: Int32) } ``` |

Modified sf_hdtr.headers

|  | Declaration |
| --- | --- |
| From | ``` var headers: UnsafeMutablePointer<iovec> ``` |
| To | ``` var headers: UnsafeMutablePointer<iovec>! ``` |

Modified sf_hdtr.trailers

|  | Declaration |
| --- | --- |
| From | ``` var trailers: UnsafeMutablePointer<iovec> ``` |
| To | ``` var trailers: UnsafeMutablePointer<iovec>! ``` |

Modified sigevent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sigevent {     var sigev_notify: Int32     var sigev_signo: Int32     var sigev_value: sigval     var sigev_notify_function: ((sigval) -> Void)!     var sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t>     init()     init(sigev_notify sigev_notify: Int32, sigev_signo sigev_signo: Int32, sigev_value sigev_value: sigval, sigev_notify_function sigev_notify_function: ((sigval) -> Void)!, sigev_notify_attributes sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t>) } ``` |
| To | ``` struct sigevent {     var sigev_notify: Int32     var sigev_signo: Int32     var sigev_value: sigval     var sigev_notify_function: ((sigval) -> Swift.Void)!     var sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t>!     init()     init(sigev_notify sigev_notify: Int32, sigev_signo sigev_signo: Int32, sigev_value sigev_value: sigval, sigev_notify_function sigev_notify_function: (@escaping (sigval) -> Swift.Void)!, sigev_notify_attributes sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t>!) } ``` |

Modified sigevent.sigev_notify_attributes

|  | Declaration |
| --- | --- |
| From | ``` var sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t> ``` |
| To | ``` var sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t>! ``` |

Modified sigevent.sigev_notify_function

|  | Declaration |
| --- | --- |
| From | ``` var sigev_notify_function: ((sigval) -> Void)! ``` |
| To | ``` var sigev_notify_function: ((sigval) -> Swift.Void)! ``` |

Modified sigstack [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sigstack {     var ss_sp: UnsafeMutablePointer<Int8>     var ss_onstack: Int32     init()     init(ss_sp ss_sp: UnsafeMutablePointer<Int8>, ss_onstack ss_onstack: Int32) } ``` |
| To | ``` struct sigstack {     var ss_sp: UnsafeMutablePointer<Int8>!     var ss_onstack: Int32     init()     init(ss_sp ss_sp: UnsafeMutablePointer<Int8>!, ss_onstack ss_onstack: Int32) } ``` |

Modified sigstack.ss_sp

|  | Declaration |
| --- | --- |
| From | ``` var ss_sp: UnsafeMutablePointer<Int8> ``` |
| To | ``` var ss_sp: UnsafeMutablePointer<Int8>! ``` |

Modified sigval [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sigval {     var sival_int: Int32     var sival_ptr: UnsafeMutablePointer<Void>     init(sival_int sival_int: Int32)     init(sival_ptr sival_ptr: UnsafeMutablePointer<Void>)     init() } ``` |
| To | ``` struct sigval {     var sival_int: Int32     var sival_ptr: UnsafeMutableRawPointer!     init(sival_int sival_int: Int32)     init(sival_ptr sival_ptr: UnsafeMutableRawPointer!)     init() } ``` |

Modified sigval.sival_ptr

|  | Declaration |
| --- | --- |
| From | ``` var sival_ptr: UnsafeMutablePointer<Void> ``` |
| To | ``` var sival_ptr: UnsafeMutableRawPointer! ``` |

Modified sigvec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sigvec {     var sv_handler: ((Int32) -> Void)!     var sv_mask: Int32     var sv_flags: Int32     init()     init(sv_handler sv_handler: ((Int32) -> Void)!, sv_mask sv_mask: Int32, sv_flags sv_flags: Int32) } ``` |
| To | ``` struct sigvec {     var sv_handler: ((Int32) -> Swift.Void)!     var sv_mask: Int32     var sv_flags: Int32     init()     init(sv_handler sv_handler: (@escaping (Int32) -> Swift.Void)!, sv_mask sv_mask: Int32, sv_flags sv_flags: Int32) } ``` |

Modified sigvec.init(sv_handler: ( (Int32) -> Swift.Void)!, sv_mask: Int32, sv_flags: Int32)

|  | Declaration |
| --- | --- |
| From | ``` init(sv_handler sv_handler: ((Int32) -> Void)!, sv_mask sv_mask: Int32, sv_flags sv_flags: Int32) ``` |
| To | ``` init(sv_handler sv_handler: (@escaping (Int32) -> Swift.Void)!, sv_mask sv_mask: Int32, sv_flags sv_flags: Int32) ``` |

Modified sigvec.sv_handler

|  | Declaration |
| --- | --- |
| From | ``` var sv_handler: ((Int32) -> Void)! ``` |
| To | ``` var sv_handler: ((Int32) -> Swift.Void)! ``` |

Modified task_basic_info.init(suspend_count: integer_t, virtual_size: vm_size_t, resident_size: vm_size_t, user_time: time_value_t, system_time: time_value_t, policy: policy_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.3 |

Modified task_power_info_v2 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_power_info_v2 {     var cpu_energy: task_power_info_data_t     var gpu_energy: gpu_energy_data     init()     init(cpu_energy cpu_energy: task_power_info_data_t, gpu_energy gpu_energy: gpu_energy_data) } ``` |
| To | ``` struct task_power_info_v2 {     var cpu_energy: task_power_info_data_t     var gpu_energy: gpu_energy_data     var task_energy: UInt64     init()     init(cpu_energy cpu_energy: task_power_info_data_t, gpu_energy gpu_energy: gpu_energy_data, task_energy task_energy: UInt64) } ``` |

Modified task_vm_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_vm_info {     var virtual_size: mach_vm_size_t     var region_count: integer_t     var page_size: integer_t     var resident_size: mach_vm_size_t     var resident_size_peak: mach_vm_size_t     var device: mach_vm_size_t     var device_peak: mach_vm_size_t     var `internal`: mach_vm_size_t     var internal_peak: mach_vm_size_t     var external: mach_vm_size_t     var external_peak: mach_vm_size_t     var reusable: mach_vm_size_t     var reusable_peak: mach_vm_size_t     var purgeable_volatile_pmap: mach_vm_size_t     var purgeable_volatile_resident: mach_vm_size_t     var purgeable_volatile_virtual: mach_vm_size_t     var compressed: mach_vm_size_t     var compressed_peak: mach_vm_size_t     var compressed_lifetime: mach_vm_size_t     var phys_footprint: mach_vm_size_t     init()     init(virtual_size virtual_size: mach_vm_size_t, region_count region_count: integer_t, page_size page_size: integer_t, resident_size resident_size: mach_vm_size_t, resident_size_peak resident_size_peak: mach_vm_size_t, device device: mach_vm_size_t, device_peak device_peak: mach_vm_size_t, internal internal: mach_vm_size_t, internal_peak internal_peak: mach_vm_size_t, external external: mach_vm_size_t, external_peak external_peak: mach_vm_size_t, reusable reusable: mach_vm_size_t, reusable_peak reusable_peak: mach_vm_size_t, purgeable_volatile_pmap purgeable_volatile_pmap: mach_vm_size_t, purgeable_volatile_resident purgeable_volatile_resident: mach_vm_size_t, purgeable_volatile_virtual purgeable_volatile_virtual: mach_vm_size_t, compressed compressed: mach_vm_size_t, compressed_peak compressed_peak: mach_vm_size_t, compressed_lifetime compressed_lifetime: mach_vm_size_t, phys_footprint phys_footprint: mach_vm_size_t) } ``` |
| To | ``` struct task_vm_info {     var virtual_size: mach_vm_size_t     var region_count: integer_t     var page_size: integer_t     var resident_size: mach_vm_size_t     var resident_size_peak: mach_vm_size_t     var device: mach_vm_size_t     var device_peak: mach_vm_size_t     var `internal`: mach_vm_size_t     var internal_peak: mach_vm_size_t     var external: mach_vm_size_t     var external_peak: mach_vm_size_t     var reusable: mach_vm_size_t     var reusable_peak: mach_vm_size_t     var purgeable_volatile_pmap: mach_vm_size_t     var purgeable_volatile_resident: mach_vm_size_t     var purgeable_volatile_virtual: mach_vm_size_t     var compressed: mach_vm_size_t     var compressed_peak: mach_vm_size_t     var compressed_lifetime: mach_vm_size_t     var phys_footprint: mach_vm_size_t     var min_address: mach_vm_address_t     var max_address: mach_vm_address_t     init()     init(virtual_size virtual_size: mach_vm_size_t, region_count region_count: integer_t, page_size page_size: integer_t, resident_size resident_size: mach_vm_size_t, resident_size_peak resident_size_peak: mach_vm_size_t, device device: mach_vm_size_t, device_peak device_peak: mach_vm_size_t, internal internal: mach_vm_size_t, internal_peak internal_peak: mach_vm_size_t, external external: mach_vm_size_t, external_peak external_peak: mach_vm_size_t, reusable reusable: mach_vm_size_t, reusable_peak reusable_peak: mach_vm_size_t, purgeable_volatile_pmap purgeable_volatile_pmap: mach_vm_size_t, purgeable_volatile_resident purgeable_volatile_resident: mach_vm_size_t, purgeable_volatile_virtual purgeable_volatile_virtual: mach_vm_size_t, compressed compressed: mach_vm_size_t, compressed_peak compressed_peak: mach_vm_size_t, compressed_lifetime compressed_lifetime: mach_vm_size_t, phys_footprint phys_footprint: mach_vm_size_t, min_address min_address: mach_vm_address_t, max_address max_address: mach_vm_address_t) } ``` |

Modified tcp_connection_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tcp_connection_info {     var tcpi_state: UInt8     var tcpi_snd_wscale: UInt8     var tcpi_rcv_wscale: UInt8     var __pad1: UInt8     var tcpi_options: UInt32     var tcpi_flags: UInt32     var tcpi_rto: UInt32     var tcpi_maxseg: UInt32     var tcpi_snd_ssthresh: UInt32     var tcpi_snd_cwnd: UInt32     var tcpi_snd_wnd: UInt32     var tcpi_snd_sbbytes: UInt32     var tcpi_rcv_wnd: UInt32     var tcpi_rttcur: UInt32     var tcpi_srtt: UInt32     var tcpi_rttvar: UInt32     var tcpi_tfo_cookie_req: UInt32     var tcpi_tfo_cookie_rcv: UInt32     var tcpi_tfo_syn_loss: UInt32     var tcpi_tfo_syn_data_sent: UInt32     var tcpi_tfo_syn_data_acked: UInt32     var tcpi_tfo_syn_data_rcv: UInt32     var tcpi_tfo_cookie_req_rcv: UInt32     var tcpi_tfo_cookie_sent: UInt32     var tcpi_tfo_cookie_invalid: UInt32     var __pad2: UInt32     var tcpi_txpackets: UInt64     var tcpi_txbytes: UInt64     var tcpi_txretransmitbytes: UInt64     var tcpi_rxpackets: UInt64     var tcpi_rxbytes: UInt64     var tcpi_rxoutoforderbytes: UInt64     init()     init(tcpi_state tcpi_state: UInt8, tcpi_snd_wscale tcpi_snd_wscale: UInt8, tcpi_rcv_wscale tcpi_rcv_wscale: UInt8, __pad1 __pad1: UInt8, tcpi_options tcpi_options: UInt32, tcpi_flags tcpi_flags: UInt32, tcpi_rto tcpi_rto: UInt32, tcpi_maxseg tcpi_maxseg: UInt32, tcpi_snd_ssthresh tcpi_snd_ssthresh: UInt32, tcpi_snd_cwnd tcpi_snd_cwnd: UInt32, tcpi_snd_wnd tcpi_snd_wnd: UInt32, tcpi_snd_sbbytes tcpi_snd_sbbytes: UInt32, tcpi_rcv_wnd tcpi_rcv_wnd: UInt32, tcpi_rttcur tcpi_rttcur: UInt32, tcpi_srtt tcpi_srtt: UInt32, tcpi_rttvar tcpi_rttvar: UInt32, tcpi_tfo_cookie_req tcpi_tfo_cookie_req: UInt32, tcpi_tfo_cookie_rcv tcpi_tfo_cookie_rcv: UInt32, tcpi_tfo_syn_loss tcpi_tfo_syn_loss: UInt32, tcpi_tfo_syn_data_sent tcpi_tfo_syn_data_sent: UInt32, tcpi_tfo_syn_data_acked tcpi_tfo_syn_data_acked: UInt32, tcpi_tfo_syn_data_rcv tcpi_tfo_syn_data_rcv: UInt32, tcpi_tfo_cookie_req_rcv tcpi_tfo_cookie_req_rcv: UInt32, tcpi_tfo_cookie_sent tcpi_tfo_cookie_sent: UInt32, tcpi_tfo_cookie_invalid tcpi_tfo_cookie_invalid: UInt32, __pad2 __pad2: UInt32, tcpi_txpackets tcpi_txpackets: UInt64, tcpi_txbytes tcpi_txbytes: UInt64, tcpi_txretransmitbytes tcpi_txretransmitbytes: UInt64, tcpi_rxpackets tcpi_rxpackets: UInt64, tcpi_rxbytes tcpi_rxbytes: UInt64, tcpi_rxoutoforderbytes tcpi_rxoutoforderbytes: UInt64) } ``` |
| To | ``` struct tcp_connection_info {     var tcpi_state: UInt8     var tcpi_snd_wscale: UInt8     var tcpi_rcv_wscale: UInt8     var __pad1: UInt8     var tcpi_options: UInt32     var tcpi_flags: UInt32     var tcpi_rto: UInt32     var tcpi_maxseg: UInt32     var tcpi_snd_ssthresh: UInt32     var tcpi_snd_cwnd: UInt32     var tcpi_snd_wnd: UInt32     var tcpi_snd_sbbytes: UInt32     var tcpi_rcv_wnd: UInt32     var tcpi_rttcur: UInt32     var tcpi_srtt: UInt32     var tcpi_rttvar: UInt32     var tcpi_tfo_cookie_req: UInt32     var tcpi_tfo_cookie_rcv: UInt32     var tcpi_tfo_syn_loss: UInt32     var tcpi_tfo_syn_data_sent: UInt32     var tcpi_tfo_syn_data_acked: UInt32     var tcpi_tfo_syn_data_rcv: UInt32     var tcpi_tfo_cookie_req_rcv: UInt32     var tcpi_tfo_cookie_sent: UInt32     var tcpi_tfo_cookie_invalid: UInt32     var tcpi_tfo_cookie_wrong: UInt32     var tcpi_tfo_no_cookie_rcv: UInt32     var tcpi_tfo_heuristics_disable: UInt32     var tcpi_tfo_send_blackhole: UInt32     var tcpi_tfo_recv_blackhole: UInt32     var __pad2: UInt32     var tcpi_txpackets: UInt64     var tcpi_txbytes: UInt64     var tcpi_txretransmitbytes: UInt64     var tcpi_rxpackets: UInt64     var tcpi_rxbytes: UInt64     var tcpi_rxoutoforderbytes: UInt64     init()     init(tcpi_state tcpi_state: UInt8, tcpi_snd_wscale tcpi_snd_wscale: UInt8, tcpi_rcv_wscale tcpi_rcv_wscale: UInt8, __pad1 __pad1: UInt8, tcpi_options tcpi_options: UInt32, tcpi_flags tcpi_flags: UInt32, tcpi_rto tcpi_rto: UInt32, tcpi_maxseg tcpi_maxseg: UInt32, tcpi_snd_ssthresh tcpi_snd_ssthresh: UInt32, tcpi_snd_cwnd tcpi_snd_cwnd: UInt32, tcpi_snd_wnd tcpi_snd_wnd: UInt32, tcpi_snd_sbbytes tcpi_snd_sbbytes: UInt32, tcpi_rcv_wnd tcpi_rcv_wnd: UInt32, tcpi_rttcur tcpi_rttcur: UInt32, tcpi_srtt tcpi_srtt: UInt32, tcpi_rttvar tcpi_rttvar: UInt32, tcpi_tfo_cookie_req tcpi_tfo_cookie_req: UInt32, tcpi_tfo_cookie_rcv tcpi_tfo_cookie_rcv: UInt32, tcpi_tfo_syn_loss tcpi_tfo_syn_loss: UInt32, tcpi_tfo_syn_data_sent tcpi_tfo_syn_data_sent: UInt32, tcpi_tfo_syn_data_acked tcpi_tfo_syn_data_acked: UInt32, tcpi_tfo_syn_data_rcv tcpi_tfo_syn_data_rcv: UInt32, tcpi_tfo_cookie_req_rcv tcpi_tfo_cookie_req_rcv: UInt32, tcpi_tfo_cookie_sent tcpi_tfo_cookie_sent: UInt32, tcpi_tfo_cookie_invalid tcpi_tfo_cookie_invalid: UInt32, tcpi_tfo_cookie_wrong tcpi_tfo_cookie_wrong: UInt32, tcpi_tfo_no_cookie_rcv tcpi_tfo_no_cookie_rcv: UInt32, tcpi_tfo_heuristics_disable tcpi_tfo_heuristics_disable: UInt32, tcpi_tfo_send_blackhole tcpi_tfo_send_blackhole: UInt32, tcpi_tfo_recv_blackhole tcpi_tfo_recv_blackhole: UInt32, __pad2 __pad2: UInt32, tcpi_txpackets tcpi_txpackets: UInt64, tcpi_txbytes tcpi_txbytes: UInt64, tcpi_txretransmitbytes tcpi_txretransmitbytes: UInt64, tcpi_rxpackets tcpi_rxpackets: UInt64, tcpi_rxbytes tcpi_rxbytes: UInt64, tcpi_rxoutoforderbytes tcpi_rxoutoforderbytes: UInt64) } ``` |

Modified tm [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tm {     var tm_sec: Int32     var tm_min: Int32     var tm_hour: Int32     var tm_mday: Int32     var tm_mon: Int32     var tm_year: Int32     var tm_wday: Int32     var tm_yday: Int32     var tm_isdst: Int32     var tm_gmtoff: Int     var tm_zone: UnsafeMutablePointer<Int8>     init()     init(tm_sec tm_sec: Int32, tm_min tm_min: Int32, tm_hour tm_hour: Int32, tm_mday tm_mday: Int32, tm_mon tm_mon: Int32, tm_year tm_year: Int32, tm_wday tm_wday: Int32, tm_yday tm_yday: Int32, tm_isdst tm_isdst: Int32, tm_gmtoff tm_gmtoff: Int, tm_zone tm_zone: UnsafeMutablePointer<Int8>) } ``` |
| To | ``` struct tm {     var tm_sec: Int32     var tm_min: Int32     var tm_hour: Int32     var tm_mday: Int32     var tm_mon: Int32     var tm_year: Int32     var tm_wday: Int32     var tm_yday: Int32     var tm_isdst: Int32     var tm_gmtoff: Int     var tm_zone: UnsafeMutablePointer<Int8>!     init()     init(tm_sec tm_sec: Int32, tm_min tm_min: Int32, tm_hour tm_hour: Int32, tm_mday tm_mday: Int32, tm_mon tm_mon: Int32, tm_year tm_year: Int32, tm_wday tm_wday: Int32, tm_yday tm_yday: Int32, tm_isdst tm_isdst: Int32, tm_gmtoff tm_gmtoff: Int, tm_zone tm_zone: UnsafeMutablePointer<Int8>!) } ``` |

Modified tm.tm_zone

|  | Declaration |
| --- | --- |
| From | ``` var tm_zone: UnsafeMutablePointer<Int8> ``` |
| To | ``` var tm_zone: UnsafeMutablePointer<Int8>! ``` |

Modified ucred [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ucred {     struct __Unnamed_struct_cr_link {         var tqe_next: UnsafeMutablePointer<ucred>         var tqe_prev: UnsafeMutablePointer<UnsafeMutablePointer<ucred>>         init()         init(tqe_next tqe_next: UnsafeMutablePointer<ucred>, tqe_prev tqe_prev: UnsafeMutablePointer<UnsafeMutablePointer<ucred>>)     }     var cr_link: ucred.__Unnamed_struct_cr_link     var cr_ref: u_long     var cr_posix: posix_cred     var cr_label: COpaquePointer     var cr_audit: au_session     init()     init(cr_link cr_link: ucred.__Unnamed_struct_cr_link, cr_ref cr_ref: u_long, cr_posix cr_posix: posix_cred, cr_label cr_label: COpaquePointer, cr_audit cr_audit: au_session) } ``` |
| To | ``` struct ucred {     struct __Unnamed_struct_cr_link {         var tqe_next: UnsafeMutablePointer<ucred>!         var tqe_prev: UnsafeMutablePointer<UnsafeMutablePointer<ucred>?>!         init()         init(tqe_next tqe_next: UnsafeMutablePointer<ucred>!, tqe_prev tqe_prev: UnsafeMutablePointer<UnsafeMutablePointer<ucred>?>!)     }     var cr_link: ucred.__Unnamed_struct_cr_link     var cr_ref: u_long     var cr_posix: posix_cred     var cr_label: OpaquePointer!     var cr_audit: au_session     init()     init(cr_link cr_link: ucred.__Unnamed_struct_cr_link, cr_ref cr_ref: u_long, cr_posix cr_posix: posix_cred, cr_label cr_label: OpaquePointer!, cr_audit cr_audit: au_session) } ``` |

Modified ucred.cr_label

|  | Declaration |
| --- | --- |
| From | ``` var cr_label: COpaquePointer ``` |
| To | ``` var cr_label: OpaquePointer! ``` |

Modified vfsidctl [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vfsidctl {     var vc_vers: Int32     var vc_fsid: fsid_t     var vc_ptr: UnsafeMutablePointer<Void>     var vc_len: Int     var vc_spare: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)     init()     init(vc_vers vc_vers: Int32, vc_fsid vc_fsid: fsid_t, vc_ptr vc_ptr: UnsafeMutablePointer<Void>, vc_len vc_len: Int, vc_spare vc_spare: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)) } ``` |
| To | ``` struct vfsidctl {     var vc_vers: Int32     var vc_fsid: fsid_t     var vc_ptr: UnsafeMutableRawPointer!     var vc_len: Int     var vc_spare: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)     init()     init(vc_vers vc_vers: Int32, vc_fsid vc_fsid: fsid_t, vc_ptr vc_ptr: UnsafeMutableRawPointer!, vc_len vc_len: Int, vc_spare vc_spare: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified vfsidctl.vc_ptr

|  | Declaration |
| --- | --- |
| From | ``` var vc_ptr: UnsafeMutablePointer<Void> ``` |
| To | ``` var vc_ptr: UnsafeMutableRawPointer! ``` |

Modified vfsstatfs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vfsstatfs {     var f_bsize: UInt32     var f_iosize: Int     var f_blocks: UInt64     var f_bfree: UInt64     var f_bavail: UInt64     var f_bused: UInt64     var f_files: UInt64     var f_ffree: UInt64     var f_fsid: fsid_t     var f_owner: uid_t     var f_flags: UInt64     var f_fstypename: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var f_mntonname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var f_mntfromname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var f_fssubtype: UInt32     var f_reserved: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)     init()     init(f_bsize f_bsize: UInt32, f_iosize f_iosize: Int, f_blocks f_blocks: UInt64, f_bfree f_bfree: UInt64, f_bavail f_bavail: UInt64, f_bused f_bused: UInt64, f_files f_files: UInt64, f_ffree f_ffree: UInt64, f_fsid f_fsid: fsid_t, f_owner f_owner: uid_t, f_flags f_flags: UInt64, f_fstypename f_fstypename: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), f_mntonname f_mntonname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), f_mntfromname f_mntfromname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), f_fssubtype f_fssubtype: UInt32, f_reserved f_reserved: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)) } ``` |
| To | ``` struct vfsstatfs {     var f_bsize: UInt32     var f_iosize: Int     var f_blocks: UInt64     var f_bfree: UInt64     var f_bavail: UInt64     var f_bused: UInt64     var f_files: UInt64     var f_ffree: UInt64     var f_fsid: fsid_t     var f_owner: uid_t     var f_flags: UInt64     var f_fstypename: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var f_mntonname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var f_mntfromname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var f_fssubtype: UInt32     var f_reserved: (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?)     init()     init(f_bsize f_bsize: UInt32, f_iosize f_iosize: Int, f_blocks f_blocks: UInt64, f_bfree f_bfree: UInt64, f_bavail f_bavail: UInt64, f_bused f_bused: UInt64, f_files f_files: UInt64, f_ffree f_ffree: UInt64, f_fsid f_fsid: fsid_t, f_owner f_owner: uid_t, f_flags f_flags: UInt64, f_fstypename f_fstypename: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), f_mntonname f_mntonname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), f_mntfromname f_mntfromname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), f_fssubtype f_fssubtype: UInt32, f_reserved f_reserved: (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?)) } ``` |

Modified vfsstatfs.f_reserved

|  | Declaration |
| --- | --- |
| From | ``` var f_reserved: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) ``` |
| To | ``` var f_reserved: (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) ``` |

Modified vm_info_object.init(vio_object: natural_t, vio_size: natural_t, vio_ref_count: UInt32, vio_resident_page_count: UInt32, vio_absent_count: UInt32, vio_copy: natural_t, vio_shadow: natural_t, vio_shadow_offset: natural_t, vio_paging_offset: natural_t, vio_copy_strategy: memory_object_copy_strategy_t, vio_last_alloc: vm_offset_t, vio_paging_in_progress: UInt32, vio_pager_created: boolean_t, vio_pager_initialized: boolean_t, vio_pager_ready: boolean_t, vio_can_persist: boolean_t, vio_internal: boolean_t, vio_temporary: boolean_t, vio_alive: boolean_t, vio_purgable: boolean_t, vio_purgable_volatile: boolean_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.3 |

Modified vm_range_t.init(address: vm_address_t, size: vm_size_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.3 |

Modified vm_read_entry.init(address: vm_address_t, size: vm_size_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.3 |

Modified vmspace [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vmspace {     var dummy: Int32     var dummy2: caddr_t     var dummy3: (Int32, Int32, Int32, Int32, Int32)     var dummy4: (caddr_t, caddr_t, caddr_t)     init()     init(dummy dummy: Int32, dummy2 dummy2: caddr_t, dummy3 dummy3: (Int32, Int32, Int32, Int32, Int32), dummy4 dummy4: (caddr_t, caddr_t, caddr_t)) } ``` |
| To | ``` struct vmspace {     var dummy: Int32     var dummy2: caddr_t!     var dummy3: (Int32, Int32, Int32, Int32, Int32)     var dummy4: (caddr_t?, caddr_t?, caddr_t?)     init()     init(dummy dummy: Int32, dummy2 dummy2: caddr_t!, dummy3 dummy3: (Int32, Int32, Int32, Int32, Int32), dummy4 dummy4: (caddr_t?, caddr_t?, caddr_t?)) } ``` |

Modified vmspace.dummy2

|  | Declaration |
| --- | --- |
| From | ``` var dummy2: caddr_t ``` |
| To | ``` var dummy2: caddr_t! ``` |

Modified vmspace.dummy4

|  | Declaration |
| --- | --- |
| From | ``` var dummy4: (caddr_t, caddr_t, caddr_t) ``` |
| To | ``` var dummy4: (caddr_t?, caddr_t?, caddr_t?) ``` |

Modified vol_capabilities_attr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vol_capabilities_attr {     var capabilities: vol_capabilities_set_t     var valid: vol_capabilities_set_t     init()     init(capabilities capabilities: vol_capabilities_set_t, valid valid: vol_capabilities_set_t) } ``` |
| To | ``` struct vol_capabilities_attr {     var capabilities: Darwin.vol_capabilities_set_t     var valid: Darwin.vol_capabilities_set_t     init()     init(capabilities capabilities: Darwin.vol_capabilities_set_t, valid valid: Darwin.vol_capabilities_set_t) } ``` |

Modified vol_capabilities_attr.capabilities

|  | Declaration |
| --- | --- |
| From | ``` var capabilities: vol_capabilities_set_t ``` |
| To | ``` var capabilities: Darwin.vol_capabilities_set_t ``` |

Modified vol_capabilities_attr.init(capabilities: Darwin.vol_capabilities_set_t, valid: Darwin.vol_capabilities_set_t)

|  | Declaration |
| --- | --- |
| From | ``` init(capabilities capabilities: vol_capabilities_set_t, valid valid: vol_capabilities_set_t) ``` |
| To | ``` init(capabilities capabilities: Darwin.vol_capabilities_set_t, valid valid: Darwin.vol_capabilities_set_t) ``` |

Modified vol_capabilities_attr.valid

|  | Declaration |
| --- | --- |
| From | ``` var valid: vol_capabilities_set_t ``` |
| To | ``` var valid: Darwin.vol_capabilities_set_t ``` |

Modified wordexp_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct wordexp_t {     var we_wordc: Int     var we_wordv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var we_offs: Int     init()     init(we_wordc we_wordc: Int, we_wordv we_wordv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, we_offs we_offs: Int) } ``` |
| To | ``` struct wordexp_t {     var we_wordc: Int     var we_wordv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!     var we_offs: Int     init()     init(we_wordc we_wordc: Int, we_wordv we_wordv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, we_offs we_offs: Int) } ``` |

Modified wordexp_t.we_wordv

|  | Declaration |
| --- | --- |
| From | ``` var we_wordv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>> ``` |
| To | ``` var we_wordv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>! ``` |

Modified zone_info.init(zi_count: integer_t, zi_cur_size: vm_size_t, zi_max_size: vm_size_t, zi_elem_size: vm_size_t, zi_alloc_size: vm_size_t, zi_pageable: integer_t, zi_sleepable: integer_t, zi_exhaustible: integer_t, zi_collectable: integer_t)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.3 |

Modified ==(_: DarwinBoolean, _: DarwinBoolean) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ==(_ lhs: DarwinBoolean, _ rhs: DarwinBoolean) -> Bool ``` |
| To | ``` func ==(_ lhs: DarwinBoolean, _ rhs: DarwinBoolean) -> Bool ``` |

Modified a64l(_: UnsafePointer<Int8>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func a64l(_ _: UnsafePointer<Int8>) -> Int ``` |
| To | ``` func a64l(_ _: UnsafePointer<Int8>!) -> Int ``` |

Modified abort() -> Never

|  | Declaration |
| --- | --- |
| From | ``` @noreturn func abort() ``` |
| To | ``` func abort() -> Never ``` |

Modified accept(_: Int32, _: UnsafeMutablePointer<sockaddr>!, _: UnsafeMutablePointer<socklen_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func accept(_ _: Int32, _ _: UnsafeMutablePointer<sockaddr>, _ _: UnsafeMutablePointer<socklen_t>) -> Int32 ``` |
| To | ``` func accept(_ _: Int32, _ _: UnsafeMutablePointer<sockaddr>!, _ _: UnsafeMutablePointer<socklen_t>!) -> Int32 ``` |

Modified access(_: UnsafePointer<Int8>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func access(_ _: UnsafePointer<Int8>, _ _: Int32) -> Int32 ``` |
| To | ``` func access(_ _: UnsafePointer<Int8>!, _ _: Int32) -> Int32 ``` |

Modified accessx_np(_: UnsafePointer<accessx_descriptor>!, _: Int, _: UnsafeMutablePointer<Int32>!, _: uid_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func accessx_np(_ _: UnsafePointer<accessx_descriptor>, _ _: Int, _ _: UnsafeMutablePointer<Int32>, _ _: uid_t) -> Int32 ``` |
| To | ``` func accessx_np(_ _: UnsafePointer<accessx_descriptor>!, _ _: Int, _ _: UnsafeMutablePointer<Int32>!, _ _: uid_t) -> Int32 ``` |

Modified acct(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acct(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func acct(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified acl_add_flag_np(_: acl_flagset_t!, _: acl_flag_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_add_flag_np(_ flagset_d: acl_flagset_t, _ flag: acl_flag_t) -> Int32 ``` |
| To | ``` func acl_add_flag_np(_ flagset_d: acl_flagset_t!, _ flag: acl_flag_t) -> Int32 ``` |

Modified acl_add_perm(_: acl_permset_t!, _: acl_perm_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_add_perm(_ permset_d: acl_permset_t, _ perm: acl_perm_t) -> Int32 ``` |
| To | ``` func acl_add_perm(_ permset_d: acl_permset_t!, _ perm: acl_perm_t) -> Int32 ``` |

Modified acl_calc_mask(_: UnsafeMutablePointer<acl_t?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_calc_mask(_ acl_p: UnsafeMutablePointer<acl_t>) -> Int32 ``` |
| To | ``` func acl_calc_mask(_ acl_p: UnsafeMutablePointer<acl_t?>!) -> Int32 ``` |

Modified acl_clear_flags_np(_: acl_flagset_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_clear_flags_np(_ flagset_d: acl_flagset_t) -> Int32 ``` |
| To | ``` func acl_clear_flags_np(_ flagset_d: acl_flagset_t!) -> Int32 ``` |

Modified acl_clear_perms(_: acl_permset_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_clear_perms(_ permset_d: acl_permset_t) -> Int32 ``` |
| To | ``` func acl_clear_perms(_ permset_d: acl_permset_t!) -> Int32 ``` |

Modified acl_copy_entry(_: acl_entry_t!, _: acl_entry_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_copy_entry(_ dest_d: acl_entry_t, _ src_d: acl_entry_t) -> Int32 ``` |
| To | ``` func acl_copy_entry(_ dest_d: acl_entry_t!, _ src_d: acl_entry_t!) -> Int32 ``` |

Modified acl_copy_ext(_: UnsafeMutableRawPointer!, _: acl_t!, _: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func acl_copy_ext(_ buf_p: UnsafeMutablePointer<Void>, _ acl: acl_t, _ size: Int) -> Int ``` |
| To | ``` func acl_copy_ext(_ buf_p: UnsafeMutableRawPointer!, _ acl: acl_t!, _ size: Int) -> Int ``` |

Modified acl_copy_ext_native(_: UnsafeMutableRawPointer!, _: acl_t!, _: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func acl_copy_ext_native(_ buf_p: UnsafeMutablePointer<Void>, _ acl: acl_t, _ size: Int) -> Int ``` |
| To | ``` func acl_copy_ext_native(_ buf_p: UnsafeMutableRawPointer!, _ acl: acl_t!, _ size: Int) -> Int ``` |

Modified acl_copy_int(_: UnsafeRawPointer!) -> acl_t!

|  | Declaration |
| --- | --- |
| From | ``` func acl_copy_int(_ buf_p: UnsafePointer<Void>) -> acl_t ``` |
| To | ``` func acl_copy_int(_ buf_p: UnsafeRawPointer!) -> acl_t! ``` |

Modified acl_copy_int_native(_: UnsafeRawPointer!) -> acl_t!

|  | Declaration |
| --- | --- |
| From | ``` func acl_copy_int_native(_ buf_p: UnsafePointer<Void>) -> acl_t ``` |
| To | ``` func acl_copy_int_native(_ buf_p: UnsafeRawPointer!) -> acl_t! ``` |

Modified acl_create_entry(_: UnsafeMutablePointer<acl_t?>!, _: UnsafeMutablePointer<acl_entry_t?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_create_entry(_ acl_p: UnsafeMutablePointer<acl_t>, _ entry_p: UnsafeMutablePointer<acl_entry_t>) -> Int32 ``` |
| To | ``` func acl_create_entry(_ acl_p: UnsafeMutablePointer<acl_t?>!, _ entry_p: UnsafeMutablePointer<acl_entry_t?>!) -> Int32 ``` |

Modified acl_create_entry_np(_: UnsafeMutablePointer<acl_t?>!, _: UnsafeMutablePointer<acl_entry_t?>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_create_entry_np(_ acl_p: UnsafeMutablePointer<acl_t>, _ entry_p: UnsafeMutablePointer<acl_entry_t>, _ entry_index: Int32) -> Int32 ``` |
| To | ``` func acl_create_entry_np(_ acl_p: UnsafeMutablePointer<acl_t?>!, _ entry_p: UnsafeMutablePointer<acl_entry_t?>!, _ entry_index: Int32) -> Int32 ``` |

Modified acl_delete_def_file(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_delete_def_file(_ path_p: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func acl_delete_def_file(_ path_p: UnsafePointer<Int8>!) -> Int32 ``` |

Modified acl_delete_entry(_: acl_t!, _: acl_entry_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_delete_entry(_ acl: acl_t, _ entry_d: acl_entry_t) -> Int32 ``` |
| To | ``` func acl_delete_entry(_ acl: acl_t!, _ entry_d: acl_entry_t!) -> Int32 ``` |

Modified acl_delete_flag_np(_: acl_flagset_t!, _: acl_flag_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_delete_flag_np(_ flagset_d: acl_flagset_t, _ flag: acl_flag_t) -> Int32 ``` |
| To | ``` func acl_delete_flag_np(_ flagset_d: acl_flagset_t!, _ flag: acl_flag_t) -> Int32 ``` |

Modified acl_delete_perm(_: acl_permset_t!, _: acl_perm_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_delete_perm(_ permset_d: acl_permset_t, _ perm: acl_perm_t) -> Int32 ``` |
| To | ``` func acl_delete_perm(_ permset_d: acl_permset_t!, _ perm: acl_perm_t) -> Int32 ``` |

Modified acl_dup(_: acl_t!) -> acl_t!

|  | Declaration |
| --- | --- |
| From | ``` func acl_dup(_ acl: acl_t) -> acl_t ``` |
| To | ``` func acl_dup(_ acl: acl_t!) -> acl_t! ``` |

Modified acl_entry_t

|  | Declaration |
| --- | --- |
| From | ``` typealias acl_entry_t = COpaquePointer ``` |
| To | ``` typealias acl_entry_t = OpaquePointer ``` |

Modified acl_flagset_t

|  | Declaration |
| --- | --- |
| From | ``` typealias acl_flagset_t = COpaquePointer ``` |
| To | ``` typealias acl_flagset_t = OpaquePointer ``` |

Modified acl_free(_: UnsafeMutableRawPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_free(_ obj_p: UnsafeMutablePointer<Void>) -> Int32 ``` |
| To | ``` func acl_free(_ obj_p: UnsafeMutableRawPointer!) -> Int32 ``` |

Modified acl_from_text(_: UnsafePointer<Int8>!) -> acl_t!

|  | Declaration |
| --- | --- |
| From | ``` func acl_from_text(_ buf_p: UnsafePointer<Int8>) -> acl_t ``` |
| To | ``` func acl_from_text(_ buf_p: UnsafePointer<Int8>!) -> acl_t! ``` |

Modified acl_get_entry(_: acl_t!, _: Int32, _: UnsafeMutablePointer<acl_entry_t?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_get_entry(_ acl: acl_t, _ entry_id: Int32, _ entry_p: UnsafeMutablePointer<acl_entry_t>) -> Int32 ``` |
| To | ``` func acl_get_entry(_ acl: acl_t!, _ entry_id: Int32, _ entry_p: UnsafeMutablePointer<acl_entry_t?>!) -> Int32 ``` |

Modified acl_get_fd(_: Int32) -> acl_t!

|  | Declaration |
| --- | --- |
| From | ``` func acl_get_fd(_ fd: Int32) -> acl_t ``` |
| To | ``` func acl_get_fd(_ fd: Int32) -> acl_t! ``` |

Modified acl_get_fd_np(_: Int32, _: acl_type_t) -> acl_t!

|  | Declaration |
| --- | --- |
| From | ``` func acl_get_fd_np(_ fd: Int32, _ type: acl_type_t) -> acl_t ``` |
| To | ``` func acl_get_fd_np(_ fd: Int32, _ type: acl_type_t) -> acl_t! ``` |

Modified acl_get_file(_: UnsafePointer<Int8>!, _: acl_type_t) -> acl_t!

|  | Declaration |
| --- | --- |
| From | ``` func acl_get_file(_ path_p: UnsafePointer<Int8>, _ type: acl_type_t) -> acl_t ``` |
| To | ``` func acl_get_file(_ path_p: UnsafePointer<Int8>!, _ type: acl_type_t) -> acl_t! ``` |

Modified acl_get_flag_np(_: acl_flagset_t!, _: acl_flag_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_get_flag_np(_ flagset_d: acl_flagset_t, _ flag: acl_flag_t) -> Int32 ``` |
| To | ``` func acl_get_flag_np(_ flagset_d: acl_flagset_t!, _ flag: acl_flag_t) -> Int32 ``` |

Modified acl_get_flagset_np(_: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<acl_flagset_t?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_get_flagset_np(_ obj_p: UnsafeMutablePointer<Void>, _ flagset_p: UnsafeMutablePointer<acl_flagset_t>) -> Int32 ``` |
| To | ``` func acl_get_flagset_np(_ obj_p: UnsafeMutableRawPointer!, _ flagset_p: UnsafeMutablePointer<acl_flagset_t?>!) -> Int32 ``` |

Modified acl_get_link_np(_: UnsafePointer<Int8>!, _: acl_type_t) -> acl_t!

|  | Declaration |
| --- | --- |
| From | ``` func acl_get_link_np(_ path_p: UnsafePointer<Int8>, _ type: acl_type_t) -> acl_t ``` |
| To | ``` func acl_get_link_np(_ path_p: UnsafePointer<Int8>!, _ type: acl_type_t) -> acl_t! ``` |

Modified acl_get_perm_np(_: acl_permset_t!, _: acl_perm_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_get_perm_np(_ permset_d: acl_permset_t, _ perm: acl_perm_t) -> Int32 ``` |
| To | ``` func acl_get_perm_np(_ permset_d: acl_permset_t!, _ perm: acl_perm_t) -> Int32 ``` |

Modified acl_get_permset(_: acl_entry_t!, _: UnsafeMutablePointer<acl_permset_t?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_get_permset(_ entry_d: acl_entry_t, _ permset_p: UnsafeMutablePointer<acl_permset_t>) -> Int32 ``` |
| To | ``` func acl_get_permset(_ entry_d: acl_entry_t!, _ permset_p: UnsafeMutablePointer<acl_permset_t?>!) -> Int32 ``` |

Modified acl_get_permset_mask_np(_: acl_entry_t!, _: UnsafeMutablePointer<acl_permset_mask_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_get_permset_mask_np(_ entry_d: acl_entry_t, _ mask_p: UnsafeMutablePointer<acl_permset_mask_t>) -> Int32 ``` |
| To | ``` func acl_get_permset_mask_np(_ entry_d: acl_entry_t!, _ mask_p: UnsafeMutablePointer<acl_permset_mask_t>!) -> Int32 ``` |

Modified acl_get_qualifier(_: acl_entry_t!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func acl_get_qualifier(_ entry_d: acl_entry_t) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func acl_get_qualifier(_ entry_d: acl_entry_t!) -> UnsafeMutableRawPointer! ``` |

Modified acl_get_tag_type(_: acl_entry_t!, _: UnsafeMutablePointer<acl_tag_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_get_tag_type(_ entry_d: acl_entry_t, _ tag_type_p: UnsafeMutablePointer<acl_tag_t>) -> Int32 ``` |
| To | ``` func acl_get_tag_type(_ entry_d: acl_entry_t!, _ tag_type_p: UnsafeMutablePointer<acl_tag_t>!) -> Int32 ``` |

Modified acl_init(_: Int32) -> acl_t!

|  | Declaration |
| --- | --- |
| From | ``` func acl_init(_ count: Int32) -> acl_t ``` |
| To | ``` func acl_init(_ count: Int32) -> acl_t! ``` |

Modified acl_maximal_permset_mask_np(_: UnsafeMutablePointer<acl_permset_mask_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_maximal_permset_mask_np(_ mask_p: UnsafeMutablePointer<acl_permset_mask_t>) -> Int32 ``` |
| To | ``` func acl_maximal_permset_mask_np(_ mask_p: UnsafeMutablePointer<acl_permset_mask_t>!) -> Int32 ``` |

Modified acl_permset_t

|  | Declaration |
| --- | --- |
| From | ``` typealias acl_permset_t = COpaquePointer ``` |
| To | ``` typealias acl_permset_t = OpaquePointer ``` |

Modified acl_set_fd(_: Int32, _: acl_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_set_fd(_ fd: Int32, _ acl: acl_t) -> Int32 ``` |
| To | ``` func acl_set_fd(_ fd: Int32, _ acl: acl_t!) -> Int32 ``` |

Modified acl_set_fd_np(_: Int32, _: acl_t!, _: acl_type_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_set_fd_np(_ fd: Int32, _ acl: acl_t, _ acl_type: acl_type_t) -> Int32 ``` |
| To | ``` func acl_set_fd_np(_ fd: Int32, _ acl: acl_t!, _ acl_type: acl_type_t) -> Int32 ``` |

Modified acl_set_file(_: UnsafePointer<Int8>!, _: acl_type_t, _: acl_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_set_file(_ path_p: UnsafePointer<Int8>, _ type: acl_type_t, _ acl: acl_t) -> Int32 ``` |
| To | ``` func acl_set_file(_ path_p: UnsafePointer<Int8>!, _ type: acl_type_t, _ acl: acl_t!) -> Int32 ``` |

Modified acl_set_flagset_np(_: UnsafeMutableRawPointer!, _: acl_flagset_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_set_flagset_np(_ obj_p: UnsafeMutablePointer<Void>, _ flagset_d: acl_flagset_t) -> Int32 ``` |
| To | ``` func acl_set_flagset_np(_ obj_p: UnsafeMutableRawPointer!, _ flagset_d: acl_flagset_t!) -> Int32 ``` |

Modified acl_set_link_np(_: UnsafePointer<Int8>!, _: acl_type_t, _: acl_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_set_link_np(_ path_p: UnsafePointer<Int8>, _ type: acl_type_t, _ acl: acl_t) -> Int32 ``` |
| To | ``` func acl_set_link_np(_ path_p: UnsafePointer<Int8>!, _ type: acl_type_t, _ acl: acl_t!) -> Int32 ``` |

Modified acl_set_permset(_: acl_entry_t!, _: acl_permset_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_set_permset(_ entry_d: acl_entry_t, _ permset_d: acl_permset_t) -> Int32 ``` |
| To | ``` func acl_set_permset(_ entry_d: acl_entry_t!, _ permset_d: acl_permset_t!) -> Int32 ``` |

Modified acl_set_permset_mask_np(_: acl_entry_t!, _: acl_permset_mask_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_set_permset_mask_np(_ entry_d: acl_entry_t, _ mask: acl_permset_mask_t) -> Int32 ``` |
| To | ``` func acl_set_permset_mask_np(_ entry_d: acl_entry_t!, _ mask: acl_permset_mask_t) -> Int32 ``` |

Modified acl_set_qualifier(_: acl_entry_t!, _: UnsafeRawPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_set_qualifier(_ entry_d: acl_entry_t, _ tag_qualifier_p: UnsafePointer<Void>) -> Int32 ``` |
| To | ``` func acl_set_qualifier(_ entry_d: acl_entry_t!, _ tag_qualifier_p: UnsafeRawPointer!) -> Int32 ``` |

Modified acl_set_tag_type(_: acl_entry_t!, _: acl_tag_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_set_tag_type(_ entry_d: acl_entry_t, _ tag_type: acl_tag_t) -> Int32 ``` |
| To | ``` func acl_set_tag_type(_ entry_d: acl_entry_t!, _ tag_type: acl_tag_t) -> Int32 ``` |

Modified acl_size(_: acl_t!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func acl_size(_ acl: acl_t) -> Int ``` |
| To | ``` func acl_size(_ acl: acl_t!) -> Int ``` |

Modified acl_t

|  | Declaration |
| --- | --- |
| From | ``` typealias acl_t = COpaquePointer ``` |
| To | ``` typealias acl_t = OpaquePointer ``` |

Modified acl_to_text(_: acl_t!, _: UnsafeMutablePointer<Int>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func acl_to_text(_ acl: acl_t, _ len_p: UnsafeMutablePointer<Int>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func acl_to_text(_ acl: acl_t!, _ len_p: UnsafeMutablePointer<Int>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified acl_valid(_: acl_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_valid(_ acl: acl_t) -> Int32 ``` |
| To | ``` func acl_valid(_ acl: acl_t!) -> Int32 ``` |

Modified acl_valid_fd_np(_: Int32, _: acl_type_t, _: acl_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_valid_fd_np(_ fd: Int32, _ type: acl_type_t, _ acl: acl_t) -> Int32 ``` |
| To | ``` func acl_valid_fd_np(_ fd: Int32, _ type: acl_type_t, _ acl: acl_t!) -> Int32 ``` |

Modified acl_valid_file_np(_: UnsafePointer<Int8>!, _: acl_type_t, _: acl_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_valid_file_np(_ path: UnsafePointer<Int8>, _ type: acl_type_t, _ acl: acl_t) -> Int32 ``` |
| To | ``` func acl_valid_file_np(_ path: UnsafePointer<Int8>!, _ type: acl_type_t, _ acl: acl_t!) -> Int32 ``` |

Modified acl_valid_link_np(_: UnsafePointer<Int8>!, _: acl_type_t, _: acl_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func acl_valid_link_np(_ path: UnsafePointer<Int8>, _ type: acl_type_t, _ acl: acl_t) -> Int32 ``` |
| To | ``` func acl_valid_link_np(_ path: UnsafePointer<Int8>!, _ type: acl_type_t, _ acl: acl_t!) -> Int32 ``` |

Modified acos(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func acos(_ x: Float) -> Float ``` |
| To | ``` func acos(_ x: Float) -> Float ``` |

Modified acosh(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func acosh(_ x: Float) -> Float ``` |
| To | ``` func acosh(_ x: Float) -> Float ``` |

Modified act_get_state(_: thread_act_t, _: Int32, _: thread_state_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func act_get_state(_ target_act: thread_act_t, _ flavor: Int32, _ old_state: thread_state_t, _ old_stateCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func act_get_state(_ target_act: thread_act_t, _ flavor: Int32, _ old_state: thread_state_t!, _ old_stateCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified act_set_state(_: thread_act_t, _: Int32, _: thread_state_t!, _: mach_msg_type_number_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func act_set_state(_ target_act: thread_act_t, _ flavor: Int32, _ new_state: thread_state_t, _ new_stateCnt: mach_msg_type_number_t) -> kern_return_t ``` |
| To | ``` func act_set_state(_ target_act: thread_act_t, _ flavor: Int32, _ new_state: thread_state_t!, _ new_stateCnt: mach_msg_type_number_t) -> kern_return_t ``` |

Modified add_profil(_: UnsafeMutablePointer<Int8>!, _: Int, _: UInt, _: UInt32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func add_profil(_ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UInt, _ _: UInt32) -> Int32 ``` |
| To | ``` func add_profil(_ _: UnsafeMutablePointer<Int8>!, _ _: Int, _ _: UInt, _ _: UInt32) -> Int32 ``` |

Modified addr2ascii(_: Int32, _: UnsafeRawPointer!, _: Int32, _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func addr2ascii(_ _: Int32, _ _: UnsafePointer<Void>, _ _: Int32, _ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func addr2ascii(_ _: Int32, _ _: UnsafeRawPointer!, _ _: Int32, _ _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified adjtime(_: UnsafePointer<timeval>!, _: UnsafeMutablePointer<timeval>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func adjtime(_ _: UnsafePointer<timeval>, _ _: UnsafeMutablePointer<timeval>) -> Int32 ``` |
| To | ``` func adjtime(_ _: UnsafePointer<timeval>!, _ _: UnsafeMutablePointer<timeval>!) -> Int32 ``` |

Modified aio_cancel(_: Int32, _: UnsafeMutablePointer<aiocb>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func aio_cancel(_ fd: Int32, _ aiocbp: UnsafeMutablePointer<aiocb>) -> Int32 ``` |
| To | ``` func aio_cancel(_ fd: Int32, _ aiocbp: UnsafeMutablePointer<aiocb>!) -> Int32 ``` |

Modified aio_error(_: UnsafePointer<aiocb>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func aio_error(_ aiocbp: UnsafePointer<aiocb>) -> Int32 ``` |
| To | ``` func aio_error(_ aiocbp: UnsafePointer<aiocb>!) -> Int32 ``` |

Modified aio_fsync(_: Int32, _: UnsafeMutablePointer<aiocb>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func aio_fsync(_ op: Int32, _ aiocbp: UnsafeMutablePointer<aiocb>) -> Int32 ``` |
| To | ``` func aio_fsync(_ op: Int32, _ aiocbp: UnsafeMutablePointer<aiocb>!) -> Int32 ``` |

Modified aio_read(_: UnsafeMutablePointer<aiocb>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func aio_read(_ aiocbp: UnsafeMutablePointer<aiocb>) -> Int32 ``` |
| To | ``` func aio_read(_ aiocbp: UnsafeMutablePointer<aiocb>!) -> Int32 ``` |

Modified aio_return(_: UnsafeMutablePointer<aiocb>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func aio_return(_ aiocbp: UnsafeMutablePointer<aiocb>) -> Int ``` |
| To | ``` func aio_return(_ aiocbp: UnsafeMutablePointer<aiocb>!) -> Int ``` |

Modified aio_suspend(_: UnsafePointer<UnsafePointer<aiocb>?>!, _: Int32, _: UnsafePointer<timespec>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func aio_suspend(_ aiocblist: UnsafePointer<UnsafePointer<aiocb>>, _ nent: Int32, _ timeoutp: UnsafePointer<timespec>) -> Int32 ``` |
| To | ``` func aio_suspend(_ aiocblist: UnsafePointer<UnsafePointer<aiocb>?>!, _ nent: Int32, _ timeoutp: UnsafePointer<timespec>!) -> Int32 ``` |

Modified aio_write(_: UnsafeMutablePointer<aiocb>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func aio_write(_ aiocbp: UnsafeMutablePointer<aiocb>) -> Int32 ``` |
| To | ``` func aio_write(_ aiocbp: UnsafeMutablePointer<aiocb>!) -> Int32 ``` |

Modified alloca(_: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func alloca(_ _: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func alloca(_ _: Int) -> UnsafeMutableRawPointer! ``` |

Modified alphasort(_: UnsafeMutablePointer<UnsafePointer<dirent>?>!, _: UnsafeMutablePointer<UnsafePointer<dirent>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func alphasort(_ _: UnsafeMutablePointer<UnsafePointer<dirent>>, _ _: UnsafeMutablePointer<UnsafePointer<dirent>>) -> Int32 ``` |
| To | ``` func alphasort(_ _: UnsafeMutablePointer<UnsafePointer<dirent>?>!, _ _: UnsafeMutablePointer<UnsafePointer<dirent>?>!) -> Int32 ``` |

Modified arc4random_addrandom(_: UnsafeMutablePointer<UInt8>!, _: Int32)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func arc4random_addrandom(_ _: UnsafeMutablePointer<UInt8>, _ _: Int32) ``` | iOS 8.0 |
| To | ``` func arc4random_addrandom(_ _: UnsafeMutablePointer<UInt8>!, _ _: Int32) ``` | iOS 2.0 |

Modified arc4random_buf(_: UnsafeMutableRawPointer!, _: Int)

|  | Declaration |
| --- | --- |
| From | ``` func arc4random_buf(_ _: UnsafeMutablePointer<Void>, _ _: Int) ``` |
| To | ``` func arc4random_buf(_ __buf: UnsafeMutableRawPointer!, _ __nbytes: Int) ``` |

Modified arm_debug_state_t

|  | Declaration |
| --- | --- |
| From | ``` typealias arm_debug_state_t = __darwin_arm_debug_state ``` |
| To | ``` typealias arm_debug_state_t = arm_legacy_debug_state ``` |

Modified ascii2addr(_: Int32, _: UnsafePointer<Int8>!, _: UnsafeMutableRawPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ascii2addr(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Void>) -> Int32 ``` |
| To | ``` func ascii2addr(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: UnsafeMutableRawPointer!) -> Int32 ``` |

Modified asctime(_: UnsafePointer<tm>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func asctime(_ _: UnsafePointer<tm>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func asctime(_ _: UnsafePointer<tm>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified asctime_r(_: UnsafePointer<tm>!, _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func asctime_r(_ _: UnsafePointer<tm>, _ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func asctime_r(_ _: UnsafePointer<tm>!, _ _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified asin(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func asin(_ x: Float) -> Float ``` |
| To | ``` func asin(_ x: Float) -> Float ``` |

Modified asinh(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func asinh(_ x: Float) -> Float ``` |
| To | ``` func asinh(_ x: Float) -> Float ``` |

Modified atan(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func atan(_ x: Float) -> Float ``` |
| To | ``` func atan(_ x: Float) -> Float ``` |

Modified atan2(_: Float, _: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func atan2(_ lhs: Float, _ rhs: Float) -> Float ``` |
| To | ``` func atan2(_ lhs: Float, _ rhs: Float) -> Float ``` |

Modified atanh(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func atanh(_ x: Float) -> Float ``` |
| To | ``` func atanh(_ x: Float) -> Float ``` |

Modified atexit(_: () -> Swift.Void) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func atexit(_ _: (() -> Void)!) -> Int32 ``` |
| To | ``` func atexit(_ _: @escaping () -> Swift.Void) -> Int32 ``` |

Modified atexit_b(_: () -> Swift.Void) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func atexit_b(_ _: (() -> Void)!) -> Int32 ``` |
| To | ``` func atexit_b(_ _: @escaping () -> Swift.Void) -> Int32 ``` |

Modified atof(_: UnsafePointer<Int8>!) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func atof(_ _: UnsafePointer<Int8>) -> Double ``` |
| To | ``` func atof(_ _: UnsafePointer<Int8>!) -> Double ``` |

Modified atof_l(_: UnsafePointer<Int8>!, _: locale_t!) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func atof_l(_ _: UnsafePointer<Int8>, _ _: locale_t) -> Double ``` |
| To | ``` func atof_l(_ _: UnsafePointer<Int8>!, _ _: locale_t!) -> Double ``` |

Modified atoi(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func atoi(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func atoi(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified atoi_l(_: UnsafePointer<Int8>!, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func atoi_l(_ _: UnsafePointer<Int8>, _ _: locale_t) -> Int32 ``` |
| To | ``` func atoi_l(_ _: UnsafePointer<Int8>!, _ _: locale_t!) -> Int32 ``` |

Modified atol(_: UnsafePointer<Int8>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func atol(_ _: UnsafePointer<Int8>) -> Int ``` |
| To | ``` func atol(_ _: UnsafePointer<Int8>!) -> Int ``` |

Modified atol_l(_: UnsafePointer<Int8>!, _: locale_t!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func atol_l(_ _: UnsafePointer<Int8>, _ _: locale_t) -> Int ``` |
| To | ``` func atol_l(_ _: UnsafePointer<Int8>!, _ _: locale_t!) -> Int ``` |

Modified atoll(_: UnsafePointer<Int8>!) -> Int64

|  | Declaration |
| --- | --- |
| From | ``` func atoll(_ _: UnsafePointer<Int8>) -> Int64 ``` |
| To | ``` func atoll(_ _: UnsafePointer<Int8>!) -> Int64 ``` |

Modified atoll_l(_: UnsafePointer<Int8>!, _: locale_t!) -> Int64

|  | Declaration |
| --- | --- |
| From | ``` func atoll_l(_ _: UnsafePointer<Int8>, _ _: locale_t) -> Int64 ``` |
| To | ``` func atoll_l(_ _: UnsafePointer<Int8>!, _ _: locale_t!) -> Int64 ``` |

Modified audit(_: UnsafeRawPointer!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func audit(_ _: UnsafePointer<Void>, _ _: Int32) -> Int32 ``` |
| To | ``` func audit(_ _: UnsafeRawPointer!, _ _: Int32) -> Int32 ``` |

Modified audit_session_port(_: au_asid_t, _: UnsafeMutablePointer<mach_port_name_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func audit_session_port(_ asid: au_asid_t, _ portname: UnsafeMutablePointer<mach_port_name_t>) -> Int32 ``` |
| To | ``` func audit_session_port(_ asid: au_asid_t, _ portname: UnsafeMutablePointer<mach_port_name_t>!) -> Int32 ``` |

Modified auditctl(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func auditctl(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func auditctl(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified auditon(_: Int32, _: UnsafeMutableRawPointer!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func auditon(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: Int32) -> Int32 ``` |
| To | ``` func auditon(_ _: Int32, _ _: UnsafeMutableRawPointer!, _ _: Int32) -> Int32 ``` |

Modified basename(_: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func basename(_ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func basename(_ _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified bcmp(_: UnsafeRawPointer!, _: UnsafeRawPointer!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func bcmp(_ _: UnsafePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int) -> Int32 ``` |
| To | ``` func bcmp(_ _: UnsafeRawPointer!, _ _: UnsafeRawPointer!, _ _: Int) -> Int32 ``` |

Modified bcopy(_: UnsafeRawPointer!, _: UnsafeMutableRawPointer!, _: Int)

|  | Declaration |
| --- | --- |
| From | ``` func bcopy(_ _: UnsafePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: Int) ``` |
| To | ``` func bcopy(_ _: UnsafeRawPointer!, _ _: UnsafeMutableRawPointer!, _ _: Int) ``` |

Modified bind(_: Int32, _: UnsafePointer<sockaddr>!, _: socklen_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func bind(_ _: Int32, _ _: UnsafePointer<sockaddr>, _ _: socklen_t) -> Int32 ``` |
| To | ``` func bind(_ _: Int32, _ _: UnsafePointer<sockaddr>!, _ _: socklen_t) -> Int32 ``` |

Modified bindresvport(_: Int32, _: UnsafeMutablePointer<sockaddr_in>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func bindresvport(_ _: Int32, _ _: UnsafeMutablePointer<sockaddr_in>) -> Int32 ``` |
| To | ``` func bindresvport(_ _: Int32, _ _: UnsafeMutablePointer<sockaddr_in>!) -> Int32 ``` |

Modified bindresvport_sa(_: Int32, _: UnsafeMutablePointer<sockaddr>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func bindresvport_sa(_ _: Int32, _ _: UnsafeMutablePointer<sockaddr>) -> Int32 ``` |
| To | ``` func bindresvport_sa(_ _: Int32, _ _: UnsafeMutablePointer<sockaddr>!) -> Int32 ``` |

Modified brk(_: UnsafeRawPointer!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func brk(_ _: UnsafePointer<Void>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func brk(_ _: UnsafeRawPointer!) -> UnsafeMutableRawPointer! ``` |

Modified bsd_signal(_: Int32, _: ( (Int32) -> Swift.Void)?) -> ((Int32) -> Swift.Void)?

|  | Declaration |
| --- | --- |
| From | ``` func bsd_signal(_ _: Int32, _ _: ((Int32) -> Void)!) -> ((Int32) -> Void)! ``` |
| To | ``` func bsd_signal(_ _: Int32, _ _: (@escaping (Int32) -> Swift.Void)?) -> ((Int32) -> Swift.Void)? ``` |

Modified bsearch(_: UnsafeRawPointer!, _: UnsafeRawPointer!, _: Int, _: Int, _: (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func bsearch(_ _: UnsafePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int, _ _: Int, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func bsearch(_ __key: UnsafeRawPointer!, _ __base: UnsafeRawPointer!, _ __nel: Int, _ __width: Int, _ __compar: @escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) -> UnsafeMutableRawPointer! ``` |

Modified bsearch_b(_: UnsafeRawPointer!, _: UnsafeRawPointer!, _: Int, _: Int, _: (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func bsearch_b(_ _: UnsafePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int, _ _: Int, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func bsearch_b(_ __key: UnsafeRawPointer!, _ __base: UnsafeRawPointer!, _ __nel: Int, _ __width: Int, _ __compar: @escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) -> UnsafeMutableRawPointer! ``` |

Modified btowc_l(_: Int32, _: locale_t!) -> wint_t

|  | Declaration |
| --- | --- |
| From | ``` func btowc_l(_ _: Int32, _ _: locale_t) -> wint_t ``` |
| To | ``` func btowc_l(_ _: Int32, _ _: locale_t!) -> wint_t ``` |

Modified bzero(_: UnsafeMutableRawPointer!, _: Int)

|  | Declaration |
| --- | --- |
| From | ``` func bzero(_ _: UnsafeMutablePointer<Void>, _ _: Int) ``` |
| To | ``` func bzero(_ _: UnsafeMutableRawPointer!, _ _: Int) ``` |

Modified calloc(_: Int, _: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func calloc(_ _: Int, _ _: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func calloc(_ __count: Int, _ __size: Int) -> UnsafeMutableRawPointer! ``` |

Modified catclose(_: nl_catd!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func catclose(_ _: nl_catd) -> Int32 ``` |
| To | ``` func catclose(_ _: nl_catd!) -> Int32 ``` |

Modified catgets(_: nl_catd!, _: Int32, _: Int32, _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func catgets(_ _: nl_catd, _ _: Int32, _ _: Int32, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func catgets(_ _: nl_catd!, _ _: Int32, _ _: Int32, _ _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified catopen(_: UnsafePointer<Int8>!, _: Int32) -> nl_catd!

|  | Declaration |
| --- | --- |
| From | ``` func catopen(_ _: UnsafePointer<Int8>, _ _: Int32) -> nl_catd ``` |
| To | ``` func catopen(_ _: UnsafePointer<Int8>!, _ _: Int32) -> nl_catd! ``` |

Modified cbrt(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func cbrt(_ x: Float) -> Float ``` |
| To | ``` func cbrt(_ x: Float) -> Float ``` |

Modified cfgetispeed(_: UnsafePointer<termios>!) -> speed_t

|  | Declaration |
| --- | --- |
| From | ``` func cfgetispeed(_ _: UnsafePointer<termios>) -> speed_t ``` |
| To | ``` func cfgetispeed(_ _: UnsafePointer<termios>!) -> speed_t ``` |

Modified cfgetospeed(_: UnsafePointer<termios>!) -> speed_t

|  | Declaration |
| --- | --- |
| From | ``` func cfgetospeed(_ _: UnsafePointer<termios>) -> speed_t ``` |
| To | ``` func cfgetospeed(_ _: UnsafePointer<termios>!) -> speed_t ``` |

Modified cfmakeraw(_: UnsafeMutablePointer<termios>!)

|  | Declaration |
| --- | --- |
| From | ``` func cfmakeraw(_ _: UnsafeMutablePointer<termios>) ``` |
| To | ``` func cfmakeraw(_ _: UnsafeMutablePointer<termios>!) ``` |

Modified cfsetispeed(_: UnsafeMutablePointer<termios>!, _: speed_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func cfsetispeed(_ _: UnsafeMutablePointer<termios>, _ _: speed_t) -> Int32 ``` |
| To | ``` func cfsetispeed(_ _: UnsafeMutablePointer<termios>!, _ _: speed_t) -> Int32 ``` |

Modified cfsetospeed(_: UnsafeMutablePointer<termios>!, _: speed_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func cfsetospeed(_ _: UnsafeMutablePointer<termios>, _ _: speed_t) -> Int32 ``` |
| To | ``` func cfsetospeed(_ _: UnsafeMutablePointer<termios>!, _ _: speed_t) -> Int32 ``` |

Modified cfsetspeed(_: UnsafeMutablePointer<termios>!, _: speed_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func cfsetspeed(_ _: UnsafeMutablePointer<termios>, _ _: speed_t) -> Int32 ``` |
| To | ``` func cfsetspeed(_ _: UnsafeMutablePointer<termios>!, _ _: speed_t) -> Int32 ``` |

Modified cgetcap(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int32) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func cgetcap(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int32) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func cgetcap(_ _: UnsafeMutablePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: Int32) -> UnsafeMutablePointer<Int8>! ``` |

Modified cgetent(_: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func cgetent(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func cgetent(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified cgetfirst(_: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func cgetfirst(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int32 ``` |
| To | ``` func cgetfirst(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Int32 ``` |

Modified cgetmatch(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func cgetmatch(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func cgetmatch(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified cgetnext(_: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func cgetnext(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int32 ``` |
| To | ``` func cgetnext(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Int32 ``` |

Modified cgetnum(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Int>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func cgetnum(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Int>) -> Int32 ``` |
| To | ``` func cgetnum(_ _: UnsafeMutablePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<Int>!) -> Int32 ``` |

Modified cgetset(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func cgetset(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func cgetset(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified cgetstr(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func cgetstr(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int32 ``` |
| To | ``` func cgetstr(_ _: UnsafeMutablePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Int32 ``` |

Modified cgetustr(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func cgetustr(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int32 ``` |
| To | ``` func cgetustr(_ _: UnsafeMutablePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Int32 ``` |

Modified chdir(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func chdir(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func chdir(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified chflags(_: UnsafePointer<Int8>!, _: __uint32_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func chflags(_ _: UnsafePointer<Int8>, _ _: __uint32_t) -> Int32 ``` |
| To | ``` func chflags(_ _: UnsafePointer<Int8>!, _ _: __uint32_t) -> Int32 ``` |

Modified chmod(_: UnsafePointer<Int8>!, _: mode_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func chmod(_ _: UnsafePointer<Int8>, _ _: mode_t) -> Int32 ``` |
| To | ``` func chmod(_ _: UnsafePointer<Int8>!, _ _: mode_t) -> Int32 ``` |

Modified chmodx_np(_: UnsafePointer<Int8>!, _: filesec_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func chmodx_np(_ _: UnsafePointer<Int8>, _ _: filesec_t) -> Int32 ``` |
| To | ``` func chmodx_np(_ _: UnsafePointer<Int8>!, _ _: filesec_t!) -> Int32 ``` |

Modified chown(_: UnsafePointer<Int8>!, _: uid_t, _: gid_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func chown(_ _: UnsafePointer<Int8>, _ _: uid_t, _ _: gid_t) -> Int32 ``` |
| To | ``` func chown(_ _: UnsafePointer<Int8>!, _ _: uid_t, _ _: gid_t) -> Int32 ``` |

Modified chroot(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func chroot(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func chroot(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified clearerr(_: UnsafeMutablePointer<FILE>!)

|  | Declaration |
| --- | --- |
| From | ``` func clearerr(_ _: UnsafeMutablePointer<FILE>) ``` |
| To | ``` func clearerr(_ _: UnsafeMutablePointer<FILE>!) ``` |

Modified clock_get_attributes(_: clock_serv_t, _: clock_flavor_t, _: clock_attr_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func clock_get_attributes(_ clock_serv: clock_serv_t, _ flavor: clock_flavor_t, _ clock_attr: clock_attr_t, _ clock_attrCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func clock_get_attributes(_ clock_serv: clock_serv_t, _ flavor: clock_flavor_t, _ clock_attr: clock_attr_t!, _ clock_attrCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified clock_get_res(_: mach_port_t, _: UnsafeMutablePointer<clock_res_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func clock_get_res(_ _: mach_port_t, _ _: UnsafeMutablePointer<clock_res_t>) -> kern_return_t ``` |
| To | ``` func clock_get_res(_ _: mach_port_t, _ _: UnsafeMutablePointer<clock_res_t>!) -> kern_return_t ``` |

Modified clock_get_time(_: clock_serv_t, _: UnsafeMutablePointer<mach_timespec_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func clock_get_time(_ clock_serv: clock_serv_t, _ cur_time: UnsafeMutablePointer<mach_timespec_t>) -> kern_return_t ``` |
| To | ``` func clock_get_time(_ clock_serv: clock_serv_t, _ cur_time: UnsafeMutablePointer<mach_timespec_t>!) -> kern_return_t ``` |

Modified clock_set_attributes(_: clock_ctrl_t, _: clock_flavor_t, _: clock_attr_t!, _: mach_msg_type_number_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func clock_set_attributes(_ clock_ctrl: clock_ctrl_t, _ flavor: clock_flavor_t, _ clock_attr: clock_attr_t, _ clock_attrCnt: mach_msg_type_number_t) -> kern_return_t ``` |
| To | ``` func clock_set_attributes(_ clock_ctrl: clock_ctrl_t, _ flavor: clock_flavor_t, _ clock_attr: clock_attr_t!, _ clock_attrCnt: mach_msg_type_number_t) -> kern_return_t ``` |

Modified clock_sleep(_: mach_port_t, _: Int32, _: mach_timespec_t, _: UnsafeMutablePointer<mach_timespec_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func clock_sleep(_ _: mach_port_t, _ _: Int32, _ _: mach_timespec_t, _ _: UnsafeMutablePointer<mach_timespec_t>) -> kern_return_t ``` |
| To | ``` func clock_sleep(_ _: mach_port_t, _ _: Int32, _ _: mach_timespec_t, _ _: UnsafeMutablePointer<mach_timespec_t>!) -> kern_return_t ``` |

Modified clock_sleep_trap(_: mach_port_name_t, _: sleep_type_t, _: Int32, _: Int32, _: UnsafeMutablePointer<mach_timespec_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func clock_sleep_trap(_ clock_name: mach_port_name_t, _ sleep_type: sleep_type_t, _ sleep_sec: Int32, _ sleep_nsec: Int32, _ wakeup_time: UnsafeMutablePointer<mach_timespec_t>) -> kern_return_t ``` |
| To | ``` func clock_sleep_trap(_ clock_name: mach_port_name_t, _ sleep_type: sleep_type_t, _ sleep_sec: Int32, _ sleep_nsec: Int32, _ wakeup_time: UnsafeMutablePointer<mach_timespec_t>!) -> kern_return_t ``` |

Modified closedir(_: UnsafeMutablePointer<DIR>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func closedir(_ _: UnsafeMutablePointer<DIR>) -> Int32 ``` |
| To | ``` func closedir(_ _: UnsafeMutablePointer<DIR>!) -> Int32 ``` |

Modified confstr(_: Int32, _: UnsafeMutablePointer<Int8>!, _: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func confstr(_ _: Int32, _ _: UnsafeMutablePointer<Int8>, _ _: Int) -> Int ``` |
| To | ``` func confstr(_ _: Int32, _ _: UnsafeMutablePointer<Int8>!, _ _: Int) -> Int ``` |

Modified connect(_: Int32, _: UnsafePointer<sockaddr>!, _: socklen_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func connect(_ _: Int32, _ _: UnsafePointer<sockaddr>, _ _: socklen_t) -> Int32 ``` |
| To | ``` func connect(_ _: Int32, _ _: UnsafePointer<sockaddr>!, _ _: socklen_t) -> Int32 ``` |

Modified connectx(_: Int32, _: UnsafePointer<sa_endpoints_t>!, _: sae_associd_t, _: UInt32, _: UnsafePointer<iovec>!, _: UInt32, _: UnsafeMutablePointer<Int>!, _: UnsafeMutablePointer<sae_connid_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func connectx(_ _: Int32, _ _: UnsafePointer<sa_endpoints_t>, _ _: sae_associd_t, _ _: UInt32, _ _: UnsafePointer<iovec>, _ _: UInt32, _ _: UnsafeMutablePointer<Int>, _ _: UnsafeMutablePointer<sae_connid_t>) -> Int32 ``` |
| To | ``` func connectx(_ _: Int32, _ _: UnsafePointer<sa_endpoints_t>!, _ _: sae_associd_t, _ _: UInt32, _ _: UnsafePointer<iovec>!, _ _: UInt32, _ _: UnsafeMutablePointer<Int>!, _ _: UnsafeMutablePointer<sae_connid_t>!) -> Int32 ``` |

Modified copyfile(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: copyfile_state_t!, _: copyfile_flags_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func copyfile(_ from: UnsafePointer<Int8>, _ to: UnsafePointer<Int8>, _ state: copyfile_state_t, _ flags: copyfile_flags_t) -> Int32 ``` |
| To | ``` func copyfile(_ from: UnsafePointer<Int8>!, _ to: UnsafePointer<Int8>!, _ state: copyfile_state_t!, _ flags: copyfile_flags_t) -> Int32 ``` |

Modified copyfile_callback_t

|  | Declaration |
| --- | --- |
| From | ``` typealias copyfile_callback_t = (Int32, Int32, copyfile_state_t, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafeMutablePointer<Void>) -> Int32 ``` |
| To | ``` typealias copyfile_callback_t = (Int32, Int32, copyfile_state_t?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafeMutableRawPointer?) -> Int32 ``` |

Modified copyfile_state_alloc() -> copyfile_state_t!

|  | Declaration |
| --- | --- |
| From | ``` func copyfile_state_alloc() -> copyfile_state_t ``` |
| To | ``` func copyfile_state_alloc() -> copyfile_state_t! ``` |

Modified copyfile_state_free(_: copyfile_state_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func copyfile_state_free(_ _: copyfile_state_t) -> Int32 ``` |
| To | ``` func copyfile_state_free(_ _: copyfile_state_t!) -> Int32 ``` |

Modified copyfile_state_get(_: copyfile_state_t!, _: UInt32, _: UnsafeMutableRawPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func copyfile_state_get(_ s: copyfile_state_t, _ flag: UInt32, _ dst: UnsafeMutablePointer<Void>) -> Int32 ``` |
| To | ``` func copyfile_state_get(_ s: copyfile_state_t!, _ flag: UInt32, _ dst: UnsafeMutableRawPointer!) -> Int32 ``` |

Modified copyfile_state_set(_: copyfile_state_t!, _: UInt32, _: UnsafeRawPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func copyfile_state_set(_ s: copyfile_state_t, _ flag: UInt32, _ src: UnsafePointer<Void>) -> Int32 ``` |
| To | ``` func copyfile_state_set(_ s: copyfile_state_t!, _ flag: UInt32, _ src: UnsafeRawPointer!) -> Int32 ``` |

Modified copyfile_state_t

|  | Declaration |
| --- | --- |
| From | ``` typealias copyfile_state_t = COpaquePointer ``` |
| To | ``` typealias copyfile_state_t = OpaquePointer ``` |

Modified copysign(_: Float, _: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func copysign(_ lhs: Float, _ rhs: Float) -> Float ``` |
| To | ``` func copysign(_ lhs: Float, _ rhs: Float) -> Float ``` |

Modified cos(_: Double) -> Double

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func cos(_ x: Double) -> Double ``` |
| To | ``` func cos(_ x: Double) -> Double ``` |

Modified cos(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func cos(_ x: Float) -> Float ``` |
| To | ``` func cos(_ x: Float) -> Float ``` |

Modified cosh(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func cosh(_ x: Float) -> Float ``` |
| To | ``` func cosh(_ x: Float) -> Float ``` |

Modified creat(_: UnsafePointer<Int8>!, _: mode_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func creat(_ _: UnsafePointer<Int8>, _ _: mode_t) -> Int32 ``` |
| To | ``` func creat(_ _: UnsafePointer<Int8>!, _ _: mode_t) -> Int32 ``` |

Modified crypt(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func crypt(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func crypt(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified ctermid(_: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func ctermid(_ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func ctermid(_ _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified ctermid_r(_: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func ctermid_r(_ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func ctermid_r(_ _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified ctime(_: UnsafePointer<time_t>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func ctime(_ _: UnsafePointer<time_t>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func ctime(_ _: UnsafePointer<time_t>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified ctime_r(_: UnsafePointer<time_t>!, _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func ctime_r(_ _: UnsafePointer<time_t>, _ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func ctime_r(_ _: UnsafePointer<time_t>!, _ _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified dbm_clearerr(_: UnsafeMutablePointer<DBM>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func dbm_clearerr(_ _: UnsafeMutablePointer<DBM>) -> Int32 ``` |
| To | ``` func dbm_clearerr(_ _: UnsafeMutablePointer<DBM>!) -> Int32 ``` |

Modified dbm_close(_: UnsafeMutablePointer<DBM>!)

|  | Declaration |
| --- | --- |
| From | ``` func dbm_close(_ _: UnsafeMutablePointer<DBM>) ``` |
| To | ``` func dbm_close(_ _: UnsafeMutablePointer<DBM>!) ``` |

Modified dbm_delete(_: UnsafeMutablePointer<DBM>!, _: datum) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func dbm_delete(_ _: UnsafeMutablePointer<DBM>, _ _: datum) -> Int32 ``` |
| To | ``` func dbm_delete(_ _: UnsafeMutablePointer<DBM>!, _ _: datum) -> Int32 ``` |

Modified dbm_dirfno(_: UnsafeMutablePointer<DBM>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func dbm_dirfno(_ _: UnsafeMutablePointer<DBM>) -> Int32 ``` |
| To | ``` func dbm_dirfno(_ _: UnsafeMutablePointer<DBM>!) -> Int32 ``` |

Modified dbm_error(_: UnsafeMutablePointer<DBM>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func dbm_error(_ _: UnsafeMutablePointer<DBM>) -> Int32 ``` |
| To | ``` func dbm_error(_ _: UnsafeMutablePointer<DBM>!) -> Int32 ``` |

Modified dbm_fetch(_: UnsafeMutablePointer<DBM>!, _: datum) -> datum

|  | Declaration |
| --- | --- |
| From | ``` func dbm_fetch(_ _: UnsafeMutablePointer<DBM>, _ _: datum) -> datum ``` |
| To | ``` func dbm_fetch(_ _: UnsafeMutablePointer<DBM>!, _ _: datum) -> datum ``` |

Modified dbm_firstkey(_: UnsafeMutablePointer<DBM>!) -> datum

|  | Declaration |
| --- | --- |
| From | ``` func dbm_firstkey(_ _: UnsafeMutablePointer<DBM>) -> datum ``` |
| To | ``` func dbm_firstkey(_ _: UnsafeMutablePointer<DBM>!) -> datum ``` |

Modified dbm_forder(_: UnsafeMutablePointer<DBM>!, _: datum) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func dbm_forder(_ _: UnsafeMutablePointer<DBM>, _ _: datum) -> Int ``` |
| To | ``` func dbm_forder(_ _: UnsafeMutablePointer<DBM>!, _ _: datum) -> Int ``` |

Modified dbm_nextkey(_: UnsafeMutablePointer<DBM>!) -> datum

|  | Declaration |
| --- | --- |
| From | ``` func dbm_nextkey(_ _: UnsafeMutablePointer<DBM>) -> datum ``` |
| To | ``` func dbm_nextkey(_ _: UnsafeMutablePointer<DBM>!) -> datum ``` |

Modified dbm_open(_: UnsafePointer<Int8>!, _: Int32, _: mode_t) -> UnsafeMutablePointer<DBM>!

|  | Declaration |
| --- | --- |
| From | ``` func dbm_open(_ _: UnsafePointer<Int8>, _ _: Int32, _ _: mode_t) -> UnsafeMutablePointer<DBM> ``` |
| To | ``` func dbm_open(_ _: UnsafePointer<Int8>!, _ _: Int32, _ _: mode_t) -> UnsafeMutablePointer<DBM>! ``` |

Modified dbm_store(_: UnsafeMutablePointer<DBM>!, _: datum, _: datum, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func dbm_store(_ _: UnsafeMutablePointer<DBM>, _ _: datum, _ _: datum, _ _: Int32) -> Int32 ``` |
| To | ``` func dbm_store(_ _: UnsafeMutablePointer<DBM>!, _ _: datum, _ _: datum, _ _: Int32) -> Int32 ``` |

Modified devname(_: dev_t, _: mode_t) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func devname(_ _: dev_t, _ _: mode_t) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func devname(_ _: dev_t, _ _: mode_t) -> UnsafeMutablePointer<Int8>! ``` |

Modified devname_r(_: dev_t, _: mode_t, _: UnsafeMutablePointer<Int8>!, _: Int32) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func devname_r(_ _: dev_t, _ _: mode_t, _ buf: UnsafeMutablePointer<Int8>, _ len: Int32) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func devname_r(_ _: dev_t, _ _: mode_t, _ buf: UnsafeMutablePointer<Int8>!, _ len: Int32) -> UnsafeMutablePointer<Int8>! ``` |

Modified digittoint_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func digittoint_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func digittoint_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified dirfd(_: UnsafeMutablePointer<DIR>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func dirfd(_ dirp: UnsafeMutablePointer<DIR>) -> Int32 ``` |
| To | ``` func dirfd(_ dirp: UnsafeMutablePointer<DIR>!) -> Int32 ``` |

Modified dirname(_: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func dirname(_ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func dirname(_ _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified dladdr(_: UnsafeRawPointer!, _: UnsafeMutablePointer<Dl_info>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func dladdr(_ _: UnsafePointer<Void>, _ _: UnsafeMutablePointer<Dl_info>) -> Int32 ``` |
| To | ``` func dladdr(_ _: UnsafeRawPointer!, _ _: UnsafeMutablePointer<Dl_info>!) -> Int32 ``` |

Modified dlclose(_: UnsafeMutableRawPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func dlclose(_ __handle: UnsafeMutablePointer<Void>) -> Int32 ``` |
| To | ``` func dlclose(_ __handle: UnsafeMutableRawPointer!) -> Int32 ``` |

Modified dlerror() -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func dlerror() -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func dlerror() -> UnsafeMutablePointer<Int8>! ``` |

Modified dlopen(_: UnsafePointer<Int8>!, _: Int32) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func dlopen(_ __path: UnsafePointer<Int8>, _ __mode: Int32) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func dlopen(_ __path: UnsafePointer<Int8>!, _ __mode: Int32) -> UnsafeMutableRawPointer! ``` |

Modified dlopen_preflight(_: UnsafePointer<Int8>!) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func dlopen_preflight(_ __path: UnsafePointer<Int8>) -> Bool ``` |
| To | ``` func dlopen_preflight(_ __path: UnsafePointer<Int8>!) -> Bool ``` |

Modified dlsym(_: UnsafeMutableRawPointer!, _: UnsafePointer<Int8>!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func dlsym(_ __handle: UnsafeMutablePointer<Void>, _ __symbol: UnsafePointer<Int8>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func dlsym(_ __handle: UnsafeMutableRawPointer!, _ __symbol: UnsafePointer<Int8>!) -> UnsafeMutableRawPointer! ``` |

Modified duplocale(_: locale_t!) -> locale_t!

|  | Declaration |
| --- | --- |
| From | ``` func duplocale(_ _: locale_t) -> locale_t ``` |
| To | ``` func duplocale(_ _: locale_t!) -> locale_t! ``` |

Modified ecvt(_: Double, _: Int32, _: UnsafeMutablePointer<Int32>!, _: UnsafeMutablePointer<Int32>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func ecvt(_ _: Double, _ _: Int32, _ _: UnsafeMutablePointer<Int32>, _ _: UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func ecvt(_ _: Double, _ _: Int32, _ _: UnsafeMutablePointer<Int32>!, _ _: UnsafeMutablePointer<Int32>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified encrypt(_: UnsafeMutablePointer<Int8>!, _: Int32)

|  | Declaration |
| --- | --- |
| From | ``` func encrypt(_ _: UnsafeMutablePointer<Int8>, _ _: Int32) ``` |
| To | ``` func encrypt(_ _: UnsafeMutablePointer<Int8>!, _ _: Int32) ``` |

Modified erand48(_: UnsafeMutablePointer<UInt16>!) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func erand48(_ _: UnsafeMutablePointer<UInt16>) -> Double ``` |
| To | ``` func erand48(_ _: UnsafeMutablePointer<UInt16>!) -> Double ``` |

Modified erf(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func erf(_ x: Float) -> Float ``` |
| To | ``` func erf(_ x: Float) -> Float ``` |

Modified erfc(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func erfc(_ x: Float) -> Float ``` |
| To | ``` func erfc(_ x: Float) -> Float ``` |

Modified err_set_exit(_: ( (Int32) -> Swift.Void)?)

|  | Declaration |
| --- | --- |
| From | ``` func err_set_exit(_ _: ((Int32) -> Void)!) ``` |
| To | ``` func err_set_exit(_ _: (@escaping (Int32) -> Swift.Void)?) ``` |

Modified err_set_exit_b(_: ( (Int32) -> Swift.Void)?)

|  | Declaration |
| --- | --- |
| From | ``` func err_set_exit_b(_ _: ((Int32) -> Void)!) ``` |
| To | ``` func err_set_exit_b(_ _: (@escaping (Int32) -> Swift.Void)?) ``` |

Modified err_set_file(_: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func err_set_file(_ _: UnsafeMutablePointer<Void>) ``` |
| To | ``` func err_set_file(_ _: UnsafeMutableRawPointer!) ``` |

Modified exception_raise(_: mach_port_t, _: mach_port_t, _: mach_port_t, _: exception_type_t, _: exception_data_t!, _: mach_msg_type_number_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func exception_raise(_ exception_port: mach_port_t, _ thread: mach_port_t, _ task: mach_port_t, _ exception: exception_type_t, _ code: exception_data_t, _ codeCnt: mach_msg_type_number_t) -> kern_return_t ``` |
| To | ``` func exception_raise(_ exception_port: mach_port_t, _ thread: mach_port_t, _ task: mach_port_t, _ exception: exception_type_t, _ code: exception_data_t!, _ codeCnt: mach_msg_type_number_t) -> kern_return_t ``` |

Modified exception_raise_state(_: mach_port_t, _: exception_type_t, _: exception_data_t!, _: mach_msg_type_number_t, _: UnsafeMutablePointer<Int32>!, _: thread_state_t!, _: mach_msg_type_number_t, _: thread_state_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func exception_raise_state(_ exception_port: mach_port_t, _ exception: exception_type_t, _ code: exception_data_t, _ codeCnt: mach_msg_type_number_t, _ flavor: UnsafeMutablePointer<Int32>, _ old_state: thread_state_t, _ old_stateCnt: mach_msg_type_number_t, _ new_state: thread_state_t, _ new_stateCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func exception_raise_state(_ exception_port: mach_port_t, _ exception: exception_type_t, _ code: exception_data_t!, _ codeCnt: mach_msg_type_number_t, _ flavor: UnsafeMutablePointer<Int32>!, _ old_state: thread_state_t!, _ old_stateCnt: mach_msg_type_number_t, _ new_state: thread_state_t!, _ new_stateCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified exception_raise_state_identity(_: mach_port_t, _: mach_port_t, _: mach_port_t, _: exception_type_t, _: exception_data_t!, _: mach_msg_type_number_t, _: UnsafeMutablePointer<Int32>!, _: thread_state_t!, _: mach_msg_type_number_t, _: thread_state_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func exception_raise_state_identity(_ exception_port: mach_port_t, _ thread: mach_port_t, _ task: mach_port_t, _ exception: exception_type_t, _ code: exception_data_t, _ codeCnt: mach_msg_type_number_t, _ flavor: UnsafeMutablePointer<Int32>, _ old_state: thread_state_t, _ old_stateCnt: mach_msg_type_number_t, _ new_state: thread_state_t, _ new_stateCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func exception_raise_state_identity(_ exception_port: mach_port_t, _ thread: mach_port_t, _ task: mach_port_t, _ exception: exception_type_t, _ code: exception_data_t!, _ codeCnt: mach_msg_type_number_t, _ flavor: UnsafeMutablePointer<Int32>!, _ old_state: thread_state_t!, _ old_stateCnt: mach_msg_type_number_t, _ new_state: thread_state_t!, _ new_stateCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified exchangedata(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UInt32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func exchangedata(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UInt) -> Int32 ``` |
| To | ``` func exchangedata(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: UInt32) -> Int32 ``` |

Modified execv(_: UnsafePointer<Int8>!, _: UnsafePointer<UnsafeMutablePointer<Int8>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func execv(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<UnsafeMutablePointer<Int8>>) -> Int32 ``` |
| To | ``` func execv(_ __path: UnsafePointer<Int8>!, _ __argv: UnsafePointer<UnsafeMutablePointer<Int8>?>!) -> Int32 ``` |

Modified execve(_: UnsafePointer<Int8>!, _: UnsafePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafePointer<UnsafeMutablePointer<Int8>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func execve(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafePointer<UnsafeMutablePointer<Int8>>) -> Int32 ``` |
| To | ``` func execve(_ __file: UnsafePointer<Int8>!, _ __argv: UnsafePointer<UnsafeMutablePointer<Int8>?>!, _ __envp: UnsafePointer<UnsafeMutablePointer<Int8>?>!) -> Int32 ``` |

Modified execvp(_: UnsafePointer<Int8>!, _: UnsafePointer<UnsafeMutablePointer<Int8>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func execvp(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<UnsafeMutablePointer<Int8>>) -> Int32 ``` |
| To | ``` func execvp(_ __file: UnsafePointer<Int8>!, _ __argv: UnsafePointer<UnsafeMutablePointer<Int8>?>!) -> Int32 ``` |

Modified execvP(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafePointer<UnsafeMutablePointer<Int8>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func execvP(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<UnsafeMutablePointer<Int8>>) -> Int32 ``` |
| To | ``` func execvP(_ __file: UnsafePointer<Int8>!, _ __searchpath: UnsafePointer<Int8>!, _ __argv: UnsafePointer<UnsafeMutablePointer<Int8>?>!) -> Int32 ``` |

Modified exit(_: Int32) -> Never

|  | Declaration |
| --- | --- |
| From | ``` @noreturn func exit(_ _: Int32) ``` |
| To | ``` func exit(_ _: Int32) -> Never ``` |

Modified exp(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func exp(_ x: Float) -> Float ``` |
| To | ``` func exp(_ x: Float) -> Float ``` |

Modified exp(_: Double) -> Double

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func exp(_ x: Double) -> Double ``` |
| To | ``` func exp(_ x: Double) -> Double ``` |

Modified exp2(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func exp2(_ x: Float) -> Float ``` |
| To | ``` func exp2(_ x: Float) -> Float ``` |

Modified exp2(_: Double) -> Double

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func exp2(_ x: Double) -> Double ``` |
| To | ``` func exp2(_ x: Double) -> Double ``` |

Modified expm1(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func expm1(_ x: Float) -> Float ``` |
| To | ``` func expm1(_ x: Float) -> Float ``` |

Modified faccessat(_: Int32, _: UnsafePointer<Int8>!, _: Int32, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func faccessat(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: Int32, _ _: Int32) -> Int32 ``` |
| To | ``` func faccessat(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: Int32, _ _: Int32) -> Int32 ``` |

Modified fchmodat(_: Int32, _: UnsafePointer<Int8>!, _: mode_t, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fchmodat(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: mode_t, _ _: Int32) -> Int32 ``` |
| To | ``` func fchmodat(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: mode_t, _ _: Int32) -> Int32 ``` |

Modified fchmodx_np(_: Int32, _: filesec_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fchmodx_np(_ _: Int32, _ _: filesec_t) -> Int32 ``` |
| To | ``` func fchmodx_np(_ _: Int32, _ _: filesec_t!) -> Int32 ``` |

Modified fchownat(_: Int32, _: UnsafePointer<Int8>!, _: uid_t, _: gid_t, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fchownat(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: uid_t, _ _: gid_t, _ _: Int32) -> Int32 ``` |
| To | ``` func fchownat(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: uid_t, _ _: gid_t, _ _: Int32) -> Int32 ``` |

Modified fclose(_: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fclose(_ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func fclose(_ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified fcntl(_: Int32, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fcntl(_ fd: CInt, _ cmd: CInt) -> CInt ``` |
| To | ``` func fcntl(_ fd: Int32, _ cmd: Int32) -> Int32 ``` |

Modified fcntl(_: Int32, _: Int32, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fcntl(_ fd: CInt, _ cmd: CInt, _ value: CInt) -> CInt ``` |
| To | ``` func fcntl(_ fd: Int32, _ cmd: Int32, _ value: Int32) -> Int32 ``` |

Modified fcopyfile(_: Int32, _: Int32, _: copyfile_state_t!, _: copyfile_flags_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fcopyfile(_ from_fd: Int32, _ to_fd: Int32, _ _: copyfile_state_t, _ flags: copyfile_flags_t) -> Int32 ``` |
| To | ``` func fcopyfile(_ from_fd: Int32, _ to_fd: Int32, _ _: copyfile_state_t!, _ flags: copyfile_flags_t) -> Int32 ``` |

Modified fcvt(_: Double, _: Int32, _: UnsafeMutablePointer<Int32>!, _: UnsafeMutablePointer<Int32>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func fcvt(_ _: Double, _ _: Int32, _ _: UnsafeMutablePointer<Int32>, _ _: UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func fcvt(_ _: Double, _ _: Int32, _ _: UnsafeMutablePointer<Int32>!, _ _: UnsafeMutablePointer<Int32>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified fdim(_: Float, _: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fdim(_ lhs: Float, _ rhs: Float) -> Float ``` |
| To | ``` func fdim(_ lhs: Float, _ rhs: Float) -> Float ``` |

Modified fdopen(_: Int32, _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<FILE>!

|  | Declaration |
| --- | --- |
| From | ``` func fdopen(_ _: Int32, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<FILE> ``` |
| To | ``` func fdopen(_ _: Int32, _ _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<FILE>! ``` |

Modified fdopendir(_: Int32) -> UnsafeMutablePointer<DIR>!

|  | Declaration |
| --- | --- |
| From | ``` func fdopendir(_ _: Int32) -> UnsafeMutablePointer<DIR> ``` |
| To | ``` func fdopendir(_ _: Int32) -> UnsafeMutablePointer<DIR>! ``` |

Modified fegetenv(_: UnsafeMutablePointer<fenv_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fegetenv(_ _: UnsafeMutablePointer<fenv_t>) -> Int32 ``` |
| To | ``` func fegetenv(_ _: UnsafeMutablePointer<fenv_t>!) -> Int32 ``` |

Modified fegetexceptflag(_: UnsafeMutablePointer<fexcept_t>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fegetexceptflag(_ _: UnsafeMutablePointer<fexcept_t>, _ _: Int32) -> Int32 ``` |
| To | ``` func fegetexceptflag(_ _: UnsafeMutablePointer<fexcept_t>!, _ _: Int32) -> Int32 ``` |

Modified feholdexcept(_: UnsafeMutablePointer<fenv_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func feholdexcept(_ _: UnsafeMutablePointer<fenv_t>) -> Int32 ``` |
| To | ``` func feholdexcept(_ _: UnsafeMutablePointer<fenv_t>!) -> Int32 ``` |

Modified feof(_: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func feof(_ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func feof(_ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified ferror(_: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ferror(_ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func ferror(_ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified fesetenv(_: UnsafePointer<fenv_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fesetenv(_ _: UnsafePointer<fenv_t>) -> Int32 ``` |
| To | ``` func fesetenv(_ _: UnsafePointer<fenv_t>!) -> Int32 ``` |

Modified fesetexceptflag(_: UnsafePointer<fexcept_t>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fesetexceptflag(_ _: UnsafePointer<fexcept_t>, _ _: Int32) -> Int32 ``` |
| To | ``` func fesetexceptflag(_ _: UnsafePointer<fexcept_t>!, _ _: Int32) -> Int32 ``` |

Modified feupdateenv(_: UnsafePointer<fenv_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func feupdateenv(_ _: UnsafePointer<fenv_t>) -> Int32 ``` |
| To | ``` func feupdateenv(_ _: UnsafePointer<fenv_t>!) -> Int32 ``` |

Modified fflagstostr(_: UInt) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func fflagstostr(_ _: UInt) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func fflagstostr(_ _: UInt) -> UnsafeMutablePointer<Int8>! ``` |

Modified fflush(_: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fflush(_ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func fflush(_ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified ffsctl(_: Int32, _: UInt, _: UnsafeMutableRawPointer!, _: UInt32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ffsctl(_ _: Int32, _ _: UInt, _ _: UnsafeMutablePointer<Void>, _ _: UInt32) -> Int32 ``` |
| To | ``` func ffsctl(_ _: Int32, _ _: UInt, _ _: UnsafeMutableRawPointer!, _ _: UInt32) -> Int32 ``` |

Modified fgetattrlist(_: Int32, _: UnsafeMutableRawPointer!, _: UnsafeMutableRawPointer!, _: Int, _: UInt32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fgetattrlist(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: UInt) -> Int32 ``` |
| To | ``` func fgetattrlist(_ _: Int32, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutableRawPointer!, _ _: Int, _ _: UInt32) -> Int32 ``` |

Modified fgetc(_: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fgetc(_ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func fgetc(_ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified fgetln(_: UnsafeMutablePointer<FILE>!, _: UnsafeMutablePointer<Int>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func fgetln(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<Int>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func fgetln(_ _: UnsafeMutablePointer<FILE>!, _ _: UnsafeMutablePointer<Int>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified fgetpos(_: UnsafeMutablePointer<FILE>!, _: UnsafeMutablePointer<fpos_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fgetpos(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<fpos_t>) -> Int32 ``` |
| To | ``` func fgetpos(_ _: UnsafeMutablePointer<FILE>!, _ _: UnsafeMutablePointer<fpos_t>!) -> Int32 ``` |

Modified fgets(_: UnsafeMutablePointer<Int8>!, _: Int32, _: UnsafeMutablePointer<FILE>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func fgets(_ _: UnsafeMutablePointer<Int8>, _ _: Int32, _ _: UnsafeMutablePointer<FILE>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func fgets(_ _: UnsafeMutablePointer<Int8>!, _ _: Int32, _ _: UnsafeMutablePointer<FILE>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified fgetwc(_: UnsafeMutablePointer<FILE>!) -> wint_t

|  | Declaration |
| --- | --- |
| From | ``` func fgetwc(_ _: UnsafeMutablePointer<FILE>) -> wint_t ``` |
| To | ``` func fgetwc(_ _: UnsafeMutablePointer<FILE>!) -> wint_t ``` |

Modified fgetwc_l(_: UnsafeMutablePointer<FILE>!, _: locale_t!) -> wint_t

|  | Declaration |
| --- | --- |
| From | ``` func fgetwc_l(_ _: UnsafeMutablePointer<FILE>, _ _: locale_t) -> wint_t ``` |
| To | ``` func fgetwc_l(_ _: UnsafeMutablePointer<FILE>!, _ _: locale_t!) -> wint_t ``` |

Modified fgetwln(_: UnsafeMutablePointer<FILE>!, _: UnsafeMutablePointer<Int>!) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func fgetwln(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<Int>) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func fgetwln(_ _: UnsafeMutablePointer<FILE>!, _ _: UnsafeMutablePointer<Int>!) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified fgetwln_l(_: UnsafeMutablePointer<FILE>!, _: UnsafeMutablePointer<Int>!, _: locale_t!) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func fgetwln_l(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<Int>, _ _: locale_t) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func fgetwln_l(_ _: UnsafeMutablePointer<FILE>!, _ _: UnsafeMutablePointer<Int>!, _ _: locale_t!) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified fgetws(_: UnsafeMutablePointer<wchar_t>!, _: Int32, _: UnsafeMutablePointer<FILE>!) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func fgetws(_ _: UnsafeMutablePointer<wchar_t>, _ _: Int32, _ _: UnsafeMutablePointer<FILE>) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func fgetws(_ _: UnsafeMutablePointer<wchar_t>!, _ _: Int32, _ _: UnsafeMutablePointer<FILE>!) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified fgetws_l(_: UnsafeMutablePointer<wchar_t>!, _: Int32, _: UnsafeMutablePointer<FILE>!, _: locale_t!) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func fgetws_l(_ _: UnsafeMutablePointer<wchar_t>, _ _: Int32, _ _: UnsafeMutablePointer<FILE>, _ _: locale_t) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func fgetws_l(_ _: UnsafeMutablePointer<wchar_t>!, _ _: Int32, _ _: UnsafeMutablePointer<FILE>!, _ _: locale_t!) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified fgetxattr(_: Int32, _: UnsafePointer<Int8>!, _: UnsafeMutableRawPointer!, _: Int, _: UInt32, _: Int32) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func fgetxattr(_ fd: Int32, _ name: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<Void>, _ size: Int, _ position: UInt32, _ options: Int32) -> Int ``` |
| To | ``` func fgetxattr(_ fd: Int32, _ name: UnsafePointer<Int8>!, _ value: UnsafeMutableRawPointer!, _ size: Int, _ position: UInt32, _ options: Int32) -> Int ``` |

Modified fhopen(_: UnsafePointer<fhandle>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fhopen(_ _: UnsafePointer<fhandle>, _ _: Int32) -> Int32 ``` |
| To | ``` func fhopen(_ _: UnsafePointer<fhandle>!, _ _: Int32) -> Int32 ``` |

Modified fileno(_: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fileno(_ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func fileno(_ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified filesec_dup(_: filesec_t!) -> filesec_t!

|  | Declaration |
| --- | --- |
| From | ``` func filesec_dup(_ _: filesec_t) -> filesec_t ``` |
| To | ``` func filesec_dup(_ _: filesec_t!) -> filesec_t! ``` |

Modified filesec_free(_: filesec_t!)

|  | Declaration |
| --- | --- |
| From | ``` func filesec_free(_ _: filesec_t) ``` |
| To | ``` func filesec_free(_ _: filesec_t!) ``` |

Modified filesec_get_property(_: filesec_t!, _: filesec_property_t, _: UnsafeMutableRawPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func filesec_get_property(_ _: filesec_t, _ _: filesec_property_t, _ _: UnsafeMutablePointer<Void>) -> Int32 ``` |
| To | ``` func filesec_get_property(_ _: filesec_t!, _ _: filesec_property_t, _ _: UnsafeMutableRawPointer!) -> Int32 ``` |

Modified filesec_init() -> filesec_t!

|  | Declaration |
| --- | --- |
| From | ``` func filesec_init() -> filesec_t ``` |
| To | ``` func filesec_init() -> filesec_t! ``` |

Modified filesec_query_property(_: filesec_t!, _: filesec_property_t, _: UnsafeMutablePointer<Int32>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func filesec_query_property(_ _: filesec_t, _ _: filesec_property_t, _ _: UnsafeMutablePointer<Int32>) -> Int32 ``` |
| To | ``` func filesec_query_property(_ _: filesec_t!, _ _: filesec_property_t, _ _: UnsafeMutablePointer<Int32>!) -> Int32 ``` |

Modified filesec_set_property(_: filesec_t!, _: filesec_property_t, _: UnsafeRawPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func filesec_set_property(_ _: filesec_t, _ _: filesec_property_t, _ _: UnsafePointer<Void>) -> Int32 ``` |
| To | ``` func filesec_set_property(_ _: filesec_t!, _ _: filesec_property_t, _ _: UnsafeRawPointer!) -> Int32 ``` |

Modified filesec_t

|  | Declaration |
| --- | --- |
| From | ``` typealias filesec_t = COpaquePointer ``` |
| To | ``` typealias filesec_t = OpaquePointer ``` |

Modified filesec_unset_property(_: filesec_t!, _: filesec_property_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func filesec_unset_property(_ _: filesec_t, _ _: filesec_property_t) -> Int32 ``` |
| To | ``` func filesec_unset_property(_ _: filesec_t!, _ _: filesec_property_t) -> Int32 ``` |

Modified flistxattr(_: Int32, _: UnsafeMutablePointer<Int8>!, _: Int, _: Int32) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func flistxattr(_ fd: Int32, _ namebuff: UnsafeMutablePointer<Int8>, _ size: Int, _ options: Int32) -> Int ``` |
| To | ``` func flistxattr(_ fd: Int32, _ namebuff: UnsafeMutablePointer<Int8>!, _ size: Int, _ options: Int32) -> Int ``` |

Modified flockfile(_: UnsafeMutablePointer<FILE>!)

|  | Declaration |
| --- | --- |
| From | ``` func flockfile(_ _: UnsafeMutablePointer<FILE>) ``` |
| To | ``` func flockfile(_ _: UnsafeMutablePointer<FILE>!) ``` |

Modified fmax(_: Float, _: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fmax(_ lhs: Float, _ rhs: Float) -> Float ``` |
| To | ``` func fmax(_ lhs: Float, _ rhs: Float) -> Float ``` |

Modified fmin(_: Float, _: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fmin(_ lhs: Float, _ rhs: Float) -> Float ``` |
| To | ``` func fmin(_ lhs: Float, _ rhs: Float) -> Float ``` |

Modified fmtcheck(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> UnsafePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func fmtcheck(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> UnsafePointer<Int8> ``` |
| To | ``` func fmtcheck(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!) -> UnsafePointer<Int8>! ``` |

Modified fmtmsg(_: Int, _: UnsafePointer<Int8>!, _: Int32, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fmtmsg(_ _: Int, _ _: UnsafePointer<Int8>, _ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func fmtmsg(_ _: Int, _ _: UnsafePointer<Int8>!, _ _: Int32, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified fnmatch(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fnmatch(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int32) -> Int32 ``` |
| To | ``` func fnmatch(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: Int32) -> Int32 ``` |

Modified fopen(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<FILE>!

|  | Declaration |
| --- | --- |
| From | ``` func fopen(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<FILE> ``` |
| To | ``` func fopen(_ __filename: UnsafePointer<Int8>!, _ __mode: UnsafePointer<Int8>!) -> UnsafeMutablePointer<FILE>! ``` |

Modified forkpty(_: UnsafeMutablePointer<Int32>!, _: UnsafeMutablePointer<Int8>!, _: UnsafeMutablePointer<termios>!, _: UnsafeMutablePointer<winsize>!) -> pid_t

|  | Declaration |
| --- | --- |
| From | ``` func forkpty(_ _: UnsafeMutablePointer<Int32>, _ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<termios>, _ _: UnsafeMutablePointer<winsize>) -> pid_t ``` |
| To | ``` func forkpty(_ _: UnsafeMutablePointer<Int32>!, _ _: UnsafeMutablePointer<Int8>!, _ _: UnsafeMutablePointer<termios>!, _ _: UnsafeMutablePointer<winsize>!) -> pid_t ``` |

Modified fparseln(_: UnsafeMutablePointer<FILE>!, _: UnsafeMutablePointer<Int>!, _: UnsafeMutablePointer<Int>!, _: UnsafePointer<Int8>!, _: Int32) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func fparseln(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<Int>, _ _: UnsafeMutablePointer<Int>, _ _: UnsafePointer<Int8>, _ _: Int32) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func fparseln(_ _: UnsafeMutablePointer<FILE>!, _ _: UnsafeMutablePointer<Int>!, _ _: UnsafeMutablePointer<Int>!, _ _: UnsafePointer<Int8>!, _ _: Int32) -> UnsafeMutablePointer<Int8>! ``` |

Modified fpclassify(_: Double) -> Int

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @warn_unused_result func fpclassify(_ x: Double) -> Int ``` | -- |
| To | ``` func fpclassify(_ value: Double) -> Int ``` | iOS 10.0 |

Modified fpclassify(_: Float) -> Int

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @warn_unused_result func fpclassify(_ x: Float) -> Int ``` | -- |
| To | ``` func fpclassify(_ value: Float) -> Int ``` | iOS 10.0 |

Modified fpurge(_: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fpurge(_ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func fpurge(_ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified fputc(_: Int32, _: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fputc(_ _: Int32, _ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func fputc(_ _: Int32, _ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified fputs(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fputs(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func fputs(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified fputwc(_: wchar_t, _: UnsafeMutablePointer<FILE>!) -> wint_t

|  | Declaration |
| --- | --- |
| From | ``` func fputwc(_ _: wchar_t, _ _: UnsafeMutablePointer<FILE>) -> wint_t ``` |
| To | ``` func fputwc(_ _: wchar_t, _ _: UnsafeMutablePointer<FILE>!) -> wint_t ``` |

Modified fputwc_l(_: wchar_t, _: UnsafeMutablePointer<FILE>!, _: locale_t!) -> wint_t

|  | Declaration |
| --- | --- |
| From | ``` func fputwc_l(_ _: wchar_t, _ _: UnsafeMutablePointer<FILE>, _ _: locale_t) -> wint_t ``` |
| To | ``` func fputwc_l(_ _: wchar_t, _ _: UnsafeMutablePointer<FILE>!, _ _: locale_t!) -> wint_t ``` |

Modified fputws(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fputws(_ _: UnsafePointer<wchar_t>, _ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func fputws(_ _: UnsafePointer<wchar_t>!, _ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified fputws_l(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<FILE>!, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fputws_l(_ _: UnsafePointer<wchar_t>, _ _: UnsafeMutablePointer<FILE>, _ _: locale_t) -> Int32 ``` |
| To | ``` func fputws_l(_ _: UnsafePointer<wchar_t>!, _ _: UnsafeMutablePointer<FILE>!, _ _: locale_t!) -> Int32 ``` |

Modified fread(_: UnsafeMutableRawPointer!, _: Int, _: Int, _: UnsafeMutablePointer<FILE>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func fread(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<FILE>) -> Int ``` |
| To | ``` func fread(_ __ptr: UnsafeMutableRawPointer!, _ __size: Int, _ __nitems: Int, _ __stream: UnsafeMutablePointer<FILE>!) -> Int ``` |

Modified free(_: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func free(_ _: UnsafeMutablePointer<Void>) ``` |
| To | ``` func free(_ _: UnsafeMutableRawPointer!) ``` |

Modified freeaddrinfo(_: UnsafeMutablePointer<addrinfo>!)

|  | Declaration |
| --- | --- |
| From | ``` func freeaddrinfo(_ _: UnsafeMutablePointer<addrinfo>) ``` |
| To | ``` func freeaddrinfo(_ _: UnsafeMutablePointer<addrinfo>!) ``` |

Modified freehostent(_: UnsafeMutablePointer<hostent>!)

|  | Declaration |
| --- | --- |
| From | ``` func freehostent(_ _: UnsafeMutablePointer<hostent>) ``` |
| To | ``` func freehostent(_ _: UnsafeMutablePointer<hostent>!) ``` |

Modified freelocale(_: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func freelocale(_ _: locale_t) -> Int32 ``` |
| To | ``` func freelocale(_ _: locale_t!) -> Int32 ``` |

Modified fremovexattr(_: Int32, _: UnsafePointer<Int8>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fremovexattr(_ fd: Int32, _ name: UnsafePointer<Int8>, _ options: Int32) -> Int32 ``` |
| To | ``` func fremovexattr(_ fd: Int32, _ name: UnsafePointer<Int8>!, _ options: Int32) -> Int32 ``` |

Modified freopen(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<FILE>!) -> UnsafeMutablePointer<FILE>!

|  | Declaration |
| --- | --- |
| From | ``` func freopen(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<FILE>) -> UnsafeMutablePointer<FILE> ``` |
| To | ``` func freopen(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<FILE>!) -> UnsafeMutablePointer<FILE>! ``` |

Modified frexp(_: Double) -> (Double, Int)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func frexp(_ value: Double) -> (Double, Int) ``` |
| To | ``` func frexp(_ value: Double) -> (Double, Int) ``` |

Modified frexp(_: Float) -> (Float, Int)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func frexp(_ value: Float) -> (Float, Int) ``` |
| To | ``` func frexp(_ value: Float) -> (Float, Int) ``` |

Modified frexp(_: Double, _: UnsafeMutablePointer<Int32>!) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func frexp(_ _: Double, _ _: UnsafeMutablePointer<Int32>) -> Double ``` |
| To | ``` func frexp(_ _: Double, _ _: UnsafeMutablePointer<Int32>!) -> Double ``` |

Modified frexpf(_: Float, _: UnsafeMutablePointer<Int32>!) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func frexpf(_ _: Float, _ _: UnsafeMutablePointer<Int32>) -> Float ``` |
| To | ``` func frexpf(_ _: Float, _ _: UnsafeMutablePointer<Int32>!) -> Float ``` |

Modified fsctl(_: UnsafePointer<Int8>!, _: UInt, _: UnsafeMutableRawPointer!, _: UInt32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fsctl(_ _: UnsafePointer<Int8>, _ _: UInt, _ _: UnsafeMutablePointer<Void>, _ _: UInt32) -> Int32 ``` |
| To | ``` func fsctl(_ _: UnsafePointer<Int8>!, _ _: UInt, _ _: UnsafeMutableRawPointer!, _ _: UInt32) -> Int32 ``` |

Modified fseek(_: UnsafeMutablePointer<FILE>!, _: Int, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fseek(_ _: UnsafeMutablePointer<FILE>, _ _: Int, _ _: Int32) -> Int32 ``` |
| To | ``` func fseek(_ _: UnsafeMutablePointer<FILE>!, _ _: Int, _ _: Int32) -> Int32 ``` |

Modified fseeko(_: UnsafeMutablePointer<FILE>!, _: off_t, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fseeko(_ _: UnsafeMutablePointer<FILE>, _ _: off_t, _ _: Int32) -> Int32 ``` |
| To | ``` func fseeko(_ __stream: UnsafeMutablePointer<FILE>!, _ __offset: off_t, _ __whence: Int32) -> Int32 ``` |

Modified fsetattrlist(_: Int32, _: UnsafeMutableRawPointer!, _: UnsafeMutableRawPointer!, _: Int, _: UInt32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fsetattrlist(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: UInt) -> Int32 ``` |
| To | ``` func fsetattrlist(_ _: Int32, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutableRawPointer!, _ _: Int, _ _: UInt32) -> Int32 ``` |

Modified fsetpos(_: UnsafeMutablePointer<FILE>!, _: UnsafePointer<fpos_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fsetpos(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafePointer<fpos_t>) -> Int32 ``` |
| To | ``` func fsetpos(_ _: UnsafeMutablePointer<FILE>!, _ _: UnsafePointer<fpos_t>!) -> Int32 ``` |

Modified fsetxattr(_: Int32, _: UnsafePointer<Int8>!, _: UnsafeRawPointer!, _: Int, _: UInt32, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fsetxattr(_ fd: Int32, _ name: UnsafePointer<Int8>, _ value: UnsafePointer<Void>, _ size: Int, _ position: UInt32, _ options: Int32) -> Int32 ``` |
| To | ``` func fsetxattr(_ fd: Int32, _ name: UnsafePointer<Int8>!, _ value: UnsafeRawPointer!, _ size: Int, _ position: UInt32, _ options: Int32) -> Int32 ``` |

Modified fstat(_: Int32, _: UnsafeMutablePointer<stat>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fstat(_ _: Int32, _ _: UnsafeMutablePointer<stat>) -> Int32 ``` |
| To | ``` func fstat(_ _: Int32, _ _: UnsafeMutablePointer<stat>!) -> Int32 ``` |

Modified fstatat(_: Int32, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<stat>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fstatat(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<stat>, _ _: Int32) -> Int32 ``` |
| To | ``` func fstatat(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<stat>!, _ _: Int32) -> Int32 ``` |

Modified fstatfs(_: Int32, _: UnsafeMutablePointer<statfs>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fstatfs(_ _: Int32, _ _: UnsafeMutablePointer<statfs>) -> Int32 ``` |
| To | ``` func fstatfs(_ _: Int32, _ _: UnsafeMutablePointer<statfs>!) -> Int32 ``` |

Modified fstatvfs(_: Int32, _: UnsafeMutablePointer<statvfs>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fstatvfs(_ _: Int32, _ _: UnsafeMutablePointer<statvfs>) -> Int32 ``` |
| To | ``` func fstatvfs(_ _: Int32, _ _: UnsafeMutablePointer<statvfs>!) -> Int32 ``` |

Modified fstatx_np(_: Int32, _: UnsafeMutablePointer<stat>!, _: filesec_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fstatx_np(_ _: Int32, _ _: UnsafeMutablePointer<stat>, _ _: filesec_t) -> Int32 ``` |
| To | ``` func fstatx_np(_ _: Int32, _ _: UnsafeMutablePointer<stat>!, _ _: filesec_t!) -> Int32 ``` |

Modified ftell(_: UnsafeMutablePointer<FILE>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func ftell(_ _: UnsafeMutablePointer<FILE>) -> Int ``` |
| To | ``` func ftell(_ _: UnsafeMutablePointer<FILE>!) -> Int ``` |

Modified ftello(_: UnsafeMutablePointer<FILE>!) -> off_t

|  | Declaration |
| --- | --- |
| From | ``` func ftello(_ _: UnsafeMutablePointer<FILE>) -> off_t ``` |
| To | ``` func ftello(_ __stream: UnsafeMutablePointer<FILE>!) -> off_t ``` |

Modified ftime(_: UnsafeMutablePointer<timeb>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ftime(_ _: UnsafeMutablePointer<timeb>) -> Int32 ``` |
| To | ``` func ftime(_ _: UnsafeMutablePointer<timeb>!) -> Int32 ``` |

Modified ftok(_: UnsafePointer<Int8>!, _: Int32) -> key_t

|  | Declaration |
| --- | --- |
| From | ``` func ftok(_ _: UnsafePointer<Int8>, _ _: Int32) -> key_t ``` |
| To | ``` func ftok(_ _: UnsafePointer<Int8>!, _ _: Int32) -> key_t ``` |

Modified ftrylockfile(_: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ftrylockfile(_ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func ftrylockfile(_ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified ftw(_: UnsafePointer<Int8>!, _: ( (UnsafePointer<Int8>?, UnsafePointer<stat>?, Int32) -> Int32)!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ftw(_ _: UnsafePointer<Int8>, _ _: ((UnsafePointer<Int8>, UnsafePointer<stat>, Int32) -> Int32)!, _ _: Int32) -> Int32 ``` |
| To | ``` func ftw(_ _: UnsafePointer<Int8>!, _ _: (@escaping (UnsafePointer<Int8>?, UnsafePointer<stat>?, Int32) -> Int32)!, _ _: Int32) -> Int32 ``` |

Modified funlockfile(_: UnsafeMutablePointer<FILE>!)

|  | Declaration |
| --- | --- |
| From | ``` func funlockfile(_ _: UnsafeMutablePointer<FILE>) ``` |
| To | ``` func funlockfile(_ _: UnsafeMutablePointer<FILE>!) ``` |

Modified funopen(_: UnsafeRawPointer!, _: ( (UnsafeMutableRawPointer?, UnsafeMutablePointer<Int8>?, Int32) -> Int32)?, _: ( (UnsafeMutableRawPointer?, UnsafePointer<Int8>?, Int32) -> Int32)?, _: ( (UnsafeMutableRawPointer?, fpos_t, Int32) -> fpos_t)?, _: ( (UnsafeMutableRawPointer?) -> Int32)?) -> UnsafeMutablePointer<FILE>!

|  | Declaration |
| --- | --- |
| From | ``` func funopen(_ _: UnsafePointer<Void>, _ _: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int8>, Int32) -> Int32)!, _ _: ((UnsafeMutablePointer<Void>, UnsafePointer<Int8>, Int32) -> Int32)!, _ _: ((UnsafeMutablePointer<Void>, fpos_t, Int32) -> fpos_t)!, _ _: ((UnsafeMutablePointer<Void>) -> Int32)!) -> UnsafeMutablePointer<FILE> ``` |
| To | ``` func funopen(_ _: UnsafeRawPointer!, _ _: (@escaping (UnsafeMutableRawPointer?, UnsafeMutablePointer<Int8>?, Int32) -> Int32)?, _ _: (@escaping (UnsafeMutableRawPointer?, UnsafePointer<Int8>?, Int32) -> Int32)?, _ _: (@escaping (UnsafeMutableRawPointer?, fpos_t, Int32) -> fpos_t)?, _ _: (@escaping (UnsafeMutableRawPointer?) -> Int32)?) -> UnsafeMutablePointer<FILE>! ``` |

Modified futimes(_: Int32, _: UnsafePointer<timeval>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func futimes(_ _: Int32, _ _: UnsafePointer<timeval>) -> Int32 ``` |
| To | ``` func futimes(_ _: Int32, _ _: UnsafePointer<timeval>!) -> Int32 ``` |

Modified fwide(_: UnsafeMutablePointer<FILE>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fwide(_ _: UnsafeMutablePointer<FILE>, _ _: Int32) -> Int32 ``` |
| To | ``` func fwide(_ _: UnsafeMutablePointer<FILE>!, _ _: Int32) -> Int32 ``` |

Modified fwrite(_: UnsafeRawPointer!, _: Int, _: Int, _: UnsafeMutablePointer<FILE>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func fwrite(_ _: UnsafePointer<Void>, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<FILE>) -> Int ``` |
| To | ``` func fwrite(_ __ptr: UnsafeRawPointer!, _ __size: Int, _ __nitems: Int, _ __stream: UnsafeMutablePointer<FILE>!) -> Int ``` |

Modified gai_strerror(_: Int32) -> UnsafePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func gai_strerror(_ _: Int32) -> UnsafePointer<Int8> ``` |
| To | ``` func gai_strerror(_ _: Int32) -> UnsafePointer<Int8>! ``` |

Modified gcvt(_: Double, _: Int32, _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func gcvt(_ _: Double, _ _: Int32, _ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func gcvt(_ _: Double, _ _: Int32, _ _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified get_dp_control_port(_: host_priv_t, _: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func get_dp_control_port(_ host: host_priv_t, _ contorl_port: UnsafeMutablePointer<mach_port_t>) -> kern_return_t ``` |
| To | ``` func get_dp_control_port(_ host: host_priv_t, _ contorl_port: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t ``` |

Modified getaddrinfo(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafePointer<addrinfo>!, _: UnsafeMutablePointer<UnsafeMutablePointer<addrinfo>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getaddrinfo(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<addrinfo>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<addrinfo>>) -> Int32 ``` |
| To | ``` func getaddrinfo(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<addrinfo>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<addrinfo>?>!) -> Int32 ``` |

Modified getattrlist(_: UnsafePointer<Int8>!, _: UnsafeMutableRawPointer!, _: UnsafeMutableRawPointer!, _: Int, _: UInt32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getattrlist(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: UInt) -> Int32 ``` |
| To | ``` func getattrlist(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutableRawPointer!, _ _: Int, _ _: UInt32) -> Int32 ``` |

Modified getattrlistat(_: Int32, _: UnsafePointer<Int8>!, _: UnsafeMutableRawPointer!, _: UnsafeMutableRawPointer!, _: Int, _: UInt) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getattrlistat(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: UInt) -> Int32 ``` |
| To | ``` func getattrlistat(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutableRawPointer!, _ _: Int, _ _: UInt) -> Int32 ``` |

Modified getattrlistbulk(_: Int32, _: UnsafeMutableRawPointer!, _: UnsafeMutableRawPointer!, _: Int, _: UInt64) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getattrlistbulk(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: UInt64) -> Int32 ``` |
| To | ``` func getattrlistbulk(_ _: Int32, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutableRawPointer!, _ _: Int, _ _: UInt64) -> Int32 ``` |

Modified getaudit_addr(_: UnsafeMutablePointer<auditinfo_addr>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getaudit_addr(_ _: UnsafeMutablePointer<auditinfo_addr>, _ _: Int32) -> Int32 ``` |
| To | ``` func getaudit_addr(_ _: UnsafeMutablePointer<auditinfo_addr>!, _ _: Int32) -> Int32 ``` |

Modified getauid(_: UnsafeMutablePointer<au_id_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getauid(_ _: UnsafeMutablePointer<au_id_t>) -> Int32 ``` |
| To | ``` func getauid(_ _: UnsafeMutablePointer<au_id_t>!) -> Int32 ``` |

Modified getbsize(_: UnsafeMutablePointer<Int32>!, _: UnsafeMutablePointer<Int>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func getbsize(_ _: UnsafeMutablePointer<Int32>, _ _: UnsafeMutablePointer<Int>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func getbsize(_ _: UnsafeMutablePointer<Int32>!, _ _: UnsafeMutablePointer<Int>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified getc(_: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getc(_ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func getc(_ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified getc_unlocked(_: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getc_unlocked(_ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func getc_unlocked(_ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified getcwd(_: UnsafeMutablePointer<Int8>!, _: Int) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func getcwd(_ _: UnsafeMutablePointer<Int8>, _ _: Int) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func getcwd(_ _: UnsafeMutablePointer<Int8>!, _ _: Int) -> UnsafeMutablePointer<Int8>! ``` |

Modified getdate(_: UnsafePointer<Int8>!) -> UnsafeMutablePointer<tm>!

|  | Declaration |
| --- | --- |
| From | ``` func getdate(_ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<tm> ``` |
| To | ``` func getdate(_ _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<tm>! ``` |

Modified getdelim(_: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafeMutablePointer<Int>!, _: Int32, _: UnsafeMutablePointer<FILE>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func getdelim(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<Int>, _ _: Int32, _ _: UnsafeMutablePointer<FILE>) -> Int ``` |
| To | ``` func getdelim(_ __linep: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ __linecapp: UnsafeMutablePointer<Int>!, _ __delimiter: Int32, _ __stream: UnsafeMutablePointer<FILE>!) -> Int ``` |

Modified getdirentries(_: Int32, _: UnsafeMutablePointer<Int8>!, _: Int32, _: UnsafeMutablePointer<Int>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getdirentries(_ _: Int32, _ _: UnsafeMutablePointer<Int8>, _ _: Int32, _ _: UnsafeMutablePointer<Int>) -> Int32 ``` |
| To | ``` func getdirentries(_ _: Int32, _ _: UnsafeMutablePointer<Int8>!, _ _: Int32, _ _: UnsafeMutablePointer<Int>!) -> Int32 ``` |

Modified getdirentriesattr(_: Int32, _: UnsafeMutableRawPointer!, _: UnsafeMutableRawPointer!, _: Int, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt32>!, _: UInt32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getdirentriesattr(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: UnsafeMutablePointer<UInt>, _ _: UnsafeMutablePointer<UInt>, _ _: UnsafeMutablePointer<UInt>, _ _: UInt) -> Int32 ``` |
| To | ``` func getdirentriesattr(_ _: Int32, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutableRawPointer!, _ _: Int, _ _: UnsafeMutablePointer<UInt32>!, _ _: UnsafeMutablePointer<UInt32>!, _ _: UnsafeMutablePointer<UInt32>!, _ _: UInt32) -> Int32 ``` |

Modified getdomainname(_: UnsafeMutablePointer<Int8>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getdomainname(_ _: UnsafeMutablePointer<Int8>, _ _: Int32) -> Int32 ``` |
| To | ``` func getdomainname(_ _: UnsafeMutablePointer<Int8>!, _ _: Int32) -> Int32 ``` |

Modified getenv(_: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func getenv(_ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func getenv(_ _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified getfh(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<fhandle_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getfh(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<fhandle_t>) -> Int32 ``` |
| To | ``` func getfh(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<fhandle_t>!) -> Int32 ``` |

Modified getfsstat(_: UnsafeMutablePointer<statfs>!, _: Int32, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getfsstat(_ _: UnsafeMutablePointer<statfs>, _ _: Int32, _ _: Int32) -> Int32 ``` |
| To | ``` func getfsstat(_ _: UnsafeMutablePointer<statfs>!, _ _: Int32, _ _: Int32) -> Int32 ``` |

Modified getgrent() -> UnsafeMutablePointer<group>!

|  | Declaration |
| --- | --- |
| From | ``` func getgrent() -> UnsafeMutablePointer<group> ``` |
| To | ``` func getgrent() -> UnsafeMutablePointer<group>! ``` |

Modified getgrgid(_: gid_t) -> UnsafeMutablePointer<group>!

|  | Declaration |
| --- | --- |
| From | ``` func getgrgid(_ _: gid_t) -> UnsafeMutablePointer<group> ``` |
| To | ``` func getgrgid(_ _: gid_t) -> UnsafeMutablePointer<group>! ``` |

Modified getgrgid_r(_: gid_t, _: UnsafeMutablePointer<group>!, _: UnsafeMutablePointer<Int8>!, _: Int, _: UnsafeMutablePointer<UnsafeMutablePointer<group>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getgrgid_r(_ _: gid_t, _ _: UnsafeMutablePointer<group>, _ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<group>>) -> Int32 ``` |
| To | ``` func getgrgid_r(_ _: gid_t, _ _: UnsafeMutablePointer<group>!, _ _: UnsafeMutablePointer<Int8>!, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<group>?>!) -> Int32 ``` |

Modified getgrnam(_: UnsafePointer<Int8>!) -> UnsafeMutablePointer<group>!

|  | Declaration |
| --- | --- |
| From | ``` func getgrnam(_ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<group> ``` |
| To | ``` func getgrnam(_ _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<group>! ``` |

Modified getgrnam_r(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<group>!, _: UnsafeMutablePointer<Int8>!, _: Int, _: UnsafeMutablePointer<UnsafeMutablePointer<group>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getgrnam_r(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<group>, _ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<group>>) -> Int32 ``` |
| To | ``` func getgrnam_r(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<group>!, _ _: UnsafeMutablePointer<Int8>!, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<group>?>!) -> Int32 ``` |

Modified getgrouplist(_: UnsafePointer<Int8>!, _: Int32, _: UnsafeMutablePointer<Int32>!, _: UnsafeMutablePointer<Int32>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getgrouplist(_ _: UnsafePointer<Int8>, _ _: Int32, _ _: UnsafeMutablePointer<Int32>, _ _: UnsafeMutablePointer<Int32>) -> Int32 ``` |
| To | ``` func getgrouplist(_ _: UnsafePointer<Int8>!, _ _: Int32, _ _: UnsafeMutablePointer<Int32>!, _ _: UnsafeMutablePointer<Int32>!) -> Int32 ``` |

Modified getgroups(_: Int32, _: UnsafeMutablePointer<gid_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getgroups(_ _: Int32, _ _: UnsafeMutablePointer<gid_t>) -> Int32 ``` |
| To | ``` func getgroups(_ _: Int32, _ _: UnsafeMutablePointer<gid_t>!) -> Int32 ``` |

Modified getgruuid(_: UnsafeMutablePointer<UInt8>!) -> UnsafeMutablePointer<group>!

|  | Declaration |
| --- | --- |
| From | ``` func getgruuid(_ _: UnsafeMutablePointer<UInt8>) -> UnsafeMutablePointer<group> ``` |
| To | ``` func getgruuid(_ _: UnsafeMutablePointer<UInt8>!) -> UnsafeMutablePointer<group>! ``` |

Modified getgruuid_r(_: UnsafeMutablePointer<UInt8>!, _: UnsafeMutablePointer<group>!, _: UnsafeMutablePointer<Int8>!, _: Int, _: UnsafeMutablePointer<UnsafeMutablePointer<group>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getgruuid_r(_ _: UnsafeMutablePointer<UInt8>, _ _: UnsafeMutablePointer<group>, _ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<group>>) -> Int32 ``` |
| To | ``` func getgruuid_r(_ _: UnsafeMutablePointer<UInt8>!, _ _: UnsafeMutablePointer<group>!, _ _: UnsafeMutablePointer<Int8>!, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<group>?>!) -> Int32 ``` |

Modified gethostbyaddr(_: UnsafeRawPointer!, _: socklen_t, _: Int32) -> UnsafeMutablePointer<hostent>!

|  | Declaration |
| --- | --- |
| From | ``` func gethostbyaddr(_ _: UnsafePointer<Void>, _ _: socklen_t, _ _: Int32) -> UnsafeMutablePointer<hostent> ``` |
| To | ``` func gethostbyaddr(_ _: UnsafeRawPointer!, _ _: socklen_t, _ _: Int32) -> UnsafeMutablePointer<hostent>! ``` |

Modified gethostbyname(_: UnsafePointer<Int8>!) -> UnsafeMutablePointer<hostent>!

|  | Declaration |
| --- | --- |
| From | ``` func gethostbyname(_ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<hostent> ``` |
| To | ``` func gethostbyname(_ _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<hostent>! ``` |

Modified gethostbyname2(_: UnsafePointer<Int8>!, _: Int32) -> UnsafeMutablePointer<hostent>!

|  | Declaration |
| --- | --- |
| From | ``` func gethostbyname2(_ _: UnsafePointer<Int8>, _ _: Int32) -> UnsafeMutablePointer<hostent> ``` |
| To | ``` func gethostbyname2(_ _: UnsafePointer<Int8>!, _ _: Int32) -> UnsafeMutablePointer<hostent>! ``` |

Modified gethostent() -> UnsafeMutablePointer<hostent>!

|  | Declaration |
| --- | --- |
| From | ``` func gethostent() -> UnsafeMutablePointer<hostent> ``` |
| To | ``` func gethostent() -> UnsafeMutablePointer<hostent>! ``` |

Modified gethostname(_: UnsafeMutablePointer<Int8>!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func gethostname(_ _: UnsafeMutablePointer<Int8>, _ _: Int) -> Int32 ``` |
| To | ``` func gethostname(_ _: UnsafeMutablePointer<Int8>!, _ _: Int) -> Int32 ``` |

Modified getipnodebyaddr(_: UnsafeRawPointer!, _: Int, _: Int32, _: UnsafeMutablePointer<Int32>!) -> UnsafeMutablePointer<hostent>!

|  | Declaration |
| --- | --- |
| From | ``` func getipnodebyaddr(_ _: UnsafePointer<Void>, _ _: Int, _ _: Int32, _ _: UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<hostent> ``` |
| To | ``` func getipnodebyaddr(_ _: UnsafeRawPointer!, _ _: Int, _ _: Int32, _ _: UnsafeMutablePointer<Int32>!) -> UnsafeMutablePointer<hostent>! ``` |

Modified getipnodebyname(_: UnsafePointer<Int8>!, _: Int32, _: Int32, _: UnsafeMutablePointer<Int32>!) -> UnsafeMutablePointer<hostent>!

|  | Declaration |
| --- | --- |
| From | ``` func getipnodebyname(_ _: UnsafePointer<Int8>, _ _: Int32, _ _: Int32, _ _: UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<hostent> ``` |
| To | ``` func getipnodebyname(_ _: UnsafePointer<Int8>!, _ _: Int32, _ _: Int32, _ _: UnsafeMutablePointer<Int32>!) -> UnsafeMutablePointer<hostent>! ``` |

Modified getipv4sourcefilter(_: Int32, _: in_addr, _: in_addr, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<in_addr>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getipv4sourcefilter(_ _: Int32, _ _: in_addr, _ _: in_addr, _ _: UnsafeMutablePointer<UInt32>, _ _: UnsafeMutablePointer<UInt32>, _ _: UnsafeMutablePointer<in_addr>) -> Int32 ``` |
| To | ``` func getipv4sourcefilter(_ _: Int32, _ _: in_addr, _ _: in_addr, _ _: UnsafeMutablePointer<UInt32>!, _ _: UnsafeMutablePointer<UInt32>!, _ _: UnsafeMutablePointer<in_addr>!) -> Int32 ``` |

Modified getitimer(_: Int32, _: UnsafeMutablePointer<itimerval>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getitimer(_ _: Int32, _ _: UnsafeMutablePointer<itimerval>) -> Int32 ``` |
| To | ``` func getitimer(_ _: Int32, _ _: UnsafeMutablePointer<itimerval>!) -> Int32 ``` |

Modified getlastlogx(_: uid_t, _: UnsafeMutablePointer<lastlogx>!) -> UnsafeMutablePointer<lastlogx>!

|  | Declaration |
| --- | --- |
| From | ``` func getlastlogx(_ _: uid_t, _ _: UnsafeMutablePointer<lastlogx>) -> UnsafeMutablePointer<lastlogx> ``` |
| To | ``` func getlastlogx(_ _: uid_t, _ _: UnsafeMutablePointer<lastlogx>!) -> UnsafeMutablePointer<lastlogx>! ``` |

Modified getlastlogxbyname(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<lastlogx>!) -> UnsafeMutablePointer<lastlogx>!

|  | Declaration |
| --- | --- |
| From | ``` func getlastlogxbyname(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<lastlogx>) -> UnsafeMutablePointer<lastlogx> ``` |
| To | ``` func getlastlogxbyname(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<lastlogx>!) -> UnsafeMutablePointer<lastlogx>! ``` |

Modified getline(_: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafeMutablePointer<Int>!, _: UnsafeMutablePointer<FILE>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func getline(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<Int>, _ _: UnsafeMutablePointer<FILE>) -> Int ``` |
| To | ``` func getline(_ __linep: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ __linecapp: UnsafeMutablePointer<Int>!, _ __stream: UnsafeMutablePointer<FILE>!) -> Int ``` |

Modified getloadavg(_: UnsafeMutablePointer<Double>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getloadavg(_ _: UnsafeMutablePointer<Double>, _ _: Int32) -> Int32 ``` |
| To | ``` func getloadavg(_ _: UnsafeMutablePointer<Double>!, _ _: Int32) -> Int32 ``` |

Modified getlogin() -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func getlogin() -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func getlogin() -> UnsafeMutablePointer<Int8>! ``` |

Modified getlogin_r(_: UnsafeMutablePointer<Int8>!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getlogin_r(_ _: UnsafeMutablePointer<Int8>, _ _: Int) -> Int32 ``` |
| To | ``` func getlogin_r(_ _: UnsafeMutablePointer<Int8>!, _ _: Int) -> Int32 ``` |

Modified getmntinfo(_: UnsafeMutablePointer<UnsafeMutablePointer<statfs>?>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getmntinfo(_ _: UnsafeMutablePointer<UnsafeMutablePointer<statfs>>, _ _: Int32) -> Int32 ``` |
| To | ``` func getmntinfo(_ _: UnsafeMutablePointer<UnsafeMutablePointer<statfs>?>!, _ _: Int32) -> Int32 ``` |

Modified getmode(_: UnsafeRawPointer!, _: mode_t) -> mode_t

|  | Declaration |
| --- | --- |
| From | ``` func getmode(_ _: UnsafePointer<Void>, _ _: mode_t) -> mode_t ``` |
| To | ``` func getmode(_ _: UnsafeRawPointer!, _ _: mode_t) -> mode_t ``` |

Modified getnameinfo(_: UnsafePointer<sockaddr>!, _: socklen_t, _: UnsafeMutablePointer<Int8>!, _: socklen_t, _: UnsafeMutablePointer<Int8>!, _: socklen_t, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getnameinfo(_ _: UnsafePointer<sockaddr>, _ _: socklen_t, _ _: UnsafeMutablePointer<Int8>, _ _: socklen_t, _ _: UnsafeMutablePointer<Int8>, _ _: socklen_t, _ _: Int32) -> Int32 ``` |
| To | ``` func getnameinfo(_ _: UnsafePointer<sockaddr>!, _ _: socklen_t, _ _: UnsafeMutablePointer<Int8>!, _ _: socklen_t, _ _: UnsafeMutablePointer<Int8>!, _ _: socklen_t, _ _: Int32) -> Int32 ``` |

Modified getnetbyaddr(_: UInt32, _: Int32) -> UnsafeMutablePointer<netent>!

|  | Declaration |
| --- | --- |
| From | ``` func getnetbyaddr(_ _: UInt32, _ _: Int32) -> UnsafeMutablePointer<netent> ``` |
| To | ``` func getnetbyaddr(_ _: UInt32, _ _: Int32) -> UnsafeMutablePointer<netent>! ``` |

Modified getnetbyname(_: UnsafePointer<Int8>!) -> UnsafeMutablePointer<netent>!

|  | Declaration |
| --- | --- |
| From | ``` func getnetbyname(_ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<netent> ``` |
| To | ``` func getnetbyname(_ _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<netent>! ``` |

Modified getnetent() -> UnsafeMutablePointer<netent>!

|  | Declaration |
| --- | --- |
| From | ``` func getnetent() -> UnsafeMutablePointer<netent> ``` |
| To | ``` func getnetent() -> UnsafeMutablePointer<netent>! ``` |

Modified getnetgrent(_: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getnetgrent(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int32 ``` |
| To | ``` func getnetgrent(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Int32 ``` |

Modified getopt(_: Int32, _: UnsafePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getopt(_ _: Int32, _ _: UnsafePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func getopt(_ _: Int32, _ _: UnsafePointer<UnsafeMutablePointer<Int8>?>!, _ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified getopt_long(_: Int32, _: UnsafePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafePointer<Int8>!, _: UnsafePointer<option>!, _: UnsafeMutablePointer<Int32>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getopt_long(_ _: Int32, _ _: UnsafePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<option>, _ _: UnsafeMutablePointer<Int32>) -> Int32 ``` |
| To | ``` func getopt_long(_ _: Int32, _ _: UnsafePointer<UnsafeMutablePointer<Int8>?>!, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<option>!, _ _: UnsafeMutablePointer<Int32>!) -> Int32 ``` |

Modified getopt_long_only(_: Int32, _: UnsafePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafePointer<Int8>!, _: UnsafePointer<option>!, _: UnsafeMutablePointer<Int32>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getopt_long_only(_ _: Int32, _ _: UnsafePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<option>, _ _: UnsafeMutablePointer<Int32>) -> Int32 ``` |
| To | ``` func getopt_long_only(_ _: Int32, _ _: UnsafePointer<UnsafeMutablePointer<Int8>?>!, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<option>!, _ _: UnsafeMutablePointer<Int32>!) -> Int32 ``` |

Modified getpass(_: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func getpass(_ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func getpass(_ _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified getpeereid(_: Int32, _: UnsafeMutablePointer<uid_t>!, _: UnsafeMutablePointer<gid_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getpeereid(_ _: Int32, _ _: UnsafeMutablePointer<uid_t>, _ _: UnsafeMutablePointer<gid_t>) -> Int32 ``` |
| To | ``` func getpeereid(_ _: Int32, _ _: UnsafeMutablePointer<uid_t>!, _ _: UnsafeMutablePointer<gid_t>!) -> Int32 ``` |

Modified getpeername(_: Int32, _: UnsafeMutablePointer<sockaddr>!, _: UnsafeMutablePointer<socklen_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getpeername(_ _: Int32, _ _: UnsafeMutablePointer<sockaddr>, _ _: UnsafeMutablePointer<socklen_t>) -> Int32 ``` |
| To | ``` func getpeername(_ _: Int32, _ _: UnsafeMutablePointer<sockaddr>!, _ _: UnsafeMutablePointer<socklen_t>!) -> Int32 ``` |

Modified getprogname() -> UnsafePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func getprogname() -> UnsafePointer<Int8> ``` |
| To | ``` func getprogname() -> UnsafePointer<Int8>! ``` |

Modified getprotobyname(_: UnsafePointer<Int8>!) -> UnsafeMutablePointer<protoent>!

|  | Declaration |
| --- | --- |
| From | ``` func getprotobyname(_ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<protoent> ``` |
| To | ``` func getprotobyname(_ _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<protoent>! ``` |

Modified getprotobynumber(_: Int32) -> UnsafeMutablePointer<protoent>!

|  | Declaration |
| --- | --- |
| From | ``` func getprotobynumber(_ _: Int32) -> UnsafeMutablePointer<protoent> ``` |
| To | ``` func getprotobynumber(_ _: Int32) -> UnsafeMutablePointer<protoent>! ``` |

Modified getprotoent() -> UnsafeMutablePointer<protoent>!

|  | Declaration |
| --- | --- |
| From | ``` func getprotoent() -> UnsafeMutablePointer<protoent> ``` |
| To | ``` func getprotoent() -> UnsafeMutablePointer<protoent>! ``` |

Modified getpwent() -> UnsafeMutablePointer<passwd>!

|  | Declaration |
| --- | --- |
| From | ``` func getpwent() -> UnsafeMutablePointer<passwd> ``` |
| To | ``` func getpwent() -> UnsafeMutablePointer<passwd>! ``` |

Modified getpwnam(_: UnsafePointer<Int8>!) -> UnsafeMutablePointer<passwd>!

|  | Declaration |
| --- | --- |
| From | ``` func getpwnam(_ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<passwd> ``` |
| To | ``` func getpwnam(_ _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<passwd>! ``` |

Modified getpwnam_r(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<passwd>!, _: UnsafeMutablePointer<Int8>!, _: Int, _: UnsafeMutablePointer<UnsafeMutablePointer<passwd>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getpwnam_r(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<passwd>, _ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<passwd>>) -> Int32 ``` |
| To | ``` func getpwnam_r(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<passwd>!, _ _: UnsafeMutablePointer<Int8>!, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<passwd>?>!) -> Int32 ``` |

Modified getpwuid(_: uid_t) -> UnsafeMutablePointer<passwd>!

|  | Declaration |
| --- | --- |
| From | ``` func getpwuid(_ _: uid_t) -> UnsafeMutablePointer<passwd> ``` |
| To | ``` func getpwuid(_ _: uid_t) -> UnsafeMutablePointer<passwd>! ``` |

Modified getpwuid_r(_: uid_t, _: UnsafeMutablePointer<passwd>!, _: UnsafeMutablePointer<Int8>!, _: Int, _: UnsafeMutablePointer<UnsafeMutablePointer<passwd>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getpwuid_r(_ _: uid_t, _ _: UnsafeMutablePointer<passwd>, _ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<passwd>>) -> Int32 ``` |
| To | ``` func getpwuid_r(_ _: uid_t, _ _: UnsafeMutablePointer<passwd>!, _ _: UnsafeMutablePointer<Int8>!, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<passwd>?>!) -> Int32 ``` |

Modified getpwuuid(_: UnsafeMutablePointer<UInt8>!) -> UnsafeMutablePointer<passwd>!

|  | Declaration |
| --- | --- |
| From | ``` func getpwuuid(_ _: UnsafeMutablePointer<UInt8>) -> UnsafeMutablePointer<passwd> ``` |
| To | ``` func getpwuuid(_ _: UnsafeMutablePointer<UInt8>!) -> UnsafeMutablePointer<passwd>! ``` |

Modified getpwuuid_r(_: UnsafeMutablePointer<UInt8>!, _: UnsafeMutablePointer<passwd>!, _: UnsafeMutablePointer<Int8>!, _: Int, _: UnsafeMutablePointer<UnsafeMutablePointer<passwd>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getpwuuid_r(_ _: UnsafeMutablePointer<UInt8>, _ _: UnsafeMutablePointer<passwd>, _ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<passwd>>) -> Int32 ``` |
| To | ``` func getpwuuid_r(_ _: UnsafeMutablePointer<UInt8>!, _ _: UnsafeMutablePointer<passwd>!, _ _: UnsafeMutablePointer<Int8>!, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<passwd>?>!) -> Int32 ``` |

Modified getrlimit(_: Int32, _: UnsafeMutablePointer<rlimit>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getrlimit(_ _: Int32, _ _: UnsafeMutablePointer<rlimit>) -> Int32 ``` |
| To | ``` func getrlimit(_ _: Int32, _ _: UnsafeMutablePointer<rlimit>!) -> Int32 ``` |

Modified getrpcbyname(_: UnsafePointer<Int8>!) -> UnsafeMutablePointer<rpcent>!

|  | Declaration |
| --- | --- |
| From | ``` func getrpcbyname(_ name: UnsafePointer<Int8>) -> UnsafeMutablePointer<rpcent> ``` |
| To | ``` func getrpcbyname(_ name: UnsafePointer<Int8>!) -> UnsafeMutablePointer<rpcent>! ``` |

Modified getrpcbynumber(_: Int32) -> UnsafeMutablePointer<rpcent>!

|  | Declaration |
| --- | --- |
| From | ``` func getrpcbynumber(_ number: Int) -> UnsafeMutablePointer<rpcent> ``` |
| To | ``` func getrpcbynumber(_ number: Int32) -> UnsafeMutablePointer<rpcent>! ``` |

Modified getrpcent() -> UnsafeMutablePointer<rpcent>!

|  | Declaration |
| --- | --- |
| From | ``` func getrpcent() -> UnsafeMutablePointer<rpcent> ``` |
| To | ``` func getrpcent() -> UnsafeMutablePointer<rpcent>! ``` |

Modified getrusage(_: Int32, _: UnsafeMutablePointer<rusage>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getrusage(_ _: Int32, _ _: UnsafeMutablePointer<rusage>) -> Int32 ``` |
| To | ``` func getrusage(_ _: Int32, _ _: UnsafeMutablePointer<rusage>!) -> Int32 ``` |

Modified gets(_: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func gets(_ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func gets(_ _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified getservbyname(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<servent>!

|  | Declaration |
| --- | --- |
| From | ``` func getservbyname(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<servent> ``` |
| To | ``` func getservbyname(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<servent>! ``` |

Modified getservbyport(_: Int32, _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<servent>!

|  | Declaration |
| --- | --- |
| From | ``` func getservbyport(_ _: Int32, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<servent> ``` |
| To | ``` func getservbyport(_ _: Int32, _ _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<servent>! ``` |

Modified getservent() -> UnsafeMutablePointer<servent>!

|  | Declaration |
| --- | --- |
| From | ``` func getservent() -> UnsafeMutablePointer<servent> ``` |
| To | ``` func getservent() -> UnsafeMutablePointer<servent>! ``` |

Modified getsgroups_np(_: UnsafeMutablePointer<Int32>!, _: UnsafeMutablePointer<UInt8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getsgroups_np(_ _: UnsafeMutablePointer<Int32>, _ _: UnsafeMutablePointer<UInt8>) -> Int32 ``` |
| To | ``` func getsgroups_np(_ _: UnsafeMutablePointer<Int32>!, _ _: UnsafeMutablePointer<UInt8>!) -> Int32 ``` |

Modified getsockname(_: Int32, _: UnsafeMutablePointer<sockaddr>!, _: UnsafeMutablePointer<socklen_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getsockname(_ _: Int32, _ _: UnsafeMutablePointer<sockaddr>, _ _: UnsafeMutablePointer<socklen_t>) -> Int32 ``` |
| To | ``` func getsockname(_ _: Int32, _ _: UnsafeMutablePointer<sockaddr>!, _ _: UnsafeMutablePointer<socklen_t>!) -> Int32 ``` |

Modified getsockopt(_: Int32, _: Int32, _: Int32, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<socklen_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getsockopt(_ _: Int32, _ _: Int32, _ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<socklen_t>) -> Int32 ``` |
| To | ``` func getsockopt(_ _: Int32, _ _: Int32, _ _: Int32, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<socklen_t>!) -> Int32 ``` |

Modified getsourcefilter(_: Int32, _: UInt32, _: UnsafeMutablePointer<sockaddr>!, _: socklen_t, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<sockaddr_storage>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getsourcefilter(_ _: Int32, _ _: UInt32, _ _: UnsafeMutablePointer<sockaddr>, _ _: socklen_t, _ _: UnsafeMutablePointer<UInt32>, _ _: UnsafeMutablePointer<UInt32>, _ _: UnsafeMutablePointer<sockaddr_storage>) -> Int32 ``` |
| To | ``` func getsourcefilter(_ _: Int32, _ _: UInt32, _ _: UnsafeMutablePointer<sockaddr>!, _ _: socklen_t, _ _: UnsafeMutablePointer<UInt32>!, _ _: UnsafeMutablePointer<UInt32>!, _ _: UnsafeMutablePointer<sockaddr_storage>!) -> Int32 ``` |

Modified getsubopt(_: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getsubopt(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int32 ``` |
| To | ``` func getsubopt(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: UnsafePointer<UnsafeMutablePointer<Int8>?>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Int32 ``` |

Modified gettimeofday(_: UnsafeMutablePointer<timeval>!, _: UnsafeMutableRawPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func gettimeofday(_ _: UnsafeMutablePointer<timeval>, _ _: UnsafeMutablePointer<Void>) -> Int32 ``` |
| To | ``` func gettimeofday(_ _: UnsafeMutablePointer<timeval>!, _ _: UnsafeMutableRawPointer!) -> Int32 ``` |

Modified getusershell() -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func getusershell() -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func getusershell() -> UnsafeMutablePointer<Int8>! ``` |

Modified getutxent() -> UnsafeMutablePointer<utmpx>!

|  | Declaration |
| --- | --- |
| From | ``` func getutxent() -> UnsafeMutablePointer<utmpx> ``` |
| To | ``` func getutxent() -> UnsafeMutablePointer<utmpx>! ``` |

Modified getutxent_wtmp() -> UnsafeMutablePointer<utmpx>!

|  | Declaration |
| --- | --- |
| From | ``` func getutxent_wtmp() -> UnsafeMutablePointer<utmpx> ``` |
| To | ``` func getutxent_wtmp() -> UnsafeMutablePointer<utmpx>! ``` |

Modified getutxid(_: UnsafePointer<utmpx>!) -> UnsafeMutablePointer<utmpx>!

|  | Declaration |
| --- | --- |
| From | ``` func getutxid(_ _: UnsafePointer<utmpx>) -> UnsafeMutablePointer<utmpx> ``` |
| To | ``` func getutxid(_ _: UnsafePointer<utmpx>!) -> UnsafeMutablePointer<utmpx>! ``` |

Modified getutxline(_: UnsafePointer<utmpx>!) -> UnsafeMutablePointer<utmpx>!

|  | Declaration |
| --- | --- |
| From | ``` func getutxline(_ _: UnsafePointer<utmpx>) -> UnsafeMutablePointer<utmpx> ``` |
| To | ``` func getutxline(_ _: UnsafePointer<utmpx>!) -> UnsafeMutablePointer<utmpx>! ``` |

Modified getvfsbyname(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<vfsconf>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getvfsbyname(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<vfsconf>) -> Int32 ``` |
| To | ``` func getvfsbyname(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<vfsconf>!) -> Int32 ``` |

Modified getw(_: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getw(_ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func getw(_ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified getwc(_: UnsafeMutablePointer<FILE>!) -> wint_t

|  | Declaration |
| --- | --- |
| From | ``` func getwc(_ _: UnsafeMutablePointer<FILE>) -> wint_t ``` |
| To | ``` func getwc(_ _: UnsafeMutablePointer<FILE>!) -> wint_t ``` |

Modified getwc_l(_: UnsafeMutablePointer<FILE>!, _: locale_t!) -> wint_t

|  | Declaration |
| --- | --- |
| From | ``` func getwc_l(_ _: UnsafeMutablePointer<FILE>, _ _: locale_t) -> wint_t ``` |
| To | ``` func getwc_l(_ _: UnsafeMutablePointer<FILE>!, _ _: locale_t!) -> wint_t ``` |

Modified getwchar_l(_: locale_t!) -> wint_t

|  | Declaration |
| --- | --- |
| From | ``` func getwchar_l(_ _: locale_t) -> wint_t ``` |
| To | ``` func getwchar_l(_ _: locale_t!) -> wint_t ``` |

Modified getwd(_: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func getwd(_ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func getwd(_ _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified getwgroups_np(_: UnsafeMutablePointer<Int32>!, _: UnsafeMutablePointer<UInt8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getwgroups_np(_ _: UnsafeMutablePointer<Int32>, _ _: UnsafeMutablePointer<UInt8>) -> Int32 ``` |
| To | ``` func getwgroups_np(_ _: UnsafeMutablePointer<Int32>!, _ _: UnsafeMutablePointer<UInt8>!) -> Int32 ``` |

Modified getxattr(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafeMutableRawPointer!, _: Int, _: UInt32, _: Int32) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func getxattr(_ path: UnsafePointer<Int8>, _ name: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<Void>, _ size: Int, _ position: UInt32, _ options: Int32) -> Int ``` |
| To | ``` func getxattr(_ path: UnsafePointer<Int8>!, _ name: UnsafePointer<Int8>!, _ value: UnsafeMutableRawPointer!, _ size: Int, _ position: UInt32, _ options: Int32) -> Int ``` |

Modified glob(_: UnsafePointer<Int8>!, _: Int32, _: ( (UnsafePointer<Int8>?, Int32) -> Int32)!, _: UnsafeMutablePointer<glob_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func glob(_ _: UnsafePointer<Int8>, _ _: Int32, _ _: ((UnsafePointer<Int8>, Int32) -> Int32)!, _ _: UnsafeMutablePointer<glob_t>) -> Int32 ``` |
| To | ``` func glob(_ _: UnsafePointer<Int8>!, _ _: Int32, _ _: (@escaping (UnsafePointer<Int8>?, Int32) -> Int32)!, _ _: UnsafeMutablePointer<glob_t>!) -> Int32 ``` |

Modified glob_b(_: UnsafePointer<Int8>!, _: Int32, _: ( (UnsafePointer<Int8>?, Int32) -> Int32)!, _: UnsafeMutablePointer<glob_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func glob_b(_ _: UnsafePointer<Int8>, _ _: Int32, _ _: ((UnsafePointer<Int8>, Int32) -> Int32)!, _ _: UnsafeMutablePointer<glob_t>) -> Int32 ``` |
| To | ``` func glob_b(_ _: UnsafePointer<Int8>!, _ _: Int32, _ _: (@escaping (UnsafePointer<Int8>?, Int32) -> Int32)!, _ _: UnsafeMutablePointer<glob_t>!) -> Int32 ``` |

Modified globfree(_: UnsafeMutablePointer<glob_t>!)

|  | Declaration |
| --- | --- |
| From | ``` func globfree(_ _: UnsafeMutablePointer<glob_t>) ``` |
| To | ``` func globfree(_ _: UnsafeMutablePointer<glob_t>!) ``` |

Modified gmtime(_: UnsafePointer<time_t>!) -> UnsafeMutablePointer<tm>!

|  | Declaration |
| --- | --- |
| From | ``` func gmtime(_ _: UnsafePointer<time_t>) -> UnsafeMutablePointer<tm> ``` |
| To | ``` func gmtime(_ _: UnsafePointer<time_t>!) -> UnsafeMutablePointer<tm>! ``` |

Modified gmtime_r(_: UnsafePointer<time_t>!, _: UnsafeMutablePointer<tm>!) -> UnsafeMutablePointer<tm>!

|  | Declaration |
| --- | --- |
| From | ``` func gmtime_r(_ _: UnsafePointer<time_t>, _ _: UnsafeMutablePointer<tm>) -> UnsafeMutablePointer<tm> ``` |
| To | ``` func gmtime_r(_ _: UnsafePointer<time_t>!, _ _: UnsafeMutablePointer<tm>!) -> UnsafeMutablePointer<tm>! ``` |

Modified group_from_gid(_: gid_t, _: Int32) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func group_from_gid(_ _: gid_t, _ _: Int32) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func group_from_gid(_ _: gid_t, _ _: Int32) -> UnsafeMutablePointer<Int8>! ``` |

Modified heapsort(_: UnsafeMutableRawPointer!, _: Int, _: Int, _: (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func heapsort(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> Int32 ``` |
| To | ``` func heapsort(_ __base: UnsafeMutableRawPointer!, _ __nel: Int, _ __width: Int, _ __compar: @escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) -> Int32 ``` |

Modified heapsort_b(_: UnsafeMutableRawPointer!, _: Int, _: Int, _: (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func heapsort_b(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> Int32 ``` |
| To | ``` func heapsort_b(_ __base: UnsafeMutableRawPointer!, _ __nel: Int, _ __width: Int, _ __compar: @escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) -> Int32 ``` |

Modified herror(_: UnsafePointer<Int8>!)

|  | Declaration |
| --- | --- |
| From | ``` func herror(_ _: UnsafePointer<Int8>) ``` |
| To | ``` func herror(_ _: UnsafePointer<Int8>!) ``` |

Modified host_check_multiuser_mode(_: host_t, _: UnsafeMutablePointer<UInt32>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_check_multiuser_mode(_ host: host_t, _ multiuser_mode: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` |
| To | ``` func host_check_multiuser_mode(_ host: host_t, _ multiuser_mode: UnsafeMutablePointer<UInt32>!) -> kern_return_t ``` |

Modified host_create_mach_voucher(_: host_t, _: mach_voucher_attr_raw_recipe_array_t!, _: mach_msg_type_number_t, _: UnsafeMutablePointer<ipc_voucher_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_create_mach_voucher(_ host: host_t, _ recipes: mach_voucher_attr_raw_recipe_array_t, _ recipesCnt: mach_msg_type_number_t, _ voucher: UnsafeMutablePointer<ipc_voucher_t>) -> kern_return_t ``` |
| To | ``` func host_create_mach_voucher(_ host: host_t, _ recipes: mach_voucher_attr_raw_recipe_array_t!, _ recipesCnt: mach_msg_type_number_t, _ voucher: UnsafeMutablePointer<ipc_voucher_t>!) -> kern_return_t ``` |

Modified host_default_memory_manager(_: host_priv_t, _: UnsafeMutablePointer<memory_object_default_t>!, _: memory_object_cluster_size_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_default_memory_manager(_ host_priv: host_priv_t, _ default_manager: UnsafeMutablePointer<memory_object_default_t>, _ cluster_size: memory_object_cluster_size_t) -> kern_return_t ``` |
| To | ``` func host_default_memory_manager(_ host_priv: host_priv_t, _ default_manager: UnsafeMutablePointer<memory_object_default_t>!, _ cluster_size: memory_object_cluster_size_t) -> kern_return_t ``` |

Modified host_get_atm_diagnostic_flag(_: host_t, _: UnsafeMutablePointer<UInt32>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_get_atm_diagnostic_flag(_ host: host_t, _ diagnostic_flag: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` |
| To | ``` func host_get_atm_diagnostic_flag(_ host: host_t, _ diagnostic_flag: UnsafeMutablePointer<UInt32>!) -> kern_return_t ``` |

Modified host_get_boot_info(_: host_priv_t, _: UnsafeMutablePointer<Int8>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_get_boot_info(_ host_priv: host_priv_t, _ boot_info: UnsafeMutablePointer<Int8>) -> kern_return_t ``` |
| To | ``` func host_get_boot_info(_ host_priv: host_priv_t, _ boot_info: UnsafeMutablePointer<Int8>!) -> kern_return_t ``` |

Modified host_get_clock_control(_: host_priv_t, _: clock_id_t, _: UnsafeMutablePointer<clock_ctrl_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_get_clock_control(_ host_priv: host_priv_t, _ clock_id: clock_id_t, _ clock_ctrl: UnsafeMutablePointer<clock_ctrl_t>) -> kern_return_t ``` |
| To | ``` func host_get_clock_control(_ host_priv: host_priv_t, _ clock_id: clock_id_t, _ clock_ctrl: UnsafeMutablePointer<clock_ctrl_t>!) -> kern_return_t ``` |

Modified host_get_clock_service(_: host_t, _: clock_id_t, _: UnsafeMutablePointer<clock_serv_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_get_clock_service(_ host: host_t, _ clock_id: clock_id_t, _ clock_serv: UnsafeMutablePointer<clock_serv_t>) -> kern_return_t ``` |
| To | ``` func host_get_clock_service(_ host: host_t, _ clock_id: clock_id_t, _ clock_serv: UnsafeMutablePointer<clock_serv_t>!) -> kern_return_t ``` |

Modified host_get_exception_ports(_: host_priv_t, _: exception_mask_t, _: exception_mask_array_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: exception_handler_array_t!, _: exception_behavior_array_t!, _: exception_flavor_array_t!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_get_exception_ports(_ host_priv: host_priv_t, _ exception_mask: exception_mask_t, _ masks: exception_mask_array_t, _ masksCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ old_handlers: exception_handler_array_t, _ old_behaviors: exception_behavior_array_t, _ old_flavors: exception_flavor_array_t) -> kern_return_t ``` |
| To | ``` func host_get_exception_ports(_ host_priv: host_priv_t, _ exception_mask: exception_mask_t, _ masks: exception_mask_array_t!, _ masksCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ old_handlers: exception_handler_array_t!, _ old_behaviors: exception_behavior_array_t!, _ old_flavors: exception_flavor_array_t!) -> kern_return_t ``` |

Modified host_get_io_master(_: host_t, _: UnsafeMutablePointer<io_master_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_get_io_master(_ host: host_t, _ io_master: UnsafeMutablePointer<io_master_t>) -> kern_return_t ``` |
| To | ``` func host_get_io_master(_ host: host_t, _ io_master: UnsafeMutablePointer<io_master_t>!) -> kern_return_t ``` |

Modified host_get_multiuser_config_flags(_: host_t, _: UnsafeMutablePointer<UInt32>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_get_multiuser_config_flags(_ host: host_t, _ multiuser_flags: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` |
| To | ``` func host_get_multiuser_config_flags(_ host: host_t, _ multiuser_flags: UnsafeMutablePointer<UInt32>!) -> kern_return_t ``` |

Modified host_get_special_port(_: host_priv_t, _: Int32, _: Int32, _: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_get_special_port(_ host_priv: host_priv_t, _ node: Int32, _ which: Int32, _ port: UnsafeMutablePointer<mach_port_t>) -> kern_return_t ``` |
| To | ``` func host_get_special_port(_ host_priv: host_priv_t, _ node: Int32, _ which: Int32, _ port: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t ``` |

Modified host_get_UNDServer(_: host_priv_t, _: UnsafeMutablePointer<UNDServerRef>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_get_UNDServer(_ host: host_priv_t, _ server: UnsafeMutablePointer<UNDServerRef>) -> kern_return_t ``` |
| To | ``` func host_get_UNDServer(_ host: host_priv_t, _ server: UnsafeMutablePointer<UNDServerRef>!) -> kern_return_t ``` |

Modified host_info(_: host_t, _: host_flavor_t, _: host_info_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_info(_ host: host_t, _ flavor: host_flavor_t, _ host_info_out: host_info_t, _ host_info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func host_info(_ host: host_t, _ flavor: host_flavor_t, _ host_info_out: host_info_t!, _ host_info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified host_kernel_version(_: host_t, _: UnsafeMutablePointer<Int8>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_kernel_version(_ host: host_t, _ kernel_version: UnsafeMutablePointer<Int8>) -> kern_return_t ``` |
| To | ``` func host_kernel_version(_ host: host_t, _ kernel_version: UnsafeMutablePointer<Int8>!) -> kern_return_t ``` |

Modified host_lockgroup_info(_: host_t, _: UnsafeMutablePointer<lockgroup_info_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_lockgroup_info(_ host: host_t, _ lockgroup_info: UnsafeMutablePointer<lockgroup_info_array_t>, _ lockgroup_infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func host_lockgroup_info(_ host: host_t, _ lockgroup_info: UnsafeMutablePointer<lockgroup_info_array_t?>!, _ lockgroup_infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified host_page_size(_: host_t, _: UnsafeMutablePointer<vm_size_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_page_size(_ _: host_t, _ _: UnsafeMutablePointer<vm_size_t>) -> kern_return_t ``` |
| To | ``` func host_page_size(_ _: host_t, _ _: UnsafeMutablePointer<vm_size_t>!) -> kern_return_t ``` |

Modified host_priv_statistics(_: host_priv_t, _: host_flavor_t, _: host_info_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_priv_statistics(_ host_priv: host_priv_t, _ flavor: host_flavor_t, _ host_info_out: host_info_t, _ host_info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func host_priv_statistics(_ host_priv: host_priv_t, _ flavor: host_flavor_t, _ host_info_out: host_info_t!, _ host_info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified host_processor_info(_: host_t, _: processor_flavor_t, _: UnsafeMutablePointer<natural_t>!, _: UnsafeMutablePointer<processor_info_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_processor_info(_ host: host_t, _ flavor: processor_flavor_t, _ out_processor_count: UnsafeMutablePointer<natural_t>, _ out_processor_info: UnsafeMutablePointer<processor_info_array_t>, _ out_processor_infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func host_processor_info(_ host: host_t, _ flavor: processor_flavor_t, _ out_processor_count: UnsafeMutablePointer<natural_t>!, _ out_processor_info: UnsafeMutablePointer<processor_info_array_t?>!, _ out_processor_infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified host_processor_set_priv(_: host_priv_t, _: processor_set_name_t, _: UnsafeMutablePointer<processor_set_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_processor_set_priv(_ host_priv: host_priv_t, _ set_name: processor_set_name_t, _ set: UnsafeMutablePointer<processor_set_t>) -> kern_return_t ``` |
| To | ``` func host_processor_set_priv(_ host_priv: host_priv_t, _ set_name: processor_set_name_t, _ set: UnsafeMutablePointer<processor_set_t>!) -> kern_return_t ``` |

Modified host_processor_sets(_: host_priv_t, _: UnsafeMutablePointer<processor_set_name_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_processor_sets(_ host_priv: host_priv_t, _ processor_sets: UnsafeMutablePointer<processor_set_name_array_t>, _ processor_setsCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func host_processor_sets(_ host_priv: host_priv_t, _ processor_sets: UnsafeMutablePointer<processor_set_name_array_t?>!, _ processor_setsCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified host_processors(_: host_priv_t, _: UnsafeMutablePointer<processor_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_processors(_ host_priv: host_priv_t, _ out_processor_list: UnsafeMutablePointer<processor_array_t>, _ out_processor_listCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func host_processors(_ host_priv: host_priv_t, _ out_processor_list: UnsafeMutablePointer<processor_array_t?>!, _ out_processor_listCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified host_register_mach_voucher_attr_manager(_: host_t, _: mach_voucher_attr_manager_t, _: mach_voucher_attr_value_handle_t, _: UnsafeMutablePointer<mach_voucher_attr_key_t>!, _: UnsafeMutablePointer<ipc_voucher_attr_control_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_register_mach_voucher_attr_manager(_ host: host_t, _ attr_manager: mach_voucher_attr_manager_t, _ default_value: mach_voucher_attr_value_handle_t, _ new_key: UnsafeMutablePointer<mach_voucher_attr_key_t>, _ new_attr_control: UnsafeMutablePointer<ipc_voucher_attr_control_t>) -> kern_return_t ``` |
| To | ``` func host_register_mach_voucher_attr_manager(_ host: host_t, _ attr_manager: mach_voucher_attr_manager_t, _ default_value: mach_voucher_attr_value_handle_t, _ new_key: UnsafeMutablePointer<mach_voucher_attr_key_t>!, _ new_attr_control: UnsafeMutablePointer<ipc_voucher_attr_control_t>!) -> kern_return_t ``` |

Modified host_register_well_known_mach_voucher_attr_manager(_: host_t, _: mach_voucher_attr_manager_t, _: mach_voucher_attr_value_handle_t, _: mach_voucher_attr_key_t, _: UnsafeMutablePointer<ipc_voucher_attr_control_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_register_well_known_mach_voucher_attr_manager(_ host: host_t, _ attr_manager: mach_voucher_attr_manager_t, _ default_value: mach_voucher_attr_value_handle_t, _ key: mach_voucher_attr_key_t, _ new_attr_control: UnsafeMutablePointer<ipc_voucher_attr_control_t>) -> kern_return_t ``` |
| To | ``` func host_register_well_known_mach_voucher_attr_manager(_ host: host_t, _ attr_manager: mach_voucher_attr_manager_t, _ default_value: mach_voucher_attr_value_handle_t, _ key: mach_voucher_attr_key_t, _ new_attr_control: UnsafeMutablePointer<ipc_voucher_attr_control_t>!) -> kern_return_t ``` |

Modified host_security_create_task_token(_: host_security_t, _: task_t, _: security_token_t, _: audit_token_t, _: host_t, _: ledger_array_t!, _: mach_msg_type_number_t, _: boolean_t, _: UnsafeMutablePointer<task_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_security_create_task_token(_ host_security: host_security_t, _ parent_task: task_t, _ sec_token: security_token_t, _ audit_token: audit_token_t, _ host: host_t, _ ledgers: ledger_array_t, _ ledgersCnt: mach_msg_type_number_t, _ inherit_memory: boolean_t, _ child_task: UnsafeMutablePointer<task_t>) -> kern_return_t ``` |
| To | ``` func host_security_create_task_token(_ host_security: host_security_t, _ parent_task: task_t, _ sec_token: security_token_t, _ audit_token: audit_token_t, _ host: host_t, _ ledgers: ledger_array_t!, _ ledgersCnt: mach_msg_type_number_t, _ inherit_memory: boolean_t, _ child_task: UnsafeMutablePointer<task_t>!) -> kern_return_t ``` |

Modified host_statistics(_: host_t, _: host_flavor_t, _: host_info_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_statistics(_ host_priv: host_t, _ flavor: host_flavor_t, _ host_info_out: host_info_t, _ host_info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func host_statistics(_ host_priv: host_t, _ flavor: host_flavor_t, _ host_info_out: host_info_t!, _ host_info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified host_statistics64(_: host_t, _: host_flavor_t, _: host_info64_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_statistics64(_ host_priv: host_t, _ flavor: host_flavor_t, _ host_info64_out: host_info64_t, _ host_info64_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func host_statistics64(_ host_priv: host_t, _ flavor: host_flavor_t, _ host_info64_out: host_info64_t!, _ host_info64_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified host_swap_exception_ports(_: host_priv_t, _: exception_mask_t, _: mach_port_t, _: exception_behavior_t, _: thread_state_flavor_t, _: exception_mask_array_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: exception_handler_array_t!, _: exception_behavior_array_t!, _: exception_flavor_array_t!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_swap_exception_ports(_ host_priv: host_priv_t, _ exception_mask: exception_mask_t, _ new_port: mach_port_t, _ behavior: exception_behavior_t, _ new_flavor: thread_state_flavor_t, _ masks: exception_mask_array_t, _ masksCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ old_handlerss: exception_handler_array_t, _ old_behaviors: exception_behavior_array_t, _ old_flavors: exception_flavor_array_t) -> kern_return_t ``` |
| To | ``` func host_swap_exception_ports(_ host_priv: host_priv_t, _ exception_mask: exception_mask_t, _ new_port: mach_port_t, _ behavior: exception_behavior_t, _ new_flavor: thread_state_flavor_t, _ masks: exception_mask_array_t!, _ masksCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ old_handlerss: exception_handler_array_t!, _ old_behaviors: exception_behavior_array_t!, _ old_flavors: exception_flavor_array_t!) -> kern_return_t ``` |

Modified host_virtual_physical_table_info(_: host_t, _: UnsafeMutablePointer<hash_info_bucket_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_virtual_physical_table_info(_ host: host_t, _ info: UnsafeMutablePointer<hash_info_bucket_array_t>, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func host_virtual_physical_table_info(_ host: host_t, _ info: UnsafeMutablePointer<hash_info_bucket_array_t?>!, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified host_zone_info(_: host_priv_t, _: UnsafeMutablePointer<zone_name_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: UnsafeMutablePointer<zone_info_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func host_zone_info(_ host: host_priv_t, _ names: UnsafeMutablePointer<zone_name_array_t>, _ namesCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ info: UnsafeMutablePointer<zone_info_array_t>, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func host_zone_info(_ host: host_priv_t, _ names: UnsafeMutablePointer<zone_name_array_t?>!, _ namesCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ info: UnsafeMutablePointer<zone_info_array_t?>!, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified hsearch(_: ENTRY, _: ACTION) -> UnsafeMutablePointer<ENTRY>!

|  | Declaration |
| --- | --- |
| From | ``` func hsearch(_ _: ENTRY, _ _: ACTION) -> UnsafeMutablePointer<ENTRY> ``` |
| To | ``` func hsearch(_ _: ENTRY, _ _: ACTION) -> UnsafeMutablePointer<ENTRY>! ``` |

Modified hstrerror(_: Int32) -> UnsafePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func hstrerror(_ _: Int32) -> UnsafePointer<Int8> ``` |
| To | ``` func hstrerror(_ _: Int32) -> UnsafePointer<Int8>! ``` |

Modified hypot(_: Float, _: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func hypot(_ lhs: Float, _ rhs: Float) -> Float ``` |
| To | ``` func hypot(_ lhs: Float, _ rhs: Float) -> Float ``` |

Modified iconv(_: iconv_t!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafeMutablePointer<Int>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafeMutablePointer<Int>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func iconv(_ _: iconv_t, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<Int>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<Int>) -> Int ``` |
| To | ``` func iconv(_ _: iconv_t!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: UnsafeMutablePointer<Int>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: UnsafeMutablePointer<Int>!) -> Int ``` |

Modified iconv_canonicalize(_: UnsafePointer<Int8>!) -> UnsafePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func iconv_canonicalize(_ name: UnsafePointer<Int8>) -> UnsafePointer<Int8> ``` |
| To | ``` func iconv_canonicalize(_ name: UnsafePointer<Int8>!) -> UnsafePointer<Int8>! ``` |

Modified iconv_close(_: iconv_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iconv_close(_ _: iconv_t) -> Int32 ``` |
| To | ``` func iconv_close(_ _: iconv_t!) -> Int32 ``` |

Modified iconv_open(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> iconv_t!

|  | Declaration |
| --- | --- |
| From | ``` func iconv_open(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> iconv_t ``` |
| To | ``` func iconv_open(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!) -> iconv_t! ``` |

Modified iconv_t

|  | Declaration |
| --- | --- |
| From | ``` typealias iconv_t = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias iconv_t = UnsafeMutableRawPointer ``` |

Modified iconv_unicode_char_hook

|  | Declaration |
| --- | --- |
| From | ``` typealias iconv_unicode_char_hook = (UInt32, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias iconv_unicode_char_hook = (UInt32, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified iconv_unicode_mb_to_uc_fallback

|  | Declaration |
| --- | --- |
| From | ``` typealias iconv_unicode_mb_to_uc_fallback = (UnsafePointer<Int8>, Int, ((UnsafePointer<UInt32>, Int, UnsafeMutablePointer<Void>) -> Void)!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias iconv_unicode_mb_to_uc_fallback = (UnsafePointer<Int8>?, Int, (@escaping (UnsafePointer<UInt32>?, Int, UnsafeMutableRawPointer?) -> Swift.Void)?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified iconv_unicode_uc_to_mb_fallback

|  | Declaration |
| --- | --- |
| From | ``` typealias iconv_unicode_uc_to_mb_fallback = (UInt32, ((UnsafePointer<Int8>, Int, UnsafeMutablePointer<Void>) -> Void)!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias iconv_unicode_uc_to_mb_fallback = (UInt32, (@escaping (UnsafePointer<Int8>?, Int, UnsafeMutableRawPointer?) -> Swift.Void)?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified iconv_wchar_mb_to_wc_fallback

|  | Declaration |
| --- | --- |
| From | ``` typealias iconv_wchar_mb_to_wc_fallback = (UnsafePointer<Int8>, Int, ((UnsafePointer<wchar_t>, Int, UnsafeMutablePointer<Void>) -> Void)!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias iconv_wchar_mb_to_wc_fallback = (UnsafePointer<Int8>?, Int, (@escaping (UnsafePointer<wchar_t>?, Int, UnsafeMutableRawPointer?) -> Swift.Void)?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified iconv_wchar_wc_to_mb_fallback

|  | Declaration |
| --- | --- |
| From | ``` typealias iconv_wchar_wc_to_mb_fallback = (wchar_t, ((UnsafePointer<Int8>, Int, UnsafeMutablePointer<Void>) -> Void)!, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias iconv_wchar_wc_to_mb_fallback = (wchar_t, (@escaping (UnsafePointer<Int8>?, Int, UnsafeMutableRawPointer?) -> Swift.Void)?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified iconv_wide_char_hook

|  | Declaration |
| --- | --- |
| From | ``` typealias iconv_wide_char_hook = (wchar_t, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias iconv_wide_char_hook = (wchar_t, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified iconvctl(_: iconv_t!, _: Int32, _: UnsafeMutableRawPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iconvctl(_ _: iconv_t, _ _: Int32, _ _: UnsafeMutablePointer<Void>) -> Int32 ``` |
| To | ``` func iconvctl(_ _: iconv_t!, _ _: Int32, _ _: UnsafeMutableRawPointer!) -> Int32 ``` |

Modified iconvlist(_: ( (UInt32, UnsafePointer<UnsafePointer<Int8>?>?, UnsafeMutableRawPointer?) -> Int32)!, _: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func iconvlist(_ _: ((UInt32, UnsafePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Void>) -> Int32)!, _ _: UnsafeMutablePointer<Void>) ``` |
| To | ``` func iconvlist(_ _: (@escaping (UInt32, UnsafePointer<UnsafePointer<Int8>?>?, UnsafeMutableRawPointer?) -> Int32)!, _ _: UnsafeMutableRawPointer!) ``` |

Modified if_freenameindex(_: UnsafeMutablePointer<if_nameindex>!)

|  | Declaration |
| --- | --- |
| From | ``` func if_freenameindex(_ _: UnsafeMutablePointer<if_nameindex>) ``` |
| To | ``` func if_freenameindex(_ _: UnsafeMutablePointer<if_nameindex>!) ``` |

Modified if_indextoname(_: UInt32, _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func if_indextoname(_ _: UInt32, _ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func if_indextoname(_ _: UInt32, _ _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified if_nameindex() -> UnsafeMutablePointer<if_nameindex>!

|  | Declaration |
| --- | --- |
| From | ``` func if_nameindex() -> UnsafeMutablePointer<if_nameindex> ``` |
| To | ``` func if_nameindex() -> UnsafeMutablePointer<if_nameindex>! ``` |

Modified if_nametoindex(_: UnsafePointer<Int8>!) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func if_nametoindex(_ _: UnsafePointer<Int8>) -> UInt32 ``` |
| To | ``` func if_nametoindex(_ _: UnsafePointer<Int8>!) -> UInt32 ``` |

Modified ilogb(_: Float) -> Int

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ilogb(_ x: Float) -> Int ``` |
| To | ``` func ilogb(_ x: Float) -> Int ``` |

Modified ilogb(_: Double) -> Int

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ilogb(_ x: Double) -> Int ``` |
| To | ``` func ilogb(_ x: Double) -> Int ``` |

Modified index(_: UnsafePointer<Int8>!, _: Int32) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func index(_ _: UnsafePointer<Int8>, _ _: Int32) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func index(_ _: UnsafePointer<Int8>!, _ _: Int32) -> UnsafeMutablePointer<Int8>! ``` |

Modified inet6_opt_append(_: UnsafeMutableRawPointer!, _: socklen_t, _: Int32, _: __uint8_t, _: socklen_t, _: __uint8_t, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_opt_append(_ _: UnsafeMutablePointer<Void>, _ _: socklen_t, _ _: Int32, _ _: __uint8_t, _ _: socklen_t, _ _: __uint8_t, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int32 ``` |
| To | ``` func inet6_opt_append(_ _: UnsafeMutableRawPointer!, _ _: socklen_t, _ _: Int32, _ _: __uint8_t, _ _: socklen_t, _ _: __uint8_t, _ _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> Int32 ``` |

Modified inet6_opt_find(_: UnsafeMutableRawPointer!, _: socklen_t, _: Int32, _: __uint8_t, _: UnsafeMutablePointer<socklen_t>!, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_opt_find(_ _: UnsafeMutablePointer<Void>, _ _: socklen_t, _ _: Int32, _ _: __uint8_t, _ _: UnsafeMutablePointer<socklen_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int32 ``` |
| To | ``` func inet6_opt_find(_ _: UnsafeMutableRawPointer!, _ _: socklen_t, _ _: Int32, _ _: __uint8_t, _ _: UnsafeMutablePointer<socklen_t>!, _ _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> Int32 ``` |

Modified inet6_opt_finish(_: UnsafeMutableRawPointer!, _: socklen_t, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_opt_finish(_ _: UnsafeMutablePointer<Void>, _ _: socklen_t, _ _: Int32) -> Int32 ``` |
| To | ``` func inet6_opt_finish(_ _: UnsafeMutableRawPointer!, _ _: socklen_t, _ _: Int32) -> Int32 ``` |

Modified inet6_opt_get_val(_: UnsafeMutableRawPointer!, _: Int32, _: UnsafeMutableRawPointer!, _: socklen_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_opt_get_val(_ _: UnsafeMutablePointer<Void>, _ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: socklen_t) -> Int32 ``` |
| To | ``` func inet6_opt_get_val(_ _: UnsafeMutableRawPointer!, _ _: Int32, _ _: UnsafeMutableRawPointer!, _ _: socklen_t) -> Int32 ``` |

Modified inet6_opt_init(_: UnsafeMutableRawPointer!, _: socklen_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_opt_init(_ _: UnsafeMutablePointer<Void>, _ _: socklen_t) -> Int32 ``` |
| To | ``` func inet6_opt_init(_ _: UnsafeMutableRawPointer!, _ _: socklen_t) -> Int32 ``` |

Modified inet6_opt_next(_: UnsafeMutableRawPointer!, _: socklen_t, _: Int32, _: UnsafeMutablePointer<__uint8_t>!, _: UnsafeMutablePointer<socklen_t>!, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_opt_next(_ _: UnsafeMutablePointer<Void>, _ _: socklen_t, _ _: Int32, _ _: UnsafeMutablePointer<__uint8_t>, _ _: UnsafeMutablePointer<socklen_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int32 ``` |
| To | ``` func inet6_opt_next(_ _: UnsafeMutableRawPointer!, _ _: socklen_t, _ _: Int32, _ _: UnsafeMutablePointer<__uint8_t>!, _ _: UnsafeMutablePointer<socklen_t>!, _ _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> Int32 ``` |

Modified inet6_opt_set_val(_: UnsafeMutableRawPointer!, _: Int32, _: UnsafeMutableRawPointer!, _: socklen_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_opt_set_val(_ _: UnsafeMutablePointer<Void>, _ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: socklen_t) -> Int32 ``` |
| To | ``` func inet6_opt_set_val(_ _: UnsafeMutableRawPointer!, _ _: Int32, _ _: UnsafeMutableRawPointer!, _ _: socklen_t) -> Int32 ``` |

Modified inet6_option_alloc(_: UnsafeMutablePointer<cmsghdr>!, _: Int32, _: Int32, _: Int32) -> UnsafeMutablePointer<__uint8_t>!

|  | Declaration |
| --- | --- |
| From | ``` func inet6_option_alloc(_ _: UnsafeMutablePointer<cmsghdr>, _ _: Int32, _ _: Int32, _ _: Int32) -> UnsafeMutablePointer<__uint8_t> ``` |
| To | ``` func inet6_option_alloc(_ _: UnsafeMutablePointer<cmsghdr>!, _ _: Int32, _ _: Int32, _ _: Int32) -> UnsafeMutablePointer<__uint8_t>! ``` |

Modified inet6_option_append(_: UnsafeMutablePointer<cmsghdr>!, _: UnsafePointer<__uint8_t>!, _: Int32, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_option_append(_ _: UnsafeMutablePointer<cmsghdr>, _ _: UnsafePointer<__uint8_t>, _ _: Int32, _ _: Int32) -> Int32 ``` |
| To | ``` func inet6_option_append(_ _: UnsafeMutablePointer<cmsghdr>!, _ _: UnsafePointer<__uint8_t>!, _ _: Int32, _ _: Int32) -> Int32 ``` |

Modified inet6_option_find(_: UnsafePointer<cmsghdr>!, _: UnsafeMutablePointer<UnsafeMutablePointer<__uint8_t>?>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_option_find(_ _: UnsafePointer<cmsghdr>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<__uint8_t>>, _ _: Int32) -> Int32 ``` |
| To | ``` func inet6_option_find(_ _: UnsafePointer<cmsghdr>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<__uint8_t>?>!, _ _: Int32) -> Int32 ``` |

Modified inet6_option_init(_: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<UnsafeMutablePointer<cmsghdr>?>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_option_init(_ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<cmsghdr>>, _ _: Int32) -> Int32 ``` |
| To | ``` func inet6_option_init(_ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<cmsghdr>?>!, _ _: Int32) -> Int32 ``` |

Modified inet6_option_next(_: UnsafePointer<cmsghdr>!, _: UnsafeMutablePointer<UnsafeMutablePointer<__uint8_t>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_option_next(_ _: UnsafePointer<cmsghdr>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<__uint8_t>>) -> Int32 ``` |
| To | ``` func inet6_option_next(_ _: UnsafePointer<cmsghdr>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<__uint8_t>?>!) -> Int32 ``` |

Modified inet6_rth_add(_: UnsafeMutableRawPointer!, _: UnsafePointer<in6_addr>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_rth_add(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<in6_addr>) -> Int32 ``` |
| To | ``` func inet6_rth_add(_ _: UnsafeMutableRawPointer!, _ _: UnsafePointer<in6_addr>!) -> Int32 ``` |

Modified inet6_rth_getaddr(_: UnsafeRawPointer!, _: Int32) -> UnsafeMutablePointer<in6_addr>!

|  | Declaration |
| --- | --- |
| From | ``` func inet6_rth_getaddr(_ _: UnsafePointer<Void>, _ _: Int32) -> UnsafeMutablePointer<in6_addr> ``` |
| To | ``` func inet6_rth_getaddr(_ _: UnsafeRawPointer!, _ _: Int32) -> UnsafeMutablePointer<in6_addr>! ``` |

Modified inet6_rth_init(_: UnsafeMutableRawPointer!, _: socklen_t, _: Int32, _: Int32) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func inet6_rth_init(_ _: UnsafeMutablePointer<Void>, _ _: socklen_t, _ _: Int32, _ _: Int32) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func inet6_rth_init(_ _: UnsafeMutableRawPointer!, _ _: socklen_t, _ _: Int32, _ _: Int32) -> UnsafeMutableRawPointer! ``` |

Modified inet6_rth_reverse(_: UnsafeRawPointer!, _: UnsafeMutableRawPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_rth_reverse(_ _: UnsafePointer<Void>, _ _: UnsafeMutablePointer<Void>) -> Int32 ``` |
| To | ``` func inet6_rth_reverse(_ _: UnsafeRawPointer!, _ _: UnsafeMutableRawPointer!) -> Int32 ``` |

Modified inet6_rth_segments(_: UnsafeRawPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_rth_segments(_ _: UnsafePointer<Void>) -> Int32 ``` |
| To | ``` func inet6_rth_segments(_ _: UnsafeRawPointer!) -> Int32 ``` |

Modified inet6_rthdr_add(_: UnsafeMutablePointer<cmsghdr>!, _: UnsafePointer<in6_addr>!, _: UInt32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_rthdr_add(_ _: UnsafeMutablePointer<cmsghdr>, _ _: UnsafePointer<in6_addr>, _ _: UInt32) -> Int32 ``` |
| To | ``` func inet6_rthdr_add(_ _: UnsafeMutablePointer<cmsghdr>!, _ _: UnsafePointer<in6_addr>!, _ _: UInt32) -> Int32 ``` |

Modified inet6_rthdr_getaddr(_: UnsafeMutablePointer<cmsghdr>!, _: Int32) -> UnsafeMutablePointer<in6_addr>!

|  | Declaration |
| --- | --- |
| From | ``` func inet6_rthdr_getaddr(_ _: UnsafeMutablePointer<cmsghdr>, _ _: Int32) -> UnsafeMutablePointer<in6_addr> ``` |
| To | ``` func inet6_rthdr_getaddr(_ _: UnsafeMutablePointer<cmsghdr>!, _ _: Int32) -> UnsafeMutablePointer<in6_addr>! ``` |

Modified inet6_rthdr_getflags(_: UnsafePointer<cmsghdr>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_rthdr_getflags(_ _: UnsafePointer<cmsghdr>, _ _: Int32) -> Int32 ``` |
| To | ``` func inet6_rthdr_getflags(_ _: UnsafePointer<cmsghdr>!, _ _: Int32) -> Int32 ``` |

Modified inet6_rthdr_init(_: UnsafeMutableRawPointer!, _: Int32) -> UnsafeMutablePointer<cmsghdr>!

|  | Declaration |
| --- | --- |
| From | ``` func inet6_rthdr_init(_ _: UnsafeMutablePointer<Void>, _ _: Int32) -> UnsafeMutablePointer<cmsghdr> ``` |
| To | ``` func inet6_rthdr_init(_ _: UnsafeMutableRawPointer!, _ _: Int32) -> UnsafeMutablePointer<cmsghdr>! ``` |

Modified inet6_rthdr_lasthop(_: UnsafeMutablePointer<cmsghdr>!, _: UInt32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_rthdr_lasthop(_ _: UnsafeMutablePointer<cmsghdr>, _ _: UInt32) -> Int32 ``` |
| To | ``` func inet6_rthdr_lasthop(_ _: UnsafeMutablePointer<cmsghdr>!, _ _: UInt32) -> Int32 ``` |

Modified inet6_rthdr_segments(_: UnsafePointer<cmsghdr>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet6_rthdr_segments(_ _: UnsafePointer<cmsghdr>) -> Int32 ``` |
| To | ``` func inet6_rthdr_segments(_ _: UnsafePointer<cmsghdr>!) -> Int32 ``` |

Modified inet_addr(_: UnsafePointer<Int8>!) -> in_addr_t

|  | Declaration |
| --- | --- |
| From | ``` func inet_addr(_ _: UnsafePointer<Int8>) -> in_addr_t ``` |
| To | ``` func inet_addr(_ _: UnsafePointer<Int8>!) -> in_addr_t ``` |

Modified inet_aton(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<in_addr>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet_aton(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<in_addr>) -> Int32 ``` |
| To | ``` func inet_aton(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<in_addr>!) -> Int32 ``` |

Modified inet_net_ntop(_: Int32, _: UnsafeRawPointer!, _: Int32, _: UnsafeMutablePointer<Int8>!, _: __darwin_size_t) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func inet_net_ntop(_ _: Int32, _ _: UnsafePointer<Void>, _ _: Int32, _ _: UnsafeMutablePointer<Int8>, _ _: __darwin_size_t) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func inet_net_ntop(_ _: Int32, _ _: UnsafeRawPointer!, _ _: Int32, _ _: UnsafeMutablePointer<Int8>!, _ _: __darwin_size_t) -> UnsafeMutablePointer<Int8>! ``` |

Modified inet_net_pton(_: Int32, _: UnsafePointer<Int8>!, _: UnsafeMutableRawPointer!, _: __darwin_size_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet_net_pton(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Void>, _ _: __darwin_size_t) -> Int32 ``` |
| To | ``` func inet_net_pton(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: UnsafeMutableRawPointer!, _ _: __darwin_size_t) -> Int32 ``` |

Modified inet_neta(_: in_addr_t, _: UnsafeMutablePointer<Int8>!, _: __darwin_size_t) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func inet_neta(_ _: in_addr_t, _ _: UnsafeMutablePointer<Int8>, _ _: __darwin_size_t) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func inet_neta(_ _: in_addr_t, _ _: UnsafeMutablePointer<Int8>!, _ _: __darwin_size_t) -> UnsafeMutablePointer<Int8>! ``` |

Modified inet_network(_: UnsafePointer<Int8>!) -> in_addr_t

|  | Declaration |
| --- | --- |
| From | ``` func inet_network(_ _: UnsafePointer<Int8>) -> in_addr_t ``` |
| To | ``` func inet_network(_ _: UnsafePointer<Int8>!) -> in_addr_t ``` |

Modified inet_nsap_addr(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UInt8>!, _: Int32) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func inet_nsap_addr(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UInt8>, _ _: Int32) -> UInt32 ``` |
| To | ``` func inet_nsap_addr(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UInt8>!, _ _: Int32) -> UInt32 ``` |

Modified inet_nsap_ntoa(_: Int32, _: UnsafePointer<UInt8>!, _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func inet_nsap_ntoa(_ _: Int32, _ _: UnsafePointer<UInt8>, _ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func inet_nsap_ntoa(_ _: Int32, _ _: UnsafePointer<UInt8>!, _ _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified inet_ntoa(_: in_addr) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func inet_ntoa(_ _: in_addr) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func inet_ntoa(_ _: in_addr) -> UnsafeMutablePointer<Int8>! ``` |

Modified inet_ntop(_: Int32, _: UnsafeRawPointer!, _: UnsafeMutablePointer<Int8>!, _: socklen_t) -> UnsafePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func inet_ntop(_ _: Int32, _ _: UnsafePointer<Void>, _ _: UnsafeMutablePointer<Int8>, _ _: socklen_t) -> UnsafePointer<Int8> ``` |
| To | ``` func inet_ntop(_ _: Int32, _ _: UnsafeRawPointer!, _ _: UnsafeMutablePointer<Int8>!, _ _: socklen_t) -> UnsafePointer<Int8>! ``` |

Modified inet_pton(_: Int32, _: UnsafePointer<Int8>!, _: UnsafeMutableRawPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func inet_pton(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Void>) -> Int32 ``` |
| To | ``` func inet_pton(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: UnsafeMutableRawPointer!) -> Int32 ``` |

Modified initgroups(_: UnsafePointer<Int8>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func initgroups(_ _: UnsafePointer<Int8>, _ _: Int32) -> Int32 ``` |
| To | ``` func initgroups(_ _: UnsafePointer<Int8>!, _ _: Int32) -> Int32 ``` |

Modified initstate(_: UInt32, _: UnsafeMutablePointer<Int8>!, _: Int) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func initstate(_ _: UInt32, _ _: UnsafeMutablePointer<Int8>, _ _: Int) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func initstate(_ _: UInt32, _ _: UnsafeMutablePointer<Int8>!, _ _: Int) -> UnsafeMutablePointer<Int8>! ``` |

Modified innetgr(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func innetgr(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func innetgr(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified insque(_: UnsafeMutableRawPointer!, _: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func insque(_ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>) ``` |
| To | ``` func insque(_ _: UnsafeMutableRawPointer!, _ _: UnsafeMutableRawPointer!) ``` |

Modified intmax_t

|  | Declaration |
| --- | --- |
| From | ``` typealias intmax_t = Int64 ``` |
| To | ``` typealias intmax_t = Int ``` |

Modified INTPTR_MAX

|  | Declaration |
| --- | --- |
| From | ``` var INTPTR_MAX: Int32 { get } ``` |
| To | ``` var INTPTR_MAX: Int64 { get } ``` |

Modified iruserok(_: UInt, _: Int32, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func iruserok(_ _: UInt, _ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> Int32 ``` | -- |
| To | ``` func iruserok(_ _: UInt, _ _: Int32, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!) -> Int32 ``` | iOS 10.0 |

Modified iruserok_sa(_: UnsafeRawPointer!, _: Int32, _: Int32, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func iruserok_sa(_ _: UnsafePointer<Void>, _ _: Int32, _ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> Int32 ``` | -- |
| To | ``` func iruserok_sa(_ _: UnsafeRawPointer!, _ _: Int32, _ _: Int32, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!) -> Int32 ``` | iOS 10.0 |

Modified isalnum_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func isalnum_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func isalnum_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified isalpha_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func isalpha_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func isalpha_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified isblank_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func isblank_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func isblank_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified iscntrl_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iscntrl_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func iscntrl_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified isdigit_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func isdigit_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func isdigit_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified isgraph_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func isgraph_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func isgraph_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified ishexnumber_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ishexnumber_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func ishexnumber_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified isideogram_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func isideogram_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func isideogram_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified islower_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func islower_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func islower_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified isnumber_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func isnumber_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func isnumber_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified isphonogram_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func isphonogram_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func isphonogram_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified isprint_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func isprint_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func isprint_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified ispunct_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ispunct_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func ispunct_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified isrune_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func isrune_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func isrune_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified isspace_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func isspace_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func isspace_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified isspecial_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func isspecial_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func isspecial_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified isupper_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func isupper_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func isupper_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified iswalnum_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswalnum_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswalnum_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswalpha_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswalpha_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswalpha_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswblank_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswblank_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswblank_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswcntrl_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswcntrl_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswcntrl_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswctype_l(_: wint_t, _: wctype_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswctype_l(_ _wc: wint_t, _ _charclass: wctype_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswctype_l(_ _wc: wint_t, _ _charclass: wctype_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswdigit_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswdigit_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswdigit_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswgraph_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswgraph_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswgraph_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswhexnumber_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswhexnumber_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswhexnumber_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswideogram_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswideogram_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswideogram_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswlower_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswlower_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswlower_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswnumber_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswnumber_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswnumber_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswphonogram_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswphonogram_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswphonogram_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswprint_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswprint_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswprint_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswpunct_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswpunct_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswpunct_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswrune_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswrune_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswrune_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswspace_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswspace_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswspace_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswspecial_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswspecial_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswspecial_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswupper_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswupper_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswupper_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified iswxdigit_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func iswxdigit_l(_ _wc: wint_t, _ _l: locale_t) -> Int32 ``` |
| To | ``` func iswxdigit_l(_ _wc: wint_t, _ _l: locale_t!) -> Int32 ``` |

Modified isxdigit_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func isxdigit_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func isxdigit_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified jmp_buf

|  | Declaration |
| --- | --- |
| From | ``` typealias jmp_buf = (Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32) ``` |
| To | ``` typealias jmp_buf = (Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32) ``` |

Modified jn(_: Int, _: Double) -> Double

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func jn(_ n: Int, _ x: Double) -> Double ``` |
| To | ``` func jn(_ n: Int, _ x: Double) -> Double ``` |

Modified kevent(_: Int32, _: UnsafePointer<kevent>!, _: Int32, _: UnsafeMutablePointer<kevent>!, _: Int32, _: UnsafePointer<timespec>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func kevent(_ kq: Int32, _ changelist: UnsafePointer<kevent>, _ nchanges: Int32, _ eventlist: UnsafeMutablePointer<kevent>, _ nevents: Int32, _ timeout: UnsafePointer<timespec>) -> Int32 ``` |
| To | ``` func kevent(_ kq: Int32, _ changelist: UnsafePointer<kevent>!, _ nchanges: Int32, _ eventlist: UnsafeMutablePointer<kevent>!, _ nevents: Int32, _ timeout: UnsafePointer<timespec>!) -> Int32 ``` |

Modified kevent64(_: Int32, _: UnsafePointer<kevent64_s>!, _: Int32, _: UnsafeMutablePointer<kevent64_s>!, _: Int32, _: UInt32, _: UnsafePointer<timespec>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func kevent64(_ kq: Int32, _ changelist: UnsafePointer<kevent64_s>, _ nchanges: Int32, _ eventlist: UnsafeMutablePointer<kevent64_s>, _ nevents: Int32, _ flags: UInt32, _ timeout: UnsafePointer<timespec>) -> Int32 ``` |
| To | ``` func kevent64(_ kq: Int32, _ changelist: UnsafePointer<kevent64_s>!, _ nchanges: Int32, _ eventlist: UnsafeMutablePointer<kevent64_s>!, _ nevents: Int32, _ flags: UInt32, _ timeout: UnsafePointer<timespec>!) -> Int32 ``` |

Modified kext_request(_: host_priv_t, _: UInt32, _: vm_offset_t, _: mach_msg_type_number_t, _: UnsafeMutablePointer<vm_offset_t>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: UnsafeMutablePointer<vm_offset_t>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: UnsafeMutablePointer<kern_return_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func kext_request(_ host_priv: host_priv_t, _ user_log_flags: UInt32, _ request_data: vm_offset_t, _ request_dataCnt: mach_msg_type_number_t, _ response_data: UnsafeMutablePointer<vm_offset_t>, _ response_dataCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ log_data: UnsafeMutablePointer<vm_offset_t>, _ log_dataCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ op_result: UnsafeMutablePointer<kern_return_t>) -> kern_return_t ``` |
| To | ``` func kext_request(_ host_priv: host_priv_t, _ user_log_flags: UInt32, _ request_data: vm_offset_t, _ request_dataCnt: mach_msg_type_number_t, _ response_data: UnsafeMutablePointer<vm_offset_t>!, _ response_dataCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ log_data: UnsafeMutablePointer<vm_offset_t>!, _ log_dataCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ op_result: UnsafeMutablePointer<kern_return_t>!) -> kern_return_t ``` |

Modified kmod_args_t

|  | Declaration |
| --- | --- |
| From | ``` typealias kmod_args_t = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias kmod_args_t = UnsafeMutableRawPointer ``` |

Modified kmod_control(_: host_priv_t, _: kmod_t, _: kmod_control_flavor_t, _: UnsafeMutablePointer<kmod_args_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func kmod_control(_ host_priv: host_priv_t, _ module: kmod_t, _ flavor: kmod_control_flavor_t, _ data: UnsafeMutablePointer<kmod_args_t>, _ dataCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func kmod_control(_ host_priv: host_priv_t, _ module: kmod_t, _ flavor: kmod_control_flavor_t, _ data: UnsafeMutablePointer<kmod_args_t?>!, _ dataCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified kmod_create(_: host_priv_t, _: vm_address_t, _: UnsafeMutablePointer<kmod_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func kmod_create(_ host_priv: host_priv_t, _ info: vm_address_t, _ module: UnsafeMutablePointer<kmod_t>) -> kern_return_t ``` |
| To | ``` func kmod_create(_ host_priv: host_priv_t, _ info: vm_address_t, _ module: UnsafeMutablePointer<kmod_t>!) -> kern_return_t ``` |

Modified kmod_get_info(_: host_t, _: UnsafeMutablePointer<kmod_args_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func kmod_get_info(_ host: host_t, _ modules: UnsafeMutablePointer<kmod_args_t>, _ modulesCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func kmod_get_info(_ host: host_t, _ modules: UnsafeMutablePointer<kmod_args_t?>!, _ modulesCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified kmod_start_func_t

|  | Declaration |
| --- | --- |
| From | ``` typealias kmod_start_func_t = (UnsafeMutablePointer<kmod_info>, UnsafeMutablePointer<Void>) -> kern_return_t ``` |
| To | ``` typealias kmod_start_func_t = (UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t ``` |

Modified kmod_stop_func_t

|  | Declaration |
| --- | --- |
| From | ``` typealias kmod_stop_func_t = (UnsafeMutablePointer<kmod_info>, UnsafeMutablePointer<Void>) -> kern_return_t ``` |
| To | ``` typealias kmod_stop_func_t = (UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t ``` |

Modified l64a(_: Int) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func l64a(_ _: Int) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func l64a(_ _: Int) -> UnsafeMutablePointer<Int8>! ``` |

Modified lchflags(_: UnsafePointer<Int8>!, _: __uint32_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func lchflags(_ _: UnsafePointer<Int8>, _ _: __uint32_t) -> Int32 ``` |
| To | ``` func lchflags(_ _: UnsafePointer<Int8>!, _ _: __uint32_t) -> Int32 ``` |

Modified lchmod(_: UnsafePointer<Int8>!, _: mode_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func lchmod(_ _: UnsafePointer<Int8>, _ _: mode_t) -> Int32 ``` |
| To | ``` func lchmod(_ _: UnsafePointer<Int8>!, _ _: mode_t) -> Int32 ``` |

Modified lchown(_: UnsafePointer<Int8>!, _: uid_t, _: gid_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func lchown(_ _: UnsafePointer<Int8>, _ _: uid_t, _ _: gid_t) -> Int32 ``` |
| To | ``` func lchown(_ _: UnsafePointer<Int8>!, _ _: uid_t, _ _: gid_t) -> Int32 ``` |

Modified lcong48(_: UnsafeMutablePointer<UInt16>!)

|  | Declaration |
| --- | --- |
| From | ``` func lcong48(_ _: UnsafeMutablePointer<UInt16>) ``` |
| To | ``` func lcong48(_ _: UnsafeMutablePointer<UInt16>!) ``` |

Modified ldexp(_: Double, _: Int) -> Double

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ldexp(_ x: Double, _ n: Int) -> Double ``` |
| To | ``` func ldexp(_ x: Double, _ n: Int) -> Double ``` |

Modified ldexp(_: Float, _: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ldexp(_ x: Float, _ n: Int) -> Float ``` |
| To | ``` func ldexp(_ x: Float, _ n: Int) -> Float ``` |

Modified lfind(_: UnsafeRawPointer!, _: UnsafeRawPointer!, _: UnsafeMutablePointer<Int>!, _: Int, _: ( (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func lfind(_ _: UnsafePointer<Void>, _ _: UnsafePointer<Void>, _ _: UnsafeMutablePointer<Int>, _ _: Int, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func lfind(_ _: UnsafeRawPointer!, _ _: UnsafeRawPointer!, _ _: UnsafeMutablePointer<Int>!, _ _: Int, _ _: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer! ``` |

Modified lgamma(_: Float) -> (Float, Int)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func lgamma(_ x: Float) -> (Float, Int) ``` |
| To | ``` func lgamma(_ x: Float) -> (Float, Int) ``` |

Modified lgamma(_: Double) -> (Double, Int)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func lgamma(_ x: Double) -> (Double, Int) ``` |
| To | ``` func lgamma(_ x: Double) -> (Double, Int) ``` |

Modified libiconv_set_relocation_prefix(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!)

|  | Declaration |
| --- | --- |
| From | ``` func libiconv_set_relocation_prefix(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) ``` |
| To | ``` func libiconv_set_relocation_prefix(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!) ``` |

Modified link(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func link(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func link(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified linkat(_: Int32, _: UnsafePointer<Int8>!, _: Int32, _: UnsafePointer<Int8>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func linkat(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: Int32, _ _: UnsafePointer<Int8>, _ _: Int32) -> Int32 ``` |
| To | ``` func linkat(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: Int32, _ _: UnsafePointer<Int8>!, _ _: Int32) -> Int32 ``` |

Modified lio_listio(_: Int32, _: UnsafePointer<UnsafeMutablePointer<aiocb>?>!, _: Int32, _: UnsafeMutablePointer<sigevent>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func lio_listio(_ mode: Int32, _ aiocblist: UnsafePointer<UnsafeMutablePointer<aiocb>>, _ nent: Int32, _ sigp: UnsafeMutablePointer<sigevent>) -> Int32 ``` |
| To | ``` func lio_listio(_ mode: Int32, _ aiocblist: UnsafePointer<UnsafeMutablePointer<aiocb>?>!, _ nent: Int32, _ sigp: UnsafeMutablePointer<sigevent>!) -> Int32 ``` |

Modified listxattr(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Int8>!, _: Int, _: Int32) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func listxattr(_ path: UnsafePointer<Int8>, _ namebuff: UnsafeMutablePointer<Int8>, _ size: Int, _ options: Int32) -> Int ``` |
| To | ``` func listxattr(_ path: UnsafePointer<Int8>!, _ namebuff: UnsafeMutablePointer<Int8>!, _ size: Int, _ options: Int32) -> Int ``` |

Modified locale_t

|  | Declaration |
| --- | --- |
| From | ``` typealias locale_t = COpaquePointer ``` |
| To | ``` typealias locale_t = OpaquePointer ``` |

Modified localeconv() -> UnsafeMutablePointer<lconv>!

|  | Declaration |
| --- | --- |
| From | ``` func localeconv() -> UnsafeMutablePointer<lconv> ``` |
| To | ``` func localeconv() -> UnsafeMutablePointer<lconv>! ``` |

Modified localeconv_l(_: locale_t!) -> UnsafeMutablePointer<lconv>!

|  | Declaration |
| --- | --- |
| From | ``` func localeconv_l(_ _: locale_t) -> UnsafeMutablePointer<lconv> ``` |
| To | ``` func localeconv_l(_ _: locale_t!) -> UnsafeMutablePointer<lconv>! ``` |

Modified localtime(_: UnsafePointer<time_t>!) -> UnsafeMutablePointer<tm>!

|  | Declaration |
| --- | --- |
| From | ``` func localtime(_ _: UnsafePointer<time_t>) -> UnsafeMutablePointer<tm> ``` |
| To | ``` func localtime(_ _: UnsafePointer<time_t>!) -> UnsafeMutablePointer<tm>! ``` |

Modified localtime_r(_: UnsafePointer<time_t>!, _: UnsafeMutablePointer<tm>!) -> UnsafeMutablePointer<tm>!

|  | Declaration |
| --- | --- |
| From | ``` func localtime_r(_ _: UnsafePointer<time_t>, _ _: UnsafeMutablePointer<tm>) -> UnsafeMutablePointer<tm> ``` |
| To | ``` func localtime_r(_ _: UnsafePointer<time_t>!, _ _: UnsafeMutablePointer<tm>!) -> UnsafeMutablePointer<tm>! ``` |

Modified lock_set_create(_: task_t, _: UnsafeMutablePointer<lock_set_t>!, _: Int32, _: Int32) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func lock_set_create(_ task: task_t, _ new_lock_set: UnsafeMutablePointer<lock_set_t>, _ n_ulocks: Int32, _ policy: Int32) -> kern_return_t ``` |
| To | ``` func lock_set_create(_ task: task_t, _ new_lock_set: UnsafeMutablePointer<lock_set_t>!, _ n_ulocks: Int32, _ policy: Int32) -> kern_return_t ``` |

Modified log(_: Double) -> Double

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func log(_ x: Double) -> Double ``` |
| To | ``` func log(_ x: Double) -> Double ``` |

Modified log(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func log(_ x: Float) -> Float ``` |
| To | ``` func log(_ x: Float) -> Float ``` |

Modified log10(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func log10(_ x: Float) -> Float ``` |
| To | ``` func log10(_ x: Float) -> Float ``` |

Modified log10(_: Double) -> Double

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func log10(_ x: Double) -> Double ``` |
| To | ``` func log10(_ x: Double) -> Double ``` |

Modified log1p(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func log1p(_ x: Float) -> Float ``` |
| To | ``` func log1p(_ x: Float) -> Float ``` |

Modified log2(_: Double) -> Double

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func log2(_ x: Double) -> Double ``` |
| To | ``` func log2(_ x: Double) -> Double ``` |

Modified log2(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func log2(_ x: Float) -> Float ``` |
| To | ``` func log2(_ x: Float) -> Float ``` |

Modified logb(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func logb(_ x: Float) -> Float ``` |
| To | ``` func logb(_ x: Float) -> Float ``` |

Modified longjmp(_: UnsafeMutablePointer<Int32>!, _: Int32) -> Never

|  | Declaration |
| --- | --- |
| From | ``` @noreturn func longjmp(_ _: UnsafeMutablePointer<Int32>, _ _: Int32) ``` |
| To | ``` func longjmp(_ _: UnsafeMutablePointer<Int32>!, _ _: Int32) -> Never ``` |

Modified lsearch(_: UnsafeRawPointer!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!, _: Int, _: ( (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func lsearch(_ _: UnsafePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>, _ _: Int, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func lsearch(_ _: UnsafeRawPointer!, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!, _ _: Int, _ _: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer! ``` |

Modified lstat(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<stat>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func lstat(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<stat>) -> Int32 ``` |
| To | ``` func lstat(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<stat>!) -> Int32 ``` |

Modified lstatx_np(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<stat>!, _: filesec_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func lstatx_np(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<stat>, _ _: filesec_t) -> Int32 ``` |
| To | ``` func lstatx_np(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<stat>!, _ _: filesec_t!) -> Int32 ``` |

Modified lutimes(_: UnsafePointer<Int8>!, _: UnsafePointer<timeval>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func lutimes(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<timeval>) -> Int32 ``` |
| To | ``` func lutimes(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<timeval>!) -> Int32 ``` |

Modified mach_error(_: UnsafePointer<Int8>!, _: mach_error_t)

|  | Declaration |
| --- | --- |
| From | ``` func mach_error(_ str: UnsafePointer<Int8>, _ error_value: mach_error_t) ``` |
| To | ``` func mach_error(_ str: UnsafePointer<Int8>!, _ error_value: mach_error_t) ``` |

Modified mach_error_string(_: mach_error_t) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func mach_error_string(_ error_value: mach_error_t) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func mach_error_string(_ error_value: mach_error_t) -> UnsafeMutablePointer<Int8>! ``` |

Modified mach_error_type(_: mach_error_t) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func mach_error_type(_ error_value: mach_error_t) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func mach_error_type(_ error_value: mach_error_t) -> UnsafeMutablePointer<Int8>! ``` |

Modified mach_make_memory_entry(_: vm_map_t, _: UnsafeMutablePointer<vm_size_t>!, _: vm_offset_t, _: vm_prot_t, _: UnsafeMutablePointer<mem_entry_name_port_t>!, _: mem_entry_name_port_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_make_memory_entry(_ target_task: vm_map_t, _ size: UnsafeMutablePointer<vm_size_t>, _ offset: vm_offset_t, _ permission: vm_prot_t, _ object_handle: UnsafeMutablePointer<mem_entry_name_port_t>, _ parent_entry: mem_entry_name_port_t) -> kern_return_t ``` |
| To | ``` func mach_make_memory_entry(_ target_task: vm_map_t, _ size: UnsafeMutablePointer<vm_size_t>!, _ offset: vm_offset_t, _ permission: vm_prot_t, _ object_handle: UnsafeMutablePointer<mem_entry_name_port_t>!, _ parent_entry: mem_entry_name_port_t) -> kern_return_t ``` |

Modified mach_make_memory_entry_64(_: vm_map_t, _: UnsafeMutablePointer<memory_object_size_t>!, _: memory_object_offset_t, _: vm_prot_t, _: UnsafeMutablePointer<mach_port_t>!, _: mem_entry_name_port_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_make_memory_entry_64(_ target_task: vm_map_t, _ size: UnsafeMutablePointer<memory_object_size_t>, _ offset: memory_object_offset_t, _ permission: vm_prot_t, _ object_handle: UnsafeMutablePointer<mach_port_t>, _ parent_entry: mem_entry_name_port_t) -> kern_return_t ``` |
| To | ``` func mach_make_memory_entry_64(_ target_task: vm_map_t, _ size: UnsafeMutablePointer<memory_object_size_t>!, _ offset: memory_object_offset_t, _ permission: vm_prot_t, _ object_handle: UnsafeMutablePointer<mach_port_t>!, _ parent_entry: mem_entry_name_port_t) -> kern_return_t ``` |

Modified mach_memory_info(_: host_priv_t, _: UnsafeMutablePointer<mach_zone_name_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: UnsafeMutablePointer<mach_zone_info_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: UnsafeMutablePointer<mach_memory_info_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_memory_info(_ host: host_priv_t, _ names: UnsafeMutablePointer<mach_zone_name_array_t>, _ namesCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ info: UnsafeMutablePointer<mach_zone_info_array_t>, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ memory_info: UnsafeMutablePointer<mach_memory_info_array_t>, _ memory_infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func mach_memory_info(_ host: host_priv_t, _ names: UnsafeMutablePointer<mach_zone_name_array_t?>!, _ namesCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ info: UnsafeMutablePointer<mach_zone_info_array_t?>!, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ memory_info: UnsafeMutablePointer<mach_memory_info_array_t?>!, _ memory_infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified mach_memory_object_memory_entry(_: host_t, _: boolean_t, _: vm_size_t, _: vm_prot_t, _: memory_object_t, _: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_memory_object_memory_entry(_ host: host_t, _ internal: boolean_t, _ size: vm_size_t, _ permission: vm_prot_t, _ pager: memory_object_t, _ entry_handle: UnsafeMutablePointer<mach_port_t>) -> kern_return_t ``` |
| To | ``` func mach_memory_object_memory_entry(_ host: host_t, _ internal: boolean_t, _ size: vm_size_t, _ permission: vm_prot_t, _ pager: memory_object_t, _ entry_handle: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t ``` |

Modified mach_memory_object_memory_entry_64(_: host_t, _: boolean_t, _: memory_object_size_t, _: vm_prot_t, _: memory_object_t, _: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_memory_object_memory_entry_64(_ host: host_t, _ internal: boolean_t, _ size: memory_object_size_t, _ permission: vm_prot_t, _ pager: memory_object_t, _ entry_handle: UnsafeMutablePointer<mach_port_t>) -> kern_return_t ``` |
| To | ``` func mach_memory_object_memory_entry_64(_ host: host_t, _ internal: boolean_t, _ size: memory_object_size_t, _ permission: vm_prot_t, _ pager: memory_object_t, _ entry_handle: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t ``` |

Modified mach_msg(_: UnsafeMutablePointer<mach_msg_header_t>!, _: mach_msg_option_t, _: mach_msg_size_t, _: mach_msg_size_t, _: mach_port_name_t, _: mach_msg_timeout_t, _: mach_port_name_t) -> mach_msg_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_msg(_ msg: UnsafeMutablePointer<mach_msg_header_t>, _ option: mach_msg_option_t, _ send_size: mach_msg_size_t, _ rcv_size: mach_msg_size_t, _ rcv_name: mach_port_name_t, _ timeout: mach_msg_timeout_t, _ notify: mach_port_name_t) -> mach_msg_return_t ``` |
| To | ``` func mach_msg(_ msg: UnsafeMutablePointer<mach_msg_header_t>!, _ option: mach_msg_option_t, _ send_size: mach_msg_size_t, _ rcv_size: mach_msg_size_t, _ rcv_name: mach_port_name_t, _ timeout: mach_msg_timeout_t, _ notify: mach_port_name_t) -> mach_msg_return_t ``` |

Modified mach_msg_destroy(_: UnsafeMutablePointer<mach_msg_header_t>!)

|  | Declaration |
| --- | --- |
| From | ``` func mach_msg_destroy(_ _: UnsafeMutablePointer<mach_msg_header_t>) ``` |
| To | ``` func mach_msg_destroy(_ _: UnsafeMutablePointer<mach_msg_header_t>!) ``` |

Modified mach_msg_overwrite(_: UnsafeMutablePointer<mach_msg_header_t>!, _: mach_msg_option_t, _: mach_msg_size_t, _: mach_msg_size_t, _: mach_port_name_t, _: mach_msg_timeout_t, _: mach_port_name_t, _: UnsafeMutablePointer<mach_msg_header_t>!, _: mach_msg_size_t) -> mach_msg_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_msg_overwrite(_ msg: UnsafeMutablePointer<mach_msg_header_t>, _ option: mach_msg_option_t, _ send_size: mach_msg_size_t, _ rcv_size: mach_msg_size_t, _ rcv_name: mach_port_name_t, _ timeout: mach_msg_timeout_t, _ notify: mach_port_name_t, _ rcv_msg: UnsafeMutablePointer<mach_msg_header_t>, _ rcv_limit: mach_msg_size_t) -> mach_msg_return_t ``` |
| To | ``` func mach_msg_overwrite(_ msg: UnsafeMutablePointer<mach_msg_header_t>!, _ option: mach_msg_option_t, _ send_size: mach_msg_size_t, _ rcv_size: mach_msg_size_t, _ rcv_name: mach_port_name_t, _ timeout: mach_msg_timeout_t, _ notify: mach_port_name_t, _ rcv_msg: UnsafeMutablePointer<mach_msg_header_t>!, _ rcv_limit: mach_msg_size_t) -> mach_msg_return_t ``` |

Modified mach_msg_receive(_: UnsafeMutablePointer<mach_msg_header_t>!) -> mach_msg_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_msg_receive(_ _: UnsafeMutablePointer<mach_msg_header_t>) -> mach_msg_return_t ``` |
| To | ``` func mach_msg_receive(_ _: UnsafeMutablePointer<mach_msg_header_t>!) -> mach_msg_return_t ``` |

Modified mach_msg_send(_: UnsafeMutablePointer<mach_msg_header_t>!) -> mach_msg_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_msg_send(_ _: UnsafeMutablePointer<mach_msg_header_t>) -> mach_msg_return_t ``` |
| To | ``` func mach_msg_send(_ _: UnsafeMutablePointer<mach_msg_header_t>!) -> mach_msg_return_t ``` |

Modified mach_msg_server(_: ( (UnsafeMutablePointer<mach_msg_header_t>?, UnsafeMutablePointer<mach_msg_header_t>?) -> boolean_t)!, _: mach_msg_size_t, _: mach_port_t, _: mach_msg_options_t) -> mach_msg_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_msg_server(_ _: ((UnsafeMutablePointer<mach_msg_header_t>, UnsafeMutablePointer<mach_msg_header_t>) -> boolean_t)!, _ _: mach_msg_size_t, _ _: mach_port_t, _ _: mach_msg_options_t) -> mach_msg_return_t ``` |
| To | ``` func mach_msg_server(_ _: (@escaping (UnsafeMutablePointer<mach_msg_header_t>?, UnsafeMutablePointer<mach_msg_header_t>?) -> boolean_t)!, _ _: mach_msg_size_t, _ _: mach_port_t, _ _: mach_msg_options_t) -> mach_msg_return_t ``` |

Modified mach_msg_server_importance(_: ( (UnsafeMutablePointer<mach_msg_header_t>?, UnsafeMutablePointer<mach_msg_header_t>?) -> boolean_t)!, _: mach_msg_size_t, _: mach_port_t, _: mach_msg_options_t) -> mach_msg_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_msg_server_importance(_ _: ((UnsafeMutablePointer<mach_msg_header_t>, UnsafeMutablePointer<mach_msg_header_t>) -> boolean_t)!, _ _: mach_msg_size_t, _ _: mach_port_t, _ _: mach_msg_options_t) -> mach_msg_return_t ``` |
| To | ``` func mach_msg_server_importance(_ _: (@escaping (UnsafeMutablePointer<mach_msg_header_t>?, UnsafeMutablePointer<mach_msg_header_t>?) -> boolean_t)!, _ _: mach_msg_size_t, _ _: mach_port_t, _ _: mach_msg_options_t) -> mach_msg_return_t ``` |

Modified mach_msg_server_once(_: ( (UnsafeMutablePointer<mach_msg_header_t>?, UnsafeMutablePointer<mach_msg_header_t>?) -> boolean_t)!, _: mach_msg_size_t, _: mach_port_t, _: mach_msg_options_t) -> mach_msg_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_msg_server_once(_ _: ((UnsafeMutablePointer<mach_msg_header_t>, UnsafeMutablePointer<mach_msg_header_t>) -> boolean_t)!, _ _: mach_msg_size_t, _ _: mach_port_t, _ _: mach_msg_options_t) -> mach_msg_return_t ``` |
| To | ``` func mach_msg_server_once(_ _: (@escaping (UnsafeMutablePointer<mach_msg_header_t>?, UnsafeMutablePointer<mach_msg_header_t>?) -> boolean_t)!, _ _: mach_msg_size_t, _ _: mach_port_t, _ _: mach_msg_options_t) -> mach_msg_return_t ``` |

Modified mach_port_allocate(_: ipc_space_t, _: mach_port_right_t, _: UnsafeMutablePointer<mach_port_name_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_allocate(_ task: ipc_space_t, _ right: mach_port_right_t, _ name: UnsafeMutablePointer<mach_port_name_t>) -> kern_return_t ``` |
| To | ``` func mach_port_allocate(_ task: ipc_space_t, _ right: mach_port_right_t, _ name: UnsafeMutablePointer<mach_port_name_t>!) -> kern_return_t ``` |

Modified mach_port_allocate_full(_: ipc_space_t, _: mach_port_right_t, _: mach_port_t, _: UnsafeMutablePointer<mach_port_qos_t>!, _: UnsafeMutablePointer<mach_port_name_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_allocate_full(_ task: ipc_space_t, _ right: mach_port_right_t, _ proto: mach_port_t, _ qos: UnsafeMutablePointer<mach_port_qos_t>, _ name: UnsafeMutablePointer<mach_port_name_t>) -> kern_return_t ``` |
| To | ``` func mach_port_allocate_full(_ task: ipc_space_t, _ right: mach_port_right_t, _ proto: mach_port_t, _ qos: UnsafeMutablePointer<mach_port_qos_t>!, _ name: UnsafeMutablePointer<mach_port_name_t>!) -> kern_return_t ``` |

Modified mach_port_allocate_qos(_: ipc_space_t, _: mach_port_right_t, _: UnsafeMutablePointer<mach_port_qos_t>!, _: UnsafeMutablePointer<mach_port_name_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_allocate_qos(_ task: ipc_space_t, _ right: mach_port_right_t, _ qos: UnsafeMutablePointer<mach_port_qos_t>, _ name: UnsafeMutablePointer<mach_port_name_t>) -> kern_return_t ``` |
| To | ``` func mach_port_allocate_qos(_ task: ipc_space_t, _ right: mach_port_right_t, _ qos: UnsafeMutablePointer<mach_port_qos_t>!, _ name: UnsafeMutablePointer<mach_port_name_t>!) -> kern_return_t ``` |

Modified mach_port_construct(_: ipc_space_t, _: mach_port_options_ptr_t!, _: mach_port_context_t, _: UnsafeMutablePointer<mach_port_name_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_construct(_ task: ipc_space_t, _ options: mach_port_options_ptr_t, _ context: mach_port_context_t, _ name: UnsafeMutablePointer<mach_port_name_t>) -> kern_return_t ``` |
| To | ``` func mach_port_construct(_ task: ipc_space_t, _ options: mach_port_options_ptr_t!, _ context: mach_port_context_t, _ name: UnsafeMutablePointer<mach_port_name_t>!) -> kern_return_t ``` |

Modified mach_port_dnrequest_info(_: ipc_space_t, _: mach_port_name_t, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt32>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_dnrequest_info(_ task: ipc_space_t, _ name: mach_port_name_t, _ dnr_total: UnsafeMutablePointer<UInt32>, _ dnr_used: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` |
| To | ``` func mach_port_dnrequest_info(_ task: ipc_space_t, _ name: mach_port_name_t, _ dnr_total: UnsafeMutablePointer<UInt32>!, _ dnr_used: UnsafeMutablePointer<UInt32>!) -> kern_return_t ``` |

Modified mach_port_extract_right(_: ipc_space_t, _: mach_port_name_t, _: mach_msg_type_name_t, _: UnsafeMutablePointer<mach_port_t>!, _: UnsafeMutablePointer<mach_msg_type_name_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_extract_right(_ task: ipc_space_t, _ name: mach_port_name_t, _ msgt_name: mach_msg_type_name_t, _ poly: UnsafeMutablePointer<mach_port_t>, _ polyPoly: UnsafeMutablePointer<mach_msg_type_name_t>) -> kern_return_t ``` |
| To | ``` func mach_port_extract_right(_ task: ipc_space_t, _ name: mach_port_name_t, _ msgt_name: mach_msg_type_name_t, _ poly: UnsafeMutablePointer<mach_port_t>!, _ polyPoly: UnsafeMutablePointer<mach_msg_type_name_t>!) -> kern_return_t ``` |

Modified mach_port_get_attributes(_: ipc_space_t, _: mach_port_name_t, _: mach_port_flavor_t, _: mach_port_info_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_get_attributes(_ task: ipc_space_t, _ name: mach_port_name_t, _ flavor: mach_port_flavor_t, _ port_info_out: mach_port_info_t, _ port_info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func mach_port_get_attributes(_ task: ipc_space_t, _ name: mach_port_name_t, _ flavor: mach_port_flavor_t, _ port_info_out: mach_port_info_t!, _ port_info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified mach_port_get_context(_: ipc_space_t, _: mach_port_name_t, _: UnsafeMutablePointer<mach_port_context_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_get_context(_ task: ipc_space_t, _ name: mach_port_name_t, _ context: UnsafeMutablePointer<mach_port_context_t>) -> kern_return_t ``` |
| To | ``` func mach_port_get_context(_ task: ipc_space_t, _ name: mach_port_name_t, _ context: UnsafeMutablePointer<mach_port_context_t>!) -> kern_return_t ``` |

Modified mach_port_get_refs(_: ipc_space_t, _: mach_port_name_t, _: mach_port_right_t, _: UnsafeMutablePointer<mach_port_urefs_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_get_refs(_ task: ipc_space_t, _ name: mach_port_name_t, _ right: mach_port_right_t, _ refs: UnsafeMutablePointer<mach_port_urefs_t>) -> kern_return_t ``` |
| To | ``` func mach_port_get_refs(_ task: ipc_space_t, _ name: mach_port_name_t, _ right: mach_port_right_t, _ refs: UnsafeMutablePointer<mach_port_urefs_t>!) -> kern_return_t ``` |

Modified mach_port_get_set_status(_: ipc_space_t, _: mach_port_name_t, _: UnsafeMutablePointer<mach_port_name_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_get_set_status(_ task: ipc_space_t, _ name: mach_port_name_t, _ members: UnsafeMutablePointer<mach_port_name_array_t>, _ membersCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func mach_port_get_set_status(_ task: ipc_space_t, _ name: mach_port_name_t, _ members: UnsafeMutablePointer<mach_port_name_array_t?>!, _ membersCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified mach_port_get_srights(_: ipc_space_t, _: mach_port_name_t, _: UnsafeMutablePointer<mach_port_rights_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_get_srights(_ task: ipc_space_t, _ name: mach_port_name_t, _ srights: UnsafeMutablePointer<mach_port_rights_t>) -> kern_return_t ``` |
| To | ``` func mach_port_get_srights(_ task: ipc_space_t, _ name: mach_port_name_t, _ srights: UnsafeMutablePointer<mach_port_rights_t>!) -> kern_return_t ``` |

Modified mach_port_kernel_object(_: ipc_space_t, _: mach_port_name_t, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<UInt32>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_kernel_object(_ task: ipc_space_t, _ name: mach_port_name_t, _ object_type: UnsafeMutablePointer<UInt32>, _ object_addr: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` |
| To | ``` func mach_port_kernel_object(_ task: ipc_space_t, _ name: mach_port_name_t, _ object_type: UnsafeMutablePointer<UInt32>!, _ object_addr: UnsafeMutablePointer<UInt32>!) -> kern_return_t ``` |

Modified mach_port_kobject(_: ipc_space_t, _: mach_port_name_t, _: UnsafeMutablePointer<natural_t>!, _: UnsafeMutablePointer<mach_vm_address_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_kobject(_ task: ipc_space_t, _ name: mach_port_name_t, _ object_type: UnsafeMutablePointer<natural_t>, _ object_addr: UnsafeMutablePointer<mach_vm_address_t>) -> kern_return_t ``` |
| To | ``` func mach_port_kobject(_ task: ipc_space_t, _ name: mach_port_name_t, _ object_type: UnsafeMutablePointer<natural_t>!, _ object_addr: UnsafeMutablePointer<mach_vm_address_t>!) -> kern_return_t ``` |

Modified mach_port_names(_: ipc_space_t, _: UnsafeMutablePointer<mach_port_name_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: UnsafeMutablePointer<mach_port_type_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_names(_ task: ipc_space_t, _ names: UnsafeMutablePointer<mach_port_name_array_t>, _ namesCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ types: UnsafeMutablePointer<mach_port_type_array_t>, _ typesCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func mach_port_names(_ task: ipc_space_t, _ names: UnsafeMutablePointer<mach_port_name_array_t?>!, _ namesCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ types: UnsafeMutablePointer<mach_port_type_array_t?>!, _ typesCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified mach_port_peek(_: ipc_space_t, _: mach_port_name_t, _: mach_msg_trailer_type_t, _: UnsafeMutablePointer<mach_port_seqno_t>!, _: UnsafeMutablePointer<mach_msg_size_t>!, _: UnsafeMutablePointer<mach_msg_id_t>!, _: mach_msg_trailer_info_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_peek(_ task: ipc_space_t, _ name: mach_port_name_t, _ trailer_type: mach_msg_trailer_type_t, _ request_seqnop: UnsafeMutablePointer<mach_port_seqno_t>, _ msg_sizep: UnsafeMutablePointer<mach_msg_size_t>, _ msg_idp: UnsafeMutablePointer<mach_msg_id_t>, _ trailer_infop: mach_msg_trailer_info_t, _ trailer_infopCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func mach_port_peek(_ task: ipc_space_t, _ name: mach_port_name_t, _ trailer_type: mach_msg_trailer_type_t, _ request_seqnop: UnsafeMutablePointer<mach_port_seqno_t>!, _ msg_sizep: UnsafeMutablePointer<mach_msg_size_t>!, _ msg_idp: UnsafeMutablePointer<mach_msg_id_t>!, _ trailer_infop: mach_msg_trailer_info_t!, _ trailer_infopCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified mach_port_request_notification(_: ipc_space_t, _: mach_port_name_t, _: mach_msg_id_t, _: mach_port_mscount_t, _: mach_port_t, _: mach_msg_type_name_t, _: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_request_notification(_ task: ipc_space_t, _ name: mach_port_name_t, _ msgid: mach_msg_id_t, _ sync: mach_port_mscount_t, _ notify: mach_port_t, _ notifyPoly: mach_msg_type_name_t, _ previous: UnsafeMutablePointer<mach_port_t>) -> kern_return_t ``` |
| To | ``` func mach_port_request_notification(_ task: ipc_space_t, _ name: mach_port_name_t, _ msgid: mach_msg_id_t, _ sync: mach_port_mscount_t, _ notify: mach_port_t, _ notifyPoly: mach_msg_type_name_t, _ previous: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t ``` |

Modified mach_port_set_attributes(_: ipc_space_t, _: mach_port_name_t, _: mach_port_flavor_t, _: mach_port_info_t!, _: mach_msg_type_number_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_set_attributes(_ task: ipc_space_t, _ name: mach_port_name_t, _ flavor: mach_port_flavor_t, _ port_info: mach_port_info_t, _ port_infoCnt: mach_msg_type_number_t) -> kern_return_t ``` |
| To | ``` func mach_port_set_attributes(_ task: ipc_space_t, _ name: mach_port_name_t, _ flavor: mach_port_flavor_t, _ port_info: mach_port_info_t!, _ port_infoCnt: mach_msg_type_number_t) -> kern_return_t ``` |

Modified mach_port_space_basic_info(_: ipc_space_t, _: UnsafeMutablePointer<ipc_info_space_basic_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_space_basic_info(_ task: ipc_space_t, _ basic_info: UnsafeMutablePointer<ipc_info_space_basic_t>) -> kern_return_t ``` |
| To | ``` func mach_port_space_basic_info(_ task: ipc_space_t, _ basic_info: UnsafeMutablePointer<ipc_info_space_basic_t>!) -> kern_return_t ``` |

Modified mach_port_space_info(_: ipc_space_t, _: UnsafeMutablePointer<ipc_info_space_t>!, _: UnsafeMutablePointer<ipc_info_name_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: UnsafeMutablePointer<ipc_info_tree_name_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_space_info(_ task: ipc_space_t, _ space_info: UnsafeMutablePointer<ipc_info_space_t>, _ table_info: UnsafeMutablePointer<ipc_info_name_array_t>, _ table_infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ tree_info: UnsafeMutablePointer<ipc_info_tree_name_array_t>, _ tree_infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func mach_port_space_info(_ task: ipc_space_t, _ space_info: UnsafeMutablePointer<ipc_info_space_t>!, _ table_info: UnsafeMutablePointer<ipc_info_name_array_t?>!, _ table_infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ tree_info: UnsafeMutablePointer<ipc_info_tree_name_array_t?>!, _ tree_infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified mach_port_type(_: ipc_space_t, _: mach_port_name_t, _: UnsafeMutablePointer<mach_port_type_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_port_type(_ task: ipc_space_t, _ name: mach_port_name_t, _ ptype: UnsafeMutablePointer<mach_port_type_t>) -> kern_return_t ``` |
| To | ``` func mach_port_type(_ task: ipc_space_t, _ name: mach_port_name_t, _ ptype: UnsafeMutablePointer<mach_port_type_t>!) -> kern_return_t ``` |

Modified mach_ports_lookup(_: task_t, _: UnsafeMutablePointer<mach_port_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_ports_lookup(_ target_task: task_t, _ init_port_set: UnsafeMutablePointer<mach_port_array_t>, _ init_port_setCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func mach_ports_lookup(_ target_task: task_t, _ init_port_set: UnsafeMutablePointer<mach_port_array_t?>!, _ init_port_setCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified mach_ports_register(_: task_t, _: mach_port_array_t!, _: mach_msg_type_number_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_ports_register(_ target_task: task_t, _ init_port_set: mach_port_array_t, _ init_port_setCnt: mach_msg_type_number_t) -> kern_return_t ``` |
| To | ``` func mach_ports_register(_ target_task: task_t, _ init_port_set: mach_port_array_t!, _ init_port_setCnt: mach_msg_type_number_t) -> kern_return_t ``` |

Modified mach_timebase_info(_: mach_timebase_info_t!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_timebase_info(_ info: mach_timebase_info_t) -> kern_return_t ``` |
| To | ``` func mach_timebase_info(_ info: mach_timebase_info_t!) -> kern_return_t ``` |

Modified mach_vm_region_info(_: vm_map_t, _: vm_address_t, _: UnsafeMutablePointer<vm_info_region_t>!, _: UnsafeMutablePointer<vm_info_object_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_vm_region_info(_ task: vm_map_t, _ address: vm_address_t, _ region: UnsafeMutablePointer<vm_info_region_t>, _ objects: UnsafeMutablePointer<vm_info_object_array_t>, _ objectsCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func mach_vm_region_info(_ task: vm_map_t, _ address: vm_address_t, _ region: UnsafeMutablePointer<vm_info_region_t>!, _ objects: UnsafeMutablePointer<vm_info_object_array_t?>!, _ objectsCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified mach_vm_region_info_64(_: vm_map_t, _: vm_address_t, _: UnsafeMutablePointer<vm_info_region_64_t>!, _: UnsafeMutablePointer<vm_info_object_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_vm_region_info_64(_ task: vm_map_t, _ address: vm_address_t, _ region: UnsafeMutablePointer<vm_info_region_64_t>, _ objects: UnsafeMutablePointer<vm_info_object_array_t>, _ objectsCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func mach_vm_region_info_64(_ task: vm_map_t, _ address: vm_address_t, _ region: UnsafeMutablePointer<vm_info_region_64_t>!, _ objects: UnsafeMutablePointer<vm_info_object_array_t?>!, _ objectsCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified mach_zone_info(_: host_priv_t, _: UnsafeMutablePointer<mach_zone_name_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: UnsafeMutablePointer<mach_zone_info_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func mach_zone_info(_ host: host_priv_t, _ names: UnsafeMutablePointer<mach_zone_name_array_t>, _ namesCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ info: UnsafeMutablePointer<mach_zone_info_array_t>, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func mach_zone_info(_ host: host_priv_t, _ names: UnsafeMutablePointer<mach_zone_name_array_t?>!, _ namesCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ info: UnsafeMutablePointer<mach_zone_info_array_t?>!, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified madvise(_: UnsafeMutableRawPointer!, _: Int, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func madvise(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32) -> Int32 ``` |
| To | ``` func madvise(_ _: UnsafeMutableRawPointer!, _ _: Int, _ _: Int32) -> Int32 ``` |

Modified malloc(_: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func malloc(_ _: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func malloc(_ __size: Int) -> UnsafeMutableRawPointer! ``` |

Modified malloc_create_zone(_: vm_size_t, _: UInt32) -> UnsafeMutablePointer<malloc_zone_t>!

|  | Declaration |
| --- | --- |
| From | ``` func malloc_create_zone(_ start_size: vm_size_t, _ flags: UInt32) -> UnsafeMutablePointer<malloc_zone_t> ``` |
| To | ``` func malloc_create_zone(_ start_size: vm_size_t, _ flags: UInt32) -> UnsafeMutablePointer<malloc_zone_t>! ``` |

Modified malloc_default_purgeable_zone() -> UnsafeMutablePointer<malloc_zone_t>!

|  | Declaration |
| --- | --- |
| From | ``` func malloc_default_purgeable_zone() -> UnsafeMutablePointer<malloc_zone_t> ``` |
| To | ``` func malloc_default_purgeable_zone() -> UnsafeMutablePointer<malloc_zone_t>! ``` |

Modified malloc_default_zone() -> UnsafeMutablePointer<malloc_zone_t>!

|  | Declaration |
| --- | --- |
| From | ``` func malloc_default_zone() -> UnsafeMutablePointer<malloc_zone_t> ``` |
| To | ``` func malloc_default_zone() -> UnsafeMutablePointer<malloc_zone_t>! ``` |

Modified malloc_destroy_zone(_: UnsafeMutablePointer<malloc_zone_t>!)

|  | Declaration |
| --- | --- |
| From | ``` func malloc_destroy_zone(_ zone: UnsafeMutablePointer<malloc_zone_t>) ``` |
| To | ``` func malloc_destroy_zone(_ zone: UnsafeMutablePointer<malloc_zone_t>!) ``` |

Modified malloc_get_all_zones(_: task_t, _: ( (task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)!, _: UnsafeMutablePointer<UnsafeMutablePointer<vm_address_t>?>!, _: UnsafeMutablePointer<UInt32>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func malloc_get_all_zones(_ task: task_t, _ reader: ((task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> kern_return_t)!, _ addresses: UnsafeMutablePointer<UnsafeMutablePointer<vm_address_t>>, _ count: UnsafeMutablePointer<UInt32>) -> kern_return_t ``` |
| To | ``` func malloc_get_all_zones(_ task: task_t, _ reader: (@escaping (task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)!, _ addresses: UnsafeMutablePointer<UnsafeMutablePointer<vm_address_t>?>!, _ count: UnsafeMutablePointer<UInt32>!) -> kern_return_t ``` |

Modified malloc_get_zone_name(_: UnsafeMutablePointer<malloc_zone_t>!) -> UnsafePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func malloc_get_zone_name(_ zone: UnsafeMutablePointer<malloc_zone_t>) -> UnsafePointer<Int8> ``` |
| To | ``` func malloc_get_zone_name(_ zone: UnsafeMutablePointer<malloc_zone_t>!) -> UnsafePointer<Int8>! ``` |

Modified malloc_make_nonpurgeable(_: UnsafeMutableRawPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func malloc_make_nonpurgeable(_ ptr: UnsafeMutablePointer<Void>) -> Int32 ``` |
| To | ``` func malloc_make_nonpurgeable(_ ptr: UnsafeMutableRawPointer!) -> Int32 ``` |

Modified malloc_make_purgeable(_: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func malloc_make_purgeable(_ ptr: UnsafeMutablePointer<Void>) ``` |
| To | ``` func malloc_make_purgeable(_ ptr: UnsafeMutableRawPointer!) ``` |

Modified malloc_set_zone_name(_: UnsafeMutablePointer<malloc_zone_t>!, _: UnsafePointer<Int8>!)

|  | Declaration |
| --- | --- |
| From | ``` func malloc_set_zone_name(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ name: UnsafePointer<Int8>) ``` |
| To | ``` func malloc_set_zone_name(_ zone: UnsafeMutablePointer<malloc_zone_t>!, _ name: UnsafePointer<Int8>!) ``` |

Modified malloc_size(_: UnsafeRawPointer!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func malloc_size(_ ptr: UnsafePointer<Void>) -> Int ``` |
| To | ``` func malloc_size(_ ptr: UnsafeRawPointer!) -> Int ``` |

Modified malloc_zone_batch_free(_: UnsafeMutablePointer<malloc_zone_t>!, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_batch_free(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ to_be_freed: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ num: UInt32) ``` |
| To | ``` func malloc_zone_batch_free(_ zone: UnsafeMutablePointer<malloc_zone_t>!, _ to_be_freed: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _ num: UInt32) ``` |

Modified malloc_zone_batch_malloc(_: UnsafeMutablePointer<malloc_zone_t>!, _: Int, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _: UInt32) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_batch_malloc(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ size: Int, _ results: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ num_requested: UInt32) -> UInt32 ``` |
| To | ``` func malloc_zone_batch_malloc(_ zone: UnsafeMutablePointer<malloc_zone_t>!, _ size: Int, _ results: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _ num_requested: UInt32) -> UInt32 ``` |

Modified malloc_zone_calloc(_: UnsafeMutablePointer<malloc_zone_t>!, _: Int, _: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_calloc(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ num_items: Int, _ size: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func malloc_zone_calloc(_ zone: UnsafeMutablePointer<malloc_zone_t>!, _ num_items: Int, _ size: Int) -> UnsafeMutableRawPointer! ``` |

Modified malloc_zone_check(_: UnsafeMutablePointer<malloc_zone_t>!) -> boolean_t

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_check(_ zone: UnsafeMutablePointer<malloc_zone_t>) -> boolean_t ``` |
| To | ``` func malloc_zone_check(_ zone: UnsafeMutablePointer<malloc_zone_t>!) -> boolean_t ``` |

Modified malloc_zone_disable_discharge_checking(_: UnsafeMutablePointer<malloc_zone_t>!)

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_disable_discharge_checking(_ zone: UnsafeMutablePointer<malloc_zone_t>) ``` |
| To | ``` func malloc_zone_disable_discharge_checking(_ zone: UnsafeMutablePointer<malloc_zone_t>!) ``` |

Modified malloc_zone_discharge(_: UnsafeMutablePointer<malloc_zone_t>!, _: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_discharge(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ memory: UnsafeMutablePointer<Void>) ``` |
| To | ``` func malloc_zone_discharge(_ zone: UnsafeMutablePointer<malloc_zone_t>!, _ memory: UnsafeMutableRawPointer!) ``` |

Modified malloc_zone_enable_discharge_checking(_: UnsafeMutablePointer<malloc_zone_t>!) -> boolean_t

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_enable_discharge_checking(_ zone: UnsafeMutablePointer<malloc_zone_t>) -> boolean_t ``` |
| To | ``` func malloc_zone_enable_discharge_checking(_ zone: UnsafeMutablePointer<malloc_zone_t>!) -> boolean_t ``` |

Modified malloc_zone_enumerate_discharged_pointers(_: UnsafeMutablePointer<malloc_zone_t>!, _: ( (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!)

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_enumerate_discharged_pointers(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ report_discharged: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)!) ``` |
| To | ``` func malloc_zone_enumerate_discharged_pointers(_ zone: UnsafeMutablePointer<malloc_zone_t>!, _ report_discharged: (@escaping (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!) ``` |

Modified malloc_zone_free(_: UnsafeMutablePointer<malloc_zone_t>!, _: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_free(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ ptr: UnsafeMutablePointer<Void>) ``` |
| To | ``` func malloc_zone_free(_ zone: UnsafeMutablePointer<malloc_zone_t>!, _ ptr: UnsafeMutableRawPointer!) ``` |

Modified malloc_zone_from_ptr(_: UnsafeRawPointer!) -> UnsafeMutablePointer<malloc_zone_t>!

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_from_ptr(_ ptr: UnsafePointer<Void>) -> UnsafeMutablePointer<malloc_zone_t> ``` |
| To | ``` func malloc_zone_from_ptr(_ ptr: UnsafeRawPointer!) -> UnsafeMutablePointer<malloc_zone_t>! ``` |

Modified malloc_zone_log(_: UnsafeMutablePointer<malloc_zone_t>!, _: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_log(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ address: UnsafeMutablePointer<Void>) ``` |
| To | ``` func malloc_zone_log(_ zone: UnsafeMutablePointer<malloc_zone_t>!, _ address: UnsafeMutableRawPointer!) ``` |

Modified malloc_zone_malloc(_: UnsafeMutablePointer<malloc_zone_t>!, _: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_malloc(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ size: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func malloc_zone_malloc(_ zone: UnsafeMutablePointer<malloc_zone_t>!, _ size: Int) -> UnsafeMutableRawPointer! ``` |

Modified malloc_zone_memalign(_: UnsafeMutablePointer<malloc_zone_t>!, _: Int, _: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_memalign(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ alignment: Int, _ size: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func malloc_zone_memalign(_ zone: UnsafeMutablePointer<malloc_zone_t>!, _ alignment: Int, _ size: Int) -> UnsafeMutableRawPointer! ``` |

Modified malloc_zone_pressure_relief(_: UnsafeMutablePointer<malloc_zone_t>!, _: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_pressure_relief(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ goal: Int) -> Int ``` |
| To | ``` func malloc_zone_pressure_relief(_ zone: UnsafeMutablePointer<malloc_zone_t>!, _ goal: Int) -> Int ``` |

Modified malloc_zone_print(_: UnsafeMutablePointer<malloc_zone_t>!, _: boolean_t)

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_print(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ verbose: boolean_t) ``` |
| To | ``` func malloc_zone_print(_ zone: UnsafeMutablePointer<malloc_zone_t>!, _ verbose: boolean_t) ``` |

Modified malloc_zone_print_ptr_info(_: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_print_ptr_info(_ ptr: UnsafeMutablePointer<Void>) ``` |
| To | ``` func malloc_zone_print_ptr_info(_ ptr: UnsafeMutableRawPointer!) ``` |

Modified malloc_zone_realloc(_: UnsafeMutablePointer<malloc_zone_t>!, _: UnsafeMutableRawPointer!, _: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_realloc(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ ptr: UnsafeMutablePointer<Void>, _ size: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func malloc_zone_realloc(_ zone: UnsafeMutablePointer<malloc_zone_t>!, _ ptr: UnsafeMutableRawPointer!, _ size: Int) -> UnsafeMutableRawPointer! ``` |

Modified malloc_zone_register(_: UnsafeMutablePointer<malloc_zone_t>!)

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_register(_ zone: UnsafeMutablePointer<malloc_zone_t>) ``` |
| To | ``` func malloc_zone_register(_ zone: UnsafeMutablePointer<malloc_zone_t>!) ``` |

Modified malloc_zone_statistics(_: UnsafeMutablePointer<malloc_zone_t>!, _: UnsafeMutablePointer<malloc_statistics_t>!)

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_statistics(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ stats: UnsafeMutablePointer<malloc_statistics_t>) ``` |
| To | ``` func malloc_zone_statistics(_ zone: UnsafeMutablePointer<malloc_zone_t>!, _ stats: UnsafeMutablePointer<malloc_statistics_t>!) ``` |

Modified malloc_zone_unregister(_: UnsafeMutablePointer<malloc_zone_t>!)

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_unregister(_ zone: UnsafeMutablePointer<malloc_zone_t>) ``` |
| To | ``` func malloc_zone_unregister(_ zone: UnsafeMutablePointer<malloc_zone_t>!) ``` |

Modified malloc_zone_valloc(_: UnsafeMutablePointer<malloc_zone_t>!, _: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_valloc(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ size: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func malloc_zone_valloc(_ zone: UnsafeMutablePointer<malloc_zone_t>!, _ size: Int) -> UnsafeMutableRawPointer! ``` |

Modified mblen(_: UnsafePointer<Int8>!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mblen(_ _: UnsafePointer<Int8>, _ _: Int) -> Int32 ``` |
| To | ``` func mblen(_ __s: UnsafePointer<Int8>!, _ __n: Int) -> Int32 ``` |

Modified mblen_l(_: UnsafePointer<Int8>!, _: Int, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mblen_l(_ _: UnsafePointer<Int8>, _ _: Int, _ _: locale_t) -> Int32 ``` |
| To | ``` func mblen_l(_ _: UnsafePointer<Int8>!, _ _: Int, _ _: locale_t!) -> Int32 ``` |

Modified mbrlen(_: UnsafePointer<Int8>!, _: Int, _: UnsafeMutablePointer<mbstate_t>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func mbrlen(_ _: UnsafePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>) -> Int ``` |
| To | ``` func mbrlen(_ _: UnsafePointer<Int8>!, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>!) -> Int ``` |

Modified mbrlen_l(_: UnsafePointer<Int8>!, _: Int, _: UnsafeMutablePointer<mbstate_t>!, _: locale_t!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func mbrlen_l(_ _: UnsafePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>, _ _: locale_t) -> Int ``` |
| To | ``` func mbrlen_l(_ _: UnsafePointer<Int8>!, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>!, _ _: locale_t!) -> Int ``` |

Modified mbrtowc(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<Int8>!, _: Int, _: UnsafeMutablePointer<mbstate_t>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func mbrtowc(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>) -> Int ``` |
| To | ``` func mbrtowc(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<Int8>!, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>!) -> Int ``` |

Modified mbrtowc_l(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<Int8>!, _: Int, _: UnsafeMutablePointer<mbstate_t>!, _: locale_t!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func mbrtowc_l(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>, _ _: locale_t) -> Int ``` |
| To | ``` func mbrtowc_l(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<Int8>!, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>!, _ _: locale_t!) -> Int ``` |

Modified mbsinit(_: UnsafePointer<mbstate_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mbsinit(_ _: UnsafePointer<mbstate_t>) -> Int32 ``` |
| To | ``` func mbsinit(_ _: UnsafePointer<mbstate_t>!) -> Int32 ``` |

Modified mbsinit_l(_: UnsafePointer<mbstate_t>!, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mbsinit_l(_ _: UnsafePointer<mbstate_t>, _ _: locale_t) -> Int32 ``` |
| To | ``` func mbsinit_l(_ _: UnsafePointer<mbstate_t>!, _ _: locale_t!) -> Int32 ``` |

Modified mbsnrtowcs(_: UnsafeMutablePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _: Int, _: Int, _: UnsafeMutablePointer<mbstate_t>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func mbsnrtowcs(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>) -> Int ``` |
| To | ``` func mbsnrtowcs(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>!) -> Int ``` |

Modified mbsnrtowcs_l(_: UnsafeMutablePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _: Int, _: Int, _: UnsafeMutablePointer<mbstate_t>!, _: locale_t!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func mbsnrtowcs_l(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>, _ _: locale_t) -> Int ``` |
| To | ``` func mbsnrtowcs_l(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>!, _ _: locale_t!) -> Int ``` |

Modified mbsrtowcs(_: UnsafeMutablePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _: Int, _: UnsafeMutablePointer<mbstate_t>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func mbsrtowcs(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>) -> Int ``` |
| To | ``` func mbsrtowcs(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>!) -> Int ``` |

Modified mbsrtowcs_l(_: UnsafeMutablePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _: Int, _: UnsafeMutablePointer<mbstate_t>!, _: locale_t!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func mbsrtowcs_l(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>, _ _: locale_t) -> Int ``` |
| To | ``` func mbsrtowcs_l(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafeMutablePointer<UnsafePointer<Int8>?>!, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>!, _ _: locale_t!) -> Int ``` |

Modified mbstowcs(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<Int8>!, _: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func mbstowcs(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<Int8>, _ _: Int) -> Int ``` |
| To | ``` func mbstowcs(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<Int8>!, _ _: Int) -> Int ``` |

Modified mbstowcs_l(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<Int8>!, _: Int, _: locale_t!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func mbstowcs_l(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<Int8>, _ _: Int, _ _: locale_t) -> Int ``` |
| To | ``` func mbstowcs_l(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<Int8>!, _ _: Int, _ _: locale_t!) -> Int ``` |

Modified mbtowc(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<Int8>!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mbtowc(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<Int8>, _ _: Int) -> Int32 ``` |
| To | ``` func mbtowc(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<Int8>!, _ _: Int) -> Int32 ``` |

Modified mbtowc_l(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<Int8>!, _: Int, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mbtowc_l(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<Int8>, _ _: Int, _ _: locale_t) -> Int32 ``` |
| To | ``` func mbtowc_l(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<Int8>!, _ _: Int, _ _: locale_t!) -> Int32 ``` |

Modified mcontext_t

|  | Declaration |
| --- | --- |
| From | ``` typealias mcontext_t = UnsafeMutablePointer<__darwin_mcontext32> ``` |
| To | ``` typealias mcontext_t = UnsafeMutablePointer<__darwin_mcontext64> ``` |

Modified memccpy(_: UnsafeMutableRawPointer!, _: UnsafeRawPointer!, _: Int32, _: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func memccpy(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int32, _ _: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func memccpy(_ __dst: UnsafeMutableRawPointer!, _ __src: UnsafeRawPointer!, _ __c: Int32, _ __n: Int) -> UnsafeMutableRawPointer! ``` |

Modified memchr(_: UnsafeRawPointer!, _: Int32, _: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func memchr(_ _: UnsafePointer<Void>, _ _: Int32, _ _: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func memchr(_ __s: UnsafeRawPointer!, _ __c: Int32, _ __n: Int) -> UnsafeMutableRawPointer! ``` |

Modified memcmp(_: UnsafeRawPointer!, _: UnsafeRawPointer!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func memcmp(_ _: UnsafePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int) -> Int32 ``` |
| To | ``` func memcmp(_ __s1: UnsafeRawPointer!, _ __s2: UnsafeRawPointer!, _ __n: Int) -> Int32 ``` |

Modified memcpy(_: UnsafeMutableRawPointer!, _: UnsafeRawPointer!, _: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func memcpy(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func memcpy(_ __dst: UnsafeMutableRawPointer!, _ __src: UnsafeRawPointer!, _ __n: Int) -> UnsafeMutableRawPointer! ``` |

Modified memmem(_: UnsafeRawPointer!, _: Int, _: UnsafeRawPointer!, _: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func memmem(_ _: UnsafePointer<Void>, _ _: Int, _ _: UnsafePointer<Void>, _ _: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func memmem(_ __big: UnsafeRawPointer!, _ __big_len: Int, _ __little: UnsafeRawPointer!, _ __little_len: Int) -> UnsafeMutableRawPointer! ``` |

Modified memmove(_: UnsafeMutableRawPointer!, _: UnsafeRawPointer!, _: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func memmove(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func memmove(_ __dst: UnsafeMutableRawPointer!, _ __src: UnsafeRawPointer!, _ __len: Int) -> UnsafeMutableRawPointer! ``` |

Modified memory_reader_t

|  | Declaration |
| --- | --- |
| From | ``` typealias memory_reader_t = (task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> kern_return_t ``` |
| To | ``` typealias memory_reader_t = (task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t ``` |

Modified memset(_: UnsafeMutableRawPointer!, _: Int32, _: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func memset(_ _: UnsafeMutablePointer<Void>, _ _: Int32, _ _: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func memset(_ __b: UnsafeMutableRawPointer!, _ __c: Int32, _ __len: Int) -> UnsafeMutableRawPointer! ``` |

Modified memset_pattern16(_: UnsafeMutableRawPointer!, _: UnsafeRawPointer!, _: Int)

|  | Declaration |
| --- | --- |
| From | ``` func memset_pattern16(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int) ``` |
| To | ``` func memset_pattern16(_ __b: UnsafeMutableRawPointer!, _ __pattern16: UnsafeRawPointer!, _ __len: Int) ``` |

Modified memset_pattern4(_: UnsafeMutableRawPointer!, _: UnsafeRawPointer!, _: Int)

|  | Declaration |
| --- | --- |
| From | ``` func memset_pattern4(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int) ``` |
| To | ``` func memset_pattern4(_ __b: UnsafeMutableRawPointer!, _ __pattern4: UnsafeRawPointer!, _ __len: Int) ``` |

Modified memset_pattern8(_: UnsafeMutableRawPointer!, _: UnsafeRawPointer!, _: Int)

|  | Declaration |
| --- | --- |
| From | ``` func memset_pattern8(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int) ``` |
| To | ``` func memset_pattern8(_ __b: UnsafeMutableRawPointer!, _ __pattern8: UnsafeRawPointer!, _ __len: Int) ``` |

Modified memset_s(_: UnsafeMutableRawPointer!, _: Int, _: Int32, _: Int) -> errno_t

|  | Declaration |
| --- | --- |
| From | ``` func memset_s(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32, _ _: Int) -> errno_t ``` |
| To | ``` func memset_s(_ __s: UnsafeMutableRawPointer!, _ __smax: Int, _ __c: Int32, _ __n: Int) -> errno_t ``` |

Modified mergesort(_: UnsafeMutableRawPointer!, _: Int, _: Int, _: (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mergesort(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> Int32 ``` |
| To | ``` func mergesort(_ __base: UnsafeMutableRawPointer!, _ __nel: Int, _ __width: Int, _ __compar: @escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) -> Int32 ``` |

Modified mergesort_b(_: UnsafeMutableRawPointer!, _: Int, _: Int, _: (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mergesort_b(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> Int32 ``` |
| To | ``` func mergesort_b(_ __base: UnsafeMutableRawPointer!, _ __nel: Int, _ __width: Int, _ __compar: @escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) -> Int32 ``` |

Modified mig_allocate(_: UnsafeMutablePointer<vm_address_t>!, _: vm_size_t)

|  | Declaration |
| --- | --- |
| From | ``` func mig_allocate(_ _: UnsafeMutablePointer<vm_address_t>, _ _: vm_size_t) ``` |
| To | ``` func mig_allocate(_ _: UnsafeMutablePointer<vm_address_t>!, _ _: vm_size_t) ``` |

Modified mig_reply_setup(_: UnsafeMutablePointer<mach_msg_header_t>!, _: UnsafeMutablePointer<mach_msg_header_t>!)

|  | Declaration |
| --- | --- |
| From | ``` func mig_reply_setup(_ _: UnsafeMutablePointer<mach_msg_header_t>, _ _: UnsafeMutablePointer<mach_msg_header_t>) ``` |
| To | ``` func mig_reply_setup(_ _: UnsafeMutablePointer<mach_msg_header_t>!, _ _: UnsafeMutablePointer<mach_msg_header_t>!) ``` |

Modified mig_routine_t

|  | Declaration |
| --- | --- |
| From | ``` typealias mig_routine_t = mig_stub_routine_t ``` |
| To | ``` typealias mig_routine_t = Darwin.mig_stub_routine_t ``` |

Modified mig_server_routine_t

|  | Declaration |
| --- | --- |
| From | ``` typealias mig_server_routine_t = (UnsafeMutablePointer<mach_msg_header_t>) -> mig_routine_t! ``` |
| To | ``` typealias mig_server_routine_t = (UnsafeMutablePointer<mach_msg_header_t>?) -> Darwin.mig_routine_t? ``` |

Modified mig_strncpy(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mig_strncpy(_ dest: UnsafeMutablePointer<Int8>, _ src: UnsafePointer<Int8>, _ len: Int32) -> Int32 ``` |
| To | ``` func mig_strncpy(_ dest: UnsafeMutablePointer<Int8>!, _ src: UnsafePointer<Int8>!, _ len: Int32) -> Int32 ``` |

Modified mig_stub_routine_t

|  | Declaration |
| --- | --- |
| From | ``` typealias mig_stub_routine_t = (UnsafeMutablePointer<mach_msg_header_t>, UnsafeMutablePointer<mach_msg_header_t>) -> Void ``` |
| To | ``` typealias mig_stub_routine_t = (UnsafeMutablePointer<mach_msg_header_t>?, UnsafeMutablePointer<mach_msg_header_t>?) -> Swift.Void ``` |

Modified mincore(_: UnsafeRawPointer!, _: Int, _: UnsafeMutablePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mincore(_ _: UnsafePointer<Void>, _ _: Int, _ _: UnsafeMutablePointer<Int8>) -> Int32 ``` |
| To | ``` func mincore(_ _: UnsafeRawPointer!, _ _: Int, _ _: UnsafeMutablePointer<Int8>!) -> Int32 ``` |

Modified minherit(_: UnsafeMutableRawPointer!, _: Int, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func minherit(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32) -> Int32 ``` |
| To | ``` func minherit(_ _: UnsafeMutableRawPointer!, _ _: Int, _ _: Int32) -> Int32 ``` |

Modified mkdir(_: UnsafePointer<Int8>!, _: mode_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mkdir(_ _: UnsafePointer<Int8>, _ _: mode_t) -> Int32 ``` |
| To | ``` func mkdir(_ _: UnsafePointer<Int8>!, _ _: mode_t) -> Int32 ``` |

Modified mkdirat(_: Int32, _: UnsafePointer<Int8>!, _: mode_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mkdirat(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: mode_t) -> Int32 ``` |
| To | ``` func mkdirat(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: mode_t) -> Int32 ``` |

Modified mkdirx_np(_: UnsafePointer<Int8>!, _: filesec_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mkdirx_np(_ _: UnsafePointer<Int8>, _ _: filesec_t) -> Int32 ``` |
| To | ``` func mkdirx_np(_ _: UnsafePointer<Int8>!, _ _: filesec_t!) -> Int32 ``` |

Modified mkdtemp(_: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func mkdtemp(_ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func mkdtemp(_ _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified mkfifo(_: UnsafePointer<Int8>!, _: mode_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mkfifo(_ _: UnsafePointer<Int8>, _ _: mode_t) -> Int32 ``` |
| To | ``` func mkfifo(_ _: UnsafePointer<Int8>!, _ _: mode_t) -> Int32 ``` |

Modified mkfifox_np(_: UnsafePointer<Int8>!, _: filesec_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mkfifox_np(_ _: UnsafePointer<Int8>, _ _: filesec_t) -> Int32 ``` |
| To | ``` func mkfifox_np(_ _: UnsafePointer<Int8>!, _ _: filesec_t!) -> Int32 ``` |

Modified mknod(_: UnsafePointer<Int8>!, _: mode_t, _: dev_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mknod(_ _: UnsafePointer<Int8>, _ _: mode_t, _ _: dev_t) -> Int32 ``` |
| To | ``` func mknod(_ _: UnsafePointer<Int8>!, _ _: mode_t, _ _: dev_t) -> Int32 ``` |

Modified mkpath_np(_: UnsafePointer<Int8>!, _: mode_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mkpath_np(_ path: UnsafePointer<Int8>, _ omode: mode_t) -> Int32 ``` |
| To | ``` func mkpath_np(_ path: UnsafePointer<Int8>!, _ omode: mode_t) -> Int32 ``` |

Modified mkstemp(_: UnsafeMutablePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mkstemp(_ _: UnsafeMutablePointer<Int8>) -> Int32 ``` |
| To | ``` func mkstemp(_ _: UnsafeMutablePointer<Int8>!) -> Int32 ``` |

Modified mkstemps(_: UnsafeMutablePointer<Int8>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mkstemps(_ _: UnsafeMutablePointer<Int8>, _ _: Int32) -> Int32 ``` |
| To | ``` func mkstemps(_ _: UnsafeMutablePointer<Int8>!, _ _: Int32) -> Int32 ``` |

Modified mktemp(_: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func mktemp(_ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func mktemp(_ _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified mktime(_: UnsafeMutablePointer<tm>!) -> time_t

|  | Declaration |
| --- | --- |
| From | ``` func mktime(_ _: UnsafeMutablePointer<tm>) -> time_t ``` |
| To | ``` func mktime(_ _: UnsafeMutablePointer<tm>!) -> time_t ``` |

Modified mlock(_: UnsafeRawPointer!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mlock(_ _: UnsafePointer<Void>, _ _: Int) -> Int32 ``` |
| To | ``` func mlock(_ _: UnsafeRawPointer!, _ _: Int) -> Int32 ``` |

Modified mmap(_: UnsafeMutableRawPointer!, _: Int, _: Int32, _: Int32, _: Int32, _: off_t) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func mmap(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32, _ _: Int32, _ _: Int32, _ _: off_t) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func mmap(_ _: UnsafeMutableRawPointer!, _ _: Int, _ _: Int32, _ _: Int32, _ _: Int32, _ _: off_t) -> UnsafeMutableRawPointer! ``` |

Modified modf(_: Float) -> (Float, Float)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func modf(_ value: Float) -> (Float, Float) ``` |
| To | ``` func modf(_ value: Float) -> (Float, Float) ``` |

Modified modf(_: Double) -> (Double, Double)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func modf(_ value: Double) -> (Double, Double) ``` |
| To | ``` func modf(_ value: Double) -> (Double, Double) ``` |

Modified modf(_: Double, _: UnsafeMutablePointer<Double>!) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func modf(_ _: Double, _ _: UnsafeMutablePointer<Double>) -> Double ``` |
| To | ``` func modf(_ _: Double, _ _: UnsafeMutablePointer<Double>!) -> Double ``` |

Modified modff(_: Float, _: UnsafeMutablePointer<Float>!) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func modff(_ _: Float, _ _: UnsafeMutablePointer<Float>) -> Float ``` |
| To | ``` func modff(_ _: Float, _ _: UnsafeMutablePointer<Float>!) -> Float ``` |

Modified mount(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int32, _: UnsafeMutableRawPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mount(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int32, _ _: UnsafeMutablePointer<Void>) -> Int32 ``` |
| To | ``` func mount(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: Int32, _ _: UnsafeMutableRawPointer!) -> Int32 ``` |

Modified mount_t

|  | Declaration |
| --- | --- |
| From | ``` typealias mount_t = COpaquePointer ``` |
| To | ``` typealias mount_t = OpaquePointer ``` |

Modified mprotect(_: UnsafeMutableRawPointer!, _: Int, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mprotect(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32) -> Int32 ``` |
| To | ``` func mprotect(_ _: UnsafeMutableRawPointer!, _ _: Int, _ _: Int32) -> Int32 ``` |

Modified msgctl(_: Int32, _: Int32, _: UnsafeMutablePointer<__msqid_ds_new>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func msgctl(_ _: Int32, _ _: Int32, _ _: UnsafeMutablePointer<__msqid_ds_new>) -> Int32 ``` |
| To | ``` func msgctl(_ _: Int32, _ _: Int32, _ _: UnsafeMutablePointer<__msqid_ds_new>!) -> Int32 ``` |

Modified msgrcv(_: Int32, _: UnsafeMutableRawPointer!, _: Int, _: Int, _: Int32) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func msgrcv(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: Int32) -> Int ``` |
| To | ``` func msgrcv(_ _: Int32, _ _: UnsafeMutableRawPointer!, _ _: Int, _ _: Int, _ _: Int32) -> Int ``` |

Modified msgsnd(_: Int32, _: UnsafeRawPointer!, _: Int, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func msgsnd(_ _: Int32, _ _: UnsafePointer<Void>, _ _: Int, _ _: Int32) -> Int32 ``` |
| To | ``` func msgsnd(_ _: Int32, _ _: UnsafeRawPointer!, _ _: Int, _ _: Int32) -> Int32 ``` |

Modified msync(_: UnsafeMutableRawPointer!, _: Int, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func msync(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32) -> Int32 ``` |
| To | ``` func msync(_ _: UnsafeMutableRawPointer!, _ _: Int, _ _: Int32) -> Int32 ``` |

Modified munlock(_: UnsafeRawPointer!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func munlock(_ _: UnsafePointer<Void>, _ _: Int) -> Int32 ``` |
| To | ``` func munlock(_ _: UnsafeRawPointer!, _ _: Int) -> Int32 ``` |

Modified munmap(_: UnsafeMutableRawPointer!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func munmap(_ _: UnsafeMutablePointer<Void>, _ _: Int) -> Int32 ``` |
| To | ``` func munmap(_ _: UnsafeMutableRawPointer!, _ _: Int) -> Int32 ``` |

Modified nan(_: UnsafePointer<Int8>!) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func nan(_ _: UnsafePointer<Int8>) -> Double ``` |
| To | ``` func nan(_ _: UnsafePointer<Int8>!) -> Double ``` |

Modified nan(_: String) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func nan(_ tag: String) -> Float ``` |
| To | ``` func nan(_ tag: String) -> Float ``` |

Modified nanf(_: UnsafePointer<Int8>!) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func nanf(_ _: UnsafePointer<Int8>) -> Float ``` |
| To | ``` func nanf(_ _: UnsafePointer<Int8>!) -> Float ``` |

Modified nanosleep(_: UnsafePointer<timespec>!, _: UnsafeMutablePointer<timespec>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func nanosleep(_ _: UnsafePointer<timespec>, _ _: UnsafeMutablePointer<timespec>) -> Int32 ``` |
| To | ``` func nanosleep(_ __rqtp: UnsafePointer<timespec>!, _ __rmtp: UnsafeMutablePointer<timespec>!) -> Int32 ``` |

Modified nearbyint(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func nearbyint(_ x: Float) -> Float ``` |
| To | ``` func nearbyint(_ x: Float) -> Float ``` |

Modified nearbyint(_: Double) -> Double

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func nearbyint(_ x: Double) -> Double ``` |
| To | ``` func nearbyint(_ x: Double) -> Double ``` |

Modified newlocale(_: Int32, _: UnsafePointer<Int8>!, _: locale_t!) -> locale_t!

|  | Declaration |
| --- | --- |
| From | ``` func newlocale(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: locale_t) -> locale_t ``` |
| To | ``` func newlocale(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: locale_t!) -> locale_t! ``` |

Modified nextafter(_: Float, _: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func nextafter(_ lhs: Float, _ rhs: Float) -> Float ``` |
| To | ``` func nextafter(_ lhs: Float, _ rhs: Float) -> Float ``` |

Modified nextwctype_l(_: wint_t, _: wctype_t, _: locale_t!) -> wint_t

|  | Declaration |
| --- | --- |
| From | ``` func nextwctype_l(_ _: wint_t, _ _: wctype_t, _ _: locale_t) -> wint_t ``` |
| To | ``` func nextwctype_l(_ _: wint_t, _ _: wctype_t, _ _: locale_t!) -> wint_t ``` |

Modified nfssvc(_: Int32, _: UnsafeMutableRawPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func nfssvc(_ _: Int32, _ _: UnsafeMutablePointer<Void>) -> Int32 ``` |
| To | ``` func nfssvc(_ _: Int32, _ _: UnsafeMutableRawPointer!) -> Int32 ``` |

Modified nftw(_: UnsafePointer<Int8>!, _: ( (UnsafePointer<Int8>?, UnsafePointer<stat>?, Int32, UnsafeMutablePointer<FTW>?) -> Int32)!, _: Int32, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func nftw(_ _: UnsafePointer<Int8>, _ _: ((UnsafePointer<Int8>, UnsafePointer<stat>, Int32, UnsafeMutablePointer<FTW>) -> Int32)!, _ _: Int32, _ _: Int32) -> Int32 ``` |
| To | ``` func nftw(_ _: UnsafePointer<Int8>!, _ _: (@escaping (UnsafePointer<Int8>?, UnsafePointer<stat>?, Int32, UnsafeMutablePointer<FTW>?) -> Int32)!, _ _: Int32, _ _: Int32) -> Int32 ``` |

Modified nl_langinfo(_: nl_item) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func nl_langinfo(_ _: nl_item) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func nl_langinfo(_ _: nl_item) -> UnsafeMutablePointer<Int8>! ``` |

Modified nl_langinfo_l(_: nl_item, _: locale_t!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func nl_langinfo_l(_ _: nl_item, _ _: locale_t) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func nl_langinfo_l(_ _: nl_item, _ _: locale_t!) -> UnsafeMutablePointer<Int8>! ``` |

Modified open(_: UnsafePointer<CChar>, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func open(_ path: UnsafePointer<CChar>, _ oflag: CInt) -> CInt ``` |
| To | ``` func open(_ path: UnsafePointer<CChar>, _ oflag: Int32) -> Int32 ``` |

Modified open(_: UnsafePointer<CChar>, _: Int32, _: mode_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func open(_ path: UnsafePointer<CChar>, _ oflag: CInt, _ mode: mode_t) -> CInt ``` |
| To | ``` func open(_ path: UnsafePointer<CChar>, _ oflag: Int32, _ mode: mode_t) -> Int32 ``` |

Modified openat(_: Int32, _: UnsafePointer<CChar>, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func openat(_ fd: CInt, _ path: UnsafePointer<CChar>, _ oflag: CInt) -> CInt ``` |
| To | ``` func openat(_ fd: Int32, _ path: UnsafePointer<CChar>, _ oflag: Int32) -> Int32 ``` |

Modified openat(_: Int32, _: UnsafePointer<CChar>, _: Int32, _: mode_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func openat(_ fd: CInt, _ path: UnsafePointer<CChar>, _ oflag: CInt, _ mode: mode_t) -> CInt ``` |
| To | ``` func openat(_ fd: Int32, _ path: UnsafePointer<CChar>, _ oflag: Int32, _ mode: mode_t) -> Int32 ``` |

Modified opendev(_: UnsafeMutablePointer<Int8>!, _: Int32, _: Int32, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func opendev(_ _: UnsafeMutablePointer<Int8>, _ _: Int32, _ _: Int32, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int32 ``` |
| To | ``` func opendev(_ _: UnsafeMutablePointer<Int8>!, _ _: Int32, _ _: Int32, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Int32 ``` |

Modified opendir(_: UnsafePointer<Int8>!) -> UnsafeMutablePointer<DIR>!

|  | Declaration |
| --- | --- |
| From | ``` func opendir(_ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<DIR> ``` |
| To | ``` func opendir(_ _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<DIR>! ``` |

Modified openlog(_: UnsafePointer<Int8>!, _: Int32, _: Int32)

|  | Declaration |
| --- | --- |
| From | ``` func openlog(_ _: UnsafePointer<Int8>, _ _: Int32, _ _: Int32) ``` |
| To | ``` func openlog(_ _: UnsafePointer<Int8>!, _ _: Int32, _ _: Int32) ``` |

Modified openpty(_: UnsafeMutablePointer<Int32>!, _: UnsafeMutablePointer<Int32>!, _: UnsafeMutablePointer<Int8>!, _: UnsafeMutablePointer<termios>!, _: UnsafeMutablePointer<winsize>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func openpty(_ _: UnsafeMutablePointer<Int32>, _ _: UnsafeMutablePointer<Int32>, _ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<termios>, _ _: UnsafeMutablePointer<winsize>) -> Int32 ``` |
| To | ``` func openpty(_ _: UnsafeMutablePointer<Int32>!, _ _: UnsafeMutablePointer<Int32>!, _ _: UnsafeMutablePointer<Int8>!, _ _: UnsafeMutablePointer<termios>!, _ _: UnsafeMutablePointer<winsize>!) -> Int32 ``` |

Modified openx_np(_: UnsafePointer<Int8>!, _: Int32, _: filesec_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func openx_np(_ _: UnsafePointer<Int8>, _ _: Int32, _ _: filesec_t) -> Int32 ``` |
| To | ``` func openx_np(_ _: UnsafePointer<Int8>!, _ _: Int32, _ _: filesec_t!) -> Int32 ``` |

Modified optarg

|  | Declaration |
| --- | --- |
| From | ``` var optarg: UnsafeMutablePointer<Int8> ``` |
| To | ``` var optarg: UnsafeMutablePointer<Int8>! ``` |

Modified OSAtomicAdd32(_: Int32, _: UnsafeMutablePointer<Int32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicAdd32(_ __theAmount: Int32, _ __theValue: UnsafeMutablePointer<Int32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicAdd32(_ __theAmount: Int32, _ __theValue: UnsafeMutablePointer<Int32>!) -> Int32 ``` | iOS 10.0 |

Modified OSAtomicAdd32Barrier(_: Int32, _: UnsafeMutablePointer<Int32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicAdd32Barrier(_ __theAmount: Int32, _ __theValue: UnsafeMutablePointer<Int32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicAdd32Barrier(_ __theAmount: Int32, _ __theValue: UnsafeMutablePointer<Int32>!) -> Int32 ``` | iOS 10.0 |

Modified OSAtomicAdd64(_: Int64, _: UnsafeMutablePointer<OSAtomic_int64_aligned64_t>!) -> Int64

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicAdd64(_ __theAmount: Int64, _ __theValue: UnsafeMutablePointer<Int64>) -> Int64 ``` | -- |
| To | ``` func OSAtomicAdd64(_ __theAmount: Int64, _ __theValue: UnsafeMutablePointer<OSAtomic_int64_aligned64_t>!) -> Int64 ``` | iOS 10.0 |

Modified OSAtomicAdd64Barrier(_: Int64, _: UnsafeMutablePointer<OSAtomic_int64_aligned64_t>!) -> Int64

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicAdd64Barrier(_ __theAmount: Int64, _ __theValue: UnsafeMutablePointer<Int64>) -> Int64 ``` | -- |
| To | ``` func OSAtomicAdd64Barrier(_ __theAmount: Int64, _ __theValue: UnsafeMutablePointer<OSAtomic_int64_aligned64_t>!) -> Int64 ``` | iOS 10.0 |

Modified OSAtomicAnd32(_: UInt32, _: UnsafeMutablePointer<UInt32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicAnd32(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicAnd32(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>!) -> Int32 ``` | iOS 10.0 |

Modified OSAtomicAnd32Barrier(_: UInt32, _: UnsafeMutablePointer<UInt32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicAnd32Barrier(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicAnd32Barrier(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>!) -> Int32 ``` | iOS 10.0 |

Modified OSAtomicAnd32Orig(_: UInt32, _: UnsafeMutablePointer<UInt32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicAnd32Orig(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicAnd32Orig(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>!) -> Int32 ``` | iOS 10.0 |

Modified OSAtomicAnd32OrigBarrier(_: UInt32, _: UnsafeMutablePointer<UInt32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicAnd32OrigBarrier(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicAnd32OrigBarrier(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>!) -> Int32 ``` | iOS 10.0 |

Modified OSAtomicCompareAndSwap32(_: Int32, _: Int32, _: UnsafeMutablePointer<Int32>!) -> Bool

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicCompareAndSwap32(_ __oldValue: Int32, _ __newValue: Int32, _ __theValue: UnsafeMutablePointer<Int32>) -> Bool ``` | -- |
| To | ``` func OSAtomicCompareAndSwap32(_ __oldValue: Int32, _ __newValue: Int32, _ __theValue: UnsafeMutablePointer<Int32>!) -> Bool ``` | iOS 10.0 |

Modified OSAtomicCompareAndSwap32Barrier(_: Int32, _: Int32, _: UnsafeMutablePointer<Int32>!) -> Bool

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicCompareAndSwap32Barrier(_ __oldValue: Int32, _ __newValue: Int32, _ __theValue: UnsafeMutablePointer<Int32>) -> Bool ``` | -- |
| To | ``` func OSAtomicCompareAndSwap32Barrier(_ __oldValue: Int32, _ __newValue: Int32, _ __theValue: UnsafeMutablePointer<Int32>!) -> Bool ``` | iOS 10.0 |

Modified OSAtomicCompareAndSwap64(_: Int64, _: Int64, _: UnsafeMutablePointer<OSAtomic_int64_aligned64_t>!) -> Bool

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicCompareAndSwap64(_ __oldValue: Int64, _ __newValue: Int64, _ __theValue: UnsafeMutablePointer<Int64>) -> Bool ``` | -- |
| To | ``` func OSAtomicCompareAndSwap64(_ __oldValue: Int64, _ __newValue: Int64, _ __theValue: UnsafeMutablePointer<OSAtomic_int64_aligned64_t>!) -> Bool ``` | iOS 10.0 |

Modified OSAtomicCompareAndSwap64Barrier(_: Int64, _: Int64, _: UnsafeMutablePointer<OSAtomic_int64_aligned64_t>!) -> Bool

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicCompareAndSwap64Barrier(_ __oldValue: Int64, _ __newValue: Int64, _ __theValue: UnsafeMutablePointer<Int64>) -> Bool ``` | -- |
| To | ``` func OSAtomicCompareAndSwap64Barrier(_ __oldValue: Int64, _ __newValue: Int64, _ __theValue: UnsafeMutablePointer<OSAtomic_int64_aligned64_t>!) -> Bool ``` | iOS 10.0 |

Modified OSAtomicCompareAndSwapInt(_: Int32, _: Int32, _: UnsafeMutablePointer<Int32>!) -> Bool

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicCompareAndSwapInt(_ __oldValue: Int32, _ __newValue: Int32, _ __theValue: UnsafeMutablePointer<Int32>) -> Bool ``` | -- |
| To | ``` func OSAtomicCompareAndSwapInt(_ __oldValue: Int32, _ __newValue: Int32, _ __theValue: UnsafeMutablePointer<Int32>!) -> Bool ``` | iOS 10.0 |

Modified OSAtomicCompareAndSwapIntBarrier(_: Int32, _: Int32, _: UnsafeMutablePointer<Int32>!) -> Bool

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicCompareAndSwapIntBarrier(_ __oldValue: Int32, _ __newValue: Int32, _ __theValue: UnsafeMutablePointer<Int32>) -> Bool ``` | -- |
| To | ``` func OSAtomicCompareAndSwapIntBarrier(_ __oldValue: Int32, _ __newValue: Int32, _ __theValue: UnsafeMutablePointer<Int32>!) -> Bool ``` | iOS 10.0 |

Modified OSAtomicCompareAndSwapLong(_: Int, _: Int, _: UnsafeMutablePointer<Int>!) -> Bool

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicCompareAndSwapLong(_ __oldValue: Int, _ __newValue: Int, _ __theValue: UnsafeMutablePointer<Int>) -> Bool ``` | -- |
| To | ``` func OSAtomicCompareAndSwapLong(_ __oldValue: Int, _ __newValue: Int, _ __theValue: UnsafeMutablePointer<Int>!) -> Bool ``` | iOS 10.0 |

Modified OSAtomicCompareAndSwapLongBarrier(_: Int, _: Int, _: UnsafeMutablePointer<Int>!) -> Bool

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicCompareAndSwapLongBarrier(_ __oldValue: Int, _ __newValue: Int, _ __theValue: UnsafeMutablePointer<Int>) -> Bool ``` | -- |
| To | ``` func OSAtomicCompareAndSwapLongBarrier(_ __oldValue: Int, _ __newValue: Int, _ __theValue: UnsafeMutablePointer<Int>!) -> Bool ``` | iOS 10.0 |

Modified OSAtomicCompareAndSwapPtr(_: UnsafeMutableRawPointer!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> Bool

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicCompareAndSwapPtr(_ __oldValue: UnsafeMutablePointer<Void>, _ __newValue: UnsafeMutablePointer<Void>, _ __theValue: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Bool ``` | -- |
| To | ``` func OSAtomicCompareAndSwapPtr(_ __oldValue: UnsafeMutableRawPointer!, _ __newValue: UnsafeMutableRawPointer!, _ __theValue: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> Bool ``` | iOS 10.0 |

Modified OSAtomicCompareAndSwapPtrBarrier(_: UnsafeMutableRawPointer!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> Bool

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicCompareAndSwapPtrBarrier(_ __oldValue: UnsafeMutablePointer<Void>, _ __newValue: UnsafeMutablePointer<Void>, _ __theValue: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Bool ``` | -- |
| To | ``` func OSAtomicCompareAndSwapPtrBarrier(_ __oldValue: UnsafeMutableRawPointer!, _ __newValue: UnsafeMutableRawPointer!, _ __theValue: UnsafeMutablePointer<UnsafeMutableRawPointer?>!) -> Bool ``` | iOS 10.0 |

Modified OSAtomicDecrement32(_: UnsafeMutablePointer<Int32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicDecrement32(_ __theValue: UnsafeMutablePointer<Int32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicDecrement32(_ __theValue: UnsafeMutablePointer<Int32>!) -> Int32 ``` | iOS 10.0 |

Modified OSAtomicDecrement32Barrier(_: UnsafeMutablePointer<Int32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicDecrement32Barrier(_ __theValue: UnsafeMutablePointer<Int32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicDecrement32Barrier(_ __theValue: UnsafeMutablePointer<Int32>!) -> Int32 ``` | iOS 10.0 |

Modified OSAtomicDecrement64(_: UnsafeMutablePointer<OSAtomic_int64_aligned64_t>!) -> Int64

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicDecrement64(_ __theValue: UnsafeMutablePointer<Int64>) -> Int64 ``` | -- |
| To | ``` func OSAtomicDecrement64(_ __theValue: UnsafeMutablePointer<OSAtomic_int64_aligned64_t>!) -> Int64 ``` | iOS 10.0 |

Modified OSAtomicDecrement64Barrier(_: UnsafeMutablePointer<OSAtomic_int64_aligned64_t>!) -> Int64

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicDecrement64Barrier(_ __theValue: UnsafeMutablePointer<Int64>) -> Int64 ``` | -- |
| To | ``` func OSAtomicDecrement64Barrier(_ __theValue: UnsafeMutablePointer<OSAtomic_int64_aligned64_t>!) -> Int64 ``` | iOS 10.0 |

Modified OSAtomicDequeue(_: OpaquePointer!, _: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func OSAtomicDequeue(_ __list: COpaquePointer, _ __offset: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func OSAtomicDequeue(_ __list: OpaquePointer!, _ __offset: Int) -> UnsafeMutableRawPointer! ``` |

Modified OSAtomicEnqueue(_: OpaquePointer!, _: UnsafeMutableRawPointer!, _: Int)

|  | Declaration |
| --- | --- |
| From | ``` func OSAtomicEnqueue(_ __list: COpaquePointer, _ __new: UnsafeMutablePointer<Void>, _ __offset: Int) ``` |
| To | ``` func OSAtomicEnqueue(_ __list: OpaquePointer!, _ __new: UnsafeMutableRawPointer!, _ __offset: Int) ``` |

Modified OSAtomicIncrement32(_: UnsafeMutablePointer<Int32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicIncrement32(_ __theValue: UnsafeMutablePointer<Int32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicIncrement32(_ __theValue: UnsafeMutablePointer<Int32>!) -> Int32 ``` | iOS 10.0 |

Modified OSAtomicIncrement32Barrier(_: UnsafeMutablePointer<Int32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicIncrement32Barrier(_ __theValue: UnsafeMutablePointer<Int32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicIncrement32Barrier(_ __theValue: UnsafeMutablePointer<Int32>!) -> Int32 ``` | iOS 10.0 |

Modified OSAtomicIncrement64(_: UnsafeMutablePointer<OSAtomic_int64_aligned64_t>!) -> Int64

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicIncrement64(_ __theValue: UnsafeMutablePointer<Int64>) -> Int64 ``` | -- |
| To | ``` func OSAtomicIncrement64(_ __theValue: UnsafeMutablePointer<OSAtomic_int64_aligned64_t>!) -> Int64 ``` | iOS 10.0 |

Modified OSAtomicIncrement64Barrier(_: UnsafeMutablePointer<OSAtomic_int64_aligned64_t>!) -> Int64

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicIncrement64Barrier(_ __theValue: UnsafeMutablePointer<Int64>) -> Int64 ``` | -- |
| To | ``` func OSAtomicIncrement64Barrier(_ __theValue: UnsafeMutablePointer<OSAtomic_int64_aligned64_t>!) -> Int64 ``` | iOS 10.0 |

Modified OSAtomicOr32(_: UInt32, _: UnsafeMutablePointer<UInt32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicOr32(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicOr32(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>!) -> Int32 ``` | iOS 10.0 |

Modified OSAtomicOr32Barrier(_: UInt32, _: UnsafeMutablePointer<UInt32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicOr32Barrier(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicOr32Barrier(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>!) -> Int32 ``` | iOS 10.0 |

Modified OSAtomicOr32Orig(_: UInt32, _: UnsafeMutablePointer<UInt32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicOr32Orig(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicOr32Orig(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>!) -> Int32 ``` | iOS 10.0 |

Modified OSAtomicOr32OrigBarrier(_: UInt32, _: UnsafeMutablePointer<UInt32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicOr32OrigBarrier(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicOr32OrigBarrier(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>!) -> Int32 ``` | iOS 10.0 |

Modified OSAtomicTestAndClear(_: UInt32, _: UnsafeMutableRawPointer!) -> Bool

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicTestAndClear(_ __n: UInt32, _ __theAddress: UnsafeMutablePointer<Void>) -> Bool ``` | -- |
| To | ``` func OSAtomicTestAndClear(_ __n: UInt32, _ __theAddress: UnsafeMutableRawPointer!) -> Bool ``` | iOS 10.0 |

Modified OSAtomicTestAndClearBarrier(_: UInt32, _: UnsafeMutableRawPointer!) -> Bool

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicTestAndClearBarrier(_ __n: UInt32, _ __theAddress: UnsafeMutablePointer<Void>) -> Bool ``` | -- |
| To | ``` func OSAtomicTestAndClearBarrier(_ __n: UInt32, _ __theAddress: UnsafeMutableRawPointer!) -> Bool ``` | iOS 10.0 |

Modified OSAtomicTestAndSet(_: UInt32, _: UnsafeMutableRawPointer!) -> Bool

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicTestAndSet(_ __n: UInt32, _ __theAddress: UnsafeMutablePointer<Void>) -> Bool ``` | -- |
| To | ``` func OSAtomicTestAndSet(_ __n: UInt32, _ __theAddress: UnsafeMutableRawPointer!) -> Bool ``` | iOS 10.0 |

Modified OSAtomicTestAndSetBarrier(_: UInt32, _: UnsafeMutableRawPointer!) -> Bool

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicTestAndSetBarrier(_ __n: UInt32, _ __theAddress: UnsafeMutablePointer<Void>) -> Bool ``` | -- |
| To | ``` func OSAtomicTestAndSetBarrier(_ __n: UInt32, _ __theAddress: UnsafeMutableRawPointer!) -> Bool ``` | iOS 10.0 |

Modified OSAtomicXor32(_: UInt32, _: UnsafeMutablePointer<UInt32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicXor32(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicXor32(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>!) -> Int32 ``` | iOS 10.0 |

Modified OSAtomicXor32Barrier(_: UInt32, _: UnsafeMutablePointer<UInt32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicXor32Barrier(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicXor32Barrier(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>!) -> Int32 ``` | iOS 10.0 |

Modified OSAtomicXor32Orig(_: UInt32, _: UnsafeMutablePointer<UInt32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicXor32Orig(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicXor32Orig(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>!) -> Int32 ``` | iOS 10.0 |

Modified OSAtomicXor32OrigBarrier(_: UInt32, _: UnsafeMutablePointer<UInt32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSAtomicXor32OrigBarrier(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>) -> Int32 ``` | -- |
| To | ``` func OSAtomicXor32OrigBarrier(_ __theMask: UInt32, _ __theValue: UnsafeMutablePointer<UInt32>!) -> Int32 ``` | iOS 10.0 |

Modified OSMemoryBarrier()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified OSReadSwapInt16(_: UnsafeRawPointer!, _: UInt) -> UInt16

|  | Declaration |
| --- | --- |
| From | ``` func OSReadSwapInt16(_ base: UnsafePointer<Void>, _ offset: UInt) -> UInt16 ``` |
| To | ``` func OSReadSwapInt16(_ base: UnsafeRawPointer!, _ offset: UInt) -> UInt16 ``` |

Modified OSReadSwapInt32(_: UnsafeRawPointer!, _: UInt) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func OSReadSwapInt32(_ base: UnsafePointer<Void>, _ offset: UInt) -> UInt32 ``` |
| To | ``` func OSReadSwapInt32(_ base: UnsafeRawPointer!, _ offset: UInt) -> UInt32 ``` |

Modified OSReadSwapInt64(_: UnsafeRawPointer!, _: UInt) -> UInt64

|  | Declaration |
| --- | --- |
| From | ``` func OSReadSwapInt64(_ base: UnsafePointer<Void>, _ offset: UInt) -> UInt64 ``` |
| To | ``` func OSReadSwapInt64(_ base: UnsafeRawPointer!, _ offset: UInt) -> UInt64 ``` |

Modified OSSpinLock

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified OSSpinLockLock(_: UnsafeMutablePointer<OSSpinLock>!)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSSpinLockLock(_ __lock: UnsafeMutablePointer<OSSpinLock>) ``` | -- |
| To | ``` func OSSpinLockLock(_ __lock: UnsafeMutablePointer<OSSpinLock>!) ``` | iOS 10.0 |

Modified OSSpinLockTry(_: UnsafeMutablePointer<OSSpinLock>!) -> Bool

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSSpinLockTry(_ __lock: UnsafeMutablePointer<OSSpinLock>) -> Bool ``` | -- |
| To | ``` func OSSpinLockTry(_ __lock: UnsafeMutablePointer<OSSpinLock>!) -> Bool ``` | iOS 10.0 |

Modified OSSpinLockUnlock(_: UnsafeMutablePointer<OSSpinLock>!)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func OSSpinLockUnlock(_ __lock: UnsafeMutablePointer<OSSpinLock>) ``` | -- |
| To | ``` func OSSpinLockUnlock(_ __lock: UnsafeMutablePointer<OSSpinLock>!) ``` | iOS 10.0 |

Modified OSWriteSwapInt16(_: UnsafeMutableRawPointer!, _: UInt, _: UInt16)

|  | Declaration |
| --- | --- |
| From | ``` func OSWriteSwapInt16(_ base: UnsafeMutablePointer<Void>, _ offset: UInt, _ data: UInt16) ``` |
| To | ``` func OSWriteSwapInt16(_ base: UnsafeMutableRawPointer!, _ offset: UInt, _ data: UInt16) ``` |

Modified OSWriteSwapInt32(_: UnsafeMutableRawPointer!, _: UInt, _: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` func OSWriteSwapInt32(_ base: UnsafeMutablePointer<Void>, _ offset: UInt, _ data: UInt32) ``` |
| To | ``` func OSWriteSwapInt32(_ base: UnsafeMutableRawPointer!, _ offset: UInt, _ data: UInt32) ``` |

Modified OSWriteSwapInt64(_: UnsafeMutableRawPointer!, _: UInt, _: UInt64)

|  | Declaration |
| --- | --- |
| From | ``` func OSWriteSwapInt64(_ base: UnsafeMutablePointer<Void>, _ offset: UInt, _ data: UInt64) ``` |
| To | ``` func OSWriteSwapInt64(_ base: UnsafeMutableRawPointer!, _ offset: UInt, _ data: UInt64) ``` |

Modified pathconf(_: UnsafePointer<Int8>!, _: Int32) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func pathconf(_ _: UnsafePointer<Int8>, _ _: Int32) -> Int ``` |
| To | ``` func pathconf(_ _: UnsafePointer<Int8>!, _ _: Int32) -> Int ``` |

Modified perror(_: UnsafePointer<Int8>!)

|  | Declaration |
| --- | --- |
| From | ``` func perror(_ _: UnsafePointer<Int8>) ``` |
| To | ``` func perror(_ _: UnsafePointer<Int8>!) ``` |

Modified pfctlinput(_: Int32, _: UnsafeMutablePointer<sockaddr>!)

|  | Declaration |
| --- | --- |
| From | ``` func pfctlinput(_ _: Int32, _ _: UnsafeMutablePointer<sockaddr>) ``` |
| To | ``` func pfctlinput(_ _: Int32, _ _: UnsafeMutablePointer<sockaddr>!) ``` |

Modified pid_for_task(_: mach_port_name_t, _: UnsafeMutablePointer<Int32>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func pid_for_task(_ t: mach_port_name_t, _ x: UnsafeMutablePointer<Int32>) -> kern_return_t ``` |
| To | ``` func pid_for_task(_ t: mach_port_name_t, _ x: UnsafeMutablePointer<Int32>!) -> kern_return_t ``` |

Modified pidlock(_: UnsafePointer<Int8>!, _: Int32, _: UnsafeMutablePointer<pid_t>!, _: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pidlock(_ _: UnsafePointer<Int8>, _ _: Int32, _ _: UnsafeMutablePointer<pid_t>, _ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func pidlock(_ _: UnsafePointer<Int8>!, _ _: Int32, _ _: UnsafeMutablePointer<pid_t>!, _ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified pipe(_: UnsafeMutablePointer<Int32>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pipe(_ _: UnsafeMutablePointer<Int32>) -> Int32 ``` |
| To | ``` func pipe(_ _: UnsafeMutablePointer<Int32>!) -> Int32 ``` |

Modified poll(_: UnsafeMutablePointer<pollfd>!, _: nfds_t, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func poll(_ _: UnsafeMutablePointer<pollfd>, _ _: nfds_t, _ _: Int32) -> Int32 ``` |
| To | ``` func poll(_ _: UnsafeMutablePointer<pollfd>!, _ _: nfds_t, _ _: Int32) -> Int32 ``` |

Modified port_obj_table

|  | Declaration |
| --- | --- |
| From | ``` var port_obj_table: UnsafeMutablePointer<port_obj_tentry> ``` |
| To | ``` var port_obj_table: UnsafeMutablePointer<port_obj_tentry>! ``` |

Modified posix_madvise(_: UnsafeMutableRawPointer!, _: Int, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_madvise(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32) -> Int32 ``` |
| To | ``` func posix_madvise(_ _: UnsafeMutableRawPointer!, _ _: Int, _ _: Int32) -> Int32 ``` |

Modified posix_memalign(_: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _: Int, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_memalign(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ _: Int, _ _: Int) -> Int32 ``` |
| To | ``` func posix_memalign(_ __memptr: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _ __alignment: Int, _ __size: Int) -> Int32 ``` |

Modified posix_spawn(_: UnsafeMutablePointer<pid_t>!, _: UnsafePointer<Int8>!, _: UnsafePointer<posix_spawn_file_actions_t?>!, _: UnsafePointer<posix_spawnattr_t?>!, _: UnsafePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafePointer<UnsafeMutablePointer<Int8>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawn(_ _: UnsafeMutablePointer<pid_t>, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<posix_spawn_file_actions_t>, _ _: UnsafePointer<posix_spawnattr_t>, _ __argv: UnsafePointer<UnsafeMutablePointer<Int8>>, _ __envp: UnsafePointer<UnsafeMutablePointer<Int8>>) -> Int32 ``` |
| To | ``` func posix_spawn(_ _: UnsafeMutablePointer<pid_t>!, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<posix_spawn_file_actions_t?>!, _ _: UnsafePointer<posix_spawnattr_t?>!, _ __argv: UnsafePointer<UnsafeMutablePointer<Int8>?>!, _ __envp: UnsafePointer<UnsafeMutablePointer<Int8>?>!) -> Int32 ``` |

Modified posix_spawn_file_actions_addclose(_: UnsafeMutablePointer<posix_spawn_file_actions_t?>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawn_file_actions_addclose(_ _: UnsafeMutablePointer<posix_spawn_file_actions_t>, _ _: Int32) -> Int32 ``` |
| To | ``` func posix_spawn_file_actions_addclose(_ _: UnsafeMutablePointer<posix_spawn_file_actions_t?>!, _ _: Int32) -> Int32 ``` |

Modified posix_spawn_file_actions_adddup2(_: UnsafeMutablePointer<posix_spawn_file_actions_t?>!, _: Int32, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawn_file_actions_adddup2(_ _: UnsafeMutablePointer<posix_spawn_file_actions_t>, _ _: Int32, _ _: Int32) -> Int32 ``` |
| To | ``` func posix_spawn_file_actions_adddup2(_ _: UnsafeMutablePointer<posix_spawn_file_actions_t?>!, _ _: Int32, _ _: Int32) -> Int32 ``` |

Modified posix_spawn_file_actions_addinherit_np(_: UnsafeMutablePointer<posix_spawn_file_actions_t?>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawn_file_actions_addinherit_np(_ _: UnsafeMutablePointer<posix_spawn_file_actions_t>, _ _: Int32) -> Int32 ``` |
| To | ``` func posix_spawn_file_actions_addinherit_np(_ _: UnsafeMutablePointer<posix_spawn_file_actions_t?>!, _ _: Int32) -> Int32 ``` |

Modified posix_spawn_file_actions_addopen(_: UnsafeMutablePointer<posix_spawn_file_actions_t?>!, _: Int32, _: UnsafePointer<Int8>!, _: Int32, _: mode_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawn_file_actions_addopen(_ _: UnsafeMutablePointer<posix_spawn_file_actions_t>, _ _: Int32, _ _: UnsafePointer<Int8>, _ _: Int32, _ _: mode_t) -> Int32 ``` |
| To | ``` func posix_spawn_file_actions_addopen(_ _: UnsafeMutablePointer<posix_spawn_file_actions_t?>!, _ _: Int32, _ _: UnsafePointer<Int8>!, _ _: Int32, _ _: mode_t) -> Int32 ``` |

Modified posix_spawn_file_actions_destroy(_: UnsafeMutablePointer<posix_spawn_file_actions_t?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawn_file_actions_destroy(_ _: UnsafeMutablePointer<posix_spawn_file_actions_t>) -> Int32 ``` |
| To | ``` func posix_spawn_file_actions_destroy(_ _: UnsafeMutablePointer<posix_spawn_file_actions_t?>!) -> Int32 ``` |

Modified posix_spawn_file_actions_init(_: UnsafeMutablePointer<posix_spawn_file_actions_t?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawn_file_actions_init(_ _: UnsafeMutablePointer<posix_spawn_file_actions_t>) -> Int32 ``` |
| To | ``` func posix_spawn_file_actions_init(_ _: UnsafeMutablePointer<posix_spawn_file_actions_t?>!) -> Int32 ``` |

Modified posix_spawn_file_actions_t

|  | Declaration |
| --- | --- |
| From | ``` typealias posix_spawn_file_actions_t = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias posix_spawn_file_actions_t = UnsafeMutableRawPointer ``` |

Modified posix_spawnattr_destroy(_: UnsafeMutablePointer<posix_spawnattr_t?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnattr_destroy(_ _: UnsafeMutablePointer<posix_spawnattr_t>) -> Int32 ``` |
| To | ``` func posix_spawnattr_destroy(_ _: UnsafeMutablePointer<posix_spawnattr_t?>!) -> Int32 ``` |

Modified posix_spawnattr_getbinpref_np(_: UnsafePointer<posix_spawnattr_t?>!, _: Int, _: UnsafeMutablePointer<cpu_type_t>!, _: UnsafeMutablePointer<Int>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnattr_getbinpref_np(_ _: UnsafePointer<posix_spawnattr_t>, _ _: Int, _ _: UnsafeMutablePointer<cpu_type_t>, _ _: UnsafeMutablePointer<Int>) -> Int32 ``` |
| To | ``` func posix_spawnattr_getbinpref_np(_ _: UnsafePointer<posix_spawnattr_t?>!, _ _: Int, _ _: UnsafeMutablePointer<cpu_type_t>!, _ _: UnsafeMutablePointer<Int>!) -> Int32 ``` |

Modified posix_spawnattr_getflags(_: UnsafePointer<posix_spawnattr_t?>!, _: UnsafeMutablePointer<Int16>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnattr_getflags(_ _: UnsafePointer<posix_spawnattr_t>, _ _: UnsafeMutablePointer<Int16>) -> Int32 ``` |
| To | ``` func posix_spawnattr_getflags(_ _: UnsafePointer<posix_spawnattr_t?>!, _ _: UnsafeMutablePointer<Int16>!) -> Int32 ``` |

Modified posix_spawnattr_getpgroup(_: UnsafePointer<posix_spawnattr_t?>!, _: UnsafeMutablePointer<pid_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnattr_getpgroup(_ _: UnsafePointer<posix_spawnattr_t>, _ _: UnsafeMutablePointer<pid_t>) -> Int32 ``` |
| To | ``` func posix_spawnattr_getpgroup(_ _: UnsafePointer<posix_spawnattr_t?>!, _ _: UnsafeMutablePointer<pid_t>!) -> Int32 ``` |

Modified posix_spawnattr_getsigdefault(_: UnsafePointer<posix_spawnattr_t?>!, _: UnsafeMutablePointer<sigset_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnattr_getsigdefault(_ _: UnsafePointer<posix_spawnattr_t>, _ _: UnsafeMutablePointer<sigset_t>) -> Int32 ``` |
| To | ``` func posix_spawnattr_getsigdefault(_ _: UnsafePointer<posix_spawnattr_t?>!, _ _: UnsafeMutablePointer<sigset_t>!) -> Int32 ``` |

Modified posix_spawnattr_getsigmask(_: UnsafePointer<posix_spawnattr_t?>!, _: UnsafeMutablePointer<sigset_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnattr_getsigmask(_ _: UnsafePointer<posix_spawnattr_t>, _ _: UnsafeMutablePointer<sigset_t>) -> Int32 ``` |
| To | ``` func posix_spawnattr_getsigmask(_ _: UnsafePointer<posix_spawnattr_t?>!, _ _: UnsafeMutablePointer<sigset_t>!) -> Int32 ``` |

Modified posix_spawnattr_init(_: UnsafeMutablePointer<posix_spawnattr_t?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnattr_init(_ _: UnsafeMutablePointer<posix_spawnattr_t>) -> Int32 ``` |
| To | ``` func posix_spawnattr_init(_ _: UnsafeMutablePointer<posix_spawnattr_t?>!) -> Int32 ``` |

Modified posix_spawnattr_setauditsessionport_np(_: UnsafeMutablePointer<posix_spawnattr_t?>!, _: mach_port_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnattr_setauditsessionport_np(_ _: UnsafeMutablePointer<posix_spawnattr_t>, _ _: mach_port_t) -> Int32 ``` |
| To | ``` func posix_spawnattr_setauditsessionport_np(_ _: UnsafeMutablePointer<posix_spawnattr_t?>!, _ _: mach_port_t) -> Int32 ``` |

Modified posix_spawnattr_setbinpref_np(_: UnsafeMutablePointer<posix_spawnattr_t?>!, _: Int, _: UnsafeMutablePointer<cpu_type_t>!, _: UnsafeMutablePointer<Int>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnattr_setbinpref_np(_ _: UnsafeMutablePointer<posix_spawnattr_t>, _ _: Int, _ _: UnsafeMutablePointer<cpu_type_t>, _ _: UnsafeMutablePointer<Int>) -> Int32 ``` |
| To | ``` func posix_spawnattr_setbinpref_np(_ _: UnsafeMutablePointer<posix_spawnattr_t?>!, _ _: Int, _ _: UnsafeMutablePointer<cpu_type_t>!, _ _: UnsafeMutablePointer<Int>!) -> Int32 ``` |

Modified posix_spawnattr_setexceptionports_np(_: UnsafeMutablePointer<posix_spawnattr_t?>!, _: exception_mask_t, _: mach_port_t, _: exception_behavior_t, _: thread_state_flavor_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnattr_setexceptionports_np(_ _: UnsafeMutablePointer<posix_spawnattr_t>, _ _: exception_mask_t, _ _: mach_port_t, _ _: exception_behavior_t, _ _: thread_state_flavor_t) -> Int32 ``` |
| To | ``` func posix_spawnattr_setexceptionports_np(_ _: UnsafeMutablePointer<posix_spawnattr_t?>!, _ _: exception_mask_t, _ _: mach_port_t, _ _: exception_behavior_t, _ _: thread_state_flavor_t) -> Int32 ``` |

Modified posix_spawnattr_setflags(_: UnsafeMutablePointer<posix_spawnattr_t?>!, _: Int16) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnattr_setflags(_ _: UnsafeMutablePointer<posix_spawnattr_t>, _ _: Int16) -> Int32 ``` |
| To | ``` func posix_spawnattr_setflags(_ _: UnsafeMutablePointer<posix_spawnattr_t?>!, _ _: Int16) -> Int32 ``` |

Modified posix_spawnattr_setpgroup(_: UnsafeMutablePointer<posix_spawnattr_t?>!, _: pid_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnattr_setpgroup(_ _: UnsafeMutablePointer<posix_spawnattr_t>, _ _: pid_t) -> Int32 ``` |
| To | ``` func posix_spawnattr_setpgroup(_ _: UnsafeMutablePointer<posix_spawnattr_t?>!, _ _: pid_t) -> Int32 ``` |

Modified posix_spawnattr_setsigdefault(_: UnsafeMutablePointer<posix_spawnattr_t?>!, _: UnsafePointer<sigset_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnattr_setsigdefault(_ _: UnsafeMutablePointer<posix_spawnattr_t>, _ _: UnsafePointer<sigset_t>) -> Int32 ``` |
| To | ``` func posix_spawnattr_setsigdefault(_ _: UnsafeMutablePointer<posix_spawnattr_t?>!, _ _: UnsafePointer<sigset_t>!) -> Int32 ``` |

Modified posix_spawnattr_setsigmask(_: UnsafeMutablePointer<posix_spawnattr_t?>!, _: UnsafePointer<sigset_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnattr_setsigmask(_ _: UnsafeMutablePointer<posix_spawnattr_t>, _ _: UnsafePointer<sigset_t>) -> Int32 ``` |
| To | ``` func posix_spawnattr_setsigmask(_ _: UnsafeMutablePointer<posix_spawnattr_t?>!, _ _: UnsafePointer<sigset_t>!) -> Int32 ``` |

Modified posix_spawnattr_setspecialport_np(_: UnsafeMutablePointer<posix_spawnattr_t?>!, _: mach_port_t, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnattr_setspecialport_np(_ _: UnsafeMutablePointer<posix_spawnattr_t>, _ _: mach_port_t, _ _: Int32) -> Int32 ``` |
| To | ``` func posix_spawnattr_setspecialport_np(_ _: UnsafeMutablePointer<posix_spawnattr_t?>!, _ _: mach_port_t, _ _: Int32) -> Int32 ``` |

Modified posix_spawnattr_t

|  | Declaration |
| --- | --- |
| From | ``` typealias posix_spawnattr_t = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias posix_spawnattr_t = UnsafeMutableRawPointer ``` |

Modified posix_spawnp(_: UnsafeMutablePointer<pid_t>!, _: UnsafePointer<Int8>!, _: UnsafePointer<posix_spawn_file_actions_t?>!, _: UnsafePointer<posix_spawnattr_t?>!, _: UnsafePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafePointer<UnsafeMutablePointer<Int8>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnp(_ _: UnsafeMutablePointer<pid_t>, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<posix_spawn_file_actions_t>, _ _: UnsafePointer<posix_spawnattr_t>, _ __argv: UnsafePointer<UnsafeMutablePointer<Int8>>, _ __envp: UnsafePointer<UnsafeMutablePointer<Int8>>) -> Int32 ``` |
| To | ``` func posix_spawnp(_ _: UnsafeMutablePointer<pid_t>!, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<posix_spawn_file_actions_t?>!, _ _: UnsafePointer<posix_spawnattr_t?>!, _ __argv: UnsafePointer<UnsafeMutablePointer<Int8>?>!, _ __envp: UnsafePointer<UnsafeMutablePointer<Int8>?>!) -> Int32 ``` |

Modified pow(_: Float, _: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func pow(_ lhs: Float, _ rhs: Float) -> Float ``` |
| To | ``` func pow(_ lhs: Float, _ rhs: Float) -> Float ``` |

Modified pread(_: Int32, _: UnsafeMutableRawPointer!, _: Int, _: off_t) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func pread(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: off_t) -> Int ``` |
| To | ``` func pread(_ __fd: Int32, _ __buf: UnsafeMutableRawPointer!, _ __nbyte: Int, _ __offset: off_t) -> Int ``` |

Modified processor_control(_: processor_t, _: processor_info_t!, _: mach_msg_type_number_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func processor_control(_ processor: processor_t, _ processor_cmd: processor_info_t, _ processor_cmdCnt: mach_msg_type_number_t) -> kern_return_t ``` |
| To | ``` func processor_control(_ processor: processor_t, _ processor_cmd: processor_info_t!, _ processor_cmdCnt: mach_msg_type_number_t) -> kern_return_t ``` |

Modified processor_get_assignment(_: processor_t, _: UnsafeMutablePointer<processor_set_name_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func processor_get_assignment(_ processor: processor_t, _ assigned_set: UnsafeMutablePointer<processor_set_name_t>) -> kern_return_t ``` |
| To | ``` func processor_get_assignment(_ processor: processor_t, _ assigned_set: UnsafeMutablePointer<processor_set_name_t>!) -> kern_return_t ``` |

Modified processor_info(_: processor_t, _: processor_flavor_t, _: UnsafeMutablePointer<host_t>!, _: processor_info_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func processor_info(_ processor: processor_t, _ flavor: processor_flavor_t, _ host: UnsafeMutablePointer<host_t>, _ processor_info_out: processor_info_t, _ processor_info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func processor_info(_ processor: processor_t, _ flavor: processor_flavor_t, _ host: UnsafeMutablePointer<host_t>!, _ processor_info_out: processor_info_t!, _ processor_info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified processor_set_create(_: host_t, _: UnsafeMutablePointer<processor_set_t>!, _: UnsafeMutablePointer<processor_set_name_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func processor_set_create(_ host: host_t, _ new_set: UnsafeMutablePointer<processor_set_t>, _ new_name: UnsafeMutablePointer<processor_set_name_t>) -> kern_return_t ``` |
| To | ``` func processor_set_create(_ host: host_t, _ new_set: UnsafeMutablePointer<processor_set_t>!, _ new_name: UnsafeMutablePointer<processor_set_name_t>!) -> kern_return_t ``` |

Modified processor_set_default(_: host_t, _: UnsafeMutablePointer<processor_set_name_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func processor_set_default(_ host: host_t, _ default_set: UnsafeMutablePointer<processor_set_name_t>) -> kern_return_t ``` |
| To | ``` func processor_set_default(_ host: host_t, _ default_set: UnsafeMutablePointer<processor_set_name_t>!) -> kern_return_t ``` |

Modified processor_set_info(_: processor_set_name_t, _: Int32, _: UnsafeMutablePointer<host_t>!, _: processor_set_info_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func processor_set_info(_ set_name: processor_set_name_t, _ flavor: Int32, _ host: UnsafeMutablePointer<host_t>, _ info_out: processor_set_info_t, _ info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func processor_set_info(_ set_name: processor_set_name_t, _ flavor: Int32, _ host: UnsafeMutablePointer<host_t>!, _ info_out: processor_set_info_t!, _ info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified processor_set_policy_control(_: processor_set_t, _: processor_set_flavor_t, _: processor_set_info_t!, _: mach_msg_type_number_t, _: boolean_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func processor_set_policy_control(_ pset: processor_set_t, _ flavor: processor_set_flavor_t, _ policy_info: processor_set_info_t, _ policy_infoCnt: mach_msg_type_number_t, _ change: boolean_t) -> kern_return_t ``` |
| To | ``` func processor_set_policy_control(_ pset: processor_set_t, _ flavor: processor_set_flavor_t, _ policy_info: processor_set_info_t!, _ policy_infoCnt: mach_msg_type_number_t, _ change: boolean_t) -> kern_return_t ``` |

Modified processor_set_stack_usage(_: processor_set_t, _: UnsafeMutablePointer<UInt32>!, _: UnsafeMutablePointer<vm_size_t>!, _: UnsafeMutablePointer<vm_size_t>!, _: UnsafeMutablePointer<vm_size_t>!, _: UnsafeMutablePointer<vm_offset_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func processor_set_stack_usage(_ pset: processor_set_t, _ ltotal: UnsafeMutablePointer<UInt32>, _ space: UnsafeMutablePointer<vm_size_t>, _ resident: UnsafeMutablePointer<vm_size_t>, _ maxusage: UnsafeMutablePointer<vm_size_t>, _ maxstack: UnsafeMutablePointer<vm_offset_t>) -> kern_return_t ``` |
| To | ``` func processor_set_stack_usage(_ pset: processor_set_t, _ ltotal: UnsafeMutablePointer<UInt32>!, _ space: UnsafeMutablePointer<vm_size_t>!, _ resident: UnsafeMutablePointer<vm_size_t>!, _ maxusage: UnsafeMutablePointer<vm_size_t>!, _ maxstack: UnsafeMutablePointer<vm_offset_t>!) -> kern_return_t ``` |

Modified processor_set_statistics(_: processor_set_name_t, _: processor_set_flavor_t, _: processor_set_info_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func processor_set_statistics(_ pset: processor_set_name_t, _ flavor: processor_set_flavor_t, _ info_out: processor_set_info_t, _ info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func processor_set_statistics(_ pset: processor_set_name_t, _ flavor: processor_set_flavor_t, _ info_out: processor_set_info_t!, _ info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified processor_set_tasks(_: processor_set_t, _: UnsafeMutablePointer<task_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func processor_set_tasks(_ processor_set: processor_set_t, _ task_list: UnsafeMutablePointer<task_array_t>, _ task_listCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func processor_set_tasks(_ processor_set: processor_set_t, _ task_list: UnsafeMutablePointer<task_array_t?>!, _ task_listCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified processor_set_threads(_: processor_set_t, _: UnsafeMutablePointer<thread_act_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func processor_set_threads(_ processor_set: processor_set_t, _ thread_list: UnsafeMutablePointer<thread_act_array_t>, _ thread_listCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func processor_set_threads(_ processor_set: processor_set_t, _ thread_list: UnsafeMutablePointer<thread_act_array_t?>!, _ thread_listCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified profil(_: UnsafeMutablePointer<Int8>!, _: Int, _: UInt, _: UInt32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func profil(_ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UInt, _ _: UInt32) -> Int32 ``` |
| To | ``` func profil(_ _: UnsafeMutablePointer<Int8>!, _ _: Int, _ _: UInt, _ _: UInt32) -> Int32 ``` |

Modified pselect(_: Int32, _: UnsafeMutablePointer<fd_set>!, _: UnsafeMutablePointer<fd_set>!, _: UnsafeMutablePointer<fd_set>!, _: UnsafePointer<timespec>!, _: UnsafePointer<sigset_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pselect(_ _: Int32, _ _: UnsafeMutablePointer<fd_set>, _ _: UnsafeMutablePointer<fd_set>, _ _: UnsafeMutablePointer<fd_set>, _ _: UnsafePointer<timespec>, _ _: UnsafePointer<sigset_t>) -> Int32 ``` |
| To | ``` func pselect(_ _: Int32, _ _: UnsafeMutablePointer<fd_set>!, _ _: UnsafeMutablePointer<fd_set>!, _ _: UnsafeMutablePointer<fd_set>!, _ _: UnsafePointer<timespec>!, _ _: UnsafePointer<sigset_t>!) -> Int32 ``` |

Modified psignal(_: UInt32, _: UnsafePointer<Int8>!)

|  | Declaration |
| --- | --- |
| From | ``` func psignal(_ _: UInt32, _ _: UnsafePointer<Int8>) ``` |
| To | ``` func psignal(_ _: UInt32, _ _: UnsafePointer<Int8>!) ``` |

Modified psort(_: UnsafeMutableRawPointer!, _: Int, _: Int, _: (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)

|  | Declaration |
| --- | --- |
| From | ``` func psort(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) ``` |
| To | ``` func psort(_ __base: UnsafeMutableRawPointer!, _ __nel: Int, _ __width: Int, _ __compar: @escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) ``` |

Modified psort_b(_: UnsafeMutableRawPointer!, _: Int, _: Int, _: (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)

|  | Declaration |
| --- | --- |
| From | ``` func psort_b(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) ``` |
| To | ``` func psort_b(_ __base: UnsafeMutableRawPointer!, _ __nel: Int, _ __width: Int, _ __compar: @escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) ``` |

Modified psort_r(_: UnsafeMutableRawPointer!, _: Int, _: Int, _: UnsafeMutableRawPointer!, _: (UnsafeMutableRawPointer?, UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)

|  | Declaration |
| --- | --- |
| From | ``` func psort_r(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: ((UnsafeMutablePointer<Void>, UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) ``` |
| To | ``` func psort_r(_ __base: UnsafeMutableRawPointer!, _ __nel: Int, _ __width: Int, _ _: UnsafeMutableRawPointer!, _ __compar: @escaping (UnsafeMutableRawPointer?, UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) ``` |

Modified pthread_atfork(_: ( () -> Swift.Void)?, _: ( () -> Swift.Void)?, _: ( () -> Swift.Void)?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_atfork(_ _: (() -> Void)!, _ _: (() -> Void)!, _ _: (() -> Void)!) -> Int32 ``` |
| To | ``` func pthread_atfork(_ _: (@escaping () -> Swift.Void)?, _ _: (@escaping () -> Swift.Void)?, _ _: (@escaping () -> Swift.Void)?) -> Int32 ``` |

Modified pthread_attr_get_qos_class_np(_: UnsafeMutablePointer<pthread_attr_t>, _: UnsafeMutablePointer<qos_class_t>?, _: UnsafeMutablePointer<Int32>?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_attr_get_qos_class_np(_ __attr: UnsafeMutablePointer<pthread_attr_t>, _ __qos_class: UnsafeMutablePointer<qos_class_t>, _ __relative_priority: UnsafeMutablePointer<Int32>) -> Int32 ``` |
| To | ``` func pthread_attr_get_qos_class_np(_ __attr: UnsafeMutablePointer<pthread_attr_t>, _ __qos_class: UnsafeMutablePointer<qos_class_t>?, _ __relative_priority: UnsafeMutablePointer<Int32>?) -> Int32 ``` |

Modified pthread_attr_getstack(_: UnsafePointer<pthread_attr_t>, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>, _: UnsafeMutablePointer<Int>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_attr_getstack(_ _: UnsafePointer<pthread_attr_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ _: UnsafeMutablePointer<Int>) -> Int32 ``` |
| To | ``` func pthread_attr_getstack(_ _: UnsafePointer<pthread_attr_t>, _ _: UnsafeMutablePointer<UnsafeMutableRawPointer?>, _ _: UnsafeMutablePointer<Int>) -> Int32 ``` |

Modified pthread_attr_getstackaddr(_: UnsafePointer<pthread_attr_t>, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_attr_getstackaddr(_ _: UnsafePointer<pthread_attr_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int32 ``` |
| To | ``` func pthread_attr_getstackaddr(_ _: UnsafePointer<pthread_attr_t>, _ _: UnsafeMutablePointer<UnsafeMutableRawPointer?>) -> Int32 ``` |

Modified pthread_attr_setstack(_: UnsafeMutablePointer<pthread_attr_t>, _: UnsafeMutableRawPointer, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_attr_setstack(_ _: UnsafeMutablePointer<pthread_attr_t>, _ _: UnsafeMutablePointer<Void>, _ _: Int) -> Int32 ``` |
| To | ``` func pthread_attr_setstack(_ _: UnsafeMutablePointer<pthread_attr_t>, _ _: UnsafeMutableRawPointer, _ _: Int) -> Int32 ``` |

Modified pthread_attr_setstackaddr(_: UnsafeMutablePointer<pthread_attr_t>, _: UnsafeMutableRawPointer) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_attr_setstackaddr(_ _: UnsafeMutablePointer<pthread_attr_t>, _ _: UnsafeMutablePointer<Void>) -> Int32 ``` |
| To | ``` func pthread_attr_setstackaddr(_ _: UnsafeMutablePointer<pthread_attr_t>, _ _: UnsafeMutableRawPointer) -> Int32 ``` |

Modified pthread_cond_init(_: UnsafeMutablePointer<pthread_cond_t>, _: UnsafePointer<pthread_condattr_t>?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_cond_init(_ _: UnsafeMutablePointer<pthread_cond_t>, _ _: UnsafePointer<pthread_condattr_t>) -> Int32 ``` |
| To | ``` func pthread_cond_init(_ _: UnsafeMutablePointer<pthread_cond_t>, _ _: UnsafePointer<pthread_condattr_t>?) -> Int32 ``` |

Modified pthread_cond_signal_thread_np(_: UnsafeMutablePointer<pthread_cond_t>, _: pthread_t?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_cond_signal_thread_np(_ _: UnsafeMutablePointer<pthread_cond_t>, _ _: pthread_t) -> Int32 ``` |
| To | ``` func pthread_cond_signal_thread_np(_ _: UnsafeMutablePointer<pthread_cond_t>, _ _: pthread_t?) -> Int32 ``` |

Modified pthread_cond_timedwait(_: UnsafeMutablePointer<pthread_cond_t>, _: UnsafeMutablePointer<pthread_mutex_t>, _: UnsafePointer<timespec>?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_cond_timedwait(_ _: UnsafeMutablePointer<pthread_cond_t>, _ _: UnsafeMutablePointer<pthread_mutex_t>, _ _: UnsafePointer<timespec>) -> Int32 ``` |
| To | ``` func pthread_cond_timedwait(_ _: UnsafeMutablePointer<pthread_cond_t>, _ _: UnsafeMutablePointer<pthread_mutex_t>, _ _: UnsafePointer<timespec>?) -> Int32 ``` |

Modified pthread_cond_timedwait_relative_np(_: UnsafeMutablePointer<pthread_cond_t>, _: UnsafeMutablePointer<pthread_mutex_t>, _: UnsafePointer<timespec>?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_cond_timedwait_relative_np(_ _: UnsafeMutablePointer<pthread_cond_t>, _ _: UnsafeMutablePointer<pthread_mutex_t>, _ _: UnsafePointer<timespec>) -> Int32 ``` |
| To | ``` func pthread_cond_timedwait_relative_np(_ _: UnsafeMutablePointer<pthread_cond_t>, _ _: UnsafeMutablePointer<pthread_mutex_t>, _ _: UnsafePointer<timespec>?) -> Int32 ``` |

Modified pthread_create(_: UnsafeMutablePointer<pthread_t?>!, _: UnsafePointer<pthread_attr_t>?, _: (UnsafeMutableRawPointer) -> UnsafeMutableRawPointer?, _: UnsafeMutableRawPointer?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_create(_ _: UnsafeMutablePointer<pthread_t>, _ _: UnsafePointer<pthread_attr_t>, _ _: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!, _ _: UnsafeMutablePointer<Void>) -> Int32 ``` |
| To | ``` func pthread_create(_ _: UnsafeMutablePointer<pthread_t?>!, _ _: UnsafePointer<pthread_attr_t>?, _ _: @escaping (UnsafeMutableRawPointer) -> UnsafeMutableRawPointer?, _ _: UnsafeMutableRawPointer?) -> Int32 ``` |

Modified pthread_create_suspended_np(_: UnsafeMutablePointer<pthread_t?>!, _: UnsafePointer<pthread_attr_t>?, _: (UnsafeMutableRawPointer) -> UnsafeMutableRawPointer?, _: UnsafeMutableRawPointer?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_create_suspended_np(_ _: UnsafeMutablePointer<pthread_t>, _ _: UnsafePointer<pthread_attr_t>, _ _: ((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void>)!, _ _: UnsafeMutablePointer<Void>) -> Int32 ``` |
| To | ``` func pthread_create_suspended_np(_ _: UnsafeMutablePointer<pthread_t?>!, _ _: UnsafePointer<pthread_attr_t>?, _ _: @escaping (UnsafeMutableRawPointer) -> UnsafeMutableRawPointer?, _ _: UnsafeMutableRawPointer?) -> Int32 ``` |

Modified pthread_equal(_: pthread_t?, _: pthread_t?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_equal(_ _: pthread_t, _ _: pthread_t) -> Int32 ``` |
| To | ``` func pthread_equal(_ _: pthread_t?, _ _: pthread_t?) -> Int32 ``` |

Modified pthread_exit(_: UnsafeMutableRawPointer?) -> Never

|  | Declaration |
| --- | --- |
| From | ``` @noreturn func pthread_exit(_ _: UnsafeMutablePointer<Void>) ``` |
| To | ``` func pthread_exit(_ _: UnsafeMutableRawPointer?) -> Never ``` |

Modified pthread_from_mach_thread_np(_: mach_port_t) -> pthread_t?

|  | Declaration |
| --- | --- |
| From | ``` func pthread_from_mach_thread_np(_ _: mach_port_t) -> pthread_t ``` |
| To | ``` func pthread_from_mach_thread_np(_ _: mach_port_t) -> pthread_t? ``` |

Modified pthread_get_qos_class_np(_: pthread_t, _: UnsafeMutablePointer<qos_class_t>?, _: UnsafeMutablePointer<Int32>?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_get_qos_class_np(_ __pthread: pthread_t, _ __qos_class: UnsafeMutablePointer<qos_class_t>, _ __relative_priority: UnsafeMutablePointer<Int32>) -> Int32 ``` |
| To | ``` func pthread_get_qos_class_np(_ __pthread: pthread_t, _ __qos_class: UnsafeMutablePointer<qos_class_t>?, _ __relative_priority: UnsafeMutablePointer<Int32>?) -> Int32 ``` |

Modified pthread_get_stackaddr_np(_: pthread_t) -> UnsafeMutableRawPointer

|  | Declaration |
| --- | --- |
| From | ``` func pthread_get_stackaddr_np(_ _: pthread_t) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func pthread_get_stackaddr_np(_ _: pthread_t) -> UnsafeMutableRawPointer ``` |

Modified pthread_getschedparam(_: pthread_t, _: UnsafeMutablePointer<Int32>?, _: UnsafeMutablePointer<sched_param>?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_getschedparam(_ _: pthread_t, _ _: UnsafeMutablePointer<Int32>, _ _: UnsafeMutablePointer<sched_param>) -> Int32 ``` |
| To | ``` func pthread_getschedparam(_ _: pthread_t, _ _: UnsafeMutablePointer<Int32>?, _ _: UnsafeMutablePointer<sched_param>?) -> Int32 ``` |

Modified pthread_getspecific(_: pthread_key_t) -> UnsafeMutableRawPointer?

|  | Declaration |
| --- | --- |
| From | ``` func pthread_getspecific(_ _: pthread_key_t) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func pthread_getspecific(_ _: pthread_key_t) -> UnsafeMutableRawPointer? ``` |

Modified pthread_getugid_np(_: UnsafeMutablePointer<uid_t>!, _: UnsafeMutablePointer<gid_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_getugid_np(_ _: UnsafeMutablePointer<uid_t>, _ _: UnsafeMutablePointer<gid_t>) -> Int32 ``` |
| To | ``` func pthread_getugid_np(_ _: UnsafeMutablePointer<uid_t>!, _ _: UnsafeMutablePointer<gid_t>!) -> Int32 ``` |

Modified pthread_join(_: pthread_t, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_join(_ _: pthread_t, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int32 ``` |
| To | ``` func pthread_join(_ _: pthread_t, _ _: UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> Int32 ``` |

Modified pthread_key_create(_: UnsafeMutablePointer<pthread_key_t>, _: ( (UnsafeMutableRawPointer) -> Swift.Void)?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_key_create(_ _: UnsafeMutablePointer<pthread_key_t>, _ _: ((UnsafeMutablePointer<Void>) -> Void)!) -> Int32 ``` |
| To | ``` func pthread_key_create(_ _: UnsafeMutablePointer<pthread_key_t>, _ _: (@escaping (UnsafeMutableRawPointer) -> Swift.Void)?) -> Int32 ``` |

Modified pthread_mutex_init(_: UnsafeMutablePointer<pthread_mutex_t>, _: UnsafePointer<pthread_mutexattr_t>?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_mutex_init(_ _: UnsafeMutablePointer<pthread_mutex_t>, _ _: UnsafePointer<pthread_mutexattr_t>) -> Int32 ``` |
| To | ``` func pthread_mutex_init(_ _: UnsafeMutablePointer<pthread_mutex_t>, _ _: UnsafePointer<pthread_mutexattr_t>?) -> Int32 ``` |

Modified pthread_override_t

|  | Declaration |
| --- | --- |
| From | ``` typealias pthread_override_t = COpaquePointer ``` |
| To | ``` typealias pthread_override_t = OpaquePointer ``` |

Modified pthread_rwlock_init(_: UnsafeMutablePointer<pthread_rwlock_t>, _: UnsafePointer<pthread_rwlockattr_t>?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_rwlock_init(_ _: UnsafeMutablePointer<pthread_rwlock_t>, _ _: UnsafePointer<pthread_rwlockattr_t>) -> Int32 ``` |
| To | ``` func pthread_rwlock_init(_ _: UnsafeMutablePointer<pthread_rwlock_t>, _ _: UnsafePointer<pthread_rwlockattr_t>?) -> Int32 ``` |

Modified pthread_setcancelstate(_: Int32, _: UnsafeMutablePointer<Int32>?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_setcancelstate(_ _: Int32, _ _: UnsafeMutablePointer<Int32>) -> Int32 ``` |
| To | ``` func pthread_setcancelstate(_ _: Int32, _ _: UnsafeMutablePointer<Int32>?) -> Int32 ``` |

Modified pthread_setcanceltype(_: Int32, _: UnsafeMutablePointer<Int32>?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_setcanceltype(_ _: Int32, _ _: UnsafeMutablePointer<Int32>) -> Int32 ``` |
| To | ``` func pthread_setcanceltype(_ _: Int32, _ _: UnsafeMutablePointer<Int32>?) -> Int32 ``` |

Modified pthread_setspecific(_: pthread_key_t, _: UnsafeRawPointer?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_setspecific(_ _: pthread_key_t, _ _: UnsafePointer<Void>) -> Int32 ``` |
| To | ``` func pthread_setspecific(_ _: pthread_key_t, _ _: UnsafeRawPointer?) -> Int32 ``` |

Modified pthread_sigmask(_: Int32, _: UnsafePointer<sigset_t>?, _: UnsafeMutablePointer<sigset_t>?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_sigmask(_ _: Int32, _ _: UnsafePointer<sigset_t>, _ _: UnsafeMutablePointer<sigset_t>) -> Int32 ``` |
| To | ``` func pthread_sigmask(_ _: Int32, _ _: UnsafePointer<sigset_t>?, _ _: UnsafeMutablePointer<sigset_t>?) -> Int32 ``` |

Modified pthread_threadid_np(_: pthread_t?, _: UnsafeMutablePointer<__uint64_t>?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_threadid_np(_ _: pthread_t, _ _: UnsafeMutablePointer<__uint64_t>) -> Int32 ``` |
| To | ``` func pthread_threadid_np(_ _: pthread_t?, _ _: UnsafeMutablePointer<__uint64_t>?) -> Int32 ``` |

Modified PTRDIFF_MAX

|  | Declaration |
| --- | --- |
| From | ``` var PTRDIFF_MAX: Int32 { get } ``` |
| To | ``` var PTRDIFF_MAX: Int64 { get } ``` |

Modified ptsname(_: Int32) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func ptsname(_ _: Int32) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func ptsname(_ _: Int32) -> UnsafeMutablePointer<Int8>! ``` |

Modified putc(_: Int32, _: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func putc(_ _: Int32, _ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func putc(_ _: Int32, _ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified putc_unlocked(_: Int32, _: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func putc_unlocked(_ _: Int32, _ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func putc_unlocked(_ _: Int32, _ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified putenv(_: UnsafeMutablePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func putenv(_ _: UnsafeMutablePointer<Int8>) -> Int32 ``` |
| To | ``` func putenv(_ _: UnsafeMutablePointer<Int8>!) -> Int32 ``` |

Modified puts(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func puts(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func puts(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified pututxline(_: UnsafePointer<utmpx>!) -> UnsafeMutablePointer<utmpx>!

|  | Declaration |
| --- | --- |
| From | ``` func pututxline(_ _: UnsafePointer<utmpx>) -> UnsafeMutablePointer<utmpx> ``` |
| To | ``` func pututxline(_ _: UnsafePointer<utmpx>!) -> UnsafeMutablePointer<utmpx>! ``` |

Modified putw(_: Int32, _: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func putw(_ _: Int32, _ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func putw(_ _: Int32, _ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified putwc(_: wchar_t, _: UnsafeMutablePointer<FILE>!) -> wint_t

|  | Declaration |
| --- | --- |
| From | ``` func putwc(_ _: wchar_t, _ _: UnsafeMutablePointer<FILE>) -> wint_t ``` |
| To | ``` func putwc(_ _: wchar_t, _ _: UnsafeMutablePointer<FILE>!) -> wint_t ``` |

Modified putwc_l(_: wchar_t, _: UnsafeMutablePointer<FILE>!, _: locale_t!) -> wint_t

|  | Declaration |
| --- | --- |
| From | ``` func putwc_l(_ _: wchar_t, _ _: UnsafeMutablePointer<FILE>, _ _: locale_t) -> wint_t ``` |
| To | ``` func putwc_l(_ _: wchar_t, _ _: UnsafeMutablePointer<FILE>!, _ _: locale_t!) -> wint_t ``` |

Modified putwchar_l(_: wchar_t, _: locale_t!) -> wint_t

|  | Declaration |
| --- | --- |
| From | ``` func putwchar_l(_ _: wchar_t, _ _: locale_t) -> wint_t ``` |
| To | ``` func putwchar_l(_ _: wchar_t, _ _: locale_t!) -> wint_t ``` |

Modified pwrite(_: Int32, _: UnsafeRawPointer!, _: Int, _: off_t) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func pwrite(_ _: Int32, _ _: UnsafePointer<Void>, _ _: Int, _ _: off_t) -> Int ``` |
| To | ``` func pwrite(_ __fd: Int32, _ __buf: UnsafeRawPointer!, _ __nbyte: Int, _ __offset: off_t) -> Int ``` |

Modified qsort(_: UnsafeMutableRawPointer!, _: Int, _: Int, _: (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)

|  | Declaration |
| --- | --- |
| From | ``` func qsort(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) ``` |
| To | ``` func qsort(_ __base: UnsafeMutableRawPointer!, _ __nel: Int, _ __width: Int, _ __compar: @escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) ``` |

Modified qsort_b(_: UnsafeMutableRawPointer!, _: Int, _: Int, _: (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)

|  | Declaration |
| --- | --- |
| From | ``` func qsort_b(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) ``` |
| To | ``` func qsort_b(_ __base: UnsafeMutableRawPointer!, _ __nel: Int, _ __width: Int, _ __compar: @escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) ``` |

Modified qsort_r(_: UnsafeMutableRawPointer!, _: Int, _: Int, _: UnsafeMutableRawPointer!, _: (UnsafeMutableRawPointer?, UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)

|  | Declaration |
| --- | --- |
| From | ``` func qsort_r(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: ((UnsafeMutablePointer<Void>, UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) ``` |
| To | ``` func qsort_r(_ __base: UnsafeMutableRawPointer!, _ __nel: Int, _ __width: Int, _ _: UnsafeMutableRawPointer!, _ __compar: @escaping (UnsafeMutableRawPointer?, UnsafeRawPointer?, UnsafeRawPointer?) -> Int32) ``` |

Modified querylocale(_: Int32, _: locale_t!) -> UnsafePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func querylocale(_ _: Int32, _ _: locale_t) -> UnsafePointer<Int8> ``` |
| To | ``` func querylocale(_ _: Int32, _ _: locale_t!) -> UnsafePointer<Int8>! ``` |

Modified quotactl(_: UnsafePointer<Int8>!, _: Int32, _: Int32, _: caddr_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func quotactl(_ _: UnsafePointer<Int8>, _ _: Int32, _ _: Int32, _ _: caddr_t) -> Int32 ``` |
| To | ``` func quotactl(_ _: UnsafePointer<Int8>!, _ _: Int32, _ _: Int32, _ _: caddr_t!) -> Int32 ``` |

Modified radixsort(_: UnsafeMutablePointer<UnsafePointer<UInt8>?>!, _: Int32, _: UnsafePointer<UInt8>!, _: UInt32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func radixsort(_ _: UnsafeMutablePointer<UnsafePointer<UInt8>>, _ _: Int32, _ _: UnsafePointer<UInt8>, _ _: UInt32) -> Int32 ``` |
| To | ``` func radixsort(_ __base: UnsafeMutablePointer<UnsafePointer<UInt8>?>!, _ __nel: Int32, _ __table: UnsafePointer<UInt8>!, _ __endbyte: UInt32) -> Int32 ``` |

Modified rb_tree_count(_: UnsafeMutablePointer<rb_tree_t>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func rb_tree_count(_ _: UnsafeMutablePointer<rb_tree_t>) -> Int ``` |
| To | ``` func rb_tree_count(_ _: UnsafeMutablePointer<rb_tree_t>!) -> Int ``` |

Modified rb_tree_find_node(_: UnsafeMutablePointer<rb_tree_t>!, _: UnsafeRawPointer!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func rb_tree_find_node(_ _: UnsafeMutablePointer<rb_tree_t>, _ _: UnsafePointer<Void>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func rb_tree_find_node(_ _: UnsafeMutablePointer<rb_tree_t>!, _ _: UnsafeRawPointer!) -> UnsafeMutableRawPointer! ``` |

Modified rb_tree_find_node_geq(_: UnsafeMutablePointer<rb_tree_t>!, _: UnsafeRawPointer!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func rb_tree_find_node_geq(_ _: UnsafeMutablePointer<rb_tree_t>, _ _: UnsafePointer<Void>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func rb_tree_find_node_geq(_ _: UnsafeMutablePointer<rb_tree_t>!, _ _: UnsafeRawPointer!) -> UnsafeMutableRawPointer! ``` |

Modified rb_tree_find_node_leq(_: UnsafeMutablePointer<rb_tree_t>!, _: UnsafeRawPointer!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func rb_tree_find_node_leq(_ _: UnsafeMutablePointer<rb_tree_t>, _ _: UnsafePointer<Void>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func rb_tree_find_node_leq(_ _: UnsafeMutablePointer<rb_tree_t>!, _ _: UnsafeRawPointer!) -> UnsafeMutableRawPointer! ``` |

Modified rb_tree_init(_: UnsafeMutablePointer<rb_tree_t>!, _: UnsafePointer<rb_tree_ops_t>!)

|  | Declaration |
| --- | --- |
| From | ``` func rb_tree_init(_ _: UnsafeMutablePointer<rb_tree_t>, _ _: UnsafePointer<rb_tree_ops_t>) ``` |
| To | ``` func rb_tree_init(_ _: UnsafeMutablePointer<rb_tree_t>!, _ _: UnsafePointer<rb_tree_ops_t>!) ``` |

Modified rb_tree_insert_node(_: UnsafeMutablePointer<rb_tree_t>!, _: UnsafeMutableRawPointer!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func rb_tree_insert_node(_ _: UnsafeMutablePointer<rb_tree_t>, _ _: UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func rb_tree_insert_node(_ _: UnsafeMutablePointer<rb_tree_t>!, _ _: UnsafeMutableRawPointer!) -> UnsafeMutableRawPointer! ``` |

Modified rb_tree_iterate(_: UnsafeMutablePointer<rb_tree_t>!, _: UnsafeMutableRawPointer!, _: UInt32) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func rb_tree_iterate(_ _: UnsafeMutablePointer<rb_tree_t>, _ _: UnsafeMutablePointer<Void>, _ _: UInt32) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func rb_tree_iterate(_ _: UnsafeMutablePointer<rb_tree_t>!, _ _: UnsafeMutableRawPointer!, _ _: UInt32) -> UnsafeMutableRawPointer! ``` |

Modified rb_tree_remove_node(_: UnsafeMutablePointer<rb_tree_t>!, _: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func rb_tree_remove_node(_ _: UnsafeMutablePointer<rb_tree_t>, _ _: UnsafeMutablePointer<Void>) ``` |
| To | ``` func rb_tree_remove_node(_ _: UnsafeMutablePointer<rb_tree_t>!, _ _: UnsafeMutableRawPointer!) ``` |

Modified rbto_compare_key_fn

|  | Declaration |
| --- | --- |
| From | ``` typealias rbto_compare_key_fn = (UnsafeMutablePointer<Void>, UnsafePointer<Void>, UnsafePointer<Void>) -> Int32 ``` |
| To | ``` typealias rbto_compare_key_fn = (UnsafeMutableRawPointer?, UnsafeRawPointer?, UnsafeRawPointer?) -> Int32 ``` |

Modified rbto_compare_nodes_fn

|  | Declaration |
| --- | --- |
| From | ``` typealias rbto_compare_nodes_fn = (UnsafeMutablePointer<Void>, UnsafePointer<Void>, UnsafePointer<Void>) -> Int32 ``` |
| To | ``` typealias rbto_compare_nodes_fn = (UnsafeMutableRawPointer?, UnsafeRawPointer?, UnsafeRawPointer?) -> Int32 ``` |

Modified rcmd(_: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Int32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func rcmd(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Int32>) -> Int32 ``` | -- |
| To | ``` func rcmd(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: Int32, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<Int32>!) -> Int32 ``` | iOS 10.0 |

Modified rcmd_af(_: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Int32>!, _: Int32) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func rcmd_af(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Int32>, _ _: Int32) -> Int32 ``` | -- |
| To | ``` func rcmd_af(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: Int32, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<Int32>!, _ _: Int32) -> Int32 ``` | iOS 10.0 |

Modified read(_: Int32, _: UnsafeMutableRawPointer!, _: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func read(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: Int) -> Int ``` |
| To | ``` func read(_ _: Int32, _ _: UnsafeMutableRawPointer!, _ _: Int) -> Int ``` |

Modified readdir(_: UnsafeMutablePointer<DIR>!) -> UnsafeMutablePointer<dirent>!

|  | Declaration |
| --- | --- |
| From | ``` func readdir(_ _: UnsafeMutablePointer<DIR>) -> UnsafeMutablePointer<dirent> ``` |
| To | ``` func readdir(_ _: UnsafeMutablePointer<DIR>!) -> UnsafeMutablePointer<dirent>! ``` |

Modified readdir_r(_: UnsafeMutablePointer<DIR>!, _: UnsafeMutablePointer<dirent>!, _: UnsafeMutablePointer<UnsafeMutablePointer<dirent>?>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func readdir_r(_ _: UnsafeMutablePointer<DIR>, _ _: UnsafeMutablePointer<dirent>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<dirent>>) -> Int32 ``` |
| To | ``` func readdir_r(_ _: UnsafeMutablePointer<DIR>!, _ _: UnsafeMutablePointer<dirent>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<dirent>?>!) -> Int32 ``` |

Modified readlink(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Int8>!, _: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func readlink(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Int8>, _ _: Int) -> Int ``` |
| To | ``` func readlink(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<Int8>!, _ _: Int) -> Int ``` |

Modified readlinkat(_: Int32, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Int8>!, _: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func readlinkat(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Int8>, _ _: Int) -> Int ``` |
| To | ``` func readlinkat(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<Int8>!, _ _: Int) -> Int ``` |

Modified readpassphrase(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Int8>!, _: Int, _: Int32) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func readpassphrase(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: Int32) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func readpassphrase(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<Int8>!, _ _: Int, _ _: Int32) -> UnsafeMutablePointer<Int8>! ``` |

Modified readv(_: Int32, _: UnsafePointer<iovec>!, _: Int32) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func readv(_ _: Int32, _ _: UnsafePointer<iovec>, _ _: Int32) -> Int ``` |
| To | ``` func readv(_ _: Int32, _ _: UnsafePointer<iovec>!, _ _: Int32) -> Int ``` |

Modified realloc(_: UnsafeMutableRawPointer!, _: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func realloc(_ _: UnsafeMutablePointer<Void>, _ _: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func realloc(_ __ptr: UnsafeMutableRawPointer!, _ __size: Int) -> UnsafeMutableRawPointer! ``` |

Modified reallocf(_: UnsafeMutableRawPointer!, _: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func reallocf(_ _: UnsafeMutablePointer<Void>, _ _: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func reallocf(_ __ptr: UnsafeMutableRawPointer!, _ __size: Int) -> UnsafeMutableRawPointer! ``` |

Modified realpath(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func realpath(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func realpath(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified recv(_: Int32, _: UnsafeMutableRawPointer!, _: Int, _: Int32) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func recv(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32) -> Int ``` |
| To | ``` func recv(_ _: Int32, _ _: UnsafeMutableRawPointer!, _ _: Int, _ _: Int32) -> Int ``` |

Modified recvfrom(_: Int32, _: UnsafeMutableRawPointer!, _: Int, _: Int32, _: UnsafeMutablePointer<sockaddr>!, _: UnsafeMutablePointer<socklen_t>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func recvfrom(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32, _ _: UnsafeMutablePointer<sockaddr>, _ _: UnsafeMutablePointer<socklen_t>) -> Int ``` |
| To | ``` func recvfrom(_ _: Int32, _ _: UnsafeMutableRawPointer!, _ _: Int, _ _: Int32, _ _: UnsafeMutablePointer<sockaddr>!, _ _: UnsafeMutablePointer<socklen_t>!) -> Int ``` |

Modified recvmsg(_: Int32, _: UnsafeMutablePointer<msghdr>!, _: Int32) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func recvmsg(_ _: Int32, _ _: UnsafeMutablePointer<msghdr>, _ _: Int32) -> Int ``` |
| To | ``` func recvmsg(_ _: Int32, _ _: UnsafeMutablePointer<msghdr>!, _ _: Int32) -> Int ``` |

Modified regcomp(_: UnsafeMutablePointer<regex_t>!, _: UnsafePointer<Int8>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func regcomp(_ _: UnsafeMutablePointer<regex_t>, _ _: UnsafePointer<Int8>, _ _: Int32) -> Int32 ``` |
| To | ``` func regcomp(_ _: UnsafeMutablePointer<regex_t>!, _ _: UnsafePointer<Int8>!, _ _: Int32) -> Int32 ``` |

Modified regerror(_: Int32, _: UnsafePointer<regex_t>!, _: UnsafeMutablePointer<Int8>!, _: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func regerror(_ _: Int32, _ _: UnsafePointer<regex_t>, _ _: UnsafeMutablePointer<Int8>, _ _: Int) -> Int ``` |
| To | ``` func regerror(_ _: Int32, _ _: UnsafePointer<regex_t>!, _ _: UnsafeMutablePointer<Int8>!, _ _: Int) -> Int ``` |

Modified regexec(_: UnsafePointer<regex_t>!, _: UnsafePointer<Int8>!, _: Int, _: UnsafeMutablePointer<regmatch_t>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func regexec(_ _: UnsafePointer<regex_t>, _ _: UnsafePointer<Int8>, _ _: Int, _ __pmatch: UnsafeMutablePointer<regmatch_t>, _ _: Int32) -> Int32 ``` |
| To | ``` func regexec(_ _: UnsafePointer<regex_t>!, _ _: UnsafePointer<Int8>!, _ _: Int, _ __pmatch: UnsafeMutablePointer<regmatch_t>!, _ _: Int32) -> Int32 ``` |

Modified regfree(_: UnsafeMutablePointer<regex_t>!)

|  | Declaration |
| --- | --- |
| From | ``` func regfree(_ _: UnsafeMutablePointer<regex_t>) ``` |
| To | ``` func regfree(_ _: UnsafeMutablePointer<regex_t>!) ``` |

Modified register_t

|  | Declaration |
| --- | --- |
| From | ``` typealias register_t = Int32 ``` |
| To | ``` typealias register_t = Int64 ``` |

Modified regncomp(_: UnsafeMutablePointer<regex_t>!, _: UnsafePointer<Int8>!, _: Int, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func regncomp(_ _: UnsafeMutablePointer<regex_t>, _ _: UnsafePointer<Int8>, _ _: Int, _ _: Int32) -> Int32 ``` |
| To | ``` func regncomp(_ _: UnsafeMutablePointer<regex_t>!, _ _: UnsafePointer<Int8>!, _ _: Int, _ _: Int32) -> Int32 ``` |

Modified regnexec(_: UnsafePointer<regex_t>!, _: UnsafePointer<Int8>!, _: Int, _: Int, _: UnsafeMutablePointer<regmatch_t>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func regnexec(_ _: UnsafePointer<regex_t>, _ _: UnsafePointer<Int8>, _ _: Int, _ _: Int, _ __pmatch: UnsafeMutablePointer<regmatch_t>, _ _: Int32) -> Int32 ``` |
| To | ``` func regnexec(_ _: UnsafePointer<regex_t>!, _ _: UnsafePointer<Int8>!, _ _: Int, _ _: Int, _ __pmatch: UnsafeMutablePointer<regmatch_t>!, _ _: Int32) -> Int32 ``` |

Modified regwcomp(_: UnsafeMutablePointer<regex_t>!, _: UnsafePointer<wchar_t>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func regwcomp(_ _: UnsafeMutablePointer<regex_t>, _ _: UnsafePointer<wchar_t>, _ _: Int32) -> Int32 ``` |
| To | ``` func regwcomp(_ _: UnsafeMutablePointer<regex_t>!, _ _: UnsafePointer<wchar_t>!, _ _: Int32) -> Int32 ``` |

Modified regwexec(_: UnsafePointer<regex_t>!, _: UnsafePointer<wchar_t>!, _: Int, _: UnsafeMutablePointer<regmatch_t>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func regwexec(_ _: UnsafePointer<regex_t>, _ _: UnsafePointer<wchar_t>, _ _: Int, _ __pmatch: UnsafeMutablePointer<regmatch_t>, _ _: Int32) -> Int32 ``` |
| To | ``` func regwexec(_ _: UnsafePointer<regex_t>!, _ _: UnsafePointer<wchar_t>!, _ _: Int, _ __pmatch: UnsafeMutablePointer<regmatch_t>!, _ _: Int32) -> Int32 ``` |

Modified regwncomp(_: UnsafeMutablePointer<regex_t>!, _: UnsafePointer<wchar_t>!, _: Int, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func regwncomp(_ _: UnsafeMutablePointer<regex_t>, _ _: UnsafePointer<wchar_t>, _ _: Int, _ _: Int32) -> Int32 ``` |
| To | ``` func regwncomp(_ _: UnsafeMutablePointer<regex_t>!, _ _: UnsafePointer<wchar_t>!, _ _: Int, _ _: Int32) -> Int32 ``` |

Modified regwnexec(_: UnsafePointer<regex_t>!, _: UnsafePointer<wchar_t>!, _: Int, _: Int, _: UnsafeMutablePointer<regmatch_t>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func regwnexec(_ _: UnsafePointer<regex_t>, _ _: UnsafePointer<wchar_t>, _ _: Int, _ _: Int, _ __pmatch: UnsafeMutablePointer<regmatch_t>, _ _: Int32) -> Int32 ``` |
| To | ``` func regwnexec(_ _: UnsafePointer<regex_t>!, _ _: UnsafePointer<wchar_t>!, _ _: Int, _ _: Int, _ __pmatch: UnsafeMutablePointer<regmatch_t>!, _ _: Int32) -> Int32 ``` |

Modified remove(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func remove(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func remove(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified removexattr(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func removexattr(_ path: UnsafePointer<Int8>, _ name: UnsafePointer<Int8>, _ options: Int32) -> Int32 ``` |
| To | ``` func removexattr(_ path: UnsafePointer<Int8>!, _ name: UnsafePointer<Int8>!, _ options: Int32) -> Int32 ``` |

Modified remque(_: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func remque(_ _: UnsafeMutablePointer<Void>) ``` |
| To | ``` func remque(_ _: UnsafeMutableRawPointer!) ``` |

Modified remquo(_: Float, _: Float) -> (Float, Int)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func remquo(_ x: Float, _ y: Float) -> (Float, Int) ``` |
| To | ``` func remquo(_ x: Float, _ y: Float) -> (Float, Int) ``` |

Modified remquo(_: Double, _: Double) -> (Double, Int)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func remquo(_ x: Double, _ y: Double) -> (Double, Int) ``` |
| To | ``` func remquo(_ x: Double, _ y: Double) -> (Double, Int) ``` |

Modified remquo(_: Double, _: Double, _: UnsafeMutablePointer<Int32>!) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func remquo(_ _: Double, _ _: Double, _ _: UnsafeMutablePointer<Int32>) -> Double ``` |
| To | ``` func remquo(_ _: Double, _ _: Double, _ _: UnsafeMutablePointer<Int32>!) -> Double ``` |

Modified remquof(_: Float, _: Float, _: UnsafeMutablePointer<Int32>!) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func remquof(_ _: Float, _ _: Float, _ _: UnsafeMutablePointer<Int32>) -> Float ``` |
| To | ``` func remquof(_ _: Float, _ _: Float, _ _: UnsafeMutablePointer<Int32>!) -> Float ``` |

Modified rename(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func rename(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func rename(_ __old: UnsafePointer<Int8>!, _ __new: UnsafePointer<Int8>!) -> Int32 ``` |

Modified renameat(_: Int32, _: UnsafePointer<Int8>!, _: Int32, _: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func renameat(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: Int32, _ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func renameat(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: Int32, _ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified revoke(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func revoke(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func revoke(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified rewind(_: UnsafeMutablePointer<FILE>!)

|  | Declaration |
| --- | --- |
| From | ``` func rewind(_ _: UnsafeMutablePointer<FILE>) ``` |
| To | ``` func rewind(_ _: UnsafeMutablePointer<FILE>!) ``` |

Modified rewinddir(_: UnsafeMutablePointer<DIR>!)

|  | Declaration |
| --- | --- |
| From | ``` func rewinddir(_ _: UnsafeMutablePointer<DIR>) ``` |
| To | ``` func rewinddir(_ _: UnsafeMutablePointer<DIR>!) ``` |

Modified rindex(_: UnsafePointer<Int8>!, _: Int32) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func rindex(_ _: UnsafePointer<Int8>, _ _: Int32) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func rindex(_ _: UnsafePointer<Int8>!, _ _: Int32) -> UnsafeMutablePointer<Int8>! ``` |

Modified rint(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func rint(_ x: Float) -> Float ``` |
| To | ``` func rint(_ x: Float) -> Float ``` |

Modified rint(_: Double) -> Double

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func rint(_ x: Double) -> Double ``` |
| To | ``` func rint(_ x: Double) -> Double ``` |

Modified rmdir(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func rmdir(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func rmdir(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified rresvport(_: UnsafeMutablePointer<Int32>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func rresvport(_ _: UnsafeMutablePointer<Int32>) -> Int32 ``` | -- |
| To | ``` func rresvport(_ _: UnsafeMutablePointer<Int32>!) -> Int32 ``` | iOS 10.0 |

Modified rresvport_af(_: UnsafeMutablePointer<Int32>!, _: Int32) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func rresvport_af(_ _: UnsafeMutablePointer<Int32>, _ _: Int32) -> Int32 ``` | -- |
| To | ``` func rresvport_af(_ _: UnsafeMutablePointer<Int32>!, _ _: Int32) -> Int32 ``` | iOS 10.0 |

Modified rusage_info_t

|  | Declaration |
| --- | --- |
| From | ``` typealias rusage_info_t = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias rusage_info_t = UnsafeMutableRawPointer ``` |

Modified ruserok(_: UnsafePointer<Int8>!, _: Int32, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> Int32

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func ruserok(_ _: UnsafePointer<Int8>, _ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> Int32 ``` | -- |
| To | ``` func ruserok(_ _: UnsafePointer<Int8>!, _ _: Int32, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!) -> Int32 ``` | iOS 10.0 |

Modified safe_gets(_: UnsafeMutablePointer<Int8>!, _: UnsafeMutablePointer<Int8>!, _: Int32)

|  | Declaration |
| --- | --- |
| From | ``` func safe_gets(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<Int8>, _ _: Int32) ``` |
| To | ``` func safe_gets(_ _: UnsafeMutablePointer<Int8>!, _ _: UnsafeMutablePointer<Int8>!, _ _: Int32) ``` |

Modified sbrk(_: Int32) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func sbrk(_ _: Int32) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func sbrk(_ _: Int32) -> UnsafeMutableRawPointer! ``` |

Modified scalbn(_: Double, _: Int) -> Double

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func scalbn(_ x: Double, _ n: Int) -> Double ``` |
| To | ``` func scalbn(_ x: Double, _ n: Int) -> Double ``` |

Modified scalbn(_: Float, _: Int) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func scalbn(_ x: Float, _ n: Int) -> Float ``` |
| To | ``` func scalbn(_ x: Float, _ n: Int) -> Float ``` |

Modified scandir(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<dirent>?>?>!, _: ( (UnsafePointer<dirent>?) -> Int32)!, _: ( (UnsafeMutablePointer<UnsafePointer<dirent>?>?, UnsafeMutablePointer<UnsafePointer<dirent>?>?) -> Int32)!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func scandir(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<dirent>>>, _ _: ((UnsafePointer<dirent>) -> Int32)!, _ _: ((UnsafeMutablePointer<UnsafePointer<dirent>>, UnsafeMutablePointer<UnsafePointer<dirent>>) -> Int32)!) -> Int32 ``` |
| To | ``` func scandir(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<dirent>?>?>!, _ _: (@escaping (UnsafePointer<dirent>?) -> Int32)!, _ _: (@escaping (UnsafeMutablePointer<UnsafePointer<dirent>?>?, UnsafeMutablePointer<UnsafePointer<dirent>?>?) -> Int32)!) -> Int32 ``` |

Modified scandir_b(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<dirent>?>?>!, _: ( (UnsafePointer<dirent>?) -> Int32)!, _: ( (UnsafeMutablePointer<UnsafePointer<dirent>?>?, UnsafeMutablePointer<UnsafePointer<dirent>?>?) -> Int32)!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func scandir_b(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<dirent>>>, _ _: ((UnsafePointer<dirent>) -> Int32)!, _ _: ((UnsafeMutablePointer<UnsafePointer<dirent>>, UnsafeMutablePointer<UnsafePointer<dirent>>) -> Int32)!) -> Int32 ``` |
| To | ``` func scandir_b(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<dirent>?>?>!, _ _: (@escaping (UnsafePointer<dirent>?) -> Int32)!, _ _: (@escaping (UnsafeMutablePointer<UnsafePointer<dirent>?>?, UnsafeMutablePointer<UnsafePointer<dirent>?>?) -> Int32)!) -> Int32 ``` |

Modified searchfs(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<fssearchblock>!, _: UnsafeMutablePointer<UInt>!, _: UInt32, _: UInt32, _: UnsafeMutablePointer<searchstate>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func searchfs(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<fssearchblock>, _ _: UnsafeMutablePointer<UInt>, _ _: UInt32, _ _: UInt32, _ _: UnsafeMutablePointer<searchstate>) -> Int32 ``` |
| To | ``` func searchfs(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<fssearchblock>!, _ _: UnsafeMutablePointer<UInt>!, _ _: UInt32, _ _: UInt32, _ _: UnsafeMutablePointer<searchstate>!) -> Int32 ``` |

Modified seed48(_: UnsafeMutablePointer<UInt16>!) -> UnsafeMutablePointer<UInt16>!

|  | Declaration |
| --- | --- |
| From | ``` func seed48(_ _: UnsafeMutablePointer<UInt16>) -> UnsafeMutablePointer<UInt16> ``` |
| To | ``` func seed48(_ _: UnsafeMutablePointer<UInt16>!) -> UnsafeMutablePointer<UInt16>! ``` |

Modified seekdir(_: UnsafeMutablePointer<DIR>!, _: Int)

|  | Declaration |
| --- | --- |
| From | ``` func seekdir(_ _: UnsafeMutablePointer<DIR>, _ _: Int) ``` |
| To | ``` func seekdir(_ _: UnsafeMutablePointer<DIR>!, _ _: Int) ``` |

Modified select(_: Int32, _: UnsafeMutablePointer<fd_set>!, _: UnsafeMutablePointer<fd_set>!, _: UnsafeMutablePointer<fd_set>!, _: UnsafeMutablePointer<timeval>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func select(_ _: Int32, _ _: UnsafeMutablePointer<fd_set>, _ _: UnsafeMutablePointer<fd_set>, _ _: UnsafeMutablePointer<fd_set>, _ _: UnsafeMutablePointer<timeval>) -> Int32 ``` |
| To | ``` func select(_ _: Int32, _ _: UnsafeMutablePointer<fd_set>!, _ _: UnsafeMutablePointer<fd_set>!, _ _: UnsafeMutablePointer<fd_set>!, _ _: UnsafeMutablePointer<timeval>!) -> Int32 ``` |

Modified sem_close(_: UnsafeMutablePointer<sem_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sem_close(_ _: UnsafeMutablePointer<sem_t>) -> Int32 ``` |
| To | ``` func sem_close(_ _: UnsafeMutablePointer<sem_t>!) -> Int32 ``` |

Modified sem_destroy(_: UnsafeMutablePointer<sem_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sem_destroy(_ _: UnsafeMutablePointer<sem_t>) -> Int32 ``` |
| To | ``` func sem_destroy(_ _: UnsafeMutablePointer<sem_t>!) -> Int32 ``` |

Modified SEM_FAILED

|  | Declaration |
| --- | --- |
| From | ``` var SEM_FAILED: UnsafeMutablePointer<sem_t> { get } ``` |
| To | ``` var SEM_FAILED: UnsafeMutablePointer<sem_t>? { get } ``` |

Modified sem_getvalue(_: UnsafeMutablePointer<sem_t>!, _: UnsafeMutablePointer<Int32>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sem_getvalue(_ _: UnsafeMutablePointer<sem_t>, _ _: UnsafeMutablePointer<Int32>) -> Int32 ``` |
| To | ``` func sem_getvalue(_ _: UnsafeMutablePointer<sem_t>!, _ _: UnsafeMutablePointer<Int32>!) -> Int32 ``` |

Modified sem_init(_: UnsafeMutablePointer<sem_t>!, _: Int32, _: UInt32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sem_init(_ _: UnsafeMutablePointer<sem_t>, _ _: Int32, _ _: UInt32) -> Int32 ``` |
| To | ``` func sem_init(_ _: UnsafeMutablePointer<sem_t>!, _ _: Int32, _ _: UInt32) -> Int32 ``` |

Modified sem_post(_: UnsafeMutablePointer<sem_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sem_post(_ _: UnsafeMutablePointer<sem_t>) -> Int32 ``` |
| To | ``` func sem_post(_ _: UnsafeMutablePointer<sem_t>!) -> Int32 ``` |

Modified sem_trywait(_: UnsafeMutablePointer<sem_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sem_trywait(_ _: UnsafeMutablePointer<sem_t>) -> Int32 ``` |
| To | ``` func sem_trywait(_ _: UnsafeMutablePointer<sem_t>!) -> Int32 ``` |

Modified sem_unlink(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sem_unlink(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func sem_unlink(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified sem_wait(_: UnsafeMutablePointer<sem_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sem_wait(_ _: UnsafeMutablePointer<sem_t>) -> Int32 ``` |
| To | ``` func sem_wait(_ _: UnsafeMutablePointer<sem_t>!) -> Int32 ``` |

Modified semaphore_create(_: task_t, _: UnsafeMutablePointer<semaphore_t>!, _: Int32, _: Int32) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func semaphore_create(_ task: task_t, _ semaphore: UnsafeMutablePointer<semaphore_t>, _ policy: Int32, _ value: Int32) -> kern_return_t ``` |
| To | ``` func semaphore_create(_ task: task_t, _ semaphore: UnsafeMutablePointer<semaphore_t>!, _ policy: Int32, _ value: Int32) -> kern_return_t ``` |

Modified semop(_: Int32, _: UnsafeMutablePointer<sembuf>!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func semop(_ _: Int32, _ _: UnsafeMutablePointer<sembuf>, _ _: Int) -> Int32 ``` |
| To | ``` func semop(_ _: Int32, _ _: UnsafeMutablePointer<sembuf>!, _ _: Int) -> Int32 ``` |

Modified send(_: Int32, _: UnsafeRawPointer!, _: Int, _: Int32) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func send(_ _: Int32, _ _: UnsafePointer<Void>, _ _: Int, _ _: Int32) -> Int ``` |
| To | ``` func send(_ _: Int32, _ _: UnsafeRawPointer!, _ _: Int, _ _: Int32) -> Int ``` |

Modified sendfile(_: Int32, _: Int32, _: off_t, _: UnsafeMutablePointer<off_t>!, _: UnsafeMutablePointer<sf_hdtr>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sendfile(_ _: Int32, _ _: Int32, _ _: off_t, _ _: UnsafeMutablePointer<off_t>, _ _: UnsafeMutablePointer<sf_hdtr>, _ _: Int32) -> Int32 ``` |
| To | ``` func sendfile(_ _: Int32, _ _: Int32, _ _: off_t, _ _: UnsafeMutablePointer<off_t>!, _ _: UnsafeMutablePointer<sf_hdtr>!, _ _: Int32) -> Int32 ``` |

Modified sendmsg(_: Int32, _: UnsafePointer<msghdr>!, _: Int32) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func sendmsg(_ _: Int32, _ _: UnsafePointer<msghdr>, _ _: Int32) -> Int ``` |
| To | ``` func sendmsg(_ _: Int32, _ _: UnsafePointer<msghdr>!, _ _: Int32) -> Int ``` |

Modified sendto(_: Int32, _: UnsafeRawPointer!, _: Int, _: Int32, _: UnsafePointer<sockaddr>!, _: socklen_t) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func sendto(_ _: Int32, _ _: UnsafePointer<Void>, _ _: Int, _ _: Int32, _ _: UnsafePointer<sockaddr>, _ _: socklen_t) -> Int ``` |
| To | ``` func sendto(_ _: Int32, _ _: UnsafeRawPointer!, _ _: Int, _ _: Int32, _ _: UnsafePointer<sockaddr>!, _ _: socklen_t) -> Int ``` |

Modified setattrlist(_: UnsafePointer<Int8>!, _: UnsafeMutableRawPointer!, _: UnsafeMutableRawPointer!, _: Int, _: UInt32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setattrlist(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: UInt) -> Int32 ``` |
| To | ``` func setattrlist(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutableRawPointer!, _ _: Int, _ _: UInt32) -> Int32 ``` |

Modified setaudit_addr(_: UnsafePointer<auditinfo_addr>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setaudit_addr(_ _: UnsafePointer<auditinfo_addr>, _ _: Int32) -> Int32 ``` |
| To | ``` func setaudit_addr(_ _: UnsafePointer<auditinfo_addr>!, _ _: Int32) -> Int32 ``` |

Modified setauid(_: UnsafePointer<au_id_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setauid(_ _: UnsafePointer<au_id_t>) -> Int32 ``` |
| To | ``` func setauid(_ _: UnsafePointer<au_id_t>!) -> Int32 ``` |

Modified setbuf(_: UnsafeMutablePointer<FILE>!, _: UnsafeMutablePointer<Int8>!)

|  | Declaration |
| --- | --- |
| From | ``` func setbuf(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<Int8>) ``` |
| To | ``` func setbuf(_ _: UnsafeMutablePointer<FILE>!, _ _: UnsafeMutablePointer<Int8>!) ``` |

Modified setbuffer(_: UnsafeMutablePointer<FILE>!, _: UnsafeMutablePointer<Int8>!, _: Int32)

|  | Declaration |
| --- | --- |
| From | ``` func setbuffer(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<Int8>, _ _: Int32) ``` |
| To | ``` func setbuffer(_ _: UnsafeMutablePointer<FILE>!, _ _: UnsafeMutablePointer<Int8>!, _ _: Int32) ``` |

Modified setdomainname(_: UnsafePointer<Int8>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setdomainname(_ _: UnsafePointer<Int8>, _ _: Int32) -> Int32 ``` |
| To | ``` func setdomainname(_ _: UnsafePointer<Int8>!, _ _: Int32) -> Int32 ``` |

Modified setenv(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setenv(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int32) -> Int32 ``` |
| To | ``` func setenv(_ __name: UnsafePointer<Int8>!, _ __value: UnsafePointer<Int8>!, _ __overwrite: Int32) -> Int32 ``` |

Modified setgrfile(_: UnsafePointer<Int8>!)

|  | Declaration |
| --- | --- |
| From | ``` func setgrfile(_ _: UnsafePointer<Int8>) ``` |
| To | ``` func setgrfile(_ _: UnsafePointer<Int8>!) ``` |

Modified setgroups(_: Int32, _: UnsafePointer<gid_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setgroups(_ _: Int32, _ _: UnsafePointer<gid_t>) -> Int32 ``` |
| To | ``` func setgroups(_ _: Int32, _ _: UnsafePointer<gid_t>!) -> Int32 ``` |

Modified sethostname(_: UnsafePointer<Int8>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sethostname(_ _: UnsafePointer<Int8>, _ _: Int32) -> Int32 ``` |
| To | ``` func sethostname(_ _: UnsafePointer<Int8>!, _ _: Int32) -> Int32 ``` |

Modified setipv4sourcefilter(_: Int32, _: in_addr, _: in_addr, _: UInt32, _: UInt32, _: UnsafeMutablePointer<in_addr>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setipv4sourcefilter(_ _: Int32, _ _: in_addr, _ _: in_addr, _ _: UInt32, _ _: UInt32, _ _: UnsafeMutablePointer<in_addr>) -> Int32 ``` |
| To | ``` func setipv4sourcefilter(_ _: Int32, _ _: in_addr, _ _: in_addr, _ _: UInt32, _ _: UInt32, _ _: UnsafeMutablePointer<in_addr>!) -> Int32 ``` |

Modified setitimer(_: Int32, _: UnsafePointer<itimerval>!, _: UnsafeMutablePointer<itimerval>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setitimer(_ _: Int32, _ _: UnsafePointer<itimerval>, _ _: UnsafeMutablePointer<itimerval>) -> Int32 ``` |
| To | ``` func setitimer(_ _: Int32, _ _: UnsafePointer<itimerval>!, _ _: UnsafeMutablePointer<itimerval>!) -> Int32 ``` |

Modified setjmp(_: UnsafeMutablePointer<Int32>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setjmp(_ _: UnsafeMutablePointer<Int32>) -> Int32 ``` |
| To | ``` func setjmp(_ _: UnsafeMutablePointer<Int32>!) -> Int32 ``` |

Modified setkey(_: UnsafePointer<Int8>!)

|  | Declaration |
| --- | --- |
| From | ``` func setkey(_ _: UnsafePointer<Int8>) ``` |
| To | ``` func setkey(_ _: UnsafePointer<Int8>!) ``` |

Modified setlinebuf(_: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setlinebuf(_ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func setlinebuf(_ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified setlocale(_: Int32, _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func setlocale(_ _: Int32, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func setlocale(_ _: Int32, _ _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified setlogin(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setlogin(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func setlogin(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified setmode(_: UnsafePointer<Int8>!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func setmode(_ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func setmode(_ _: UnsafePointer<Int8>!) -> UnsafeMutableRawPointer! ``` |

Modified setnetgrent(_: UnsafePointer<Int8>!)

|  | Declaration |
| --- | --- |
| From | ``` func setnetgrent(_ _: UnsafePointer<Int8>) ``` |
| To | ``` func setnetgrent(_ _: UnsafePointer<Int8>!) ``` |

Modified setprogname(_: UnsafePointer<Int8>!)

|  | Declaration |
| --- | --- |
| From | ``` func setprogname(_ _: UnsafePointer<Int8>) ``` |
| To | ``` func setprogname(_ _: UnsafePointer<Int8>!) ``` |

Modified setrlimit(_: Int32, _: UnsafePointer<rlimit>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setrlimit(_ _: Int32, _ _: UnsafePointer<rlimit>) -> Int32 ``` |
| To | ``` func setrlimit(_ _: Int32, _ _: UnsafePointer<rlimit>!) -> Int32 ``` |

Modified setsgroups_np(_: Int32, _: UnsafePointer<UInt8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setsgroups_np(_ _: Int32, _ _: UnsafePointer<UInt8>) -> Int32 ``` |
| To | ``` func setsgroups_np(_ _: Int32, _ _: UnsafePointer<UInt8>!) -> Int32 ``` |

Modified setsockopt(_: Int32, _: Int32, _: Int32, _: UnsafeRawPointer!, _: socklen_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setsockopt(_ _: Int32, _ _: Int32, _ _: Int32, _ _: UnsafePointer<Void>, _ _: socklen_t) -> Int32 ``` |
| To | ``` func setsockopt(_ _: Int32, _ _: Int32, _ _: Int32, _ _: UnsafeRawPointer!, _ _: socklen_t) -> Int32 ``` |

Modified setsourcefilter(_: Int32, _: UInt32, _: UnsafeMutablePointer<sockaddr>!, _: socklen_t, _: UInt32, _: UInt32, _: UnsafeMutablePointer<sockaddr_storage>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setsourcefilter(_ _: Int32, _ _: UInt32, _ _: UnsafeMutablePointer<sockaddr>, _ _: socklen_t, _ _: UInt32, _ _: UInt32, _ _: UnsafeMutablePointer<sockaddr_storage>) -> Int32 ``` |
| To | ``` func setsourcefilter(_ _: Int32, _ _: UInt32, _ _: UnsafeMutablePointer<sockaddr>!, _ _: socklen_t, _ _: UInt32, _ _: UInt32, _ _: UnsafeMutablePointer<sockaddr_storage>!) -> Int32 ``` |

Modified setstate(_: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func setstate(_ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func setstate(_ _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified settimeofday(_: UnsafePointer<timeval>!, _: UnsafePointer<timezone>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func settimeofday(_ _: UnsafePointer<timeval>, _ _: UnsafePointer<timezone>) -> Int32 ``` |
| To | ``` func settimeofday(_ _: UnsafePointer<timeval>!, _ _: UnsafePointer<timezone>!) -> Int32 ``` |

Modified setvbuf(_: UnsafeMutablePointer<FILE>!, _: UnsafeMutablePointer<Int8>!, _: Int32, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setvbuf(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<Int8>, _ _: Int32, _ _: Int) -> Int32 ``` |
| To | ``` func setvbuf(_ _: UnsafeMutablePointer<FILE>!, _ _: UnsafeMutablePointer<Int8>!, _ _: Int32, _ _: Int) -> Int32 ``` |

Modified setwgroups_np(_: Int32, _: UnsafePointer<UInt8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setwgroups_np(_ _: Int32, _ _: UnsafePointer<UInt8>) -> Int32 ``` |
| To | ``` func setwgroups_np(_ _: Int32, _ _: UnsafePointer<UInt8>!) -> Int32 ``` |

Modified setxattr(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafeRawPointer!, _: Int, _: UInt32, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func setxattr(_ path: UnsafePointer<Int8>, _ name: UnsafePointer<Int8>, _ value: UnsafePointer<Void>, _ size: Int, _ position: UInt32, _ options: Int32) -> Int32 ``` |
| To | ``` func setxattr(_ path: UnsafePointer<Int8>!, _ name: UnsafePointer<Int8>!, _ value: UnsafeRawPointer!, _ size: Int, _ position: UInt32, _ options: Int32) -> Int32 ``` |

Modified shm_unlink(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func shm_unlink(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func shm_unlink(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified shmat(_: Int32, _: UnsafeRawPointer!, _: Int32) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func shmat(_ _: Int32, _ _: UnsafePointer<Void>, _ _: Int32) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func shmat(_ _: Int32, _ _: UnsafeRawPointer!, _ _: Int32) -> UnsafeMutableRawPointer! ``` |

Modified shmctl(_: Int32, _: Int32, _: UnsafeMutablePointer<__shmid_ds_new>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func shmctl(_ _: Int32, _ _: Int32, _ _: UnsafeMutablePointer<__shmid_ds_new>) -> Int32 ``` |
| To | ``` func shmctl(_ _: Int32, _ _: Int32, _ _: UnsafeMutablePointer<__shmid_ds_new>!) -> Int32 ``` |

Modified shmdt(_: UnsafeRawPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func shmdt(_ _: UnsafePointer<Void>) -> Int32 ``` |
| To | ``` func shmdt(_ _: UnsafeRawPointer!) -> Int32 ``` |

Modified SIG_DFL

|  | Declaration |
| --- | --- |
| From | ``` var SIG_DFL: sig_t? { get } ``` |
| To | ``` var SIG_DFL: Darwin.sig_t? { get } ``` |

Modified SIG_ERR

|  | Declaration |
| --- | --- |
| From | ``` var SIG_ERR: sig_t { get } ``` |
| To | ``` var SIG_ERR: Darwin.sig_t { get } ``` |

Modified SIG_HOLD

|  | Declaration |
| --- | --- |
| From | ``` var SIG_HOLD: sig_t { get } ``` |
| To | ``` var SIG_HOLD: Darwin.sig_t { get } ``` |

Modified SIG_IGN

|  | Declaration |
| --- | --- |
| From | ``` var SIG_IGN: sig_t { get } ``` |
| To | ``` var SIG_IGN: Darwin.sig_t { get } ``` |

Modified sig_t

|  | Declaration |
| --- | --- |
| From | ``` typealias sig_t = (Int32) -> Void ``` |
| To | ``` typealias sig_t = (Int32) -> Swift.Void ``` |

Modified sigaction(_: Int32, _: UnsafePointer<sigaction>!, _: UnsafeMutablePointer<sigaction>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sigaction(_ _: Int32, _ _: UnsafePointer<sigaction>, _ _: UnsafeMutablePointer<sigaction>) -> Int32 ``` |
| To | ``` func sigaction(_ _: Int32, _ _: UnsafePointer<sigaction>!, _ _: UnsafeMutablePointer<sigaction>!) -> Int32 ``` |

Modified sigaddset(_: UnsafeMutablePointer<sigset_t>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sigaddset(_ _: UnsafeMutablePointer<sigset_t>, _ _: Int32) -> Int32 ``` |
| To | ``` func sigaddset(_ _: UnsafeMutablePointer<sigset_t>!, _ _: Int32) -> Int32 ``` |

Modified sigaltstack(_: UnsafePointer<stack_t>!, _: UnsafeMutablePointer<stack_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sigaltstack(_ _: UnsafePointer<stack_t>, _ _: UnsafeMutablePointer<stack_t>) -> Int32 ``` |
| To | ``` func sigaltstack(_ _: UnsafePointer<stack_t>!, _ _: UnsafeMutablePointer<stack_t>!) -> Int32 ``` |

Modified sigdelset(_: UnsafeMutablePointer<sigset_t>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sigdelset(_ _: UnsafeMutablePointer<sigset_t>, _ _: Int32) -> Int32 ``` |
| To | ``` func sigdelset(_ _: UnsafeMutablePointer<sigset_t>!, _ _: Int32) -> Int32 ``` |

Modified sigemptyset(_: UnsafeMutablePointer<sigset_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sigemptyset(_ _: UnsafeMutablePointer<sigset_t>) -> Int32 ``` |
| To | ``` func sigemptyset(_ _: UnsafeMutablePointer<sigset_t>!) -> Int32 ``` |

Modified sigfillset(_: UnsafeMutablePointer<sigset_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sigfillset(_ _: UnsafeMutablePointer<sigset_t>) -> Int32 ``` |
| To | ``` func sigfillset(_ _: UnsafeMutablePointer<sigset_t>!) -> Int32 ``` |

Modified sigismember(_: UnsafePointer<sigset_t>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sigismember(_ _: UnsafePointer<sigset_t>, _ _: Int32) -> Int32 ``` |
| To | ``` func sigismember(_ _: UnsafePointer<sigset_t>!, _ _: Int32) -> Int32 ``` |

Modified sigjmp_buf

|  | Declaration |
| --- | --- |
| From | ``` typealias sigjmp_buf = (Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32) ``` |
| To | ``` typealias sigjmp_buf = (Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32, Int32) ``` |

Modified siglongjmp(_: UnsafeMutablePointer<Int32>!, _: Int32) -> Never

|  | Declaration |
| --- | --- |
| From | ``` @noreturn func siglongjmp(_ _: UnsafeMutablePointer<Int32>, _ _: Int32) ``` |
| To | ``` func siglongjmp(_ _: UnsafeMutablePointer<Int32>!, _ _: Int32) -> Never ``` |

Modified signal(_: Int32, _: ( (Int32) -> Swift.Void)!) -> ((Int32) -> Swift.Void)!

|  | Declaration |
| --- | --- |
| From | ``` func signal(_ _: Int32, _ _: ((Int32) -> Void)!) -> ((Int32) -> Void)! ``` |
| To | ``` func signal(_ _: Int32, _ _: (@escaping (Int32) -> Swift.Void)!) -> ((Int32) -> Swift.Void)! ``` |

Modified sigpending(_: UnsafeMutablePointer<sigset_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sigpending(_ _: UnsafeMutablePointer<sigset_t>) -> Int32 ``` |
| To | ``` func sigpending(_ _: UnsafeMutablePointer<sigset_t>!) -> Int32 ``` |

Modified sigprocmask(_: Int32, _: UnsafePointer<sigset_t>!, _: UnsafeMutablePointer<sigset_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sigprocmask(_ _: Int32, _ _: UnsafePointer<sigset_t>, _ _: UnsafeMutablePointer<sigset_t>) -> Int32 ``` |
| To | ``` func sigprocmask(_ _: Int32, _ _: UnsafePointer<sigset_t>!, _ _: UnsafeMutablePointer<sigset_t>!) -> Int32 ``` |

Modified sigset(_: Int32, _: ( (Int32) -> Swift.Void)?) -> ((Int32) -> Swift.Void)?

|  | Declaration |
| --- | --- |
| From | ``` func sigset(_ _: Int32, _ _: ((Int32) -> Void)!) -> ((Int32) -> Void)! ``` |
| To | ``` func sigset(_ _: Int32, _ _: (@escaping (Int32) -> Swift.Void)?) -> ((Int32) -> Swift.Void)? ``` |

Modified sigsetjmp(_: UnsafeMutablePointer<Int32>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sigsetjmp(_ _: UnsafeMutablePointer<Int32>, _ _: Int32) -> Int32 ``` |
| To | ``` func sigsetjmp(_ _: UnsafeMutablePointer<Int32>!, _ _: Int32) -> Int32 ``` |

Modified sigsuspend(_: UnsafePointer<sigset_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sigsuspend(_ _: UnsafePointer<sigset_t>) -> Int32 ``` |
| To | ``` func sigsuspend(_ _: UnsafePointer<sigset_t>!) -> Int32 ``` |

Modified sigvec(_: Int32, _: UnsafeMutablePointer<sigvec>!, _: UnsafeMutablePointer<sigvec>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sigvec(_ _: Int32, _ _: UnsafeMutablePointer<sigvec>, _ _: UnsafeMutablePointer<sigvec>) -> Int32 ``` |
| To | ``` func sigvec(_ _: Int32, _ _: UnsafeMutablePointer<sigvec>!, _ _: UnsafeMutablePointer<sigvec>!) -> Int32 ``` |

Modified sigwait(_: UnsafePointer<sigset_t>!, _: UnsafeMutablePointer<Int32>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sigwait(_ _: UnsafePointer<sigset_t>, _ _: UnsafeMutablePointer<Int32>) -> Int32 ``` |
| To | ``` func sigwait(_ _: UnsafePointer<sigset_t>!, _ _: UnsafeMutablePointer<Int32>!) -> Int32 ``` |

Modified sin(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func sin(_ x: Float) -> Float ``` |
| To | ``` func sin(_ x: Float) -> Float ``` |

Modified sin(_: Double) -> Double

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func sin(_ x: Double) -> Double ``` |
| To | ``` func sin(_ x: Double) -> Double ``` |

Modified sinh(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func sinh(_ x: Float) -> Float ``` |
| To | ``` func sinh(_ x: Float) -> Float ``` |

Modified SIZE_MAX

|  | Declaration |
| --- | --- |
| From | ``` var SIZE_MAX: UInt32 { get } ``` |
| To | ``` var SIZE_MAX: UInt64 { get } ``` |

Modified slot_name(_: cpu_type_t, _: cpu_subtype_t, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!)

|  | Declaration |
| --- | --- |
| From | ``` func slot_name(_ _: cpu_type_t, _ _: cpu_subtype_t, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) ``` |
| To | ``` func slot_name(_ _: cpu_type_t, _ _: cpu_subtype_t, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) ``` |

Modified socketpair(_: Int32, _: Int32, _: Int32, _: UnsafeMutablePointer<Int32>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func socketpair(_ _: Int32, _ _: Int32, _ _: Int32, _ _: UnsafeMutablePointer<Int32>) -> Int32 ``` |
| To | ``` func socketpair(_ _: Int32, _ _: Int32, _ _: Int32, _ _: UnsafeMutablePointer<Int32>!) -> Int32 ``` |

Modified sradixsort(_: UnsafeMutablePointer<UnsafePointer<UInt8>?>!, _: Int32, _: UnsafePointer<UInt8>!, _: UInt32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sradixsort(_ _: UnsafeMutablePointer<UnsafePointer<UInt8>>, _ _: Int32, _ _: UnsafePointer<UInt8>, _ _: UInt32) -> Int32 ``` |
| To | ``` func sradixsort(_ __base: UnsafeMutablePointer<UnsafePointer<UInt8>?>!, _ __nel: Int32, _ __table: UnsafePointer<UInt8>!, _ __endbyte: UInt32) -> Int32 ``` |

Modified stat(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<stat>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func stat(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<stat>) -> Int32 ``` |
| To | ``` func stat(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<stat>!) -> Int32 ``` |

Modified statfs(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<statfs>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func statfs(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<statfs>) -> Int32 ``` |
| To | ``` func statfs(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<statfs>!) -> Int32 ``` |

Modified statvfs(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<statvfs>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func statvfs(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<statvfs>) -> Int32 ``` |
| To | ``` func statvfs(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<statvfs>!) -> Int32 ``` |

Modified statx_np(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<stat>!, _: filesec_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func statx_np(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<stat>, _ _: filesec_t) -> Int32 ``` |
| To | ``` func statx_np(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<stat>!, _ _: filesec_t!) -> Int32 ``` |

Modified stpcpy(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func stpcpy(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func stpcpy(_ __dst: UnsafeMutablePointer<Int8>!, _ __src: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified stpncpy(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func stpncpy(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func stpncpy(_ __dst: UnsafeMutablePointer<Int8>!, _ __src: UnsafePointer<Int8>!, _ __n: Int) -> UnsafeMutablePointer<Int8>! ``` |

Modified strcasecmp(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func strcasecmp(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func strcasecmp(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified strcasecmp_l(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func strcasecmp_l(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: locale_t) -> Int32 ``` |
| To | ``` func strcasecmp_l(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: locale_t!) -> Int32 ``` |

Modified strcasestr(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strcasestr(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strcasestr(_ __big: UnsafePointer<Int8>!, _ __little: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified strcasestr_l(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: locale_t!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strcasestr_l(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: locale_t) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strcasestr_l(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: locale_t!) -> UnsafeMutablePointer<Int8>! ``` |

Modified strcat(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strcat(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strcat(_ __s1: UnsafeMutablePointer<Int8>!, _ __s2: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified strchr(_: UnsafePointer<Int8>!, _: Int32) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strchr(_ _: UnsafePointer<Int8>, _ _: Int32) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strchr(_ __s: UnsafePointer<Int8>!, _ __c: Int32) -> UnsafeMutablePointer<Int8>! ``` |

Modified strcmp(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func strcmp(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func strcmp(_ __s1: UnsafePointer<Int8>!, _ __s2: UnsafePointer<Int8>!) -> Int32 ``` |

Modified strcoll(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func strcoll(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func strcoll(_ __s1: UnsafePointer<Int8>!, _ __s2: UnsafePointer<Int8>!) -> Int32 ``` |

Modified strcoll_l(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func strcoll_l(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: locale_t) -> Int32 ``` |
| To | ``` func strcoll_l(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: locale_t!) -> Int32 ``` |

Modified strcpy(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strcpy(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strcpy(_ __dst: UnsafeMutablePointer<Int8>!, _ __src: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified strcspn(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func strcspn(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> UInt ``` |
| To | ``` func strcspn(_ __s: UnsafePointer<Int8>!, _ __charset: UnsafePointer<Int8>!) -> UInt ``` |

Modified strdup(_: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strdup(_ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strdup(_ __s1: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified strerror(_: Int32) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strerror(_ _: Int32) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strerror(_ __errnum: Int32) -> UnsafeMutablePointer<Int8>! ``` |

Modified strerror_r(_: Int32, _: UnsafeMutablePointer<Int8>!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func strerror_r(_ _: Int32, _ _: UnsafeMutablePointer<Int8>, _ _: Int) -> Int32 ``` |
| To | ``` func strerror_r(_ __errnum: Int32, _ __strerrbuf: UnsafeMutablePointer<Int8>!, _ __buflen: Int) -> Int32 ``` |

Modified strftime(_: UnsafeMutablePointer<Int8>!, _: Int, _: UnsafePointer<Int8>!, _: UnsafePointer<tm>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func strftime(_ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<tm>) -> Int ``` |
| To | ``` func strftime(_ _: UnsafeMutablePointer<Int8>!, _ _: Int, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<tm>!) -> Int ``` |

Modified strftime_l(_: UnsafeMutablePointer<Int8>!, _: Int, _: UnsafePointer<Int8>!, _: UnsafePointer<tm>!, _: locale_t!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func strftime_l(_ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<tm>, _ _: locale_t) -> Int ``` |
| To | ``` func strftime_l(_ _: UnsafeMutablePointer<Int8>!, _ _: Int, _ _: UnsafePointer<Int8>!, _ _: UnsafePointer<tm>!, _ _: locale_t!) -> Int ``` |

Modified strlcat(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int) -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func strlcat(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> UInt ``` |
| To | ``` func strlcat(_ __dst: UnsafeMutablePointer<Int8>!, _ __source: UnsafePointer<Int8>!, _ __size: Int) -> UInt ``` |

Modified strlcpy(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int) -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func strlcpy(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> UInt ``` |
| To | ``` func strlcpy(_ __dst: UnsafeMutablePointer<Int8>!, _ __source: UnsafePointer<Int8>!, _ __size: Int) -> UInt ``` |

Modified strlen(_: UnsafePointer<Int8>!) -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func strlen(_ _: UnsafePointer<Int8>) -> UInt ``` |
| To | ``` func strlen(_ __s: UnsafePointer<Int8>!) -> UInt ``` |

Modified strmode(_: Int32, _: UnsafeMutablePointer<Int8>!)

|  | Declaration |
| --- | --- |
| From | ``` func strmode(_ _: Int32, _ _: UnsafeMutablePointer<Int8>) ``` |
| To | ``` func strmode(_ __mode: Int32, _ __bp: UnsafeMutablePointer<Int8>!) ``` |

Modified strncasecmp(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func strncasecmp(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> Int32 ``` |
| To | ``` func strncasecmp(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: Int) -> Int32 ``` |

Modified strncasecmp_l(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func strncasecmp_l(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int, _ _: locale_t) -> Int32 ``` |
| To | ``` func strncasecmp_l(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: Int, _ _: locale_t!) -> Int32 ``` |

Modified strncat(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strncat(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strncat(_ __s1: UnsafeMutablePointer<Int8>!, _ __s2: UnsafePointer<Int8>!, _ __n: Int) -> UnsafeMutablePointer<Int8>! ``` |

Modified strncmp(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func strncmp(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> Int32 ``` |
| To | ``` func strncmp(_ __s1: UnsafePointer<Int8>!, _ __s2: UnsafePointer<Int8>!, _ __n: Int) -> Int32 ``` |

Modified strncpy(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strncpy(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strncpy(_ __dst: UnsafeMutablePointer<Int8>!, _ __src: UnsafePointer<Int8>!, _ __n: Int) -> UnsafeMutablePointer<Int8>! ``` |

Modified strndup(_: UnsafePointer<Int8>!, _: Int) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strndup(_ _: UnsafePointer<Int8>, _ _: Int) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strndup(_ __s1: UnsafePointer<Int8>!, _ __n: Int) -> UnsafeMutablePointer<Int8>! ``` |

Modified strnlen(_: UnsafePointer<Int8>!, _: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func strnlen(_ _: UnsafePointer<Int8>, _ _: Int) -> Int ``` |
| To | ``` func strnlen(_ __s1: UnsafePointer<Int8>!, _ __n: Int) -> Int ``` |

Modified strnstr(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strnstr(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strnstr(_ __big: UnsafePointer<Int8>!, _ __little: UnsafePointer<Int8>!, _ __len: Int) -> UnsafeMutablePointer<Int8>! ``` |

Modified strpbrk(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strpbrk(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strpbrk(_ __s: UnsafePointer<Int8>!, _ __charset: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified strptime(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<tm>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strptime(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<tm>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strptime(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<tm>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified strptime_l(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<tm>!, _: locale_t!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strptime_l(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<tm>, _ _: locale_t) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strptime_l(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<tm>!, _ _: locale_t!) -> UnsafeMutablePointer<Int8>! ``` |

Modified strrchr(_: UnsafePointer<Int8>!, _: Int32) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strrchr(_ _: UnsafePointer<Int8>, _ _: Int32) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strrchr(_ __s: UnsafePointer<Int8>!, _ __c: Int32) -> UnsafeMutablePointer<Int8>! ``` |

Modified strsep(_: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strsep(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strsep(_ __stringp: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ __delim: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified strsignal(_: Int32) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strsignal(_ sig: Int32) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strsignal(_ __sig: Int32) -> UnsafeMutablePointer<Int8>! ``` |

Modified strspn(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func strspn(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> UInt ``` |
| To | ``` func strspn(_ __s: UnsafePointer<Int8>!, _ __charset: UnsafePointer<Int8>!) -> UInt ``` |

Modified strstr(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strstr(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strstr(_ __big: UnsafePointer<Int8>!, _ __little: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified strtod(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func strtod(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Double ``` |
| To | ``` func strtod(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Double ``` |

Modified strtod_l(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: locale_t!) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func strtod_l(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: locale_t) -> Double ``` |
| To | ``` func strtod_l(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: locale_t!) -> Double ``` |

Modified strtof(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func strtof(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Float ``` |
| To | ``` func strtof(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> Float ``` |

Modified strtof_l(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: locale_t!) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func strtof_l(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: locale_t) -> Float ``` |
| To | ``` func strtof_l(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: locale_t!) -> Float ``` |

Modified strtofflags(_: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafeMutablePointer<UInt>!, _: UnsafeMutablePointer<UInt>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func strtofflags(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<UInt>, _ _: UnsafeMutablePointer<UInt>) -> Int32 ``` |
| To | ``` func strtofflags(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: UnsafeMutablePointer<UInt>!, _ _: UnsafeMutablePointer<UInt>!) -> Int32 ``` |

Modified strtoimax(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32) -> intmax_t

|  | Declaration |
| --- | --- |
| From | ``` func strtoimax(_ __nptr: UnsafePointer<Int8>, _ __endptr: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ __base: Int32) -> intmax_t ``` |
| To | ``` func strtoimax(_ __nptr: UnsafePointer<Int8>!, _ __endptr: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ __base: Int32) -> intmax_t ``` |

Modified strtoimax_l(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32, _: locale_t!) -> intmax_t

|  | Declaration |
| --- | --- |
| From | ``` func strtoimax_l(_ nptr: UnsafePointer<Int8>, _ endptr: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ base: Int32, _ _: locale_t) -> intmax_t ``` |
| To | ``` func strtoimax_l(_ nptr: UnsafePointer<Int8>!, _ endptr: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ base: Int32, _ _: locale_t!) -> intmax_t ``` |

Modified strtok(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strtok(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strtok(_ __str: UnsafeMutablePointer<Int8>!, _ __sep: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified strtok_r(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func strtok_r(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strtok_r(_ __str: UnsafeMutablePointer<Int8>!, _ __sep: UnsafePointer<Int8>!, _ __lasts: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified strtol(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func strtol(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32) -> Int ``` |
| To | ``` func strtol(_ __str: UnsafePointer<Int8>!, _ __endptr: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ __base: Int32) -> Int ``` |

Modified strtol_l(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32, _: locale_t!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func strtol_l(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32, _ _: locale_t) -> Int ``` |
| To | ``` func strtol_l(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: Int32, _ _: locale_t!) -> Int ``` |

Modified strtoll(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32) -> Int64

|  | Declaration |
| --- | --- |
| From | ``` func strtoll(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32) -> Int64 ``` |
| To | ``` func strtoll(_ __str: UnsafePointer<Int8>!, _ __endptr: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ __base: Int32) -> Int64 ``` |

Modified strtoll_l(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32, _: locale_t!) -> Int64

|  | Declaration |
| --- | --- |
| From | ``` func strtoll_l(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32, _ _: locale_t) -> Int64 ``` |
| To | ``` func strtoll_l(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: Int32, _ _: locale_t!) -> Int64 ``` |

Modified strtoq(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32) -> Int64

|  | Declaration |
| --- | --- |
| From | ``` func strtoq(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32) -> Int64 ``` |
| To | ``` func strtoq(_ __str: UnsafePointer<Int8>!, _ __endptr: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ __base: Int32) -> Int64 ``` |

Modified strtoq_l(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32, _: locale_t!) -> Int64

|  | Declaration |
| --- | --- |
| From | ``` func strtoq_l(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32, _ _: locale_t) -> Int64 ``` |
| To | ``` func strtoq_l(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: Int32, _ _: locale_t!) -> Int64 ``` |

Modified strtoul(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32) -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func strtoul(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32) -> UInt ``` |
| To | ``` func strtoul(_ __str: UnsafePointer<Int8>!, _ __endptr: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ __base: Int32) -> UInt ``` |

Modified strtoul_l(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32, _: locale_t!) -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func strtoul_l(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32, _ _: locale_t) -> UInt ``` |
| To | ``` func strtoul_l(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: Int32, _ _: locale_t!) -> UInt ``` |

Modified strtoull(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32) -> UInt64

|  | Declaration |
| --- | --- |
| From | ``` func strtoull(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32) -> UInt64 ``` |
| To | ``` func strtoull(_ __str: UnsafePointer<Int8>!, _ __endptr: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ __base: Int32) -> UInt64 ``` |

Modified strtoull_l(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32, _: locale_t!) -> UInt64

|  | Declaration |
| --- | --- |
| From | ``` func strtoull_l(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32, _ _: locale_t) -> UInt64 ``` |
| To | ``` func strtoull_l(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: Int32, _ _: locale_t!) -> UInt64 ``` |

Modified strtoumax(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32) -> uintmax_t

|  | Declaration |
| --- | --- |
| From | ``` func strtoumax(_ __nptr: UnsafePointer<Int8>, _ __endptr: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ __base: Int32) -> uintmax_t ``` |
| To | ``` func strtoumax(_ __nptr: UnsafePointer<Int8>!, _ __endptr: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ __base: Int32) -> uintmax_t ``` |

Modified strtoumax_l(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32, _: locale_t!) -> uintmax_t

|  | Declaration |
| --- | --- |
| From | ``` func strtoumax_l(_ nptr: UnsafePointer<Int8>, _ endptr: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ base: Int32, _ _: locale_t) -> uintmax_t ``` |
| To | ``` func strtoumax_l(_ nptr: UnsafePointer<Int8>!, _ endptr: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ base: Int32, _ _: locale_t!) -> uintmax_t ``` |

Modified strtouq(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32) -> UInt64

|  | Declaration |
| --- | --- |
| From | ``` func strtouq(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32) -> UInt64 ``` |
| To | ``` func strtouq(_ __str: UnsafePointer<Int8>!, _ __endptr: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ __base: Int32) -> UInt64 ``` |

Modified strtouq_l(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: Int32, _: locale_t!) -> UInt64

|  | Declaration |
| --- | --- |
| From | ``` func strtouq_l(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32, _ _: locale_t) -> UInt64 ``` |
| To | ``` func strtouq_l(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: Int32, _ _: locale_t!) -> UInt64 ``` |

Modified strxfrm(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int) -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func strxfrm(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> UInt ``` |
| To | ``` func strxfrm(_ __s1: UnsafeMutablePointer<Int8>!, _ __s2: UnsafePointer<Int8>!, _ __n: Int) -> UInt ``` |

Modified strxfrm_l(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int, _: locale_t!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func strxfrm_l(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int, _ _: locale_t) -> Int ``` |
| To | ``` func strxfrm_l(_ _: UnsafeMutablePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: Int, _ _: locale_t!) -> Int ``` |

Modified suboptarg

|  | Declaration |
| --- | --- |
| From | ``` var suboptarg: UnsafeMutablePointer<Int8> ``` |
| To | ``` var suboptarg: UnsafeMutablePointer<Int8>! ``` |

Modified swab(_: UnsafeRawPointer!, _: UnsafeMutableRawPointer!, _: Int)

|  | Declaration |
| --- | --- |
| From | ``` func swab(_ _: UnsafePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: Int) ``` |
| To | ``` func swab(_ _: UnsafeRawPointer!, _ _: UnsafeMutableRawPointer!, _ _: Int) ``` |

Modified swapon(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func swapon(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func swapon(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified symlink(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func symlink(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func symlink(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified symlinkat(_: UnsafePointer<Int8>!, _: Int32, _: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func symlinkat(_ _: UnsafePointer<Int8>, _ _: Int32, _ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func symlinkat(_ _: UnsafePointer<Int8>!, _ _: Int32, _ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified sync_volume_np(_: UnsafePointer<Int8>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sync_volume_np(_ _: UnsafePointer<Int8>, _ _: Int32) -> Int32 ``` |
| To | ``` func sync_volume_np(_ _: UnsafePointer<Int8>!, _ _: Int32) -> Int32 ``` |

Modified sys_siglist

|  | Declaration |
| --- | --- |
| From | ``` let sys_siglist: (UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>) ``` |
| To | ``` let sys_siglist: (UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?) ``` |

Modified sys_signame

|  | Declaration |
| --- | --- |
| From | ``` let sys_signame: (UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafePointer<Int8>) ``` |
| To | ``` let sys_signame: (UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?, UnsafePointer<Int8>?) ``` |

Modified syscall_arg_t

|  | Declaration |
| --- | --- |
| From | ``` typealias syscall_arg_t = UInt32 ``` |
| To | ``` typealias syscall_arg_t = UInt64 ``` |

Modified sysctl(_: UnsafeMutablePointer<Int32>!, _: u_int, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!, _: UnsafeMutableRawPointer!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sysctl(_ _: UnsafeMutablePointer<Int32>, _ _: u_int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>, _ _: UnsafeMutablePointer<Void>, _ _: Int) -> Int32 ``` |
| To | ``` func sysctl(_ _: UnsafeMutablePointer<Int32>!, _ _: u_int, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!, _ _: UnsafeMutableRawPointer!, _ _: Int) -> Int32 ``` |

Modified sysctlbyname(_: UnsafePointer<Int8>!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!, _: UnsafeMutableRawPointer!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sysctlbyname(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>, _ _: UnsafeMutablePointer<Void>, _ _: Int) -> Int32 ``` |
| To | ``` func sysctlbyname(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!, _ _: UnsafeMutableRawPointer!, _ _: Int) -> Int32 ``` |

Modified sysctlnametomib(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<Int32>!, _: UnsafeMutablePointer<Int>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func sysctlnametomib(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Int32>, _ _: UnsafeMutablePointer<Int>) -> Int32 ``` |
| To | ``` func sysctlnametomib(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<Int32>!, _ _: UnsafeMutablePointer<Int>!) -> Int32 ``` |

Modified tan(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func tan(_ x: Float) -> Float ``` |
| To | ``` func tan(_ x: Float) -> Float ``` |

Modified tanh(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func tanh(_ x: Float) -> Float ``` |
| To | ``` func tanh(_ x: Float) -> Float ``` |

Modified task_create(_: task_t, _: ledger_array_t!, _: mach_msg_type_number_t, _: boolean_t, _: UnsafeMutablePointer<task_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_create(_ target_task: task_t, _ ledgers: ledger_array_t, _ ledgersCnt: mach_msg_type_number_t, _ inherit_memory: boolean_t, _ child_task: UnsafeMutablePointer<task_t>) -> kern_return_t ``` |
| To | ``` func task_create(_ target_task: task_t, _ ledgers: ledger_array_t!, _ ledgersCnt: mach_msg_type_number_t, _ inherit_memory: boolean_t, _ child_task: UnsafeMutablePointer<task_t>!) -> kern_return_t ``` |

Modified task_for_pid(_: mach_port_name_t, _: Int32, _: UnsafeMutablePointer<mach_port_name_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_for_pid(_ target_tport: mach_port_name_t, _ pid: Int32, _ t: UnsafeMutablePointer<mach_port_name_t>) -> kern_return_t ``` |
| To | ``` func task_for_pid(_ target_tport: mach_port_name_t, _ pid: Int32, _ t: UnsafeMutablePointer<mach_port_name_t>!) -> kern_return_t ``` |

Modified task_get_assignment(_: task_t, _: UnsafeMutablePointer<processor_set_name_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_get_assignment(_ task: task_t, _ assigned_set: UnsafeMutablePointer<processor_set_name_t>) -> kern_return_t ``` |
| To | ``` func task_get_assignment(_ task: task_t, _ assigned_set: UnsafeMutablePointer<processor_set_name_t>!) -> kern_return_t ``` |

Modified task_get_emulation_vector(_: task_t, _: UnsafeMutablePointer<Int32>!, _: UnsafeMutablePointer<emulation_vector_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_get_emulation_vector(_ task: task_t, _ vector_start: UnsafeMutablePointer<Int32>, _ emulation_vector: UnsafeMutablePointer<emulation_vector_t>, _ emulation_vectorCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func task_get_emulation_vector(_ task: task_t, _ vector_start: UnsafeMutablePointer<Int32>!, _ emulation_vector: UnsafeMutablePointer<emulation_vector_t?>!, _ emulation_vectorCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified task_get_exception_ports(_: task_t, _: exception_mask_t, _: exception_mask_array_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: exception_handler_array_t!, _: exception_behavior_array_t!, _: exception_flavor_array_t!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_get_exception_ports(_ task: task_t, _ exception_mask: exception_mask_t, _ masks: exception_mask_array_t, _ masksCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ old_handlers: exception_handler_array_t, _ old_behaviors: exception_behavior_array_t, _ old_flavors: exception_flavor_array_t) -> kern_return_t ``` |
| To | ``` func task_get_exception_ports(_ task: task_t, _ exception_mask: exception_mask_t, _ masks: exception_mask_array_t!, _ masksCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ old_handlers: exception_handler_array_t!, _ old_behaviors: exception_behavior_array_t!, _ old_flavors: exception_flavor_array_t!) -> kern_return_t ``` |

Modified task_get_mach_voucher(_: task_t, _: mach_voucher_selector_t, _: UnsafeMutablePointer<ipc_voucher_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_get_mach_voucher(_ task: task_t, _ which: mach_voucher_selector_t, _ voucher: UnsafeMutablePointer<ipc_voucher_t>) -> kern_return_t ``` |
| To | ``` func task_get_mach_voucher(_ task: task_t, _ which: mach_voucher_selector_t, _ voucher: UnsafeMutablePointer<ipc_voucher_t>!) -> kern_return_t ``` |

Modified task_get_special_port(_: task_t, _: Int32, _: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_get_special_port(_ task: task_t, _ which_port: Int32, _ special_port: UnsafeMutablePointer<mach_port_t>) -> kern_return_t ``` |
| To | ``` func task_get_special_port(_ task: task_t, _ which_port: Int32, _ special_port: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t ``` |

Modified task_get_state(_: task_t, _: thread_state_flavor_t, _: thread_state_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_get_state(_ task: task_t, _ flavor: thread_state_flavor_t, _ old_state: thread_state_t, _ old_stateCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func task_get_state(_ task: task_t, _ flavor: thread_state_flavor_t, _ old_state: thread_state_t!, _ old_stateCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified task_info(_: task_name_t, _: task_flavor_t, _: task_info_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_info(_ target_task: task_name_t, _ flavor: task_flavor_t, _ task_info_out: task_info_t, _ task_info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func task_info(_ target_task: task_name_t, _ flavor: task_flavor_t, _ task_info_out: task_info_t!, _ task_info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified task_name_for_pid(_: mach_port_name_t, _: Int32, _: UnsafeMutablePointer<mach_port_name_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_name_for_pid(_ target_tport: mach_port_name_t, _ pid: Int32, _ tn: UnsafeMutablePointer<mach_port_name_t>) -> kern_return_t ``` |
| To | ``` func task_name_for_pid(_ target_tport: mach_port_name_t, _ pid: Int32, _ tn: UnsafeMutablePointer<mach_port_name_t>!) -> kern_return_t ``` |

Modified task_policy(_: task_t, _: policy_t, _: policy_base_t!, _: mach_msg_type_number_t, _: boolean_t, _: boolean_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_policy(_ task: task_t, _ policy: policy_t, _ base: policy_base_t, _ baseCnt: mach_msg_type_number_t, _ set_limit: boolean_t, _ change: boolean_t) -> kern_return_t ``` |
| To | ``` func task_policy(_ task: task_t, _ policy: policy_t, _ base: policy_base_t!, _ baseCnt: mach_msg_type_number_t, _ set_limit: boolean_t, _ change: boolean_t) -> kern_return_t ``` |

Modified task_policy_get(_: task_t, _: task_policy_flavor_t, _: task_policy_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: UnsafeMutablePointer<boolean_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_policy_get(_ task: task_t, _ flavor: task_policy_flavor_t, _ policy_info: task_policy_t, _ policy_infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ get_default: UnsafeMutablePointer<boolean_t>) -> kern_return_t ``` |
| To | ``` func task_policy_get(_ task: task_t, _ flavor: task_policy_flavor_t, _ policy_info: task_policy_t!, _ policy_infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ get_default: UnsafeMutablePointer<boolean_t>!) -> kern_return_t ``` |

Modified task_policy_set(_: task_t, _: task_policy_flavor_t, _: task_policy_t!, _: mach_msg_type_number_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_policy_set(_ task: task_t, _ flavor: task_policy_flavor_t, _ policy_info: task_policy_t, _ policy_infoCnt: mach_msg_type_number_t) -> kern_return_t ``` |
| To | ``` func task_policy_set(_ task: task_t, _ flavor: task_policy_flavor_t, _ policy_info: task_policy_t!, _ policy_infoCnt: mach_msg_type_number_t) -> kern_return_t ``` |

Modified task_purgable_info(_: task_t, _: UnsafeMutablePointer<task_purgable_info_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_purgable_info(_ task: task_t, _ stats: UnsafeMutablePointer<task_purgable_info_t>) -> kern_return_t ``` |
| To | ``` func task_purgable_info(_ task: task_t, _ stats: UnsafeMutablePointer<task_purgable_info_t>!) -> kern_return_t ``` |

Modified task_set_emulation_vector(_: task_t, _: Int32, _: emulation_vector_t!, _: mach_msg_type_number_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_set_emulation_vector(_ task: task_t, _ vector_start: Int32, _ emulation_vector: emulation_vector_t, _ emulation_vectorCnt: mach_msg_type_number_t) -> kern_return_t ``` |
| To | ``` func task_set_emulation_vector(_ task: task_t, _ vector_start: Int32, _ emulation_vector: emulation_vector_t!, _ emulation_vectorCnt: mach_msg_type_number_t) -> kern_return_t ``` |

Modified task_set_info(_: task_t, _: task_flavor_t, _: task_info_t!, _: mach_msg_type_number_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_set_info(_ target_task: task_t, _ flavor: task_flavor_t, _ task_info_in: task_info_t, _ task_info_inCnt: mach_msg_type_number_t) -> kern_return_t ``` |
| To | ``` func task_set_info(_ target_task: task_t, _ flavor: task_flavor_t, _ task_info_in: task_info_t!, _ task_info_inCnt: mach_msg_type_number_t) -> kern_return_t ``` |

Modified task_set_phys_footprint_limit(_: task_t, _: Int32, _: UnsafeMutablePointer<Int32>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_set_phys_footprint_limit(_ task: task_t, _ new_limit: Int32, _ old_limit: UnsafeMutablePointer<Int32>) -> kern_return_t ``` |
| To | ``` func task_set_phys_footprint_limit(_ task: task_t, _ new_limit: Int32, _ old_limit: UnsafeMutablePointer<Int32>!) -> kern_return_t ``` |

Modified task_set_policy(_: task_t, _: processor_set_t, _: policy_t, _: policy_base_t!, _: mach_msg_type_number_t, _: policy_limit_t!, _: mach_msg_type_number_t, _: boolean_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_set_policy(_ task: task_t, _ pset: processor_set_t, _ policy: policy_t, _ base: policy_base_t, _ baseCnt: mach_msg_type_number_t, _ limit: policy_limit_t, _ limitCnt: mach_msg_type_number_t, _ change: boolean_t) -> kern_return_t ``` |
| To | ``` func task_set_policy(_ task: task_t, _ pset: processor_set_t, _ policy: policy_t, _ base: policy_base_t!, _ baseCnt: mach_msg_type_number_t, _ limit: policy_limit_t!, _ limitCnt: mach_msg_type_number_t, _ change: boolean_t) -> kern_return_t ``` |

Modified task_set_state(_: task_t, _: thread_state_flavor_t, _: thread_state_t!, _: mach_msg_type_number_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_set_state(_ task: task_t, _ flavor: thread_state_flavor_t, _ new_state: thread_state_t, _ new_stateCnt: mach_msg_type_number_t) -> kern_return_t ``` |
| To | ``` func task_set_state(_ task: task_t, _ flavor: thread_state_flavor_t, _ new_state: thread_state_t!, _ new_stateCnt: mach_msg_type_number_t) -> kern_return_t ``` |

Modified task_suspend2(_: task_t, _: UnsafeMutablePointer<task_suspension_token_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_suspend2(_ target_task: task_t, _ suspend_token: UnsafeMutablePointer<task_suspension_token_t>) -> kern_return_t ``` |
| To | ``` func task_suspend2(_ target_task: task_t, _ suspend_token: UnsafeMutablePointer<task_suspension_token_t>!) -> kern_return_t ``` |

Modified task_swap_exception_ports(_: task_t, _: exception_mask_t, _: mach_port_t, _: exception_behavior_t, _: thread_state_flavor_t, _: exception_mask_array_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: exception_handler_array_t!, _: exception_behavior_array_t!, _: exception_flavor_array_t!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_swap_exception_ports(_ task: task_t, _ exception_mask: exception_mask_t, _ new_port: mach_port_t, _ behavior: exception_behavior_t, _ new_flavor: thread_state_flavor_t, _ masks: exception_mask_array_t, _ masksCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ old_handlerss: exception_handler_array_t, _ old_behaviors: exception_behavior_array_t, _ old_flavors: exception_flavor_array_t) -> kern_return_t ``` |
| To | ``` func task_swap_exception_ports(_ task: task_t, _ exception_mask: exception_mask_t, _ new_port: mach_port_t, _ behavior: exception_behavior_t, _ new_flavor: thread_state_flavor_t, _ masks: exception_mask_array_t!, _ masksCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ old_handlerss: exception_handler_array_t!, _ old_behaviors: exception_behavior_array_t!, _ old_flavors: exception_flavor_array_t!) -> kern_return_t ``` |

Modified task_swap_mach_voucher(_: task_t, _: ipc_voucher_t, _: UnsafeMutablePointer<ipc_voucher_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_swap_mach_voucher(_ task: task_t, _ new_voucher: ipc_voucher_t, _ old_voucher: UnsafeMutablePointer<ipc_voucher_t>) -> kern_return_t ``` |
| To | ``` func task_swap_mach_voucher(_ task: task_t, _ new_voucher: ipc_voucher_t, _ old_voucher: UnsafeMutablePointer<ipc_voucher_t>!) -> kern_return_t ``` |

Modified task_threads(_: task_t, _: UnsafeMutablePointer<thread_act_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_threads(_ target_task: task_t, _ act_list: UnsafeMutablePointer<thread_act_array_t>, _ act_listCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func task_threads(_ target_task: task_t, _ act_list: UnsafeMutablePointer<thread_act_array_t?>!, _ act_listCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified task_zone_info(_: task_t, _: UnsafeMutablePointer<mach_zone_name_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: UnsafeMutablePointer<task_zone_info_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func task_zone_info(_ target_task: task_t, _ names: UnsafeMutablePointer<mach_zone_name_array_t>, _ namesCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ info: UnsafeMutablePointer<task_zone_info_array_t>, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func task_zone_info(_ target_task: task_t, _ names: UnsafeMutablePointer<mach_zone_name_array_t?>!, _ namesCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ info: UnsafeMutablePointer<task_zone_info_array_t?>!, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified tcgetattr(_: Int32, _: UnsafeMutablePointer<termios>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func tcgetattr(_ _: Int32, _ _: UnsafeMutablePointer<termios>) -> Int32 ``` |
| To | ``` func tcgetattr(_ _: Int32, _ _: UnsafeMutablePointer<termios>!) -> Int32 ``` |

Modified tcsetattr(_: Int32, _: Int32, _: UnsafePointer<termios>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func tcsetattr(_ _: Int32, _ _: Int32, _ _: UnsafePointer<termios>) -> Int32 ``` |
| To | ``` func tcsetattr(_ _: Int32, _ _: Int32, _ _: UnsafePointer<termios>!) -> Int32 ``` |

Modified tdelete(_: UnsafeRawPointer!, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _: ( (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func tdelete(_ _: UnsafePointer<Void>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func tdelete(_ _: UnsafeRawPointer!, _ _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _ _: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer! ``` |

Modified telldir(_: UnsafeMutablePointer<DIR>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func telldir(_ _: UnsafeMutablePointer<DIR>) -> Int ``` |
| To | ``` func telldir(_ _: UnsafeMutablePointer<DIR>!) -> Int ``` |

Modified tfind(_: UnsafeRawPointer!, _: UnsafePointer<UnsafeMutableRawPointer?>!, _: ( (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func tfind(_ _: UnsafePointer<Void>, _ _: UnsafePointer<UnsafeMutablePointer<Void>>, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func tfind(_ _: UnsafeRawPointer!, _ _: UnsafePointer<UnsafeMutableRawPointer?>!, _ _: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer! ``` |

Modified tgamma(_: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func tgamma(_ x: Float) -> Float ``` |
| To | ``` func tgamma(_ x: Float) -> Float ``` |

Modified thread_create(_: task_t, _: UnsafeMutablePointer<thread_act_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func thread_create(_ parent_task: task_t, _ child_act: UnsafeMutablePointer<thread_act_t>) -> kern_return_t ``` |
| To | ``` func thread_create(_ parent_task: task_t, _ child_act: UnsafeMutablePointer<thread_act_t>!) -> kern_return_t ``` |

Modified thread_create_running(_: task_t, _: thread_state_flavor_t, _: thread_state_t!, _: mach_msg_type_number_t, _: UnsafeMutablePointer<thread_act_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func thread_create_running(_ parent_task: task_t, _ flavor: thread_state_flavor_t, _ new_state: thread_state_t, _ new_stateCnt: mach_msg_type_number_t, _ child_act: UnsafeMutablePointer<thread_act_t>) -> kern_return_t ``` |
| To | ``` func thread_create_running(_ parent_task: task_t, _ flavor: thread_state_flavor_t, _ new_state: thread_state_t!, _ new_stateCnt: mach_msg_type_number_t, _ child_act: UnsafeMutablePointer<thread_act_t>!) -> kern_return_t ``` |

Modified thread_get_assignment(_: thread_act_t, _: UnsafeMutablePointer<processor_set_name_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func thread_get_assignment(_ thread: thread_act_t, _ assigned_set: UnsafeMutablePointer<processor_set_name_t>) -> kern_return_t ``` |
| To | ``` func thread_get_assignment(_ thread: thread_act_t, _ assigned_set: UnsafeMutablePointer<processor_set_name_t>!) -> kern_return_t ``` |

Modified thread_get_exception_ports(_: thread_act_t, _: exception_mask_t, _: exception_mask_array_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: exception_handler_array_t!, _: exception_behavior_array_t!, _: exception_flavor_array_t!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func thread_get_exception_ports(_ thread: thread_act_t, _ exception_mask: exception_mask_t, _ masks: exception_mask_array_t, _ masksCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ old_handlers: exception_handler_array_t, _ old_behaviors: exception_behavior_array_t, _ old_flavors: exception_flavor_array_t) -> kern_return_t ``` |
| To | ``` func thread_get_exception_ports(_ thread: thread_act_t, _ exception_mask: exception_mask_t, _ masks: exception_mask_array_t!, _ masksCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ old_handlers: exception_handler_array_t!, _ old_behaviors: exception_behavior_array_t!, _ old_flavors: exception_flavor_array_t!) -> kern_return_t ``` |

Modified thread_get_mach_voucher(_: thread_act_t, _: mach_voucher_selector_t, _: UnsafeMutablePointer<ipc_voucher_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func thread_get_mach_voucher(_ thr_act: thread_act_t, _ which: mach_voucher_selector_t, _ voucher: UnsafeMutablePointer<ipc_voucher_t>) -> kern_return_t ``` |
| To | ``` func thread_get_mach_voucher(_ thr_act: thread_act_t, _ which: mach_voucher_selector_t, _ voucher: UnsafeMutablePointer<ipc_voucher_t>!) -> kern_return_t ``` |

Modified thread_get_special_port(_: thread_act_t, _: Int32, _: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func thread_get_special_port(_ thr_act: thread_act_t, _ which_port: Int32, _ special_port: UnsafeMutablePointer<mach_port_t>) -> kern_return_t ``` |
| To | ``` func thread_get_special_port(_ thr_act: thread_act_t, _ which_port: Int32, _ special_port: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t ``` |

Modified thread_get_state(_: thread_act_t, _: thread_state_flavor_t, _: thread_state_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func thread_get_state(_ target_act: thread_act_t, _ flavor: thread_state_flavor_t, _ old_state: thread_state_t, _ old_stateCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func thread_get_state(_ target_act: thread_act_t, _ flavor: thread_state_flavor_t, _ old_state: thread_state_t!, _ old_stateCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified thread_info(_: thread_act_t, _: thread_flavor_t, _: thread_info_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func thread_info(_ target_act: thread_act_t, _ flavor: thread_flavor_t, _ thread_info_out: thread_info_t, _ thread_info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func thread_info(_ target_act: thread_act_t, _ flavor: thread_flavor_t, _ thread_info_out: thread_info_t!, _ thread_info_outCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified thread_policy(_: thread_act_t, _: policy_t, _: policy_base_t!, _: mach_msg_type_number_t, _: boolean_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func thread_policy(_ thr_act: thread_act_t, _ policy: policy_t, _ base: policy_base_t, _ baseCnt: mach_msg_type_number_t, _ set_limit: boolean_t) -> kern_return_t ``` |
| To | ``` func thread_policy(_ thr_act: thread_act_t, _ policy: policy_t, _ base: policy_base_t!, _ baseCnt: mach_msg_type_number_t, _ set_limit: boolean_t) -> kern_return_t ``` |

Modified thread_policy_get(_: thread_act_t, _: thread_policy_flavor_t, _: thread_policy_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: UnsafeMutablePointer<boolean_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func thread_policy_get(_ thread: thread_act_t, _ flavor: thread_policy_flavor_t, _ policy_info: thread_policy_t, _ policy_infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ get_default: UnsafeMutablePointer<boolean_t>) -> kern_return_t ``` |
| To | ``` func thread_policy_get(_ thread: thread_act_t, _ flavor: thread_policy_flavor_t, _ policy_info: thread_policy_t!, _ policy_infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ get_default: UnsafeMutablePointer<boolean_t>!) -> kern_return_t ``` |

Modified thread_policy_set(_: thread_act_t, _: thread_policy_flavor_t, _: thread_policy_t!, _: mach_msg_type_number_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func thread_policy_set(_ thread: thread_act_t, _ flavor: thread_policy_flavor_t, _ policy_info: thread_policy_t, _ policy_infoCnt: mach_msg_type_number_t) -> kern_return_t ``` |
| To | ``` func thread_policy_set(_ thread: thread_act_t, _ flavor: thread_policy_flavor_t, _ policy_info: thread_policy_t!, _ policy_infoCnt: mach_msg_type_number_t) -> kern_return_t ``` |

Modified thread_set_policy(_: thread_act_t, _: processor_set_t, _: policy_t, _: policy_base_t!, _: mach_msg_type_number_t, _: policy_limit_t!, _: mach_msg_type_number_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func thread_set_policy(_ thr_act: thread_act_t, _ pset: processor_set_t, _ policy: policy_t, _ base: policy_base_t, _ baseCnt: mach_msg_type_number_t, _ limit: policy_limit_t, _ limitCnt: mach_msg_type_number_t) -> kern_return_t ``` |
| To | ``` func thread_set_policy(_ thr_act: thread_act_t, _ pset: processor_set_t, _ policy: policy_t, _ base: policy_base_t!, _ baseCnt: mach_msg_type_number_t, _ limit: policy_limit_t!, _ limitCnt: mach_msg_type_number_t) -> kern_return_t ``` |

Modified thread_set_state(_: thread_act_t, _: thread_state_flavor_t, _: thread_state_t!, _: mach_msg_type_number_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func thread_set_state(_ target_act: thread_act_t, _ flavor: thread_state_flavor_t, _ new_state: thread_state_t, _ new_stateCnt: mach_msg_type_number_t) -> kern_return_t ``` |
| To | ``` func thread_set_state(_ target_act: thread_act_t, _ flavor: thread_state_flavor_t, _ new_state: thread_state_t!, _ new_stateCnt: mach_msg_type_number_t) -> kern_return_t ``` |

Modified thread_swap_exception_ports(_: thread_act_t, _: exception_mask_t, _: mach_port_t, _: exception_behavior_t, _: thread_state_flavor_t, _: exception_mask_array_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: exception_handler_array_t!, _: exception_behavior_array_t!, _: exception_flavor_array_t!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func thread_swap_exception_ports(_ thread: thread_act_t, _ exception_mask: exception_mask_t, _ new_port: mach_port_t, _ behavior: exception_behavior_t, _ new_flavor: thread_state_flavor_t, _ masks: exception_mask_array_t, _ masksCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ old_handlers: exception_handler_array_t, _ old_behaviors: exception_behavior_array_t, _ old_flavors: exception_flavor_array_t) -> kern_return_t ``` |
| To | ``` func thread_swap_exception_ports(_ thread: thread_act_t, _ exception_mask: exception_mask_t, _ new_port: mach_port_t, _ behavior: exception_behavior_t, _ new_flavor: thread_state_flavor_t, _ masks: exception_mask_array_t!, _ masksCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ old_handlers: exception_handler_array_t!, _ old_behaviors: exception_behavior_array_t!, _ old_flavors: exception_flavor_array_t!) -> kern_return_t ``` |

Modified thread_swap_mach_voucher(_: thread_act_t, _: ipc_voucher_t, _: UnsafeMutablePointer<ipc_voucher_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func thread_swap_mach_voucher(_ thr_act: thread_act_t, _ new_voucher: ipc_voucher_t, _ old_voucher: UnsafeMutablePointer<ipc_voucher_t>) -> kern_return_t ``` |
| To | ``` func thread_swap_mach_voucher(_ thr_act: thread_act_t, _ new_voucher: ipc_voucher_t, _ old_voucher: UnsafeMutablePointer<ipc_voucher_t>!) -> kern_return_t ``` |

Modified time(_: UnsafeMutablePointer<time_t>!) -> time_t

|  | Declaration |
| --- | --- |
| From | ``` func time(_ _: UnsafeMutablePointer<time_t>) -> time_t ``` |
| To | ``` func time(_ _: UnsafeMutablePointer<time_t>!) -> time_t ``` |

Modified timegm(_: UnsafeMutablePointer<tm>!) -> time_t

|  | Declaration |
| --- | --- |
| From | ``` func timegm(_ _: UnsafeMutablePointer<tm>) -> time_t ``` |
| To | ``` func timegm(_ _: UnsafeMutablePointer<tm>!) -> time_t ``` |

Modified timelocal(_: UnsafeMutablePointer<tm>!) -> time_t

|  | Declaration |
| --- | --- |
| From | ``` func timelocal(_ _: UnsafeMutablePointer<tm>) -> time_t ``` |
| To | ``` func timelocal(_ _: UnsafeMutablePointer<tm>!) -> time_t ``` |

Modified times(_: UnsafeMutablePointer<tms>!) -> clock_t

|  | Declaration |
| --- | --- |
| From | ``` func times(_ _: UnsafeMutablePointer<tms>) -> clock_t ``` |
| To | ``` func times(_ _: UnsafeMutablePointer<tms>!) -> clock_t ``` |

Modified tmpfile() -> UnsafeMutablePointer<FILE>!

|  | Declaration |
| --- | --- |
| From | ``` func tmpfile() -> UnsafeMutablePointer<FILE> ``` |
| To | ``` func tmpfile() -> UnsafeMutablePointer<FILE>! ``` |

Modified tolower_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func tolower_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func tolower_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified toupper_l(_: Int32, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func toupper_l(_ c: Int32, _ l: locale_t) -> Int32 ``` |
| To | ``` func toupper_l(_ c: Int32, _ l: locale_t!) -> Int32 ``` |

Modified towctrans_l(_: wint_t, _: wctrans_t, _: locale_t!) -> wint_t

|  | Declaration |
| --- | --- |
| From | ``` func towctrans_l(_ _: wint_t, _ _: wctrans_t, _ _: locale_t) -> wint_t ``` |
| To | ``` func towctrans_l(_ _: wint_t, _ _: wctrans_t, _ _: locale_t!) -> wint_t ``` |

Modified towlower_l(_: wint_t, _: locale_t!) -> wint_t

|  | Declaration |
| --- | --- |
| From | ``` func towlower_l(_ _wc: wint_t, _ _l: locale_t) -> wint_t ``` |
| To | ``` func towlower_l(_ _wc: wint_t, _ _l: locale_t!) -> wint_t ``` |

Modified towupper_l(_: wint_t, _: locale_t!) -> wint_t

|  | Declaration |
| --- | --- |
| From | ``` func towupper_l(_ _wc: wint_t, _ _l: locale_t) -> wint_t ``` |
| To | ``` func towupper_l(_ _wc: wint_t, _ _l: locale_t!) -> wint_t ``` |

Modified truncate(_: UnsafePointer<Int8>!, _: off_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func truncate(_ _: UnsafePointer<Int8>, _ _: off_t) -> Int32 ``` |
| To | ``` func truncate(_ _: UnsafePointer<Int8>!, _ _: off_t) -> Int32 ``` |

Modified tsearch(_: UnsafeRawPointer!, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _: ( (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func tsearch(_ _: UnsafePointer<Void>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func tsearch(_ _: UnsafeRawPointer!, _ _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _ _: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer! ``` |

Modified ttyaction(_: UnsafeMutablePointer<Int8>!, _: UnsafeMutablePointer<Int8>!, _: UnsafeMutablePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ttyaction(_ tty: UnsafeMutablePointer<Int8>, _ act: UnsafeMutablePointer<Int8>, _ user: UnsafeMutablePointer<Int8>) -> Int32 ``` |
| To | ``` func ttyaction(_ tty: UnsafeMutablePointer<Int8>!, _ act: UnsafeMutablePointer<Int8>!, _ user: UnsafeMutablePointer<Int8>!) -> Int32 ``` |

Modified ttylock(_: UnsafePointer<Int8>!, _: Int32, _: UnsafeMutablePointer<pid_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ttylock(_ _: UnsafePointer<Int8>, _ _: Int32, _ _: UnsafeMutablePointer<pid_t>) -> Int32 ``` |
| To | ``` func ttylock(_ _: UnsafePointer<Int8>!, _ _: Int32, _ _: UnsafeMutablePointer<pid_t>!) -> Int32 ``` |

Modified ttymsg(_: UnsafeMutablePointer<iovec>!, _: Int32, _: UnsafePointer<Int8>!, _: Int32) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func ttymsg(_ _: UnsafeMutablePointer<iovec>, _ _: Int32, _ _: UnsafePointer<Int8>, _ _: Int32) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func ttymsg(_ _: UnsafeMutablePointer<iovec>!, _ _: Int32, _ _: UnsafePointer<Int8>!, _ _: Int32) -> UnsafeMutablePointer<Int8>! ``` |

Modified ttyname(_: Int32) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func ttyname(_ _: Int32) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func ttyname(_ _: Int32) -> UnsafeMutablePointer<Int8>! ``` |

Modified ttyname_r(_: Int32, _: UnsafeMutablePointer<Int8>!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ttyname_r(_ _: Int32, _ _: UnsafeMutablePointer<Int8>, _ _: Int) -> Int32 ``` |
| To | ``` func ttyname_r(_ _: Int32, _ _: UnsafeMutablePointer<Int8>!, _ _: Int) -> Int32 ``` |

Modified ttyunlock(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ttyunlock(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func ttyunlock(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified twalk(_: UnsafeRawPointer!, _: ( (UnsafeRawPointer?, VISIT, Int32) -> Swift.Void)!)

|  | Declaration |
| --- | --- |
| From | ``` func twalk(_ _: UnsafePointer<Void>, _ _: ((UnsafePointer<Void>, VISIT, Int32) -> Void)!) ``` |
| To | ``` func twalk(_ _: UnsafeRawPointer!, _ _: (@escaping (UnsafeRawPointer?, VISIT, Int32) -> Swift.Void)!) ``` |

Modified uintmax_t

|  | Declaration |
| --- | --- |
| From | ``` typealias uintmax_t = UInt64 ``` |
| To | ``` typealias uintmax_t = UInt ``` |

Modified UINTPTR_MAX

|  | Declaration |
| --- | --- |
| From | ``` var UINTPTR_MAX: UInt32 { get } ``` |
| To | ``` var UINTPTR_MAX: UInt64 { get } ``` |

Modified uname(_: UnsafeMutablePointer<utsname>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func uname(_ _: UnsafeMutablePointer<utsname>) -> Int32 ``` |
| To | ``` func uname(_ _: UnsafeMutablePointer<utsname>!) -> Int32 ``` |

Modified undelete(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func undelete(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func undelete(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified ungetc(_: Int32, _: UnsafeMutablePointer<FILE>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ungetc(_ _: Int32, _ _: UnsafeMutablePointer<FILE>) -> Int32 ``` |
| To | ``` func ungetc(_ _: Int32, _ _: UnsafeMutablePointer<FILE>!) -> Int32 ``` |

Modified ungetwc(_: wint_t, _: UnsafeMutablePointer<FILE>!) -> wint_t

|  | Declaration |
| --- | --- |
| From | ``` func ungetwc(_ _: wint_t, _ _: UnsafeMutablePointer<FILE>) -> wint_t ``` |
| To | ``` func ungetwc(_ _: wint_t, _ _: UnsafeMutablePointer<FILE>!) -> wint_t ``` |

Modified ungetwc_l(_: wint_t, _: UnsafeMutablePointer<FILE>!, _: locale_t!) -> wint_t

|  | Declaration |
| --- | --- |
| From | ``` func ungetwc_l(_ _: wint_t, _ _: UnsafeMutablePointer<FILE>, _ _: locale_t) -> wint_t ``` |
| To | ``` func ungetwc_l(_ _: wint_t, _ _: UnsafeMutablePointer<FILE>!, _ _: locale_t!) -> wint_t ``` |

Modified unlink(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func unlink(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func unlink(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified unlinkat(_: Int32, _: UnsafePointer<Int8>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func unlinkat(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: Int32) -> Int32 ``` |
| To | ``` func unlinkat(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: Int32) -> Int32 ``` |

Modified unmount(_: UnsafePointer<Int8>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func unmount(_ _: UnsafePointer<Int8>, _ _: Int32) -> Int32 ``` |
| To | ``` func unmount(_ _: UnsafePointer<Int8>!, _ _: Int32) -> Int32 ``` |

Modified unsetenv(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func unsetenv(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func unsetenv(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified unwhiteout(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func unwhiteout(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func unwhiteout(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified uselocale(_: locale_t!) -> locale_t!

|  | Declaration |
| --- | --- |
| From | ``` func uselocale(_ _: locale_t) -> locale_t ``` |
| To | ``` func uselocale(_ _: locale_t!) -> locale_t! ``` |

Modified user_addr_t

|  | Declaration |
| --- | --- |
| From | ``` typealias user_addr_t = UInt32 ``` |
| To | ``` typealias user_addr_t = UInt64 ``` |

Modified user_from_uid(_: uid_t, _: Int32) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func user_from_uid(_ _: uid_t, _ _: Int32) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func user_from_uid(_ _: uid_t, _ _: Int32) -> UnsafeMutablePointer<Int8>! ``` |

Modified user_long_t

|  | Declaration |
| --- | --- |
| From | ``` typealias user_long_t = Int32 ``` |
| To | ``` typealias user_long_t = Int64 ``` |

Modified user_size_t

|  | Declaration |
| --- | --- |
| From | ``` typealias user_size_t = UInt32 ``` |
| To | ``` typealias user_size_t = UInt64 ``` |

Modified user_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` typealias user_ssize_t = Int32 ``` |
| To | ``` typealias user_ssize_t = Int64 ``` |

Modified user_time_t

|  | Declaration |
| --- | --- |
| From | ``` typealias user_time_t = Int32 ``` |
| To | ``` typealias user_time_t = Int64 ``` |

Modified user_ulong_t

|  | Declaration |
| --- | --- |
| From | ``` typealias user_ulong_t = UInt32 ``` |
| To | ``` typealias user_ulong_t = UInt64 ``` |

Modified utime(_: UnsafePointer<Int8>!, _: UnsafePointer<utimbuf>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func utime(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<utimbuf>) -> Int32 ``` |
| To | ``` func utime(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<utimbuf>!) -> Int32 ``` |

Modified utimes(_: UnsafePointer<Int8>!, _: UnsafePointer<timeval>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func utimes(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<timeval>) -> Int32 ``` |
| To | ``` func utimes(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<timeval>!) -> Int32 ``` |

Modified utmpxname(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func utmpxname(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func utmpxname(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified uuid_clear(_: UnsafeMutablePointer<UInt8>!)

|  | Declaration |
| --- | --- |
| From | ``` func uuid_clear(_ uu: UnsafeMutablePointer<UInt8>) ``` |
| To | ``` func uuid_clear(_ uu: UnsafeMutablePointer<UInt8>!) ``` |

Modified uuid_compare(_: UnsafePointer<UInt8>!, _: UnsafePointer<UInt8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func uuid_compare(_ uu1: UnsafePointer<UInt8>, _ uu2: UnsafePointer<UInt8>) -> Int32 ``` |
| To | ``` func uuid_compare(_ uu1: UnsafePointer<UInt8>!, _ uu2: UnsafePointer<UInt8>!) -> Int32 ``` |

Modified uuid_copy(_: UnsafeMutablePointer<UInt8>!, _: UnsafePointer<UInt8>!)

|  | Declaration |
| --- | --- |
| From | ``` func uuid_copy(_ dst: UnsafeMutablePointer<UInt8>, _ src: UnsafePointer<UInt8>) ``` |
| To | ``` func uuid_copy(_ dst: UnsafeMutablePointer<UInt8>!, _ src: UnsafePointer<UInt8>!) ``` |

Modified uuid_generate(_: UnsafeMutablePointer<UInt8>!)

|  | Declaration |
| --- | --- |
| From | ``` func uuid_generate(_ out: UnsafeMutablePointer<UInt8>) ``` |
| To | ``` func uuid_generate(_ out: UnsafeMutablePointer<UInt8>!) ``` |

Modified uuid_generate_random(_: UnsafeMutablePointer<UInt8>!)

|  | Declaration |
| --- | --- |
| From | ``` func uuid_generate_random(_ out: UnsafeMutablePointer<UInt8>) ``` |
| To | ``` func uuid_generate_random(_ out: UnsafeMutablePointer<UInt8>!) ``` |

Modified uuid_generate_time(_: UnsafeMutablePointer<UInt8>!)

|  | Declaration |
| --- | --- |
| From | ``` func uuid_generate_time(_ out: UnsafeMutablePointer<UInt8>) ``` |
| To | ``` func uuid_generate_time(_ out: UnsafeMutablePointer<UInt8>!) ``` |

Modified uuid_is_null(_: UnsafePointer<UInt8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func uuid_is_null(_ uu: UnsafePointer<UInt8>) -> Int32 ``` |
| To | ``` func uuid_is_null(_ uu: UnsafePointer<UInt8>!) -> Int32 ``` |

Modified uuid_parse(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UInt8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func uuid_parse(_ in: UnsafePointer<Int8>, _ uu: UnsafeMutablePointer<UInt8>) -> Int32 ``` |
| To | ``` func uuid_parse(_ in: UnsafePointer<Int8>!, _ uu: UnsafeMutablePointer<UInt8>!) -> Int32 ``` |

Modified uuid_string_t

|  | Declaration |
| --- | --- |
| From | ``` typealias uuid_string_t = __darwin_uuid_string_t ``` |
| To | ``` typealias uuid_string_t = Darwin.__darwin_uuid_string_t ``` |

Modified uuid_t

|  | Declaration |
| --- | --- |
| From | ``` typealias uuid_t = __darwin_uuid_t ``` |
| To | ``` typealias uuid_t = Darwin.__darwin_uuid_t ``` |

Modified uuid_unparse(_: UnsafePointer<UInt8>!, _: UnsafeMutablePointer<Int8>!)

|  | Declaration |
| --- | --- |
| From | ``` func uuid_unparse(_ uu: UnsafePointer<UInt8>, _ out: UnsafeMutablePointer<Int8>) ``` |
| To | ``` func uuid_unparse(_ uu: UnsafePointer<UInt8>!, _ out: UnsafeMutablePointer<Int8>!) ``` |

Modified uuid_unparse_lower(_: UnsafePointer<UInt8>!, _: UnsafeMutablePointer<Int8>!)

|  | Declaration |
| --- | --- |
| From | ``` func uuid_unparse_lower(_ uu: UnsafePointer<UInt8>, _ out: UnsafeMutablePointer<Int8>) ``` |
| To | ``` func uuid_unparse_lower(_ uu: UnsafePointer<UInt8>!, _ out: UnsafeMutablePointer<Int8>!) ``` |

Modified uuid_unparse_upper(_: UnsafePointer<UInt8>!, _: UnsafeMutablePointer<Int8>!)

|  | Declaration |
| --- | --- |
| From | ``` func uuid_unparse_upper(_ uu: UnsafePointer<UInt8>, _ out: UnsafeMutablePointer<Int8>) ``` |
| To | ``` func uuid_unparse_upper(_ uu: UnsafePointer<UInt8>!, _ out: UnsafeMutablePointer<Int8>!) ``` |

Modified valloc(_: Int) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func valloc(_ _: Int) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func valloc(_ _: Int) -> UnsafeMutableRawPointer! ``` |

Modified vasprintf(_: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: UnsafePointer<Int8>!, _: CVaListPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vasprintf(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func vasprintf(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: UnsafePointer<Int8>!, _ _: CVaListPointer!) -> Int32 ``` |

Modified vasprintf_l(_: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _: locale_t!, _: UnsafePointer<Int8>!, _: CVaListPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vasprintf_l(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: locale_t, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func vasprintf_l(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>?>!, _ _: locale_t!, _ _: UnsafePointer<Int8>!, _ _: CVaListPointer!) -> Int32 ``` |

Modified vdprintf(_: Int32, _: UnsafePointer<Int8>!, _: CVaListPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vdprintf(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func vdprintf(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: CVaListPointer!) -> Int32 ``` |

Modified vdprintf_l(_: Int32, _: locale_t!, _: UnsafePointer<Int8>!, _: CVaListPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vdprintf_l(_ _: Int32, _ _: locale_t, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func vdprintf_l(_ _: Int32, _ _: locale_t!, _ _: UnsafePointer<Int8>!, _ _: CVaListPointer!) -> Int32 ``` |

Modified verr(_: Int32, _: UnsafePointer<Int8>!, _: __darwin_va_list!) -> Never

|  | Declaration |
| --- | --- |
| From | ``` @noreturn func verr(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: __darwin_va_list) ``` |
| To | ``` func verr(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: __darwin_va_list!) -> Never ``` |

Modified verrc(_: Int32, _: Int32, _: UnsafePointer<Int8>!, _: __darwin_va_list!) -> Never

|  | Declaration |
| --- | --- |
| From | ``` @noreturn func verrc(_ _: Int32, _ _: Int32, _ _: UnsafePointer<Int8>, _ _: __darwin_va_list) ``` |
| To | ``` func verrc(_ _: Int32, _ _: Int32, _ _: UnsafePointer<Int8>!, _ _: __darwin_va_list!) -> Never ``` |

Modified verrx(_: Int32, _: UnsafePointer<Int8>!, _: __darwin_va_list!) -> Never

|  | Declaration |
| --- | --- |
| From | ``` @noreturn func verrx(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: __darwin_va_list) ``` |
| To | ``` func verrx(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: __darwin_va_list!) -> Never ``` |

Modified vfprintf(_: UnsafeMutablePointer<FILE>!, _: UnsafePointer<Int8>!, _: CVaListPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vfprintf(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func vfprintf(_ _: UnsafeMutablePointer<FILE>!, _ _: UnsafePointer<Int8>!, _ _: CVaListPointer!) -> Int32 ``` |

Modified vfprintf_l(_: UnsafeMutablePointer<FILE>!, _: locale_t!, _: UnsafePointer<Int8>!, _: CVaListPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vfprintf_l(_ _: UnsafeMutablePointer<FILE>, _ _: locale_t, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func vfprintf_l(_ _: UnsafeMutablePointer<FILE>!, _ _: locale_t!, _ _: UnsafePointer<Int8>!, _ _: CVaListPointer!) -> Int32 ``` |

Modified vfscanf(_: UnsafeMutablePointer<FILE>!, _: UnsafePointer<Int8>!, _: CVaListPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vfscanf(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func vfscanf(_ __stream: UnsafeMutablePointer<FILE>!, _ __format: UnsafePointer<Int8>!, _ _: CVaListPointer!) -> Int32 ``` |

Modified vfscanf_l(_: UnsafeMutablePointer<FILE>!, _: locale_t!, _: UnsafePointer<Int8>!, _: CVaListPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vfscanf_l(_ _: UnsafeMutablePointer<FILE>, _ _: locale_t, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func vfscanf_l(_ _: UnsafeMutablePointer<FILE>!, _ _: locale_t!, _ _: UnsafePointer<Int8>!, _ _: CVaListPointer!) -> Int32 ``` |

Modified vfwprintf(_: UnsafeMutablePointer<FILE>!, _: UnsafePointer<wchar_t>!, _: __darwin_va_list!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vfwprintf(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafePointer<wchar_t>, _ _: __darwin_va_list) -> Int32 ``` |
| To | ``` func vfwprintf(_ _: UnsafeMutablePointer<FILE>!, _ _: UnsafePointer<wchar_t>!, _ _: __darwin_va_list!) -> Int32 ``` |

Modified vfwprintf_l(_: UnsafeMutablePointer<FILE>!, _: locale_t!, _: UnsafePointer<wchar_t>!, _: __darwin_va_list!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vfwprintf_l(_ _: UnsafeMutablePointer<FILE>, _ _: locale_t, _ _: UnsafePointer<wchar_t>, _ _: __darwin_va_list) -> Int32 ``` |
| To | ``` func vfwprintf_l(_ _: UnsafeMutablePointer<FILE>!, _ _: locale_t!, _ _: UnsafePointer<wchar_t>!, _ _: __darwin_va_list!) -> Int32 ``` |

Modified vfwscanf(_: UnsafeMutablePointer<FILE>!, _: UnsafePointer<wchar_t>!, _: __darwin_va_list!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vfwscanf(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafePointer<wchar_t>, _ _: __darwin_va_list) -> Int32 ``` |
| To | ``` func vfwscanf(_ _: UnsafeMutablePointer<FILE>!, _ _: UnsafePointer<wchar_t>!, _ _: __darwin_va_list!) -> Int32 ``` |

Modified vfwscanf_l(_: UnsafeMutablePointer<FILE>!, _: locale_t!, _: UnsafePointer<wchar_t>!, _: __darwin_va_list!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vfwscanf_l(_ _: UnsafeMutablePointer<FILE>, _ _: locale_t, _ _: UnsafePointer<wchar_t>, _ _: __darwin_va_list) -> Int32 ``` |
| To | ``` func vfwscanf_l(_ _: UnsafeMutablePointer<FILE>!, _ _: locale_t!, _ _: UnsafePointer<wchar_t>!, _ _: __darwin_va_list!) -> Int32 ``` |

Modified vm_allocate(_: vm_map_t, _: UnsafeMutablePointer<vm_address_t>!, _: vm_size_t, _: Int32) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vm_allocate(_ target_task: vm_map_t, _ address: UnsafeMutablePointer<vm_address_t>, _ size: vm_size_t, _ flags: Int32) -> kern_return_t ``` |
| To | ``` func vm_allocate(_ target_task: vm_map_t, _ address: UnsafeMutablePointer<vm_address_t>!, _ size: vm_size_t, _ flags: Int32) -> kern_return_t ``` |

Modified vm_allocate_cpm(_: host_priv_t, _: vm_map_t, _: UnsafeMutablePointer<vm_address_t>!, _: vm_size_t, _: Int32) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vm_allocate_cpm(_ host_priv: host_priv_t, _ task: vm_map_t, _ address: UnsafeMutablePointer<vm_address_t>, _ size: vm_size_t, _ flags: Int32) -> kern_return_t ``` |
| To | ``` func vm_allocate_cpm(_ host_priv: host_priv_t, _ task: vm_map_t, _ address: UnsafeMutablePointer<vm_address_t>!, _ size: vm_size_t, _ flags: Int32) -> kern_return_t ``` |

Modified vm_machine_attribute(_: vm_map_t, _: vm_address_t, _: vm_size_t, _: vm_machine_attribute_t, _: UnsafeMutablePointer<vm_machine_attribute_val_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vm_machine_attribute(_ target_task: vm_map_t, _ address: vm_address_t, _ size: vm_size_t, _ attribute: vm_machine_attribute_t, _ value: UnsafeMutablePointer<vm_machine_attribute_val_t>) -> kern_return_t ``` |
| To | ``` func vm_machine_attribute(_ target_task: vm_map_t, _ address: vm_address_t, _ size: vm_size_t, _ attribute: vm_machine_attribute_t, _ value: UnsafeMutablePointer<vm_machine_attribute_val_t>!) -> kern_return_t ``` |

Modified vm_map(_: vm_map_t, _: UnsafeMutablePointer<vm_address_t>!, _: vm_size_t, _: vm_address_t, _: Int32, _: mem_entry_name_port_t, _: vm_offset_t, _: boolean_t, _: vm_prot_t, _: vm_prot_t, _: vm_inherit_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vm_map(_ target_task: vm_map_t, _ address: UnsafeMutablePointer<vm_address_t>, _ size: vm_size_t, _ mask: vm_address_t, _ flags: Int32, _ object: mem_entry_name_port_t, _ offset: vm_offset_t, _ copy: boolean_t, _ cur_protection: vm_prot_t, _ max_protection: vm_prot_t, _ inheritance: vm_inherit_t) -> kern_return_t ``` |
| To | ``` func vm_map(_ target_task: vm_map_t, _ address: UnsafeMutablePointer<vm_address_t>!, _ size: vm_size_t, _ mask: vm_address_t, _ flags: Int32, _ object: mem_entry_name_port_t, _ offset: vm_offset_t, _ copy: boolean_t, _ cur_protection: vm_prot_t, _ max_protection: vm_prot_t, _ inheritance: vm_inherit_t) -> kern_return_t ``` |

Modified vm_map_64(_: vm_map_t, _: UnsafeMutablePointer<vm_address_t>!, _: vm_size_t, _: vm_address_t, _: Int32, _: mem_entry_name_port_t, _: memory_object_offset_t, _: boolean_t, _: vm_prot_t, _: vm_prot_t, _: vm_inherit_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vm_map_64(_ target_task: vm_map_t, _ address: UnsafeMutablePointer<vm_address_t>, _ size: vm_size_t, _ mask: vm_address_t, _ flags: Int32, _ object: mem_entry_name_port_t, _ offset: memory_object_offset_t, _ copy: boolean_t, _ cur_protection: vm_prot_t, _ max_protection: vm_prot_t, _ inheritance: vm_inherit_t) -> kern_return_t ``` |
| To | ``` func vm_map_64(_ target_task: vm_map_t, _ address: UnsafeMutablePointer<vm_address_t>!, _ size: vm_size_t, _ mask: vm_address_t, _ flags: Int32, _ object: mem_entry_name_port_t, _ offset: memory_object_offset_t, _ copy: boolean_t, _ cur_protection: vm_prot_t, _ max_protection: vm_prot_t, _ inheritance: vm_inherit_t) -> kern_return_t ``` |

Modified vm_map_address_t

|  | Declaration |
| --- | --- |
| From | ``` typealias vm_map_address_t = UInt32 ``` |
| To | ``` typealias vm_map_address_t = UInt64 ``` |

Modified vm_map_offset_t

|  | Declaration |
| --- | --- |
| From | ``` typealias vm_map_offset_t = UInt32 ``` |
| To | ``` typealias vm_map_offset_t = UInt64 ``` |

Modified vm_map_page_query(_: vm_map_t, _: vm_offset_t, _: UnsafeMutablePointer<integer_t>!, _: UnsafeMutablePointer<integer_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vm_map_page_query(_ target_map: vm_map_t, _ offset: vm_offset_t, _ disposition: UnsafeMutablePointer<integer_t>, _ ref_count: UnsafeMutablePointer<integer_t>) -> kern_return_t ``` |
| To | ``` func vm_map_page_query(_ target_map: vm_map_t, _ offset: vm_offset_t, _ disposition: UnsafeMutablePointer<integer_t>!, _ ref_count: UnsafeMutablePointer<integer_t>!) -> kern_return_t ``` |

Modified vm_map_size_t

|  | Declaration |
| --- | --- |
| From | ``` typealias vm_map_size_t = UInt32 ``` |
| To | ``` typealias vm_map_size_t = UInt64 ``` |

Modified vm_mapped_pages_info(_: vm_map_t, _: UnsafeMutablePointer<page_address_array_t?>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vm_mapped_pages_info(_ task: vm_map_t, _ pages: UnsafeMutablePointer<page_address_array_t>, _ pagesCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func vm_mapped_pages_info(_ task: vm_map_t, _ pages: UnsafeMutablePointer<page_address_array_t?>!, _ pagesCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified vm_offset_t

|  | Declaration |
| --- | --- |
| From | ``` typealias vm_offset_t = natural_t ``` |
| To | ``` typealias vm_offset_t = UInt ``` |

Modified vm_purgable_control(_: vm_map_t, _: vm_address_t, _: vm_purgable_t, _: UnsafeMutablePointer<Int32>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vm_purgable_control(_ target_task: vm_map_t, _ address: vm_address_t, _ control: vm_purgable_t, _ state: UnsafeMutablePointer<Int32>) -> kern_return_t ``` |
| To | ``` func vm_purgable_control(_ target_task: vm_map_t, _ address: vm_address_t, _ control: vm_purgable_t, _ state: UnsafeMutablePointer<Int32>!) -> kern_return_t ``` |

Modified vm_range_recorder_t

|  | Declaration |
| --- | --- |
| From | ``` typealias vm_range_recorder_t = (task_t, UnsafeMutablePointer<Void>, UInt32, UnsafeMutablePointer<vm_range_t>, UInt32) -> Void ``` |
| To | ``` typealias vm_range_recorder_t = (task_t, UnsafeMutableRawPointer?, UInt32, UnsafeMutablePointer<vm_range_t>?, UInt32) -> Swift.Void ``` |

Modified vm_read(_: vm_map_t, _: vm_address_t, _: vm_size_t, _: UnsafeMutablePointer<vm_offset_t>!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vm_read(_ target_task: vm_map_t, _ address: vm_address_t, _ size: vm_size_t, _ data: UnsafeMutablePointer<vm_offset_t>, _ dataCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func vm_read(_ target_task: vm_map_t, _ address: vm_address_t, _ size: vm_size_t, _ data: UnsafeMutablePointer<vm_offset_t>!, _ dataCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified vm_read_list(_: vm_map_t, _: UnsafeMutablePointer<vm_read_entry>!, _: natural_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vm_read_list(_ target_task: vm_map_t, _ data_list: UnsafeMutablePointer<vm_read_entry>, _ count: natural_t) -> kern_return_t ``` |
| To | ``` func vm_read_list(_ target_task: vm_map_t, _ data_list: UnsafeMutablePointer<vm_read_entry>!, _ count: natural_t) -> kern_return_t ``` |

Modified vm_read_overwrite(_: vm_map_t, _: vm_address_t, _: vm_size_t, _: vm_address_t, _: UnsafeMutablePointer<vm_size_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vm_read_overwrite(_ target_task: vm_map_t, _ address: vm_address_t, _ size: vm_size_t, _ data: vm_address_t, _ outsize: UnsafeMutablePointer<vm_size_t>) -> kern_return_t ``` |
| To | ``` func vm_read_overwrite(_ target_task: vm_map_t, _ address: vm_address_t, _ size: vm_size_t, _ data: vm_address_t, _ outsize: UnsafeMutablePointer<vm_size_t>!) -> kern_return_t ``` |

Modified vm_region(_: vm_map_t, _: UnsafeMutablePointer<vm_address_t>!, _: UnsafeMutablePointer<vm_size_t>!, _: vm_region_flavor_t, _: vm_region_info_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vm_region(_ target_task: vm_map_t, _ address: UnsafeMutablePointer<vm_address_t>, _ size: UnsafeMutablePointer<vm_size_t>, _ flavor: vm_region_flavor_t, _ info: vm_region_info_t, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ object_name: UnsafeMutablePointer<mach_port_t>) -> kern_return_t ``` |
| To | ``` func vm_region(_ target_task: vm_map_t, _ address: UnsafeMutablePointer<vm_address_t>!, _ size: UnsafeMutablePointer<vm_size_t>!, _ flavor: vm_region_flavor_t, _ info: vm_region_info_t!, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ object_name: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t ``` |

Modified vm_region_64(_: vm_map_t, _: UnsafeMutablePointer<vm_address_t>!, _: UnsafeMutablePointer<vm_size_t>!, _: vm_region_flavor_t, _: vm_region_info_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!, _: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vm_region_64(_ target_task: vm_map_t, _ address: UnsafeMutablePointer<vm_address_t>, _ size: UnsafeMutablePointer<vm_size_t>, _ flavor: vm_region_flavor_t, _ info: vm_region_info_t, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>, _ object_name: UnsafeMutablePointer<mach_port_t>) -> kern_return_t ``` |
| To | ``` func vm_region_64(_ target_task: vm_map_t, _ address: UnsafeMutablePointer<vm_address_t>!, _ size: UnsafeMutablePointer<vm_size_t>!, _ flavor: vm_region_flavor_t, _ info: vm_region_info_t!, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>!, _ object_name: UnsafeMutablePointer<mach_port_t>!) -> kern_return_t ``` |

Modified vm_region_recurse(_: vm_map_t, _: UnsafeMutablePointer<vm_address_t>!, _: UnsafeMutablePointer<vm_size_t>!, _: UnsafeMutablePointer<natural_t>!, _: vm_region_recurse_info_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vm_region_recurse(_ target_task: vm_map_t, _ address: UnsafeMutablePointer<vm_address_t>, _ size: UnsafeMutablePointer<vm_size_t>, _ nesting_depth: UnsafeMutablePointer<natural_t>, _ info: vm_region_recurse_info_t, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func vm_region_recurse(_ target_task: vm_map_t, _ address: UnsafeMutablePointer<vm_address_t>!, _ size: UnsafeMutablePointer<vm_size_t>!, _ nesting_depth: UnsafeMutablePointer<natural_t>!, _ info: vm_region_recurse_info_t!, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified vm_region_recurse_64(_: vm_map_t, _: UnsafeMutablePointer<vm_address_t>!, _: UnsafeMutablePointer<vm_size_t>!, _: UnsafeMutablePointer<natural_t>!, _: vm_region_recurse_info_t!, _: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vm_region_recurse_64(_ target_task: vm_map_t, _ address: UnsafeMutablePointer<vm_address_t>, _ size: UnsafeMutablePointer<vm_size_t>, _ nesting_depth: UnsafeMutablePointer<natural_t>, _ info: vm_region_recurse_info_t, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>) -> kern_return_t ``` |
| To | ``` func vm_region_recurse_64(_ target_task: vm_map_t, _ address: UnsafeMutablePointer<vm_address_t>!, _ size: UnsafeMutablePointer<vm_size_t>!, _ nesting_depth: UnsafeMutablePointer<natural_t>!, _ info: vm_region_recurse_info_t!, _ infoCnt: UnsafeMutablePointer<mach_msg_type_number_t>!) -> kern_return_t ``` |

Modified vm_remap(_: vm_map_t, _: UnsafeMutablePointer<vm_address_t>!, _: vm_size_t, _: vm_address_t, _: Int32, _: vm_map_t, _: vm_address_t, _: boolean_t, _: UnsafeMutablePointer<vm_prot_t>!, _: UnsafeMutablePointer<vm_prot_t>!, _: vm_inherit_t) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func vm_remap(_ target_task: vm_map_t, _ target_address: UnsafeMutablePointer<vm_address_t>, _ size: vm_size_t, _ mask: vm_address_t, _ flags: Int32, _ src_task: vm_map_t, _ src_address: vm_address_t, _ copy: boolean_t, _ cur_protection: UnsafeMutablePointer<vm_prot_t>, _ max_protection: UnsafeMutablePointer<vm_prot_t>, _ inheritance: vm_inherit_t) -> kern_return_t ``` |
| To | ``` func vm_remap(_ target_task: vm_map_t, _ target_address: UnsafeMutablePointer<vm_address_t>!, _ size: vm_size_t, _ mask: vm_address_t, _ flags: Int32, _ src_task: vm_map_t, _ src_address: vm_address_t, _ copy: boolean_t, _ cur_protection: UnsafeMutablePointer<vm_prot_t>!, _ max_protection: UnsafeMutablePointer<vm_prot_t>!, _ inheritance: vm_inherit_t) -> kern_return_t ``` |

Modified vm_size_t

|  | Declaration |
| --- | --- |
| From | ``` typealias vm_size_t = natural_t ``` |
| To | ``` typealias vm_size_t = UInt ``` |

Modified vnode_t

|  | Declaration |
| --- | --- |
| From | ``` typealias vnode_t = COpaquePointer ``` |
| To | ``` typealias vnode_t = OpaquePointer ``` |

Modified voucher_mach_msg_adopt(_: UnsafeMutablePointer<mach_msg_header_t>!) -> voucher_mach_msg_state_t!

|  | Declaration |
| --- | --- |
| From | ``` func voucher_mach_msg_adopt(_ msg: UnsafeMutablePointer<mach_msg_header_t>) -> voucher_mach_msg_state_t ``` |
| To | ``` func voucher_mach_msg_adopt(_ msg: UnsafeMutablePointer<mach_msg_header_t>!) -> voucher_mach_msg_state_t! ``` |

Modified voucher_mach_msg_clear(_: UnsafeMutablePointer<mach_msg_header_t>!)

|  | Declaration |
| --- | --- |
| From | ``` func voucher_mach_msg_clear(_ msg: UnsafeMutablePointer<mach_msg_header_t>) ``` |
| To | ``` func voucher_mach_msg_clear(_ msg: UnsafeMutablePointer<mach_msg_header_t>!) ``` |

Modified voucher_mach_msg_revert(_: voucher_mach_msg_state_t!)

|  | Declaration |
| --- | --- |
| From | ``` func voucher_mach_msg_revert(_ state: voucher_mach_msg_state_t) ``` |
| To | ``` func voucher_mach_msg_revert(_ state: voucher_mach_msg_state_t!) ``` |

Modified voucher_mach_msg_set(_: UnsafeMutablePointer<mach_msg_header_t>!) -> boolean_t

|  | Declaration |
| --- | --- |
| From | ``` func voucher_mach_msg_set(_ msg: UnsafeMutablePointer<mach_msg_header_t>) -> boolean_t ``` |
| To | ``` func voucher_mach_msg_set(_ msg: UnsafeMutablePointer<mach_msg_header_t>!) -> boolean_t ``` |

Modified voucher_mach_msg_state_t

|  | Declaration |
| --- | --- |
| From | ``` typealias voucher_mach_msg_state_t = COpaquePointer ``` |
| To | ``` typealias voucher_mach_msg_state_t = OpaquePointer ``` |

Modified vprintf(_: UnsafePointer<Int8>!, _: CVaListPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vprintf(_ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func vprintf(_ _: UnsafePointer<Int8>!, _ _: CVaListPointer!) -> Int32 ``` |

Modified vprintf_l(_: locale_t!, _: UnsafePointer<Int8>!, _: CVaListPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vprintf_l(_ _: locale_t, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func vprintf_l(_ _: locale_t!, _ _: UnsafePointer<Int8>!, _ _: CVaListPointer!) -> Int32 ``` |

Modified vprintf_stderr_func

|  | Declaration |
| --- | --- |
| From | ``` var vprintf_stderr_func: ((UnsafePointer<Int8>, CVaListPointer) -> Int32)! ``` |
| To | ``` var vprintf_stderr_func: ((UnsafePointer<Int8>?, CVaListPointer?) -> Int32)! ``` |

Modified vscanf(_: UnsafePointer<Int8>!, _: CVaListPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vscanf(_ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func vscanf(_ __format: UnsafePointer<Int8>!, _ _: CVaListPointer!) -> Int32 ``` |

Modified vscanf_l(_: locale_t!, _: UnsafePointer<Int8>!, _: CVaListPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vscanf_l(_ _: locale_t, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func vscanf_l(_ _: locale_t!, _ _: UnsafePointer<Int8>!, _ _: CVaListPointer!) -> Int32 ``` |

Modified vsnprintf(_: UnsafeMutablePointer<Int8>!, _: Int, _: UnsafePointer<Int8>!, _: CVaListPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vsnprintf(_ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func vsnprintf(_ __str: UnsafeMutablePointer<Int8>!, _ __size: Int, _ __format: UnsafePointer<Int8>!, _ _: CVaListPointer!) -> Int32 ``` |

Modified vsnprintf_l(_: UnsafeMutablePointer<Int8>!, _: Int, _: locale_t!, _: UnsafePointer<Int8>!, _: CVaListPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vsnprintf_l(_ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: locale_t, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func vsnprintf_l(_ _: UnsafeMutablePointer<Int8>!, _ _: Int, _ _: locale_t!, _ _: UnsafePointer<Int8>!, _ _: CVaListPointer!) -> Int32 ``` |

Modified vsscanf(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: CVaListPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vsscanf(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func vsscanf(_ __str: UnsafePointer<Int8>!, _ __format: UnsafePointer<Int8>!, _ _: CVaListPointer!) -> Int32 ``` |

Modified vsscanf_l(_: UnsafePointer<Int8>!, _: locale_t!, _: UnsafePointer<Int8>!, _: CVaListPointer!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vsscanf_l(_ _: UnsafePointer<Int8>, _ _: locale_t, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func vsscanf_l(_ _: UnsafePointer<Int8>!, _ _: locale_t!, _ _: UnsafePointer<Int8>!, _ _: CVaListPointer!) -> Int32 ``` |

Modified vswprintf(_: UnsafeMutablePointer<wchar_t>!, _: Int, _: UnsafePointer<wchar_t>!, _: __darwin_va_list!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vswprintf(_ _: UnsafeMutablePointer<wchar_t>, _ _: Int, _ _: UnsafePointer<wchar_t>, _ _: __darwin_va_list) -> Int32 ``` |
| To | ``` func vswprintf(_ _: UnsafeMutablePointer<wchar_t>!, _ _: Int, _ _: UnsafePointer<wchar_t>!, _ _: __darwin_va_list!) -> Int32 ``` |

Modified vswprintf_l(_: UnsafeMutablePointer<wchar_t>!, _: Int, _: locale_t!, _: UnsafePointer<wchar_t>!, _: __darwin_va_list!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vswprintf_l(_ _: UnsafeMutablePointer<wchar_t>, _ n: Int, _ _: locale_t, _ _: UnsafePointer<wchar_t>, _ _: __darwin_va_list) -> Int32 ``` |
| To | ``` func vswprintf_l(_ _: UnsafeMutablePointer<wchar_t>!, _ n: Int, _ _: locale_t!, _ _: UnsafePointer<wchar_t>!, _ _: __darwin_va_list!) -> Int32 ``` |

Modified vswscanf(_: UnsafePointer<wchar_t>!, _: UnsafePointer<wchar_t>!, _: __darwin_va_list!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vswscanf(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: __darwin_va_list) -> Int32 ``` |
| To | ``` func vswscanf(_ _: UnsafePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!, _ _: __darwin_va_list!) -> Int32 ``` |

Modified vswscanf_l(_: UnsafePointer<wchar_t>!, _: locale_t!, _: UnsafePointer<wchar_t>!, _: __darwin_va_list!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vswscanf_l(_ _: UnsafePointer<wchar_t>, _ _: locale_t, _ _: UnsafePointer<wchar_t>, _ _: __darwin_va_list) -> Int32 ``` |
| To | ``` func vswscanf_l(_ _: UnsafePointer<wchar_t>!, _ _: locale_t!, _ _: UnsafePointer<wchar_t>!, _ _: __darwin_va_list!) -> Int32 ``` |

Modified vsyslog(_: Int32, _: UnsafePointer<Int8>!, _: __darwin_va_list!)

|  | Declaration |
| --- | --- |
| From | ``` func vsyslog(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: __darwin_va_list) ``` |
| To | ``` func vsyslog(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: __darwin_va_list!) ``` |

Modified vwarn(_: UnsafePointer<Int8>!, _: __darwin_va_list!)

|  | Declaration |
| --- | --- |
| From | ``` func vwarn(_ _: UnsafePointer<Int8>, _ _: __darwin_va_list) ``` |
| To | ``` func vwarn(_ _: UnsafePointer<Int8>!, _ _: __darwin_va_list!) ``` |

Modified vwarnc(_: Int32, _: UnsafePointer<Int8>!, _: __darwin_va_list!)

|  | Declaration |
| --- | --- |
| From | ``` func vwarnc(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: __darwin_va_list) ``` |
| To | ``` func vwarnc(_ _: Int32, _ _: UnsafePointer<Int8>!, _ _: __darwin_va_list!) ``` |

Modified vwarnx(_: UnsafePointer<Int8>!, _: __darwin_va_list!)

|  | Declaration |
| --- | --- |
| From | ``` func vwarnx(_ _: UnsafePointer<Int8>, _ _: __darwin_va_list) ``` |
| To | ``` func vwarnx(_ _: UnsafePointer<Int8>!, _ _: __darwin_va_list!) ``` |

Modified vwprintf(_: UnsafePointer<wchar_t>!, _: __darwin_va_list!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vwprintf(_ _: UnsafePointer<wchar_t>, _ _: __darwin_va_list) -> Int32 ``` |
| To | ``` func vwprintf(_ _: UnsafePointer<wchar_t>!, _ _: __darwin_va_list!) -> Int32 ``` |

Modified vwprintf_l(_: locale_t!, _: UnsafePointer<wchar_t>!, _: __darwin_va_list!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vwprintf_l(_ _: locale_t, _ _: UnsafePointer<wchar_t>, _ _: __darwin_va_list) -> Int32 ``` |
| To | ``` func vwprintf_l(_ _: locale_t!, _ _: UnsafePointer<wchar_t>!, _ _: __darwin_va_list!) -> Int32 ``` |

Modified vwscanf(_: UnsafePointer<wchar_t>!, _: __darwin_va_list!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vwscanf(_ _: UnsafePointer<wchar_t>, _ _: __darwin_va_list) -> Int32 ``` |
| To | ``` func vwscanf(_ _: UnsafePointer<wchar_t>!, _ _: __darwin_va_list!) -> Int32 ``` |

Modified vwscanf_l(_: locale_t!, _: UnsafePointer<wchar_t>!, _: __darwin_va_list!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vwscanf_l(_ _: locale_t, _ _: UnsafePointer<wchar_t>, _ _: __darwin_va_list) -> Int32 ``` |
| To | ``` func vwscanf_l(_ _: locale_t!, _ _: UnsafePointer<wchar_t>!, _ _: __darwin_va_list!) -> Int32 ``` |

Modified wait(_: UnsafeMutablePointer<Int32>!) -> pid_t

|  | Declaration |
| --- | --- |
| From | ``` func wait(_ _: UnsafeMutablePointer<Int32>) -> pid_t ``` |
| To | ``` func wait(_ _: UnsafeMutablePointer<Int32>!) -> pid_t ``` |

Modified wait3(_: UnsafeMutablePointer<Int32>!, _: Int32, _: UnsafeMutablePointer<rusage>!) -> pid_t

|  | Declaration |
| --- | --- |
| From | ``` func wait3(_ _: UnsafeMutablePointer<Int32>, _ _: Int32, _ _: UnsafeMutablePointer<rusage>) -> pid_t ``` |
| To | ``` func wait3(_ _: UnsafeMutablePointer<Int32>!, _ _: Int32, _ _: UnsafeMutablePointer<rusage>!) -> pid_t ``` |

Modified wait4(_: pid_t, _: UnsafeMutablePointer<Int32>!, _: Int32, _: UnsafeMutablePointer<rusage>!) -> pid_t

|  | Declaration |
| --- | --- |
| From | ``` func wait4(_ _: pid_t, _ _: UnsafeMutablePointer<Int32>, _ _: Int32, _ _: UnsafeMutablePointer<rusage>) -> pid_t ``` |
| To | ``` func wait4(_ _: pid_t, _ _: UnsafeMutablePointer<Int32>!, _ _: Int32, _ _: UnsafeMutablePointer<rusage>!) -> pid_t ``` |

Modified waitid(_: idtype_t, _: id_t, _: UnsafeMutablePointer<siginfo_t>!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func waitid(_ _: idtype_t, _ _: id_t, _ _: UnsafeMutablePointer<siginfo_t>, _ _: Int32) -> Int32 ``` |
| To | ``` func waitid(_ _: idtype_t, _ _: id_t, _ _: UnsafeMutablePointer<siginfo_t>!, _ _: Int32) -> Int32 ``` |

Modified waitpid(_: pid_t, _: UnsafeMutablePointer<Int32>!, _: Int32) -> pid_t

|  | Declaration |
| --- | --- |
| From | ``` func waitpid(_ _: pid_t, _ _: UnsafeMutablePointer<Int32>, _ _: Int32) -> pid_t ``` |
| To | ``` func waitpid(_ _: pid_t, _ _: UnsafeMutablePointer<Int32>!, _ _: Int32) -> pid_t ``` |

Modified wcpcpy(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<wchar_t>!) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func wcpcpy(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func wcpcpy(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified wcpncpy(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<wchar_t>!, _: Int) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func wcpncpy(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func wcpncpy(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!, _ _: Int) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified wcrtomb(_: UnsafeMutablePointer<Int8>!, _: wchar_t, _: UnsafeMutablePointer<mbstate_t>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcrtomb(_ _: UnsafeMutablePointer<Int8>, _ _: wchar_t, _ _: UnsafeMutablePointer<mbstate_t>) -> Int ``` |
| To | ``` func wcrtomb(_ _: UnsafeMutablePointer<Int8>!, _ _: wchar_t, _ _: UnsafeMutablePointer<mbstate_t>!) -> Int ``` |

Modified wcrtomb_l(_: UnsafeMutablePointer<Int8>!, _: wchar_t, _: UnsafeMutablePointer<mbstate_t>!, _: locale_t!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcrtomb_l(_ _: UnsafeMutablePointer<Int8>, _ _: wchar_t, _ _: UnsafeMutablePointer<mbstate_t>, _ _: locale_t) -> Int ``` |
| To | ``` func wcrtomb_l(_ _: UnsafeMutablePointer<Int8>!, _ _: wchar_t, _ _: UnsafeMutablePointer<mbstate_t>!, _ _: locale_t!) -> Int ``` |

Modified wcscasecmp(_: UnsafePointer<wchar_t>!, _: UnsafePointer<wchar_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func wcscasecmp(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>) -> Int32 ``` |
| To | ``` func wcscasecmp(_ _: UnsafePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!) -> Int32 ``` |

Modified wcscasecmp_l(_: UnsafePointer<wchar_t>!, _: UnsafePointer<wchar_t>!, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func wcscasecmp_l(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: locale_t) -> Int32 ``` |
| To | ``` func wcscasecmp_l(_ _: UnsafePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!, _ _: locale_t!) -> Int32 ``` |

Modified wcscat(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<wchar_t>!) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func wcscat(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func wcscat(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified wcschr(_: UnsafePointer<wchar_t>!, _: wchar_t) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func wcschr(_ _: UnsafePointer<wchar_t>, _ _: wchar_t) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func wcschr(_ _: UnsafePointer<wchar_t>!, _ _: wchar_t) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified wcscmp(_: UnsafePointer<wchar_t>!, _: UnsafePointer<wchar_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func wcscmp(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>) -> Int32 ``` |
| To | ``` func wcscmp(_ _: UnsafePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!) -> Int32 ``` |

Modified wcscoll(_: UnsafePointer<wchar_t>!, _: UnsafePointer<wchar_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func wcscoll(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>) -> Int32 ``` |
| To | ``` func wcscoll(_ _: UnsafePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!) -> Int32 ``` |

Modified wcscoll_l(_: UnsafePointer<wchar_t>!, _: UnsafePointer<wchar_t>!, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func wcscoll_l(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: locale_t) -> Int32 ``` |
| To | ``` func wcscoll_l(_ _: UnsafePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!, _ _: locale_t!) -> Int32 ``` |

Modified wcscpy(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<wchar_t>!) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func wcscpy(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func wcscpy(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified wcscspn(_: UnsafePointer<wchar_t>!, _: UnsafePointer<wchar_t>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcscspn(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>) -> Int ``` |
| To | ``` func wcscspn(_ _: UnsafePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!) -> Int ``` |

Modified wcsdup(_: UnsafePointer<wchar_t>!) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func wcsdup(_ _: UnsafePointer<wchar_t>) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func wcsdup(_ _: UnsafePointer<wchar_t>!) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified wcsftime(_: UnsafeMutablePointer<wchar_t>!, _: Int, _: UnsafePointer<wchar_t>!, _: UnsafePointer<tm>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcsftime(_ _: UnsafeMutablePointer<wchar_t>, _ _: Int, _ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<tm>) -> Int ``` |
| To | ``` func wcsftime(_ _: UnsafeMutablePointer<wchar_t>!, _ _: Int, _ _: UnsafePointer<wchar_t>!, _ _: UnsafePointer<tm>!) -> Int ``` |

Modified wcsftime_l(_: UnsafeMutablePointer<wchar_t>!, _: Int, _: UnsafePointer<wchar_t>!, _: UnsafePointer<tm>!, _: locale_t!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcsftime_l(_ _: UnsafeMutablePointer<wchar_t>, _ _: Int, _ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<tm>, _ _: locale_t) -> Int ``` |
| To | ``` func wcsftime_l(_ _: UnsafeMutablePointer<wchar_t>!, _ _: Int, _ _: UnsafePointer<wchar_t>!, _ _: UnsafePointer<tm>!, _ _: locale_t!) -> Int ``` |

Modified wcslcat(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<wchar_t>!, _: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcslcat(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> Int ``` |
| To | ``` func wcslcat(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!, _ _: Int) -> Int ``` |

Modified wcslcpy(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<wchar_t>!, _: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcslcpy(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> Int ``` |
| To | ``` func wcslcpy(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!, _ _: Int) -> Int ``` |

Modified wcslen(_: UnsafePointer<wchar_t>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcslen(_ _: UnsafePointer<wchar_t>) -> Int ``` |
| To | ``` func wcslen(_ _: UnsafePointer<wchar_t>!) -> Int ``` |

Modified wcsncasecmp(_: UnsafePointer<wchar_t>!, _: UnsafePointer<wchar_t>!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func wcsncasecmp(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ n: Int) -> Int32 ``` |
| To | ``` func wcsncasecmp(_ _: UnsafePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!, _ n: Int) -> Int32 ``` |

Modified wcsncasecmp_l(_: UnsafePointer<wchar_t>!, _: UnsafePointer<wchar_t>!, _: Int, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func wcsncasecmp_l(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ n: Int, _ _: locale_t) -> Int32 ``` |
| To | ``` func wcsncasecmp_l(_ _: UnsafePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!, _ n: Int, _ _: locale_t!) -> Int32 ``` |

Modified wcsncat(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<wchar_t>!, _: Int) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func wcsncat(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func wcsncat(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!, _ _: Int) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified wcsncmp(_: UnsafePointer<wchar_t>!, _: UnsafePointer<wchar_t>!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func wcsncmp(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> Int32 ``` |
| To | ``` func wcsncmp(_ _: UnsafePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!, _ _: Int) -> Int32 ``` |

Modified wcsncpy(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<wchar_t>!, _: Int) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func wcsncpy(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func wcsncpy(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!, _ _: Int) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified wcsnlen(_: UnsafePointer<wchar_t>!, _: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcsnlen(_ _: UnsafePointer<wchar_t>, _ _: Int) -> Int ``` |
| To | ``` func wcsnlen(_ _: UnsafePointer<wchar_t>!, _ _: Int) -> Int ``` |

Modified wcsnrtombs(_: UnsafeMutablePointer<Int8>!, _: UnsafeMutablePointer<UnsafePointer<wchar_t>?>!, _: Int, _: Int, _: UnsafeMutablePointer<mbstate_t>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcsnrtombs(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<UnsafePointer<wchar_t>>, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>) -> Int ``` |
| To | ``` func wcsnrtombs(_ _: UnsafeMutablePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafePointer<wchar_t>?>!, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>!) -> Int ``` |

Modified wcsnrtombs_l(_: UnsafeMutablePointer<Int8>!, _: UnsafeMutablePointer<UnsafePointer<wchar_t>?>!, _: Int, _: Int, _: UnsafeMutablePointer<mbstate_t>!, _: locale_t!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcsnrtombs_l(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<UnsafePointer<wchar_t>>, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>, _ _: locale_t) -> Int ``` |
| To | ``` func wcsnrtombs_l(_ _: UnsafeMutablePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafePointer<wchar_t>?>!, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>!, _ _: locale_t!) -> Int ``` |

Modified wcspbrk(_: UnsafePointer<wchar_t>!, _: UnsafePointer<wchar_t>!) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func wcspbrk(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func wcspbrk(_ _: UnsafePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified wcsrchr(_: UnsafePointer<wchar_t>!, _: wchar_t) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func wcsrchr(_ _: UnsafePointer<wchar_t>, _ _: wchar_t) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func wcsrchr(_ _: UnsafePointer<wchar_t>!, _ _: wchar_t) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified wcsrtombs(_: UnsafeMutablePointer<Int8>!, _: UnsafeMutablePointer<UnsafePointer<wchar_t>?>!, _: Int, _: UnsafeMutablePointer<mbstate_t>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcsrtombs(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<UnsafePointer<wchar_t>>, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>) -> Int ``` |
| To | ``` func wcsrtombs(_ _: UnsafeMutablePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafePointer<wchar_t>?>!, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>!) -> Int ``` |

Modified wcsrtombs_l(_: UnsafeMutablePointer<Int8>!, _: UnsafeMutablePointer<UnsafePointer<wchar_t>?>!, _: Int, _: UnsafeMutablePointer<mbstate_t>!, _: locale_t!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcsrtombs_l(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<UnsafePointer<wchar_t>>, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>, _ _: locale_t) -> Int ``` |
| To | ``` func wcsrtombs_l(_ _: UnsafeMutablePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafePointer<wchar_t>?>!, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>!, _ _: locale_t!) -> Int ``` |

Modified wcsspn(_: UnsafePointer<wchar_t>!, _: UnsafePointer<wchar_t>!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcsspn(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>) -> Int ``` |
| To | ``` func wcsspn(_ _: UnsafePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!) -> Int ``` |

Modified wcsstr(_: UnsafePointer<wchar_t>!, _: UnsafePointer<wchar_t>!) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func wcsstr(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func wcsstr(_ _: UnsafePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified wcstod(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func wcstod(_ _: UnsafePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>) -> Double ``` |
| To | ``` func wcstod(_ _: UnsafePointer<wchar_t>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!) -> Double ``` |

Modified wcstod_l(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _: locale_t!) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func wcstod_l(_ _: UnsafePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, _ _: locale_t) -> Double ``` |
| To | ``` func wcstod_l(_ _: UnsafePointer<wchar_t>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _ _: locale_t!) -> Double ``` |

Modified wcstof(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func wcstof(_ _: UnsafePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>) -> Float ``` |
| To | ``` func wcstof(_ _: UnsafePointer<wchar_t>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!) -> Float ``` |

Modified wcstof_l(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _: locale_t!) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func wcstof_l(_ _: UnsafePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, _ _: locale_t) -> Float ``` |
| To | ``` func wcstof_l(_ _: UnsafePointer<wchar_t>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _ _: locale_t!) -> Float ``` |

Modified wcstoimax(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _: Int32) -> intmax_t

|  | Declaration |
| --- | --- |
| From | ``` func wcstoimax(_ __nptr: UnsafePointer<wchar_t>, _ __endptr: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, _ __base: Int32) -> intmax_t ``` |
| To | ``` func wcstoimax(_ __nptr: UnsafePointer<wchar_t>!, _ __endptr: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _ __base: Int32) -> intmax_t ``` |

Modified wcstoimax_l(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _: Int32, _: locale_t!) -> intmax_t

|  | Declaration |
| --- | --- |
| From | ``` func wcstoimax_l(_ nptr: UnsafePointer<wchar_t>, _ endptr: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, _ base: Int32, _ _: locale_t) -> intmax_t ``` |
| To | ``` func wcstoimax_l(_ nptr: UnsafePointer<wchar_t>!, _ endptr: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _ base: Int32, _ _: locale_t!) -> intmax_t ``` |

Modified wcstok(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func wcstok(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func wcstok(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified wcstol(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _: Int32) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcstol(_ _: UnsafePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, _ _: Int32) -> Int ``` |
| To | ``` func wcstol(_ _: UnsafePointer<wchar_t>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _ _: Int32) -> Int ``` |

Modified wcstol_l(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _: Int32, _: locale_t!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcstol_l(_ _: UnsafePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, _ _: Int32, _ _: locale_t) -> Int ``` |
| To | ``` func wcstol_l(_ _: UnsafePointer<wchar_t>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _ _: Int32, _ _: locale_t!) -> Int ``` |

Modified wcstoll(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _: Int32) -> Int64

|  | Declaration |
| --- | --- |
| From | ``` func wcstoll(_ _: UnsafePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, _ _: Int32) -> Int64 ``` |
| To | ``` func wcstoll(_ _: UnsafePointer<wchar_t>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _ _: Int32) -> Int64 ``` |

Modified wcstoll_l(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _: Int32, _: locale_t!) -> Int64

|  | Declaration |
| --- | --- |
| From | ``` func wcstoll_l(_ _: UnsafePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, _ _: Int32, _ _: locale_t) -> Int64 ``` |
| To | ``` func wcstoll_l(_ _: UnsafePointer<wchar_t>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _ _: Int32, _ _: locale_t!) -> Int64 ``` |

Modified wcstombs(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<wchar_t>!, _: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcstombs(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> Int ``` |
| To | ``` func wcstombs(_ _: UnsafeMutablePointer<Int8>!, _ _: UnsafePointer<wchar_t>!, _ _: Int) -> Int ``` |

Modified wcstombs_l(_: UnsafeMutablePointer<Int8>!, _: UnsafePointer<wchar_t>!, _: Int, _: locale_t!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcstombs_l(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<wchar_t>, _ _: Int, _ _: locale_t) -> Int ``` |
| To | ``` func wcstombs_l(_ _: UnsafeMutablePointer<Int8>!, _ _: UnsafePointer<wchar_t>!, _ _: Int, _ _: locale_t!) -> Int ``` |

Modified wcstoul(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _: Int32) -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func wcstoul(_ _: UnsafePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, _ _: Int32) -> UInt ``` |
| To | ``` func wcstoul(_ _: UnsafePointer<wchar_t>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _ _: Int32) -> UInt ``` |

Modified wcstoul_l(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _: Int32, _: locale_t!) -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func wcstoul_l(_ _: UnsafePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, _ _: Int32, _ _: locale_t) -> UInt ``` |
| To | ``` func wcstoul_l(_ _: UnsafePointer<wchar_t>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _ _: Int32, _ _: locale_t!) -> UInt ``` |

Modified wcstoull(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _: Int32) -> UInt64

|  | Declaration |
| --- | --- |
| From | ``` func wcstoull(_ _: UnsafePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, _ _: Int32) -> UInt64 ``` |
| To | ``` func wcstoull(_ _: UnsafePointer<wchar_t>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _ _: Int32) -> UInt64 ``` |

Modified wcstoull_l(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _: Int32, _: locale_t!) -> UInt64

|  | Declaration |
| --- | --- |
| From | ``` func wcstoull_l(_ _: UnsafePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, _ _: Int32, _ _: locale_t) -> UInt64 ``` |
| To | ``` func wcstoull_l(_ _: UnsafePointer<wchar_t>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _ _: Int32, _ _: locale_t!) -> UInt64 ``` |

Modified wcstoumax(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _: Int32) -> uintmax_t

|  | Declaration |
| --- | --- |
| From | ``` func wcstoumax(_ __nptr: UnsafePointer<wchar_t>, _ __endptr: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, _ __base: Int32) -> uintmax_t ``` |
| To | ``` func wcstoumax(_ __nptr: UnsafePointer<wchar_t>!, _ __endptr: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _ __base: Int32) -> uintmax_t ``` |

Modified wcstoumax_l(_: UnsafePointer<wchar_t>!, _: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _: Int32, _: locale_t!) -> uintmax_t

|  | Declaration |
| --- | --- |
| From | ``` func wcstoumax_l(_ nptr: UnsafePointer<wchar_t>, _ endptr: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, _ base: Int32, _ _: locale_t) -> uintmax_t ``` |
| To | ``` func wcstoumax_l(_ nptr: UnsafePointer<wchar_t>!, _ endptr: UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>?>!, _ base: Int32, _ _: locale_t!) -> uintmax_t ``` |

Modified wcswidth(_: UnsafePointer<wchar_t>!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func wcswidth(_ _: UnsafePointer<wchar_t>, _ _: Int) -> Int32 ``` |
| To | ``` func wcswidth(_ _: UnsafePointer<wchar_t>!, _ _: Int) -> Int32 ``` |

Modified wcswidth_l(_: UnsafePointer<wchar_t>!, _: Int, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func wcswidth_l(_ _: UnsafePointer<wchar_t>, _ _: Int, _ _: locale_t) -> Int32 ``` |
| To | ``` func wcswidth_l(_ _: UnsafePointer<wchar_t>!, _ _: Int, _ _: locale_t!) -> Int32 ``` |

Modified wcsxfrm(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<wchar_t>!, _: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcsxfrm(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> Int ``` |
| To | ``` func wcsxfrm(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!, _ _: Int) -> Int ``` |

Modified wcsxfrm_l(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<wchar_t>!, _: Int, _: locale_t!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcsxfrm_l(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int, _ _: locale_t) -> Int ``` |
| To | ``` func wcsxfrm_l(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!, _ _: Int, _ _: locale_t!) -> Int ``` |

Modified wctob_l(_: wint_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func wctob_l(_ _: wint_t, _ _: locale_t) -> Int32 ``` |
| To | ``` func wctob_l(_ _: wint_t, _ _: locale_t!) -> Int32 ``` |

Modified wctomb(_: UnsafeMutablePointer<Int8>!, _: wchar_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func wctomb(_ _: UnsafeMutablePointer<Int8>, _ _: wchar_t) -> Int32 ``` |
| To | ``` func wctomb(_ _: UnsafeMutablePointer<Int8>!, _ _: wchar_t) -> Int32 ``` |

Modified wctomb_l(_: UnsafeMutablePointer<Int8>!, _: wchar_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func wctomb_l(_ _: UnsafeMutablePointer<Int8>, _ _: wchar_t, _ _: locale_t) -> Int32 ``` |
| To | ``` func wctomb_l(_ _: UnsafeMutablePointer<Int8>!, _ _: wchar_t, _ _: locale_t!) -> Int32 ``` |

Modified wctrans(_: UnsafePointer<Int8>!) -> wctrans_t

|  | Declaration |
| --- | --- |
| From | ``` func wctrans(_ _: UnsafePointer<Int8>) -> wctrans_t ``` |
| To | ``` func wctrans(_ _: UnsafePointer<Int8>!) -> wctrans_t ``` |

Modified wctrans_l(_: UnsafePointer<Int8>!, _: locale_t!) -> wctrans_t

|  | Declaration |
| --- | --- |
| From | ``` func wctrans_l(_ _: UnsafePointer<Int8>, _ _: locale_t) -> wctrans_t ``` |
| To | ``` func wctrans_l(_ _: UnsafePointer<Int8>!, _ _: locale_t!) -> wctrans_t ``` |

Modified wctype(_: UnsafePointer<Int8>!) -> wctype_t

|  | Declaration |
| --- | --- |
| From | ``` func wctype(_ _: UnsafePointer<Int8>) -> wctype_t ``` |
| To | ``` func wctype(_ _: UnsafePointer<Int8>!) -> wctype_t ``` |

Modified wctype_l(_: UnsafePointer<Int8>!, _: locale_t!) -> wctype_t

|  | Declaration |
| --- | --- |
| From | ``` func wctype_l(_ _: UnsafePointer<Int8>, _ _: locale_t) -> wctype_t ``` |
| To | ``` func wctype_l(_ _: UnsafePointer<Int8>!, _ _: locale_t!) -> wctype_t ``` |

Modified wcwidth_l(_: wchar_t, _: locale_t!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func wcwidth_l(_ _: wchar_t, _ _: locale_t) -> Int32 ``` |
| To | ``` func wcwidth_l(_ _: wchar_t, _ _: locale_t!) -> Int32 ``` |

Modified wmemchr(_: UnsafePointer<wchar_t>!, _: wchar_t, _: Int) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func wmemchr(_ _: UnsafePointer<wchar_t>, _ _: wchar_t, _ _: Int) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func wmemchr(_ _: UnsafePointer<wchar_t>!, _ _: wchar_t, _ _: Int) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified wmemcmp(_: UnsafePointer<wchar_t>!, _: UnsafePointer<wchar_t>!, _: Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func wmemcmp(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> Int32 ``` |
| To | ``` func wmemcmp(_ _: UnsafePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!, _ _: Int) -> Int32 ``` |

Modified wmemcpy(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<wchar_t>!, _: Int) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func wmemcpy(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func wmemcpy(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!, _ _: Int) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified wmemmove(_: UnsafeMutablePointer<wchar_t>!, _: UnsafePointer<wchar_t>!, _: Int) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func wmemmove(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func wmemmove(_ _: UnsafeMutablePointer<wchar_t>!, _ _: UnsafePointer<wchar_t>!, _ _: Int) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified wmemset(_: UnsafeMutablePointer<wchar_t>!, _: wchar_t, _: Int) -> UnsafeMutablePointer<wchar_t>!

|  | Declaration |
| --- | --- |
| From | ``` func wmemset(_ _: UnsafeMutablePointer<wchar_t>, _ _: wchar_t, _ _: Int) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func wmemset(_ _: UnsafeMutablePointer<wchar_t>!, _ _: wchar_t, _ _: Int) -> UnsafeMutablePointer<wchar_t>! ``` |

Modified write(_: Int32, _: UnsafeRawPointer!, _: Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func write(_ _: Int32, _ _: UnsafePointer<Void>, _ _: Int) -> Int ``` |
| To | ``` func write(_ __fd: Int32, _ __buf: UnsafeRawPointer!, _ __nbyte: Int) -> Int ``` |

Modified writev(_: Int32, _: UnsafePointer<iovec>!, _: Int32) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func writev(_ _: Int32, _ _: UnsafePointer<iovec>, _ _: Int32) -> Int ``` |
| To | ``` func writev(_ _: Int32, _ _: UnsafePointer<iovec>!, _ _: Int32) -> Int ``` |

Modified wtmpxname(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func wtmpxname(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func wtmpxname(_ _: UnsafePointer<Int8>!) -> Int32 ``` |

Modified xattr_flags_from_name(_: UnsafePointer<Int8>!) -> xattr_flags_t

|  | Declaration |
| --- | --- |
| From | ``` func xattr_flags_from_name(_ _: UnsafePointer<Int8>) -> xattr_flags_t ``` |
| To | ``` func xattr_flags_from_name(_ _: UnsafePointer<Int8>!) -> xattr_flags_t ``` |

Modified xattr_name_with_flags(_: UnsafePointer<Int8>!, _: xattr_flags_t) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func xattr_name_with_flags(_ _: UnsafePointer<Int8>, _ _: xattr_flags_t) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func xattr_name_with_flags(_ _: UnsafePointer<Int8>!, _ _: xattr_flags_t) -> UnsafeMutablePointer<Int8>! ``` |

Modified xattr_name_without_flags(_: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func xattr_name_without_flags(_ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func xattr_name_without_flags(_ _: UnsafePointer<Int8>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified xattr_preserve_for_intent(_: UnsafePointer<Int8>!, _: xattr_operation_intent_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func xattr_preserve_for_intent(_ _: UnsafePointer<Int8>, _ _: xattr_operation_intent_t) -> Int32 ``` |
| To | ``` func xattr_preserve_for_intent(_ _: UnsafePointer<Int8>!, _ _: xattr_operation_intent_t) -> Int32 ``` |

Modified yn(_: Int, _: Double) -> Double

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func yn(_ n: Int, _ x: Double) -> Double ``` |
| To | ``` func yn(_ n: Int, _ x: Double) -> Double ``` |

Modified zopen(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int32) -> UnsafeMutablePointer<FILE>!

|  | Declaration |
| --- | --- |
| From | ``` func zopen(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int32) -> UnsafeMutablePointer<FILE> ``` |
| To | ``` func zopen(_ _: UnsafePointer<Int8>!, _ _: UnsafePointer<Int8>!, _ _: Int32) -> UnsafeMutablePointer<FILE>! ``` |

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
