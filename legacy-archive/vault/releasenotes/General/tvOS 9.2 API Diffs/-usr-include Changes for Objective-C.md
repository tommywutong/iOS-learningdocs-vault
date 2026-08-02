---
title: tvOS 9.2 API Diffs
apple_id: TP40016673
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS92APIDiffs/Objective-C/usr_include.html
archived_at: '2026-07-18T02:58:04.752504Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 9.2 API Diffs](tvOS%209.1%20to%209.2%20API%20Differences.md)


# /usr/include Changes for Objective-C

### /usr/include

#### /usr/include/mach-o/arch.h (Added)

Added NXArchInfoAdded NXCombineCpuSubtypes()Added NXFindBestFatArch()Added NXGetAllArchInfos()Added NXGetArchInfoFromCpuType()Added NXGetArchInfoFromName()Added NXGetLocalArchInfo()

#### /usr/include/mach-o/arm/reloc.h (Added)

Added ARM_RELOC_BR24Added ARM_RELOC_HALFAdded ARM_RELOC_HALF_SECTDIFFAdded ARM_RELOC_LOCAL_SECTDIFFAdded ARM_RELOC_PAIRAdded ARM_RELOC_PB_LA_PTRAdded ARM_RELOC_SECTDIFFAdded ARM_RELOC_VANILLAAdded ARM_THUMB_32BIT_BRANCHAdded ARM_THUMB_RELOC_BR22Added reloc_type_arm

#### /usr/include/mach-o/arm64/reloc.h (Added)

Added ARM64_RELOC_ADDENDAdded ARM64_RELOC_BRANCH26Added ARM64_RELOC_GOT_LOAD_PAGE21Added ARM64_RELOC_GOT_LOAD_PAGEOFF12Added ARM64_RELOC_PAGE21Added ARM64_RELOC_PAGEOFF12Added ARM64_RELOC_POINTER_TO_GOTAdded ARM64_RELOC_SUBTRACTORAdded ARM64_RELOC_TLVP_LOAD_PAGE21Added ARM64_RELOC_TLVP_LOAD_PAGEOFF12Added ARM64_RELOC_UNSIGNEDAdded reloc_type_arm64

#### /usr/include/mach-o/compact_unwind_encoding.h (Added)

Added compact_unwind_encoding_tAdded UNWIND_ARM64_DWARF_SECTION_OFFSETAdded UNWIND_ARM64_FRAME_D10_D11_PAIRAdded UNWIND_ARM64_FRAME_D12_D13_PAIRAdded UNWIND_ARM64_FRAME_D14_D15_PAIRAdded UNWIND_ARM64_FRAME_D8_D9_PAIRAdded UNWIND_ARM64_FRAME_X19_X20_PAIRAdded UNWIND_ARM64_FRAME_X21_X22_PAIRAdded UNWIND_ARM64_FRAME_X23_X24_PAIRAdded UNWIND_ARM64_FRAME_X25_X26_PAIRAdded UNWIND_ARM64_FRAME_X27_X28_PAIRAdded UNWIND_ARM64_FRAMELESS_STACK_SIZE_MASKAdded UNWIND_ARM64_MODE_DWARFAdded UNWIND_ARM64_MODE_FRAMEAdded UNWIND_ARM64_MODE_FRAMELESSAdded UNWIND_ARM64_MODE_MASKAdded UNWIND_HAS_LSDAAdded #def UNWIND_INFO_COMPRESSED_ENTRY_ENCODING_INDEXAdded #def UNWIND_INFO_COMPRESSED_ENTRY_FUNC_OFFSETAdded unwind_info_compressed_second_level_page_headerAdded unwind_info_regular_second_level_entryAdded unwind_info_regular_second_level_page_headerAdded unwind_info_section_headerAdded unwind_info_section_header_index_entryAdded unwind_info_section_header_lsda_index_entryAdded UNWIND_IS_NOT_FUNCTION_STARTAdded UNWIND_PERSONALITY_MASKAdded #def UNWIND_SECOND_LEVEL_COMPRESSEDAdded #def UNWIND_SECOND_LEVEL_REGULARAdded #def UNWIND_SECTION_VERSIONAdded UNWIND_X86_64_DWARF_SECTION_OFFSETAdded UNWIND_X86_64_FRAMELESS_STACK_ADJUSTAdded UNWIND_X86_64_FRAMELESS_STACK_REG_COUNTAdded UNWIND_X86_64_FRAMELESS_STACK_REG_PERMUTATIONAdded UNWIND_X86_64_FRAMELESS_STACK_SIZEAdded UNWIND_X86_64_MODE_DWARFAdded UNWIND_X86_64_MODE_MASKAdded UNWIND_X86_64_MODE_RBP_FRAMEAdded UNWIND_X86_64_MODE_STACK_IMMDAdded UNWIND_X86_64_MODE_STACK_INDAdded UNWIND_X86_64_RBP_FRAME_OFFSETAdded UNWIND_X86_64_RBP_FRAME_REGISTERSAdded UNWIND_X86_64_REG_NONEAdded UNWIND_X86_64_REG_R12Added UNWIND_X86_64_REG_R13Added UNWIND_X86_64_REG_R14Added UNWIND_X86_64_REG_R15Added UNWIND_X86_64_REG_RBPAdded UNWIND_X86_64_REG_RBXAdded UNWIND_X86_DWARF_SECTION_OFFSETAdded UNWIND_X86_EBP_FRAME_OFFSETAdded UNWIND_X86_EBP_FRAME_REGISTERSAdded UNWIND_X86_FRAMELESS_STACK_ADJUSTAdded UNWIND_X86_FRAMELESS_STACK_REG_COUNTAdded UNWIND_X86_FRAMELESS_STACK_REG_PERMUTATIONAdded UNWIND_X86_FRAMELESS_STACK_SIZEAdded UNWIND_X86_MODE_DWARFAdded UNWIND_X86_MODE_EBP_FRAMEAdded UNWIND_X86_MODE_MASKAdded UNWIND_X86_MODE_STACK_IMMDAdded UNWIND_X86_MODE_STACK_INDAdded UNWIND_X86_REG_EBPAdded UNWIND_X86_REG_EBXAdded UNWIND_X86_REG_ECXAdded UNWIND_X86_REG_EDIAdded UNWIND_X86_REG_EDXAdded UNWIND_X86_REG_ESIAdded UNWIND_X86_REG_NONE

