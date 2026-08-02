---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/Darwin.html
archived_at: '2026-07-18T02:56:23.574606Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# Darwin Changes

## Darwin

Removed FixedPoint [struct]Removed FixedPoint.xRemoved FixedPoint.yRemoved FixedRect [struct]Removed FixedRect.bottomRemoved FixedRect.leftRemoved FixedRect.rightRemoved FixedRect.topRemoved Float32Point [struct]Removed Float32Point.xRemoved Float32Point.yRemoved Float80 [struct]Removed Float80.expRemoved Float80.manRemoved Float96 [struct]Removed Float96.expRemoved Float96.manRemoved NumVersion [struct]Removed NumVersion.majorRevRemoved NumVersion.minorAndBugRevRemoved NumVersion.nonRelRevRemoved NumVersion.stageRemoved Point [struct]Removed Point.hRemoved Point.vRemoved Rect [struct]Removed Rect.bottomRemoved Rect.leftRemoved Rect.rightRemoved Rect.topRemoved TimeRecord [struct]Removed TimeRecord.baseRemoved TimeRecord.scaleRemoved TimeRecord.valueRemoved UnsignedWide [struct]Removed UnsignedWide.hiRemoved UnsignedWide.loRemoved VersRec [struct]Removed VersRec.countryCodeRemoved VersRec.numericVersionRemoved VersRec.reservedRemoved VersRec.shortVersionRemoved wide [struct]Removed wide.hiRemoved wide.loRemoved ALLOW_OBSOLETE_CARBON_MACMEMORYRemoved ALLOW_OBSOLETE_CARBON_OSUTILSRemoved AbsoluteTimeRemoved ByteRemoved ByteCountRemoved ByteOffsetRemoved BytePtrRemoved CHAR_MINRemoved CharParameterRemoved CompTimeValueRemoved ConstLogicalAddressRemoved ConstStr15ParamRemoved ConstStr255ParamRemoved ConstStr27ParamRemoved ConstStr31ParamRemoved ConstStr32ParamRemoved ConstStr63ParamRemoved ConstStrFileNameParamRemoved ConstStringPtrRemoved DurationRemoved FixedRemoved FixedPtrRemoved FractRemoved FractPtrRemoved HandleRemoved ItemCountRemoved LangCodeRemoved LogicalAddressRemoved NumVersionVariantHandleRemoved NumVersionVariantPtrRemoved OSTypePtrRemoved PBVersionRemoved PRefConRemoved PhysicalAddressRemoved PointPtrRemoved ProcHandleRemoved ProcPtrRemoved ProcessSerialNumberPtrRemoved PtrRemoved RectPtrRemoved RegionCodeRemoved Register68kProcPtrRemoved ResTypeRemoved ResTypePtrRemoved SCHAR_MINRemoved SHRT_MINRemoved SIZE_T_MAXRemoved SRefConRemoved ScriptCodeRemoved ShortFixedRemoved ShortFixedPtrRemoved SignedByteRemoved SizeRemoved Str15Removed Str255Removed Str27Removed Str31Removed Str32Removed Str32FieldRemoved Str63Removed StrFileNameRemoved StringHandleRemoved StringPtrRemoved StyleRemoved StyleFieldRemoved StyleParameterRemoved TimeBaseRemoved TimeScaleRemoved TimeValueRemoved TimeValue64Removed UCHAR_MAXRemoved UINT_MAXRemoved ULLONG_MAXRemoved ULONG_MAXRemoved UQUAD_MAXRemoved URefConRemoved USHRT_MAXRemoved UniCharCountRemoved UniCharCountPtrRemoved UniCharPtrRemoved UnicodeScalarValueRemoved UniversalProcHandleRemoved UniversalProcPtrRemoved UnsignedFixedRemoved UnsignedFixedPtrRemoved UnsignedWidePtrRemoved VHSelectRemoved VersRecHndlRemoved VersRecPtrRemoved WidePtrRemoved alphaStageRemoved betaStageRemoved boldRemoved condenseRemoved developStageRemoved extendRemoved extended80Removed extended96Removed finalStageRemoved italicRemoved kInvalidIDRemoved kNilOptionsRemoved memcmp(UnsafePointer<Void>, UnsafePointer<Void>, UInt) -> Int32Removed normalRemoved outlineRemoved shadowRemoved sqrt(Double) -> DoubleRemoved underlineAdded DBM.init()Added DBM.init(__opaque: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added DIR.init()Added DIR.init(__dd_fd: Int32, __dd_loc: Int, __dd_size: Int, __dd_buf: UnsafeMutablePointer<Int8>, __dd_len: Int32, __dd_seek: Int, __dd_rewind: Int, __dd_flags: Int32, __dd_lock: __darwin_pthread_mutex_t, __dd_td: COpaquePointer)Added FTW.init()Added FTW.init(base: Int32, level: Int32)Added NDR_record_t.init()Added NDR_record_t.init(mig_vers: UInt8, if_vers: UInt8, reserved1: UInt8, mig_encoding: UInt8, int_rep: UInt8, char_rep: UInt8, float_rep: UInt8, reserved2: UInt8)Added ProcessSerialNumber.init()Added ProcessSerialNumber.init(highLongOfPSN: UInt32, lowLongOfPSN: UInt32)Added accessx_descriptor.init()Added accessx_descriptor.init(ad_name_offset: UInt32, ad_flags: Int32, ad_pad:(Int32, Int32))Added addrinfo.init()Added addrinfo.init(ai_flags: Int32, ai_family: Int32, ai_socktype: Int32, ai_protocol: Int32, ai_addrlen: socklen_t, ai_canonname: UnsafeMutablePointer<Int8>, ai_addr: UnsafeMutablePointer<sockaddr>, ai_next: UnsafeMutablePointer<addrinfo>)Added aiocb.init()Added aiocb.init(aio_fildes: Int32, aio_offset: off_t, aio_buf: UnsafeMutablePointer<Void>, aio_nbytes: Int, aio_reqprio: Int32, aio_sigevent: sigevent, aio_lio_opcode: Int32)Added arm_state_hdr.init()Added arm_state_hdr.init(flavor: UInt32, count: UInt32)Added arm_unified_thread_state.init()Added attribute_set.init()Added attribute_set.init(commonattr: attrgroup_t, volattr: attrgroup_t, dirattr: attrgroup_t, fileattr: attrgroup_t, forkattr: attrgroup_t)Added attrlist.init()Added attrlist.init(bitmapcount: u_short, reserved: UInt16, commonattr: attrgroup_t, volattr: attrgroup_t, dirattr: attrgroup_t, fileattr: attrgroup_t, forkattr: attrgroup_t)Added attrreference.init()Added attrreference.init(attr_dataoffset: Int32, attr_length: UInt32)Added au_evclass_map.init()Added au_evclass_map.init(ec_number: au_event_t, ec_class: au_class_t)Added au_mask.init()Added au_mask.init(am_success: UInt32, am_failure: UInt32)Added au_qctrl.init()Added au_qctrl.init(aq_hiwater: Int32, aq_lowater: Int32, aq_bufsz: Int32, aq_delay: Int32, aq_minfree: Int32)Added au_session.init()Added au_session.init(as_aia_p: UnsafeMutablePointer<auditinfo_addr_t>, as_mask: au_mask_t)Added au_tid.init()Added au_tid.init(port: dev_t, machine: UInt32)Added au_tid_addr.init()Added au_tid_addr.init(at_port: dev_t, at_type: UInt32, at_addr:(UInt32, UInt32, UInt32, UInt32))Added audit_fstat.init()Added audit_fstat.init(af_filesz: UInt64, af_currsz: UInt64)Added audit_stat.init()Added audit_stat.init(as_version: UInt32, as_numevent: UInt32, as_generated: Int32, as_nonattrib: Int32, as_kernel: Int32, as_audit: Int32, as_auditctl: Int32, as_enqueue: Int32, as_written: Int32, as_wblocked: Int32, as_rblocked: Int32, as_dropped: Int32, as_totalsize: Int32, as_memused: UInt32)Added audit_token_t.init()Added audit_token_t.init(val: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32))Added auditinfo.init()Added auditinfo.init(ai_auid: au_id_t, ai_mask: au_mask_t, ai_termid: au_tid_t, ai_asid: au_asid_t)Added auditinfo_addr.init()Added auditinfo_addr.init(ai_auid: au_id_t, ai_mask: au_mask_t, ai_termid: au_tid_addr_t, ai_asid: au_asid_t, ai_flags: au_asflgs_t)Added auditpinfo.init()Added auditpinfo.init(ap_pid: pid_t, ap_auid: au_id_t, ap_mask: au_mask_t, ap_termid: au_tid_t, ap_asid: au_asid_t)Added auditpinfo_addr.init()Added auditpinfo_addr.init(ap_pid: pid_t, ap_auid: au_id_t, ap_mask: au_mask_t, ap_termid: au_tid_addr_t, ap_asid: au_asid_t, ap_flags: au_asflgs_t)Added clockinfo.init()Added clockinfo.init(hz: Int32, tick: Int32, tickadj: Int32, stathz: Int32, profhz: Int32)Added cmsghdr.init()Added cmsghdr.init(cmsg_len: socklen_t, cmsg_level: Int32, cmsg_type: Int32)Added ctlname.init()Added ctlname.init(ctl_name: UnsafeMutablePointer<Int8>, ctl_type: Int32)Added datum.init()Added datum.init(dptr: UnsafeMutablePointer<Void>, dsize: Int)Added dirent.init()Added diskextent.init()Added diskextent.init(startblock: UInt32, blockcount: UInt32)Added div_t.init()Added div_t.init(quot: Int32, rem: Int32)Added dl_info.init()Added dl_info.init(dli_fname: UnsafePointer<Int8>, dli_fbase: UnsafeMutablePointer<Void>, dli_sname: UnsafePointer<Int8>, dli_saddr: UnsafeMutablePointer<Void>)Added dqblk.init()Added dqblk.init(dqb_bhardlimit: UInt64, dqb_bsoftlimit: UInt64, dqb_curbytes: UInt64, dqb_ihardlimit: UInt32, dqb_isoftlimit: UInt32, dqb_curinodes: UInt32, dqb_btime: UInt32, dqb_itime: UInt32, dqb_id: UInt32, dqb_spare:(UInt32, UInt32, UInt32, UInt32))Added dqfilehdr.init()Added dqfilehdr.init(dqh_magic: UInt32, dqh_version: UInt32, dqh_maxentries: UInt32, dqh_entrycnt: UInt32, dqh_flags: UInt32, dqh_chktime: UInt32, dqh_btime: UInt32, dqh_itime: UInt32, dqh_string:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), dqh_spare:(UInt32, UInt32, UInt32, UInt32))Added entry.init()Added entry.init(key: UnsafeMutablePointer<Int8>, data: UnsafeMutablePointer<Void>)Added exception.init()Added exception.init(type: Int32, name: UnsafeMutablePointer<Int8>, arg1: Double, arg2: Double, retval: Double)Added extern_proc.init()Added fbootstraptransfer.init()Added fbootstraptransfer.init(fbt_offset: off_t, fbt_length: Int, fbt_buffer: UnsafeMutablePointer<Void>)Added fcodeblobs.init()Added fcodeblobs.init(f_cd_hash: UnsafeMutablePointer<Void>, f_hash_size: Int, f_cd_buffer: UnsafeMutablePointer<Void>, f_cd_size: Int, f_out_size: UnsafeMutablePointer<UInt32>, f_arch: Int32, __padding: Int32)Added fd_set.init()Added fd_set.init(fds_bits: (__int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t))Added fenv_t.init()Added fenv_t.init(__fpscr: UInt32, __reserved0: UInt32, __reserved1: UInt32, __reserved2: UInt32)Added fhandle.init()Added fhandle.init(fh_len: Int32, fh_data:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added flock.init()Added flock.init(l_start: off_t, l_len: off_t, l_pid: pid_t, l_type: Int16, l_whence: Int16)Added flocktimeout.init()Added flocktimeout.init(fl: flock, timeout: timespec)Added fsid.init()Added fsid.init(val: (Int32, Int32))Added fsignatures.init()Added fsignatures.init(fs_file_start: off_t, fs_blob_start: UnsafeMutablePointer<Void>, fs_blob_size: Int)Added fsobj_id.init()Added fsobj_id.init(fid_objno: UInt32, fid_generation: UInt32)Added fssearchblock.init()Added fssearchblock.init(returnattrs: UnsafeMutablePointer<attrlist>, returnbuffer: UnsafeMutablePointer<Void>, returnbuffersize: Int, maxmatches: u_long, timelimit: timeval, searchparams1: UnsafeMutablePointer<Void>, sizeofsearchparams1: Int, searchparams2: UnsafeMutablePointer<Void>, sizeofsearchparams2: Int, searchattrs: attrlist)Added fstore.init()Added fstore.init(fst_flags: UInt32, fst_posmode: Int32, fst_offset: off_t, fst_length: off_t, fst_bytesalloc: off_t)Added glob_t.init()Added gpu_energy_data.init()Added gpu_energy_data.init(task_gpu_utilisation: UInt64, task_gpu_stat_reserved0: UInt64, task_gpu_stat_reserved1: UInt64, task_gpu_stat_reserved2: UInt64)Added group.init()Added group.init(gr_name: UnsafeMutablePointer<Int8>, gr_passwd: UnsafeMutablePointer<Int8>, gr_gid: gid_t, gr_mem: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>)Added group_req.init()Added group_req.init(gr_interface: UInt32, gr_group: sockaddr_storage)Added group_source_req.init()Added group_source_req.init(gsr_interface: UInt32, gsr_group: sockaddr_storage, gsr_source: sockaddr_storage)Added guid_t.init()Added guid_t.init(g_guid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added hash_info_bucket.init()Added hash_info_bucket.init(hib_count: natural_t)Added host_basic_info.init()Added host_basic_info.init(max_cpus: integer_t, avail_cpus: integer_t, memory_size: natural_t, cpu_type: cpu_type_t, cpu_subtype: cpu_subtype_t, cpu_threadtype: cpu_threadtype_t, physical_cpu: integer_t, physical_cpu_max: integer_t, logical_cpu: integer_t, logical_cpu_max: integer_t, max_mem: UInt64)Added host_cpu_load_info.init()Added host_cpu_load_info.init(cpu_ticks: (natural_t, natural_t, natural_t, natural_t))Added host_load_info.init()Added host_load_info.init(avenrun: (integer_t, integer_t, integer_t), mach_factor:(integer_t, integer_t, integer_t))Added host_priority_info.init()Added host_priority_info.init(kernel_priority: integer_t, system_priority: integer_t, server_priority: integer_t, user_priority: integer_t, depress_priority: integer_t, idle_priority: integer_t, minimum_priority: integer_t, maximum_priority: integer_t)Added host_sched_info.init()Added host_sched_info.init(min_timeout: integer_t, min_quantum: integer_t)Added hostent.init()Added hostent.init(h_name: UnsafeMutablePointer<Int8>, h_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, h_addrtype: Int32, h_length: Int32, h_addr_list: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>)Added iconv_fallbacks.init()Added iconv_fallbacks.init(mb_to_uc_fallback: iconv_unicode_mb_to_uc_fallback, uc_to_mb_fallback: iconv_unicode_uc_to_mb_fallback, mb_to_wc_fallback: iconv_wchar_mb_to_wc_fallback, wc_to_mb_fallback: iconv_wchar_wc_to_mb_fallback, data: UnsafeMutablePointer<Void>)Added iconv_hooks.init()Added iconv_hooks.init(uc_hook: iconv_unicode_char_hook, wc_hook: iconv_wide_char_hook, data: UnsafeMutablePointer<Void>)Added if_clonereq.init()Added if_clonereq.init(ifcr_total: Int32, ifcr_count: Int32, ifcr_buffer: UnsafeMutablePointer<Int8>)Added if_data.init()Added if_data.init(ifi_type: u_char, ifi_typelen: u_char, ifi_physical: u_char, ifi_addrlen: u_char, ifi_hdrlen: u_char, ifi_recvquota: u_char, ifi_xmitquota: u_char, ifi_unused1: u_char, ifi_mtu: UInt32, ifi_metric: UInt32, ifi_baudrate: UInt32, ifi_ipackets: UInt32, ifi_ierrors: UInt32, ifi_opackets: UInt32, ifi_oerrors: UInt32, ifi_collisions: UInt32, ifi_ibytes: UInt32, ifi_obytes: UInt32, ifi_imcasts: UInt32, ifi_omcasts: UInt32, ifi_iqdrops: UInt32, ifi_noproto: UInt32, ifi_recvtiming: UInt32, ifi_xmittiming: UInt32, ifi_lastchange: timeval, ifi_unused2: UInt32, ifi_hwassist: UInt32, ifi_reserved1: UInt32, ifi_reserved2: UInt32)Added if_data64.init()Added if_data64.init(ifi_type: u_char, ifi_typelen: u_char, ifi_physical: u_char, ifi_addrlen: u_char, ifi_hdrlen: u_char, ifi_recvquota: u_char, ifi_xmitquota: u_char, ifi_unused1: u_char, ifi_mtu: UInt32, ifi_metric: UInt32, ifi_baudrate: UInt64, ifi_ipackets: UInt64, ifi_ierrors: UInt64, ifi_opackets: UInt64, ifi_oerrors: UInt64, ifi_collisions: UInt64, ifi_ibytes: UInt64, ifi_obytes: UInt64, ifi_imcasts: UInt64, ifi_omcasts: UInt64, ifi_iqdrops: UInt64, ifi_noproto: UInt64, ifi_recvtiming: UInt32, ifi_xmittiming: UInt32, ifi_lastchange: timeval)Added if_msghdr.init()Added if_msghdr.init(ifm_msglen: UInt16, ifm_version: UInt8, ifm_type: UInt8, ifm_addrs: Int32, ifm_flags: Int32, ifm_index: UInt16, ifm_data: if_data)Added if_msghdr2.init()Added if_msghdr2.init(ifm_msglen: u_short, ifm_version: u_char, ifm_type: u_char, ifm_addrs: Int32, ifm_flags: Int32, ifm_index: u_short, ifm_snd_len: Int32, ifm_snd_maxlen: Int32, ifm_snd_drops: Int32, ifm_timer: Int32, ifm_data: if_data64)Added if_nameindex.init()Added if_nameindex.init(if_index: UInt32, if_name: UnsafeMutablePointer<Int8>)Added ifa_msghdr.init()Added ifa_msghdr.init(ifam_msglen: UInt16, ifam_version: UInt8, ifam_type: UInt8, ifam_addrs: Int32, ifam_flags: Int32, ifam_index: UInt16, ifam_metric: Int32)Added ifaliasreq.init()Added ifaliasreq.init(ifra_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifra_addr: sockaddr, ifra_broadaddr: sockaddr, ifra_mask: sockaddr)Added ifconf.init()Added ifdevmtu.init()Added ifdevmtu.init(ifdm_current: Int32, ifdm_min: Int32, ifdm_max: Int32)Added ifdrv.init()Added ifdrv.init(ifd_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifd_cmd: UInt, ifd_len: Int, ifd_data: UnsafeMutablePointer<Void>)Added ifkpi.init()Added ifma_msghdr.init()Added ifma_msghdr.init(ifmam_msglen: UInt16, ifmam_version: UInt8, ifmam_type: UInt8, ifmam_addrs: Int32, ifmam_flags: Int32, ifmam_index: UInt16)Added ifma_msghdr2.init()Added ifma_msghdr2.init(ifmam_msglen: u_short, ifmam_version: u_char, ifmam_type: u_char, ifmam_addrs: Int32, ifmam_flags: Int32, ifmam_index: u_short, ifmam_refcount: Int32)Added ifmediareq.init()Added ifmediareq.init(ifm_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifm_current: Int32, ifm_mask: Int32, ifm_status: Int32, ifm_active: Int32, ifm_count: Int32, ifm_ulist: UnsafeMutablePointer<Int32>)Added ifqueue.init()Added ifqueue.init(ifq_head: UnsafeMutablePointer<Void>, ifq_tail: UnsafeMutablePointer<Void>, ifq_len: Int32, ifq_maxlen: Int32, ifq_drops: Int32)Added ifreq.init()Added ifstat.init()Added imaxdiv_t.init()Added imaxdiv_t.init(quot: intmax_t, rem: intmax_t)Added in6_addr.init()Added in6_pktinfo.init()Added in6_pktinfo.init(ipi6_addr: in6_addr, ipi6_ifindex: UInt32)Added in_addr.init()Added in_addr.init(s_addr: in_addr_t)Added in_pktinfo.init()Added in_pktinfo.init(ipi_ifindex: UInt32, ipi_spec_dst: in_addr, ipi_addr: in_addr)Added io_stat_entry.init()Added io_stat_entry.init(count: UInt64, size: UInt64)Added io_stat_info.init()Added io_stat_info.init(disk_reads: io_stat_entry, io_priority:(io_stat_entry, io_stat_entry, io_stat_entry, io_stat_entry), paging: io_stat_entry, metadata: io_stat_entry, total_io: io_stat_entry)Added iovec.init()Added iovec.init(iov_base: UnsafeMutablePointer<Void>, iov_len: Int)Added ip6_mtuinfo.init()Added ip6_mtuinfo.init(ip6m_addr: sockaddr_in6, ip6m_mtu: UInt32)Added ip_mreq.init()Added ip_mreq.init(imr_multiaddr: in_addr, imr_interface: in_addr)Added ip_mreq_source.init()Added ip_mreq_source.init(imr_multiaddr: in_addr, imr_sourceaddr: in_addr, imr_interface: in_addr)Added ip_mreqn.init()Added ip_mreqn.init(imr_multiaddr: in_addr, imr_address: in_addr, imr_ifindex: Int32)Added ip_opts.init()Added ip_opts.init(ip_dst: in_addr, ip_opts:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added ipc_info_name.init()Added ipc_info_name.init(iin_name: mach_port_name_t, iin_collision: integer_t, iin_type: mach_port_type_t, iin_urefs: mach_port_urefs_t, iin_object: natural_t, iin_next: natural_t, iin_hash: natural_t)Added ipc_info_space.init()Added ipc_info_space.init(iis_genno_mask: natural_t, iis_table_size: natural_t, iis_table_next: natural_t, iis_tree_size: natural_t, iis_tree_small: natural_t, iis_tree_hash: natural_t)Added ipc_info_space_basic.init()Added ipc_info_space_basic.init(iisb_genno_mask: natural_t, iisb_table_size: natural_t, iisb_table_next: natural_t, iisb_table_inuse: natural_t, iisb_reserved:(natural_t, natural_t))Added ipc_info_tree_name.init()Added ipc_info_tree_name.init(iitn_name: ipc_info_name_t, iitn_lchild: mach_port_name_t, iitn_rchild: mach_port_name_t)Added ipc_perm.init()Added ipc_perm.init(uid: uid_t, gid: gid_t, cuid: uid_t, cgid: gid_t, mode: mode_t, _seq: UInt16, _key: key_t)Added ipv6_mreq.init()Added ipv6_mreq.init(ipv6mr_multiaddr: in6_addr, ipv6mr_interface: UInt32)Added itimerval.init()Added itimerval.init(it_interval: timeval, it_value: timeval)Added kauth_ace.init()Added kauth_ace.init(ace_applicable: guid_t, ace_flags: UInt32, ace_rights: kauth_ace_rights_t)Added kauth_acl.init()Added kauth_acl.init(acl_entrycount: UInt32, acl_flags: UInt32, acl_ace:(kauth_ace))Added kauth_cache_sizes.init()Added kauth_cache_sizes.init(kcs_group_size: UInt32, kcs_id_size: UInt32)Added kauth_filesec.init()Added kauth_filesec.init(fsec_magic: UInt32, fsec_owner: guid_t, fsec_group: guid_t, fsec_acl: kauth_acl)Added kauth_identity_extlookup.init()Added kauth_identity_extlookup.init(el_seqno: UInt32, el_result: UInt32, el_flags: UInt32, el_info_pid: __darwin_pid_t, el_extend: UInt64, el_info_reserved_1: UInt32, el_uid: uid_t, el_uguid: guid_t, el_uguid_valid: UInt32, el_usid: ntsid_t, el_usid_valid: UInt32, el_gid: gid_t, el_gguid: guid_t, el_gguid_valid: UInt32, el_gsid: ntsid_t, el_gsid_valid: UInt32, el_member_valid: UInt32, el_sup_grp_cnt: UInt32, el_sup_groups:(gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t))Added kernel_resource_sizes.init()Added kernel_resource_sizes.init(task: natural_t, thread: natural_t, port: natural_t, memory_region: natural_t, memory_object: natural_t)Added kev_dl_proto_data.init()Added kev_dl_proto_data.init(link_data: net_event_data, proto_family: UInt32, proto_remaining_count: UInt32)Added kevent.init()Added kevent.init(ident: UInt, filter: Int16, flags: UInt16, fflags: UInt32, data: Int, udata: UnsafeMutablePointer<Void>)Added kevent64_s.init()Added kevent64_s.init(ident: UInt64, filter: Int16, flags: UInt16, fflags: UInt32, data: Int64, udata: UInt64, ext:(UInt64, UInt64))Added kinfo_lctx.init()Added kinfo_lctx.init(id: pid_t, mc: Int32)Added kinfo_proc.init()Added kinfo_proc.init(kp_proc: extern_proc, kp_eproc: eproc)Added klist.init()Added klist.init(slh_first: COpaquePointer)Added kmod_info.init()Added kmod_info.init(next: UnsafeMutablePointer<kmod_info>, info_version: Int32, id: UInt32, name:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), version:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), reference_count: Int32, reference_list: UnsafeMutablePointer<kmod_reference_t>, address: vm_address_t, size: vm_size_t, hdr_size: vm_size_t, start: CFunctionPointer<kmod_start_func_t>, stop: CFunctionPointer<kmod_stop_func_t>)Added kmod_info_32_v1.init()Added kmod_info_32_v1.init(next_addr: UInt32, info_version: Int32, id: UInt32, name:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), version:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), reference_count: Int32, reference_list_addr: UInt32, address: UInt32, size: UInt32, hdr_size: UInt32, start_addr: UInt32, stop_addr: UInt32)Added kmod_info_64_v1.init()Added kmod_info_64_v1.init(next_addr: UInt64, info_version: Int32, id: UInt32, name:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), version:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), reference_count: Int32, reference_list_addr: UInt64, address: UInt64, size: UInt64, hdr_size: UInt64, start_addr: UInt64, stop_addr: UInt64)Added kmod_reference.init()Added kmod_reference.init(next: UnsafeMutablePointer<kmod_reference>, info: UnsafeMutablePointer<kmod_info>)Added lastlogx.init()Added lastlogx.init(ll_tv: timeval, ll_line:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ll_host:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added lconv.init()Added lconv.init(decimal_point: UnsafeMutablePointer<Int8>, thousands_sep: UnsafeMutablePointer<Int8>, grouping: UnsafeMutablePointer<Int8>, int_curr_symbol: UnsafeMutablePointer<Int8>, currency_symbol: UnsafeMutablePointer<Int8>, mon_decimal_point: UnsafeMutablePointer<Int8>, mon_thousands_sep: UnsafeMutablePointer<Int8>, mon_grouping: UnsafeMutablePointer<Int8>, positive_sign: UnsafeMutablePointer<Int8>, negative_sign: UnsafeMutablePointer<Int8>, int_frac_digits: Int8, frac_digits: Int8, p_cs_precedes: Int8, p_sep_by_space: Int8, n_cs_precedes: Int8, n_sep_by_space: Int8, p_sign_posn: Int8, n_sign_posn: Int8, int_p_cs_precedes: Int8, int_n_cs_precedes: Int8, int_p_sep_by_space: Int8, int_n_sep_by_space: Int8, int_p_sign_posn: Int8, int_n_sign_posn: Int8)Added ldiv_t.init()Added ldiv_t.init(quot: Int, rem: Int)Added linger.init()Added linger.init(l_onoff: Int32, l_linger: Int32)Added lldiv_t.init()Added lldiv_t.init(quot: Int64, rem: Int64)Added loadavg.init()Added loadavg.init(ldavg: (fixpt_t, fixpt_t, fixpt_t), fscale: Int)Added lockgroup_info.init()Added lockgroup_info.init(lockgroup_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), lockgroup_attr: UInt64, lock_spin_cnt: UInt64, lock_spin_util_cnt: UInt64, lock_spin_held_cnt: UInt64, lock_spin_miss_cnt: UInt64, lock_spin_held_max: UInt64, lock_spin_held_cum: UInt64, lock_mtx_cnt: UInt64, lock_mtx_util_cnt: UInt64, lock_mtx_held_cnt: UInt64, lock_mtx_miss_cnt: UInt64, lock_mtx_wait_cnt: UInt64, lock_mtx_held_max: UInt64, lock_mtx_held_cum: UInt64, lock_mtx_wait_max: UInt64, lock_mtx_wait_cum: UInt64, lock_rw_cnt: UInt64, lock_rw_util_cnt: UInt64, lock_rw_held_cnt: UInt64, lock_rw_miss_cnt: UInt64, lock_rw_wait_cnt: UInt64, lock_rw_held_max: UInt64, lock_rw_held_cum: UInt64, lock_rw_wait_max: UInt64, lock_rw_wait_cum: UInt64)Added log2phys.init()Added log2phys.init(l2p_flags: UInt32, l2p_contigbytes: off_t, l2p_devoffset: off_t)Added mach_dead_name_notification_t.init()Added mach_dead_name_notification_t.init(not_header: mach_msg_header_t, NDR: NDR_record_t, not_port: mach_port_name_t, trailer: mach_msg_format_0_trailer_t)Added mach_msg_audit_trailer_t.init()Added mach_msg_audit_trailer_t.init(msgh_trailer_type: mach_msg_trailer_type_t, msgh_trailer_size: mach_msg_trailer_size_t, msgh_seqno: mach_port_seqno_t, msgh_sender: security_token_t, msgh_audit: audit_token_t)Added mach_msg_base_t.init()Added mach_msg_base_t.init(header: mach_msg_header_t, body: mach_msg_body_t)Added mach_msg_body_t.init()Added mach_msg_body_t.init(msgh_descriptor_count: mach_msg_size_t)Added mach_msg_context_trailer_t.init()Added mach_msg_context_trailer_t.init(msgh_trailer_type: mach_msg_trailer_type_t, msgh_trailer_size: mach_msg_trailer_size_t, msgh_seqno: mach_port_seqno_t, msgh_sender: security_token_t, msgh_audit: audit_token_t, msgh_context: mach_port_context_t)Added mach_msg_descriptor_t [struct]Added mach_msg_descriptor_t.init()Added mach_msg_empty_rcv_t.init()Added mach_msg_empty_rcv_t.init(header: mach_msg_header_t, trailer: mach_msg_trailer_t)Added mach_msg_empty_send_t.init()Added mach_msg_empty_send_t.init(header: mach_msg_header_t)Added mach_msg_empty_t [struct]Added mach_msg_empty_t.init()Added mach_msg_header_t.init()Added mach_msg_header_t.init(msgh_bits: mach_msg_bits_t, msgh_size: mach_msg_size_t, msgh_remote_port: mach_port_t, msgh_local_port: mach_port_t, msgh_voucher_port: mach_port_name_t, msgh_id: mach_msg_id_t)Added mach_msg_mac_trailer_t.init()Added mach_msg_mac_trailer_t.init(msgh_trailer_type: mach_msg_trailer_type_t, msgh_trailer_size: mach_msg_trailer_size_t, msgh_seqno: mach_port_seqno_t, msgh_sender: security_token_t, msgh_audit: audit_token_t, msgh_context: mach_port_context_t, msgh_ad: Int32, msgh_labels: msg_labels_t)Added mach_msg_ool_descriptor32_t [struct]Added mach_msg_ool_descriptor32_t.init()Added mach_msg_ool_descriptor32_t.addressAdded mach_msg_ool_descriptor32_t.sizeAdded mach_msg_ool_descriptor64_t [struct]Added mach_msg_ool_descriptor64_t.init()Added mach_msg_ool_descriptor64_t.addressAdded mach_msg_ool_descriptor64_t.sizeAdded mach_msg_ool_descriptor_t [struct]Added mach_msg_ool_descriptor_t.init()Added mach_msg_ool_descriptor_t.addressAdded mach_msg_ool_descriptor_t.sizeAdded mach_msg_ool_ports_descriptor32_t [struct]Added mach_msg_ool_ports_descriptor32_t.init()Added mach_msg_ool_ports_descriptor32_t.addressAdded mach_msg_ool_ports_descriptor32_t.countAdded mach_msg_ool_ports_descriptor64_t [struct]Added mach_msg_ool_ports_descriptor64_t.init()Added mach_msg_ool_ports_descriptor64_t.addressAdded mach_msg_ool_ports_descriptor64_t.countAdded mach_msg_ool_ports_descriptor_t [struct]Added mach_msg_ool_ports_descriptor_t.init()Added mach_msg_ool_ports_descriptor_t.addressAdded mach_msg_ool_ports_descriptor_t.countAdded mach_msg_port_descriptor_t [struct]Added mach_msg_port_descriptor_t.init()Added mach_msg_port_descriptor_t.nameAdded mach_msg_port_descriptor_t.pad1Added mach_msg_security_trailer_t.init()Added mach_msg_security_trailer_t.init(msgh_trailer_type: mach_msg_trailer_type_t, msgh_trailer_size: mach_msg_trailer_size_t, msgh_seqno: mach_port_seqno_t, msgh_sender: security_token_t)Added mach_msg_seqno_trailer_t.init()Added mach_msg_seqno_trailer_t.init(msgh_trailer_type: mach_msg_trailer_type_t, msgh_trailer_size: mach_msg_trailer_size_t, msgh_seqno: mach_port_seqno_t)Added mach_msg_trailer_t.init()Added mach_msg_trailer_t.init(msgh_trailer_type: mach_msg_trailer_type_t, msgh_trailer_size: mach_msg_trailer_size_t)Added mach_msg_type_descriptor_t [struct]Added mach_msg_type_descriptor_t.init()Added mach_msg_type_descriptor_t.pad1Added mach_msg_type_descriptor_t.pad2Added mach_no_senders_notification_t.init()Added mach_no_senders_notification_t.init(not_header: mach_msg_header_t, NDR: NDR_record_t, not_count: mach_msg_type_number_t, trailer: mach_msg_format_0_trailer_t)Added mach_port_deleted_notification_t.init()Added mach_port_deleted_notification_t.init(not_header: mach_msg_header_t, NDR: NDR_record_t, not_port: mach_port_name_t, trailer: mach_msg_format_0_trailer_t)Added mach_port_destroyed_notification_t.init()Added mach_port_destroyed_notification_t.init(not_header: mach_msg_header_t, not_body: mach_msg_body_t, not_port: mach_msg_port_descriptor_t, trailer: mach_msg_format_0_trailer_t)Added mach_port_destroyed_notification_t.not_portAdded mach_port_info_ext.init()Added mach_port_info_ext.init(mpie_status: mach_port_status_t, mpie_boost_cnt: mach_port_msgcount_t, reserved:(UInt32, UInt32, UInt32, UInt32, UInt32, UInt32))Added mach_port_limits.init()Added mach_port_limits.init(mpl_qlimit: mach_port_msgcount_t)Added mach_port_options.init()Added mach_port_options.init(flags: UInt32, mpl: mach_port_limits_t, reserved:(UInt64, UInt64))Added mach_port_qos [struct]Added mach_port_qos.init()Added mach_port_qos.lenAdded mach_port_status.init()Added mach_port_status.init(mps_pset: mach_port_rights_t, mps_seqno: mach_port_seqno_t, mps_mscount: mach_port_mscount_t, mps_qlimit: mach_port_msgcount_t, mps_msgcount: mach_port_msgcount_t, mps_sorights: mach_port_rights_t, mps_srights: boolean_t, mps_pdrequest: boolean_t, mps_nsrequest: boolean_t, mps_flags: natural_t)Added mach_send_once_notification_t.init()Added mach_send_once_notification_t.init(not_header: mach_msg_header_t, trailer: mach_msg_format_0_trailer_t)Added mach_send_possible_notification_t.init()Added mach_send_possible_notification_t.init(not_header: mach_msg_header_t, NDR: NDR_record_t, not_port: mach_port_name_t, trailer: mach_msg_format_0_trailer_t)Added mach_task_basic_info.init()Added mach_task_basic_info.init(virtual_size: mach_vm_size_t, resident_size: mach_vm_size_t, resident_size_max: mach_vm_size_t, user_time: time_value_t, system_time: time_value_t, policy: policy_t, suspend_count: integer_t)Added mach_timebase_info.init()Added mach_timebase_info.init(numer: UInt32, denom: UInt32)Added mach_timespec.init()Added mach_timespec.init(tv_sec: UInt32, tv_nsec: clock_res_t)Added mach_vm_info_region.init()Added mach_vm_info_region.init(vir_start: mach_vm_offset_t, vir_end: mach_vm_offset_t, vir_object: mach_vm_offset_t, vir_offset: memory_object_offset_t, vir_needs_copy: boolean_t, vir_protection: vm_prot_t, vir_max_protection: vm_prot_t, vir_inheritance: vm_inherit_t, vir_wired_count: natural_t, vir_user_wired_count: natural_t)Added mach_vm_read_entry.init()Added mach_vm_read_entry.init(address: mach_vm_address_t, size: mach_vm_size_t)Added mach_voucher_attr_recipe_data.init()Added mach_zone_info_data.init()Added mach_zone_info_data.init(mzi_count: UInt64, mzi_cur_size: UInt64, mzi_max_size: UInt64, mzi_elem_size: UInt64, mzi_alloc_size: UInt64, mzi_sum_size: UInt64, mzi_exhaustible: UInt64, mzi_collectable: UInt64)Added mach_zone_name.init()Added mach_zone_name.init(mzn_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added malloc_introspection_t.init()Added malloc_introspection_t.init(enumerator: CFunctionPointer<((task_t, UnsafeMutablePointer<Void>, UInt32, vm_address_t, CFunctionPointer<memory_reader_t>, CFunctionPointer<vm_range_recorder_t>) -> kern_return_t)>, good_size: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, Int) -> Int)>, check: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)>, print: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, boolean_t) -> Void)>, log: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>) -> Void)>, force_lock: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> Void)>, force_unlock: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> Void)>, statistics: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<malloc_statistics_t>) -> Void)>, zone_locked: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)>, enable_discharge_checking: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)>, disable_discharge_checking: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> Void)>, discharge: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>) -> Void)>, enumerate_discharged_pointers: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>,((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)!) -> Void)>)Added malloc_statistics_t.init()Added malloc_statistics_t.init(blocks_in_use: UInt32, size_in_use: Int, max_size_in_use: Int, size_allocated: Int)Added memory_object_attr_info.init()Added memory_object_attr_info.init(copy_strategy: memory_object_copy_strategy_t, cluster_size: memory_object_cluster_size_t, may_cache_object: boolean_t, temporary: boolean_t)Added memory_object_behave_info.init()Added memory_object_behave_info.init(copy_strategy: memory_object_copy_strategy_t, temporary: boolean_t, invalidate: boolean_t, silent_overwrite: boolean_t, advisory_pageout: boolean_t)Added memory_object_perf_info.init()Added memory_object_perf_info.init(cluster_size: memory_object_cluster_size_t, may_cache: boolean_t)Added mig_reply_error_t.init()Added mig_reply_error_t.init(Head: mach_msg_header_t, NDR: NDR_record_t, RetCode: kern_return_t)Added mig_subsystem.init()Added mig_subsystem.init(server: mig_server_routine_t, start: mach_msg_id_t, end: mach_msg_id_t, maxsize: mach_msg_size_t, reserved: vm_address_t, routine:(mig_routine_descriptor))Added mig_symtab.init()Added mig_symtab.init(ms_routine_name: UnsafeMutablePointer<Int8>, ms_routine_number: Int32, ms_routine: CFunctionPointer<(() -> Void)>)Added msg.init()Added msg_labels_t.init()Added msg_labels_t.init(sender: mach_port_name_t)Added msghdr.init()Added msghdr.init(msg_name: UnsafeMutablePointer<Void>, msg_namelen: socklen_t, msg_iov: UnsafeMutablePointer<iovec>, msg_iovlen: Int32, msg_control: UnsafeMutablePointer<Void>, msg_controllen: socklen_t, msg_flags: Int32)Added msginfo.init()Added msginfo.init(msgmax: Int32, msgmni: Int32, msgmnb: Int32, msgtql: Int32, msgssz: Int32, msgseg: Int32)Added mstats.init()Added mstats.init(bytes_total: Int, chunks_used: Int, bytes_used: Int, chunks_free: Int, bytes_free: Int)Added mymsg.init()Added mymsg.init(mtype: Int, mtext:(Int8))Added net_event_data.init()Added net_event_data.init(if_family: UInt32, if_unit: UInt32, if_name:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added netent.init()Added netent.init(n_name: UnsafeMutablePointer<Int8>, n_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, n_addrtype: Int32, n_net: UInt32)Added netfs_status.init()Added netfs_status.init(ns_status: UInt32, ns_mountopts:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ns_waittime: UInt32, ns_threadcount: UInt32, ns_threadids:())Added ntsid_t.init()Added ntsid_t.init(sid_kind: UInt8, sid_authcount: UInt8, sid_authority:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), sid_authorities:(UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32))Added option.init()Added option.init(name: UnsafePointer<Int8>, has_arg: Int32, flag: UnsafeMutablePointer<Int32>, val: Int32)Added ostat.init()Added ostat.init(st_dev: __uint16_t, st_ino: ino_t, st_mode: mode_t, st_nlink: nlink_t, st_uid: __uint16_t, st_gid: __uint16_t, st_rdev: __uint16_t, st_size: __int32_t, st_atimespec: timespec, st_mtimespec: timespec, st_ctimespec: timespec, st_blksize: __int32_t, st_blocks: __int32_t, st_flags: __uint32_t, st_gen: __uint32_t)Added passwd.init()Added passwd.init(pw_name: UnsafeMutablePointer<Int8>, pw_passwd: UnsafeMutablePointer<Int8>, pw_uid: uid_t, pw_gid: gid_t, pw_change: __darwin_time_t, pw_class: UnsafeMutablePointer<Int8>, pw_gecos: UnsafeMutablePointer<Int8>, pw_dir: UnsafeMutablePointer<Int8>, pw_shell: UnsafeMutablePointer<Int8>, pw_expire: __darwin_time_t)Added policy_bases.init()Added policy_bases.init(ts: policy_timeshare_base_data_t, rr: policy_rr_base_data_t, fifo: policy_fifo_base_data_t)Added policy_fifo_base.init()Added policy_fifo_base.init(base_priority: integer_t)Added policy_fifo_info.init()Added policy_fifo_info.init(max_priority: integer_t, base_priority: integer_t, depressed: boolean_t, depress_priority: integer_t)Added policy_fifo_limit.init()Added policy_fifo_limit.init(max_priority: integer_t)Added policy_infos.init()Added policy_infos.init(ts: policy_timeshare_info_data_t, rr: policy_rr_info_data_t, fifo: policy_fifo_info_data_t)Added policy_limits.init()Added policy_limits.init(ts: policy_timeshare_limit_data_t, rr: policy_rr_limit_data_t, fifo: policy_fifo_limit_data_t)Added policy_rr_base.init()Added policy_rr_base.init(base_priority: integer_t, quantum: integer_t)Added policy_rr_info.init()Added policy_rr_info.init(max_priority: integer_t, base_priority: integer_t, quantum: integer_t, depressed: boolean_t, depress_priority: integer_t)Added policy_rr_limit.init()Added policy_rr_limit.init(max_priority: integer_t)Added policy_timeshare_base.init()Added policy_timeshare_base.init(base_priority: integer_t)Added policy_timeshare_info.init()Added policy_timeshare_info.init(max_priority: integer_t, base_priority: integer_t, cur_priority: integer_t, depressed: boolean_t, depress_priority: integer_t)Added policy_timeshare_limit.init()Added policy_timeshare_limit.init(max_priority: integer_t)Added pollfd.init()Added pollfd.init(fd: Int32, events: Int16, revents: Int16)Added port_obj_tentry.init()Added port_obj_tentry.init(pos_value: UnsafeMutablePointer<Void>, pos_type: Int32)Added proc_rlimit_control_wakeupmon.init()Added proc_rlimit_control_wakeupmon.init(wm_flags: UInt32, wm_rate: Int32)Added processor_basic_info.init()Added processor_basic_info.init(cpu_type: cpu_type_t, cpu_subtype: cpu_subtype_t, running: boolean_t, slot_num: Int32, is_master: boolean_t)Added processor_cpu_load_info.init()Added processor_cpu_load_info.init(cpu_ticks: (UInt32, UInt32, UInt32, UInt32))Added processor_cpu_stat.init()Added processor_cpu_stat.init(irq_ex_cnt: UInt32, ipi_cnt: UInt32, timer_cnt: UInt32, undef_ex_cnt: UInt32, unaligned_cnt: UInt32, vfp_cnt: UInt32, vfp_shortv_cnt: UInt32, data_ex_cnt: UInt32, instr_ex_cnt: UInt32)Added processor_set_basic_info.init()Added processor_set_basic_info.init(processor_count: Int32, default_policy: Int32)Added processor_set_load_info.init()Added processor_set_load_info.init(task_count: Int32, thread_count: Int32, load_average: integer_t, mach_factor: integer_t)Added protoent.init()Added protoent.init(p_name: UnsafeMutablePointer<Int8>, p_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, p_proto: Int32)Added radvisory.init()Added radvisory.init(ra_offset: off_t, ra_count: Int32)Added rb_node.init()Added rb_node.init(opaque: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>))Added rb_tree.init()Added rb_tree.init(opaque: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>))Added rb_tree_ops_t.init()Added rb_tree_ops_t.init(rbto_compare_nodes: rbto_compare_nodes_fn, rbto_compare_key: rbto_compare_key_fn, rbto_node_offset: Int, rbto_context: UnsafeMutablePointer<Void>)Added regex_t.init()Added regmatch_t.init()Added regmatch_t.init(rm_so: regoff_t, rm_eo: regoff_t)Added rlimit.init()Added rlimit.init(rlim_cur: rlim_t, rlim_max: rlim_t)Added routine_descriptor.init()Added routine_descriptor.init(impl_routine: mig_impl_routine_t, stub_routine: mig_stub_routine_t, argc: UInt32, descr_count: UInt32, arg_descr: routine_arg_descriptor_t, max_reply_msg: UInt32)Added rpc_routine_arg_descriptor.init()Added rpc_routine_arg_descriptor.init(type: routine_arg_type, size: routine_arg_size, count: routine_arg_size, offset: routine_arg_offset)Added rpc_routine_descriptor.init()Added rpc_routine_descriptor.init(impl_routine: mig_impl_routine_t, stub_routine: mig_stub_routine_t, argc: UInt32, descr_count: UInt32, arg_descr: rpc_routine_arg_descriptor_t, max_reply_msg: UInt32)Added rpc_signature.init()Added rpc_signature.init(rd: rpc_routine_descriptor, rad:(rpc_routine_arg_descriptor))Added rpc_subsystem.init()Added rpc_subsystem.init(reserved: UnsafeMutablePointer<Void>, start: mach_msg_id_t, end: mach_msg_id_t, maxsize: UInt32, base_addr: vm_address_t, routine:(rpc_routine_descriptor), arg_descriptor:(rpc_routine_arg_descriptor))Added rpcent.init()Added rpcent.init(r_name: UnsafeMutablePointer<Int8>, r_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, r_number: Int32)Added rslvmulti_req.init()Added rslvmulti_req.init(sa: UnsafeMutablePointer<sockaddr>, llsa: UnsafeMutablePointer<UnsafeMutablePointer<sockaddr>>)Added rusage.init()Added rusage.init(ru_utime: timeval, ru_stime: timeval, ru_maxrss: Int, ru_ixrss: Int, ru_idrss: Int, ru_isrss: Int, ru_minflt: Int, ru_majflt: Int, ru_nswap: Int, ru_inblock: Int, ru_oublock: Int, ru_msgsnd: Int, ru_msgrcv: Int, ru_nsignals: Int, ru_nvcsw: Int, ru_nivcsw: Int)Added rusage_info_v0.init()Added rusage_info_v0.init(ri_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), ri_user_time: UInt64, ri_system_time: UInt64, ri_pkg_idle_wkups: UInt64, ri_interrupt_wkups: UInt64, ri_pageins: UInt64, ri_wired_size: UInt64, ri_resident_size: UInt64, ri_phys_footprint: UInt64, ri_proc_start_abstime: UInt64, ri_proc_exit_abstime: UInt64)Added rusage_info_v1.init()Added rusage_info_v1.init(ri_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), ri_user_time: UInt64, ri_system_time: UInt64, ri_pkg_idle_wkups: UInt64, ri_interrupt_wkups: UInt64, ri_pageins: UInt64, ri_wired_size: UInt64, ri_resident_size: UInt64, ri_phys_footprint: UInt64, ri_proc_start_abstime: UInt64, ri_proc_exit_abstime: UInt64, ri_child_user_time: UInt64, ri_child_system_time: UInt64, ri_child_pkg_idle_wkups: UInt64, ri_child_interrupt_wkups: UInt64, ri_child_pageins: UInt64, ri_child_elapsed_abstime: UInt64)Added rusage_info_v2.init()Added rusage_info_v2.init(ri_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), ri_user_time: UInt64, ri_system_time: UInt64, ri_pkg_idle_wkups: UInt64, ri_interrupt_wkups: UInt64, ri_pageins: UInt64, ri_wired_size: UInt64, ri_resident_size: UInt64, ri_phys_footprint: UInt64, ri_proc_start_abstime: UInt64, ri_proc_exit_abstime: UInt64, ri_child_user_time: UInt64, ri_child_system_time: UInt64, ri_child_pkg_idle_wkups: UInt64, ri_child_interrupt_wkups: UInt64, ri_child_pageins: UInt64, ri_child_elapsed_abstime: UInt64, ri_diskio_bytesread: UInt64, ri_diskio_byteswritten: UInt64)Added rusage_info_v3.init()Added rusage_info_v3.init(ri_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), ri_user_time: UInt64, ri_system_time: UInt64, ri_pkg_idle_wkups: UInt64, ri_interrupt_wkups: UInt64, ri_pageins: UInt64, ri_wired_size: UInt64, ri_resident_size: UInt64, ri_phys_footprint: UInt64, ri_proc_start_abstime: UInt64, ri_proc_exit_abstime: UInt64, ri_child_user_time: UInt64, ri_child_system_time: UInt64, ri_child_pkg_idle_wkups: UInt64, ri_child_interrupt_wkups: UInt64, ri_child_pageins: UInt64, ri_child_elapsed_abstime: UInt64, ri_diskio_bytesread: UInt64, ri_diskio_byteswritten: UInt64, ri_cpu_time_qos_default: UInt64, ri_cpu_time_qos_maintenance: UInt64, ri_cpu_time_qos_background: UInt64, ri_cpu_time_qos_utility: UInt64, ri_cpu_time_qos_legacy: UInt64, ri_cpu_time_qos_user_initiated: UInt64, ri_cpu_time_qos_user_interactive: UInt64, ri_billed_system_time: UInt64, ri_serviced_system_time: UInt64)Added sched_param.init()Added sched_param.init(sched_priority: Int32, __opaque:(Int8, Int8, Int8, Int8))Added searchstate.init()Added security_token_t.init()Added security_token_t.init(val: (UInt32, UInt32))Added sem.init()Added sem.init(semval: UInt16, sempid: pid_t, semncnt: UInt16, semzcnt: UInt16)Added sembuf.init()Added sembuf.init(sem_num: UInt16, sem_op: Int16, sem_flg: Int16)Added semun [struct]Added semun.init()Added servent.init()Added servent.init(s_name: UnsafeMutablePointer<Int8>, s_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, s_port: Int32, s_proto: UnsafeMutablePointer<Int8>)Added sf_hdtr.init()Added sf_hdtr.init(headers: UnsafeMutablePointer<iovec>, hdr_cnt: Int32, trailers: UnsafeMutablePointer<iovec>, trl_cnt: Int32)Added sigaction.init()Added sigaction.init(__sigaction_u: __sigaction_u, sa_mask: sigset_t, sa_flags: Int32)Added sigevent.init()Added sigevent.init(sigev_notify: Int32, sigev_signo: Int32, sigev_value: sigval, sigev_notify_function: CFunctionPointer<((sigval) -> Void)>, sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t>)Added sigevent.sigev_valueAdded sigstack.init()Added sigstack.init(ss_sp: UnsafeMutablePointer<Int8>, ss_onstack: Int32)Added sigval [struct]Added sigval.init()Added sigvec.init()Added sigvec.init(sv_handler: CFunctionPointer<((Int32) -> Void)>, sv_mask: Int32, sv_flags: Int32)Added so_np_extensions.init()Added so_np_extensions.init(npx_flags: UInt32, npx_mask: UInt32)Added sockaddr.init()Added sockaddr.init(sa_len: __uint8_t, sa_family: sa_family_t, sa_data:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added sockaddr_in.init()Added sockaddr_in.init(sin_len: __uint8_t, sin_family: sa_family_t, sin_port: in_port_t, sin_addr: in_addr, sin_zero:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added sockaddr_in6.init()Added sockaddr_in6.init(sin6_len: __uint8_t, sin6_family: sa_family_t, sin6_port: in_port_t, sin6_flowinfo: __uint32_t, sin6_addr: in6_addr, sin6_scope_id: __uint32_t)Added sockaddr_storage.init()Added sockaddr_storage.init(ss_len: __uint8_t, ss_family: sa_family_t, __ss_pad1:(Int8, Int8, Int8, Int8, Int8, Int8), __ss_align: __int64_t, __ss_pad2:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added sockaddr_un.init()Added sockaddr_un.init(sun_len: UInt8, sun_family: sa_family_t, sun_path:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added sockproto.init()Added sockproto.init(sp_family: __uint16_t, sp_protocol: __uint16_t)Added stat.init(st_dev: dev_t, st_mode: mode_t, st_nlink: nlink_t, st_ino: __darwin_ino64_t, st_uid: uid_t, st_gid: gid_t, st_rdev: dev_t, st_atimespec: timespec, st_mtimespec: timespec, st_ctimespec: timespec, st_birthtimespec: timespec, st_size: off_t, st_blocks: blkcnt_t, st_blksize: blksize_t, st_flags: __uint32_t, st_gen: __uint32_t, st_lspare: __int32_t, st_qspare:(__int64_t, __int64_t))Added statfs.init()Added statvfs.init()Added statvfs.init(f_bsize: UInt, f_frsize: UInt, f_blocks: fsblkcnt_t, f_bfree: fsblkcnt_t, f_bavail: fsblkcnt_t, f_files: fsfilcnt_t, f_ffree: fsfilcnt_t, f_favail: fsfilcnt_t, f_fsid: UInt, f_flag: UInt, f_namemax: UInt)Added task_absolutetime_info.init()Added task_absolutetime_info.init(total_user: UInt64, total_system: UInt64, threads_user: UInt64, threads_system: UInt64)Added task_affinity_tag_info.init()Added task_affinity_tag_info.init(set_count: integer_t, min: integer_t, max: integer_t, task_count: integer_t)Added task_basic_info.init()Added task_basic_info.init(suspend_count: integer_t, virtual_size: vm_size_t, resident_size: vm_size_t, user_time: time_value_t, system_time: time_value_t, policy: policy_t)Added task_basic_info_32.init()Added task_basic_info_32.init(suspend_count: integer_t, virtual_size: natural_t, resident_size: natural_t, user_time: time_value_t, system_time: time_value_t, policy: policy_t)Added task_basic_info_64.init()Added task_basic_info_64.init(suspend_count: integer_t, virtual_size: mach_vm_size_t, resident_size: mach_vm_size_t, user_time: time_value_t, system_time: time_value_t, policy: policy_t)Added task_basic_info_64_2.init()Added task_basic_info_64_2.init(suspend_count: integer_t, virtual_size: mach_vm_size_t, resident_size: mach_vm_size_t, user_time: time_value_t, system_time: time_value_t, policy: policy_t)Added task_category_policy.init()Added task_category_policy.init(role: task_role_t)Added task_dyld_info.init()Added task_dyld_info.init(all_image_info_addr: mach_vm_address_t, all_image_info_size: mach_vm_size_t, all_image_info_format: integer_t)Added task_events_info.init()Added task_events_info.init(faults: integer_t, pageins: integer_t, cow_faults: integer_t, messages_sent: integer_t, messages_received: integer_t, syscalls_mach: integer_t, syscalls_unix: integer_t, csw: integer_t)Added task_extmod_info.init()Added task_extmod_info.init(task_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), extmod_statistics: vm_extmod_statistics_data_t)Added task_kernelmemory_info.init()Added task_kernelmemory_info.init(total_palloc: UInt64, total_pfree: UInt64, total_salloc: UInt64, total_sfree: UInt64)Added task_power_info.init()Added task_power_info.init(total_user: UInt64, total_system: UInt64, task_interrupt_wakeups: UInt64, task_platform_idle_wakeups: UInt64, task_timer_wakeups_bin_1: UInt64, task_timer_wakeups_bin_2: UInt64)Added task_power_info_v2.init()Added task_power_info_v2.init(cpu_energy: task_power_info_data_t, gpu_energy: gpu_energy_data)Added task_qos_policy.init()Added task_qos_policy.init(task_latency_qos_tier: task_latency_qos_t, task_throughput_qos_tier: task_throughput_qos_t)Added task_thread_times_info.init()Added task_thread_times_info.init(user_time: time_value_t, system_time: time_value_t)Added task_trace_memory_info.init()Added task_trace_memory_info.init(user_memory_address: UInt64, buffer_size: UInt64, mailbox_array_size: UInt64)Added task_vm_info.init()Added task_vm_info.init(virtual_size: mach_vm_size_t, region_count: integer_t, page_size: integer_t, resident_size: mach_vm_size_t, resident_size_peak: mach_vm_size_t, device: mach_vm_size_t, device_peak: mach_vm_size_t, internal: mach_vm_size_t, internal_peak: mach_vm_size_t, external: mach_vm_size_t, external_peak: mach_vm_size_t, reusable: mach_vm_size_t, reusable_peak: mach_vm_size_t, purgeable_volatile_pmap: mach_vm_size_t, purgeable_volatile_resident: mach_vm_size_t, purgeable_volatile_virtual: mach_vm_size_t, compressed: mach_vm_size_t, compressed_peak: mach_vm_size_t, compressed_lifetime: mach_vm_size_t)Added task_wait_state_info.init()Added task_wait_state_info.init(total_wait_state_time: UInt64, total_wait_sfi_state_time: UInt64, _reserved:(UInt32, UInt32, UInt32, UInt32))Added task_zone_info_data.init()Added task_zone_info_data.init(tzi_count: UInt64, tzi_cur_size: UInt64, tzi_max_size: UInt64, tzi_elem_size: UInt64, tzi_alloc_size: UInt64, tzi_sum_size: UInt64, tzi_exhaustible: UInt64, tzi_collectable: UInt64, tzi_caller_acct: UInt64, tzi_task_alloc: UInt64, tzi_task_free: UInt64)Added tcphdr [struct]Added tcphdr.init()Added tcphdr.th_ackAdded tcphdr.th_dportAdded tcphdr.th_flagsAdded tcphdr.th_seqAdded tcphdr.th_sportAdded tcphdr.th_sumAdded tcphdr.th_urpAdded tcphdr.th_winAdded termios.init()Added termios.init(c_iflag: tcflag_t, c_oflag: tcflag_t, c_cflag: tcflag_t, c_lflag: tcflag_t, c_cc:(cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t), c_ispeed: speed_t, c_ospeed: speed_t)Added thread_affinity_policy.init()Added thread_affinity_policy.init(affinity_tag: integer_t)Added thread_background_policy.init()Added thread_background_policy.init(priority: integer_t)Added thread_basic_info.init()Added thread_basic_info.init(user_time: time_value_t, system_time: time_value_t, cpu_usage: integer_t, policy: policy_t, run_state: integer_t, flags: integer_t, suspend_count: integer_t, sleep_time: integer_t)Added thread_extended_policy.init()Added thread_extended_policy.init(timeshare: boolean_t)Added thread_identifier_info.init()Added thread_identifier_info.init(thread_id: UInt64, thread_handle: UInt64, dispatch_qaddr: UInt64)Added thread_latency_qos_policy.init()Added thread_latency_qos_policy.init(thread_latency_qos_tier: thread_latency_qos_t)Added thread_precedence_policy.init()Added thread_precedence_policy.init(importance: integer_t)Added thread_standard_policy.init()Added thread_standard_policy.init(no_data: natural_t)Added thread_throughput_qos_policy.init()Added thread_throughput_qos_policy.init(thread_throughput_qos_tier: thread_throughput_qos_t)Added thread_time_constraint_policy.init()Added thread_time_constraint_policy.init(period: UInt32, computation: UInt32, constraint: UInt32, preemptible: boolean_t)Added time_value.init()Added time_value.init(seconds: integer_t, microseconds: integer_t)Added timeb.init()Added timeb.init(time: time_t, millitm: UInt16, timezone: Int16, dstflag: Int16)Added timespec.init()Added timespec.init(tv_sec: __darwin_time_t, tv_nsec: Int)Added timeval.init()Added timeval.init(tv_sec: __darwin_time_t, tv_usec: __darwin_suseconds_t)Added timeval32.init()Added timeval32.init(tv_sec: __int32_t, tv_usec: __int32_t)Added timezone.init()Added timezone.init(tz_minuteswest: Int32, tz_dsttime: Int32)Added tm.init()Added tm.init(tm_sec: Int32, tm_min: Int32, tm_hour: Int32, tm_mday: Int32, tm_mon: Int32, tm_year: Int32, tm_wday: Int32, tm_yday: Int32, tm_isdst: Int32, tm_gmtoff: Int, tm_zone: UnsafeMutablePointer<Int8>)Added tms.init()Added tms.init(tms_utime: clock_t, tms_stime: clock_t, tms_cutime: clock_t, tms_cstime: clock_t)Added ttysize.init()Added ttysize.init(ts_lines: UInt16, ts_cols: UInt16, ts_xxx: UInt16, ts_yyy: UInt16)Added ucred.init()Added utimbuf.init()Added utimbuf.init(actime: time_t, modtime: time_t)Added utmpx.init()Added utmpx.init(ut_user: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ut_id:(Int8, Int8, Int8, Int8), ut_line:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ut_pid: pid_t, ut_type: Int16, ut_tv: timeval, ut_host:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ut_pad:(__uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t))Added utsname.init()Added vfs_server.init()Added vfsconf.init()Added vfsconf.init(vfc_reserved1: UInt32, vfc_name:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), vfc_typenum: Int32, vfc_refcount: Int32, vfc_flags: Int32, vfc_reserved2: UInt32, vfc_reserved3: UInt32)Added vfsidctl.init()Added vfsidctl.init(vc_vers: Int32, vc_fsid: fsid_t, vc_ptr: UnsafeMutablePointer<Void>, vc_len: Int, vc_spare:(UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32))Added vfsquery.init()Added vfsquery.init(vq_flags: UInt32, vq_spare:(UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32))Added vfsstatfs.init()Added vm_extmod_statistics.init()Added vm_extmod_statistics.init(task_for_pid_count: Int64, task_for_pid_caller_count: Int64, thread_creation_count: Int64, thread_creation_caller_count: Int64, thread_set_state_count: Int64, thread_set_state_caller_count: Int64)Added vm_info_object.init()Added vm_info_object.init(vio_object: natural_t, vio_size: natural_t, vio_ref_count: UInt32, vio_resident_page_count: UInt32, vio_absent_count: UInt32, vio_copy: natural_t, vio_shadow: natural_t, vio_shadow_offset: natural_t, vio_paging_offset: natural_t, vio_copy_strategy: memory_object_copy_strategy_t, vio_last_alloc: vm_offset_t, vio_paging_in_progress: UInt32, vio_pager_created: boolean_t, vio_pager_initialized: boolean_t, vio_pager_ready: boolean_t, vio_can_persist: boolean_t, vio_internal: boolean_t, vio_temporary: boolean_t, vio_alive: boolean_t, vio_purgable: boolean_t, vio_purgable_volatile: boolean_t)Added vm_info_region.init()Added vm_info_region.init(vir_start: natural_t, vir_end: natural_t, vir_object: natural_t, vir_offset: natural_t, vir_needs_copy: boolean_t, vir_protection: vm_prot_t, vir_max_protection: vm_prot_t, vir_inheritance: vm_inherit_t, vir_wired_count: natural_t, vir_user_wired_count: natural_t)Added vm_info_region_64.init()Added vm_info_region_64.init(vir_start: natural_t, vir_end: natural_t, vir_object: natural_t, vir_offset: memory_object_offset_t, vir_needs_copy: boolean_t, vir_protection: vm_prot_t, vir_max_protection: vm_prot_t, vir_inheritance: vm_inherit_t, vir_wired_count: natural_t, vir_user_wired_count: natural_t)Added vm_page_info_basic.init()Added vm_page_info_basic.init(disposition: Int32, ref_count: Int32, object_id: vm_object_id_t, offset: memory_object_offset_t, depth: Int32, __pad: Int32)Added vm_purgeable_info.init()Added vm_purgeable_info.init(fifo_data: (vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t), obsolete_data: vm_purgeable_stat_t, lifo_data:(vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t))Added vm_purgeable_stat.init()Added vm_purgeable_stat.init(count: UInt64, size: UInt64)Added vm_range_t.init()Added vm_range_t.init(address: vm_address_t, size: vm_size_t)Added vm_read_entry.init()Added vm_read_entry.init(address: vm_address_t, size: vm_size_t)Added vm_region_basic_info.init()Added vm_region_basic_info.init(protection: vm_prot_t, max_protection: vm_prot_t, inheritance: vm_inherit_t, shared: boolean_t, reserved: boolean_t, offset: UInt32, behavior: vm_behavior_t, user_wired_count: UInt16)Added vm_region_basic_info_64.init()Added vm_region_basic_info_64.init(protection: vm_prot_t, max_protection: vm_prot_t, inheritance: vm_inherit_t, shared: boolean_t, reserved: boolean_t, offset: memory_object_offset_t, behavior: vm_behavior_t, user_wired_count: UInt16)Added vm_region_extended_info.init()Added vm_region_extended_info.init(protection: vm_prot_t, user_tag: UInt32, pages_resident: UInt32, pages_shared_now_private: UInt32, pages_swapped_out: UInt32, pages_dirtied: UInt32, ref_count: UInt32, shadow_depth: UInt16, external_pager: UInt8, share_mode: UInt8, pages_reusable: UInt32)Added vm_region_submap_info.init()Added vm_region_submap_info.init(protection: vm_prot_t, max_protection: vm_prot_t, inheritance: vm_inherit_t, offset: UInt32, user_tag: UInt32, pages_resident: UInt32, pages_shared_now_private: UInt32, pages_swapped_out: UInt32, pages_dirtied: UInt32, ref_count: UInt32, shadow_depth: UInt16, external_pager: UInt8, share_mode: UInt8, is_submap: boolean_t, behavior: vm_behavior_t, object_id: vm32_object_id_t, user_wired_count: UInt16)Added vm_region_submap_info_64.init()Added vm_region_submap_info_64.init(protection: vm_prot_t, max_protection: vm_prot_t, inheritance: vm_inherit_t, offset: memory_object_offset_t, user_tag: UInt32, pages_resident: UInt32, pages_shared_now_private: UInt32, pages_swapped_out: UInt32, pages_dirtied: UInt32, ref_count: UInt32, shadow_depth: UInt16, external_pager: UInt8, share_mode: UInt8, is_submap: boolean_t, behavior: vm_behavior_t, object_id: vm32_object_id_t, user_wired_count: UInt16, pages_reusable: UInt32)Added vm_region_submap_short_info_64.init()Added vm_region_submap_short_info_64.init(protection: vm_prot_t, max_protection: vm_prot_t, inheritance: vm_inherit_t, offset: memory_object_offset_t, user_tag: UInt32, ref_count: UInt32, shadow_depth: UInt16, external_pager: UInt8, share_mode: UInt8, is_submap: boolean_t, behavior: vm_behavior_t, object_id: vm32_object_id_t, user_wired_count: UInt16)Added vm_region_top_info.init()Added vm_region_top_info.init(obj_id: UInt32, ref_count: UInt32, private_pages_resident: UInt32, shared_pages_resident: UInt32, share_mode: UInt8)Added vm_statistics.init()Added vm_statistics.init(free_count: natural_t, active_count: natural_t, inactive_count: natural_t, wire_count: natural_t, zero_fill_count: natural_t, reactivations: natural_t, pageins: natural_t, pageouts: natural_t, faults: natural_t, cow_faults: natural_t, lookups: natural_t, hits: natural_t, purgeable_count: natural_t, purges: natural_t, speculative_count: natural_t)Added vm_statistics64.init()Added vm_statistics64.init(free_count: natural_t, active_count: natural_t, inactive_count: natural_t, wire_count: natural_t, zero_fill_count: UInt64, reactivations: UInt64, pageins: UInt64, pageouts: UInt64, faults: UInt64, cow_faults: UInt64, lookups: UInt64, hits: UInt64, purges: UInt64, purgeable_count: natural_t, speculative_count: natural_t, decompressions: UInt64, compressions: UInt64, swapins: UInt64, swapouts: UInt64, compressor_page_count: natural_t, throttled_count: natural_t, external_page_count: natural_t, internal_page_count: natural_t, total_uncompressed_pages_in_compressor: UInt64)Added vmspace.init()Added vmspace.init(dummy: Int32, dummy2: caddr_t, dummy3:(Int32, Int32, Int32, Int32, Int32), dummy4:(caddr_t, caddr_t, caddr_t))Added vol_attributes_attr.init()Added vol_attributes_attr.init(validattr: attribute_set_t, nativeattr: attribute_set_t)Added vol_capabilities_attr.init()Added vol_capabilities_attr.init(capabilities: vol_capabilities_set_t, valid: vol_capabilities_set_t)Added wait [struct]Added wait.init()Added winsize.init()Added winsize.init(ws_row: UInt16, ws_col: UInt16, ws_xpixel: UInt16, ws_ypixel: UInt16)Added wordexp_t.init()Added wordexp_t.init(we_wordc: Int, we_wordv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, we_offs: Int)Added xsw_usage.init()Added xsw_usage.init(xsu_total: UInt64, xsu_avail: UInt64, xsu_used: UInt64, xsu_pagesize: UInt32, xsu_encrypted: boolean_t)Added xucred.init()Added xucred.init(cr_version: u_int, cr_uid: uid_t, cr_ngroups: Int16, cr_groups:(gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t))Added zone_info.init()Added zone_info.init(zi_count: integer_t, zi_cur_size: vm_size_t, zi_max_size: vm_size_t, zi_elem_size: vm_size_t, zi_alloc_size: vm_size_t, zi_pageable: integer_t, zi_sleepable: integer_t, zi_exhaustible: integer_t, zi_collectable: integer_t)Added zone_name.init()Added zone_name.init(zn_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8))Added LC_COLLATE_MASKAdded LC_CTYPE_MASKAdded LC_MESSAGES_MASKAdded LC_MONETARY_MASKAdded LC_NUMERIC_MASKAdded LC_TIME_MASKAdded TASK_VM_INFO_PURGEABLE_ACCOUNTAdded atof_l(UnsafePointer<Int8>, locale_t) -> DoubleAdded atoi_l(UnsafePointer<Int8>, locale_t) -> Int32Added atol_l(UnsafePointer<Int8>, locale_t) -> IntAdded atoll_l(UnsafePointer<Int8>, locale_t) -> Int64Added btowc_l(Int32, locale_t) -> wint_tAdded digittoint_l(Int32, locale_t) -> Int32Added duplocale() -> locale_tAdded falseAdded fgetwc_l(UnsafeMutablePointer<FILE>, locale_t) -> wint_tAdded fgetwln_l(UnsafeMutablePointer<FILE>, UnsafeMutablePointer<Int>, locale_t) -> UnsafeMutablePointer<wchar_t>Added fgetws_l(UnsafeMutablePointer<wchar_t>, Int32, UnsafeMutablePointer<FILE>, locale_t) -> UnsafeMutablePointer<wchar_t>Added fputwc_l(wchar_t, UnsafeMutablePointer<FILE>, locale_t) -> wint_tAdded fputws_l(UnsafePointer<wchar_t>, UnsafeMutablePointer<FILE>, locale_t) -> Int32Added freelocale() -> Int32Added getwc_l(UnsafeMutablePointer<FILE>, locale_t) -> wint_tAdded getwchar_l() -> wint_tAdded isalnum_l(Int32, locale_t) -> Int32Added isalpha_l(Int32, locale_t) -> Int32Added isblank_l(Int32, locale_t) -> Int32Added iscntrl_l(Int32, locale_t) -> Int32Added isdigit_l(Int32, locale_t) -> Int32Added isgraph_l(Int32, locale_t) -> Int32Added ishexnumber_l(Int32, locale_t) -> Int32Added isideogram_l(Int32, locale_t) -> Int32Added islower_l(Int32, locale_t) -> Int32Added isnumber_l(Int32, locale_t) -> Int32Added isphonogram_l(Int32, locale_t) -> Int32Added isprint_l(Int32, locale_t) -> Int32Added ispunct_l(Int32, locale_t) -> Int32Added isrune_l(Int32, locale_t) -> Int32Added isspace_l(Int32, locale_t) -> Int32Added isspecial_l(Int32, locale_t) -> Int32Added isupper_l(Int32, locale_t) -> Int32Added iswalnum_l(wint_t, locale_t) -> Int32Added iswalpha_l(wint_t, locale_t) -> Int32Added iswblank_l(wint_t, locale_t) -> Int32Added iswcntrl_l(wint_t, locale_t) -> Int32Added iswctype_l(wint_t, wctype_t, locale_t) -> Int32Added iswdigit_l(wint_t, locale_t) -> Int32Added iswgraph_l(wint_t, locale_t) -> Int32Added iswhexnumber_l(wint_t, locale_t) -> Int32Added iswideogram_l(wint_t, locale_t) -> Int32Added iswlower_l(wint_t, locale_t) -> Int32Added iswnumber_l(wint_t, locale_t) -> Int32Added iswphonogram_l(wint_t, locale_t) -> Int32Added iswprint_l(wint_t, locale_t) -> Int32Added iswpunct_l(wint_t, locale_t) -> Int32Added iswrune_l(wint_t, locale_t) -> Int32Added iswspace_l(wint_t, locale_t) -> Int32Added iswspecial_l(wint_t, locale_t) -> Int32Added iswupper_l(wint_t, locale_t) -> Int32Added iswxdigit_l(wint_t, locale_t) -> Int32Added isxdigit_l(Int32, locale_t) -> Int32Added locale_tAdded localeconv_l() -> UnsafeMutablePointer<lconv>Added mach_port_qos_tAdded malloc_size(UnsafePointer<Void>) -> IntAdded mblen_l(UnsafePointer<Int8>, Int, locale_t) -> Int32Added mbrlen_l(UnsafePointer<Int8>, Int, UnsafeMutablePointer<mbstate_t>, locale_t) -> IntAdded mbrtowc_l(UnsafeMutablePointer<wchar_t>, UnsafePointer<Int8>, Int, UnsafeMutablePointer<mbstate_t>, locale_t) -> IntAdded mbsinit_l(UnsafePointer<mbstate_t>, locale_t) -> Int32Added mbsnrtowcs_l(UnsafeMutablePointer<wchar_t>, UnsafeMutablePointer<UnsafePointer<Int8>>, Int, Int, UnsafeMutablePointer<mbstate_t>, locale_t) -> IntAdded mbsrtowcs_l(UnsafeMutablePointer<wchar_t>, UnsafeMutablePointer<UnsafePointer<Int8>>, Int, UnsafeMutablePointer<mbstate_t>, locale_t) -> IntAdded mbstate_tAdded mbstowcs_l(UnsafeMutablePointer<wchar_t>, UnsafePointer<Int8>, Int, locale_t) -> IntAdded mbtowc_l(UnsafeMutablePointer<wchar_t>, UnsafePointer<Int8>, Int, locale_t) -> Int32Added newlocale(Int32, UnsafePointer<Int8>, locale_t) -> locale_tAdded nextwctype_l(wint_t, wctype_t, locale_t) -> wint_tAdded nl_langinfo_l(nl_item, locale_t) -> UnsafeMutablePointer<Int8>Added putwc_l(wchar_t, UnsafeMutablePointer<FILE>, locale_t) -> wint_tAdded putwchar_l(wchar_t, locale_t) -> wint_tAdded querylocale(Int32, locale_t) -> UnsafePointer<Int8>Added routine_arg_descriptorAdded semun_tAdded strcasecmp_l(UnsafePointer<Int8>, UnsafePointer<Int8>, locale_t) -> Int32Added strcasestr_l(UnsafePointer<Int8>, UnsafePointer<Int8>, locale_t) -> UnsafeMutablePointer<Int8>Added strcoll_l(UnsafePointer<Int8>, UnsafePointer<Int8>, locale_t) -> Int32Added strftime_l(UnsafeMutablePointer<Int8>, Int, UnsafePointer<Int8>, UnsafePointer<tm>, locale_t) -> IntAdded strncasecmp_l(UnsafePointer<Int8>, UnsafePointer<Int8>, Int, locale_t) -> Int32Added strptime_l(UnsafePointer<Int8>, UnsafePointer<Int8>, UnsafeMutablePointer<tm>, locale_t) -> UnsafeMutablePointer<Int8>Added strtod_l(UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, locale_t) -> DoubleAdded strtof_l(UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, locale_t) -> FloatAdded strtoimax_l(UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, Int32, locale_t) -> intmax_tAdded strtol_l(UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, Int32, locale_t) -> IntAdded strtoll_l(UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, Int32, locale_t) -> Int64Added strtoq_l(UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, Int32, locale_t) -> Int64Added strtoul_l(UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, Int32, locale_t) -> UIntAdded strtoull_l(UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, Int32, locale_t) -> UInt64Added strtoumax_l(UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, Int32, locale_t) -> uintmax_tAdded strtouq_l(UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, Int32, locale_t) -> UInt64Added strxfrm_l(UnsafeMutablePointer<Int8>, UnsafePointer<Int8>, Int, locale_t) -> IntAdded tolower_l(Int32, locale_t) -> Int32Added toupper_l(Int32, locale_t) -> Int32Added towctrans_l(wint_t, wctrans_t, locale_t) -> wint_tAdded towlower_l(wint_t, locale_t) -> wint_tAdded towupper_l(wint_t, locale_t) -> wint_tAdded trueAdded ungetwc_l(wint_t, UnsafeMutablePointer<FILE>, locale_t) -> wint_tAdded uselocale() -> locale_tAdded vasprintf_l(UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, locale_t, UnsafePointer<Int8>, CVaListPointer) -> Int32Added vdprintf_l(Int32, locale_t, UnsafePointer<Int8>, CVaListPointer) -> Int32Added vfprintf_l(UnsafeMutablePointer<FILE>, locale_t, UnsafePointer<Int8>, CVaListPointer) -> Int32Added vfscanf_l(UnsafeMutablePointer<FILE>, locale_t, UnsafePointer<Int8>, CVaListPointer) -> Int32Added vfwprintf_l(UnsafeMutablePointer<FILE>, locale_t, UnsafePointer<wchar_t>, __darwin_va_list) -> Int32Added vfwscanf_l(UnsafeMutablePointer<FILE>, locale_t, UnsafePointer<wchar_t>, __darwin_va_list) -> Int32Added vprintf_l(locale_t, UnsafePointer<Int8>, CVaListPointer) -> Int32Added vscanf_l(locale_t, UnsafePointer<Int8>, CVaListPointer) -> Int32Added vsnprintf_l(UnsafeMutablePointer<Int8>, Int, locale_t, UnsafePointer<Int8>, CVaListPointer) -> Int32Added vsprintf_l(UnsafeMutablePointer<Int8>, locale_t, UnsafePointer<Int8>, CVaListPointer) -> Int32Added vsscanf_l(UnsafePointer<Int8>, locale_t, UnsafePointer<Int8>, CVaListPointer) -> Int32Added vswprintf_l(UnsafeMutablePointer<wchar_t>, Int, locale_t, UnsafePointer<wchar_t>, __darwin_va_list) -> Int32Added vswscanf_l(UnsafePointer<wchar_t>, locale_t, UnsafePointer<wchar_t>, __darwin_va_list) -> Int32Added vwprintf_l(locale_t, UnsafePointer<wchar_t>, __darwin_va_list) -> Int32Added vwscanf_l(locale_t, UnsafePointer<wchar_t>, __darwin_va_list) -> Int32Added wcrtomb_l(UnsafeMutablePointer<Int8>, wchar_t, UnsafeMutablePointer<mbstate_t>, locale_t) -> IntAdded wcscasecmp_l(UnsafePointer<wchar_t>, UnsafePointer<wchar_t>, locale_t) -> Int32Added wcscoll_l(UnsafePointer<wchar_t>, UnsafePointer<wchar_t>, locale_t) -> Int32Added wcsftime_l(UnsafeMutablePointer<wchar_t>, Int, UnsafePointer<wchar_t>, UnsafePointer<tm>, locale_t) -> IntAdded wcsncasecmp_l(UnsafePointer<wchar_t>, UnsafePointer<wchar_t>, Int, locale_t) -> Int32Added wcsnrtombs_l(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UnsafePointer<wchar_t>>, Int, Int, UnsafeMutablePointer<mbstate_t>, locale_t) -> IntAdded wcsrtombs_l(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UnsafePointer<wchar_t>>, Int, UnsafeMutablePointer<mbstate_t>, locale_t) -> IntAdded wcstod_l(UnsafePointer<wchar_t>, UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, locale_t) -> DoubleAdded wcstof_l(UnsafePointer<wchar_t>, UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, locale_t) -> FloatAdded wcstoimax_l(UnsafePointer<wchar_t>, UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, Int32, locale_t) -> intmax_tAdded wcstol_l(UnsafePointer<wchar_t>, UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, Int32, locale_t) -> IntAdded wcstoll_l(UnsafePointer<wchar_t>, UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, Int32, locale_t) -> Int64Added wcstombs_l(UnsafeMutablePointer<Int8>, UnsafePointer<wchar_t>, Int, locale_t) -> IntAdded wcstoul_l(UnsafePointer<wchar_t>, UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, Int32, locale_t) -> UIntAdded wcstoull_l(UnsafePointer<wchar_t>, UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, Int32, locale_t) -> UInt64Added wcstoumax_l(UnsafePointer<wchar_t>, UnsafeMutablePointer<UnsafeMutablePointer<wchar_t>>, Int32, locale_t) -> uintmax_tAdded wcswidth_l(UnsafePointer<wchar_t>, Int, locale_t) -> Int32Added wcsxfrm_l(UnsafeMutablePointer<wchar_t>, UnsafePointer<wchar_t>, Int, locale_t) -> IntAdded wctob_l(wint_t, locale_t) -> Int32Added wctomb_l(UnsafeMutablePointer<Int8>, wchar_t, locale_t) -> Int32Added wctrans_l(UnsafePointer<Int8>, locale_t) -> wctrans_tAdded wctype_l(UnsafePointer<Int8>, locale_t) -> wctype_tAdded wcwidth_l(wchar_t, locale_t) -> Int32Modified DBM [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DBM {     var __opaque: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct DBM {     var __opaque: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(__opaque __opaque: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified DIR [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DIR {     var __dd_fd: Int32     var __dd_loc: Int     var __dd_size: Int     var __dd_buf: UnsafeMutablePointer<Int8>     var __dd_len: Int32     var __dd_seek: Int     var __dd_rewind: Int     var __dd_flags: Int32     var __dd_lock: __darwin_pthread_mutex_t     var __dd_td: COpaquePointer } ``` |
| To | ``` struct DIR {     var __dd_fd: Int32     var __dd_loc: Int     var __dd_size: Int     var __dd_buf: UnsafeMutablePointer<Int8>     var __dd_len: Int32     var __dd_seek: Int     var __dd_rewind: Int     var __dd_flags: Int32     var __dd_lock: __darwin_pthread_mutex_t     var __dd_td: COpaquePointer     init()     init(__dd_fd __dd_fd: Int32, __dd_loc __dd_loc: Int, __dd_size __dd_size: Int, __dd_buf __dd_buf: UnsafeMutablePointer<Int8>, __dd_len __dd_len: Int32, __dd_seek __dd_seek: Int, __dd_rewind __dd_rewind: Int, __dd_flags __dd_flags: Int32, __dd_lock __dd_lock: __darwin_pthread_mutex_t, __dd_td __dd_td: COpaquePointer) } ``` |

Modified FTW [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FTW {     var base: Int32     var level: Int32 } ``` |
| To | ``` struct FTW {     var base: Int32     var level: Int32     init()     init(base base: Int32, level level: Int32) } ``` |

Modified NDR_record_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NDR_record_t {     var mig_vers: UInt8     var if_vers: UInt8     var reserved1: UInt8     var mig_encoding: UInt8     var int_rep: UInt8     var char_rep: UInt8     var float_rep: UInt8     var reserved2: UInt8 } ``` |
| To | ``` struct NDR_record_t {     var mig_vers: UInt8     var if_vers: UInt8     var reserved1: UInt8     var mig_encoding: UInt8     var int_rep: UInt8     var char_rep: UInt8     var float_rep: UInt8     var reserved2: UInt8     init()     init(mig_vers mig_vers: UInt8, if_vers if_vers: UInt8, reserved1 reserved1: UInt8, mig_encoding mig_encoding: UInt8, int_rep int_rep: UInt8, char_rep char_rep: UInt8, float_rep float_rep: UInt8, reserved2 reserved2: UInt8) } ``` |

Modified ProcessSerialNumber [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ProcessSerialNumber {     var highLongOfPSN: UInt32     var lowLongOfPSN: UInt32 } ``` |
| To | ``` struct ProcessSerialNumber {     var highLongOfPSN: UInt32     var lowLongOfPSN: UInt32     init()     init(highLongOfPSN highLongOfPSN: UInt32, lowLongOfPSN lowLongOfPSN: UInt32) } ``` |

Modified accessx_descriptor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct accessx_descriptor {     var ad_name_offset: UInt32     var ad_flags: Int32     var ad_pad: (Int32, Int32) } ``` |
| To | ``` struct accessx_descriptor {     var ad_name_offset: UInt32     var ad_flags: Int32     var ad_pad: (Int32, Int32)     init()     init(ad_name_offset ad_name_offset: UInt32, ad_flags ad_flags: Int32, ad_pad ad_pad: (Int32, Int32)) } ``` |

Modified addrinfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct addrinfo {     var ai_flags: Int32     var ai_family: Int32     var ai_socktype: Int32     var ai_protocol: Int32     var ai_addrlen: socklen_t     var ai_canonname: UnsafeMutablePointer<Int8>     var ai_addr: UnsafeMutablePointer<sockaddr>     var ai_next: UnsafeMutablePointer<addrinfo> } ``` |
| To | ``` struct addrinfo {     var ai_flags: Int32     var ai_family: Int32     var ai_socktype: Int32     var ai_protocol: Int32     var ai_addrlen: socklen_t     var ai_canonname: UnsafeMutablePointer<Int8>     var ai_addr: UnsafeMutablePointer<sockaddr>     var ai_next: UnsafeMutablePointer<addrinfo>     init()     init(ai_flags ai_flags: Int32, ai_family ai_family: Int32, ai_socktype ai_socktype: Int32, ai_protocol ai_protocol: Int32, ai_addrlen ai_addrlen: socklen_t, ai_canonname ai_canonname: UnsafeMutablePointer<Int8>, ai_addr ai_addr: UnsafeMutablePointer<sockaddr>, ai_next ai_next: UnsafeMutablePointer<addrinfo>) } ``` |

Modified aiocb [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct aiocb {     var aio_fildes: Int32     var aio_offset: off_t     var aio_buf: UnsafeMutablePointer<Void>     var aio_nbytes: UInt     var aio_reqprio: Int32     var aio_sigevent: sigevent     var aio_lio_opcode: Int32 } ``` |
| To | ``` struct aiocb {     var aio_fildes: Int32     var aio_offset: off_t     var aio_buf: UnsafeMutablePointer<Void>     var aio_nbytes: Int     var aio_reqprio: Int32     var aio_sigevent: sigevent     var aio_lio_opcode: Int32     init()     init(aio_fildes aio_fildes: Int32, aio_offset aio_offset: off_t, aio_buf aio_buf: UnsafeMutablePointer<Void>, aio_nbytes aio_nbytes: Int, aio_reqprio aio_reqprio: Int32, aio_sigevent aio_sigevent: sigevent, aio_lio_opcode aio_lio_opcode: Int32) } ``` |

Modified aiocb.aio_nbytes

|  | Declaration |
| --- | --- |
| From | ``` var aio_nbytes: UInt ``` |
| To | ``` var aio_nbytes: Int ``` |

Modified arm_state_hdr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct arm_state_hdr {     var flavor: UInt32     var count: UInt32 } ``` |
| To | ``` struct arm_state_hdr {     var flavor: UInt32     var count: UInt32     init()     init(flavor flavor: UInt32, count count: UInt32) } ``` |

Modified arm_unified_thread_state [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct arm_unified_thread_state {     var ash: arm_state_hdr_t } ``` |
| To | ``` struct arm_unified_thread_state {     var ash: arm_state_hdr_t     init() } ``` |

Modified attribute_set [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct attribute_set {     var commonattr: attrgroup_t     var volattr: attrgroup_t     var dirattr: attrgroup_t     var fileattr: attrgroup_t     var forkattr: attrgroup_t } ``` |
| To | ``` struct attribute_set {     var commonattr: attrgroup_t     var volattr: attrgroup_t     var dirattr: attrgroup_t     var fileattr: attrgroup_t     var forkattr: attrgroup_t     init()     init(commonattr commonattr: attrgroup_t, volattr volattr: attrgroup_t, dirattr dirattr: attrgroup_t, fileattr fileattr: attrgroup_t, forkattr forkattr: attrgroup_t) } ``` |

Modified attrlist [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct attrlist {     var bitmapcount: u_short     var reserved: UInt16     var commonattr: attrgroup_t     var volattr: attrgroup_t     var dirattr: attrgroup_t     var fileattr: attrgroup_t     var forkattr: attrgroup_t } ``` |
| To | ``` struct attrlist {     var bitmapcount: u_short     var reserved: UInt16     var commonattr: attrgroup_t     var volattr: attrgroup_t     var dirattr: attrgroup_t     var fileattr: attrgroup_t     var forkattr: attrgroup_t     init()     init(bitmapcount bitmapcount: u_short, reserved reserved: UInt16, commonattr commonattr: attrgroup_t, volattr volattr: attrgroup_t, dirattr dirattr: attrgroup_t, fileattr fileattr: attrgroup_t, forkattr forkattr: attrgroup_t) } ``` |

Modified attrreference [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct attrreference {     var attr_dataoffset: Int32     var attr_length: UInt32 } ``` |
| To | ``` struct attrreference {     var attr_dataoffset: Int32     var attr_length: UInt32     init()     init(attr_dataoffset attr_dataoffset: Int32, attr_length attr_length: UInt32) } ``` |

Modified au_evclass_map [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct au_evclass_map {     var ec_number: au_event_t     var ec_class: au_class_t } ``` |
| To | ``` struct au_evclass_map {     var ec_number: au_event_t     var ec_class: au_class_t     init()     init(ec_number ec_number: au_event_t, ec_class ec_class: au_class_t) } ``` |

Modified au_mask [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct au_mask {     var am_success: UInt32     var am_failure: UInt32 } ``` |
| To | ``` struct au_mask {     var am_success: UInt32     var am_failure: UInt32     init()     init(am_success am_success: UInt32, am_failure am_failure: UInt32) } ``` |

Modified au_qctrl [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct au_qctrl {     var aq_hiwater: Int32     var aq_lowater: Int32     var aq_bufsz: Int32     var aq_delay: Int32     var aq_minfree: Int32 } ``` |
| To | ``` struct au_qctrl {     var aq_hiwater: Int32     var aq_lowater: Int32     var aq_bufsz: Int32     var aq_delay: Int32     var aq_minfree: Int32     init()     init(aq_hiwater aq_hiwater: Int32, aq_lowater aq_lowater: Int32, aq_bufsz aq_bufsz: Int32, aq_delay aq_delay: Int32, aq_minfree aq_minfree: Int32) } ``` |

Modified au_session [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct au_session {     var as_aia_p: UnsafeMutablePointer<auditinfo_addr_t>     var as_mask: au_mask_t } ``` |
| To | ``` struct au_session {     var as_aia_p: UnsafeMutablePointer<auditinfo_addr_t>     var as_mask: au_mask_t     init()     init(as_aia_p as_aia_p: UnsafeMutablePointer<auditinfo_addr_t>, as_mask as_mask: au_mask_t) } ``` |

Modified au_tid [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct au_tid {     var port: dev_t     var machine: UInt32 } ``` |
| To | ``` struct au_tid {     var port: dev_t     var machine: UInt32     init()     init(port port: dev_t, machine machine: UInt32) } ``` |

Modified au_tid_addr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct au_tid_addr {     var at_port: dev_t     var at_type: UInt32     var at_addr: (UInt32, UInt32, UInt32, UInt32) } ``` |
| To | ``` struct au_tid_addr {     var at_port: dev_t     var at_type: UInt32     var at_addr: (UInt32, UInt32, UInt32, UInt32)     init()     init(at_port at_port: dev_t, at_type at_type: UInt32, at_addr at_addr: (UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified audit_fstat [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct audit_fstat {     var af_filesz: UInt64     var af_currsz: UInt64 } ``` |
| To | ``` struct audit_fstat {     var af_filesz: UInt64     var af_currsz: UInt64     init()     init(af_filesz af_filesz: UInt64, af_currsz af_currsz: UInt64) } ``` |

Modified audit_stat [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct audit_stat {     var as_version: UInt32     var as_numevent: UInt32     var as_generated: Int32     var as_nonattrib: Int32     var as_kernel: Int32     var as_audit: Int32     var as_auditctl: Int32     var as_enqueue: Int32     var as_written: Int32     var as_wblocked: Int32     var as_rblocked: Int32     var as_dropped: Int32     var as_totalsize: Int32     var as_memused: UInt32 } ``` |
| To | ``` struct audit_stat {     var as_version: UInt32     var as_numevent: UInt32     var as_generated: Int32     var as_nonattrib: Int32     var as_kernel: Int32     var as_audit: Int32     var as_auditctl: Int32     var as_enqueue: Int32     var as_written: Int32     var as_wblocked: Int32     var as_rblocked: Int32     var as_dropped: Int32     var as_totalsize: Int32     var as_memused: UInt32     init()     init(as_version as_version: UInt32, as_numevent as_numevent: UInt32, as_generated as_generated: Int32, as_nonattrib as_nonattrib: Int32, as_kernel as_kernel: Int32, as_audit as_audit: Int32, as_auditctl as_auditctl: Int32, as_enqueue as_enqueue: Int32, as_written as_written: Int32, as_wblocked as_wblocked: Int32, as_rblocked as_rblocked: Int32, as_dropped as_dropped: Int32, as_totalsize as_totalsize: Int32, as_memused as_memused: UInt32) } ``` |

Modified audit_token_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct audit_token_t {     var val: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32) } ``` |
| To | ``` struct audit_token_t {     var val: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)     init()     init(val val: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified auditinfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct auditinfo {     var ai_auid: au_id_t     var ai_mask: au_mask_t     var ai_termid: au_tid_t     var ai_asid: au_asid_t } ``` |
| To | ``` struct auditinfo {     var ai_auid: au_id_t     var ai_mask: au_mask_t     var ai_termid: au_tid_t     var ai_asid: au_asid_t     init()     init(ai_auid ai_auid: au_id_t, ai_mask ai_mask: au_mask_t, ai_termid ai_termid: au_tid_t, ai_asid ai_asid: au_asid_t) } ``` |

Modified auditinfo_addr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct auditinfo_addr {     var ai_auid: au_id_t     var ai_mask: au_mask_t     var ai_termid: au_tid_addr_t     var ai_asid: au_asid_t     var ai_flags: au_asflgs_t } ``` |
| To | ``` struct auditinfo_addr {     var ai_auid: au_id_t     var ai_mask: au_mask_t     var ai_termid: au_tid_addr_t     var ai_asid: au_asid_t     var ai_flags: au_asflgs_t     init()     init(ai_auid ai_auid: au_id_t, ai_mask ai_mask: au_mask_t, ai_termid ai_termid: au_tid_addr_t, ai_asid ai_asid: au_asid_t, ai_flags ai_flags: au_asflgs_t) } ``` |

Modified auditpinfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct auditpinfo {     var ap_pid: pid_t     var ap_auid: au_id_t     var ap_mask: au_mask_t     var ap_termid: au_tid_t     var ap_asid: au_asid_t } ``` |
| To | ``` struct auditpinfo {     var ap_pid: pid_t     var ap_auid: au_id_t     var ap_mask: au_mask_t     var ap_termid: au_tid_t     var ap_asid: au_asid_t     init()     init(ap_pid ap_pid: pid_t, ap_auid ap_auid: au_id_t, ap_mask ap_mask: au_mask_t, ap_termid ap_termid: au_tid_t, ap_asid ap_asid: au_asid_t) } ``` |

Modified auditpinfo_addr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct auditpinfo_addr {     var ap_pid: pid_t     var ap_auid: au_id_t     var ap_mask: au_mask_t     var ap_termid: au_tid_addr_t     var ap_asid: au_asid_t     var ap_flags: au_asflgs_t } ``` |
| To | ``` struct auditpinfo_addr {     var ap_pid: pid_t     var ap_auid: au_id_t     var ap_mask: au_mask_t     var ap_termid: au_tid_addr_t     var ap_asid: au_asid_t     var ap_flags: au_asflgs_t     init()     init(ap_pid ap_pid: pid_t, ap_auid ap_auid: au_id_t, ap_mask ap_mask: au_mask_t, ap_termid ap_termid: au_tid_addr_t, ap_asid ap_asid: au_asid_t, ap_flags ap_flags: au_asflgs_t) } ``` |

Modified clockinfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct clockinfo {     var hz: Int32     var tick: Int32     var tickadj: Int32     var stathz: Int32     var profhz: Int32 } ``` |
| To | ``` struct clockinfo {     var hz: Int32     var tick: Int32     var tickadj: Int32     var stathz: Int32     var profhz: Int32     init()     init(hz hz: Int32, tick tick: Int32, tickadj tickadj: Int32, stathz stathz: Int32, profhz profhz: Int32) } ``` |

Modified cmsghdr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct cmsghdr {     var cmsg_len: socklen_t     var cmsg_level: Int32     var cmsg_type: Int32 } ``` |
| To | ``` struct cmsghdr {     var cmsg_len: socklen_t     var cmsg_level: Int32     var cmsg_type: Int32     init()     init(cmsg_len cmsg_len: socklen_t, cmsg_level cmsg_level: Int32, cmsg_type cmsg_type: Int32) } ``` |

Modified ctlname [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ctlname {     var ctl_name: UnsafeMutablePointer<Int8>     var ctl_type: Int32 } ``` |
| To | ``` struct ctlname {     var ctl_name: UnsafeMutablePointer<Int8>     var ctl_type: Int32     init()     init(ctl_name ctl_name: UnsafeMutablePointer<Int8>, ctl_type ctl_type: Int32) } ``` |

Modified datum [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct datum {     var dptr: UnsafeMutablePointer<Void>     var dsize: UInt } ``` |
| To | ``` struct datum {     var dptr: UnsafeMutablePointer<Void>     var dsize: Int     init()     init(dptr dptr: UnsafeMutablePointer<Void>, dsize dsize: Int) } ``` |

Modified datum.dsize

|  | Declaration |
| --- | --- |
| From | ``` var dsize: UInt ``` |
| To | ``` var dsize: Int ``` |

Modified diskextent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct diskextent {     var startblock: UInt32     var blockcount: UInt32 } ``` |
| To | ``` struct diskextent {     var startblock: UInt32     var blockcount: UInt32     init()     init(startblock startblock: UInt32, blockcount blockcount: UInt32) } ``` |

Modified div_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct div_t {     var quot: Int32     var rem: Int32 } ``` |
| To | ``` struct div_t {     var quot: Int32     var rem: Int32     init()     init(quot quot: Int32, rem rem: Int32) } ``` |

Modified dl_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dl_info {     var dli_fname: UnsafePointer<Int8>     var dli_fbase: UnsafeMutablePointer<Void>     var dli_sname: UnsafePointer<Int8>     var dli_saddr: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct dl_info {     var dli_fname: UnsafePointer<Int8>     var dli_fbase: UnsafeMutablePointer<Void>     var dli_sname: UnsafePointer<Int8>     var dli_saddr: UnsafeMutablePointer<Void>     init()     init(dli_fname dli_fname: UnsafePointer<Int8>, dli_fbase dli_fbase: UnsafeMutablePointer<Void>, dli_sname dli_sname: UnsafePointer<Int8>, dli_saddr dli_saddr: UnsafeMutablePointer<Void>) } ``` |

Modified dqblk [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dqblk {     var dqb_bhardlimit: UInt64     var dqb_bsoftlimit: UInt64     var dqb_curbytes: UInt64     var dqb_ihardlimit: UInt32     var dqb_isoftlimit: UInt32     var dqb_curinodes: UInt32     var dqb_btime: UInt32     var dqb_itime: UInt32     var dqb_id: UInt32     var dqb_spare: (UInt32, UInt32, UInt32, UInt32) } ``` |
| To | ``` struct dqblk {     var dqb_bhardlimit: UInt64     var dqb_bsoftlimit: UInt64     var dqb_curbytes: UInt64     var dqb_ihardlimit: UInt32     var dqb_isoftlimit: UInt32     var dqb_curinodes: UInt32     var dqb_btime: UInt32     var dqb_itime: UInt32     var dqb_id: UInt32     var dqb_spare: (UInt32, UInt32, UInt32, UInt32)     init()     init(dqb_bhardlimit dqb_bhardlimit: UInt64, dqb_bsoftlimit dqb_bsoftlimit: UInt64, dqb_curbytes dqb_curbytes: UInt64, dqb_ihardlimit dqb_ihardlimit: UInt32, dqb_isoftlimit dqb_isoftlimit: UInt32, dqb_curinodes dqb_curinodes: UInt32, dqb_btime dqb_btime: UInt32, dqb_itime dqb_itime: UInt32, dqb_id dqb_id: UInt32, dqb_spare dqb_spare: (UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified dqfilehdr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dqfilehdr {     var dqh_magic: UInt32     var dqh_version: UInt32     var dqh_maxentries: UInt32     var dqh_entrycnt: UInt32     var dqh_flags: UInt32     var dqh_chktime: UInt32     var dqh_btime: UInt32     var dqh_itime: UInt32     var dqh_string: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var dqh_spare: (UInt32, UInt32, UInt32, UInt32) } ``` |
| To | ``` struct dqfilehdr {     var dqh_magic: UInt32     var dqh_version: UInt32     var dqh_maxentries: UInt32     var dqh_entrycnt: UInt32     var dqh_flags: UInt32     var dqh_chktime: UInt32     var dqh_btime: UInt32     var dqh_itime: UInt32     var dqh_string: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var dqh_spare: (UInt32, UInt32, UInt32, UInt32)     init()     init(dqh_magic dqh_magic: UInt32, dqh_version dqh_version: UInt32, dqh_maxentries dqh_maxentries: UInt32, dqh_entrycnt dqh_entrycnt: UInt32, dqh_flags dqh_flags: UInt32, dqh_chktime dqh_chktime: UInt32, dqh_btime dqh_btime: UInt32, dqh_itime dqh_itime: UInt32, dqh_string dqh_string: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), dqh_spare dqh_spare: (UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified entry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct entry {     var key: UnsafeMutablePointer<Int8>     var data: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct entry {     var key: UnsafeMutablePointer<Int8>     var data: UnsafeMutablePointer<Void>     init()     init(key key: UnsafeMutablePointer<Int8>, data data: UnsafeMutablePointer<Void>) } ``` |

Modified exception [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct exception {     var type: Int32     var name: UnsafeMutablePointer<Int8>     var arg1: Double     var arg2: Double     var retval: Double } ``` |
| To | ``` struct exception {     var type: Int32     var name: UnsafeMutablePointer<Int8>     var arg1: Double     var arg2: Double     var retval: Double     init()     init(type type: Int32, name name: UnsafeMutablePointer<Int8>, arg1 arg1: Double, arg2 arg2: Double, retval retval: Double) } ``` |

Modified extern_proc [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct extern_proc {     var p_vmspace: UnsafeMutablePointer<vmspace>     var p_sigacts: COpaquePointer     var p_flag: Int32     var p_stat: Int8     var p_pid: pid_t     var p_oppid: pid_t     var p_dupfd: Int32     var user_stack: caddr_t     var exit_thread: UnsafeMutablePointer<Void>     var p_debugger: Int32     var sigwait: boolean_t     var p_estcpu: u_int     var p_cpticks: Int32     var p_pctcpu: fixpt_t     var p_wchan: UnsafeMutablePointer<Void>     var p_wmesg: UnsafeMutablePointer<Int8>     var p_swtime: u_int     var p_slptime: u_int     var p_realtimer: itimerval     var p_rtime: timeval     var p_uticks: u_quad_t     var p_sticks: u_quad_t     var p_iticks: u_quad_t     var p_traceflag: Int32     var p_tracep: COpaquePointer     var p_siglist: Int32     var p_textvp: COpaquePointer     var p_holdcnt: Int32     var p_sigmask: sigset_t     var p_sigignore: sigset_t     var p_sigcatch: sigset_t     var p_priority: u_char     var p_usrpri: u_char     var p_nice: Int8     var p_comm: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var p_pgrp: COpaquePointer     var p_addr: COpaquePointer     var p_xstat: u_short     var p_acflag: u_short     var p_ru: UnsafeMutablePointer<rusage> } ``` |
| To | ``` struct extern_proc {     var p_vmspace: UnsafeMutablePointer<vmspace>     var p_sigacts: COpaquePointer     var p_flag: Int32     var p_stat: Int8     var p_pid: pid_t     var p_oppid: pid_t     var p_dupfd: Int32     var user_stack: caddr_t     var exit_thread: UnsafeMutablePointer<Void>     var p_debugger: Int32     var sigwait: boolean_t     var p_estcpu: u_int     var p_cpticks: Int32     var p_pctcpu: fixpt_t     var p_wchan: UnsafeMutablePointer<Void>     var p_wmesg: UnsafeMutablePointer<Int8>     var p_swtime: u_int     var p_slptime: u_int     var p_realtimer: itimerval     var p_rtime: timeval     var p_uticks: u_quad_t     var p_sticks: u_quad_t     var p_iticks: u_quad_t     var p_traceflag: Int32     var p_tracep: COpaquePointer     var p_siglist: Int32     var p_textvp: COpaquePointer     var p_holdcnt: Int32     var p_sigmask: sigset_t     var p_sigignore: sigset_t     var p_sigcatch: sigset_t     var p_priority: u_char     var p_usrpri: u_char     var p_nice: Int8     var p_comm: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var p_pgrp: COpaquePointer     var p_addr: COpaquePointer     var p_xstat: u_short     var p_acflag: u_short     var p_ru: UnsafeMutablePointer<rusage>     init() } ``` |

Modified fbootstraptransfer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fbootstraptransfer {     var fbt_offset: off_t     var fbt_length: UInt     var fbt_buffer: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct fbootstraptransfer {     var fbt_offset: off_t     var fbt_length: Int     var fbt_buffer: UnsafeMutablePointer<Void>     init()     init(fbt_offset fbt_offset: off_t, fbt_length fbt_length: Int, fbt_buffer fbt_buffer: UnsafeMutablePointer<Void>) } ``` |

Modified fbootstraptransfer.fbt_length

|  | Declaration |
| --- | --- |
| From | ``` var fbt_length: UInt ``` |
| To | ``` var fbt_length: Int ``` |

Modified fcodeblobs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fcodeblobs {     var f_cd_hash: UnsafeMutablePointer<Void>     var f_hash_size: UInt     var f_cd_buffer: UnsafeMutablePointer<Void>     var f_cd_size: UInt     var f_out_size: UnsafeMutablePointer<UInt32>     var f_arch: Int32     var __padding: Int32 } ``` |
| To | ``` struct fcodeblobs {     var f_cd_hash: UnsafeMutablePointer<Void>     var f_hash_size: Int     var f_cd_buffer: UnsafeMutablePointer<Void>     var f_cd_size: Int     var f_out_size: UnsafeMutablePointer<UInt32>     var f_arch: Int32     var __padding: Int32     init()     init(f_cd_hash f_cd_hash: UnsafeMutablePointer<Void>, f_hash_size f_hash_size: Int, f_cd_buffer f_cd_buffer: UnsafeMutablePointer<Void>, f_cd_size f_cd_size: Int, f_out_size f_out_size: UnsafeMutablePointer<UInt32>, f_arch f_arch: Int32, __padding __padding: Int32) } ``` |

Modified fcodeblobs.f_cd_size

|  | Declaration |
| --- | --- |
| From | ``` var f_cd_size: UInt ``` |
| To | ``` var f_cd_size: Int ``` |

Modified fcodeblobs.f_hash_size

|  | Declaration |
| --- | --- |
| From | ``` var f_hash_size: UInt ``` |
| To | ``` var f_hash_size: Int ``` |

Modified fd_set [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fd_set {     var fds_bits: (__int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t) } ``` |
| To | ``` struct fd_set {     var fds_bits: (__int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t)     init()     init(fds_bits fds_bits: (__int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t, __int32_t)) } ``` |

Modified fenv_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fenv_t {     var __fpscr: UInt32     var __reserved0: UInt32     var __reserved1: UInt32     var __reserved2: UInt32 } ``` |
| To | ``` struct fenv_t {     var __fpscr: UInt32     var __reserved0: UInt32     var __reserved1: UInt32     var __reserved2: UInt32     init()     init(__fpscr __fpscr: UInt32, __reserved0 __reserved0: UInt32, __reserved1 __reserved1: UInt32, __reserved2 __reserved2: UInt32) } ``` |

Modified fhandle [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fhandle {     var fh_len: Int32     var fh_data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct fhandle {     var fh_len: Int32     var fh_data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(fh_len fh_len: Int32, fh_data fh_data: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified flock [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct flock {     var l_start: off_t     var l_len: off_t     var l_pid: pid_t     var l_type: Int16     var l_whence: Int16 } ``` |
| To | ``` struct flock {     var l_start: off_t     var l_len: off_t     var l_pid: pid_t     var l_type: Int16     var l_whence: Int16     init()     init(l_start l_start: off_t, l_len l_len: off_t, l_pid l_pid: pid_t, l_type l_type: Int16, l_whence l_whence: Int16) } ``` |

Modified flocktimeout [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct flocktimeout {     var fl: flock     var timeout: timespec } ``` |
| To | ``` struct flocktimeout {     var fl: flock     var timeout: timespec     init()     init(fl fl: flock, timeout timeout: timespec) } ``` |

Modified fsid [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fsid {     var val: (Int32, Int32) } ``` |
| To | ``` struct fsid {     var val: (Int32, Int32)     init()     init(val val: (Int32, Int32)) } ``` |

Modified fsignatures [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fsignatures {     var fs_file_start: off_t     var fs_blob_start: UnsafeMutablePointer<Void>     var fs_blob_size: UInt } ``` |
| To | ``` struct fsignatures {     var fs_file_start: off_t     var fs_blob_start: UnsafeMutablePointer<Void>     var fs_blob_size: Int     init()     init(fs_file_start fs_file_start: off_t, fs_blob_start fs_blob_start: UnsafeMutablePointer<Void>, fs_blob_size fs_blob_size: Int) } ``` |

Modified fsignatures.fs_blob_size

|  | Declaration |
| --- | --- |
| From | ``` var fs_blob_size: UInt ``` |
| To | ``` var fs_blob_size: Int ``` |

Modified fsobj_id [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fsobj_id {     var fid_objno: UInt32     var fid_generation: UInt32 } ``` |
| To | ``` struct fsobj_id {     var fid_objno: UInt32     var fid_generation: UInt32     init()     init(fid_objno fid_objno: UInt32, fid_generation fid_generation: UInt32) } ``` |

Modified fssearchblock [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fssearchblock {     var returnattrs: UnsafeMutablePointer<attrlist>     var returnbuffer: UnsafeMutablePointer<Void>     var returnbuffersize: UInt     var maxmatches: u_long     var timelimit: timeval     var searchparams1: UnsafeMutablePointer<Void>     var sizeofsearchparams1: UInt     var searchparams2: UnsafeMutablePointer<Void>     var sizeofsearchparams2: UInt     var searchattrs: attrlist } ``` |
| To | ``` struct fssearchblock {     var returnattrs: UnsafeMutablePointer<attrlist>     var returnbuffer: UnsafeMutablePointer<Void>     var returnbuffersize: Int     var maxmatches: u_long     var timelimit: timeval     var searchparams1: UnsafeMutablePointer<Void>     var sizeofsearchparams1: Int     var searchparams2: UnsafeMutablePointer<Void>     var sizeofsearchparams2: Int     var searchattrs: attrlist     init()     init(returnattrs returnattrs: UnsafeMutablePointer<attrlist>, returnbuffer returnbuffer: UnsafeMutablePointer<Void>, returnbuffersize returnbuffersize: Int, maxmatches maxmatches: u_long, timelimit timelimit: timeval, searchparams1 searchparams1: UnsafeMutablePointer<Void>, sizeofsearchparams1 sizeofsearchparams1: Int, searchparams2 searchparams2: UnsafeMutablePointer<Void>, sizeofsearchparams2 sizeofsearchparams2: Int, searchattrs searchattrs: attrlist) } ``` |

Modified fssearchblock.returnbuffersize

|  | Declaration |
| --- | --- |
| From | ``` var returnbuffersize: UInt ``` |
| To | ``` var returnbuffersize: Int ``` |

Modified fssearchblock.sizeofsearchparams1

|  | Declaration |
| --- | --- |
| From | ``` var sizeofsearchparams1: UInt ``` |
| To | ``` var sizeofsearchparams1: Int ``` |

Modified fssearchblock.sizeofsearchparams2

|  | Declaration |
| --- | --- |
| From | ``` var sizeofsearchparams2: UInt ``` |
| To | ``` var sizeofsearchparams2: Int ``` |

Modified fstore [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fstore {     var fst_flags: UInt32     var fst_posmode: Int32     var fst_offset: off_t     var fst_length: off_t     var fst_bytesalloc: off_t } ``` |
| To | ``` struct fstore {     var fst_flags: UInt32     var fst_posmode: Int32     var fst_offset: off_t     var fst_length: off_t     var fst_bytesalloc: off_t     init()     init(fst_flags fst_flags: UInt32, fst_posmode fst_posmode: Int32, fst_offset fst_offset: off_t, fst_length fst_length: off_t, fst_bytesalloc fst_bytesalloc: off_t) } ``` |

Modified glob_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct glob_t {     var gl_pathc: UInt     var gl_matchc: Int32     var gl_offs: UInt     var gl_flags: Int32     var gl_pathv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var gl_closedir: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>     var gl_readdir: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<dirent>)>     var gl_opendir: CFunctionPointer<((UnsafePointer<Int8>) -> UnsafeMutablePointer<Void>)>     var gl_lstat: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<stat>) -> Int32)>     var gl_stat: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<stat>) -> Int32)> } ``` |
| To | ``` struct glob_t {     var gl_pathc: Int     var gl_matchc: Int32     var gl_offs: Int     var gl_flags: Int32     var gl_pathv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var gl_closedir: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>     var gl_readdir: CFunctionPointer<((UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<dirent>)>     var gl_opendir: CFunctionPointer<((UnsafePointer<Int8>) -> UnsafeMutablePointer<Void>)>     var gl_lstat: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<stat>) -> Int32)>     var gl_stat: CFunctionPointer<((UnsafePointer<Int8>, UnsafeMutablePointer<stat>) -> Int32)>     init() } ``` |

Modified glob_t.gl_offs

|  | Declaration |
| --- | --- |
| From | ``` var gl_offs: UInt ``` |
| To | ``` var gl_offs: Int ``` |

Modified glob_t.gl_pathc

|  | Declaration |
| --- | --- |
| From | ``` var gl_pathc: UInt ``` |
| To | ``` var gl_pathc: Int ``` |

Modified gpu_energy_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gpu_energy_data {     var task_gpu_utilisation: UInt64     var task_gpu_stat_reserved0: UInt64     var task_gpu_stat_reserved1: UInt64     var task_gpu_stat_reserved2: UInt64 } ``` |
| To | ``` struct gpu_energy_data {     var task_gpu_utilisation: UInt64     var task_gpu_stat_reserved0: UInt64     var task_gpu_stat_reserved1: UInt64     var task_gpu_stat_reserved2: UInt64     init()     init(task_gpu_utilisation task_gpu_utilisation: UInt64, task_gpu_stat_reserved0 task_gpu_stat_reserved0: UInt64, task_gpu_stat_reserved1 task_gpu_stat_reserved1: UInt64, task_gpu_stat_reserved2 task_gpu_stat_reserved2: UInt64) } ``` |

Modified group [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct group {     var gr_name: UnsafeMutablePointer<Int8>     var gr_passwd: UnsafeMutablePointer<Int8>     var gr_gid: gid_t     var gr_mem: UnsafeMutablePointer<UnsafeMutablePointer<Int8>> } ``` |
| To | ``` struct group {     var gr_name: UnsafeMutablePointer<Int8>     var gr_passwd: UnsafeMutablePointer<Int8>     var gr_gid: gid_t     var gr_mem: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     init()     init(gr_name gr_name: UnsafeMutablePointer<Int8>, gr_passwd gr_passwd: UnsafeMutablePointer<Int8>, gr_gid gr_gid: gid_t, gr_mem gr_mem: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) } ``` |

Modified group_req [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct group_req {     var gr_interface: UInt32     var gr_group: sockaddr_storage } ``` |
| To | ``` struct group_req {     var gr_interface: UInt32     var gr_group: sockaddr_storage     init()     init(gr_interface gr_interface: UInt32, gr_group gr_group: sockaddr_storage) } ``` |

Modified group_source_req [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct group_source_req {     var gsr_interface: UInt32     var gsr_group: sockaddr_storage     var gsr_source: sockaddr_storage } ``` |
| To | ``` struct group_source_req {     var gsr_interface: UInt32     var gsr_group: sockaddr_storage     var gsr_source: sockaddr_storage     init()     init(gsr_interface gsr_interface: UInt32, gsr_group gsr_group: sockaddr_storage, gsr_source gsr_source: sockaddr_storage) } ``` |

Modified guid_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct guid_t {     var g_guid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct guid_t {     var g_guid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(g_guid g_guid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified hash_info_bucket [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct hash_info_bucket {     var hib_count: natural_t } ``` |
| To | ``` struct hash_info_bucket {     var hib_count: natural_t     init()     init(hib_count hib_count: natural_t) } ``` |

Modified host_basic_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct host_basic_info {     var max_cpus: integer_t     var avail_cpus: integer_t     var memory_size: natural_t     var cpu_type: cpu_type_t     var cpu_subtype: cpu_subtype_t     var cpu_threadtype: cpu_threadtype_t     var physical_cpu: integer_t     var physical_cpu_max: integer_t     var logical_cpu: integer_t     var logical_cpu_max: integer_t     var max_mem: UInt64 } ``` |
| To | ``` struct host_basic_info {     var max_cpus: integer_t     var avail_cpus: integer_t     var memory_size: natural_t     var cpu_type: cpu_type_t     var cpu_subtype: cpu_subtype_t     var cpu_threadtype: cpu_threadtype_t     var physical_cpu: integer_t     var physical_cpu_max: integer_t     var logical_cpu: integer_t     var logical_cpu_max: integer_t     var max_mem: UInt64     init()     init(max_cpus max_cpus: integer_t, avail_cpus avail_cpus: integer_t, memory_size memory_size: natural_t, cpu_type cpu_type: cpu_type_t, cpu_subtype cpu_subtype: cpu_subtype_t, cpu_threadtype cpu_threadtype: cpu_threadtype_t, physical_cpu physical_cpu: integer_t, physical_cpu_max physical_cpu_max: integer_t, logical_cpu logical_cpu: integer_t, logical_cpu_max logical_cpu_max: integer_t, max_mem max_mem: UInt64) } ``` |

Modified host_cpu_load_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct host_cpu_load_info {     var cpu_ticks: (natural_t, natural_t, natural_t, natural_t) } ``` |
| To | ``` struct host_cpu_load_info {     var cpu_ticks: (natural_t, natural_t, natural_t, natural_t)     init()     init(cpu_ticks cpu_ticks: (natural_t, natural_t, natural_t, natural_t)) } ``` |

Modified host_load_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct host_load_info {     var avenrun: (integer_t, integer_t, integer_t)     var mach_factor: (integer_t, integer_t, integer_t) } ``` |
| To | ``` struct host_load_info {     var avenrun: (integer_t, integer_t, integer_t)     var mach_factor: (integer_t, integer_t, integer_t)     init()     init(avenrun avenrun: (integer_t, integer_t, integer_t), mach_factor mach_factor: (integer_t, integer_t, integer_t)) } ``` |

Modified host_priority_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct host_priority_info {     var kernel_priority: integer_t     var system_priority: integer_t     var server_priority: integer_t     var user_priority: integer_t     var depress_priority: integer_t     var idle_priority: integer_t     var minimum_priority: integer_t     var maximum_priority: integer_t } ``` |
| To | ``` struct host_priority_info {     var kernel_priority: integer_t     var system_priority: integer_t     var server_priority: integer_t     var user_priority: integer_t     var depress_priority: integer_t     var idle_priority: integer_t     var minimum_priority: integer_t     var maximum_priority: integer_t     init()     init(kernel_priority kernel_priority: integer_t, system_priority system_priority: integer_t, server_priority server_priority: integer_t, user_priority user_priority: integer_t, depress_priority depress_priority: integer_t, idle_priority idle_priority: integer_t, minimum_priority minimum_priority: integer_t, maximum_priority maximum_priority: integer_t) } ``` |

Modified host_sched_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct host_sched_info {     var min_timeout: integer_t     var min_quantum: integer_t } ``` |
| To | ``` struct host_sched_info {     var min_timeout: integer_t     var min_quantum: integer_t     init()     init(min_timeout min_timeout: integer_t, min_quantum min_quantum: integer_t) } ``` |

Modified hostent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct hostent {     var h_name: UnsafeMutablePointer<Int8>     var h_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var h_addrtype: Int32     var h_length: Int32     var h_addr_list: UnsafeMutablePointer<UnsafeMutablePointer<Int8>> } ``` |
| To | ``` struct hostent {     var h_name: UnsafeMutablePointer<Int8>     var h_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var h_addrtype: Int32     var h_length: Int32     var h_addr_list: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     init()     init(h_name h_name: UnsafeMutablePointer<Int8>, h_aliases h_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, h_addrtype h_addrtype: Int32, h_length h_length: Int32, h_addr_list h_addr_list: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) } ``` |

Modified iconv_fallbacks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct iconv_fallbacks {     var mb_to_uc_fallback: iconv_unicode_mb_to_uc_fallback     var uc_to_mb_fallback: iconv_unicode_uc_to_mb_fallback     var mb_to_wc_fallback: iconv_wchar_mb_to_wc_fallback     var wc_to_mb_fallback: iconv_wchar_wc_to_mb_fallback     var data: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct iconv_fallbacks {     var mb_to_uc_fallback: iconv_unicode_mb_to_uc_fallback     var uc_to_mb_fallback: iconv_unicode_uc_to_mb_fallback     var mb_to_wc_fallback: iconv_wchar_mb_to_wc_fallback     var wc_to_mb_fallback: iconv_wchar_wc_to_mb_fallback     var data: UnsafeMutablePointer<Void>     init()     init(mb_to_uc_fallback mb_to_uc_fallback: iconv_unicode_mb_to_uc_fallback, uc_to_mb_fallback uc_to_mb_fallback: iconv_unicode_uc_to_mb_fallback, mb_to_wc_fallback mb_to_wc_fallback: iconv_wchar_mb_to_wc_fallback, wc_to_mb_fallback wc_to_mb_fallback: iconv_wchar_wc_to_mb_fallback, data data: UnsafeMutablePointer<Void>) } ``` |

Modified iconv_hooks [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct iconv_hooks {     var uc_hook: iconv_unicode_char_hook     var wc_hook: iconv_wide_char_hook     var data: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct iconv_hooks {     var uc_hook: iconv_unicode_char_hook     var wc_hook: iconv_wide_char_hook     var data: UnsafeMutablePointer<Void>     init()     init(uc_hook uc_hook: iconv_unicode_char_hook, wc_hook wc_hook: iconv_wide_char_hook, data data: UnsafeMutablePointer<Void>) } ``` |

Modified if_clonereq [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct if_clonereq {     var ifcr_total: Int32     var ifcr_count: Int32     var ifcr_buffer: UnsafeMutablePointer<Int8> } ``` |
| To | ``` struct if_clonereq {     var ifcr_total: Int32     var ifcr_count: Int32     var ifcr_buffer: UnsafeMutablePointer<Int8>     init()     init(ifcr_total ifcr_total: Int32, ifcr_count ifcr_count: Int32, ifcr_buffer ifcr_buffer: UnsafeMutablePointer<Int8>) } ``` |

Modified if_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct if_data {     var ifi_type: u_char     var ifi_typelen: u_char     var ifi_physical: u_char     var ifi_addrlen: u_char     var ifi_hdrlen: u_char     var ifi_recvquota: u_char     var ifi_xmitquota: u_char     var ifi_unused1: u_char     var ifi_mtu: UInt32     var ifi_metric: UInt32     var ifi_baudrate: UInt32     var ifi_ipackets: UInt32     var ifi_ierrors: UInt32     var ifi_opackets: UInt32     var ifi_oerrors: UInt32     var ifi_collisions: UInt32     var ifi_ibytes: UInt32     var ifi_obytes: UInt32     var ifi_imcasts: UInt32     var ifi_omcasts: UInt32     var ifi_iqdrops: UInt32     var ifi_noproto: UInt32     var ifi_recvtiming: UInt32     var ifi_xmittiming: UInt32     var ifi_lastchange: timeval     var ifi_unused2: UInt32     var ifi_hwassist: UInt32     var ifi_reserved1: UInt32     var ifi_reserved2: UInt32 } ``` |
| To | ``` struct if_data {     var ifi_type: u_char     var ifi_typelen: u_char     var ifi_physical: u_char     var ifi_addrlen: u_char     var ifi_hdrlen: u_char     var ifi_recvquota: u_char     var ifi_xmitquota: u_char     var ifi_unused1: u_char     var ifi_mtu: UInt32     var ifi_metric: UInt32     var ifi_baudrate: UInt32     var ifi_ipackets: UInt32     var ifi_ierrors: UInt32     var ifi_opackets: UInt32     var ifi_oerrors: UInt32     var ifi_collisions: UInt32     var ifi_ibytes: UInt32     var ifi_obytes: UInt32     var ifi_imcasts: UInt32     var ifi_omcasts: UInt32     var ifi_iqdrops: UInt32     var ifi_noproto: UInt32     var ifi_recvtiming: UInt32     var ifi_xmittiming: UInt32     var ifi_lastchange: timeval     var ifi_unused2: UInt32     var ifi_hwassist: UInt32     var ifi_reserved1: UInt32     var ifi_reserved2: UInt32     init()     init(ifi_type ifi_type: u_char, ifi_typelen ifi_typelen: u_char, ifi_physical ifi_physical: u_char, ifi_addrlen ifi_addrlen: u_char, ifi_hdrlen ifi_hdrlen: u_char, ifi_recvquota ifi_recvquota: u_char, ifi_xmitquota ifi_xmitquota: u_char, ifi_unused1 ifi_unused1: u_char, ifi_mtu ifi_mtu: UInt32, ifi_metric ifi_metric: UInt32, ifi_baudrate ifi_baudrate: UInt32, ifi_ipackets ifi_ipackets: UInt32, ifi_ierrors ifi_ierrors: UInt32, ifi_opackets ifi_opackets: UInt32, ifi_oerrors ifi_oerrors: UInt32, ifi_collisions ifi_collisions: UInt32, ifi_ibytes ifi_ibytes: UInt32, ifi_obytes ifi_obytes: UInt32, ifi_imcasts ifi_imcasts: UInt32, ifi_omcasts ifi_omcasts: UInt32, ifi_iqdrops ifi_iqdrops: UInt32, ifi_noproto ifi_noproto: UInt32, ifi_recvtiming ifi_recvtiming: UInt32, ifi_xmittiming ifi_xmittiming: UInt32, ifi_lastchange ifi_lastchange: timeval, ifi_unused2 ifi_unused2: UInt32, ifi_hwassist ifi_hwassist: UInt32, ifi_reserved1 ifi_reserved1: UInt32, ifi_reserved2 ifi_reserved2: UInt32) } ``` |

Modified if_data64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct if_data64 {     var ifi_type: u_char     var ifi_typelen: u_char     var ifi_physical: u_char     var ifi_addrlen: u_char     var ifi_hdrlen: u_char     var ifi_recvquota: u_char     var ifi_xmitquota: u_char     var ifi_unused1: u_char     var ifi_mtu: UInt32     var ifi_metric: UInt32     var ifi_baudrate: UInt64     var ifi_ipackets: UInt64     var ifi_ierrors: UInt64     var ifi_opackets: UInt64     var ifi_oerrors: UInt64     var ifi_collisions: UInt64     var ifi_ibytes: UInt64     var ifi_obytes: UInt64     var ifi_imcasts: UInt64     var ifi_omcasts: UInt64     var ifi_iqdrops: UInt64     var ifi_noproto: UInt64     var ifi_recvtiming: UInt32     var ifi_xmittiming: UInt32     var ifi_lastchange: timeval } ``` |
| To | ``` struct if_data64 {     var ifi_type: u_char     var ifi_typelen: u_char     var ifi_physical: u_char     var ifi_addrlen: u_char     var ifi_hdrlen: u_char     var ifi_recvquota: u_char     var ifi_xmitquota: u_char     var ifi_unused1: u_char     var ifi_mtu: UInt32     var ifi_metric: UInt32     var ifi_baudrate: UInt64     var ifi_ipackets: UInt64     var ifi_ierrors: UInt64     var ifi_opackets: UInt64     var ifi_oerrors: UInt64     var ifi_collisions: UInt64     var ifi_ibytes: UInt64     var ifi_obytes: UInt64     var ifi_imcasts: UInt64     var ifi_omcasts: UInt64     var ifi_iqdrops: UInt64     var ifi_noproto: UInt64     var ifi_recvtiming: UInt32     var ifi_xmittiming: UInt32     var ifi_lastchange: timeval     init()     init(ifi_type ifi_type: u_char, ifi_typelen ifi_typelen: u_char, ifi_physical ifi_physical: u_char, ifi_addrlen ifi_addrlen: u_char, ifi_hdrlen ifi_hdrlen: u_char, ifi_recvquota ifi_recvquota: u_char, ifi_xmitquota ifi_xmitquota: u_char, ifi_unused1 ifi_unused1: u_char, ifi_mtu ifi_mtu: UInt32, ifi_metric ifi_metric: UInt32, ifi_baudrate ifi_baudrate: UInt64, ifi_ipackets ifi_ipackets: UInt64, ifi_ierrors ifi_ierrors: UInt64, ifi_opackets ifi_opackets: UInt64, ifi_oerrors ifi_oerrors: UInt64, ifi_collisions ifi_collisions: UInt64, ifi_ibytes ifi_ibytes: UInt64, ifi_obytes ifi_obytes: UInt64, ifi_imcasts ifi_imcasts: UInt64, ifi_omcasts ifi_omcasts: UInt64, ifi_iqdrops ifi_iqdrops: UInt64, ifi_noproto ifi_noproto: UInt64, ifi_recvtiming ifi_recvtiming: UInt32, ifi_xmittiming ifi_xmittiming: UInt32, ifi_lastchange ifi_lastchange: timeval) } ``` |

Modified if_msghdr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct if_msghdr {     var ifm_msglen: UInt16     var ifm_version: UInt8     var ifm_type: UInt8     var ifm_addrs: Int32     var ifm_flags: Int32     var ifm_index: UInt16     var ifm_data: if_data } ``` |
| To | ``` struct if_msghdr {     var ifm_msglen: UInt16     var ifm_version: UInt8     var ifm_type: UInt8     var ifm_addrs: Int32     var ifm_flags: Int32     var ifm_index: UInt16     var ifm_data: if_data     init()     init(ifm_msglen ifm_msglen: UInt16, ifm_version ifm_version: UInt8, ifm_type ifm_type: UInt8, ifm_addrs ifm_addrs: Int32, ifm_flags ifm_flags: Int32, ifm_index ifm_index: UInt16, ifm_data ifm_data: if_data) } ``` |

Modified if_msghdr2 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct if_msghdr2 {     var ifm_msglen: u_short     var ifm_version: u_char     var ifm_type: u_char     var ifm_addrs: Int32     var ifm_flags: Int32     var ifm_index: u_short     var ifm_snd_len: Int32     var ifm_snd_maxlen: Int32     var ifm_snd_drops: Int32     var ifm_timer: Int32     var ifm_data: if_data64 } ``` |
| To | ``` struct if_msghdr2 {     var ifm_msglen: u_short     var ifm_version: u_char     var ifm_type: u_char     var ifm_addrs: Int32     var ifm_flags: Int32     var ifm_index: u_short     var ifm_snd_len: Int32     var ifm_snd_maxlen: Int32     var ifm_snd_drops: Int32     var ifm_timer: Int32     var ifm_data: if_data64     init()     init(ifm_msglen ifm_msglen: u_short, ifm_version ifm_version: u_char, ifm_type ifm_type: u_char, ifm_addrs ifm_addrs: Int32, ifm_flags ifm_flags: Int32, ifm_index ifm_index: u_short, ifm_snd_len ifm_snd_len: Int32, ifm_snd_maxlen ifm_snd_maxlen: Int32, ifm_snd_drops ifm_snd_drops: Int32, ifm_timer ifm_timer: Int32, ifm_data ifm_data: if_data64) } ``` |

Modified if_nameindex [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct if_nameindex {     var if_index: UInt32     var if_name: UnsafeMutablePointer<Int8> } ``` |
| To | ``` struct if_nameindex {     var if_index: UInt32     var if_name: UnsafeMutablePointer<Int8>     init()     init(if_index if_index: UInt32, if_name if_name: UnsafeMutablePointer<Int8>) } ``` |

Modified ifa_msghdr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifa_msghdr {     var ifam_msglen: UInt16     var ifam_version: UInt8     var ifam_type: UInt8     var ifam_addrs: Int32     var ifam_flags: Int32     var ifam_index: UInt16     var ifam_metric: Int32 } ``` |
| To | ``` struct ifa_msghdr {     var ifam_msglen: UInt16     var ifam_version: UInt8     var ifam_type: UInt8     var ifam_addrs: Int32     var ifam_flags: Int32     var ifam_index: UInt16     var ifam_metric: Int32     init()     init(ifam_msglen ifam_msglen: UInt16, ifam_version ifam_version: UInt8, ifam_type ifam_type: UInt8, ifam_addrs ifam_addrs: Int32, ifam_flags ifam_flags: Int32, ifam_index ifam_index: UInt16, ifam_metric ifam_metric: Int32) } ``` |

Modified ifaliasreq [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifaliasreq {     var ifra_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ifra_addr: sockaddr     var ifra_broadaddr: sockaddr     var ifra_mask: sockaddr } ``` |
| To | ``` struct ifaliasreq {     var ifra_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ifra_addr: sockaddr     var ifra_broadaddr: sockaddr     var ifra_mask: sockaddr     init()     init(ifra_name ifra_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifra_addr ifra_addr: sockaddr, ifra_broadaddr ifra_broadaddr: sockaddr, ifra_mask ifra_mask: sockaddr) } ``` |

Modified ifconf [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifconf {     var ifc_len: Int32 } ``` |
| To | ``` struct ifconf {     var ifc_len: Int32     init() } ``` |

Modified ifdevmtu [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifdevmtu {     var ifdm_current: Int32     var ifdm_min: Int32     var ifdm_max: Int32 } ``` |
| To | ``` struct ifdevmtu {     var ifdm_current: Int32     var ifdm_min: Int32     var ifdm_max: Int32     init()     init(ifdm_current ifdm_current: Int32, ifdm_min ifdm_min: Int32, ifdm_max ifdm_max: Int32) } ``` |

Modified ifdrv [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifdrv {     var ifd_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ifd_cmd: UInt     var ifd_len: UInt     var ifd_data: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct ifdrv {     var ifd_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ifd_cmd: UInt     var ifd_len: Int     var ifd_data: UnsafeMutablePointer<Void>     init()     init(ifd_name ifd_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifd_cmd ifd_cmd: UInt, ifd_len ifd_len: Int, ifd_data ifd_data: UnsafeMutablePointer<Void>) } ``` |

Modified ifdrv.ifd_len

|  | Declaration |
| --- | --- |
| From | ``` var ifd_len: UInt ``` |
| To | ``` var ifd_len: Int ``` |

Modified ifkpi [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifkpi {     var ifk_module_id: UInt32     var ifk_type: UInt32 } ``` |
| To | ``` struct ifkpi {     var ifk_module_id: UInt32     var ifk_type: UInt32     init() } ``` |

Modified ifma_msghdr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifma_msghdr {     var ifmam_msglen: UInt16     var ifmam_version: UInt8     var ifmam_type: UInt8     var ifmam_addrs: Int32     var ifmam_flags: Int32     var ifmam_index: UInt16 } ``` |
| To | ``` struct ifma_msghdr {     var ifmam_msglen: UInt16     var ifmam_version: UInt8     var ifmam_type: UInt8     var ifmam_addrs: Int32     var ifmam_flags: Int32     var ifmam_index: UInt16     init()     init(ifmam_msglen ifmam_msglen: UInt16, ifmam_version ifmam_version: UInt8, ifmam_type ifmam_type: UInt8, ifmam_addrs ifmam_addrs: Int32, ifmam_flags ifmam_flags: Int32, ifmam_index ifmam_index: UInt16) } ``` |

Modified ifma_msghdr2 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifma_msghdr2 {     var ifmam_msglen: u_short     var ifmam_version: u_char     var ifmam_type: u_char     var ifmam_addrs: Int32     var ifmam_flags: Int32     var ifmam_index: u_short     var ifmam_refcount: Int32 } ``` |
| To | ``` struct ifma_msghdr2 {     var ifmam_msglen: u_short     var ifmam_version: u_char     var ifmam_type: u_char     var ifmam_addrs: Int32     var ifmam_flags: Int32     var ifmam_index: u_short     var ifmam_refcount: Int32     init()     init(ifmam_msglen ifmam_msglen: u_short, ifmam_version ifmam_version: u_char, ifmam_type ifmam_type: u_char, ifmam_addrs ifmam_addrs: Int32, ifmam_flags ifmam_flags: Int32, ifmam_index ifmam_index: u_short, ifmam_refcount ifmam_refcount: Int32) } ``` |

Modified ifmediareq [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifmediareq {     var ifm_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ifm_current: Int32     var ifm_mask: Int32     var ifm_status: Int32     var ifm_active: Int32     var ifm_count: Int32     var ifm_ulist: UnsafeMutablePointer<Int32> } ``` |
| To | ``` struct ifmediareq {     var ifm_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ifm_current: Int32     var ifm_mask: Int32     var ifm_status: Int32     var ifm_active: Int32     var ifm_count: Int32     var ifm_ulist: UnsafeMutablePointer<Int32>     init()     init(ifm_name ifm_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ifm_current ifm_current: Int32, ifm_mask ifm_mask: Int32, ifm_status ifm_status: Int32, ifm_active ifm_active: Int32, ifm_count ifm_count: Int32, ifm_ulist ifm_ulist: UnsafeMutablePointer<Int32>) } ``` |

Modified ifqueue [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifqueue {     var ifq_head: UnsafeMutablePointer<Void>     var ifq_tail: UnsafeMutablePointer<Void>     var ifq_len: Int32     var ifq_maxlen: Int32     var ifq_drops: Int32 } ``` |
| To | ``` struct ifqueue {     var ifq_head: UnsafeMutablePointer<Void>     var ifq_tail: UnsafeMutablePointer<Void>     var ifq_len: Int32     var ifq_maxlen: Int32     var ifq_drops: Int32     init()     init(ifq_head ifq_head: UnsafeMutablePointer<Void>, ifq_tail ifq_tail: UnsafeMutablePointer<Void>, ifq_len ifq_len: Int32, ifq_maxlen ifq_maxlen: Int32, ifq_drops ifq_drops: Int32) } ``` |

Modified ifreq [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifreq {     var ifr_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct ifreq {     var ifr_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init() } ``` |

Modified ifstat [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ifstat {     var ifs_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ascii: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ```  ``` |

Modified imaxdiv_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct imaxdiv_t {     var quot: intmax_t     var rem: intmax_t } ``` |
| To | ``` struct imaxdiv_t {     var quot: intmax_t     var rem: intmax_t     init()     init(quot quot: intmax_t, rem rem: intmax_t) } ``` |

Modified in6_addr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct in6_addr { } ``` |
| To | ``` struct in6_addr {     init() } ``` |

Modified in6_pktinfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct in6_pktinfo {     var ipi6_addr: in6_addr     var ipi6_ifindex: UInt32 } ``` |
| To | ``` struct in6_pktinfo {     var ipi6_addr: in6_addr     var ipi6_ifindex: UInt32     init()     init(ipi6_addr ipi6_addr: in6_addr, ipi6_ifindex ipi6_ifindex: UInt32) } ``` |

Modified in_addr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct in_addr {     var s_addr: in_addr_t } ``` |
| To | ``` struct in_addr {     var s_addr: in_addr_t     init()     init(s_addr s_addr: in_addr_t) } ``` |

Modified in_pktinfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct in_pktinfo {     var ipi_ifindex: UInt32     var ipi_spec_dst: in_addr     var ipi_addr: in_addr } ``` |
| To | ``` struct in_pktinfo {     var ipi_ifindex: UInt32     var ipi_spec_dst: in_addr     var ipi_addr: in_addr     init()     init(ipi_ifindex ipi_ifindex: UInt32, ipi_spec_dst ipi_spec_dst: in_addr, ipi_addr ipi_addr: in_addr) } ``` |

Modified io_stat_entry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct io_stat_entry {     var count: UInt64     var size: UInt64 } ``` |
| To | ``` struct io_stat_entry {     var count: UInt64     var size: UInt64     init()     init(count count: UInt64, size size: UInt64) } ``` |

Modified io_stat_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct io_stat_info {     var disk_reads: io_stat_entry     var io_priority: (io_stat_entry, io_stat_entry, io_stat_entry, io_stat_entry)     var paging: io_stat_entry     var metadata: io_stat_entry     var total_io: io_stat_entry } ``` |
| To | ``` struct io_stat_info {     var disk_reads: io_stat_entry     var io_priority: (io_stat_entry, io_stat_entry, io_stat_entry, io_stat_entry)     var paging: io_stat_entry     var metadata: io_stat_entry     var total_io: io_stat_entry     init()     init(disk_reads disk_reads: io_stat_entry, io_priority io_priority: (io_stat_entry, io_stat_entry, io_stat_entry, io_stat_entry), paging paging: io_stat_entry, metadata metadata: io_stat_entry, total_io total_io: io_stat_entry) } ``` |

Modified iovec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct iovec {     var iov_base: UnsafeMutablePointer<Void>     var iov_len: UInt } ``` |
| To | ``` struct iovec {     var iov_base: UnsafeMutablePointer<Void>     var iov_len: Int     init()     init(iov_base iov_base: UnsafeMutablePointer<Void>, iov_len iov_len: Int) } ``` |

Modified iovec.iov_len

|  | Declaration |
| --- | --- |
| From | ``` var iov_len: UInt ``` |
| To | ``` var iov_len: Int ``` |

Modified ip6_mtuinfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ip6_mtuinfo {     var ip6m_addr: sockaddr_in6     var ip6m_mtu: UInt32 } ``` |
| To | ``` struct ip6_mtuinfo {     var ip6m_addr: sockaddr_in6     var ip6m_mtu: UInt32     init()     init(ip6m_addr ip6m_addr: sockaddr_in6, ip6m_mtu ip6m_mtu: UInt32) } ``` |

Modified ip_mreq [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ip_mreq {     var imr_multiaddr: in_addr     var imr_interface: in_addr } ``` |
| To | ``` struct ip_mreq {     var imr_multiaddr: in_addr     var imr_interface: in_addr     init()     init(imr_multiaddr imr_multiaddr: in_addr, imr_interface imr_interface: in_addr) } ``` |

Modified ip_mreq_source [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ip_mreq_source {     var imr_multiaddr: in_addr     var imr_sourceaddr: in_addr     var imr_interface: in_addr } ``` |
| To | ``` struct ip_mreq_source {     var imr_multiaddr: in_addr     var imr_sourceaddr: in_addr     var imr_interface: in_addr     init()     init(imr_multiaddr imr_multiaddr: in_addr, imr_sourceaddr imr_sourceaddr: in_addr, imr_interface imr_interface: in_addr) } ``` |

Modified ip_mreqn [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ip_mreqn {     var imr_multiaddr: in_addr     var imr_address: in_addr     var imr_ifindex: Int32 } ``` |
| To | ``` struct ip_mreqn {     var imr_multiaddr: in_addr     var imr_address: in_addr     var imr_ifindex: Int32     init()     init(imr_multiaddr imr_multiaddr: in_addr, imr_address imr_address: in_addr, imr_ifindex imr_ifindex: Int32) } ``` |

Modified ip_opts [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ip_opts {     var ip_dst: in_addr     var ip_opts: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct ip_opts {     var ip_dst: in_addr     var ip_opts: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(ip_dst ip_dst: in_addr, ip_opts ip_opts: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified ipc_info_name [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ipc_info_name {     var iin_name: mach_port_name_t     var iin_collision: integer_t     var iin_type: mach_port_type_t     var iin_urefs: mach_port_urefs_t     var iin_object: natural_t     var iin_next: natural_t     var iin_hash: natural_t } ``` |
| To | ``` struct ipc_info_name {     var iin_name: mach_port_name_t     var iin_collision: integer_t     var iin_type: mach_port_type_t     var iin_urefs: mach_port_urefs_t     var iin_object: natural_t     var iin_next: natural_t     var iin_hash: natural_t     init()     init(iin_name iin_name: mach_port_name_t, iin_collision iin_collision: integer_t, iin_type iin_type: mach_port_type_t, iin_urefs iin_urefs: mach_port_urefs_t, iin_object iin_object: natural_t, iin_next iin_next: natural_t, iin_hash iin_hash: natural_t) } ``` |

Modified ipc_info_space [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ipc_info_space {     var iis_genno_mask: natural_t     var iis_table_size: natural_t     var iis_table_next: natural_t     var iis_tree_size: natural_t     var iis_tree_small: natural_t     var iis_tree_hash: natural_t } ``` |
| To | ``` struct ipc_info_space {     var iis_genno_mask: natural_t     var iis_table_size: natural_t     var iis_table_next: natural_t     var iis_tree_size: natural_t     var iis_tree_small: natural_t     var iis_tree_hash: natural_t     init()     init(iis_genno_mask iis_genno_mask: natural_t, iis_table_size iis_table_size: natural_t, iis_table_next iis_table_next: natural_t, iis_tree_size iis_tree_size: natural_t, iis_tree_small iis_tree_small: natural_t, iis_tree_hash iis_tree_hash: natural_t) } ``` |

Modified ipc_info_space_basic [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ipc_info_space_basic {     var iisb_genno_mask: natural_t     var iisb_table_size: natural_t     var iisb_table_next: natural_t     var iisb_table_inuse: natural_t     var iisb_reserved: (natural_t, natural_t) } ``` |
| To | ``` struct ipc_info_space_basic {     var iisb_genno_mask: natural_t     var iisb_table_size: natural_t     var iisb_table_next: natural_t     var iisb_table_inuse: natural_t     var iisb_reserved: (natural_t, natural_t)     init()     init(iisb_genno_mask iisb_genno_mask: natural_t, iisb_table_size iisb_table_size: natural_t, iisb_table_next iisb_table_next: natural_t, iisb_table_inuse iisb_table_inuse: natural_t, iisb_reserved iisb_reserved: (natural_t, natural_t)) } ``` |

Modified ipc_info_tree_name [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ipc_info_tree_name {     var iitn_name: ipc_info_name_t     var iitn_lchild: mach_port_name_t     var iitn_rchild: mach_port_name_t } ``` |
| To | ``` struct ipc_info_tree_name {     var iitn_name: ipc_info_name_t     var iitn_lchild: mach_port_name_t     var iitn_rchild: mach_port_name_t     init()     init(iitn_name iitn_name: ipc_info_name_t, iitn_lchild iitn_lchild: mach_port_name_t, iitn_rchild iitn_rchild: mach_port_name_t) } ``` |

Modified ipc_perm [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ipc_perm {     var uid: uid_t     var gid: gid_t     var cuid: uid_t     var cgid: gid_t     var mode: mode_t     var _seq: UInt16     var _key: key_t } ``` |
| To | ``` struct ipc_perm {     var uid: uid_t     var gid: gid_t     var cuid: uid_t     var cgid: gid_t     var mode: mode_t     var _seq: UInt16     var _key: key_t     init()     init(uid uid: uid_t, gid gid: gid_t, cuid cuid: uid_t, cgid cgid: gid_t, mode mode: mode_t, _seq _seq: UInt16, _key _key: key_t) } ``` |

Modified ipv6_mreq [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ipv6_mreq {     var ipv6mr_multiaddr: in6_addr     var ipv6mr_interface: UInt32 } ``` |
| To | ``` struct ipv6_mreq {     var ipv6mr_multiaddr: in6_addr     var ipv6mr_interface: UInt32     init()     init(ipv6mr_multiaddr ipv6mr_multiaddr: in6_addr, ipv6mr_interface ipv6mr_interface: UInt32) } ``` |

Modified itimerval [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct itimerval {     var it_interval: timeval     var it_value: timeval } ``` |
| To | ``` struct itimerval {     var it_interval: timeval     var it_value: timeval     init()     init(it_interval it_interval: timeval, it_value it_value: timeval) } ``` |

Modified kauth_ace [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kauth_ace {     var ace_applicable: guid_t     var ace_flags: UInt32     var ace_rights: kauth_ace_rights_t } ``` |
| To | ``` struct kauth_ace {     var ace_applicable: guid_t     var ace_flags: UInt32     var ace_rights: kauth_ace_rights_t     init()     init(ace_applicable ace_applicable: guid_t, ace_flags ace_flags: UInt32, ace_rights ace_rights: kauth_ace_rights_t) } ``` |

Modified kauth_acl [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kauth_acl {     var acl_entrycount: UInt32     var acl_flags: UInt32     var acl_ace: (kauth_ace) } ``` |
| To | ``` struct kauth_acl {     var acl_entrycount: UInt32     var acl_flags: UInt32     var acl_ace: (kauth_ace)     init()     init(acl_entrycount acl_entrycount: UInt32, acl_flags acl_flags: UInt32, acl_ace acl_ace: (kauth_ace)) } ``` |

Modified kauth_cache_sizes [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kauth_cache_sizes {     var kcs_group_size: UInt32     var kcs_id_size: UInt32 } ``` |
| To | ``` struct kauth_cache_sizes {     var kcs_group_size: UInt32     var kcs_id_size: UInt32     init()     init(kcs_group_size kcs_group_size: UInt32, kcs_id_size kcs_id_size: UInt32) } ``` |

Modified kauth_filesec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kauth_filesec {     var fsec_magic: UInt32     var fsec_owner: guid_t     var fsec_group: guid_t     var fsec_acl: kauth_acl } ``` |
| To | ``` struct kauth_filesec {     var fsec_magic: UInt32     var fsec_owner: guid_t     var fsec_group: guid_t     var fsec_acl: kauth_acl     init()     init(fsec_magic fsec_magic: UInt32, fsec_owner fsec_owner: guid_t, fsec_group fsec_group: guid_t, fsec_acl fsec_acl: kauth_acl) } ``` |

Modified kauth_identity_extlookup [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kauth_identity_extlookup {     var el_seqno: UInt32     var el_result: UInt32     var el_flags: UInt32     var el_info_pid: __darwin_pid_t     var el_extend: UInt64     var el_info_reserved_1: UInt32     var el_uid: uid_t     var el_uguid: guid_t     var el_uguid_valid: UInt32     var el_usid: ntsid_t     var el_usid_valid: UInt32     var el_gid: gid_t     var el_gguid: guid_t     var el_gguid_valid: UInt32     var el_gsid: ntsid_t     var el_gsid_valid: UInt32     var el_member_valid: UInt32     var el_sup_grp_cnt: UInt32     var el_sup_groups: (gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t) } ``` |
| To | ``` struct kauth_identity_extlookup {     var el_seqno: UInt32     var el_result: UInt32     var el_flags: UInt32     var el_info_pid: __darwin_pid_t     var el_extend: UInt64     var el_info_reserved_1: UInt32     var el_uid: uid_t     var el_uguid: guid_t     var el_uguid_valid: UInt32     var el_usid: ntsid_t     var el_usid_valid: UInt32     var el_gid: gid_t     var el_gguid: guid_t     var el_gguid_valid: UInt32     var el_gsid: ntsid_t     var el_gsid_valid: UInt32     var el_member_valid: UInt32     var el_sup_grp_cnt: UInt32     var el_sup_groups: (gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t)     init()     init(el_seqno el_seqno: UInt32, el_result el_result: UInt32, el_flags el_flags: UInt32, el_info_pid el_info_pid: __darwin_pid_t, el_extend el_extend: UInt64, el_info_reserved_1 el_info_reserved_1: UInt32, el_uid el_uid: uid_t, el_uguid el_uguid: guid_t, el_uguid_valid el_uguid_valid: UInt32, el_usid el_usid: ntsid_t, el_usid_valid el_usid_valid: UInt32, el_gid el_gid: gid_t, el_gguid el_gguid: guid_t, el_gguid_valid el_gguid_valid: UInt32, el_gsid el_gsid: ntsid_t, el_gsid_valid el_gsid_valid: UInt32, el_member_valid el_member_valid: UInt32, el_sup_grp_cnt el_sup_grp_cnt: UInt32, el_sup_groups el_sup_groups: (gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t)) } ``` |

Modified kernel_resource_sizes [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kernel_resource_sizes {     var task: natural_t     var thread: natural_t     var port: natural_t     var memory_region: natural_t     var memory_object: natural_t } ``` |
| To | ``` struct kernel_resource_sizes {     var task: natural_t     var thread: natural_t     var port: natural_t     var memory_region: natural_t     var memory_object: natural_t     init()     init(task task: natural_t, thread thread: natural_t, port port: natural_t, memory_region memory_region: natural_t, memory_object memory_object: natural_t) } ``` |

Modified kev_dl_proto_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kev_dl_proto_data {     var link_data: net_event_data     var proto_family: UInt32     var proto_remaining_count: UInt32 } ``` |
| To | ``` struct kev_dl_proto_data {     var link_data: net_event_data     var proto_family: UInt32     var proto_remaining_count: UInt32     init()     init(link_data link_data: net_event_data, proto_family proto_family: UInt32, proto_remaining_count proto_remaining_count: UInt32) } ``` |

Modified kevent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kevent {     var ident: UInt     var filter: Int16     var flags: UInt16     var fflags: UInt32     var data: Int     var udata: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct kevent {     var ident: UInt     var filter: Int16     var flags: UInt16     var fflags: UInt32     var data: Int     var udata: UnsafeMutablePointer<Void>     init()     init(ident ident: UInt, filter filter: Int16, flags flags: UInt16, fflags fflags: UInt32, data data: Int, udata udata: UnsafeMutablePointer<Void>) } ``` |

Modified kevent64_s [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kevent64_s {     var ident: UInt64     var filter: Int16     var flags: UInt16     var fflags: UInt32     var data: Int64     var udata: UInt64     var ext: (UInt64, UInt64) } ``` |
| To | ``` struct kevent64_s {     var ident: UInt64     var filter: Int16     var flags: UInt16     var fflags: UInt32     var data: Int64     var udata: UInt64     var ext: (UInt64, UInt64)     init()     init(ident ident: UInt64, filter filter: Int16, flags flags: UInt16, fflags fflags: UInt32, data data: Int64, udata udata: UInt64, ext ext: (UInt64, UInt64)) } ``` |

Modified kinfo_lctx [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kinfo_lctx {     var id: pid_t     var mc: Int32 } ``` |
| To | ``` struct kinfo_lctx {     var id: pid_t     var mc: Int32     init()     init(id id: pid_t, mc mc: Int32) } ``` |

Modified kinfo_proc [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kinfo_proc {     var kp_proc: extern_proc     var kp_eproc: eproc } ``` |
| To | ``` struct kinfo_proc {     var kp_proc: extern_proc     var kp_eproc: eproc     init()     init(kp_proc kp_proc: extern_proc, kp_eproc kp_eproc: eproc) } ``` |

Modified klist [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct klist {     var slh_first: COpaquePointer } ``` |
| To | ``` struct klist {     var slh_first: COpaquePointer     init()     init(slh_first slh_first: COpaquePointer) } ``` |

Modified kmod_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kmod_info {     var next: UnsafeMutablePointer<kmod_info>     var info_version: Int32     var id: UInt32     var name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var version: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var reference_count: Int32     var reference_list: UnsafeMutablePointer<kmod_reference_t>     var address: vm_address_t     var size: vm_size_t     var hdr_size: vm_size_t     var start: CFunctionPointer<kmod_start_func_t>     var stop: CFunctionPointer<kmod_stop_func_t> } ``` |
| To | ``` struct kmod_info {     var next: UnsafeMutablePointer<kmod_info>     var info_version: Int32     var id: UInt32     var name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var version: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var reference_count: Int32     var reference_list: UnsafeMutablePointer<kmod_reference_t>     var address: vm_address_t     var size: vm_size_t     var hdr_size: vm_size_t     var start: CFunctionPointer<kmod_start_func_t>     var stop: CFunctionPointer<kmod_stop_func_t>     init()     init(next next: UnsafeMutablePointer<kmod_info>, info_version info_version: Int32, id id: UInt32, name name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), version version: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), reference_count reference_count: Int32, reference_list reference_list: UnsafeMutablePointer<kmod_reference_t>, address address: vm_address_t, size size: vm_size_t, hdr_size hdr_size: vm_size_t, start start: CFunctionPointer<kmod_start_func_t>, stop stop: CFunctionPointer<kmod_stop_func_t>) } ``` |

Modified kmod_info_32_v1 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kmod_info_32_v1 {     var next_addr: UInt32     var info_version: Int32     var id: UInt32     var name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var version: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var reference_count: Int32     var reference_list_addr: UInt32     var address: UInt32     var size: UInt32     var hdr_size: UInt32     var start_addr: UInt32     var stop_addr: UInt32 } ``` |
| To | ``` struct kmod_info_32_v1 {     var next_addr: UInt32     var info_version: Int32     var id: UInt32     var name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var version: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var reference_count: Int32     var reference_list_addr: UInt32     var address: UInt32     var size: UInt32     var hdr_size: UInt32     var start_addr: UInt32     var stop_addr: UInt32     init()     init(next_addr next_addr: UInt32, info_version info_version: Int32, id id: UInt32, name name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), version version: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), reference_count reference_count: Int32, reference_list_addr reference_list_addr: UInt32, address address: UInt32, size size: UInt32, hdr_size hdr_size: UInt32, start_addr start_addr: UInt32, stop_addr stop_addr: UInt32) } ``` |

Modified kmod_info_64_v1 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kmod_info_64_v1 {     var next_addr: UInt64     var info_version: Int32     var id: UInt32     var name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var version: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var reference_count: Int32     var reference_list_addr: UInt64     var address: UInt64     var size: UInt64     var hdr_size: UInt64     var start_addr: UInt64     var stop_addr: UInt64 } ``` |
| To | ``` struct kmod_info_64_v1 {     var next_addr: UInt64     var info_version: Int32     var id: UInt32     var name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var version: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var reference_count: Int32     var reference_list_addr: UInt64     var address: UInt64     var size: UInt64     var hdr_size: UInt64     var start_addr: UInt64     var stop_addr: UInt64     init()     init(next_addr next_addr: UInt64, info_version info_version: Int32, id id: UInt32, name name: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), version version: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), reference_count reference_count: Int32, reference_list_addr reference_list_addr: UInt64, address address: UInt64, size size: UInt64, hdr_size hdr_size: UInt64, start_addr start_addr: UInt64, stop_addr stop_addr: UInt64) } ``` |

Modified kmod_reference [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kmod_reference {     var next: UnsafeMutablePointer<kmod_reference>     var info: UnsafeMutablePointer<kmod_info> } ``` |
| To | ``` struct kmod_reference {     var next: UnsafeMutablePointer<kmod_reference>     var info: UnsafeMutablePointer<kmod_info>     init()     init(next next: UnsafeMutablePointer<kmod_reference>, info info: UnsafeMutablePointer<kmod_info>) } ``` |

Modified lastlogx [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct lastlogx {     var ll_tv: timeval     var ll_line: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ll_host: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct lastlogx {     var ll_tv: timeval     var ll_line: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ll_host: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(ll_tv ll_tv: timeval, ll_line ll_line: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), ll_host ll_host: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified lconv [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct lconv {     var decimal_point: UnsafeMutablePointer<Int8>     var thousands_sep: UnsafeMutablePointer<Int8>     var grouping: UnsafeMutablePointer<Int8>     var int_curr_symbol: UnsafeMutablePointer<Int8>     var currency_symbol: UnsafeMutablePointer<Int8>     var mon_decimal_point: UnsafeMutablePointer<Int8>     var mon_thousands_sep: UnsafeMutablePointer<Int8>     var mon_grouping: UnsafeMutablePointer<Int8>     var positive_sign: UnsafeMutablePointer<Int8>     var negative_sign: UnsafeMutablePointer<Int8>     var int_frac_digits: Int8     var frac_digits: Int8     var p_cs_precedes: Int8     var p_sep_by_space: Int8     var n_cs_precedes: Int8     var n_sep_by_space: Int8     var p_sign_posn: Int8     var n_sign_posn: Int8     var int_p_cs_precedes: Int8     var int_n_cs_precedes: Int8     var int_p_sep_by_space: Int8     var int_n_sep_by_space: Int8     var int_p_sign_posn: Int8     var int_n_sign_posn: Int8 } ``` |
| To | ``` struct lconv {     var decimal_point: UnsafeMutablePointer<Int8>     var thousands_sep: UnsafeMutablePointer<Int8>     var grouping: UnsafeMutablePointer<Int8>     var int_curr_symbol: UnsafeMutablePointer<Int8>     var currency_symbol: UnsafeMutablePointer<Int8>     var mon_decimal_point: UnsafeMutablePointer<Int8>     var mon_thousands_sep: UnsafeMutablePointer<Int8>     var mon_grouping: UnsafeMutablePointer<Int8>     var positive_sign: UnsafeMutablePointer<Int8>     var negative_sign: UnsafeMutablePointer<Int8>     var int_frac_digits: Int8     var frac_digits: Int8     var p_cs_precedes: Int8     var p_sep_by_space: Int8     var n_cs_precedes: Int8     var n_sep_by_space: Int8     var p_sign_posn: Int8     var n_sign_posn: Int8     var int_p_cs_precedes: Int8     var int_n_cs_precedes: Int8     var int_p_sep_by_space: Int8     var int_n_sep_by_space: Int8     var int_p_sign_posn: Int8     var int_n_sign_posn: Int8     init()     init(decimal_point decimal_point: UnsafeMutablePointer<Int8>, thousands_sep thousands_sep: UnsafeMutablePointer<Int8>, grouping grouping: UnsafeMutablePointer<Int8>, int_curr_symbol int_curr_symbol: UnsafeMutablePointer<Int8>, currency_symbol currency_symbol: UnsafeMutablePointer<Int8>, mon_decimal_point mon_decimal_point: UnsafeMutablePointer<Int8>, mon_thousands_sep mon_thousands_sep: UnsafeMutablePointer<Int8>, mon_grouping mon_grouping: UnsafeMutablePointer<Int8>, positive_sign positive_sign: UnsafeMutablePointer<Int8>, negative_sign negative_sign: UnsafeMutablePointer<Int8>, int_frac_digits int_frac_digits: Int8, frac_digits frac_digits: Int8, p_cs_precedes p_cs_precedes: Int8, p_sep_by_space p_sep_by_space: Int8, n_cs_precedes n_cs_precedes: Int8, n_sep_by_space n_sep_by_space: Int8, p_sign_posn p_sign_posn: Int8, n_sign_posn n_sign_posn: Int8, int_p_cs_precedes int_p_cs_precedes: Int8, int_n_cs_precedes int_n_cs_precedes: Int8, int_p_sep_by_space int_p_sep_by_space: Int8, int_n_sep_by_space int_n_sep_by_space: Int8, int_p_sign_posn int_p_sign_posn: Int8, int_n_sign_posn int_n_sign_posn: Int8) } ``` |

Modified ldiv_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ldiv_t {     var quot: Int     var rem: Int } ``` |
| To | ``` struct ldiv_t {     var quot: Int     var rem: Int     init()     init(quot quot: Int, rem rem: Int) } ``` |

Modified linger [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct linger {     var l_onoff: Int32     var l_linger: Int32 } ``` |
| To | ``` struct linger {     var l_onoff: Int32     var l_linger: Int32     init()     init(l_onoff l_onoff: Int32, l_linger l_linger: Int32) } ``` |

Modified lldiv_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct lldiv_t {     var quot: Int64     var rem: Int64 } ``` |
| To | ``` struct lldiv_t {     var quot: Int64     var rem: Int64     init()     init(quot quot: Int64, rem rem: Int64) } ``` |

Modified loadavg [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct loadavg {     var ldavg: (fixpt_t, fixpt_t, fixpt_t)     var fscale: Int } ``` |
| To | ``` struct loadavg {     var ldavg: (fixpt_t, fixpt_t, fixpt_t)     var fscale: Int     init()     init(ldavg ldavg: (fixpt_t, fixpt_t, fixpt_t), fscale fscale: Int) } ``` |

Modified lockgroup_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct lockgroup_info {     var lockgroup_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var lockgroup_attr: UInt64     var lock_spin_cnt: UInt64     var lock_spin_util_cnt: UInt64     var lock_spin_held_cnt: UInt64     var lock_spin_miss_cnt: UInt64     var lock_spin_held_max: UInt64     var lock_spin_held_cum: UInt64     var lock_mtx_cnt: UInt64     var lock_mtx_util_cnt: UInt64     var lock_mtx_held_cnt: UInt64     var lock_mtx_miss_cnt: UInt64     var lock_mtx_wait_cnt: UInt64     var lock_mtx_held_max: UInt64     var lock_mtx_held_cum: UInt64     var lock_mtx_wait_max: UInt64     var lock_mtx_wait_cum: UInt64     var lock_rw_cnt: UInt64     var lock_rw_util_cnt: UInt64     var lock_rw_held_cnt: UInt64     var lock_rw_miss_cnt: UInt64     var lock_rw_wait_cnt: UInt64     var lock_rw_held_max: UInt64     var lock_rw_held_cum: UInt64     var lock_rw_wait_max: UInt64     var lock_rw_wait_cum: UInt64 } ``` |
| To | ``` struct lockgroup_info {     var lockgroup_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var lockgroup_attr: UInt64     var lock_spin_cnt: UInt64     var lock_spin_util_cnt: UInt64     var lock_spin_held_cnt: UInt64     var lock_spin_miss_cnt: UInt64     var lock_spin_held_max: UInt64     var lock_spin_held_cum: UInt64     var lock_mtx_cnt: UInt64     var lock_mtx_util_cnt: UInt64     var lock_mtx_held_cnt: UInt64     var lock_mtx_miss_cnt: UInt64     var lock_mtx_wait_cnt: UInt64     var lock_mtx_held_max: UInt64     var lock_mtx_held_cum: UInt64     var lock_mtx_wait_max: UInt64     var lock_mtx_wait_cum: UInt64     var lock_rw_cnt: UInt64     var lock_rw_util_cnt: UInt64     var lock_rw_held_cnt: UInt64     var lock_rw_miss_cnt: UInt64     var lock_rw_wait_cnt: UInt64     var lock_rw_held_max: UInt64     var lock_rw_held_cum: UInt64     var lock_rw_wait_max: UInt64     var lock_rw_wait_cum: UInt64     init()     init(lockgroup_name lockgroup_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), lockgroup_attr lockgroup_attr: UInt64, lock_spin_cnt lock_spin_cnt: UInt64, lock_spin_util_cnt lock_spin_util_cnt: UInt64, lock_spin_held_cnt lock_spin_held_cnt: UInt64, lock_spin_miss_cnt lock_spin_miss_cnt: UInt64, lock_spin_held_max lock_spin_held_max: UInt64, lock_spin_held_cum lock_spin_held_cum: UInt64, lock_mtx_cnt lock_mtx_cnt: UInt64, lock_mtx_util_cnt lock_mtx_util_cnt: UInt64, lock_mtx_held_cnt lock_mtx_held_cnt: UInt64, lock_mtx_miss_cnt lock_mtx_miss_cnt: UInt64, lock_mtx_wait_cnt lock_mtx_wait_cnt: UInt64, lock_mtx_held_max lock_mtx_held_max: UInt64, lock_mtx_held_cum lock_mtx_held_cum: UInt64, lock_mtx_wait_max lock_mtx_wait_max: UInt64, lock_mtx_wait_cum lock_mtx_wait_cum: UInt64, lock_rw_cnt lock_rw_cnt: UInt64, lock_rw_util_cnt lock_rw_util_cnt: UInt64, lock_rw_held_cnt lock_rw_held_cnt: UInt64, lock_rw_miss_cnt lock_rw_miss_cnt: UInt64, lock_rw_wait_cnt lock_rw_wait_cnt: UInt64, lock_rw_held_max lock_rw_held_max: UInt64, lock_rw_held_cum lock_rw_held_cum: UInt64, lock_rw_wait_max lock_rw_wait_max: UInt64, lock_rw_wait_cum lock_rw_wait_cum: UInt64) } ``` |

Modified log2phys [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct log2phys {     var l2p_flags: UInt32     var l2p_contigbytes: off_t     var l2p_devoffset: off_t } ``` |
| To | ``` struct log2phys {     var l2p_flags: UInt32     var l2p_contigbytes: off_t     var l2p_devoffset: off_t     init()     init(l2p_flags l2p_flags: UInt32, l2p_contigbytes l2p_contigbytes: off_t, l2p_devoffset l2p_devoffset: off_t) } ``` |

Modified mach_dead_name_notification_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_dead_name_notification_t {     var not_header: mach_msg_header_t     var NDR: NDR_record_t     var not_port: mach_port_name_t     var trailer: mach_msg_format_0_trailer_t } ``` |
| To | ``` struct mach_dead_name_notification_t {     var not_header: mach_msg_header_t     var NDR: NDR_record_t     var not_port: mach_port_name_t     var trailer: mach_msg_format_0_trailer_t     init()     init(not_header not_header: mach_msg_header_t, NDR NDR: NDR_record_t, not_port not_port: mach_port_name_t, trailer trailer: mach_msg_format_0_trailer_t) } ``` |

Modified mach_msg_audit_trailer_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_audit_trailer_t {     var msgh_trailer_type: mach_msg_trailer_type_t     var msgh_trailer_size: mach_msg_trailer_size_t     var msgh_seqno: mach_port_seqno_t     var msgh_sender: security_token_t     var msgh_audit: audit_token_t } ``` |
| To | ``` struct mach_msg_audit_trailer_t {     var msgh_trailer_type: mach_msg_trailer_type_t     var msgh_trailer_size: mach_msg_trailer_size_t     var msgh_seqno: mach_port_seqno_t     var msgh_sender: security_token_t     var msgh_audit: audit_token_t     init()     init(msgh_trailer_type msgh_trailer_type: mach_msg_trailer_type_t, msgh_trailer_size msgh_trailer_size: mach_msg_trailer_size_t, msgh_seqno msgh_seqno: mach_port_seqno_t, msgh_sender msgh_sender: security_token_t, msgh_audit msgh_audit: audit_token_t) } ``` |

Modified mach_msg_base_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_base_t {     var header: mach_msg_header_t     var body: mach_msg_body_t } ``` |
| To | ``` struct mach_msg_base_t {     var header: mach_msg_header_t     var body: mach_msg_body_t     init()     init(header header: mach_msg_header_t, body body: mach_msg_body_t) } ``` |

Modified mach_msg_body_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_body_t {     var msgh_descriptor_count: mach_msg_size_t } ``` |
| To | ``` struct mach_msg_body_t {     var msgh_descriptor_count: mach_msg_size_t     init()     init(msgh_descriptor_count msgh_descriptor_count: mach_msg_size_t) } ``` |

Modified mach_msg_context_trailer_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_context_trailer_t {     var msgh_trailer_type: mach_msg_trailer_type_t     var msgh_trailer_size: mach_msg_trailer_size_t     var msgh_seqno: mach_port_seqno_t     var msgh_sender: security_token_t     var msgh_audit: audit_token_t     var msgh_context: mach_port_context_t } ``` |
| To | ``` struct mach_msg_context_trailer_t {     var msgh_trailer_type: mach_msg_trailer_type_t     var msgh_trailer_size: mach_msg_trailer_size_t     var msgh_seqno: mach_port_seqno_t     var msgh_sender: security_token_t     var msgh_audit: audit_token_t     var msgh_context: mach_port_context_t     init()     init(msgh_trailer_type msgh_trailer_type: mach_msg_trailer_type_t, msgh_trailer_size msgh_trailer_size: mach_msg_trailer_size_t, msgh_seqno msgh_seqno: mach_port_seqno_t, msgh_sender msgh_sender: security_token_t, msgh_audit msgh_audit: audit_token_t, msgh_context msgh_context: mach_port_context_t) } ``` |

Modified mach_msg_empty_rcv_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_empty_rcv_t {     var header: mach_msg_header_t     var trailer: mach_msg_trailer_t } ``` |
| To | ``` struct mach_msg_empty_rcv_t {     var header: mach_msg_header_t     var trailer: mach_msg_trailer_t     init()     init(header header: mach_msg_header_t, trailer trailer: mach_msg_trailer_t) } ``` |

Modified mach_msg_empty_send_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_empty_send_t {     var header: mach_msg_header_t } ``` |
| To | ``` struct mach_msg_empty_send_t {     var header: mach_msg_header_t     init()     init(header header: mach_msg_header_t) } ``` |

Modified mach_msg_header_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_header_t {     var msgh_bits: mach_msg_bits_t     var msgh_size: mach_msg_size_t     var msgh_remote_port: mach_port_t     var msgh_local_port: mach_port_t     var msgh_voucher_port: mach_port_name_t     var msgh_id: mach_msg_id_t } ``` |
| To | ``` struct mach_msg_header_t {     var msgh_bits: mach_msg_bits_t     var msgh_size: mach_msg_size_t     var msgh_remote_port: mach_port_t     var msgh_local_port: mach_port_t     var msgh_voucher_port: mach_port_name_t     var msgh_id: mach_msg_id_t     init()     init(msgh_bits msgh_bits: mach_msg_bits_t, msgh_size msgh_size: mach_msg_size_t, msgh_remote_port msgh_remote_port: mach_port_t, msgh_local_port msgh_local_port: mach_port_t, msgh_voucher_port msgh_voucher_port: mach_port_name_t, msgh_id msgh_id: mach_msg_id_t) } ``` |

Modified mach_msg_mac_trailer_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_mac_trailer_t {     var msgh_trailer_type: mach_msg_trailer_type_t     var msgh_trailer_size: mach_msg_trailer_size_t     var msgh_seqno: mach_port_seqno_t     var msgh_sender: security_token_t     var msgh_audit: audit_token_t     var msgh_context: mach_port_context_t     var msgh_ad: Int32     var msgh_labels: msg_labels_t } ``` |
| To | ``` struct mach_msg_mac_trailer_t {     var msgh_trailer_type: mach_msg_trailer_type_t     var msgh_trailer_size: mach_msg_trailer_size_t     var msgh_seqno: mach_port_seqno_t     var msgh_sender: security_token_t     var msgh_audit: audit_token_t     var msgh_context: mach_port_context_t     var msgh_ad: Int32     var msgh_labels: msg_labels_t     init()     init(msgh_trailer_type msgh_trailer_type: mach_msg_trailer_type_t, msgh_trailer_size msgh_trailer_size: mach_msg_trailer_size_t, msgh_seqno msgh_seqno: mach_port_seqno_t, msgh_sender msgh_sender: security_token_t, msgh_audit msgh_audit: audit_token_t, msgh_context msgh_context: mach_port_context_t, msgh_ad msgh_ad: Int32, msgh_labels msgh_labels: msg_labels_t) } ``` |

Modified mach_msg_security_trailer_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_security_trailer_t {     var msgh_trailer_type: mach_msg_trailer_type_t     var msgh_trailer_size: mach_msg_trailer_size_t     var msgh_seqno: mach_port_seqno_t     var msgh_sender: security_token_t } ``` |
| To | ``` struct mach_msg_security_trailer_t {     var msgh_trailer_type: mach_msg_trailer_type_t     var msgh_trailer_size: mach_msg_trailer_size_t     var msgh_seqno: mach_port_seqno_t     var msgh_sender: security_token_t     init()     init(msgh_trailer_type msgh_trailer_type: mach_msg_trailer_type_t, msgh_trailer_size msgh_trailer_size: mach_msg_trailer_size_t, msgh_seqno msgh_seqno: mach_port_seqno_t, msgh_sender msgh_sender: security_token_t) } ``` |

Modified mach_msg_seqno_trailer_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_seqno_trailer_t {     var msgh_trailer_type: mach_msg_trailer_type_t     var msgh_trailer_size: mach_msg_trailer_size_t     var msgh_seqno: mach_port_seqno_t } ``` |
| To | ``` struct mach_msg_seqno_trailer_t {     var msgh_trailer_type: mach_msg_trailer_type_t     var msgh_trailer_size: mach_msg_trailer_size_t     var msgh_seqno: mach_port_seqno_t     init()     init(msgh_trailer_type msgh_trailer_type: mach_msg_trailer_type_t, msgh_trailer_size msgh_trailer_size: mach_msg_trailer_size_t, msgh_seqno msgh_seqno: mach_port_seqno_t) } ``` |

Modified mach_msg_trailer_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_msg_trailer_t {     var msgh_trailer_type: mach_msg_trailer_type_t     var msgh_trailer_size: mach_msg_trailer_size_t } ``` |
| To | ``` struct mach_msg_trailer_t {     var msgh_trailer_type: mach_msg_trailer_type_t     var msgh_trailer_size: mach_msg_trailer_size_t     init()     init(msgh_trailer_type msgh_trailer_type: mach_msg_trailer_type_t, msgh_trailer_size msgh_trailer_size: mach_msg_trailer_size_t) } ``` |

Modified mach_no_senders_notification_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_no_senders_notification_t {     var not_header: mach_msg_header_t     var NDR: NDR_record_t     var not_count: mach_msg_type_number_t     var trailer: mach_msg_format_0_trailer_t } ``` |
| To | ``` struct mach_no_senders_notification_t {     var not_header: mach_msg_header_t     var NDR: NDR_record_t     var not_count: mach_msg_type_number_t     var trailer: mach_msg_format_0_trailer_t     init()     init(not_header not_header: mach_msg_header_t, NDR NDR: NDR_record_t, not_count not_count: mach_msg_type_number_t, trailer trailer: mach_msg_format_0_trailer_t) } ``` |

Modified mach_port_deleted_notification_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_port_deleted_notification_t {     var not_header: mach_msg_header_t     var NDR: NDR_record_t     var not_port: mach_port_name_t     var trailer: mach_msg_format_0_trailer_t } ``` |
| To | ``` struct mach_port_deleted_notification_t {     var not_header: mach_msg_header_t     var NDR: NDR_record_t     var not_port: mach_port_name_t     var trailer: mach_msg_format_0_trailer_t     init()     init(not_header not_header: mach_msg_header_t, NDR NDR: NDR_record_t, not_port not_port: mach_port_name_t, trailer trailer: mach_msg_format_0_trailer_t) } ``` |

Modified mach_port_destroyed_notification_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_port_destroyed_notification_t {     var not_header: mach_msg_header_t     var not_body: mach_msg_body_t     var trailer: mach_msg_format_0_trailer_t } ``` |
| To | ``` struct mach_port_destroyed_notification_t {     var not_header: mach_msg_header_t     var not_body: mach_msg_body_t     var not_port: mach_msg_port_descriptor_t     var trailer: mach_msg_format_0_trailer_t     init()     init(not_header not_header: mach_msg_header_t, not_body not_body: mach_msg_body_t, not_port not_port: mach_msg_port_descriptor_t, trailer trailer: mach_msg_format_0_trailer_t) } ``` |

Modified mach_port_info_ext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_port_info_ext {     var mpie_status: mach_port_status_t     var mpie_boost_cnt: mach_port_msgcount_t     var reserved: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32) } ``` |
| To | ``` struct mach_port_info_ext {     var mpie_status: mach_port_status_t     var mpie_boost_cnt: mach_port_msgcount_t     var reserved: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)     init()     init(mpie_status mpie_status: mach_port_status_t, mpie_boost_cnt mpie_boost_cnt: mach_port_msgcount_t, reserved reserved: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified mach_port_limits [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_port_limits {     var mpl_qlimit: mach_port_msgcount_t } ``` |
| To | ``` struct mach_port_limits {     var mpl_qlimit: mach_port_msgcount_t     init()     init(mpl_qlimit mpl_qlimit: mach_port_msgcount_t) } ``` |

Modified mach_port_options [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_port_options {     var flags: UInt32     var mpl: mach_port_limits_t     var reserved: (UInt64, UInt64) } ``` |
| To | ``` struct mach_port_options {     var flags: UInt32     var mpl: mach_port_limits_t     var reserved: (UInt64, UInt64)     init()     init(flags flags: UInt32, mpl mpl: mach_port_limits_t, reserved reserved: (UInt64, UInt64)) } ``` |

Modified mach_port_status [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_port_status {     var mps_pset: mach_port_rights_t     var mps_seqno: mach_port_seqno_t     var mps_mscount: mach_port_mscount_t     var mps_qlimit: mach_port_msgcount_t     var mps_msgcount: mach_port_msgcount_t     var mps_sorights: mach_port_rights_t     var mps_srights: boolean_t     var mps_pdrequest: boolean_t     var mps_nsrequest: boolean_t     var mps_flags: natural_t } ``` |
| To | ``` struct mach_port_status {     var mps_pset: mach_port_rights_t     var mps_seqno: mach_port_seqno_t     var mps_mscount: mach_port_mscount_t     var mps_qlimit: mach_port_msgcount_t     var mps_msgcount: mach_port_msgcount_t     var mps_sorights: mach_port_rights_t     var mps_srights: boolean_t     var mps_pdrequest: boolean_t     var mps_nsrequest: boolean_t     var mps_flags: natural_t     init()     init(mps_pset mps_pset: mach_port_rights_t, mps_seqno mps_seqno: mach_port_seqno_t, mps_mscount mps_mscount: mach_port_mscount_t, mps_qlimit mps_qlimit: mach_port_msgcount_t, mps_msgcount mps_msgcount: mach_port_msgcount_t, mps_sorights mps_sorights: mach_port_rights_t, mps_srights mps_srights: boolean_t, mps_pdrequest mps_pdrequest: boolean_t, mps_nsrequest mps_nsrequest: boolean_t, mps_flags mps_flags: natural_t) } ``` |

Modified mach_send_once_notification_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_send_once_notification_t {     var not_header: mach_msg_header_t     var trailer: mach_msg_format_0_trailer_t } ``` |
| To | ``` struct mach_send_once_notification_t {     var not_header: mach_msg_header_t     var trailer: mach_msg_format_0_trailer_t     init()     init(not_header not_header: mach_msg_header_t, trailer trailer: mach_msg_format_0_trailer_t) } ``` |

Modified mach_send_possible_notification_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_send_possible_notification_t {     var not_header: mach_msg_header_t     var NDR: NDR_record_t     var not_port: mach_port_name_t     var trailer: mach_msg_format_0_trailer_t } ``` |
| To | ``` struct mach_send_possible_notification_t {     var not_header: mach_msg_header_t     var NDR: NDR_record_t     var not_port: mach_port_name_t     var trailer: mach_msg_format_0_trailer_t     init()     init(not_header not_header: mach_msg_header_t, NDR NDR: NDR_record_t, not_port not_port: mach_port_name_t, trailer trailer: mach_msg_format_0_trailer_t) } ``` |

Modified mach_task_basic_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_task_basic_info {     var virtual_size: mach_vm_size_t     var resident_size: mach_vm_size_t     var resident_size_max: mach_vm_size_t     var user_time: time_value_t     var system_time: time_value_t     var policy: policy_t     var suspend_count: integer_t } ``` |
| To | ``` struct mach_task_basic_info {     var virtual_size: mach_vm_size_t     var resident_size: mach_vm_size_t     var resident_size_max: mach_vm_size_t     var user_time: time_value_t     var system_time: time_value_t     var policy: policy_t     var suspend_count: integer_t     init()     init(virtual_size virtual_size: mach_vm_size_t, resident_size resident_size: mach_vm_size_t, resident_size_max resident_size_max: mach_vm_size_t, user_time user_time: time_value_t, system_time system_time: time_value_t, policy policy: policy_t, suspend_count suspend_count: integer_t) } ``` |

Modified mach_timebase_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_timebase_info {     var numer: UInt32     var denom: UInt32 } ``` |
| To | ``` struct mach_timebase_info {     var numer: UInt32     var denom: UInt32     init()     init(numer numer: UInt32, denom denom: UInt32) } ``` |

Modified mach_timespec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_timespec {     var tv_sec: UInt32     var tv_nsec: clock_res_t } ``` |
| To | ``` struct mach_timespec {     var tv_sec: UInt32     var tv_nsec: clock_res_t     init()     init(tv_sec tv_sec: UInt32, tv_nsec tv_nsec: clock_res_t) } ``` |

Modified mach_vm_info_region [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_vm_info_region {     var vir_start: mach_vm_offset_t     var vir_end: mach_vm_offset_t     var vir_object: mach_vm_offset_t     var vir_offset: memory_object_offset_t     var vir_needs_copy: boolean_t     var vir_protection: vm_prot_t     var vir_max_protection: vm_prot_t     var vir_inheritance: vm_inherit_t     var vir_wired_count: natural_t     var vir_user_wired_count: natural_t } ``` |
| To | ``` struct mach_vm_info_region {     var vir_start: mach_vm_offset_t     var vir_end: mach_vm_offset_t     var vir_object: mach_vm_offset_t     var vir_offset: memory_object_offset_t     var vir_needs_copy: boolean_t     var vir_protection: vm_prot_t     var vir_max_protection: vm_prot_t     var vir_inheritance: vm_inherit_t     var vir_wired_count: natural_t     var vir_user_wired_count: natural_t     init()     init(vir_start vir_start: mach_vm_offset_t, vir_end vir_end: mach_vm_offset_t, vir_object vir_object: mach_vm_offset_t, vir_offset vir_offset: memory_object_offset_t, vir_needs_copy vir_needs_copy: boolean_t, vir_protection vir_protection: vm_prot_t, vir_max_protection vir_max_protection: vm_prot_t, vir_inheritance vir_inheritance: vm_inherit_t, vir_wired_count vir_wired_count: natural_t, vir_user_wired_count vir_user_wired_count: natural_t) } ``` |

Modified mach_vm_read_entry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_vm_read_entry {     var address: mach_vm_address_t     var size: mach_vm_size_t } ``` |
| To | ``` struct mach_vm_read_entry {     var address: mach_vm_address_t     var size: mach_vm_size_t     init()     init(address address: mach_vm_address_t, size size: mach_vm_size_t) } ``` |

Modified mach_voucher_attr_recipe_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_voucher_attr_recipe_data {     var key: mach_voucher_attr_key_t     var command: mach_voucher_attr_recipe_command_t     var previous_voucher: mach_voucher_name_t     var content_size: mach_voucher_attr_content_size_t } ``` |
| To | ``` struct mach_voucher_attr_recipe_data {     var key: mach_voucher_attr_key_t     var command: mach_voucher_attr_recipe_command_t     var previous_voucher: mach_voucher_name_t     var content_size: mach_voucher_attr_content_size_t     init() } ``` |

Modified mach_zone_info_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_zone_info_data {     var mzi_count: UInt64     var mzi_cur_size: UInt64     var mzi_max_size: UInt64     var mzi_elem_size: UInt64     var mzi_alloc_size: UInt64     var mzi_sum_size: UInt64     var mzi_exhaustible: UInt64     var mzi_collectable: UInt64 } ``` |
| To | ``` struct mach_zone_info_data {     var mzi_count: UInt64     var mzi_cur_size: UInt64     var mzi_max_size: UInt64     var mzi_elem_size: UInt64     var mzi_alloc_size: UInt64     var mzi_sum_size: UInt64     var mzi_exhaustible: UInt64     var mzi_collectable: UInt64     init()     init(mzi_count mzi_count: UInt64, mzi_cur_size mzi_cur_size: UInt64, mzi_max_size mzi_max_size: UInt64, mzi_elem_size mzi_elem_size: UInt64, mzi_alloc_size mzi_alloc_size: UInt64, mzi_sum_size mzi_sum_size: UInt64, mzi_exhaustible mzi_exhaustible: UInt64, mzi_collectable mzi_collectable: UInt64) } ``` |

Modified mach_zone_name [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_zone_name {     var mzn_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct mach_zone_name {     var mzn_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(mzn_name mzn_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified malloc_introspection_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct malloc_introspection_t {     var enumerator: CFunctionPointer<((task_t, UnsafeMutablePointer<Void>, UInt32, vm_address_t, CFunctionPointer<memory_reader_t>, CFunctionPointer<vm_range_recorder_t>) -> kern_return_t)>     var good_size: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, UInt) -> UInt)>     var check: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)>     var print: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, boolean_t) -> Void)>     var log: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>) -> Void)>     var force_lock: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> Void)>     var force_unlock: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> Void)>     var statistics: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<malloc_statistics_t>) -> Void)>     var zone_locked: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)>     var enable_discharge_checking: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)>     var disable_discharge_checking: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> Void)>     var discharge: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>) -> Void)>     var enumerate_discharged_pointers: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)!) -> Void)> } ``` |
| To | ``` struct malloc_introspection_t {     var enumerator: CFunctionPointer<((task_t, UnsafeMutablePointer<Void>, UInt32, vm_address_t, CFunctionPointer<memory_reader_t>, CFunctionPointer<vm_range_recorder_t>) -> kern_return_t)>     var good_size: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, Int) -> Int)>     var check: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)>     var print: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, boolean_t) -> Void)>     var log: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>) -> Void)>     var force_lock: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> Void)>     var force_unlock: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> Void)>     var statistics: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<malloc_statistics_t>) -> Void)>     var zone_locked: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)>     var enable_discharge_checking: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)>     var disable_discharge_checking: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> Void)>     var discharge: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>) -> Void)>     var enumerate_discharged_pointers: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)!) -> Void)>     init()     init(enumerator enumerator: CFunctionPointer<((task_t, UnsafeMutablePointer<Void>, UInt32, vm_address_t, CFunctionPointer<memory_reader_t>, CFunctionPointer<vm_range_recorder_t>) -> kern_return_t)>, good_size good_size: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, Int) -> Int)>, check check: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)>, print print: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, boolean_t) -> Void)>, log log: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>) -> Void)>, force_lock force_lock: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> Void)>, force_unlock force_unlock: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> Void)>, statistics statistics: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<malloc_statistics_t>) -> Void)>, zone_locked zone_locked: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)>, enable_discharge_checking enable_discharge_checking: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> boolean_t)>, disable_discharge_checking disable_discharge_checking: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>) -> Void)>, discharge discharge: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>) -> Void)>, enumerate_discharged_pointers enumerate_discharged_pointers: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)!) -> Void)>) } ``` |

Modified malloc_introspection_t.good_size

|  | Declaration |
| --- | --- |
| From | ``` var good_size: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, UInt) -> UInt)> ``` |
| To | ``` var good_size: CFunctionPointer<((UnsafeMutablePointer<malloc_zone_t>, Int) -> Int)> ``` |

Modified malloc_statistics_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct malloc_statistics_t {     var blocks_in_use: UInt32     var size_in_use: UInt     var max_size_in_use: UInt     var size_allocated: UInt } ``` |
| To | ``` struct malloc_statistics_t {     var blocks_in_use: UInt32     var size_in_use: Int     var max_size_in_use: Int     var size_allocated: Int     init()     init(blocks_in_use blocks_in_use: UInt32, size_in_use size_in_use: Int, max_size_in_use max_size_in_use: Int, size_allocated size_allocated: Int) } ``` |

Modified malloc_statistics_t.max_size_in_use

|  | Declaration |
| --- | --- |
| From | ``` var max_size_in_use: UInt ``` |
| To | ``` var max_size_in_use: Int ``` |

Modified malloc_statistics_t.size_allocated

|  | Declaration |
| --- | --- |
| From | ``` var size_allocated: UInt ``` |
| To | ``` var size_allocated: Int ``` |

Modified malloc_statistics_t.size_in_use

|  | Declaration |
| --- | --- |
| From | ``` var size_in_use: UInt ``` |
| To | ``` var size_in_use: Int ``` |

Modified memory_object_attr_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct memory_object_attr_info {     var copy_strategy: memory_object_copy_strategy_t     var cluster_size: memory_object_cluster_size_t     var may_cache_object: boolean_t     var temporary: boolean_t } ``` |
| To | ``` struct memory_object_attr_info {     var copy_strategy: memory_object_copy_strategy_t     var cluster_size: memory_object_cluster_size_t     var may_cache_object: boolean_t     var temporary: boolean_t     init()     init(copy_strategy copy_strategy: memory_object_copy_strategy_t, cluster_size cluster_size: memory_object_cluster_size_t, may_cache_object may_cache_object: boolean_t, temporary temporary: boolean_t) } ``` |

Modified memory_object_behave_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct memory_object_behave_info {     var copy_strategy: memory_object_copy_strategy_t     var temporary: boolean_t     var invalidate: boolean_t     var silent_overwrite: boolean_t     var advisory_pageout: boolean_t } ``` |
| To | ``` struct memory_object_behave_info {     var copy_strategy: memory_object_copy_strategy_t     var temporary: boolean_t     var invalidate: boolean_t     var silent_overwrite: boolean_t     var advisory_pageout: boolean_t     init()     init(copy_strategy copy_strategy: memory_object_copy_strategy_t, temporary temporary: boolean_t, invalidate invalidate: boolean_t, silent_overwrite silent_overwrite: boolean_t, advisory_pageout advisory_pageout: boolean_t) } ``` |

Modified memory_object_perf_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct memory_object_perf_info {     var cluster_size: memory_object_cluster_size_t     var may_cache: boolean_t } ``` |
| To | ``` struct memory_object_perf_info {     var cluster_size: memory_object_cluster_size_t     var may_cache: boolean_t     init()     init(cluster_size cluster_size: memory_object_cluster_size_t, may_cache may_cache: boolean_t) } ``` |

Modified mig_reply_error_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mig_reply_error_t {     var Head: mach_msg_header_t     var NDR: NDR_record_t     var RetCode: kern_return_t } ``` |
| To | ``` struct mig_reply_error_t {     var Head: mach_msg_header_t     var NDR: NDR_record_t     var RetCode: kern_return_t     init()     init(Head Head: mach_msg_header_t, NDR NDR: NDR_record_t, RetCode RetCode: kern_return_t) } ``` |

Modified mig_subsystem [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mig_subsystem {     var server: mig_server_routine_t     var start: mach_msg_id_t     var end: mach_msg_id_t     var maxsize: mach_msg_size_t     var reserved: vm_address_t     var routine: (mig_routine_descriptor) } ``` |
| To | ``` struct mig_subsystem {     var server: mig_server_routine_t     var start: mach_msg_id_t     var end: mach_msg_id_t     var maxsize: mach_msg_size_t     var reserved: vm_address_t     var routine: (mig_routine_descriptor)     init()     init(server server: mig_server_routine_t, start start: mach_msg_id_t, end end: mach_msg_id_t, maxsize maxsize: mach_msg_size_t, reserved reserved: vm_address_t, routine routine: (mig_routine_descriptor)) } ``` |

Modified mig_symtab [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mig_symtab {     var ms_routine_name: UnsafeMutablePointer<Int8>     var ms_routine_number: Int32     var ms_routine: CFunctionPointer<(() -> Void)> } ``` |
| To | ``` struct mig_symtab {     var ms_routine_name: UnsafeMutablePointer<Int8>     var ms_routine_number: Int32     var ms_routine: CFunctionPointer<(() -> Void)>     init()     init(ms_routine_name ms_routine_name: UnsafeMutablePointer<Int8>, ms_routine_number ms_routine_number: Int32, ms_routine ms_routine: CFunctionPointer<(() -> Void)>) } ``` |

Modified msg [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct msg {     var msg_next: UnsafeMutablePointer<msg>     var msg_type: Int     var msg_ts: UInt16     var msg_spot: Int16     var label: COpaquePointer } ``` |
| To | ``` struct msg {     var msg_next: UnsafeMutablePointer<msg>     var msg_type: Int     var msg_ts: UInt16     var msg_spot: Int16     var label: COpaquePointer     init() } ``` |

Modified msg_labels_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct msg_labels_t {     var sender: mach_port_name_t } ``` |
| To | ``` struct msg_labels_t {     var sender: mach_port_name_t     init()     init(sender sender: mach_port_name_t) } ``` |

Modified msghdr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct msghdr {     var msg_name: UnsafeMutablePointer<Void>     var msg_namelen: socklen_t     var msg_iov: UnsafeMutablePointer<iovec>     var msg_iovlen: Int32     var msg_control: UnsafeMutablePointer<Void>     var msg_controllen: socklen_t     var msg_flags: Int32 } ``` |
| To | ``` struct msghdr {     var msg_name: UnsafeMutablePointer<Void>     var msg_namelen: socklen_t     var msg_iov: UnsafeMutablePointer<iovec>     var msg_iovlen: Int32     var msg_control: UnsafeMutablePointer<Void>     var msg_controllen: socklen_t     var msg_flags: Int32     init()     init(msg_name msg_name: UnsafeMutablePointer<Void>, msg_namelen msg_namelen: socklen_t, msg_iov msg_iov: UnsafeMutablePointer<iovec>, msg_iovlen msg_iovlen: Int32, msg_control msg_control: UnsafeMutablePointer<Void>, msg_controllen msg_controllen: socklen_t, msg_flags msg_flags: Int32) } ``` |

Modified msginfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct msginfo {     var msgmax: Int32     var msgmni: Int32     var msgmnb: Int32     var msgtql: Int32     var msgssz: Int32     var msgseg: Int32 } ``` |
| To | ``` struct msginfo {     var msgmax: Int32     var msgmni: Int32     var msgmnb: Int32     var msgtql: Int32     var msgssz: Int32     var msgseg: Int32     init()     init(msgmax msgmax: Int32, msgmni msgmni: Int32, msgmnb msgmnb: Int32, msgtql msgtql: Int32, msgssz msgssz: Int32, msgseg msgseg: Int32) } ``` |

Modified mstats [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mstats {     var bytes_total: UInt     var chunks_used: UInt     var bytes_used: UInt     var chunks_free: UInt     var bytes_free: UInt } ``` |
| To | ``` struct mstats {     var bytes_total: Int     var chunks_used: Int     var bytes_used: Int     var chunks_free: Int     var bytes_free: Int     init()     init(bytes_total bytes_total: Int, chunks_used chunks_used: Int, bytes_used bytes_used: Int, chunks_free chunks_free: Int, bytes_free bytes_free: Int) } ``` |

Modified mstats.bytes_free

|  | Declaration |
| --- | --- |
| From | ``` var bytes_free: UInt ``` |
| To | ``` var bytes_free: Int ``` |

Modified mstats.bytes_total

|  | Declaration |
| --- | --- |
| From | ``` var bytes_total: UInt ``` |
| To | ``` var bytes_total: Int ``` |

Modified mstats.bytes_used

|  | Declaration |
| --- | --- |
| From | ``` var bytes_used: UInt ``` |
| To | ``` var bytes_used: Int ``` |

Modified mstats.chunks_free

|  | Declaration |
| --- | --- |
| From | ``` var chunks_free: UInt ``` |
| To | ``` var chunks_free: Int ``` |

Modified mstats.chunks_used

|  | Declaration |
| --- | --- |
| From | ``` var chunks_used: UInt ``` |
| To | ``` var chunks_used: Int ``` |

Modified mymsg [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mymsg {     var mtype: Int     var mtext: (Int8) } ``` |
| To | ``` struct mymsg {     var mtype: Int     var mtext: (Int8)     init()     init(mtype mtype: Int, mtext mtext: (Int8)) } ``` |

Modified net_event_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct net_event_data {     var if_family: UInt32     var if_unit: UInt32     var if_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct net_event_data {     var if_family: UInt32     var if_unit: UInt32     var if_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(if_family if_family: UInt32, if_unit if_unit: UInt32, if_name if_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified netent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct netent {     var n_name: UnsafeMutablePointer<Int8>     var n_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var n_addrtype: Int32     var n_net: UInt32 } ``` |
| To | ``` struct netent {     var n_name: UnsafeMutablePointer<Int8>     var n_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var n_addrtype: Int32     var n_net: UInt32     init()     init(n_name n_name: UnsafeMutablePointer<Int8>, n_aliases n_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, n_addrtype n_addrtype: Int32, n_net n_net: UInt32) } ``` |

Modified netfs_status [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct netfs_status {     var ns_status: UInt32     var ns_mountopts: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ns_waittime: UInt32     var ns_threadcount: UInt32     var ns_threadids: () } ``` |
| To | ```  ``` |

Modified ntsid_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ntsid_t {     var sid_kind: UInt8     var sid_authcount: UInt8     var sid_authority: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var sid_authorities: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32) } ``` |
| To | ``` struct ntsid_t {     var sid_kind: UInt8     var sid_authcount: UInt8     var sid_authority: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var sid_authorities: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)     init()     init(sid_kind sid_kind: UInt8, sid_authcount sid_authcount: UInt8, sid_authority sid_authority: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), sid_authorities sid_authorities: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified option [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct option {     var name: UnsafePointer<Int8>     var has_arg: Int32     var flag: UnsafeMutablePointer<Int32>     var val: Int32 } ``` |
| To | ``` struct option {     var name: UnsafePointer<Int8>     var has_arg: Int32     var flag: UnsafeMutablePointer<Int32>     var val: Int32     init()     init(name name: UnsafePointer<Int8>, has_arg has_arg: Int32, flag flag: UnsafeMutablePointer<Int32>, val val: Int32) } ``` |

Modified ostat [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ostat {     var st_dev: __uint16_t     var st_ino: ino_t     var st_mode: mode_t     var st_nlink: nlink_t     var st_uid: __uint16_t     var st_gid: __uint16_t     var st_rdev: __uint16_t     var st_size: __int32_t     var st_atimespec: timespec     var st_mtimespec: timespec     var st_ctimespec: timespec     var st_blksize: __int32_t     var st_blocks: __int32_t     var st_flags: __uint32_t     var st_gen: __uint32_t } ``` |
| To | ``` struct ostat {     var st_dev: __uint16_t     var st_ino: ino_t     var st_mode: mode_t     var st_nlink: nlink_t     var st_uid: __uint16_t     var st_gid: __uint16_t     var st_rdev: __uint16_t     var st_size: __int32_t     var st_atimespec: timespec     var st_mtimespec: timespec     var st_ctimespec: timespec     var st_blksize: __int32_t     var st_blocks: __int32_t     var st_flags: __uint32_t     var st_gen: __uint32_t     init()     init(st_dev st_dev: __uint16_t, st_ino st_ino: ino_t, st_mode st_mode: mode_t, st_nlink st_nlink: nlink_t, st_uid st_uid: __uint16_t, st_gid st_gid: __uint16_t, st_rdev st_rdev: __uint16_t, st_size st_size: __int32_t, st_atimespec st_atimespec: timespec, st_mtimespec st_mtimespec: timespec, st_ctimespec st_ctimespec: timespec, st_blksize st_blksize: __int32_t, st_blocks st_blocks: __int32_t, st_flags st_flags: __uint32_t, st_gen st_gen: __uint32_t) } ``` |

Modified passwd [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct passwd {     var pw_name: UnsafeMutablePointer<Int8>     var pw_passwd: UnsafeMutablePointer<Int8>     var pw_uid: uid_t     var pw_gid: gid_t     var pw_change: __darwin_time_t     var pw_class: UnsafeMutablePointer<Int8>     var pw_gecos: UnsafeMutablePointer<Int8>     var pw_dir: UnsafeMutablePointer<Int8>     var pw_shell: UnsafeMutablePointer<Int8>     var pw_expire: __darwin_time_t } ``` |
| To | ``` struct passwd {     var pw_name: UnsafeMutablePointer<Int8>     var pw_passwd: UnsafeMutablePointer<Int8>     var pw_uid: uid_t     var pw_gid: gid_t     var pw_change: __darwin_time_t     var pw_class: UnsafeMutablePointer<Int8>     var pw_gecos: UnsafeMutablePointer<Int8>     var pw_dir: UnsafeMutablePointer<Int8>     var pw_shell: UnsafeMutablePointer<Int8>     var pw_expire: __darwin_time_t     init()     init(pw_name pw_name: UnsafeMutablePointer<Int8>, pw_passwd pw_passwd: UnsafeMutablePointer<Int8>, pw_uid pw_uid: uid_t, pw_gid pw_gid: gid_t, pw_change pw_change: __darwin_time_t, pw_class pw_class: UnsafeMutablePointer<Int8>, pw_gecos pw_gecos: UnsafeMutablePointer<Int8>, pw_dir pw_dir: UnsafeMutablePointer<Int8>, pw_shell pw_shell: UnsafeMutablePointer<Int8>, pw_expire pw_expire: __darwin_time_t) } ``` |

Modified policy_bases [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct policy_bases {     var ts: policy_timeshare_base_data_t     var rr: policy_rr_base_data_t     var fifo: policy_fifo_base_data_t } ``` |
| To | ``` struct policy_bases {     var ts: policy_timeshare_base_data_t     var rr: policy_rr_base_data_t     var fifo: policy_fifo_base_data_t     init()     init(ts ts: policy_timeshare_base_data_t, rr rr: policy_rr_base_data_t, fifo fifo: policy_fifo_base_data_t) } ``` |

Modified policy_fifo_base [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct policy_fifo_base {     var base_priority: integer_t } ``` |
| To | ``` struct policy_fifo_base {     var base_priority: integer_t     init()     init(base_priority base_priority: integer_t) } ``` |

Modified policy_fifo_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct policy_fifo_info {     var max_priority: integer_t     var base_priority: integer_t     var depressed: boolean_t     var depress_priority: integer_t } ``` |
| To | ``` struct policy_fifo_info {     var max_priority: integer_t     var base_priority: integer_t     var depressed: boolean_t     var depress_priority: integer_t     init()     init(max_priority max_priority: integer_t, base_priority base_priority: integer_t, depressed depressed: boolean_t, depress_priority depress_priority: integer_t) } ``` |

Modified policy_fifo_limit [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct policy_fifo_limit {     var max_priority: integer_t } ``` |
| To | ``` struct policy_fifo_limit {     var max_priority: integer_t     init()     init(max_priority max_priority: integer_t) } ``` |

Modified policy_infos [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct policy_infos {     var ts: policy_timeshare_info_data_t     var rr: policy_rr_info_data_t     var fifo: policy_fifo_info_data_t } ``` |
| To | ``` struct policy_infos {     var ts: policy_timeshare_info_data_t     var rr: policy_rr_info_data_t     var fifo: policy_fifo_info_data_t     init()     init(ts ts: policy_timeshare_info_data_t, rr rr: policy_rr_info_data_t, fifo fifo: policy_fifo_info_data_t) } ``` |

Modified policy_limits [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct policy_limits {     var ts: policy_timeshare_limit_data_t     var rr: policy_rr_limit_data_t     var fifo: policy_fifo_limit_data_t } ``` |
| To | ``` struct policy_limits {     var ts: policy_timeshare_limit_data_t     var rr: policy_rr_limit_data_t     var fifo: policy_fifo_limit_data_t     init()     init(ts ts: policy_timeshare_limit_data_t, rr rr: policy_rr_limit_data_t, fifo fifo: policy_fifo_limit_data_t) } ``` |

Modified policy_rr_base [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct policy_rr_base {     var base_priority: integer_t     var quantum: integer_t } ``` |
| To | ``` struct policy_rr_base {     var base_priority: integer_t     var quantum: integer_t     init()     init(base_priority base_priority: integer_t, quantum quantum: integer_t) } ``` |

Modified policy_rr_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct policy_rr_info {     var max_priority: integer_t     var base_priority: integer_t     var quantum: integer_t     var depressed: boolean_t     var depress_priority: integer_t } ``` |
| To | ``` struct policy_rr_info {     var max_priority: integer_t     var base_priority: integer_t     var quantum: integer_t     var depressed: boolean_t     var depress_priority: integer_t     init()     init(max_priority max_priority: integer_t, base_priority base_priority: integer_t, quantum quantum: integer_t, depressed depressed: boolean_t, depress_priority depress_priority: integer_t) } ``` |

Modified policy_rr_limit [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct policy_rr_limit {     var max_priority: integer_t } ``` |
| To | ``` struct policy_rr_limit {     var max_priority: integer_t     init()     init(max_priority max_priority: integer_t) } ``` |

Modified policy_timeshare_base [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct policy_timeshare_base {     var base_priority: integer_t } ``` |
| To | ``` struct policy_timeshare_base {     var base_priority: integer_t     init()     init(base_priority base_priority: integer_t) } ``` |

Modified policy_timeshare_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct policy_timeshare_info {     var max_priority: integer_t     var base_priority: integer_t     var cur_priority: integer_t     var depressed: boolean_t     var depress_priority: integer_t } ``` |
| To | ``` struct policy_timeshare_info {     var max_priority: integer_t     var base_priority: integer_t     var cur_priority: integer_t     var depressed: boolean_t     var depress_priority: integer_t     init()     init(max_priority max_priority: integer_t, base_priority base_priority: integer_t, cur_priority cur_priority: integer_t, depressed depressed: boolean_t, depress_priority depress_priority: integer_t) } ``` |

Modified policy_timeshare_limit [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct policy_timeshare_limit {     var max_priority: integer_t } ``` |
| To | ``` struct policy_timeshare_limit {     var max_priority: integer_t     init()     init(max_priority max_priority: integer_t) } ``` |

Modified pollfd [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct pollfd {     var fd: Int32     var events: Int16     var revents: Int16 } ``` |
| To | ``` struct pollfd {     var fd: Int32     var events: Int16     var revents: Int16     init()     init(fd fd: Int32, events events: Int16, revents revents: Int16) } ``` |

Modified port_obj_tentry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct port_obj_tentry {     var pos_value: UnsafeMutablePointer<Void>     var pos_type: Int32 } ``` |
| To | ``` struct port_obj_tentry {     var pos_value: UnsafeMutablePointer<Void>     var pos_type: Int32     init()     init(pos_value pos_value: UnsafeMutablePointer<Void>, pos_type pos_type: Int32) } ``` |

Modified proc_rlimit_control_wakeupmon [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct proc_rlimit_control_wakeupmon {     var wm_flags: UInt32     var wm_rate: Int32 } ``` |
| To | ``` struct proc_rlimit_control_wakeupmon {     var wm_flags: UInt32     var wm_rate: Int32     init()     init(wm_flags wm_flags: UInt32, wm_rate wm_rate: Int32) } ``` |

Modified processor_basic_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct processor_basic_info {     var cpu_type: cpu_type_t     var cpu_subtype: cpu_subtype_t     var running: boolean_t     var slot_num: Int32     var is_master: boolean_t } ``` |
| To | ``` struct processor_basic_info {     var cpu_type: cpu_type_t     var cpu_subtype: cpu_subtype_t     var running: boolean_t     var slot_num: Int32     var is_master: boolean_t     init()     init(cpu_type cpu_type: cpu_type_t, cpu_subtype cpu_subtype: cpu_subtype_t, running running: boolean_t, slot_num slot_num: Int32, is_master is_master: boolean_t) } ``` |

Modified processor_cpu_load_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct processor_cpu_load_info {     var cpu_ticks: (UInt32, UInt32, UInt32, UInt32) } ``` |
| To | ``` struct processor_cpu_load_info {     var cpu_ticks: (UInt32, UInt32, UInt32, UInt32)     init()     init(cpu_ticks cpu_ticks: (UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified processor_cpu_stat [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct processor_cpu_stat {     var irq_ex_cnt: UInt32     var ipi_cnt: UInt32     var timer_cnt: UInt32     var undef_ex_cnt: UInt32     var unaligned_cnt: UInt32     var vfp_cnt: UInt32     var vfp_shortv_cnt: UInt32     var data_ex_cnt: UInt32     var instr_ex_cnt: UInt32 } ``` |
| To | ``` struct processor_cpu_stat {     var irq_ex_cnt: UInt32     var ipi_cnt: UInt32     var timer_cnt: UInt32     var undef_ex_cnt: UInt32     var unaligned_cnt: UInt32     var vfp_cnt: UInt32     var vfp_shortv_cnt: UInt32     var data_ex_cnt: UInt32     var instr_ex_cnt: UInt32     init()     init(irq_ex_cnt irq_ex_cnt: UInt32, ipi_cnt ipi_cnt: UInt32, timer_cnt timer_cnt: UInt32, undef_ex_cnt undef_ex_cnt: UInt32, unaligned_cnt unaligned_cnt: UInt32, vfp_cnt vfp_cnt: UInt32, vfp_shortv_cnt vfp_shortv_cnt: UInt32, data_ex_cnt data_ex_cnt: UInt32, instr_ex_cnt instr_ex_cnt: UInt32) } ``` |

Modified processor_set_basic_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct processor_set_basic_info {     var processor_count: Int32     var default_policy: Int32 } ``` |
| To | ``` struct processor_set_basic_info {     var processor_count: Int32     var default_policy: Int32     init()     init(processor_count processor_count: Int32, default_policy default_policy: Int32) } ``` |

Modified processor_set_load_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct processor_set_load_info {     var task_count: Int32     var thread_count: Int32     var load_average: integer_t     var mach_factor: integer_t } ``` |
| To | ``` struct processor_set_load_info {     var task_count: Int32     var thread_count: Int32     var load_average: integer_t     var mach_factor: integer_t     init()     init(task_count task_count: Int32, thread_count thread_count: Int32, load_average load_average: integer_t, mach_factor mach_factor: integer_t) } ``` |

Modified protoent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct protoent {     var p_name: UnsafeMutablePointer<Int8>     var p_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var p_proto: Int32 } ``` |
| To | ``` struct protoent {     var p_name: UnsafeMutablePointer<Int8>     var p_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var p_proto: Int32     init()     init(p_name p_name: UnsafeMutablePointer<Int8>, p_aliases p_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, p_proto p_proto: Int32) } ``` |

Modified radvisory [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct radvisory {     var ra_offset: off_t     var ra_count: Int32 } ``` |
| To | ``` struct radvisory {     var ra_offset: off_t     var ra_count: Int32     init()     init(ra_offset ra_offset: off_t, ra_count ra_count: Int32) } ``` |

Modified rb_node [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rb_node {     var opaque: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct rb_node {     var opaque: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)     init()     init(opaque opaque: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)) } ``` |

Modified rb_tree [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rb_tree {     var opaque: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct rb_tree {     var opaque: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)     init()     init(opaque opaque: (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>)) } ``` |

Modified rb_tree_ops_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rb_tree_ops_t {     var rbto_compare_nodes: rbto_compare_nodes_fn     var rbto_compare_key: rbto_compare_key_fn     var rbto_node_offset: UInt     var rbto_context: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct rb_tree_ops_t {     var rbto_compare_nodes: rbto_compare_nodes_fn     var rbto_compare_key: rbto_compare_key_fn     var rbto_node_offset: Int     var rbto_context: UnsafeMutablePointer<Void>     init()     init(rbto_compare_nodes rbto_compare_nodes: rbto_compare_nodes_fn, rbto_compare_key rbto_compare_key: rbto_compare_key_fn, rbto_node_offset rbto_node_offset: Int, rbto_context rbto_context: UnsafeMutablePointer<Void>) } ``` |

Modified rb_tree_ops_t.rbto_node_offset

|  | Declaration |
| --- | --- |
| From | ``` var rbto_node_offset: UInt ``` |
| To | ``` var rbto_node_offset: Int ``` |

Modified regex_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct regex_t {     var re_magic: Int32     var re_nsub: UInt     var re_endp: UnsafePointer<Int8>     var re_g: COpaquePointer } ``` |
| To | ``` struct regex_t {     var re_magic: Int32     var re_nsub: Int     var re_endp: UnsafePointer<Int8>     var re_g: COpaquePointer     init() } ``` |

Modified regex_t.re_nsub

|  | Declaration |
| --- | --- |
| From | ``` var re_nsub: UInt ``` |
| To | ``` var re_nsub: Int ``` |

Modified regmatch_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct regmatch_t {     var rm_so: regoff_t     var rm_eo: regoff_t } ``` |
| To | ``` struct regmatch_t {     var rm_so: regoff_t     var rm_eo: regoff_t     init()     init(rm_so rm_so: regoff_t, rm_eo rm_eo: regoff_t) } ``` |

Modified rlimit [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rlimit {     var rlim_cur: rlim_t     var rlim_max: rlim_t } ``` |
| To | ``` struct rlimit {     var rlim_cur: rlim_t     var rlim_max: rlim_t     init()     init(rlim_cur rlim_cur: rlim_t, rlim_max rlim_max: rlim_t) } ``` |

Modified routine_descriptor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct routine_descriptor {     var impl_routine: mig_impl_routine_t     var stub_routine: mig_stub_routine_t     var argc: UInt32     var descr_count: UInt32     var arg_descr: routine_arg_descriptor_t     var max_reply_msg: UInt32 } ``` |
| To | ``` struct routine_descriptor {     var impl_routine: mig_impl_routine_t     var stub_routine: mig_stub_routine_t     var argc: UInt32     var descr_count: UInt32     var arg_descr: routine_arg_descriptor_t     var max_reply_msg: UInt32     init()     init(impl_routine impl_routine: mig_impl_routine_t, stub_routine stub_routine: mig_stub_routine_t, argc argc: UInt32, descr_count descr_count: UInt32, arg_descr arg_descr: routine_arg_descriptor_t, max_reply_msg max_reply_msg: UInt32) } ``` |

Modified rpc_routine_arg_descriptor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rpc_routine_arg_descriptor {     var type: routine_arg_type     var size: routine_arg_size     var count: routine_arg_size     var offset: routine_arg_offset } ``` |
| To | ``` struct rpc_routine_arg_descriptor {     var type: routine_arg_type     var size: routine_arg_size     var count: routine_arg_size     var offset: routine_arg_offset     init()     init(type type: routine_arg_type, size size: routine_arg_size, count count: routine_arg_size, offset offset: routine_arg_offset) } ``` |

Modified rpc_routine_descriptor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rpc_routine_descriptor {     var impl_routine: mig_impl_routine_t     var stub_routine: mig_stub_routine_t     var argc: UInt32     var descr_count: UInt32     var arg_descr: rpc_routine_arg_descriptor_t     var max_reply_msg: UInt32 } ``` |
| To | ``` struct rpc_routine_descriptor {     var impl_routine: mig_impl_routine_t     var stub_routine: mig_stub_routine_t     var argc: UInt32     var descr_count: UInt32     var arg_descr: rpc_routine_arg_descriptor_t     var max_reply_msg: UInt32     init()     init(impl_routine impl_routine: mig_impl_routine_t, stub_routine stub_routine: mig_stub_routine_t, argc argc: UInt32, descr_count descr_count: UInt32, arg_descr arg_descr: rpc_routine_arg_descriptor_t, max_reply_msg max_reply_msg: UInt32) } ``` |

Modified rpc_signature [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rpc_signature {     var rd: rpc_routine_descriptor     var rad: (rpc_routine_arg_descriptor) } ``` |
| To | ``` struct rpc_signature {     var rd: rpc_routine_descriptor     var rad: (rpc_routine_arg_descriptor)     init()     init(rd rd: rpc_routine_descriptor, rad rad: (rpc_routine_arg_descriptor)) } ``` |

Modified rpc_subsystem [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rpc_subsystem {     var reserved: UnsafeMutablePointer<Void>     var start: mach_msg_id_t     var end: mach_msg_id_t     var maxsize: UInt32     var base_addr: vm_address_t     var routine: (rpc_routine_descriptor)     var arg_descriptor: (rpc_routine_arg_descriptor) } ``` |
| To | ``` struct rpc_subsystem {     var reserved: UnsafeMutablePointer<Void>     var start: mach_msg_id_t     var end: mach_msg_id_t     var maxsize: UInt32     var base_addr: vm_address_t     var routine: (rpc_routine_descriptor)     var arg_descriptor: (rpc_routine_arg_descriptor)     init()     init(reserved reserved: UnsafeMutablePointer<Void>, start start: mach_msg_id_t, end end: mach_msg_id_t, maxsize maxsize: UInt32, base_addr base_addr: vm_address_t, routine routine: (rpc_routine_descriptor), arg_descriptor arg_descriptor: (rpc_routine_arg_descriptor)) } ``` |

Modified rpcent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rpcent {     var r_name: UnsafeMutablePointer<Int8>     var r_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var r_number: Int32 } ``` |
| To | ``` struct rpcent {     var r_name: UnsafeMutablePointer<Int8>     var r_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var r_number: Int32     init()     init(r_name r_name: UnsafeMutablePointer<Int8>, r_aliases r_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, r_number r_number: Int32) } ``` |

Modified rslvmulti_req [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rslvmulti_req {     var sa: UnsafeMutablePointer<sockaddr>     var llsa: UnsafeMutablePointer<UnsafeMutablePointer<sockaddr>> } ``` |
| To | ``` struct rslvmulti_req {     var sa: UnsafeMutablePointer<sockaddr>     var llsa: UnsafeMutablePointer<UnsafeMutablePointer<sockaddr>>     init()     init(sa sa: UnsafeMutablePointer<sockaddr>, llsa llsa: UnsafeMutablePointer<UnsafeMutablePointer<sockaddr>>) } ``` |

Modified rusage [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rusage {     var ru_utime: timeval     var ru_stime: timeval     var ru_maxrss: Int     var ru_ixrss: Int     var ru_idrss: Int     var ru_isrss: Int     var ru_minflt: Int     var ru_majflt: Int     var ru_nswap: Int     var ru_inblock: Int     var ru_oublock: Int     var ru_msgsnd: Int     var ru_msgrcv: Int     var ru_nsignals: Int     var ru_nvcsw: Int     var ru_nivcsw: Int } ``` |
| To | ``` struct rusage {     var ru_utime: timeval     var ru_stime: timeval     var ru_maxrss: Int     var ru_ixrss: Int     var ru_idrss: Int     var ru_isrss: Int     var ru_minflt: Int     var ru_majflt: Int     var ru_nswap: Int     var ru_inblock: Int     var ru_oublock: Int     var ru_msgsnd: Int     var ru_msgrcv: Int     var ru_nsignals: Int     var ru_nvcsw: Int     var ru_nivcsw: Int     init()     init(ru_utime ru_utime: timeval, ru_stime ru_stime: timeval, ru_maxrss ru_maxrss: Int, ru_ixrss ru_ixrss: Int, ru_idrss ru_idrss: Int, ru_isrss ru_isrss: Int, ru_minflt ru_minflt: Int, ru_majflt ru_majflt: Int, ru_nswap ru_nswap: Int, ru_inblock ru_inblock: Int, ru_oublock ru_oublock: Int, ru_msgsnd ru_msgsnd: Int, ru_msgrcv ru_msgrcv: Int, ru_nsignals ru_nsignals: Int, ru_nvcsw ru_nvcsw: Int, ru_nivcsw ru_nivcsw: Int) } ``` |

Modified rusage_info_v0 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rusage_info_v0 {     var ri_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var ri_user_time: UInt64     var ri_system_time: UInt64     var ri_pkg_idle_wkups: UInt64     var ri_interrupt_wkups: UInt64     var ri_pageins: UInt64     var ri_wired_size: UInt64     var ri_resident_size: UInt64     var ri_phys_footprint: UInt64     var ri_proc_start_abstime: UInt64     var ri_proc_exit_abstime: UInt64 } ``` |
| To | ``` struct rusage_info_v0 {     var ri_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var ri_user_time: UInt64     var ri_system_time: UInt64     var ri_pkg_idle_wkups: UInt64     var ri_interrupt_wkups: UInt64     var ri_pageins: UInt64     var ri_wired_size: UInt64     var ri_resident_size: UInt64     var ri_phys_footprint: UInt64     var ri_proc_start_abstime: UInt64     var ri_proc_exit_abstime: UInt64     init()     init(ri_uuid ri_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), ri_user_time ri_user_time: UInt64, ri_system_time ri_system_time: UInt64, ri_pkg_idle_wkups ri_pkg_idle_wkups: UInt64, ri_interrupt_wkups ri_interrupt_wkups: UInt64, ri_pageins ri_pageins: UInt64, ri_wired_size ri_wired_size: UInt64, ri_resident_size ri_resident_size: UInt64, ri_phys_footprint ri_phys_footprint: UInt64, ri_proc_start_abstime ri_proc_start_abstime: UInt64, ri_proc_exit_abstime ri_proc_exit_abstime: UInt64) } ``` |

Modified rusage_info_v1 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rusage_info_v1 {     var ri_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var ri_user_time: UInt64     var ri_system_time: UInt64     var ri_pkg_idle_wkups: UInt64     var ri_interrupt_wkups: UInt64     var ri_pageins: UInt64     var ri_wired_size: UInt64     var ri_resident_size: UInt64     var ri_phys_footprint: UInt64     var ri_proc_start_abstime: UInt64     var ri_proc_exit_abstime: UInt64     var ri_child_user_time: UInt64     var ri_child_system_time: UInt64     var ri_child_pkg_idle_wkups: UInt64     var ri_child_interrupt_wkups: UInt64     var ri_child_pageins: UInt64     var ri_child_elapsed_abstime: UInt64 } ``` |
| To | ``` struct rusage_info_v1 {     var ri_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var ri_user_time: UInt64     var ri_system_time: UInt64     var ri_pkg_idle_wkups: UInt64     var ri_interrupt_wkups: UInt64     var ri_pageins: UInt64     var ri_wired_size: UInt64     var ri_resident_size: UInt64     var ri_phys_footprint: UInt64     var ri_proc_start_abstime: UInt64     var ri_proc_exit_abstime: UInt64     var ri_child_user_time: UInt64     var ri_child_system_time: UInt64     var ri_child_pkg_idle_wkups: UInt64     var ri_child_interrupt_wkups: UInt64     var ri_child_pageins: UInt64     var ri_child_elapsed_abstime: UInt64     init()     init(ri_uuid ri_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), ri_user_time ri_user_time: UInt64, ri_system_time ri_system_time: UInt64, ri_pkg_idle_wkups ri_pkg_idle_wkups: UInt64, ri_interrupt_wkups ri_interrupt_wkups: UInt64, ri_pageins ri_pageins: UInt64, ri_wired_size ri_wired_size: UInt64, ri_resident_size ri_resident_size: UInt64, ri_phys_footprint ri_phys_footprint: UInt64, ri_proc_start_abstime ri_proc_start_abstime: UInt64, ri_proc_exit_abstime ri_proc_exit_abstime: UInt64, ri_child_user_time ri_child_user_time: UInt64, ri_child_system_time ri_child_system_time: UInt64, ri_child_pkg_idle_wkups ri_child_pkg_idle_wkups: UInt64, ri_child_interrupt_wkups ri_child_interrupt_wkups: UInt64, ri_child_pageins ri_child_pageins: UInt64, ri_child_elapsed_abstime ri_child_elapsed_abstime: UInt64) } ``` |

Modified rusage_info_v2 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rusage_info_v2 {     var ri_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var ri_user_time: UInt64     var ri_system_time: UInt64     var ri_pkg_idle_wkups: UInt64     var ri_interrupt_wkups: UInt64     var ri_pageins: UInt64     var ri_wired_size: UInt64     var ri_resident_size: UInt64     var ri_phys_footprint: UInt64     var ri_proc_start_abstime: UInt64     var ri_proc_exit_abstime: UInt64     var ri_child_user_time: UInt64     var ri_child_system_time: UInt64     var ri_child_pkg_idle_wkups: UInt64     var ri_child_interrupt_wkups: UInt64     var ri_child_pageins: UInt64     var ri_child_elapsed_abstime: UInt64     var ri_diskio_bytesread: UInt64     var ri_diskio_byteswritten: UInt64 } ``` |
| To | ``` struct rusage_info_v2 {     var ri_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var ri_user_time: UInt64     var ri_system_time: UInt64     var ri_pkg_idle_wkups: UInt64     var ri_interrupt_wkups: UInt64     var ri_pageins: UInt64     var ri_wired_size: UInt64     var ri_resident_size: UInt64     var ri_phys_footprint: UInt64     var ri_proc_start_abstime: UInt64     var ri_proc_exit_abstime: UInt64     var ri_child_user_time: UInt64     var ri_child_system_time: UInt64     var ri_child_pkg_idle_wkups: UInt64     var ri_child_interrupt_wkups: UInt64     var ri_child_pageins: UInt64     var ri_child_elapsed_abstime: UInt64     var ri_diskio_bytesread: UInt64     var ri_diskio_byteswritten: UInt64     init()     init(ri_uuid ri_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), ri_user_time ri_user_time: UInt64, ri_system_time ri_system_time: UInt64, ri_pkg_idle_wkups ri_pkg_idle_wkups: UInt64, ri_interrupt_wkups ri_interrupt_wkups: UInt64, ri_pageins ri_pageins: UInt64, ri_wired_size ri_wired_size: UInt64, ri_resident_size ri_resident_size: UInt64, ri_phys_footprint ri_phys_footprint: UInt64, ri_proc_start_abstime ri_proc_start_abstime: UInt64, ri_proc_exit_abstime ri_proc_exit_abstime: UInt64, ri_child_user_time ri_child_user_time: UInt64, ri_child_system_time ri_child_system_time: UInt64, ri_child_pkg_idle_wkups ri_child_pkg_idle_wkups: UInt64, ri_child_interrupt_wkups ri_child_interrupt_wkups: UInt64, ri_child_pageins ri_child_pageins: UInt64, ri_child_elapsed_abstime ri_child_elapsed_abstime: UInt64, ri_diskio_bytesread ri_diskio_bytesread: UInt64, ri_diskio_byteswritten ri_diskio_byteswritten: UInt64) } ``` |

Modified rusage_info_v3 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rusage_info_v3 {     var ri_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var ri_user_time: UInt64     var ri_system_time: UInt64     var ri_pkg_idle_wkups: UInt64     var ri_interrupt_wkups: UInt64     var ri_pageins: UInt64     var ri_wired_size: UInt64     var ri_resident_size: UInt64     var ri_phys_footprint: UInt64     var ri_proc_start_abstime: UInt64     var ri_proc_exit_abstime: UInt64     var ri_child_user_time: UInt64     var ri_child_system_time: UInt64     var ri_child_pkg_idle_wkups: UInt64     var ri_child_interrupt_wkups: UInt64     var ri_child_pageins: UInt64     var ri_child_elapsed_abstime: UInt64     var ri_diskio_bytesread: UInt64     var ri_diskio_byteswritten: UInt64     var ri_cpu_time_qos_default: UInt64     var ri_cpu_time_qos_maintenance: UInt64     var ri_cpu_time_qos_background: UInt64     var ri_cpu_time_qos_utility: UInt64     var ri_cpu_time_qos_legacy: UInt64     var ri_cpu_time_qos_user_initiated: UInt64     var ri_cpu_time_qos_user_interactive: UInt64     var ri_billed_system_time: UInt64     var ri_serviced_system_time: UInt64 } ``` |
| To | ``` struct rusage_info_v3 {     var ri_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var ri_user_time: UInt64     var ri_system_time: UInt64     var ri_pkg_idle_wkups: UInt64     var ri_interrupt_wkups: UInt64     var ri_pageins: UInt64     var ri_wired_size: UInt64     var ri_resident_size: UInt64     var ri_phys_footprint: UInt64     var ri_proc_start_abstime: UInt64     var ri_proc_exit_abstime: UInt64     var ri_child_user_time: UInt64     var ri_child_system_time: UInt64     var ri_child_pkg_idle_wkups: UInt64     var ri_child_interrupt_wkups: UInt64     var ri_child_pageins: UInt64     var ri_child_elapsed_abstime: UInt64     var ri_diskio_bytesread: UInt64     var ri_diskio_byteswritten: UInt64     var ri_cpu_time_qos_default: UInt64     var ri_cpu_time_qos_maintenance: UInt64     var ri_cpu_time_qos_background: UInt64     var ri_cpu_time_qos_utility: UInt64     var ri_cpu_time_qos_legacy: UInt64     var ri_cpu_time_qos_user_initiated: UInt64     var ri_cpu_time_qos_user_interactive: UInt64     var ri_billed_system_time: UInt64     var ri_serviced_system_time: UInt64     init()     init(ri_uuid ri_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), ri_user_time ri_user_time: UInt64, ri_system_time ri_system_time: UInt64, ri_pkg_idle_wkups ri_pkg_idle_wkups: UInt64, ri_interrupt_wkups ri_interrupt_wkups: UInt64, ri_pageins ri_pageins: UInt64, ri_wired_size ri_wired_size: UInt64, ri_resident_size ri_resident_size: UInt64, ri_phys_footprint ri_phys_footprint: UInt64, ri_proc_start_abstime ri_proc_start_abstime: UInt64, ri_proc_exit_abstime ri_proc_exit_abstime: UInt64, ri_child_user_time ri_child_user_time: UInt64, ri_child_system_time ri_child_system_time: UInt64, ri_child_pkg_idle_wkups ri_child_pkg_idle_wkups: UInt64, ri_child_interrupt_wkups ri_child_interrupt_wkups: UInt64, ri_child_pageins ri_child_pageins: UInt64, ri_child_elapsed_abstime ri_child_elapsed_abstime: UInt64, ri_diskio_bytesread ri_diskio_bytesread: UInt64, ri_diskio_byteswritten ri_diskio_byteswritten: UInt64, ri_cpu_time_qos_default ri_cpu_time_qos_default: UInt64, ri_cpu_time_qos_maintenance ri_cpu_time_qos_maintenance: UInt64, ri_cpu_time_qos_background ri_cpu_time_qos_background: UInt64, ri_cpu_time_qos_utility ri_cpu_time_qos_utility: UInt64, ri_cpu_time_qos_legacy ri_cpu_time_qos_legacy: UInt64, ri_cpu_time_qos_user_initiated ri_cpu_time_qos_user_initiated: UInt64, ri_cpu_time_qos_user_interactive ri_cpu_time_qos_user_interactive: UInt64, ri_billed_system_time ri_billed_system_time: UInt64, ri_serviced_system_time ri_serviced_system_time: UInt64) } ``` |

Modified sched_param [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sched_param {     var sched_priority: Int32     var __opaque: (Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct sched_param {     var sched_priority: Int32     var __opaque: (Int8, Int8, Int8, Int8)     init()     init(sched_priority sched_priority: Int32, __opaque __opaque: (Int8, Int8, Int8, Int8)) } ``` |

Modified searchstate [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct searchstate {     var ss_union_flags: UInt32     var ss_union_layer: UInt32     var ss_fsstate: (u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char, u_char) } ``` |
| To | ```  ``` |

Modified security_token_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct security_token_t {     var val: (UInt32, UInt32) } ``` |
| To | ``` struct security_token_t {     var val: (UInt32, UInt32)     init()     init(val val: (UInt32, UInt32)) } ``` |

Modified sem [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sem {     var semval: UInt16     var sempid: pid_t     var semncnt: UInt16     var semzcnt: UInt16 } ``` |
| To | ``` struct sem {     var semval: UInt16     var sempid: pid_t     var semncnt: UInt16     var semzcnt: UInt16     init()     init(semval semval: UInt16, sempid sempid: pid_t, semncnt semncnt: UInt16, semzcnt semzcnt: UInt16) } ``` |

Modified sembuf [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sembuf {     var sem_num: UInt16     var sem_op: Int16     var sem_flg: Int16 } ``` |
| To | ``` struct sembuf {     var sem_num: UInt16     var sem_op: Int16     var sem_flg: Int16     init()     init(sem_num sem_num: UInt16, sem_op sem_op: Int16, sem_flg sem_flg: Int16) } ``` |

Modified servent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct servent {     var s_name: UnsafeMutablePointer<Int8>     var s_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var s_port: Int32     var s_proto: UnsafeMutablePointer<Int8> } ``` |
| To | ``` struct servent {     var s_name: UnsafeMutablePointer<Int8>     var s_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var s_port: Int32     var s_proto: UnsafeMutablePointer<Int8>     init()     init(s_name s_name: UnsafeMutablePointer<Int8>, s_aliases s_aliases: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, s_port s_port: Int32, s_proto s_proto: UnsafeMutablePointer<Int8>) } ``` |

Modified sf_hdtr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sf_hdtr {     var headers: UnsafeMutablePointer<iovec>     var hdr_cnt: Int32     var trailers: UnsafeMutablePointer<iovec>     var trl_cnt: Int32 } ``` |
| To | ``` struct sf_hdtr {     var headers: UnsafeMutablePointer<iovec>     var hdr_cnt: Int32     var trailers: UnsafeMutablePointer<iovec>     var trl_cnt: Int32     init()     init(headers headers: UnsafeMutablePointer<iovec>, hdr_cnt hdr_cnt: Int32, trailers trailers: UnsafeMutablePointer<iovec>, trl_cnt trl_cnt: Int32) } ``` |

Modified sigaction [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sigaction {     var sa_mask: sigset_t     var sa_flags: Int32 } ``` |
| To | ``` struct sigaction {     var __sigaction_u: __sigaction_u     var sa_mask: sigset_t     var sa_flags: Int32     init()     init(__sigaction_u __sigaction_u: __sigaction_u, sa_mask sa_mask: sigset_t, sa_flags sa_flags: Int32) } ``` |

Modified sigevent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sigevent {     var sigev_notify: Int32     var sigev_signo: Int32     var sigev_notify_function: COpaquePointer     var sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t> } ``` |
| To | ``` struct sigevent {     var sigev_notify: Int32     var sigev_signo: Int32     var sigev_value: sigval     var sigev_notify_function: CFunctionPointer<((sigval) -> Void)>     var sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t>     init()     init(sigev_notify sigev_notify: Int32, sigev_signo sigev_signo: Int32, sigev_value sigev_value: sigval, sigev_notify_function sigev_notify_function: CFunctionPointer<((sigval) -> Void)>, sigev_notify_attributes sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t>) } ``` |

Modified sigevent.sigev_notify_function

|  | Declaration |
| --- | --- |
| From | ``` var sigev_notify_function: COpaquePointer ``` |
| To | ``` var sigev_notify_function: CFunctionPointer<((sigval) -> Void)> ``` |

Modified sigstack [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sigstack {     var ss_sp: UnsafeMutablePointer<Int8>     var ss_onstack: Int32 } ``` |
| To | ``` struct sigstack {     var ss_sp: UnsafeMutablePointer<Int8>     var ss_onstack: Int32     init()     init(ss_sp ss_sp: UnsafeMutablePointer<Int8>, ss_onstack ss_onstack: Int32) } ``` |

Modified sigvec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sigvec {     var sv_handler: CFunctionPointer<((Int32) -> Void)>     var sv_mask: Int32     var sv_flags: Int32 } ``` |
| To | ``` struct sigvec {     var sv_handler: CFunctionPointer<((Int32) -> Void)>     var sv_mask: Int32     var sv_flags: Int32     init()     init(sv_handler sv_handler: CFunctionPointer<((Int32) -> Void)>, sv_mask sv_mask: Int32, sv_flags sv_flags: Int32) } ``` |

Modified so_np_extensions [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct so_np_extensions {     var npx_flags: UInt32     var npx_mask: UInt32 } ``` |
| To | ``` struct so_np_extensions {     var npx_flags: UInt32     var npx_mask: UInt32     init()     init(npx_flags npx_flags: UInt32, npx_mask npx_mask: UInt32) } ``` |

Modified sockaddr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sockaddr {     var sa_len: __uint8_t     var sa_family: sa_family_t     var sa_data: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct sockaddr {     var sa_len: __uint8_t     var sa_family: sa_family_t     var sa_data: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(sa_len sa_len: __uint8_t, sa_family sa_family: sa_family_t, sa_data sa_data: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified sockaddr_in [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sockaddr_in {     var sin_len: __uint8_t     var sin_family: sa_family_t     var sin_port: in_port_t     var sin_addr: in_addr     var sin_zero: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct sockaddr_in {     var sin_len: __uint8_t     var sin_family: sa_family_t     var sin_port: in_port_t     var sin_addr: in_addr     var sin_zero: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(sin_len sin_len: __uint8_t, sin_family sin_family: sa_family_t, sin_port sin_port: in_port_t, sin_addr sin_addr: in_addr, sin_zero sin_zero: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified sockaddr_in6 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sockaddr_in6 {     var sin6_len: __uint8_t     var sin6_family: sa_family_t     var sin6_port: in_port_t     var sin6_flowinfo: __uint32_t     var sin6_addr: in6_addr     var sin6_scope_id: __uint32_t } ``` |
| To | ``` struct sockaddr_in6 {     var sin6_len: __uint8_t     var sin6_family: sa_family_t     var sin6_port: in_port_t     var sin6_flowinfo: __uint32_t     var sin6_addr: in6_addr     var sin6_scope_id: __uint32_t     init()     init(sin6_len sin6_len: __uint8_t, sin6_family sin6_family: sa_family_t, sin6_port sin6_port: in_port_t, sin6_flowinfo sin6_flowinfo: __uint32_t, sin6_addr sin6_addr: in6_addr, sin6_scope_id sin6_scope_id: __uint32_t) } ``` |

Modified sockaddr_storage [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sockaddr_storage {     var ss_len: __uint8_t     var ss_family: sa_family_t     var __ss_pad1: (Int8, Int8, Int8, Int8, Int8, Int8)     var __ss_align: __int64_t     var __ss_pad2: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct sockaddr_storage {     var ss_len: __uint8_t     var ss_family: sa_family_t     var __ss_pad1: (Int8, Int8, Int8, Int8, Int8, Int8)     var __ss_align: __int64_t     var __ss_pad2: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(ss_len ss_len: __uint8_t, ss_family ss_family: sa_family_t, __ss_pad1 __ss_pad1: (Int8, Int8, Int8, Int8, Int8, Int8), __ss_align __ss_align: __int64_t, __ss_pad2 __ss_pad2: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified sockaddr_un [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sockaddr_un {     var sun_len: UInt8     var sun_family: sa_family_t     var sun_path: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct sockaddr_un {     var sun_len: UInt8     var sun_family: sa_family_t     var sun_path: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(sun_len sun_len: UInt8, sun_family sun_family: sa_family_t, sun_path sun_path: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified sockproto [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sockproto {     var sp_family: __uint16_t     var sp_protocol: __uint16_t } ``` |
| To | ``` struct sockproto {     var sp_family: __uint16_t     var sp_protocol: __uint16_t     init()     init(sp_family sp_family: __uint16_t, sp_protocol sp_protocol: __uint16_t) } ``` |

Modified stat [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct stat {     var st_dev: dev_t     var st_mode: mode_t     var st_nlink: nlink_t     var st_ino: __darwin_ino64_t     var st_uid: uid_t     var st_gid: gid_t     var st_rdev: dev_t     var st_atimespec: timespec     var st_mtimespec: timespec     var st_ctimespec: timespec     var st_birthtimespec: timespec     var st_size: off_t     var st_blocks: blkcnt_t     var st_blksize: blksize_t     var st_flags: __uint32_t     var st_gen: __uint32_t     var st_lspare: __int32_t     var st_qspare: (__int64_t, __int64_t) } ``` |
| To | ``` struct stat {     var st_dev: dev_t     var st_mode: mode_t     var st_nlink: nlink_t     var st_ino: __darwin_ino64_t     var st_uid: uid_t     var st_gid: gid_t     var st_rdev: dev_t     var st_atimespec: timespec     var st_mtimespec: timespec     var st_ctimespec: timespec     var st_birthtimespec: timespec     var st_size: off_t     var st_blocks: blkcnt_t     var st_blksize: blksize_t     var st_flags: __uint32_t     var st_gen: __uint32_t     var st_lspare: __int32_t     var st_qspare: (__int64_t, __int64_t)     init()     init(st_dev st_dev: dev_t, st_mode st_mode: mode_t, st_nlink st_nlink: nlink_t, st_ino st_ino: __darwin_ino64_t, st_uid st_uid: uid_t, st_gid st_gid: gid_t, st_rdev st_rdev: dev_t, st_atimespec st_atimespec: timespec, st_mtimespec st_mtimespec: timespec, st_ctimespec st_ctimespec: timespec, st_birthtimespec st_birthtimespec: timespec, st_size st_size: off_t, st_blocks st_blocks: blkcnt_t, st_blksize st_blksize: blksize_t, st_flags st_flags: __uint32_t, st_gen st_gen: __uint32_t, st_lspare st_lspare: __int32_t, st_qspare st_qspare: (__int64_t, __int64_t)) } ``` |

Modified statvfs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct statvfs {     var f_bsize: UInt     var f_frsize: UInt     var f_blocks: fsblkcnt_t     var f_bfree: fsblkcnt_t     var f_bavail: fsblkcnt_t     var f_files: fsfilcnt_t     var f_ffree: fsfilcnt_t     var f_favail: fsfilcnt_t     var f_fsid: UInt     var f_flag: UInt     var f_namemax: UInt } ``` |
| To | ``` struct statvfs {     var f_bsize: UInt     var f_frsize: UInt     var f_blocks: fsblkcnt_t     var f_bfree: fsblkcnt_t     var f_bavail: fsblkcnt_t     var f_files: fsfilcnt_t     var f_ffree: fsfilcnt_t     var f_favail: fsfilcnt_t     var f_fsid: UInt     var f_flag: UInt     var f_namemax: UInt     init()     init(f_bsize f_bsize: UInt, f_frsize f_frsize: UInt, f_blocks f_blocks: fsblkcnt_t, f_bfree f_bfree: fsblkcnt_t, f_bavail f_bavail: fsblkcnt_t, f_files f_files: fsfilcnt_t, f_ffree f_ffree: fsfilcnt_t, f_favail f_favail: fsfilcnt_t, f_fsid f_fsid: UInt, f_flag f_flag: UInt, f_namemax f_namemax: UInt) } ``` |

Modified task_absolutetime_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_absolutetime_info {     var total_user: UInt64     var total_system: UInt64     var threads_user: UInt64     var threads_system: UInt64 } ``` |
| To | ``` struct task_absolutetime_info {     var total_user: UInt64     var total_system: UInt64     var threads_user: UInt64     var threads_system: UInt64     init()     init(total_user total_user: UInt64, total_system total_system: UInt64, threads_user threads_user: UInt64, threads_system threads_system: UInt64) } ``` |

Modified task_affinity_tag_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_affinity_tag_info {     var set_count: integer_t     var min: integer_t     var max: integer_t     var task_count: integer_t } ``` |
| To | ``` struct task_affinity_tag_info {     var set_count: integer_t     var min: integer_t     var max: integer_t     var task_count: integer_t     init()     init(set_count set_count: integer_t, min min: integer_t, max max: integer_t, task_count task_count: integer_t) } ``` |

Modified task_basic_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_basic_info {     var suspend_count: integer_t     var virtual_size: vm_size_t     var resident_size: vm_size_t     var user_time: time_value_t     var system_time: time_value_t     var policy: policy_t } ``` |
| To | ``` struct task_basic_info {     var suspend_count: integer_t     var virtual_size: vm_size_t     var resident_size: vm_size_t     var user_time: time_value_t     var system_time: time_value_t     var policy: policy_t     init()     init(suspend_count suspend_count: integer_t, virtual_size virtual_size: vm_size_t, resident_size resident_size: vm_size_t, user_time user_time: time_value_t, system_time system_time: time_value_t, policy policy: policy_t) } ``` |

Modified task_basic_info_32 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_basic_info_32 {     var suspend_count: integer_t     var virtual_size: natural_t     var resident_size: natural_t     var user_time: time_value_t     var system_time: time_value_t     var policy: policy_t } ``` |
| To | ``` struct task_basic_info_32 {     var suspend_count: integer_t     var virtual_size: natural_t     var resident_size: natural_t     var user_time: time_value_t     var system_time: time_value_t     var policy: policy_t     init()     init(suspend_count suspend_count: integer_t, virtual_size virtual_size: natural_t, resident_size resident_size: natural_t, user_time user_time: time_value_t, system_time system_time: time_value_t, policy policy: policy_t) } ``` |

Modified task_basic_info_64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_basic_info_64 {     var suspend_count: integer_t     var virtual_size: mach_vm_size_t     var resident_size: mach_vm_size_t     var user_time: time_value_t     var system_time: time_value_t     var policy: policy_t } ``` |
| To | ``` struct task_basic_info_64 {     var suspend_count: integer_t     var virtual_size: mach_vm_size_t     var resident_size: mach_vm_size_t     var user_time: time_value_t     var system_time: time_value_t     var policy: policy_t     init()     init(suspend_count suspend_count: integer_t, virtual_size virtual_size: mach_vm_size_t, resident_size resident_size: mach_vm_size_t, user_time user_time: time_value_t, system_time system_time: time_value_t, policy policy: policy_t) } ``` |

Modified task_basic_info_64_2 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_basic_info_64_2 {     var suspend_count: integer_t     var virtual_size: mach_vm_size_t     var resident_size: mach_vm_size_t     var user_time: time_value_t     var system_time: time_value_t     var policy: policy_t } ``` |
| To | ``` struct task_basic_info_64_2 {     var suspend_count: integer_t     var virtual_size: mach_vm_size_t     var resident_size: mach_vm_size_t     var user_time: time_value_t     var system_time: time_value_t     var policy: policy_t     init()     init(suspend_count suspend_count: integer_t, virtual_size virtual_size: mach_vm_size_t, resident_size resident_size: mach_vm_size_t, user_time user_time: time_value_t, system_time system_time: time_value_t, policy policy: policy_t) } ``` |

Modified task_category_policy [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_category_policy {     var role: task_role_t } ``` |
| To | ``` struct task_category_policy {     var role: task_role_t     init()     init(role role: task_role_t) } ``` |

Modified task_dyld_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_dyld_info {     var all_image_info_addr: mach_vm_address_t     var all_image_info_size: mach_vm_size_t     var all_image_info_format: integer_t } ``` |
| To | ``` struct task_dyld_info {     var all_image_info_addr: mach_vm_address_t     var all_image_info_size: mach_vm_size_t     var all_image_info_format: integer_t     init()     init(all_image_info_addr all_image_info_addr: mach_vm_address_t, all_image_info_size all_image_info_size: mach_vm_size_t, all_image_info_format all_image_info_format: integer_t) } ``` |

Modified task_events_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_events_info {     var faults: integer_t     var pageins: integer_t     var cow_faults: integer_t     var messages_sent: integer_t     var messages_received: integer_t     var syscalls_mach: integer_t     var syscalls_unix: integer_t     var csw: integer_t } ``` |
| To | ``` struct task_events_info {     var faults: integer_t     var pageins: integer_t     var cow_faults: integer_t     var messages_sent: integer_t     var messages_received: integer_t     var syscalls_mach: integer_t     var syscalls_unix: integer_t     var csw: integer_t     init()     init(faults faults: integer_t, pageins pageins: integer_t, cow_faults cow_faults: integer_t, messages_sent messages_sent: integer_t, messages_received messages_received: integer_t, syscalls_mach syscalls_mach: integer_t, syscalls_unix syscalls_unix: integer_t, csw csw: integer_t) } ``` |

Modified task_extmod_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_extmod_info {     var task_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var extmod_statistics: vm_extmod_statistics_data_t } ``` |
| To | ``` struct task_extmod_info {     var task_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var extmod_statistics: vm_extmod_statistics_data_t     init()     init(task_uuid task_uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), extmod_statistics extmod_statistics: vm_extmod_statistics_data_t) } ``` |

Modified task_kernelmemory_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_kernelmemory_info {     var total_palloc: UInt64     var total_pfree: UInt64     var total_salloc: UInt64     var total_sfree: UInt64 } ``` |
| To | ``` struct task_kernelmemory_info {     var total_palloc: UInt64     var total_pfree: UInt64     var total_salloc: UInt64     var total_sfree: UInt64     init()     init(total_palloc total_palloc: UInt64, total_pfree total_pfree: UInt64, total_salloc total_salloc: UInt64, total_sfree total_sfree: UInt64) } ``` |

Modified task_power_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_power_info {     var total_user: UInt64     var total_system: UInt64     var task_interrupt_wakeups: UInt64     var task_platform_idle_wakeups: UInt64     var task_timer_wakeups_bin_1: UInt64     var task_timer_wakeups_bin_2: UInt64 } ``` |
| To | ``` struct task_power_info {     var total_user: UInt64     var total_system: UInt64     var task_interrupt_wakeups: UInt64     var task_platform_idle_wakeups: UInt64     var task_timer_wakeups_bin_1: UInt64     var task_timer_wakeups_bin_2: UInt64     init()     init(total_user total_user: UInt64, total_system total_system: UInt64, task_interrupt_wakeups task_interrupt_wakeups: UInt64, task_platform_idle_wakeups task_platform_idle_wakeups: UInt64, task_timer_wakeups_bin_1 task_timer_wakeups_bin_1: UInt64, task_timer_wakeups_bin_2 task_timer_wakeups_bin_2: UInt64) } ``` |

Modified task_power_info_v2 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_power_info_v2 {     var cpu_energy: task_power_info_data_t     var gpu_energy: gpu_energy_data } ``` |
| To | ``` struct task_power_info_v2 {     var cpu_energy: task_power_info_data_t     var gpu_energy: gpu_energy_data     init()     init(cpu_energy cpu_energy: task_power_info_data_t, gpu_energy gpu_energy: gpu_energy_data) } ``` |

Modified task_qos_policy [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_qos_policy {     var task_latency_qos_tier: task_latency_qos_t     var task_throughput_qos_tier: task_throughput_qos_t } ``` |
| To | ``` struct task_qos_policy {     var task_latency_qos_tier: task_latency_qos_t     var task_throughput_qos_tier: task_throughput_qos_t     init()     init(task_latency_qos_tier task_latency_qos_tier: task_latency_qos_t, task_throughput_qos_tier task_throughput_qos_tier: task_throughput_qos_t) } ``` |

Modified task_thread_times_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_thread_times_info {     var user_time: time_value_t     var system_time: time_value_t } ``` |
| To | ``` struct task_thread_times_info {     var user_time: time_value_t     var system_time: time_value_t     init()     init(user_time user_time: time_value_t, system_time system_time: time_value_t) } ``` |

Modified task_trace_memory_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_trace_memory_info {     var user_memory_address: UInt64     var buffer_size: UInt64     var mailbox_array_size: UInt64 } ``` |
| To | ``` struct task_trace_memory_info {     var user_memory_address: UInt64     var buffer_size: UInt64     var mailbox_array_size: UInt64     init()     init(user_memory_address user_memory_address: UInt64, buffer_size buffer_size: UInt64, mailbox_array_size mailbox_array_size: UInt64) } ``` |

Modified task_vm_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_vm_info {     var virtual_size: mach_vm_size_t     var region_count: integer_t     var page_size: integer_t     var resident_size: mach_vm_size_t     var resident_size_peak: mach_vm_size_t     var device: mach_vm_size_t     var device_peak: mach_vm_size_t     var `internal`: mach_vm_size_t     var internal_peak: mach_vm_size_t     var external: mach_vm_size_t     var external_peak: mach_vm_size_t     var reusable: mach_vm_size_t     var reusable_peak: mach_vm_size_t     var purgeable_volatile_pmap: mach_vm_size_t     var purgeable_volatile_resident: mach_vm_size_t     var purgeable_volatile_virtual: mach_vm_size_t     var compressed: mach_vm_size_t     var compressed_peak: mach_vm_size_t     var compressed_lifetime: mach_vm_size_t } ``` |
| To | ``` struct task_vm_info {     var virtual_size: mach_vm_size_t     var region_count: integer_t     var page_size: integer_t     var resident_size: mach_vm_size_t     var resident_size_peak: mach_vm_size_t     var device: mach_vm_size_t     var device_peak: mach_vm_size_t     var `internal`: mach_vm_size_t     var internal_peak: mach_vm_size_t     var external: mach_vm_size_t     var external_peak: mach_vm_size_t     var reusable: mach_vm_size_t     var reusable_peak: mach_vm_size_t     var purgeable_volatile_pmap: mach_vm_size_t     var purgeable_volatile_resident: mach_vm_size_t     var purgeable_volatile_virtual: mach_vm_size_t     var compressed: mach_vm_size_t     var compressed_peak: mach_vm_size_t     var compressed_lifetime: mach_vm_size_t     init()     init(virtual_size virtual_size: mach_vm_size_t, region_count region_count: integer_t, page_size page_size: integer_t, resident_size resident_size: mach_vm_size_t, resident_size_peak resident_size_peak: mach_vm_size_t, device device: mach_vm_size_t, device_peak device_peak: mach_vm_size_t, `internal` `internal`: mach_vm_size_t, internal_peak internal_peak: mach_vm_size_t, external external: mach_vm_size_t, external_peak external_peak: mach_vm_size_t, reusable reusable: mach_vm_size_t, reusable_peak reusable_peak: mach_vm_size_t, purgeable_volatile_pmap purgeable_volatile_pmap: mach_vm_size_t, purgeable_volatile_resident purgeable_volatile_resident: mach_vm_size_t, purgeable_volatile_virtual purgeable_volatile_virtual: mach_vm_size_t, compressed compressed: mach_vm_size_t, compressed_peak compressed_peak: mach_vm_size_t, compressed_lifetime compressed_lifetime: mach_vm_size_t) } ``` |

Modified task_wait_state_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_wait_state_info {     var total_wait_state_time: UInt64     var total_wait_sfi_state_time: UInt64     var _reserved: (UInt32, UInt32, UInt32, UInt32) } ``` |
| To | ``` struct task_wait_state_info {     var total_wait_state_time: UInt64     var total_wait_sfi_state_time: UInt64     var _reserved: (UInt32, UInt32, UInt32, UInt32)     init()     init(total_wait_state_time total_wait_state_time: UInt64, total_wait_sfi_state_time total_wait_sfi_state_time: UInt64, _reserved _reserved: (UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified task_zone_info_data [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct task_zone_info_data {     var tzi_count: UInt64     var tzi_cur_size: UInt64     var tzi_max_size: UInt64     var tzi_elem_size: UInt64     var tzi_alloc_size: UInt64     var tzi_sum_size: UInt64     var tzi_exhaustible: UInt64     var tzi_collectable: UInt64     var tzi_caller_acct: UInt64     var tzi_task_alloc: UInt64     var tzi_task_free: UInt64 } ``` |
| To | ``` struct task_zone_info_data {     var tzi_count: UInt64     var tzi_cur_size: UInt64     var tzi_max_size: UInt64     var tzi_elem_size: UInt64     var tzi_alloc_size: UInt64     var tzi_sum_size: UInt64     var tzi_exhaustible: UInt64     var tzi_collectable: UInt64     var tzi_caller_acct: UInt64     var tzi_task_alloc: UInt64     var tzi_task_free: UInt64     init()     init(tzi_count tzi_count: UInt64, tzi_cur_size tzi_cur_size: UInt64, tzi_max_size tzi_max_size: UInt64, tzi_elem_size tzi_elem_size: UInt64, tzi_alloc_size tzi_alloc_size: UInt64, tzi_sum_size tzi_sum_size: UInt64, tzi_exhaustible tzi_exhaustible: UInt64, tzi_collectable tzi_collectable: UInt64, tzi_caller_acct tzi_caller_acct: UInt64, tzi_task_alloc tzi_task_alloc: UInt64, tzi_task_free tzi_task_free: UInt64) } ``` |

Modified termios [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct termios {     var c_iflag: tcflag_t     var c_oflag: tcflag_t     var c_cflag: tcflag_t     var c_lflag: tcflag_t     var c_cc: (cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t)     var c_ispeed: speed_t     var c_ospeed: speed_t } ``` |
| To | ``` struct termios {     var c_iflag: tcflag_t     var c_oflag: tcflag_t     var c_cflag: tcflag_t     var c_lflag: tcflag_t     var c_cc: (cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t)     var c_ispeed: speed_t     var c_ospeed: speed_t     init()     init(c_iflag c_iflag: tcflag_t, c_oflag c_oflag: tcflag_t, c_cflag c_cflag: tcflag_t, c_lflag c_lflag: tcflag_t, c_cc c_cc: (cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t, cc_t), c_ispeed c_ispeed: speed_t, c_ospeed c_ospeed: speed_t) } ``` |

Modified thread_affinity_policy [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct thread_affinity_policy {     var affinity_tag: integer_t } ``` |
| To | ``` struct thread_affinity_policy {     var affinity_tag: integer_t     init()     init(affinity_tag affinity_tag: integer_t) } ``` |

Modified thread_background_policy [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct thread_background_policy {     var priority: integer_t } ``` |
| To | ``` struct thread_background_policy {     var priority: integer_t     init()     init(priority priority: integer_t) } ``` |

Modified thread_basic_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct thread_basic_info {     var user_time: time_value_t     var system_time: time_value_t     var cpu_usage: integer_t     var policy: policy_t     var run_state: integer_t     var flags: integer_t     var suspend_count: integer_t     var sleep_time: integer_t } ``` |
| To | ``` struct thread_basic_info {     var user_time: time_value_t     var system_time: time_value_t     var cpu_usage: integer_t     var policy: policy_t     var run_state: integer_t     var flags: integer_t     var suspend_count: integer_t     var sleep_time: integer_t     init()     init(user_time user_time: time_value_t, system_time system_time: time_value_t, cpu_usage cpu_usage: integer_t, policy policy: policy_t, run_state run_state: integer_t, flags flags: integer_t, suspend_count suspend_count: integer_t, sleep_time sleep_time: integer_t) } ``` |

Modified thread_extended_policy [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct thread_extended_policy {     var timeshare: boolean_t } ``` |
| To | ``` struct thread_extended_policy {     var timeshare: boolean_t     init()     init(timeshare timeshare: boolean_t) } ``` |

Modified thread_identifier_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct thread_identifier_info {     var thread_id: UInt64     var thread_handle: UInt64     var dispatch_qaddr: UInt64 } ``` |
| To | ``` struct thread_identifier_info {     var thread_id: UInt64     var thread_handle: UInt64     var dispatch_qaddr: UInt64     init()     init(thread_id thread_id: UInt64, thread_handle thread_handle: UInt64, dispatch_qaddr dispatch_qaddr: UInt64) } ``` |

Modified thread_latency_qos_policy [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct thread_latency_qos_policy {     var thread_latency_qos_tier: thread_latency_qos_t } ``` |
| To | ``` struct thread_latency_qos_policy {     var thread_latency_qos_tier: thread_latency_qos_t     init()     init(thread_latency_qos_tier thread_latency_qos_tier: thread_latency_qos_t) } ``` |

Modified thread_precedence_policy [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct thread_precedence_policy {     var importance: integer_t } ``` |
| To | ``` struct thread_precedence_policy {     var importance: integer_t     init()     init(importance importance: integer_t) } ``` |

Modified thread_standard_policy [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct thread_standard_policy {     var no_data: natural_t } ``` |
| To | ``` struct thread_standard_policy {     var no_data: natural_t     init()     init(no_data no_data: natural_t) } ``` |

Modified thread_throughput_qos_policy [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct thread_throughput_qos_policy {     var thread_throughput_qos_tier: thread_throughput_qos_t } ``` |
| To | ``` struct thread_throughput_qos_policy {     var thread_throughput_qos_tier: thread_throughput_qos_t     init()     init(thread_throughput_qos_tier thread_throughput_qos_tier: thread_throughput_qos_t) } ``` |

Modified thread_time_constraint_policy [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct thread_time_constraint_policy {     var period: UInt32     var computation: UInt32     var constraint: UInt32     var preemptible: boolean_t } ``` |
| To | ``` struct thread_time_constraint_policy {     var period: UInt32     var computation: UInt32     var constraint: UInt32     var preemptible: boolean_t     init()     init(period period: UInt32, computation computation: UInt32, constraint constraint: UInt32, preemptible preemptible: boolean_t) } ``` |

Modified time_value [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct time_value {     var seconds: integer_t     var microseconds: integer_t } ``` |
| To | ``` struct time_value {     var seconds: integer_t     var microseconds: integer_t     init()     init(seconds seconds: integer_t, microseconds microseconds: integer_t) } ``` |

Modified timeb [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct timeb {     var time: time_t     var millitm: UInt16     var timezone: Int16     var dstflag: Int16 } ``` |
| To | ``` struct timeb {     var time: time_t     var millitm: UInt16     var timezone: Int16     var dstflag: Int16     init()     init(time time: time_t, millitm millitm: UInt16, timezone timezone: Int16, dstflag dstflag: Int16) } ``` |

Modified timespec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct timespec {     var tv_sec: __darwin_time_t     var tv_nsec: Int } ``` |
| To | ``` struct timespec {     var tv_sec: __darwin_time_t     var tv_nsec: Int     init()     init(tv_sec tv_sec: __darwin_time_t, tv_nsec tv_nsec: Int) } ``` |

Modified timeval [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct timeval {     var tv_sec: __darwin_time_t     var tv_usec: __darwin_suseconds_t } ``` |
| To | ``` struct timeval {     var tv_sec: __darwin_time_t     var tv_usec: __darwin_suseconds_t     init()     init(tv_sec tv_sec: __darwin_time_t, tv_usec tv_usec: __darwin_suseconds_t) } ``` |

Modified timeval32 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct timeval32 {     var tv_sec: __int32_t     var tv_usec: __int32_t } ``` |
| To | ``` struct timeval32 {     var tv_sec: __int32_t     var tv_usec: __int32_t     init()     init(tv_sec tv_sec: __int32_t, tv_usec tv_usec: __int32_t) } ``` |

Modified timezone [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct timezone {     var tz_minuteswest: Int32     var tz_dsttime: Int32 } ``` |
| To | ``` struct timezone {     var tz_minuteswest: Int32     var tz_dsttime: Int32     init()     init(tz_minuteswest tz_minuteswest: Int32, tz_dsttime tz_dsttime: Int32) } ``` |

Modified tm [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tm {     var tm_sec: Int32     var tm_min: Int32     var tm_hour: Int32     var tm_mday: Int32     var tm_mon: Int32     var tm_year: Int32     var tm_wday: Int32     var tm_yday: Int32     var tm_isdst: Int32     var tm_gmtoff: Int     var tm_zone: UnsafeMutablePointer<Int8> } ``` |
| To | ``` struct tm {     var tm_sec: Int32     var tm_min: Int32     var tm_hour: Int32     var tm_mday: Int32     var tm_mon: Int32     var tm_year: Int32     var tm_wday: Int32     var tm_yday: Int32     var tm_isdst: Int32     var tm_gmtoff: Int     var tm_zone: UnsafeMutablePointer<Int8>     init()     init(tm_sec tm_sec: Int32, tm_min tm_min: Int32, tm_hour tm_hour: Int32, tm_mday tm_mday: Int32, tm_mon tm_mon: Int32, tm_year tm_year: Int32, tm_wday tm_wday: Int32, tm_yday tm_yday: Int32, tm_isdst tm_isdst: Int32, tm_gmtoff tm_gmtoff: Int, tm_zone tm_zone: UnsafeMutablePointer<Int8>) } ``` |

Modified tms [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tms {     var tms_utime: clock_t     var tms_stime: clock_t     var tms_cutime: clock_t     var tms_cstime: clock_t } ``` |
| To | ``` struct tms {     var tms_utime: clock_t     var tms_stime: clock_t     var tms_cutime: clock_t     var tms_cstime: clock_t     init()     init(tms_utime tms_utime: clock_t, tms_stime tms_stime: clock_t, tms_cutime tms_cutime: clock_t, tms_cstime tms_cstime: clock_t) } ``` |

Modified ttysize [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ttysize {     var ts_lines: UInt16     var ts_cols: UInt16     var ts_xxx: UInt16     var ts_yyy: UInt16 } ``` |
| To | ``` struct ttysize {     var ts_lines: UInt16     var ts_cols: UInt16     var ts_xxx: UInt16     var ts_yyy: UInt16     init()     init(ts_lines ts_lines: UInt16, ts_cols ts_cols: UInt16, ts_xxx ts_xxx: UInt16, ts_yyy ts_yyy: UInt16) } ``` |

Modified ucred [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ucred {     var cr_ref: u_long     var cr_posix: posix_cred     var cr_label: COpaquePointer     var cr_audit: au_session } ``` |
| To | ``` struct ucred {     var cr_ref: u_long     var cr_posix: posix_cred     var cr_label: COpaquePointer     var cr_audit: au_session     init() } ``` |

Modified utimbuf [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct utimbuf {     var actime: time_t     var modtime: time_t } ``` |
| To | ``` struct utimbuf {     var actime: time_t     var modtime: time_t     init()     init(actime actime: time_t, modtime modtime: time_t) } ``` |

Modified utmpx [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct utmpx {     var ut_user: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ut_id: (Int8, Int8, Int8, Int8)     var ut_line: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ut_pid: pid_t     var ut_type: Int16     var ut_tv: timeval     var ut_host: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var ut_pad: (__uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t, __uint32_t) } ``` |
| To | ```  ``` |

Modified vfsconf [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vfsconf {     var vfc_reserved1: UInt32     var vfc_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var vfc_typenum: Int32     var vfc_refcount: Int32     var vfc_flags: Int32     var vfc_reserved2: UInt32     var vfc_reserved3: UInt32 } ``` |
| To | ``` struct vfsconf {     var vfc_reserved1: UInt32     var vfc_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var vfc_typenum: Int32     var vfc_refcount: Int32     var vfc_flags: Int32     var vfc_reserved2: UInt32     var vfc_reserved3: UInt32     init()     init(vfc_reserved1 vfc_reserved1: UInt32, vfc_name vfc_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), vfc_typenum vfc_typenum: Int32, vfc_refcount vfc_refcount: Int32, vfc_flags vfc_flags: Int32, vfc_reserved2 vfc_reserved2: UInt32, vfc_reserved3 vfc_reserved3: UInt32) } ``` |

Modified vfsidctl [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vfsidctl {     var vc_vers: Int32     var vc_fsid: fsid_t     var vc_ptr: UnsafeMutablePointer<Void>     var vc_len: UInt     var vc_spare: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32) } ``` |
| To | ``` struct vfsidctl {     var vc_vers: Int32     var vc_fsid: fsid_t     var vc_ptr: UnsafeMutablePointer<Void>     var vc_len: Int     var vc_spare: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)     init()     init(vc_vers vc_vers: Int32, vc_fsid vc_fsid: fsid_t, vc_ptr vc_ptr: UnsafeMutablePointer<Void>, vc_len vc_len: Int, vc_spare vc_spare: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified vfsidctl.vc_len

|  | Declaration |
| --- | --- |
| From | ``` var vc_len: UInt ``` |
| To | ``` var vc_len: Int ``` |

Modified vfsquery [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vfsquery {     var vq_flags: UInt32     var vq_spare: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32) } ``` |
| To | ``` struct vfsquery {     var vq_flags: UInt32     var vq_spare: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)     init()     init(vq_flags vq_flags: UInt32, vq_spare vq_spare: (UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified vfsstatfs.f_iosize

|  | Declaration |
| --- | --- |
| From | ``` var f_iosize: UInt ``` |
| To | ``` var f_iosize: Int ``` |

Modified vm_extmod_statistics [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_extmod_statistics {     var task_for_pid_count: Int64     var task_for_pid_caller_count: Int64     var thread_creation_count: Int64     var thread_creation_caller_count: Int64     var thread_set_state_count: Int64     var thread_set_state_caller_count: Int64 } ``` |
| To | ``` struct vm_extmod_statistics {     var task_for_pid_count: Int64     var task_for_pid_caller_count: Int64     var thread_creation_count: Int64     var thread_creation_caller_count: Int64     var thread_set_state_count: Int64     var thread_set_state_caller_count: Int64     init()     init(task_for_pid_count task_for_pid_count: Int64, task_for_pid_caller_count task_for_pid_caller_count: Int64, thread_creation_count thread_creation_count: Int64, thread_creation_caller_count thread_creation_caller_count: Int64, thread_set_state_count thread_set_state_count: Int64, thread_set_state_caller_count thread_set_state_caller_count: Int64) } ``` |

Modified vm_info_object [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_info_object {     var vio_object: natural_t     var vio_size: natural_t     var vio_ref_count: UInt32     var vio_resident_page_count: UInt32     var vio_absent_count: UInt32     var vio_copy: natural_t     var vio_shadow: natural_t     var vio_shadow_offset: natural_t     var vio_paging_offset: natural_t     var vio_copy_strategy: memory_object_copy_strategy_t     var vio_last_alloc: vm_offset_t     var vio_paging_in_progress: UInt32     var vio_pager_created: boolean_t     var vio_pager_initialized: boolean_t     var vio_pager_ready: boolean_t     var vio_can_persist: boolean_t     var vio_internal: boolean_t     var vio_temporary: boolean_t     var vio_alive: boolean_t     var vio_purgable: boolean_t     var vio_purgable_volatile: boolean_t } ``` |
| To | ``` struct vm_info_object {     var vio_object: natural_t     var vio_size: natural_t     var vio_ref_count: UInt32     var vio_resident_page_count: UInt32     var vio_absent_count: UInt32     var vio_copy: natural_t     var vio_shadow: natural_t     var vio_shadow_offset: natural_t     var vio_paging_offset: natural_t     var vio_copy_strategy: memory_object_copy_strategy_t     var vio_last_alloc: vm_offset_t     var vio_paging_in_progress: UInt32     var vio_pager_created: boolean_t     var vio_pager_initialized: boolean_t     var vio_pager_ready: boolean_t     var vio_can_persist: boolean_t     var vio_internal: boolean_t     var vio_temporary: boolean_t     var vio_alive: boolean_t     var vio_purgable: boolean_t     var vio_purgable_volatile: boolean_t     init()     init(vio_object vio_object: natural_t, vio_size vio_size: natural_t, vio_ref_count vio_ref_count: UInt32, vio_resident_page_count vio_resident_page_count: UInt32, vio_absent_count vio_absent_count: UInt32, vio_copy vio_copy: natural_t, vio_shadow vio_shadow: natural_t, vio_shadow_offset vio_shadow_offset: natural_t, vio_paging_offset vio_paging_offset: natural_t, vio_copy_strategy vio_copy_strategy: memory_object_copy_strategy_t, vio_last_alloc vio_last_alloc: vm_offset_t, vio_paging_in_progress vio_paging_in_progress: UInt32, vio_pager_created vio_pager_created: boolean_t, vio_pager_initialized vio_pager_initialized: boolean_t, vio_pager_ready vio_pager_ready: boolean_t, vio_can_persist vio_can_persist: boolean_t, vio_internal vio_internal: boolean_t, vio_temporary vio_temporary: boolean_t, vio_alive vio_alive: boolean_t, vio_purgable vio_purgable: boolean_t, vio_purgable_volatile vio_purgable_volatile: boolean_t) } ``` |

Modified vm_info_region [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_info_region {     var vir_start: natural_t     var vir_end: natural_t     var vir_object: natural_t     var vir_offset: natural_t     var vir_needs_copy: boolean_t     var vir_protection: vm_prot_t     var vir_max_protection: vm_prot_t     var vir_inheritance: vm_inherit_t     var vir_wired_count: natural_t     var vir_user_wired_count: natural_t } ``` |
| To | ``` struct vm_info_region {     var vir_start: natural_t     var vir_end: natural_t     var vir_object: natural_t     var vir_offset: natural_t     var vir_needs_copy: boolean_t     var vir_protection: vm_prot_t     var vir_max_protection: vm_prot_t     var vir_inheritance: vm_inherit_t     var vir_wired_count: natural_t     var vir_user_wired_count: natural_t     init()     init(vir_start vir_start: natural_t, vir_end vir_end: natural_t, vir_object vir_object: natural_t, vir_offset vir_offset: natural_t, vir_needs_copy vir_needs_copy: boolean_t, vir_protection vir_protection: vm_prot_t, vir_max_protection vir_max_protection: vm_prot_t, vir_inheritance vir_inheritance: vm_inherit_t, vir_wired_count vir_wired_count: natural_t, vir_user_wired_count vir_user_wired_count: natural_t) } ``` |

Modified vm_info_region_64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_info_region_64 {     var vir_start: natural_t     var vir_end: natural_t     var vir_object: natural_t     var vir_offset: memory_object_offset_t     var vir_needs_copy: boolean_t     var vir_protection: vm_prot_t     var vir_max_protection: vm_prot_t     var vir_inheritance: vm_inherit_t     var vir_wired_count: natural_t     var vir_user_wired_count: natural_t } ``` |
| To | ``` struct vm_info_region_64 {     var vir_start: natural_t     var vir_end: natural_t     var vir_object: natural_t     var vir_offset: memory_object_offset_t     var vir_needs_copy: boolean_t     var vir_protection: vm_prot_t     var vir_max_protection: vm_prot_t     var vir_inheritance: vm_inherit_t     var vir_wired_count: natural_t     var vir_user_wired_count: natural_t     init()     init(vir_start vir_start: natural_t, vir_end vir_end: natural_t, vir_object vir_object: natural_t, vir_offset vir_offset: memory_object_offset_t, vir_needs_copy vir_needs_copy: boolean_t, vir_protection vir_protection: vm_prot_t, vir_max_protection vir_max_protection: vm_prot_t, vir_inheritance vir_inheritance: vm_inherit_t, vir_wired_count vir_wired_count: natural_t, vir_user_wired_count vir_user_wired_count: natural_t) } ``` |

Modified vm_page_info_basic [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_page_info_basic {     var disposition: Int32     var ref_count: Int32     var object_id: vm_object_id_t     var offset: memory_object_offset_t     var depth: Int32     var __pad: Int32 } ``` |
| To | ``` struct vm_page_info_basic {     var disposition: Int32     var ref_count: Int32     var object_id: vm_object_id_t     var offset: memory_object_offset_t     var depth: Int32     var __pad: Int32     init()     init(disposition disposition: Int32, ref_count ref_count: Int32, object_id object_id: vm_object_id_t, offset offset: memory_object_offset_t, depth depth: Int32, __pad __pad: Int32) } ``` |

Modified vm_purgeable_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_purgeable_info {     var fifo_data: (vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t)     var obsolete_data: vm_purgeable_stat_t     var lifo_data: (vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t) } ``` |
| To | ``` struct vm_purgeable_info {     var fifo_data: (vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t)     var obsolete_data: vm_purgeable_stat_t     var lifo_data: (vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t)     init()     init(fifo_data fifo_data: (vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t), obsolete_data obsolete_data: vm_purgeable_stat_t, lifo_data lifo_data: (vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t, vm_purgeable_stat_t)) } ``` |

Modified vm_purgeable_stat [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_purgeable_stat {     var count: UInt64     var size: UInt64 } ``` |
| To | ``` struct vm_purgeable_stat {     var count: UInt64     var size: UInt64     init()     init(count count: UInt64, size size: UInt64) } ``` |

Modified vm_range_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_range_t {     var address: vm_address_t     var size: vm_size_t } ``` |
| To | ``` struct vm_range_t {     var address: vm_address_t     var size: vm_size_t     init()     init(address address: vm_address_t, size size: vm_size_t) } ``` |

Modified vm_read_entry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_read_entry {     var address: vm_address_t     var size: vm_size_t } ``` |
| To | ``` struct vm_read_entry {     var address: vm_address_t     var size: vm_size_t     init()     init(address address: vm_address_t, size size: vm_size_t) } ``` |

Modified vm_region_basic_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_region_basic_info {     var protection: vm_prot_t     var max_protection: vm_prot_t     var inheritance: vm_inherit_t     var shared: boolean_t     var reserved: boolean_t     var offset: UInt32     var behavior: vm_behavior_t     var user_wired_count: UInt16 } ``` |
| To | ``` struct vm_region_basic_info {     var protection: vm_prot_t     var max_protection: vm_prot_t     var inheritance: vm_inherit_t     var shared: boolean_t     var reserved: boolean_t     var offset: UInt32     var behavior: vm_behavior_t     var user_wired_count: UInt16     init()     init(protection protection: vm_prot_t, max_protection max_protection: vm_prot_t, inheritance inheritance: vm_inherit_t, shared shared: boolean_t, reserved reserved: boolean_t, offset offset: UInt32, behavior behavior: vm_behavior_t, user_wired_count user_wired_count: UInt16) } ``` |

Modified vm_region_basic_info_64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_region_basic_info_64 {     var protection: vm_prot_t     var max_protection: vm_prot_t     var inheritance: vm_inherit_t     var shared: boolean_t     var reserved: boolean_t     var offset: memory_object_offset_t     var behavior: vm_behavior_t     var user_wired_count: UInt16 } ``` |
| To | ``` struct vm_region_basic_info_64 {     var protection: vm_prot_t     var max_protection: vm_prot_t     var inheritance: vm_inherit_t     var shared: boolean_t     var reserved: boolean_t     var offset: memory_object_offset_t     var behavior: vm_behavior_t     var user_wired_count: UInt16     init()     init(protection protection: vm_prot_t, max_protection max_protection: vm_prot_t, inheritance inheritance: vm_inherit_t, shared shared: boolean_t, reserved reserved: boolean_t, offset offset: memory_object_offset_t, behavior behavior: vm_behavior_t, user_wired_count user_wired_count: UInt16) } ``` |

Modified vm_region_extended_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_region_extended_info {     var protection: vm_prot_t     var user_tag: UInt32     var pages_resident: UInt32     var pages_shared_now_private: UInt32     var pages_swapped_out: UInt32     var pages_dirtied: UInt32     var ref_count: UInt32     var shadow_depth: UInt16     var external_pager: UInt8     var share_mode: UInt8     var pages_reusable: UInt32 } ``` |
| To | ``` struct vm_region_extended_info {     var protection: vm_prot_t     var user_tag: UInt32     var pages_resident: UInt32     var pages_shared_now_private: UInt32     var pages_swapped_out: UInt32     var pages_dirtied: UInt32     var ref_count: UInt32     var shadow_depth: UInt16     var external_pager: UInt8     var share_mode: UInt8     var pages_reusable: UInt32     init()     init(protection protection: vm_prot_t, user_tag user_tag: UInt32, pages_resident pages_resident: UInt32, pages_shared_now_private pages_shared_now_private: UInt32, pages_swapped_out pages_swapped_out: UInt32, pages_dirtied pages_dirtied: UInt32, ref_count ref_count: UInt32, shadow_depth shadow_depth: UInt16, external_pager external_pager: UInt8, share_mode share_mode: UInt8, pages_reusable pages_reusable: UInt32) } ``` |

Modified vm_region_submap_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_region_submap_info {     var protection: vm_prot_t     var max_protection: vm_prot_t     var inheritance: vm_inherit_t     var offset: UInt32     var user_tag: UInt32     var pages_resident: UInt32     var pages_shared_now_private: UInt32     var pages_swapped_out: UInt32     var pages_dirtied: UInt32     var ref_count: UInt32     var shadow_depth: UInt16     var external_pager: UInt8     var share_mode: UInt8     var is_submap: boolean_t     var behavior: vm_behavior_t     var object_id: vm32_object_id_t     var user_wired_count: UInt16 } ``` |
| To | ``` struct vm_region_submap_info {     var protection: vm_prot_t     var max_protection: vm_prot_t     var inheritance: vm_inherit_t     var offset: UInt32     var user_tag: UInt32     var pages_resident: UInt32     var pages_shared_now_private: UInt32     var pages_swapped_out: UInt32     var pages_dirtied: UInt32     var ref_count: UInt32     var shadow_depth: UInt16     var external_pager: UInt8     var share_mode: UInt8     var is_submap: boolean_t     var behavior: vm_behavior_t     var object_id: vm32_object_id_t     var user_wired_count: UInt16     init()     init(protection protection: vm_prot_t, max_protection max_protection: vm_prot_t, inheritance inheritance: vm_inherit_t, offset offset: UInt32, user_tag user_tag: UInt32, pages_resident pages_resident: UInt32, pages_shared_now_private pages_shared_now_private: UInt32, pages_swapped_out pages_swapped_out: UInt32, pages_dirtied pages_dirtied: UInt32, ref_count ref_count: UInt32, shadow_depth shadow_depth: UInt16, external_pager external_pager: UInt8, share_mode share_mode: UInt8, is_submap is_submap: boolean_t, behavior behavior: vm_behavior_t, object_id object_id: vm32_object_id_t, user_wired_count user_wired_count: UInt16) } ``` |

Modified vm_region_submap_info_64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_region_submap_info_64 {     var protection: vm_prot_t     var max_protection: vm_prot_t     var inheritance: vm_inherit_t     var offset: memory_object_offset_t     var user_tag: UInt32     var pages_resident: UInt32     var pages_shared_now_private: UInt32     var pages_swapped_out: UInt32     var pages_dirtied: UInt32     var ref_count: UInt32     var shadow_depth: UInt16     var external_pager: UInt8     var share_mode: UInt8     var is_submap: boolean_t     var behavior: vm_behavior_t     var object_id: vm32_object_id_t     var user_wired_count: UInt16     var pages_reusable: UInt32 } ``` |
| To | ``` struct vm_region_submap_info_64 {     var protection: vm_prot_t     var max_protection: vm_prot_t     var inheritance: vm_inherit_t     var offset: memory_object_offset_t     var user_tag: UInt32     var pages_resident: UInt32     var pages_shared_now_private: UInt32     var pages_swapped_out: UInt32     var pages_dirtied: UInt32     var ref_count: UInt32     var shadow_depth: UInt16     var external_pager: UInt8     var share_mode: UInt8     var is_submap: boolean_t     var behavior: vm_behavior_t     var object_id: vm32_object_id_t     var user_wired_count: UInt16     var pages_reusable: UInt32     init()     init(protection protection: vm_prot_t, max_protection max_protection: vm_prot_t, inheritance inheritance: vm_inherit_t, offset offset: memory_object_offset_t, user_tag user_tag: UInt32, pages_resident pages_resident: UInt32, pages_shared_now_private pages_shared_now_private: UInt32, pages_swapped_out pages_swapped_out: UInt32, pages_dirtied pages_dirtied: UInt32, ref_count ref_count: UInt32, shadow_depth shadow_depth: UInt16, external_pager external_pager: UInt8, share_mode share_mode: UInt8, is_submap is_submap: boolean_t, behavior behavior: vm_behavior_t, object_id object_id: vm32_object_id_t, user_wired_count user_wired_count: UInt16, pages_reusable pages_reusable: UInt32) } ``` |

Modified vm_region_submap_short_info_64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_region_submap_short_info_64 {     var protection: vm_prot_t     var max_protection: vm_prot_t     var inheritance: vm_inherit_t     var offset: memory_object_offset_t     var user_tag: UInt32     var ref_count: UInt32     var shadow_depth: UInt16     var external_pager: UInt8     var share_mode: UInt8     var is_submap: boolean_t     var behavior: vm_behavior_t     var object_id: vm32_object_id_t     var user_wired_count: UInt16 } ``` |
| To | ``` struct vm_region_submap_short_info_64 {     var protection: vm_prot_t     var max_protection: vm_prot_t     var inheritance: vm_inherit_t     var offset: memory_object_offset_t     var user_tag: UInt32     var ref_count: UInt32     var shadow_depth: UInt16     var external_pager: UInt8     var share_mode: UInt8     var is_submap: boolean_t     var behavior: vm_behavior_t     var object_id: vm32_object_id_t     var user_wired_count: UInt16     init()     init(protection protection: vm_prot_t, max_protection max_protection: vm_prot_t, inheritance inheritance: vm_inherit_t, offset offset: memory_object_offset_t, user_tag user_tag: UInt32, ref_count ref_count: UInt32, shadow_depth shadow_depth: UInt16, external_pager external_pager: UInt8, share_mode share_mode: UInt8, is_submap is_submap: boolean_t, behavior behavior: vm_behavior_t, object_id object_id: vm32_object_id_t, user_wired_count user_wired_count: UInt16) } ``` |

Modified vm_region_top_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_region_top_info {     var obj_id: UInt32     var ref_count: UInt32     var private_pages_resident: UInt32     var shared_pages_resident: UInt32     var share_mode: UInt8 } ``` |
| To | ``` struct vm_region_top_info {     var obj_id: UInt32     var ref_count: UInt32     var private_pages_resident: UInt32     var shared_pages_resident: UInt32     var share_mode: UInt8     init()     init(obj_id obj_id: UInt32, ref_count ref_count: UInt32, private_pages_resident private_pages_resident: UInt32, shared_pages_resident shared_pages_resident: UInt32, share_mode share_mode: UInt8) } ``` |

Modified vm_statistics [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_statistics {     var free_count: natural_t     var active_count: natural_t     var inactive_count: natural_t     var wire_count: natural_t     var zero_fill_count: natural_t     var reactivations: natural_t     var pageins: natural_t     var pageouts: natural_t     var faults: natural_t     var cow_faults: natural_t     var lookups: natural_t     var hits: natural_t     var purgeable_count: natural_t     var purges: natural_t     var speculative_count: natural_t } ``` |
| To | ``` struct vm_statistics {     var free_count: natural_t     var active_count: natural_t     var inactive_count: natural_t     var wire_count: natural_t     var zero_fill_count: natural_t     var reactivations: natural_t     var pageins: natural_t     var pageouts: natural_t     var faults: natural_t     var cow_faults: natural_t     var lookups: natural_t     var hits: natural_t     var purgeable_count: natural_t     var purges: natural_t     var speculative_count: natural_t     init()     init(free_count free_count: natural_t, active_count active_count: natural_t, inactive_count inactive_count: natural_t, wire_count wire_count: natural_t, zero_fill_count zero_fill_count: natural_t, reactivations reactivations: natural_t, pageins pageins: natural_t, pageouts pageouts: natural_t, faults faults: natural_t, cow_faults cow_faults: natural_t, lookups lookups: natural_t, hits hits: natural_t, purgeable_count purgeable_count: natural_t, purges purges: natural_t, speculative_count speculative_count: natural_t) } ``` |

Modified vm_statistics64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vm_statistics64 {     var free_count: natural_t     var active_count: natural_t     var inactive_count: natural_t     var wire_count: natural_t     var zero_fill_count: UInt64     var reactivations: UInt64     var pageins: UInt64     var pageouts: UInt64     var faults: UInt64     var cow_faults: UInt64     var lookups: UInt64     var hits: UInt64     var purges: UInt64     var purgeable_count: natural_t     var speculative_count: natural_t     var decompressions: UInt64     var compressions: UInt64     var swapins: UInt64     var swapouts: UInt64     var compressor_page_count: natural_t     var throttled_count: natural_t     var external_page_count: natural_t     var internal_page_count: natural_t     var total_uncompressed_pages_in_compressor: UInt64 } ``` |
| To | ``` struct vm_statistics64 {     var free_count: natural_t     var active_count: natural_t     var inactive_count: natural_t     var wire_count: natural_t     var zero_fill_count: UInt64     var reactivations: UInt64     var pageins: UInt64     var pageouts: UInt64     var faults: UInt64     var cow_faults: UInt64     var lookups: UInt64     var hits: UInt64     var purges: UInt64     var purgeable_count: natural_t     var speculative_count: natural_t     var decompressions: UInt64     var compressions: UInt64     var swapins: UInt64     var swapouts: UInt64     var compressor_page_count: natural_t     var throttled_count: natural_t     var external_page_count: natural_t     var internal_page_count: natural_t     var total_uncompressed_pages_in_compressor: UInt64     init()     init(free_count free_count: natural_t, active_count active_count: natural_t, inactive_count inactive_count: natural_t, wire_count wire_count: natural_t, zero_fill_count zero_fill_count: UInt64, reactivations reactivations: UInt64, pageins pageins: UInt64, pageouts pageouts: UInt64, faults faults: UInt64, cow_faults cow_faults: UInt64, lookups lookups: UInt64, hits hits: UInt64, purges purges: UInt64, purgeable_count purgeable_count: natural_t, speculative_count speculative_count: natural_t, decompressions decompressions: UInt64, compressions compressions: UInt64, swapins swapins: UInt64, swapouts swapouts: UInt64, compressor_page_count compressor_page_count: natural_t, throttled_count throttled_count: natural_t, external_page_count external_page_count: natural_t, internal_page_count internal_page_count: natural_t, total_uncompressed_pages_in_compressor total_uncompressed_pages_in_compressor: UInt64) } ``` |

Modified vmspace [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vmspace {     var dummy: Int32     var dummy2: caddr_t     var dummy3: (Int32, Int32, Int32, Int32, Int32)     var dummy4: (caddr_t, caddr_t, caddr_t) } ``` |
| To | ``` struct vmspace {     var dummy: Int32     var dummy2: caddr_t     var dummy3: (Int32, Int32, Int32, Int32, Int32)     var dummy4: (caddr_t, caddr_t, caddr_t)     init()     init(dummy dummy: Int32, dummy2 dummy2: caddr_t, dummy3 dummy3: (Int32, Int32, Int32, Int32, Int32), dummy4 dummy4: (caddr_t, caddr_t, caddr_t)) } ``` |

Modified vol_attributes_attr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vol_attributes_attr {     var validattr: attribute_set_t     var nativeattr: attribute_set_t } ``` |
| To | ``` struct vol_attributes_attr {     var validattr: attribute_set_t     var nativeattr: attribute_set_t     init()     init(validattr validattr: attribute_set_t, nativeattr nativeattr: attribute_set_t) } ``` |

Modified vol_capabilities_attr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vol_capabilities_attr {     var capabilities: vol_capabilities_set_t     var valid: vol_capabilities_set_t } ``` |
| To | ``` struct vol_capabilities_attr {     var capabilities: vol_capabilities_set_t     var valid: vol_capabilities_set_t     init()     init(capabilities capabilities: vol_capabilities_set_t, valid valid: vol_capabilities_set_t) } ``` |

Modified winsize [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct winsize {     var ws_row: UInt16     var ws_col: UInt16     var ws_xpixel: UInt16     var ws_ypixel: UInt16 } ``` |
| To | ``` struct winsize {     var ws_row: UInt16     var ws_col: UInt16     var ws_xpixel: UInt16     var ws_ypixel: UInt16     init()     init(ws_row ws_row: UInt16, ws_col ws_col: UInt16, ws_xpixel ws_xpixel: UInt16, ws_ypixel ws_ypixel: UInt16) } ``` |

Modified wordexp_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct wordexp_t {     var we_wordc: UInt     var we_wordv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var we_offs: UInt } ``` |
| To | ``` struct wordexp_t {     var we_wordc: Int     var we_wordv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>     var we_offs: Int     init()     init(we_wordc we_wordc: Int, we_wordv we_wordv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, we_offs we_offs: Int) } ``` |

Modified wordexp_t.we_offs

|  | Declaration |
| --- | --- |
| From | ``` var we_offs: UInt ``` |
| To | ``` var we_offs: Int ``` |

Modified wordexp_t.we_wordc

|  | Declaration |
| --- | --- |
| From | ``` var we_wordc: UInt ``` |
| To | ``` var we_wordc: Int ``` |

Modified xsw_usage [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct xsw_usage {     var xsu_total: UInt64     var xsu_avail: UInt64     var xsu_used: UInt64     var xsu_pagesize: UInt32     var xsu_encrypted: boolean_t } ``` |
| To | ``` struct xsw_usage {     var xsu_total: UInt64     var xsu_avail: UInt64     var xsu_used: UInt64     var xsu_pagesize: UInt32     var xsu_encrypted: boolean_t     init()     init(xsu_total xsu_total: UInt64, xsu_avail xsu_avail: UInt64, xsu_used xsu_used: UInt64, xsu_pagesize xsu_pagesize: UInt32, xsu_encrypted xsu_encrypted: boolean_t) } ``` |

Modified xucred [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct xucred {     var cr_version: u_int     var cr_uid: uid_t     var cr_ngroups: Int16     var cr_groups: (gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t) } ``` |
| To | ``` struct xucred {     var cr_version: u_int     var cr_uid: uid_t     var cr_ngroups: Int16     var cr_groups: (gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t)     init()     init(cr_version cr_version: u_int, cr_uid cr_uid: uid_t, cr_ngroups cr_ngroups: Int16, cr_groups cr_groups: (gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t, gid_t)) } ``` |

Modified zone_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct zone_info {     var zi_count: integer_t     var zi_cur_size: vm_size_t     var zi_max_size: vm_size_t     var zi_elem_size: vm_size_t     var zi_alloc_size: vm_size_t     var zi_pageable: integer_t     var zi_sleepable: integer_t     var zi_exhaustible: integer_t     var zi_collectable: integer_t } ``` |
| To | ``` struct zone_info {     var zi_count: integer_t     var zi_cur_size: vm_size_t     var zi_max_size: vm_size_t     var zi_elem_size: vm_size_t     var zi_alloc_size: vm_size_t     var zi_pageable: integer_t     var zi_sleepable: integer_t     var zi_exhaustible: integer_t     var zi_collectable: integer_t     init()     init(zi_count zi_count: integer_t, zi_cur_size zi_cur_size: vm_size_t, zi_max_size zi_max_size: vm_size_t, zi_elem_size zi_elem_size: vm_size_t, zi_alloc_size zi_alloc_size: vm_size_t, zi_pageable zi_pageable: integer_t, zi_sleepable zi_sleepable: integer_t, zi_exhaustible zi_exhaustible: integer_t, zi_collectable zi_collectable: integer_t) } ``` |

Modified zone_name [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct zone_name {     var zn_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) } ``` |
| To | ``` struct zone_name {     var zn_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     init()     init(zn_name zn_name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)) } ``` |

Modified OSAtomicDequeue(COpaquePointer, Int) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func OSAtomicDequeue(_ __list: COpaquePointer, _ __offset: UInt) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func OSAtomicDequeue(_ __list: COpaquePointer, _ __offset: Int) -> UnsafeMutablePointer<Void> ``` |

Modified OSAtomicEnqueue(COpaquePointer, UnsafeMutablePointer<Void>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func OSAtomicEnqueue(_ __list: COpaquePointer, _ __new: UnsafeMutablePointer<Void>, _ __offset: UInt) ``` |
| To | ``` func OSAtomicEnqueue(_ __list: COpaquePointer, _ __new: UnsafeMutablePointer<Void>, _ __offset: Int) ``` |

Modified WCHAR_MAX

|  | Declaration |
| --- | --- |
| From | ``` var WCHAR_MAX: UInt32 { get } ``` |
| To | ``` var WCHAR_MAX: Int32 { get } ``` |

Modified accessx_np(UnsafePointer<accessx_descriptor>, Int, UnsafeMutablePointer<Int32>, uid_t) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func accessx_np(_ _: UnsafePointer<accessx_descriptor>, _ _: UInt, _ _: UnsafeMutablePointer<Int32>, _ _: uid_t) -> Int32 ``` | iOS 8.0 |
| To | ``` func accessx_np(_ _: UnsafePointer<accessx_descriptor>, _ _: Int, _ _: UnsafeMutablePointer<Int32>, _ _: uid_t) -> Int32 ``` | iOS 8.3 |

Modified add_profil(UnsafeMutablePointer<Int8>, Int, UInt, UInt32) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func add_profil(_ _: UnsafeMutablePointer<Int8>, _ _: UInt, _ _: UInt, _ _: UInt32) -> Int32 ``` | iOS 8.0 |
| To | ``` func add_profil(_ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UInt, _ _: UInt32) -> Int32 ``` | iOS 8.3 |

Modified alloca() -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func alloca(_ _: UInt) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func alloca(_ _: Int) -> UnsafeMutablePointer<Void> ``` |

Modified arc4random_buf(UnsafeMutablePointer<Void>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func arc4random_buf(_ _: UnsafeMutablePointer<Void>, _ _: UInt) ``` |
| To | ``` func arc4random_buf(_ _: UnsafeMutablePointer<Void>, _ _: Int) ``` |

Modified bcmp(UnsafePointer<Void>, UnsafePointer<Void>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func bcmp(_ _: UnsafePointer<Void>, _ _: UnsafePointer<Void>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func bcmp(_ _: UnsafePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified bcopy(UnsafePointer<Void>, UnsafeMutablePointer<Void>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func bcopy(_ _: UnsafePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: UInt) ``` | iOS 8.0 |
| To | ``` func bcopy(_ _: UnsafePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: Int) ``` | iOS 8.3 |

Modified bsearch(UnsafePointer<Void>, UnsafePointer<Void>, Int, Int, CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func bsearch(_ _: UnsafePointer<Void>, _ _: UnsafePointer<Void>, _ _: UInt, _ _: UInt, _ _: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) -> UnsafeMutablePointer<Void> ``` | iOS 8.0 |
| To | ``` func bsearch(_ _: UnsafePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int, _ _: Int, _ _: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) -> UnsafeMutablePointer<Void> ``` | iOS 8.3 |

Modified bsearch_b(UnsafePointer<Void>, UnsafePointer<Void>, Int, Int,((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func bsearch_b(_ _: UnsafePointer<Void>, _ _: UnsafePointer<Void>, _ _: UInt, _ _: UInt, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func bsearch_b(_ _: UnsafePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int, _ _: Int, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> UnsafeMutablePointer<Void> ``` |

Modified bzero(UnsafeMutablePointer<Void>, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func bzero(_ _: UnsafeMutablePointer<Void>, _ _: UInt) ``` | iOS 8.0 |
| To | ``` func bzero(_ _: UnsafeMutablePointer<Void>, _ _: Int) ``` | iOS 8.3 |

Modified calloc(Int, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func calloc(_ _: UInt, _ _: UInt) -> UnsafeMutablePointer<Void> ``` | iOS 8.0 |
| To | ``` func calloc(_ _: Int, _ _: Int) -> UnsafeMutablePointer<Void> ``` | iOS 8.3 |

Modified confstr(Int32, UnsafeMutablePointer<Int8>, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func confstr(_ _: Int32, _ _: UnsafeMutablePointer<Int8>, _ _: UInt) -> UInt ``` | iOS 8.0 |
| To | ``` func confstr(_ _: Int32, _ _: UnsafeMutablePointer<Int8>, _ _: Int) -> Int ``` | iOS 8.3 |

Modified fgetattrlist(Int32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int, UInt) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fgetattrlist(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UInt) -> Int32 ``` |
| To | ``` func fgetattrlist(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: UInt) -> Int32 ``` |

Modified fgetln(UnsafeMutablePointer<FILE>, UnsafeMutablePointer<Int>) -> UnsafeMutablePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func fgetln(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<UInt>) -> UnsafeMutablePointer<Int8> ``` | iOS 8.0 |
| To | ``` func fgetln(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<Int>) -> UnsafeMutablePointer<Int8> ``` | iOS 8.3 |

Modified fgetwln(UnsafeMutablePointer<FILE>, UnsafeMutablePointer<Int>) -> UnsafeMutablePointer<wchar_t>

|  | Declaration |
| --- | --- |
| From | ``` func fgetwln(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<UInt>) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func fgetwln(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<Int>) -> UnsafeMutablePointer<wchar_t> ``` |

Modified fread(UnsafeMutablePointer<Void>, Int, Int, UnsafeMutablePointer<FILE>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func fread(_ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UInt, _ _: UnsafeMutablePointer<FILE>) -> UInt ``` | iOS 8.0 |
| To | ``` func fread(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<FILE>) -> Int ``` | iOS 8.3 |

Modified fsetattrlist(Int32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int, UInt) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func fsetattrlist(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UInt) -> Int32 ``` |
| To | ``` func fsetattrlist(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: UInt) -> Int32 ``` |

Modified fwrite(UnsafePointer<Void>, Int, Int, UnsafeMutablePointer<FILE>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func fwrite(_ _: UnsafePointer<Void>, _ _: UInt, _ _: UInt, _ _: UnsafeMutablePointer<FILE>) -> UInt ``` | iOS 8.0 |
| To | ``` func fwrite(_ _: UnsafePointer<Void>, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<FILE>) -> Int ``` | iOS 8.3 |

Modified getattrlist(UnsafePointer<Int8>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int, UInt) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getattrlist(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func getattrlist(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: UInt) -> Int32 ``` | iOS 8.3 |

Modified getattrlistat(Int32, UnsafePointer<Int8>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int, UInt) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getattrlistat(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UInt) -> Int32 ``` |
| To | ``` func getattrlistat(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: UInt) -> Int32 ``` |

Modified getattrlistbulk(Int32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int, UInt64) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func getattrlistbulk(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UInt64) -> Int32 ``` |
| To | ``` func getattrlistbulk(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: UInt64) -> Int32 ``` |

Modified getcwd(UnsafeMutablePointer<Int8>, Int) -> UnsafeMutablePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getcwd(_ _: UnsafeMutablePointer<Int8>, _ _: UInt) -> UnsafeMutablePointer<Int8> ``` | iOS 8.0 |
| To | ``` func getcwd(_ _: UnsafeMutablePointer<Int8>, _ _: Int) -> UnsafeMutablePointer<Int8> ``` | iOS 8.3 |

Modified getdelim(UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, UnsafeMutablePointer<Int>, Int32, UnsafeMutablePointer<FILE>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func getdelim(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<UInt>, _ _: Int32, _ _: UnsafeMutablePointer<FILE>) -> Int ``` |
| To | ``` func getdelim(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<Int>, _ _: Int32, _ _: UnsafeMutablePointer<FILE>) -> Int ``` |

Modified getdirentriesattr(Int32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<UInt>, UnsafeMutablePointer<UInt>, UInt) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getdirentriesattr(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UnsafeMutablePointer<UInt>, _ _: UnsafeMutablePointer<UInt>, _ _: UnsafeMutablePointer<UInt>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func getdirentriesattr(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: UnsafeMutablePointer<UInt>, _ _: UnsafeMutablePointer<UInt>, _ _: UnsafeMutablePointer<UInt>, _ _: UInt) -> Int32 ``` | iOS 8.3 |

Modified getgrgid_r(gid_t, UnsafeMutablePointer<group>, UnsafeMutablePointer<Int8>, Int, UnsafeMutablePointer<UnsafeMutablePointer<group>>) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getgrgid_r(_ _: gid_t, _ _: UnsafeMutablePointer<group>, _ _: UnsafeMutablePointer<Int8>, _ _: UInt, _ _: UnsafeMutablePointer<UnsafeMutablePointer<group>>) -> Int32 ``` | iOS 8.0 |
| To | ``` func getgrgid_r(_ _: gid_t, _ _: UnsafeMutablePointer<group>, _ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<group>>) -> Int32 ``` | iOS 8.3 |

Modified getgrnam_r(UnsafePointer<Int8>, UnsafeMutablePointer<group>, UnsafeMutablePointer<Int8>, Int, UnsafeMutablePointer<UnsafeMutablePointer<group>>) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getgrnam_r(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<group>, _ _: UnsafeMutablePointer<Int8>, _ _: UInt, _ _: UnsafeMutablePointer<UnsafeMutablePointer<group>>) -> Int32 ``` | iOS 8.0 |
| To | ``` func getgrnam_r(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<group>, _ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<group>>) -> Int32 ``` | iOS 8.3 |

Modified getgruuid_r(UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<group>, UnsafeMutablePointer<Int8>, Int, UnsafeMutablePointer<UnsafeMutablePointer<group>>) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getgruuid_r(_ _: UnsafeMutablePointer<UInt8>, _ _: UnsafeMutablePointer<group>, _ _: UnsafeMutablePointer<Int8>, _ _: UInt, _ _: UnsafeMutablePointer<UnsafeMutablePointer<group>>) -> Int32 ``` | iOS 8.0 |
| To | ``` func getgruuid_r(_ _: UnsafeMutablePointer<UInt8>, _ _: UnsafeMutablePointer<group>, _ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<group>>) -> Int32 ``` | iOS 8.3 |

Modified gethostname(UnsafeMutablePointer<Int8>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func gethostname(_ _: UnsafeMutablePointer<Int8>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func gethostname(_ _: UnsafeMutablePointer<Int8>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified getipnodebyaddr(UnsafePointer<Void>, Int, Int32, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<hostent>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getipnodebyaddr(_ _: UnsafePointer<Void>, _ _: UInt, _ _: Int32, _ _: UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<hostent> ``` | iOS 8.0 |
| To | ``` func getipnodebyaddr(_ _: UnsafePointer<Void>, _ _: Int, _ _: Int32, _ _: UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<hostent> ``` | iOS 8.3 |

Modified getline(UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<FILE>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func getline(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<UInt>, _ _: UnsafeMutablePointer<FILE>) -> Int ``` |
| To | ``` func getline(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<Int>, _ _: UnsafeMutablePointer<FILE>) -> Int ``` |

Modified getlogin_r(UnsafeMutablePointer<Int8>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getlogin_r(_ _: UnsafeMutablePointer<Int8>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func getlogin_r(_ _: UnsafeMutablePointer<Int8>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified getpwnam_r(UnsafePointer<Int8>, UnsafeMutablePointer<passwd>, UnsafeMutablePointer<Int8>, Int, UnsafeMutablePointer<UnsafeMutablePointer<passwd>>) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getpwnam_r(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<passwd>, _ _: UnsafeMutablePointer<Int8>, _ _: UInt, _ _: UnsafeMutablePointer<UnsafeMutablePointer<passwd>>) -> Int32 ``` | iOS 8.0 |
| To | ``` func getpwnam_r(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<passwd>, _ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<passwd>>) -> Int32 ``` | iOS 8.3 |

Modified getpwuid_r(uid_t, UnsafeMutablePointer<passwd>, UnsafeMutablePointer<Int8>, Int, UnsafeMutablePointer<UnsafeMutablePointer<passwd>>) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getpwuid_r(_ _: uid_t, _ _: UnsafeMutablePointer<passwd>, _ _: UnsafeMutablePointer<Int8>, _ _: UInt, _ _: UnsafeMutablePointer<UnsafeMutablePointer<passwd>>) -> Int32 ``` | iOS 8.0 |
| To | ``` func getpwuid_r(_ _: uid_t, _ _: UnsafeMutablePointer<passwd>, _ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<passwd>>) -> Int32 ``` | iOS 8.3 |

Modified getpwuuid_r(UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<passwd>, UnsafeMutablePointer<Int8>, Int, UnsafeMutablePointer<UnsafeMutablePointer<passwd>>) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getpwuuid_r(_ _: UnsafeMutablePointer<UInt8>, _ _: UnsafeMutablePointer<passwd>, _ _: UnsafeMutablePointer<Int8>, _ _: UInt, _ _: UnsafeMutablePointer<UnsafeMutablePointer<passwd>>) -> Int32 ``` | iOS 8.0 |
| To | ``` func getpwuuid_r(_ _: UnsafeMutablePointer<UInt8>, _ _: UnsafeMutablePointer<passwd>, _ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<UnsafeMutablePointer<passwd>>) -> Int32 ``` | iOS 8.3 |

Modified hcreate() -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func hcreate(_ _: UInt) -> Int32 ``` |
| To | ``` func hcreate(_ _: Int) -> Int32 ``` |

Modified heapsort(UnsafeMutablePointer<Void>, Int, Int, CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func heapsort(_ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UInt, _ _: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) -> Int32 ``` | iOS 8.0 |
| To | ``` func heapsort(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) -> Int32 ``` | iOS 8.3 |

Modified heapsort_b(UnsafeMutablePointer<Void>, Int, Int,((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func heapsort_b(_ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UInt, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> Int32 ``` |
| To | ``` func heapsort_b(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> Int32 ``` |

Modified iconv(iconv_t, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, UnsafeMutablePointer<Int>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func iconv(_ _: iconv_t, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<UInt>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<UInt>) -> UInt ``` | iOS 8.0 |
| To | ``` func iconv(_ _: iconv_t, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<Int>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: UnsafeMutablePointer<Int>) -> Int ``` | iOS 8.3 |

Modified iconv_unicode_mb_to_uc_fallback

|  | Declaration |
| --- | --- |
| From | ``` typealias iconv_unicode_mb_to_uc_fallback = CFunctionPointer<((UnsafePointer<Int8>, UInt, CFunctionPointer<((UnsafePointer<UInt32>, UInt, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias iconv_unicode_mb_to_uc_fallback = CFunctionPointer<((UnsafePointer<Int8>, Int, CFunctionPointer<((UnsafePointer<UInt32>, Int, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified iconv_unicode_uc_to_mb_fallback

|  | Declaration |
| --- | --- |
| From | ``` typealias iconv_unicode_uc_to_mb_fallback = CFunctionPointer<((UInt32, CFunctionPointer<((UnsafePointer<Int8>, UInt, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias iconv_unicode_uc_to_mb_fallback = CFunctionPointer<((UInt32, CFunctionPointer<((UnsafePointer<Int8>, Int, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified iconv_wchar_mb_to_wc_fallback

|  | Declaration |
| --- | --- |
| From | ``` typealias iconv_wchar_mb_to_wc_fallback = CFunctionPointer<((UnsafePointer<Int8>, UInt, CFunctionPointer<((UnsafePointer<wchar_t>, UInt, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias iconv_wchar_mb_to_wc_fallback = CFunctionPointer<((UnsafePointer<Int8>, Int, CFunctionPointer<((UnsafePointer<wchar_t>, Int, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified iconv_wchar_wc_to_mb_fallback

|  | Declaration |
| --- | --- |
| From | ``` typealias iconv_wchar_wc_to_mb_fallback = CFunctionPointer<((wchar_t, CFunctionPointer<((UnsafePointer<Int8>, UInt, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias iconv_wchar_wc_to_mb_fallback = CFunctionPointer<((wchar_t, CFunctionPointer<((UnsafePointer<Int8>, Int, UnsafeMutablePointer<Void>) -> Void)>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified inet6_rthdr_space(Int32, Int32) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func inet6_rthdr_space(_ _: Int32, _ _: Int32) -> UInt ``` | iOS 8.0 |
| To | ``` func inet6_rthdr_space(_ _: Int32, _ _: Int32) -> Int ``` | iOS 8.3 |

Modified initstate(UInt32, UnsafeMutablePointer<Int8>, Int) -> UnsafeMutablePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func initstate(_ _: UInt32, _ _: UnsafeMutablePointer<Int8>, _ _: UInt) -> UnsafeMutablePointer<Int8> ``` | iOS 8.0 |
| To | ``` func initstate(_ _: UInt32, _ _: UnsafeMutablePointer<Int8>, _ _: Int) -> UnsafeMutablePointer<Int8> ``` | iOS 8.3 |

Modified lfind(UnsafePointer<Void>, UnsafePointer<Void>, UnsafeMutablePointer<Int>, Int, CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func lfind(_ _: UnsafePointer<Void>, _ _: UnsafePointer<Void>, _ _: UnsafeMutablePointer<UInt>, _ _: UInt, _ _: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) -> UnsafeMutablePointer<Void> ``` | iOS 8.0 |
| To | ``` func lfind(_ _: UnsafePointer<Void>, _ _: UnsafePointer<Void>, _ _: UnsafeMutablePointer<Int>, _ _: Int, _ _: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) -> UnsafeMutablePointer<Void> ``` | iOS 8.3 |

Modified lsearch(UnsafePointer<Void>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>, Int, CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func lsearch(_ _: UnsafePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<UInt>, _ _: UInt, _ _: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) -> UnsafeMutablePointer<Void> ``` | iOS 8.0 |
| To | ``` func lsearch(_ _: UnsafePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>, _ _: Int, _ _: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) -> UnsafeMutablePointer<Void> ``` | iOS 8.3 |

Modified mach_port_allocate_full(ipc_space_t, mach_port_right_t, mach_port_t, UnsafeMutablePointer<mach_port_qos_t>, UnsafeMutablePointer<mach_port_name_t>) -> kern_return_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func mach_port_allocate_full(_ task: ipc_space_t, _ right: mach_port_right_t, _ proto: mach_port_t, _ qos: COpaquePointer, _ name: UnsafeMutablePointer<mach_port_name_t>) -> kern_return_t ``` | iOS 8.0 |
| To | ``` func mach_port_allocate_full(_ task: ipc_space_t, _ right: mach_port_right_t, _ proto: mach_port_t, _ qos: UnsafeMutablePointer<mach_port_qos_t>, _ name: UnsafeMutablePointer<mach_port_name_t>) -> kern_return_t ``` | iOS 8.3 |

Modified mach_port_allocate_qos(ipc_space_t, mach_port_right_t, UnsafeMutablePointer<mach_port_qos_t>, UnsafeMutablePointer<mach_port_name_t>) -> kern_return_t

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func mach_port_allocate_qos(_ task: ipc_space_t, _ right: mach_port_right_t, _ qos: COpaquePointer, _ name: UnsafeMutablePointer<mach_port_name_t>) -> kern_return_t ``` | iOS 8.0 |
| To | ``` func mach_port_allocate_qos(_ task: ipc_space_t, _ right: mach_port_right_t, _ qos: UnsafeMutablePointer<mach_port_qos_t>, _ name: UnsafeMutablePointer<mach_port_name_t>) -> kern_return_t ``` | iOS 8.3 |

Modified madvise(UnsafeMutablePointer<Void>, Int, Int32) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func madvise(_ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: Int32) -> Int32 ``` | iOS 8.0 |
| To | ``` func madvise(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32) -> Int32 ``` | iOS 8.3 |

Modified malloc() -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func malloc(_ _: UInt) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func malloc(_ _: Int) -> UnsafeMutablePointer<Void> ``` |

Modified malloc_good_size(Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func malloc_good_size(_ size: UInt) -> UInt ``` | iOS 8.0 |
| To | ``` func malloc_good_size(_ size: Int) -> Int ``` | iOS 8.3 |

Modified malloc_zone_batch_malloc(UnsafeMutablePointer<malloc_zone_t>, Int, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UInt32) -> UInt32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func malloc_zone_batch_malloc(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ size: UInt, _ results: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ num_requested: UInt32) -> UInt32 ``` | iOS 8.0 |
| To | ``` func malloc_zone_batch_malloc(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ size: Int, _ results: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ num_requested: UInt32) -> UInt32 ``` | iOS 8.3 |

Modified malloc_zone_calloc(UnsafeMutablePointer<malloc_zone_t>, Int, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func malloc_zone_calloc(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ num_items: UInt, _ size: UInt) -> UnsafeMutablePointer<Void> ``` | iOS 8.0 |
| To | ``` func malloc_zone_calloc(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ num_items: Int, _ size: Int) -> UnsafeMutablePointer<Void> ``` | iOS 8.3 |

Modified malloc_zone_malloc(UnsafeMutablePointer<malloc_zone_t>, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func malloc_zone_malloc(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ size: UInt) -> UnsafeMutablePointer<Void> ``` | iOS 8.0 |
| To | ``` func malloc_zone_malloc(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ size: Int) -> UnsafeMutablePointer<Void> ``` | iOS 8.3 |

Modified malloc_zone_memalign(UnsafeMutablePointer<malloc_zone_t>, Int, Int) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_memalign(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ alignment: UInt, _ size: UInt) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func malloc_zone_memalign(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ alignment: Int, _ size: Int) -> UnsafeMutablePointer<Void> ``` |

Modified malloc_zone_pressure_relief(UnsafeMutablePointer<malloc_zone_t>, Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_pressure_relief(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ goal: UInt) -> UInt ``` |
| To | ``` func malloc_zone_pressure_relief(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ goal: Int) -> Int ``` |

Modified malloc_zone_realloc(UnsafeMutablePointer<malloc_zone_t>, UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func malloc_zone_realloc(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ ptr: UnsafeMutablePointer<Void>, _ size: UInt) -> UnsafeMutablePointer<Void> ``` | iOS 8.0 |
| To | ``` func malloc_zone_realloc(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ ptr: UnsafeMutablePointer<Void>, _ size: Int) -> UnsafeMutablePointer<Void> ``` | iOS 8.3 |

Modified malloc_zone_valloc(UnsafeMutablePointer<malloc_zone_t>, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func malloc_zone_valloc(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ size: UInt) -> UnsafeMutablePointer<Void> ``` | iOS 8.0 |
| To | ``` func malloc_zone_valloc(_ zone: UnsafeMutablePointer<malloc_zone_t>, _ size: Int) -> UnsafeMutablePointer<Void> ``` | iOS 8.3 |

Modified mblen(UnsafePointer<Int8>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func mblen(_ _: UnsafePointer<Int8>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func mblen(_ _: UnsafePointer<Int8>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified mbrlen(UnsafePointer<Int8>, Int, UnsafeMutablePointer<mbstate_t>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func mbrlen(_ _: UnsafePointer<Int8>, _ _: UInt, _ _: COpaquePointer) -> UInt ``` | iOS 8.0 |
| To | ``` func mbrlen(_ _: UnsafePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>) -> Int ``` | iOS 8.3 |

Modified mbrtowc(UnsafeMutablePointer<wchar_t>, UnsafePointer<Int8>, Int, UnsafeMutablePointer<mbstate_t>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func mbrtowc(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<Int8>, _ _: UInt, _ _: COpaquePointer) -> UInt ``` | iOS 8.0 |
| To | ``` func mbrtowc(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>) -> Int ``` | iOS 8.3 |

Modified mbsinit() -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mbsinit(_ _: COpaquePointer) -> Int32 ``` |
| To | ``` func mbsinit(_ _: UnsafePointer<mbstate_t>) -> Int32 ``` |

Modified mbsnrtowcs(UnsafeMutablePointer<wchar_t>, UnsafeMutablePointer<UnsafePointer<Int8>>, Int, Int, UnsafeMutablePointer<mbstate_t>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func mbsnrtowcs(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: UInt, _ _: UInt, _ _: COpaquePointer) -> UInt ``` | iOS 8.0 |
| To | ``` func mbsnrtowcs(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>) -> Int ``` | iOS 8.3 |

Modified mbsrtowcs(UnsafeMutablePointer<wchar_t>, UnsafeMutablePointer<UnsafePointer<Int8>>, Int, UnsafeMutablePointer<mbstate_t>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func mbsrtowcs(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: UInt, _ _: COpaquePointer) -> UInt ``` | iOS 8.0 |
| To | ``` func mbsrtowcs(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafeMutablePointer<UnsafePointer<Int8>>, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>) -> Int ``` | iOS 8.3 |

Modified mbstowcs(UnsafeMutablePointer<wchar_t>, UnsafePointer<Int8>, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func mbstowcs(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<Int8>, _ _: UInt) -> UInt ``` | iOS 8.0 |
| To | ``` func mbstowcs(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<Int8>, _ _: Int) -> Int ``` | iOS 8.3 |

Modified mbtowc(UnsafeMutablePointer<wchar_t>, UnsafePointer<Int8>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func mbtowc(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<Int8>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func mbtowc(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<Int8>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified memccpy(UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int32, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func memccpy(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int32, _ _: UInt) -> UnsafeMutablePointer<Void> ``` | iOS 8.0 |
| To | ``` func memccpy(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int32, _ _: Int) -> UnsafeMutablePointer<Void> ``` | iOS 8.3 |

Modified memchr(UnsafePointer<Void>, Int32, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func memchr(_ _: UnsafePointer<Void>, _ _: Int32, _ _: UInt) -> UnsafeMutablePointer<Void> ``` | iOS 8.0 |
| To | ``` func memchr(_ _: UnsafePointer<Void>, _ _: Int32, _ _: Int) -> UnsafeMutablePointer<Void> ``` | iOS 8.3 |

Modified memcpy(UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func memcpy(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: UInt) -> UnsafeMutablePointer<Void> ``` | iOS 8.0 |
| To | ``` func memcpy(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int) -> UnsafeMutablePointer<Void> ``` | iOS 8.3 |

Modified memmem(UnsafePointer<Void>, Int, UnsafePointer<Void>, Int) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func memmem(_ _: UnsafePointer<Void>, _ _: UInt, _ _: UnsafePointer<Void>, _ _: UInt) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func memmem(_ _: UnsafePointer<Void>, _ _: Int, _ _: UnsafePointer<Void>, _ _: Int) -> UnsafeMutablePointer<Void> ``` |

Modified memmove(UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func memmove(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: UInt) -> UnsafeMutablePointer<Void> ``` | iOS 8.0 |
| To | ``` func memmove(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int) -> UnsafeMutablePointer<Void> ``` | iOS 8.3 |

Modified memset(UnsafeMutablePointer<Void>, Int32, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func memset(_ _: UnsafeMutablePointer<Void>, _ _: Int32, _ _: UInt) -> UnsafeMutablePointer<Void> ``` | iOS 8.0 |
| To | ``` func memset(_ _: UnsafeMutablePointer<Void>, _ _: Int32, _ _: Int) -> UnsafeMutablePointer<Void> ``` | iOS 8.3 |

Modified memset_pattern16(UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func memset_pattern16(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: UInt) ``` |
| To | ``` func memset_pattern16(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int) ``` |

Modified memset_pattern4(UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func memset_pattern4(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: UInt) ``` |
| To | ``` func memset_pattern4(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int) ``` |

Modified memset_pattern8(UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int)

|  | Declaration |
| --- | --- |
| From | ``` func memset_pattern8(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: UInt) ``` |
| To | ``` func memset_pattern8(_ _: UnsafeMutablePointer<Void>, _ _: UnsafePointer<Void>, _ _: Int) ``` |

Modified memset_s(UnsafeMutablePointer<Void>, Int, Int32, Int) -> errno_t

|  | Declaration |
| --- | --- |
| From | ``` func memset_s(_ _: UnsafeMutablePointer<Void>, _ _: rsize_t, _ _: Int32, _ _: rsize_t) -> errno_t ``` |
| To | ``` func memset_s(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32, _ _: Int) -> errno_t ``` |

Modified mergesort(UnsafeMutablePointer<Void>, Int, Int, CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func mergesort(_ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UInt, _ _: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) -> Int32 ``` | iOS 8.0 |
| To | ``` func mergesort(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) -> Int32 ``` | iOS 8.3 |

Modified mergesort_b(UnsafeMutablePointer<Void>, Int, Int,((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func mergesort_b(_ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UInt, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> Int32 ``` |
| To | ``` func mergesort_b(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) -> Int32 ``` |

Modified mig_routine_arg_descriptor_t

|  | Declaration |
| --- | --- |
| From | ``` typealias mig_routine_arg_descriptor_t = COpaquePointer ``` |
| To | ``` typealias mig_routine_arg_descriptor_t = UnsafeMutablePointer<mach_msg_type_descriptor_t> ``` |

Modified mincore(UnsafePointer<Void>, Int, UnsafeMutablePointer<Int8>) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func mincore(_ _: UnsafePointer<Void>, _ _: UInt, _ _: UnsafeMutablePointer<Int8>) -> Int32 ``` | iOS 8.0 |
| To | ``` func mincore(_ _: UnsafePointer<Void>, _ _: Int, _ _: UnsafeMutablePointer<Int8>) -> Int32 ``` | iOS 8.3 |

Modified minherit(UnsafeMutablePointer<Void>, Int, Int32) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func minherit(_ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: Int32) -> Int32 ``` | iOS 8.0 |
| To | ``` func minherit(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32) -> Int32 ``` | iOS 8.3 |

Modified mlock(UnsafePointer<Void>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func mlock(_ _: UnsafePointer<Void>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func mlock(_ _: UnsafePointer<Void>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified mmap(UnsafeMutablePointer<Void>, Int, Int32, Int32, Int32, off_t) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func mmap(_ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: Int32, _ _: Int32, _ _: Int32, _ _: off_t) -> UnsafeMutablePointer<Void> ``` | iOS 8.0 |
| To | ``` func mmap(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32, _ _: Int32, _ _: Int32, _ _: off_t) -> UnsafeMutablePointer<Void> ``` | iOS 8.3 |

Modified mprotect(UnsafeMutablePointer<Void>, Int, Int32) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func mprotect(_ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: Int32) -> Int32 ``` | iOS 8.0 |
| To | ``` func mprotect(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32) -> Int32 ``` | iOS 8.3 |

Modified msgrcv(Int32, UnsafeMutablePointer<Void>, Int, Int, Int32) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func msgrcv(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: Int, _ _: Int32) -> Int ``` | iOS 8.0 |
| To | ``` func msgrcv(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: Int32) -> Int ``` | iOS 8.3 |

Modified msgsnd(Int32, UnsafePointer<Void>, Int, Int32) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func msgsnd(_ _: Int32, _ _: UnsafePointer<Void>, _ _: UInt, _ _: Int32) -> Int32 ``` | iOS 8.0 |
| To | ``` func msgsnd(_ _: Int32, _ _: UnsafePointer<Void>, _ _: Int, _ _: Int32) -> Int32 ``` | iOS 8.3 |

Modified msync(UnsafeMutablePointer<Void>, Int, Int32) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func msync(_ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: Int32) -> Int32 ``` | iOS 8.0 |
| To | ``` func msync(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32) -> Int32 ``` | iOS 8.3 |

Modified munlock(UnsafePointer<Void>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func munlock(_ _: UnsafePointer<Void>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func munlock(_ _: UnsafePointer<Void>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified munmap(UnsafeMutablePointer<Void>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func munmap(_ _: UnsafeMutablePointer<Void>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func munmap(_ _: UnsafeMutablePointer<Void>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified posix_madvise(UnsafeMutablePointer<Void>, Int, Int32) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func posix_madvise(_ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: Int32) -> Int32 ``` | iOS 8.0 |
| To | ``` func posix_madvise(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32) -> Int32 ``` | iOS 8.3 |

Modified posix_memalign(UnsafeMutablePointer<UnsafeMutablePointer<Void>>, Int, Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_memalign(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ _: UInt, _ _: UInt) -> Int32 ``` |
| To | ``` func posix_memalign(_ _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ _: Int, _ _: Int) -> Int32 ``` |

Modified posix_spawnattr_getbinpref_np(UnsafePointer<posix_spawnattr_t>, Int, UnsafeMutablePointer<cpu_type_t>, UnsafeMutablePointer<Int>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnattr_getbinpref_np(_ _: UnsafePointer<posix_spawnattr_t>, _ _: UInt, _ _: UnsafeMutablePointer<cpu_type_t>, _ _: UnsafeMutablePointer<UInt>) -> Int32 ``` |
| To | ``` func posix_spawnattr_getbinpref_np(_ _: UnsafePointer<posix_spawnattr_t>, _ _: Int, _ _: UnsafeMutablePointer<cpu_type_t>, _ _: UnsafeMutablePointer<Int>) -> Int32 ``` |

Modified posix_spawnattr_setbinpref_np(UnsafeMutablePointer<posix_spawnattr_t>, Int, UnsafeMutablePointer<cpu_type_t>, UnsafeMutablePointer<Int>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func posix_spawnattr_setbinpref_np(_ _: UnsafeMutablePointer<posix_spawnattr_t>, _ _: UInt, _ _: UnsafeMutablePointer<cpu_type_t>, _ _: UnsafeMutablePointer<UInt>) -> Int32 ``` |
| To | ``` func posix_spawnattr_setbinpref_np(_ _: UnsafeMutablePointer<posix_spawnattr_t>, _ _: Int, _ _: UnsafeMutablePointer<cpu_type_t>, _ _: UnsafeMutablePointer<Int>) -> Int32 ``` |

Modified pread(Int32, UnsafeMutablePointer<Void>, Int, off_t) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func pread(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: off_t) -> Int ``` | iOS 8.0 |
| To | ``` func pread(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: off_t) -> Int ``` | iOS 8.3 |

Modified profil(UnsafeMutablePointer<Int8>, Int, UInt, UInt32) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func profil(_ _: UnsafeMutablePointer<Int8>, _ _: UInt, _ _: UInt, _ _: UInt32) -> Int32 ``` | iOS 8.0 |
| To | ``` func profil(_ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UInt, _ _: UInt32) -> Int32 ``` | iOS 8.3 |

Modified psort(UnsafeMutablePointer<Void>, Int, Int, CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>)

|  | Declaration |
| --- | --- |
| From | ``` func psort(_ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UInt, _ _: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) ``` |
| To | ``` func psort(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) ``` |

Modified psort_b(UnsafeMutablePointer<Void>, Int, Int,((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!)

|  | Declaration |
| --- | --- |
| From | ``` func psort_b(_ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UInt, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) ``` |
| To | ``` func psort_b(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) ``` |

Modified psort_r(UnsafeMutablePointer<Void>, Int, Int, UnsafeMutablePointer<Void>, CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>)

|  | Declaration |
| --- | --- |
| From | ``` func psort_r(_ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UInt, _ _: UnsafeMutablePointer<Void>, _ _: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) ``` |
| To | ``` func psort_r(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) ``` |

Modified pthread_attr_getguardsize(UnsafePointer<pthread_attr_t>, UnsafeMutablePointer<Int>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_attr_getguardsize(_ _: UnsafePointer<pthread_attr_t>, _ _: UnsafeMutablePointer<UInt>) -> Int32 ``` |
| To | ``` func pthread_attr_getguardsize(_ _: UnsafePointer<pthread_attr_t>, _ _: UnsafeMutablePointer<Int>) -> Int32 ``` |

Modified pthread_attr_getstack(UnsafePointer<pthread_attr_t>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<Int>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_attr_getstack(_ _: UnsafePointer<pthread_attr_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ _: UnsafeMutablePointer<UInt>) -> Int32 ``` |
| To | ``` func pthread_attr_getstack(_ _: UnsafePointer<pthread_attr_t>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ _: UnsafeMutablePointer<Int>) -> Int32 ``` |

Modified pthread_attr_getstacksize(UnsafePointer<pthread_attr_t>, UnsafeMutablePointer<Int>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_attr_getstacksize(_ _: UnsafePointer<pthread_attr_t>, _ _: UnsafeMutablePointer<UInt>) -> Int32 ``` |
| To | ``` func pthread_attr_getstacksize(_ _: UnsafePointer<pthread_attr_t>, _ _: UnsafeMutablePointer<Int>) -> Int32 ``` |

Modified pthread_attr_setguardsize(UnsafeMutablePointer<pthread_attr_t>, Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_attr_setguardsize(_ _: UnsafeMutablePointer<pthread_attr_t>, _ _: UInt) -> Int32 ``` |
| To | ``` func pthread_attr_setguardsize(_ _: UnsafeMutablePointer<pthread_attr_t>, _ _: Int) -> Int32 ``` |

Modified pthread_attr_setstack(UnsafeMutablePointer<pthread_attr_t>, UnsafeMutablePointer<Void>, Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_attr_setstack(_ _: UnsafeMutablePointer<pthread_attr_t>, _ _: UnsafeMutablePointer<Void>, _ _: UInt) -> Int32 ``` |
| To | ``` func pthread_attr_setstack(_ _: UnsafeMutablePointer<pthread_attr_t>, _ _: UnsafeMutablePointer<Void>, _ _: Int) -> Int32 ``` |

Modified pthread_attr_setstacksize(UnsafeMutablePointer<pthread_attr_t>, Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_attr_setstacksize(_ _: UnsafeMutablePointer<pthread_attr_t>, _ _: UInt) -> Int32 ``` |
| To | ``` func pthread_attr_setstacksize(_ _: UnsafeMutablePointer<pthread_attr_t>, _ _: Int) -> Int32 ``` |

Modified pthread_get_stacksize_np() -> Int

|  | Declaration |
| --- | --- |
| From | ``` func pthread_get_stacksize_np(_ _: pthread_t) -> UInt ``` |
| To | ``` func pthread_get_stacksize_np(_ _: pthread_t) -> Int ``` |

Modified pthread_getname_np(pthread_t, UnsafeMutablePointer<Int8>, Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_getname_np(_ _: pthread_t, _ _: UnsafeMutablePointer<Int8>, _ _: UInt) -> Int32 ``` |
| To | ``` func pthread_getname_np(_ _: pthread_t, _ _: UnsafeMutablePointer<Int8>, _ _: Int) -> Int32 ``` |

Modified pwrite(Int32, UnsafePointer<Void>, Int, off_t) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func pwrite(_ _: Int32, _ _: UnsafePointer<Void>, _ _: UInt, _ _: off_t) -> Int ``` | iOS 8.0 |
| To | ``` func pwrite(_ _: Int32, _ _: UnsafePointer<Void>, _ _: Int, _ _: off_t) -> Int ``` | iOS 8.3 |

Modified qsort(UnsafeMutablePointer<Void>, Int, Int, CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func qsort(_ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UInt, _ _: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) ``` | iOS 8.0 |
| To | ``` func qsort(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: CFunctionPointer<((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) ``` | iOS 8.3 |

Modified qsort_b(UnsafeMutablePointer<Void>, Int, Int,((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!)

|  | Declaration |
| --- | --- |
| From | ``` func qsort_b(_ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UInt, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) ``` |
| To | ``` func qsort_b(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: ((UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)!) ``` |

Modified qsort_r(UnsafeMutablePointer<Void>, Int, Int, UnsafeMutablePointer<Void>, CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func qsort_r(_ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UInt, _ _: UnsafeMutablePointer<Void>, _ _: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) ``` | iOS 8.0 |
| To | ``` func qsort_r(_ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<Void>, _ _: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafePointer<Void>, UnsafePointer<Void>) -> Int32)>) ``` | iOS 8.3 |

Modified rb_tree_count() -> Int

|  | Declaration |
| --- | --- |
| From | ``` func rb_tree_count(_ _: UnsafeMutablePointer<rb_tree_t>) -> UInt ``` |
| To | ``` func rb_tree_count(_ _: UnsafeMutablePointer<rb_tree_t>) -> Int ``` |

Modified read(Int32, UnsafeMutablePointer<Void>, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func read(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UInt) -> Int ``` | iOS 8.0 |
| To | ``` func read(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: Int) -> Int ``` | iOS 8.3 |

Modified readlink(UnsafePointer<Int8>, UnsafeMutablePointer<Int8>, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func readlink(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Int8>, _ _: UInt) -> Int ``` | iOS 8.0 |
| To | ``` func readlink(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Int8>, _ _: Int) -> Int ``` | iOS 8.3 |

Modified readlinkat(Int32, UnsafePointer<Int8>, UnsafeMutablePointer<Int8>, Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func readlinkat(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Int8>, _ _: UInt) -> Int ``` |
| To | ``` func readlinkat(_ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Int8>, _ _: Int) -> Int ``` |

Modified realloc(UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func realloc(_ _: UnsafeMutablePointer<Void>, _ _: UInt) -> UnsafeMutablePointer<Void> ``` | iOS 8.0 |
| To | ``` func realloc(_ _: UnsafeMutablePointer<Void>, _ _: Int) -> UnsafeMutablePointer<Void> ``` | iOS 8.3 |

Modified reallocf(UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func reallocf(_ _: UnsafeMutablePointer<Void>, _ _: UInt) -> UnsafeMutablePointer<Void> ``` | iOS 8.0 |
| To | ``` func reallocf(_ _: UnsafeMutablePointer<Void>, _ _: Int) -> UnsafeMutablePointer<Void> ``` | iOS 8.3 |

Modified recv(Int32, UnsafeMutablePointer<Void>, Int, Int32) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func recv(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: Int32) -> Int ``` | iOS 8.0 |
| To | ``` func recv(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32) -> Int ``` | iOS 8.3 |

Modified recvfrom(Int32, UnsafeMutablePointer<Void>, Int, Int32, UnsafeMutablePointer<sockaddr>, UnsafeMutablePointer<socklen_t>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func recvfrom(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: Int32, _ _: UnsafeMutablePointer<sockaddr>, _ _: UnsafeMutablePointer<socklen_t>) -> Int ``` | iOS 8.0 |
| To | ``` func recvfrom(_ _: Int32, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: Int32, _ _: UnsafeMutablePointer<sockaddr>, _ _: UnsafeMutablePointer<socklen_t>) -> Int ``` | iOS 8.3 |

Modified regerror(Int32, UnsafePointer<regex_t>, UnsafeMutablePointer<Int8>, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func regerror(_ _: Int32, _ _: UnsafePointer<regex_t>, _ _: UnsafeMutablePointer<Int8>, _ _: UInt) -> UInt ``` | iOS 8.0 |
| To | ``` func regerror(_ _: Int32, _ _: UnsafePointer<regex_t>, _ _: UnsafeMutablePointer<Int8>, _ _: Int) -> Int ``` | iOS 8.3 |

Modified regexec(UnsafePointer<regex_t>, UnsafePointer<Int8>, Int, UnsafeMutablePointer<regmatch_t>, Int32) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func regexec(_ _: UnsafePointer<regex_t>, _ _: UnsafePointer<Int8>, _ _: UInt, _ __pmatch: UnsafeMutablePointer<regmatch_t>, _ _: Int32) -> Int32 ``` | iOS 8.0 |
| To | ``` func regexec(_ _: UnsafePointer<regex_t>, _ _: UnsafePointer<Int8>, _ _: Int, _ __pmatch: UnsafeMutablePointer<regmatch_t>, _ _: Int32) -> Int32 ``` | iOS 8.3 |

Modified regncomp(UnsafeMutablePointer<regex_t>, UnsafePointer<Int8>, Int, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func regncomp(_ _: UnsafeMutablePointer<regex_t>, _ _: UnsafePointer<Int8>, _ _: UInt, _ _: Int32) -> Int32 ``` |
| To | ``` func regncomp(_ _: UnsafeMutablePointer<regex_t>, _ _: UnsafePointer<Int8>, _ _: Int, _ _: Int32) -> Int32 ``` |

Modified regnexec(UnsafePointer<regex_t>, UnsafePointer<Int8>, Int, Int, UnsafeMutablePointer<regmatch_t>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func regnexec(_ _: UnsafePointer<regex_t>, _ _: UnsafePointer<Int8>, _ _: UInt, _ _: UInt, _ __pmatch: UnsafeMutablePointer<regmatch_t>, _ _: Int32) -> Int32 ``` |
| To | ``` func regnexec(_ _: UnsafePointer<regex_t>, _ _: UnsafePointer<Int8>, _ _: Int, _ _: Int, _ __pmatch: UnsafeMutablePointer<regmatch_t>, _ _: Int32) -> Int32 ``` |

Modified regwexec(UnsafePointer<regex_t>, UnsafePointer<wchar_t>, Int, UnsafeMutablePointer<regmatch_t>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func regwexec(_ _: UnsafePointer<regex_t>, _ _: UnsafePointer<wchar_t>, _ _: UInt, _ __pmatch: UnsafeMutablePointer<regmatch_t>, _ _: Int32) -> Int32 ``` |
| To | ``` func regwexec(_ _: UnsafePointer<regex_t>, _ _: UnsafePointer<wchar_t>, _ _: Int, _ __pmatch: UnsafeMutablePointer<regmatch_t>, _ _: Int32) -> Int32 ``` |

Modified regwncomp(UnsafeMutablePointer<regex_t>, UnsafePointer<wchar_t>, Int, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func regwncomp(_ _: UnsafeMutablePointer<regex_t>, _ _: UnsafePointer<wchar_t>, _ _: UInt, _ _: Int32) -> Int32 ``` |
| To | ``` func regwncomp(_ _: UnsafeMutablePointer<regex_t>, _ _: UnsafePointer<wchar_t>, _ _: Int, _ _: Int32) -> Int32 ``` |

Modified regwnexec(UnsafePointer<regex_t>, UnsafePointer<wchar_t>, Int, Int, UnsafeMutablePointer<regmatch_t>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func regwnexec(_ _: UnsafePointer<regex_t>, _ _: UnsafePointer<wchar_t>, _ _: UInt, _ _: UInt, _ __pmatch: UnsafeMutablePointer<regmatch_t>, _ _: Int32) -> Int32 ``` |
| To | ``` func regwnexec(_ _: UnsafePointer<regex_t>, _ _: UnsafePointer<wchar_t>, _ _: Int, _ _: Int, _ __pmatch: UnsafeMutablePointer<regmatch_t>, _ _: Int32) -> Int32 ``` |

Modified routine_arg_descriptor_t

|  | Declaration |
| --- | --- |
| From | ``` typealias routine_arg_descriptor_t = COpaquePointer ``` |
| To | ``` typealias routine_arg_descriptor_t = UnsafeMutablePointer<mach_msg_type_descriptor_t> ``` |

Modified rsize_t

|  | Declaration |
| --- | --- |
| From | ``` typealias rsize_t = UInt ``` |
| To | ``` typealias rsize_t = Int ``` |

Modified semop(Int32, UnsafeMutablePointer<sembuf>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func semop(_ _: Int32, _ _: UnsafeMutablePointer<sembuf>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func semop(_ _: Int32, _ _: UnsafeMutablePointer<sembuf>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified send(Int32, UnsafePointer<Void>, Int, Int32) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func send(_ _: Int32, _ _: UnsafePointer<Void>, _ _: UInt, _ _: Int32) -> Int ``` | iOS 8.0 |
| To | ``` func send(_ _: Int32, _ _: UnsafePointer<Void>, _ _: Int, _ _: Int32) -> Int ``` | iOS 8.3 |

Modified sendto(Int32, UnsafePointer<Void>, Int, Int32, UnsafePointer<sockaddr>, socklen_t) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sendto(_ _: Int32, _ _: UnsafePointer<Void>, _ _: UInt, _ _: Int32, _ _: UnsafePointer<sockaddr>, _ _: socklen_t) -> Int ``` | iOS 8.0 |
| To | ``` func sendto(_ _: Int32, _ _: UnsafePointer<Void>, _ _: Int, _ _: Int32, _ _: UnsafePointer<sockaddr>, _ _: socklen_t) -> Int ``` | iOS 8.3 |

Modified setattrlist(UnsafePointer<Int8>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int, UInt) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setattrlist(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: UInt, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func setattrlist(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Void>, _ _: Int, _ _: UInt) -> Int32 ``` | iOS 8.3 |

Modified setvbuf(UnsafeMutablePointer<FILE>, UnsafeMutablePointer<Int8>, Int32, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func setvbuf(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<Int8>, _ _: Int32, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func setvbuf(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<Int8>, _ _: Int32, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified shmget(key_t, Int, Int32) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func shmget(_ _: key_t, _ _: UInt, _ _: Int32) -> Int32 ``` | iOS 8.0 |
| To | ``` func shmget(_ _: key_t, _ _: Int, _ _: Int32) -> Int32 ``` | iOS 8.3 |

Modified size_t

|  | Declaration |
| --- | --- |
| From | ``` typealias size_t = UInt ``` |
| To | ``` typealias size_t = Int ``` |

Modified stpncpy(UnsafeMutablePointer<Int8>, UnsafePointer<Int8>, Int) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func stpncpy(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UInt) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func stpncpy(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> UnsafeMutablePointer<Int8> ``` |

Modified strerror_r(Int32, UnsafeMutablePointer<Int8>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func strerror_r(_ _: Int32, _ _: UnsafeMutablePointer<Int8>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func strerror_r(_ _: Int32, _ _: UnsafeMutablePointer<Int8>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified strftime(UnsafeMutablePointer<Int8>, Int, UnsafePointer<Int8>, UnsafePointer<tm>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func strftime(_ _: UnsafeMutablePointer<Int8>, _ _: UInt, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<tm>) -> UInt ``` | iOS 8.0 |
| To | ``` func strftime(_ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<tm>) -> Int ``` | iOS 8.3 |

Modified strlcat(UnsafeMutablePointer<Int8>, UnsafePointer<Int8>, Int) -> UInt

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func strlcat(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UInt) -> UInt ``` | iOS 8.0 |
| To | ``` func strlcat(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> UInt ``` | iOS 8.3 |

Modified strlcpy(UnsafeMutablePointer<Int8>, UnsafePointer<Int8>, Int) -> UInt

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func strlcpy(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UInt) -> UInt ``` | iOS 8.0 |
| To | ``` func strlcpy(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> UInt ``` | iOS 8.3 |

Modified strncasecmp(UnsafePointer<Int8>, UnsafePointer<Int8>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func strncasecmp(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func strncasecmp(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified strncat(UnsafeMutablePointer<Int8>, UnsafePointer<Int8>, Int) -> UnsafeMutablePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func strncat(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UInt) -> UnsafeMutablePointer<Int8> ``` | iOS 8.0 |
| To | ``` func strncat(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> UnsafeMutablePointer<Int8> ``` | iOS 8.3 |

Modified strncmp(UnsafePointer<Int8>, UnsafePointer<Int8>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func strncmp(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func strncmp(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified strncpy(UnsafeMutablePointer<Int8>, UnsafePointer<Int8>, Int) -> UnsafeMutablePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func strncpy(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UInt) -> UnsafeMutablePointer<Int8> ``` | iOS 8.0 |
| To | ``` func strncpy(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> UnsafeMutablePointer<Int8> ``` | iOS 8.3 |

Modified strndup(UnsafePointer<Int8>, Int) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func strndup(_ _: UnsafePointer<Int8>, _ _: UInt) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func strndup(_ _: UnsafePointer<Int8>, _ _: Int) -> UnsafeMutablePointer<Int8> ``` |

Modified strnlen(UnsafePointer<Int8>, Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func strnlen(_ _: UnsafePointer<Int8>, _ _: UInt) -> UInt ``` |
| To | ``` func strnlen(_ _: UnsafePointer<Int8>, _ _: Int) -> Int ``` |

Modified strnstr(UnsafePointer<Int8>, UnsafePointer<Int8>, Int) -> UnsafeMutablePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func strnstr(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UInt) -> UnsafeMutablePointer<Int8> ``` | iOS 8.0 |
| To | ``` func strnstr(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> UnsafeMutablePointer<Int8> ``` | iOS 8.3 |

Modified strxfrm(UnsafeMutablePointer<Int8>, UnsafePointer<Int8>, Int) -> UInt

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func strxfrm(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UInt) -> UInt ``` | iOS 8.0 |
| To | ``` func strxfrm(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int) -> UInt ``` | iOS 8.3 |

Modified sysctl(UnsafeMutablePointer<Int32>, u_int, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Void>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sysctl(_ _: UnsafeMutablePointer<Int32>, _ _: u_int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<UInt>, _ _: UnsafeMutablePointer<Void>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func sysctl(_ _: UnsafeMutablePointer<Int32>, _ _: u_int, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>, _ _: UnsafeMutablePointer<Void>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified sysctlbyname(UnsafePointer<Int8>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<Int>, UnsafeMutablePointer<Void>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sysctlbyname(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<UInt>, _ _: UnsafeMutablePointer<Void>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func sysctlbyname(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Void>, _ _: UnsafeMutablePointer<Int>, _ _: UnsafeMutablePointer<Void>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified sysctlnametomib(UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int>) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func sysctlnametomib(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Int32>, _ _: UnsafeMutablePointer<UInt>) -> Int32 ``` | iOS 8.0 |
| To | ``` func sysctlnametomib(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<Int32>, _ _: UnsafeMutablePointer<Int>) -> Int32 ``` | iOS 8.3 |

Modified ttyname_r(Int32, UnsafeMutablePointer<Int8>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func ttyname_r(_ _: Int32, _ _: UnsafeMutablePointer<Int8>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func ttyname_r(_ _: Int32, _ _: UnsafeMutablePointer<Int8>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified valloc() -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func valloc(_ _: UInt) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func valloc(_ _: Int) -> UnsafeMutablePointer<Void> ``` |

Modified vsnprintf(UnsafeMutablePointer<Int8>, Int, UnsafePointer<Int8>, CVaListPointer) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func vsnprintf(_ _: UnsafeMutablePointer<Int8>, _ _: UInt, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` | iOS 8.0 |
| To | ``` func vsnprintf(_ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` | iOS 8.3 |

Modified vswprintf(UnsafeMutablePointer<wchar_t>, Int, UnsafePointer<wchar_t>, __darwin_va_list) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func vswprintf(_ _: UnsafeMutablePointer<wchar_t>, _ _: UInt, _ _: UnsafePointer<wchar_t>, _ _: __darwin_va_list) -> Int32 ``` | iOS 8.0 |
| To | ``` func vswprintf(_ _: UnsafeMutablePointer<wchar_t>, _ _: Int, _ _: UnsafePointer<wchar_t>, _ _: __darwin_va_list) -> Int32 ``` | iOS 8.3 |

Modified wchar_t

|  | Declaration |
| --- | --- |
| From | ``` typealias wchar_t = UInt32 ``` |
| To | ``` typealias wchar_t = Int32 ``` |

Modified wcpncpy(UnsafeMutablePointer<wchar_t>, UnsafePointer<wchar_t>, Int) -> UnsafeMutablePointer<wchar_t>

|  | Declaration |
| --- | --- |
| From | ``` func wcpncpy(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: UInt) -> UnsafeMutablePointer<wchar_t> ``` |
| To | ``` func wcpncpy(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> UnsafeMutablePointer<wchar_t> ``` |

Modified wcrtomb(UnsafeMutablePointer<Int8>, wchar_t, UnsafeMutablePointer<mbstate_t>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wcrtomb(_ _: UnsafeMutablePointer<Int8>, _ _: wchar_t, _ _: COpaquePointer) -> UInt ``` | iOS 8.0 |
| To | ``` func wcrtomb(_ _: UnsafeMutablePointer<Int8>, _ _: wchar_t, _ _: UnsafeMutablePointer<mbstate_t>) -> Int ``` | iOS 8.3 |

Modified wcscspn(UnsafePointer<wchar_t>, UnsafePointer<wchar_t>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wcscspn(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>) -> UInt ``` | iOS 8.0 |
| To | ``` func wcscspn(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>) -> Int ``` | iOS 8.3 |

Modified wcsftime(UnsafeMutablePointer<wchar_t>, Int, UnsafePointer<wchar_t>, UnsafePointer<tm>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wcsftime(_ _: UnsafeMutablePointer<wchar_t>, _ _: UInt, _ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<tm>) -> UInt ``` | iOS 8.0 |
| To | ``` func wcsftime(_ _: UnsafeMutablePointer<wchar_t>, _ _: Int, _ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<tm>) -> Int ``` | iOS 8.3 |

Modified wcslcat(UnsafeMutablePointer<wchar_t>, UnsafePointer<wchar_t>, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wcslcat(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: UInt) -> UInt ``` | iOS 8.0 |
| To | ``` func wcslcat(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> Int ``` | iOS 8.3 |

Modified wcslcpy(UnsafeMutablePointer<wchar_t>, UnsafePointer<wchar_t>, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wcslcpy(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: UInt) -> UInt ``` | iOS 8.0 |
| To | ``` func wcslcpy(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> Int ``` | iOS 8.3 |

Modified wcslen() -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wcslen(_ _: UnsafePointer<wchar_t>) -> UInt ``` | iOS 8.0 |
| To | ``` func wcslen(_ _: UnsafePointer<wchar_t>) -> Int ``` | iOS 8.3 |

Modified wcsncasecmp(UnsafePointer<wchar_t>, UnsafePointer<wchar_t>, Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func wcsncasecmp(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ n: UInt) -> Int32 ``` |
| To | ``` func wcsncasecmp(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ n: Int) -> Int32 ``` |

Modified wcsncat(UnsafeMutablePointer<wchar_t>, UnsafePointer<wchar_t>, Int) -> UnsafeMutablePointer<wchar_t>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wcsncat(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: UInt) -> UnsafeMutablePointer<wchar_t> ``` | iOS 8.0 |
| To | ``` func wcsncat(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> UnsafeMutablePointer<wchar_t> ``` | iOS 8.3 |

Modified wcsncmp(UnsafePointer<wchar_t>, UnsafePointer<wchar_t>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wcsncmp(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func wcsncmp(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified wcsncpy(UnsafeMutablePointer<wchar_t>, UnsafePointer<wchar_t>, Int) -> UnsafeMutablePointer<wchar_t>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wcsncpy(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: UInt) -> UnsafeMutablePointer<wchar_t> ``` | iOS 8.0 |
| To | ``` func wcsncpy(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> UnsafeMutablePointer<wchar_t> ``` | iOS 8.3 |

Modified wcsnlen(UnsafePointer<wchar_t>, Int) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func wcsnlen(_ _: UnsafePointer<wchar_t>, _ _: UInt) -> UInt ``` |
| To | ``` func wcsnlen(_ _: UnsafePointer<wchar_t>, _ _: Int) -> Int ``` |

Modified wcsnrtombs(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UnsafePointer<wchar_t>>, Int, Int, UnsafeMutablePointer<mbstate_t>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wcsnrtombs(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<UnsafePointer<wchar_t>>, _ _: UInt, _ _: UInt, _ _: COpaquePointer) -> UInt ``` | iOS 8.0 |
| To | ``` func wcsnrtombs(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<UnsafePointer<wchar_t>>, _ _: Int, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>) -> Int ``` | iOS 8.3 |

Modified wcsrtombs(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UnsafePointer<wchar_t>>, Int, UnsafeMutablePointer<mbstate_t>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wcsrtombs(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<UnsafePointer<wchar_t>>, _ _: UInt, _ _: COpaquePointer) -> UInt ``` | iOS 8.0 |
| To | ``` func wcsrtombs(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<UnsafePointer<wchar_t>>, _ _: Int, _ _: UnsafeMutablePointer<mbstate_t>) -> Int ``` | iOS 8.3 |

Modified wcsspn(UnsafePointer<wchar_t>, UnsafePointer<wchar_t>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wcsspn(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>) -> UInt ``` | iOS 8.0 |
| To | ``` func wcsspn(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>) -> Int ``` | iOS 8.3 |

Modified wcstombs(UnsafeMutablePointer<Int8>, UnsafePointer<wchar_t>, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wcstombs(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<wchar_t>, _ _: UInt) -> UInt ``` | iOS 8.0 |
| To | ``` func wcstombs(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> Int ``` | iOS 8.3 |

Modified wcswidth(UnsafePointer<wchar_t>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wcswidth(_ _: UnsafePointer<wchar_t>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func wcswidth(_ _: UnsafePointer<wchar_t>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified wcsxfrm(UnsafeMutablePointer<wchar_t>, UnsafePointer<wchar_t>, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wcsxfrm(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: UInt) -> UInt ``` | iOS 8.0 |
| To | ``` func wcsxfrm(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> Int ``` | iOS 8.3 |

Modified wmemchr(UnsafePointer<wchar_t>, wchar_t, Int) -> UnsafeMutablePointer<wchar_t>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wmemchr(_ _: UnsafePointer<wchar_t>, _ _: wchar_t, _ _: UInt) -> UnsafeMutablePointer<wchar_t> ``` | iOS 8.0 |
| To | ``` func wmemchr(_ _: UnsafePointer<wchar_t>, _ _: wchar_t, _ _: Int) -> UnsafeMutablePointer<wchar_t> ``` | iOS 8.3 |

Modified wmemcmp(UnsafePointer<wchar_t>, UnsafePointer<wchar_t>, Int) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wmemcmp(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: UInt) -> Int32 ``` | iOS 8.0 |
| To | ``` func wmemcmp(_ _: UnsafePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> Int32 ``` | iOS 8.3 |

Modified wmemcpy(UnsafeMutablePointer<wchar_t>, UnsafePointer<wchar_t>, Int) -> UnsafeMutablePointer<wchar_t>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wmemcpy(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: UInt) -> UnsafeMutablePointer<wchar_t> ``` | iOS 8.0 |
| To | ``` func wmemcpy(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> UnsafeMutablePointer<wchar_t> ``` | iOS 8.3 |

Modified wmemmove(UnsafeMutablePointer<wchar_t>, UnsafePointer<wchar_t>, Int) -> UnsafeMutablePointer<wchar_t>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wmemmove(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: UInt) -> UnsafeMutablePointer<wchar_t> ``` | iOS 8.0 |
| To | ``` func wmemmove(_ _: UnsafeMutablePointer<wchar_t>, _ _: UnsafePointer<wchar_t>, _ _: Int) -> UnsafeMutablePointer<wchar_t> ``` | iOS 8.3 |

Modified wmemset(UnsafeMutablePointer<wchar_t>, wchar_t, Int) -> UnsafeMutablePointer<wchar_t>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func wmemset(_ _: UnsafeMutablePointer<wchar_t>, _ _: wchar_t, _ _: UInt) -> UnsafeMutablePointer<wchar_t> ``` | iOS 8.0 |
| To | ``` func wmemset(_ _: UnsafeMutablePointer<wchar_t>, _ _: wchar_t, _ _: Int) -> UnsafeMutablePointer<wchar_t> ``` | iOS 8.3 |

Modified write(Int32, UnsafePointer<Void>, Int) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func write(_ _: Int32, _ _: UnsafePointer<Void>, _ _: UInt) -> Int ``` | iOS 8.0 |
| To | ``` func write(_ _: Int32, _ _: UnsafePointer<Void>, _ _: Int) -> Int ``` | iOS 8.3 |

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