#### /usr/include/mach-o/dyld.h (Added)

Added DYLD_BOOLAdded #def ENUM_DYLD_BOOLAdded FALSEAdded #def NSADDIMAGE_OPTION_MATCH_FILENAME_BY_INSTALLNAMEAdded #def NSADDIMAGE_OPTION_NONEAdded #def NSADDIMAGE_OPTION_RETURN_ON_ERRORAdded #def NSADDIMAGE_OPTION_RETURN_ONLY_IF_LOADEDAdded #def NSADDIMAGE_OPTION_WITH_SEARCHINGAdded NSLinkEditErrorHandlersAdded NSLinkEditErrorsAdded NSLinkEditFileAccessErrorAdded NSLinkEditFileFormatErrorAdded NSLinkEditMachResourceErrorAdded NSLinkEditMultiplyDefinedErrorAdded NSLinkEditOtherErrorAdded NSLinkEditUndefinedErrorAdded NSLinkEditUnixResourceErrorAdded NSLinkEditWarningErrorAdded #def NSLINKMODULE_OPTION_BINDNOWAdded #def NSLINKMODULE_OPTION_DONT_CALL_MOD_INIT_ROUTINESAdded #def NSLINKMODULE_OPTION_NONEAdded #def NSLINKMODULE_OPTION_PRIVATEAdded #def NSLINKMODULE_OPTION_RETURN_ON_ERRORAdded #def NSLINKMODULE_OPTION_TRAILING_PHYS_NAMEAdded #def NSLOOKUPSYMBOLINIMAGE_OPTION_BINDAdded #def NSLOOKUPSYMBOLINIMAGE_OPTION_BIND_FULLYAdded #def NSLOOKUPSYMBOLINIMAGE_OPTION_BIND_NOWAdded #def NSLOOKUPSYMBOLINIMAGE_OPTION_RETURN_ON_ERRORAdded NSModuleAdded NSObjectFileImageAdded NSObjectFileImageAccessAdded NSObjectFileImageArchAdded NSObjectFileImageFailureAdded NSObjectFileImageFormatAdded NSObjectFileImageInappropriateFileAdded NSObjectFileImageReturnCodeAdded NSObjectFileImageSuccessAdded NSOtherErrorIndrLoopAdded NSOtherErrorInvalidArgsAdded NSOtherErrorLazyBindAdded NSOtherErrorLazyInitAdded NSOtherErrorNumbersAdded NSOtherErrorRelocationAdded NSSymbolAdded #def NSUNLINKMODULE_OPTION_KEEP_MEMORY_MAPPEDAdded #def NSUNLINKMODULE_OPTION_NONEAdded #def NSUNLINKMODULE_OPTION_RESET_LAZY_REFERENCESAdded NSVersionOfLinkTimeLibrary()Added NSVersionOfRunTimeLibrary()Added TRUE

#### /usr/include/mach-o/dyld_images.h (Added)

Added dyld_all_image_infosAdded dyld_error_kind_dylib_missingAdded dyld_error_kind_dylib_versionAdded dyld_error_kind_dylib_wrong_archAdded dyld_error_kind_noneAdded dyld_error_kind_symbol_missingAdded dyld_image_addingAdded dyld_image_infoAdded dyld_image_info_changeAdded dyld_image_modeAdded dyld_image_notifierAdded dyld_image_removingAdded dyld_shared_cache_rangesAdded dyld_shared_cache_rangesAdded dyld_uuid_info

#### /usr/include/mach-o/fat.h (Added)

Added [fat_arch](https://developer.apple.com/documentation/kernel/fat_arch)Added #def FAT_CIGAMAdded [fat_header](https://developer.apple.com/documentation/kernel/fat_header)Added #def FAT_MAGIC

#### /usr/include/mach-o/getsect.h (Added)

Added get_edata()Added get_end()Added get_etext()Added getsectbyname()Added getsectbynamefromheader()Added getsectbynamefromheader_64()Added getsectbynamefromheaderwithswap()Added getsectbynamefromheaderwithswap_64()Added getsectdata()Added getsectdatafromFramework()Added getsectdatafromheader()Added getsectdatafromheader_64()Added getsectiondata()Added getsegbyname()Added getsegmentdata()

#### /usr/include/mach-o/ldsyms.h (Added)

Added #def MH_BUNDLE_SYMAdded #def MH_DYLIB_SYMAdded #def MH_DYLINKER_SYMAdded #def MH_EXECUTE_SYM

#### /usr/include/mach-o/loader.h (Added)

Added #def BIND_IMMEDIATE_MASKAdded #def BIND_OPCODE_ADD_ADDR_ULEBAdded #def BIND_OPCODE_DO_BINDAdded #def BIND_OPCODE_DO_BIND_ADD_ADDR_IMM_SCALEDAdded #def BIND_OPCODE_DO_BIND_ADD_ADDR_ULEBAdded #def BIND_OPCODE_DO_BIND_ULEB_TIMES_SKIPPING_ULEBAdded #def BIND_OPCODE_DONEAdded #def BIND_OPCODE_MASKAdded #def BIND_OPCODE_SET_ADDEND_SLEBAdded #def BIND_OPCODE_SET_DYLIB_ORDINAL_IMMAdded #def BIND_OPCODE_SET_DYLIB_ORDINAL_ULEBAdded #def BIND_OPCODE_SET_DYLIB_SPECIAL_IMMAdded #def BIND_OPCODE_SET_SEGMENT_AND_OFFSET_ULEBAdded #def BIND_OPCODE_SET_SYMBOL_TRAILING_FLAGS_IMMAdded #def BIND_OPCODE_SET_TYPE_IMMAdded #def BIND_SPECIAL_DYLIB_FLAT_LOOKUPAdded #def BIND_SPECIAL_DYLIB_MAIN_EXECUTABLEAdded #def BIND_SPECIAL_DYLIB_SELFAdded #def BIND_SYMBOL_FLAGS_NON_WEAK_DEFINITIONAdded #def BIND_SYMBOL_FLAGS_WEAK_IMPORTAdded #def BIND_TYPE_POINTERAdded #def BIND_TYPE_TEXT_ABSOLUTE32Added #def BIND_TYPE_TEXT_PCREL32Added [data_in_code_entry](https://developer.apple.com/documentation/kernel/data_in_code_entry)Added #def DICE_KIND_ABS_JUMP_TABLE32Added #def DICE_KIND_DATAAdded #def DICE_KIND_JUMP_TABLE16Added #def DICE_KIND_JUMP_TABLE32Added #def DICE_KIND_JUMP_TABLE8Added [dyld_info_command](https://developer.apple.com/documentation/kernel/dyld_info_command)Added [dylib](https://developer.apple.com/documentation/kernel/dylib)Added [dylib_command](https://developer.apple.com/documentation/kernel/dylib_command)Added [dylib_module](https://developer.apple.com/documentation/kernel/dylib_module)Added [dylib_module_64](https://developer.apple.com/documentation/kernel/dylib_module_64)Added [dylib_reference](https://developer.apple.com/documentation/kernel/dylib_reference)Added [dylib_table_of_contents](https://developer.apple.com/documentation/kernel/dylib_table_of_contents)Added [dylinker_command](https://developer.apple.com/documentation/kernel/dylinker_command)Added [dysymtab_command](https://developer.apple.com/documentation/kernel/dysymtab_command)Added [encryption_info_command](https://developer.apple.com/documentation/kernel/encryption_info_command)Added [encryption_info_command_64](https://developer.apple.com/documentation/kernel/encryption_info_command_64)Added [entry_point_command](https://developer.apple.com/documentation/kernel/entry_point_command)Added #def EXPORT_SYMBOL_FLAGS_KIND_MASKAdded #def EXPORT_SYMBOL_FLAGS_KIND_REGULARAdded #def EXPORT_SYMBOL_FLAGS_KIND_THREAD_LOCALAdded #def EXPORT_SYMBOL_FLAGS_REEXPORTAdded #def EXPORT_SYMBOL_FLAGS_STUB_AND_RESOLVERAdded #def EXPORT_SYMBOL_FLAGS_WEAK_DEFINITIONAdded [fvmfile_command](https://developer.apple.com/documentation/kernel/fvmfile_command)Added [fvmlib](https://developer.apple.com/documentation/kernel/fvmlib)Added [fvmlib_command](https://developer.apple.com/documentation/kernel/fvmlib_command)Added [ident_command](https://developer.apple.com/documentation/kernel/ident_command)Added #def INDIRECT_SYMBOL_ABSAdded #def INDIRECT_SYMBOL_LOCALAdded #def LC_CODE_SIGNATUREAdded #def LC_DATA_IN_CODEAdded #def LC_DYLD_ENVIRONMENTAdded #def LC_DYLD_INFOAdded #def LC_DYLD_INFO_ONLYAdded #def LC_DYLIB_CODE_SIGN_DRSAdded #def LC_DYSYMTABAdded #def LC_ENCRYPTION_INFOAdded #def LC_ENCRYPTION_INFO_64Added #def LC_FUNCTION_STARTSAdded #def LC_FVMFILEAdded #def LC_ID_DYLIBAdded #def LC_ID_DYLINKERAdded #def LC_IDENTAdded #def LC_IDFVMLIBAdded #def LC_LAZY_LOAD_DYLIBAdded #def LC_LINKER_OPTIMIZATION_HINTAdded #def LC_LINKER_OPTIONAdded #def LC_LOAD_DYLIBAdded #def LC_LOAD_DYLINKERAdded #def LC_LOAD_UPWARD_DYLIBAdded #def LC_LOAD_WEAK_DYLIBAdded #def LC_LOADFVMLIBAdded #def LC_MAINAdded #def LC_PREBIND_CKSUMAdded #def LC_PREBOUND_DYLIBAdded #def LC_PREPAGEAdded #def LC_REEXPORT_DYLIBAdded #def LC_REQ_DYLDAdded #def LC_ROUTINESAdded #def LC_ROUTINES_64Added #def LC_RPATHAdded #def LC_SEGMENTAdded #def LC_SEGMENT_64Added #def LC_SEGMENT_SPLIT_INFOAdded #def LC_SOURCE_VERSIONAdded [lc_str](https://developer.apple.com/documentation/kernel/lc_str)Added #def LC_SUB_CLIENTAdded #def LC_SUB_FRAMEWORKAdded #def LC_SUB_LIBRARYAdded #def LC_SUB_UMBRELLAAdded #def LC_SYMSEGAdded #def LC_SYMTABAdded #def LC_THREADAdded #def LC_TWOLEVEL_HINTSAdded #def LC_UNIXTHREADAdded #def LC_UUIDAdded #def LC_VERSION_MIN_IPHONEOSAdded #def LC_VERSION_MIN_MACOSXAdded #def LC_VERSION_MIN_TVOSAdded #def LC_VERSION_MIN_WATCHOSAdded [linkedit_data_command](https://developer.apple.com/documentation/kernel/linkedit_data_command)Added [linker_option_command](https://developer.apple.com/documentation/kernel/linker_option_command)Added [load_command](https://developer.apple.com/documentation/kernel/load_command)Added [mach_header](https://developer.apple.com/documentation/kernel/mach_header)Added [mach_header_64](https://developer.apple.com/documentation/kernel/mach_header_64)Added #def MH_ALLMODSBOUNDAdded #def MH_ALLOW_STACK_EXECUTIONAdded #def MH_APP_EXTENSION_SAFEAdded #def MH_BINDATLOADAdded #def MH_BINDS_TO_WEAKAdded #def MH_BUNDLEAdded #def MH_CANONICALAdded #def MH_CIGAMAdded #def MH_CIGAM_64Added #def MH_COREAdded #def MH_DEAD_STRIPPABLE_DYLIBAdded #def MH_DSYMAdded #def MH_DYLDLINKAdded #def MH_DYLIBAdded #def MH_DYLIB_STUBAdded #def MH_DYLINKERAdded #def MH_EXECUTEAdded #def MH_FORCE_FLATAdded #def MH_FVMLIBAdded #def MH_HAS_TLV_DESCRIPTORSAdded #def MH_INCRLINKAdded #def MH_KEXT_BUNDLEAdded #def MH_LAZY_INITAdded #def MH_MAGICAdded #def MH_MAGIC_64Added #def MH_NO_HEAP_EXECUTIONAdded #def MH_NO_REEXPORTED_DYLIBSAdded #def MH_NOFIXPREBINDINGAdded #def MH_NOMULTIDEFSAdded #def MH_NOUNDEFSAdded #def MH_OBJECTAdded #def MH_PIEAdded #def MH_PREBINDABLEAdded #def MH_PREBOUNDAdded #def MH_PRELOADAdded #def MH_ROOT_SAFEAdded #def MH_SETUID_SAFEAdded #def MH_SPLIT_SEGSAdded #def MH_SUBSECTIONS_VIA_SYMBOLSAdded #def MH_TWOLEVELAdded #def MH_WEAK_DEFINESAdded [prebind_cksum_command](https://developer.apple.com/documentation/kernel/prebind_cksum_command)Added [prebound_dylib_command](https://developer.apple.com/documentation/kernel/prebound_dylib_command)Added #def REBASE_IMMEDIATE_MASKAdded #def REBASE_OPCODE_ADD_ADDR_IMM_SCALEDAdded #def REBASE_OPCODE_ADD_ADDR_ULEBAdded #def REBASE_OPCODE_DO_REBASE_ADD_ADDR_ULEBAdded #def REBASE_OPCODE_DO_REBASE_IMM_TIMESAdded #def REBASE_OPCODE_DO_REBASE_ULEB_TIMESAdded #def REBASE_OPCODE_DO_REBASE_ULEB_TIMES_SKIPPING_ULEBAdded #def REBASE_OPCODE_DONEAdded #def REBASE_OPCODE_MASKAdded #def REBASE_OPCODE_SET_SEGMENT_AND_OFFSET_ULEBAdded #def REBASE_OPCODE_SET_TYPE_IMMAdded #def REBASE_TYPE_POINTERAdded #def REBASE_TYPE_TEXT_ABSOLUTE32Added #def REBASE_TYPE_TEXT_PCREL32Added [routines_command](https://developer.apple.com/documentation/kernel/routines_command)Added [routines_command_64](https://developer.apple.com/documentation/kernel/routines_command_64)Added [rpath_command](https://developer.apple.com/documentation/kernel/rpath_command)Added #def S_16BYTE_LITERALSAdded #def S_4BYTE_LITERALSAdded #def S_8BYTE_LITERALSAdded #def S_ATTR_DEBUGAdded #def S_ATTR_EXT_RELOCAdded #def S_ATTR_LIVE_SUPPORTAdded #def S_ATTR_LOC_RELOCAdded #def S_ATTR_NO_DEAD_STRIPAdded #def S_ATTR_NO_TOCAdded #def S_ATTR_PURE_INSTRUCTIONSAdded #def S_ATTR_SELF_MODIFYING_CODEAdded #def S_ATTR_SOME_INSTRUCTIONSAdded #def S_ATTR_STRIP_STATIC_SYMSAdded #def S_COALESCEDAdded #def S_CSTRING_LITERALSAdded #def S_DTRACE_DOFAdded #def S_GB_ZEROFILLAdded #def S_INTERPOSINGAdded #def S_LAZY_DYLIB_SYMBOL_POINTERSAdded #def S_LAZY_SYMBOL_POINTERSAdded #def S_LITERAL_POINTERSAdded #def S_MOD_INIT_FUNC_POINTERSAdded #def S_MOD_TERM_FUNC_POINTERSAdded #def S_NON_LAZY_SYMBOL_POINTERSAdded #def S_REGULARAdded #def S_SYMBOL_STUBSAdded #def S_THREAD_LOCAL_INIT_FUNCTION_POINTERSAdded #def S_THREAD_LOCAL_REGULARAdded #def S_THREAD_LOCAL_VARIABLE_POINTERSAdded #def S_THREAD_LOCAL_VARIABLESAdded #def S_THREAD_LOCAL_ZEROFILLAdded #def S_ZEROFILLAdded #def SECT_BSSAdded #def SECT_COMMONAdded #def SECT_DATAAdded #def SECT_FVMLIB_INIT0Added #def SECT_FVMLIB_INIT1Added #def SECT_ICON_HEADERAdded #def SECT_ICON_TIFFAdded #def SECT_OBJC_MODULESAdded #def SECT_OBJC_REFSAdded #def SECT_OBJC_STRINGSAdded #def SECT_OBJC_SYMBOLSAdded #def SECT_TEXTAdded [section](https://developer.apple.com/documentation/kernel/section)Added [section_64](https://developer.apple.com/documentation/kernel/section_64)Added #def SECTION_ATTRIBUTESAdded #def SECTION_ATTRIBUTES_SYSAdded #def SECTION_ATTRIBUTES_USRAdded #def SECTION_TYPEAdded #def SEG_DATAAdded #def SEG_ICONAdded #def SEG_IMPORTAdded #def SEG_LINKEDITAdded #def SEG_OBJCAdded #def SEG_PAGEZEROAdded #def SEG_TEXTAdded #def SEG_UNIXSTACKAdded [segment_command](https://developer.apple.com/documentation/kernel/segment_command)Added [segment_command_64](https://developer.apple.com/documentation/kernel/segment_command_64)Added #def SG_FVMLIBAdded #def SG_HIGHVMAdded #def SG_NORELOCAdded #def SG_PROTECTED_VERSION_1Added [source_version_command](https://developer.apple.com/documentation/kernel/source_version_command)Added [sub_client_command](https://developer.apple.com/documentation/kernel/sub_client_command)Added [sub_framework_command](https://developer.apple.com/documentation/kernel/sub_framework_command)Added [sub_library_command](https://developer.apple.com/documentation/kernel/sub_library_command)Added [sub_umbrella_command](https://developer.apple.com/documentation/kernel/sub_umbrella_command)Added [symseg_command](https://developer.apple.com/documentation/kernel/symseg_command)Added [symtab_command](https://developer.apple.com/documentation/kernel/symtab_command)Added [thread_command](https://developer.apple.com/documentation/kernel/thread_command)Added [tlv_descriptor](https://developer.apple.com/documentation/kernel/tlv_descriptor)Added [twolevel_hint](https://developer.apple.com/documentation/kernel/twolevel_hint)Added [twolevel_hints_command](https://developer.apple.com/documentation/kernel/twolevel_hints_command)Added [uuid_command](https://developer.apple.com/documentation/kernel/uuid_command)Added [version_min_command](https://developer.apple.com/documentation/kernel/version_min_command)

#### /usr/include/mach-o/nlist.h (Added)

Added #def DYNAMIC_LOOKUP_ORDINALAdded #def EXECUTABLE_ORDINALAdded #def GET_COMM_ALIGNAdded #def GET_LIBRARY_ORDINALAdded #def MAX_LIBRARY_ORDINALAdded #def MAX_SECTAdded #def N_ABSAdded #def N_ALT_ENTRYAdded #def N_ARM_THUMB_DEFAdded #def N_DESC_DISCARDEDAdded #def N_EXTAdded #def N_INDRAdded #def N_NO_DEAD_STRIPAdded #def N_PBUDAdded #def N_PEXTAdded #def N_REF_TO_WEAKAdded #def N_SECTAdded #def N_STABAdded #def N_SYMBOL_RESOLVERAdded #def N_TYPEAdded #def N_UNDFAdded #def N_WEAK_DEFAdded #def N_WEAK_REFAdded [nlist()](https://developer.apple.com/documentation/kernel/1583963-nlist)Added [nlist](https://developer.apple.com/documentation/kernel/nlist)Added [nlist_64](https://developer.apple.com/documentation/kernel/nlist_64)Added #def NO_SECTAdded #def REFERENCE_FLAG_DEFINEDAdded #def REFERENCE_FLAG_PRIVATE_DEFINEDAdded #def REFERENCE_FLAG_PRIVATE_UNDEFINED_LAZYAdded #def REFERENCE_FLAG_PRIVATE_UNDEFINED_NON_LAZYAdded #def REFERENCE_FLAG_UNDEFINED_LAZYAdded #def REFERENCE_FLAG_UNDEFINED_NON_LAZYAdded #def REFERENCE_TYPEAdded #def REFERENCED_DYNAMICALLYAdded #def SELF_LIBRARY_ORDINALAdded #def SET_COMM_ALIGNAdded #def SET_LIBRARY_ORDINAL

#### /usr/include/mach-o/ranlib.h (Added)

Added ranlibAdded #def SYMDEFAdded #def SYMDEF_SORTED

#### /usr/include/mach-o/reloc.h (Added)

Added [GENERIC_RELOC_LOCAL_SECTDIFF](https://developer.apple.com/documentation/kernel/reloc_type_generic/generic_reloc_local_sectdiff)Added [GENERIC_RELOC_PAIR](https://developer.apple.com/documentation/kernel/reloc_type_generic/generic_reloc_pair)Added [GENERIC_RELOC_PB_LA_PTR](https://developer.apple.com/documentation/kernel/reloc_type_generic/generic_reloc_pb_la_ptr)Added [GENERIC_RELOC_SECTDIFF](https://developer.apple.com/documentation/kernel/reloc_type_generic/generic_reloc_sectdiff)Added [GENERIC_RELOC_TLV](https://developer.apple.com/documentation/kernel/reloc_type_generic/generic_reloc_tlv)Added [GENERIC_RELOC_VANILLA](https://developer.apple.com/documentation/kernel/reloc_type_generic/generic_reloc_vanilla)Added #def R_ABSAdded #def R_SCATTEREDAdded [reloc_type_generic](https://developer.apple.com/documentation/kernel/reloc_type_generic)Added [relocation_info](https://developer.apple.com/documentation/kernel/relocation_info)Added [scattered_relocation_info](https://developer.apple.com/documentation/kernel/scattered_relocation_info)

#### /usr/include/mach-o/stab.h (Added)

Added #def N_ASTAdded #def N_BCOMMAdded #def N_BINCLAdded #def N_BNSYMAdded #def N_ECOMLAdded #def N_ECOMMAdded #def N_EINCLAdded #def N_ENSYMAdded #def N_ENTRYAdded #def N_EXCLAdded #def N_FNAMEAdded #def N_FUNAdded #def N_GSYMAdded #def N_LBRACAdded #def N_LCSYMAdded #def N_LENGAdded #def N_LSYMAdded #def N_OLEVELAdded #def N_OPTAdded #def N_OSOAdded #def N_PARAMSAdded #def N_PCAdded #def N_PSYMAdded #def N_RBRACAdded #def N_RSYMAdded #def N_SLINEAdded #def N_SOAdded #def N_SOLAdded #def N_SSYMAdded #def N_STSYMAdded #def N_VERSION

#### /usr/include/mach-o/swap.h (Added)

Added swap_dyld_info_command()Added swap_dylib_command()Added swap_dylib_module()Added swap_dylib_module_64()Added swap_dylib_reference()Added swap_dylib_table_of_contents()Added swap_dylinker_command()Added swap_dysymtab_command()Added swap_encryption_command()Added swap_encryption_command_64()Added swap_entry_point_command()Added swap_fat_arch()Added swap_fat_header()Added swap_fvmfile_command()Added swap_fvmlib_command()Added swap_ident_command()Added swap_indirect_symbols()Added swap_linkedit_data_command()Added swap_linker_option_command()Added swap_load_command()Added swap_mach_header()Added swap_mach_header_64()Added swap_nlist()Added swap_nlist_64()Added swap_prebind_cksum_command()Added swap_prebound_dylib_command()Added swap_ranlib()Added swap_relocation_info()Added swap_routines_command()Added swap_routines_command_64()Added swap_rpath_command()Added swap_section()Added swap_section_64()Added swap_segment_command()Added swap_segment_command_64()Added swap_source_version_command()Added swap_sub_client_command()Added swap_sub_framework_command()Added swap_sub_library_command()Added swap_sub_umbrella_command()Added swap_symseg_command()Added swap_symtab_command()Added swap_thread_command()Added swap_twolevel_hint()Added swap_twolevel_hints_command()Added swap_uuid_command()Added swap_version_min_command()

#### /usr/include/objc/runtime.h

Modified [objc_getClass()](https://developer.apple.com/documentation/objectivec/1418952-objc_getclass)

|  | Declaration |
| --- | --- |
| From | ``` Class objc_getClass (     const char *name ); ``` |
| To | ``` id objc_getClass (     const char *name ); ``` |

Modified [objc_getMetaClass()](https://developer.apple.com/documentation/objectivec/1418721-objc_getmetaclass)

|  | Declaration |
| --- | --- |
| From | ``` Class objc_getMetaClass (     const char *name ); ``` |
| To | ``` id objc_getMetaClass (     const char *name ); ``` |

#### /usr/include/os/activity.h (Added)

Added [os_activity_end()](https://developer.apple.com/documentation/os/1478194-os_activity_end)Added [OS_ACTIVITY_FLAG_DEFAULT](https://developer.apple.com/documentation/os/os_activity_flag_t/os_activity_flag_default)Added [OS_ACTIVITY_FLAG_DETACHED](https://developer.apple.com/documentation/os/os_activity_flag_t/os_activity_flag_detached)Added [os_activity_flag_t](https://developer.apple.com/documentation/os/os_activity_flag_t)Added [os_activity_get_active()](https://developer.apple.com/documentation/os/1478192-os_activity_get_active)Added #def os_activity_initiateAdded #def os_activity_initiate_fAdded #def OS_ACTIVITY_NULLAdded [#def os_activity_set_breadcrumb](https://developer.apple.com/documentation/os/os_activity_set_breadcrumb)Added #def os_activity_startAdded [os_activity_t](https://developer.apple.com/documentation/os/os_activity_t)Added [os_breadcrumb_t](https://developer.apple.com/documentation/os/os_breadcrumb_t)

#### /usr/include/os/base.h (Added)

Added #def OS_ALIGNEDAdded #def OS_ALWAYS_INLINEAdded #def OS_CONCATAdded #def OS_CONSTAdded #def OS_ENUMAdded #def OS_EXPECTAdded #def OS_EXPORTAdded #def OS_FORMAT_PRINTFAdded #def OS_INLINEAdded #def OS_MALLOCAdded #def OS_NOINLINEAdded #def OS_NONNULL1Added #def OS_NONNULL10Added #def OS_NONNULL11Added #def OS_NONNULL12Added #def OS_NONNULL13Added #def OS_NONNULL14Added #def OS_NONNULL15Added #def OS_NONNULL2Added #def OS_NONNULL3Added #def OS_NONNULL4Added #def OS_NONNULL5Added #def OS_NONNULL6Added #def OS_NONNULL7Added #def OS_NONNULL8Added #def OS_NONNULL9Added #def OS_NONNULL_ALLAdded #def OS_NORETURNAdded #def OS_NOTHROWAdded #def OS_OVERLOADABLEAdded #def OS_PUREAdded #def OS_SENTINELAdded #def OS_STRINGIFYAdded #def OS_TRANSPARENT_UNIONAdded #def OS_UNUSEDAdded #def OS_USEDAdded #def OS_WARN_RESULTAdded #def OS_WEAKAdded #def OS_WEAK_IMPORT

#### /usr/include/os/object.h (Added)

Added #def OS_OBJECT_BRIDGEAdded #def OS_OBJECT_CLASSAdded #def OS_OBJECT_CONSUMEDAdded #def OS_OBJECT_DECLAdded #def OS_OBJECT_DECL_IMPLAdded #def OS_OBJECT_DECL_SUBCLASSAdded #def OS_OBJECT_GLOBAL_OBJECTAdded #def OS_OBJECT_HAVE_OBJC_SUPPORTAdded #def OS_OBJECT_RETURNS_RETAINEDAdded #def OS_OBJECT_USE_OBJCAdded #def OS_OBJECT_USE_OBJC_RETAIN_RELEASEAdded [os_release()](https://developer.apple.com/documentation/kernel/1646596-os_release)Added #def os_releaseAdded [os_retain()](https://developer.apple.com/documentation/os/1524246-os_retain)Added #def os_retainAdded #def OS_WARN_RESULT_NEEDS_RELEASE

#### /usr/include/os/trace.h (Added)

Added #def OS_COUNT_ARGSAdded #def OS_COUNT_ARGS1Added #def os_traceAdded #def os_trace_debugAdded [os_trace_debug_enabled()](https://developer.apple.com/documentation/os/1588724-os_trace_debug_enabled)Added #def os_trace_errorAdded #def os_trace_faultAdded [os_trace_payload_t](https://developer.apple.com/documentation/os/os_trace_payload_t)Added [#def OS_TRACE_TYPE_DEBUG](https://developer.apple.com/documentation/os/os_trace_type_debug)Added #def OS_TRACE_TYPE_ERRORAdded #def OS_TRACE_TYPE_FAULTAdded [#def OS_TRACE_TYPE_RELEASE](https://developer.apple.com/documentation/os/os_trace_type_release)Added [xpc_object_t](https://developer.apple.com/documentation/xpc/xpc_object_t)

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
