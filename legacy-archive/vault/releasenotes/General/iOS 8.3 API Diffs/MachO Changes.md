---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/MachO.html
archived_at: '2026-07-18T02:56:26.520992Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# MachO Changes

## MachO

Added NSLinkEditErrorHandlers.init()Added NSLinkEditErrorHandlers.init(undefined: CFunctionPointer<((UnsafePointer<Int8>) -> Void)>, multiple: CFunctionPointer<((NSSymbol, NSModule, NSModule) -> NSModule)>, linkEdit: CFunctionPointer<((NSLinkEditErrors, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Void)>)Added NXArchInfo.init()Added NXArchInfo.init(name: UnsafePointer<Int8>, cputype: cpu_type_t, cpusubtype: cpu_subtype_t, byteorder: NXByteOrder, description: UnsafePointer<Int8>)Added data_in_code_entry.init()Added data_in_code_entry.init(offset: UInt32, length: UInt16, kind: UInt16)Added dyld_all_image_infos.init()Added dyld_all_image_infos.init(version: UInt32, infoArrayCount: UInt32, infoArray: UnsafePointer<dyld_image_info>, notification: dyld_image_notifier, processDetachedFromSharedRegion: Bool, libSystemInitialized: Bool, dyldImageLoadAddress: UnsafePointer<mach_header>, jitInfo: UnsafeMutablePointer<Void>, dyldVersion: UnsafePointer<Int8>, errorMessage: UnsafePointer<Int8>, terminationFlags: UInt, coreSymbolicationShmPage: UnsafeMutablePointer<Void>, systemOrderFlag: UInt, uuidArrayCount: UInt, uuidArray: UnsafePointer<dyld_uuid_info>, dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos>, initialImageCount: UInt, errorKind: UInt, errorClientOfDylibPath: UnsafePointer<Int8>, errorTargetDylibPath: UnsafePointer<Int8>, errorSymbol: UnsafePointer<Int8>, sharedCacheSlide: UInt, sharedCacheUUID:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), reserved:(UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt))Added dyld_image_info.init()Added dyld_image_info.init(imageLoadAddress: UnsafePointer<mach_header>, imageFilePath: UnsafePointer<Int8>, imageFileModDate: UInt)Added dyld_info_command.init()Added dyld_info_command.init(cmd: UInt32, cmdsize: UInt32, rebase_off: UInt32, rebase_size: UInt32, bind_off: UInt32, bind_size: UInt32, weak_bind_off: UInt32, weak_bind_size: UInt32, lazy_bind_off: UInt32, lazy_bind_size: UInt32, export_off: UInt32, export_size: UInt32)Added dyld_shared_cache_ranges.init()Added dyld_uuid_info.init()Added dyld_uuid_info.init(imageLoadAddress: UnsafePointer<mach_header>, imageUUID: uuid_t)Added dylib.init()Added dylib.nameAdded dylib.init(name: lc_str, timestamp: UInt32, current_version: UInt32, compatibility_version: UInt32)Added dylib_command.init()Added dylib_command.init(cmd: UInt32, cmdsize: UInt32, dylib: dylib)Added dylib_module.init()Added dylib_module.init(module_name: UInt32, iextdefsym: UInt32, nextdefsym: UInt32, irefsym: UInt32, nrefsym: UInt32, ilocalsym: UInt32, nlocalsym: UInt32, iextrel: UInt32, nextrel: UInt32, iinit_iterm: UInt32, ninit_nterm: UInt32, objc_module_info_addr: UInt32, objc_module_info_size: UInt32)Added dylib_module_64.init()Added dylib_module_64.init(module_name: UInt32, iextdefsym: UInt32, nextdefsym: UInt32, irefsym: UInt32, nrefsym: UInt32, ilocalsym: UInt32, nlocalsym: UInt32, iextrel: UInt32, nextrel: UInt32, iinit_iterm: UInt32, ninit_nterm: UInt32, objc_module_info_size: UInt32, objc_module_info_addr: UInt64)Added dylib_reference [struct]Added dylib_reference.init()Added dylib_table_of_contents.init()Added dylib_table_of_contents.init(symbol_index: UInt32, module_index: UInt32)Added dylinker_command.init()Added dylinker_command.init(cmd: UInt32, cmdsize: UInt32, name: lc_str)Added dylinker_command.nameAdded dysymtab_command.init()Added dysymtab_command.init(cmd: UInt32, cmdsize: UInt32, ilocalsym: UInt32, nlocalsym: UInt32, iextdefsym: UInt32, nextdefsym: UInt32, iundefsym: UInt32, nundefsym: UInt32, tocoff: UInt32, ntoc: UInt32, modtaboff: UInt32, nmodtab: UInt32, extrefsymoff: UInt32, nextrefsyms: UInt32, indirectsymoff: UInt32, nindirectsyms: UInt32, extreloff: UInt32, nextrel: UInt32, locreloff: UInt32, nlocrel: UInt32)Added encryption_info_command.init()Added encryption_info_command.init(cmd: UInt32, cmdsize: UInt32, cryptoff: UInt32, cryptsize: UInt32, cryptid: UInt32)Added encryption_info_command_64.init()Added encryption_info_command_64.init(cmd: UInt32, cmdsize: UInt32, cryptoff: UInt32, cryptsize: UInt32, cryptid: UInt32, pad: UInt32)Added entry_point_command.init()Added entry_point_command.init(cmd: UInt32, cmdsize: UInt32, entryoff: UInt64, stacksize: UInt64)Added fat_arch.init()Added fat_arch.init(cputype: cpu_type_t, cpusubtype: cpu_subtype_t, offset: UInt32, size: UInt32, align: UInt32)Added fat_header.init()Added fat_header.init(magic: UInt32, nfat_arch: UInt32)Added fvmfile_command.init()Added fvmfile_command.init(cmd: UInt32, cmdsize: UInt32, name: lc_str, header_addr: UInt32)Added fvmfile_command.nameAdded fvmlib.init()Added fvmlib.nameAdded fvmlib.init(name: lc_str, minor_version: UInt32, header_addr: UInt32)Added fvmlib_command.init()Added fvmlib_command.init(cmd: UInt32, cmdsize: UInt32, fvmlib: fvmlib)Added ident_command.init()Added ident_command.init(cmd: UInt32, cmdsize: UInt32)Added lc_str [struct]Added lc_str.init()Added linkedit_data_command.init()Added linkedit_data_command.init(cmd: UInt32, cmdsize: UInt32, dataoff: UInt32, datasize: UInt32)Added linker_option_command.init()Added linker_option_command.init(cmd: UInt32, cmdsize: UInt32, count: UInt32)Added load_command.init()Added load_command.init(cmd: UInt32, cmdsize: UInt32)Added mach_header.init()Added mach_header.init(magic: UInt32, cputype: cpu_type_t, cpusubtype: cpu_subtype_t, filetype: UInt32, ncmds: UInt32, sizeofcmds: UInt32, flags: UInt32)Added mach_header_64.init()Added mach_header_64.init(magic: UInt32, cputype: cpu_type_t, cpusubtype: cpu_subtype_t, filetype: UInt32, ncmds: UInt32, sizeofcmds: UInt32, flags: UInt32, reserved: UInt32)Added nlist.init()Added nlist_64.init()Added prebind_cksum_command.init()Added prebind_cksum_command.init(cmd: UInt32, cmdsize: UInt32, cksum: UInt32)Added prebound_dylib_command.init()Added prebound_dylib_command.init(cmd: UInt32, cmdsize: UInt32, name: lc_str, nmodules: UInt32, linked_modules: lc_str)Added prebound_dylib_command.linked_modulesAdded prebound_dylib_command.nameAdded ranlib.init()Added relocation_info [struct]Added relocation_info.init()Added relocation_info.r_addressAdded routines_command.init()Added routines_command.init(cmd: UInt32, cmdsize: UInt32, init_address: UInt32, init_module: UInt32, reserved1: UInt32, reserved2: UInt32, reserved3: UInt32, reserved4: UInt32, reserved5: UInt32, reserved6: UInt32)Added routines_command_64.init()Added routines_command_64.init(cmd: UInt32, cmdsize: UInt32, init_address: UInt64, init_module: UInt64, reserved1: UInt64, reserved2: UInt64, reserved3: UInt64, reserved4: UInt64, reserved5: UInt64, reserved6: UInt64)Added rpath_command.init()Added rpath_command.init(cmd: UInt32, cmdsize: UInt32, path: lc_str)Added rpath_command.pathAdded scattered_relocation_info [struct]Added scattered_relocation_info.init()Added scattered_relocation_info.r_valueAdded section.init()Added section.init(sectname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), segname:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), addr: UInt32, size: UInt32, offset: UInt32, align: UInt32, reloff: UInt32, nreloc: UInt32, flags: UInt32, reserved1: UInt32, reserved2: UInt32)Added section_64.init()Added section_64.init(sectname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), segname:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), addr: UInt64, size: UInt64, offset: UInt32, align: UInt32, reloff: UInt32, nreloc: UInt32, flags: UInt32, reserved1: UInt32, reserved2: UInt32, reserved3: UInt32)Added segment_command.init()Added segment_command.init(cmd: UInt32, cmdsize: UInt32, segname:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), vmaddr: UInt32, vmsize: UInt32, fileoff: UInt32, filesize: UInt32, maxprot: vm_prot_t, initprot: vm_prot_t, nsects: UInt32, flags: UInt32)Added segment_command_64.init()Added segment_command_64.init(cmd: UInt32, cmdsize: UInt32, segname:(Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), vmaddr: UInt64, vmsize: UInt64, fileoff: UInt64, filesize: UInt64, maxprot: vm_prot_t, initprot: vm_prot_t, nsects: UInt32, flags: UInt32)Added source_version_command.init()Added source_version_command.init(cmd: UInt32, cmdsize: UInt32, version: UInt64)Added sub_client_command.init()Added sub_client_command.clientAdded sub_client_command.init(cmd: UInt32, cmdsize: UInt32, client: lc_str)Added sub_framework_command.init()Added sub_framework_command.init(cmd: UInt32, cmdsize: UInt32, umbrella: lc_str)Added sub_framework_command.umbrellaAdded sub_library_command.init()Added sub_library_command.init(cmd: UInt32, cmdsize: UInt32, sub_library: lc_str)Added sub_library_command.sub_libraryAdded sub_umbrella_command.init()Added sub_umbrella_command.init(cmd: UInt32, cmdsize: UInt32, sub_umbrella: lc_str)Added sub_umbrella_command.sub_umbrellaAdded symseg_command.init()Added symseg_command.init(cmd: UInt32, cmdsize: UInt32, offset: UInt32, size: UInt32)Added symtab_command.init()Added symtab_command.init(cmd: UInt32, cmdsize: UInt32, symoff: UInt32, nsyms: UInt32, stroff: UInt32, strsize: UInt32)Added thread_command.init()Added thread_command.init(cmd: UInt32, cmdsize: UInt32)Added tlv_descriptor.init()Added tlv_descriptor.init(thunk: CFunctionPointer<((UnsafeMutablePointer<tlv_descriptor>) -> UnsafeMutablePointer<Void>)>, key: UInt, offset: UInt)Added twolevel_hint [struct]Added twolevel_hint.init()Added twolevel_hints_command.init()Added twolevel_hints_command.init(cmd: UInt32, cmdsize: UInt32, offset: UInt32, nhints: UInt32)Added unwind_info_compressed_second_level_page_header.init()Added unwind_info_compressed_second_level_page_header.init(kind: UInt32, entryPageOffset: UInt16, entryCount: UInt16, encodingsPageOffset: UInt16, encodingsCount: UInt16)Added unwind_info_regular_second_level_entry.init()Added unwind_info_regular_second_level_entry.init(functionOffset: UInt32, encoding: compact_unwind_encoding_t)Added unwind_info_regular_second_level_page_header.init()Added unwind_info_regular_second_level_page_header.init(kind: UInt32, entryPageOffset: UInt16, entryCount: UInt16)Added unwind_info_section_header.init()Added unwind_info_section_header.init(version: UInt32, commonEncodingsArraySectionOffset: UInt32, commonEncodingsArrayCount: UInt32, personalityArraySectionOffset: UInt32, personalityArrayCount: UInt32, indexSectionOffset: UInt32, indexCount: UInt32)Added unwind_info_section_header_index_entry.init()Added unwind_info_section_header_index_entry.init(functionOffset: UInt32, secondLevelPagesSectionOffset: UInt32, lsdaIndexArraySectionOffset: UInt32)Added unwind_info_section_header_lsda_index_entry.init()Added unwind_info_section_header_lsda_index_entry.init(functionOffset: UInt32, lsdaOffset: UInt32)Added uuid_command.init()Added uuid_command.init(cmd: UInt32, cmdsize: UInt32, uuid:(UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added version_min_command.init()Added version_min_command.init(cmd: UInt32, cmdsize: UInt32, version: UInt32, sdk: UInt32)Modified NSLinkEditErrorHandlers [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSLinkEditErrorHandlers {     var undefined: CFunctionPointer<((UnsafePointer<Int8>) -> Void)>     var multiple: CFunctionPointer<((NSSymbol, NSModule, NSModule) -> NSModule)>     var linkEdit: CFunctionPointer<((NSLinkEditErrors, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Void)> } ``` |
| To | ``` struct NSLinkEditErrorHandlers {     var undefined: CFunctionPointer<((UnsafePointer<Int8>) -> Void)>     var multiple: CFunctionPointer<((NSSymbol, NSModule, NSModule) -> NSModule)>     var linkEdit: CFunctionPointer<((NSLinkEditErrors, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Void)>     init()     init(undefined undefined: CFunctionPointer<((UnsafePointer<Int8>) -> Void)>, multiple multiple: CFunctionPointer<((NSSymbol, NSModule, NSModule) -> NSModule)>, linkEdit linkEdit: CFunctionPointer<((NSLinkEditErrors, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Void)>) } ``` |

Modified NXArchInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NXArchInfo {     var name: UnsafePointer<Int8>     var cputype: cpu_type_t     var cpusubtype: cpu_subtype_t     var byteorder: NXByteOrder     var description: UnsafePointer<Int8> } ``` |
| To | ``` struct NXArchInfo {     var name: UnsafePointer<Int8>     var cputype: cpu_type_t     var cpusubtype: cpu_subtype_t     var byteorder: NXByteOrder     var description: UnsafePointer<Int8>     init()     init(name name: UnsafePointer<Int8>, cputype cputype: cpu_type_t, cpusubtype cpusubtype: cpu_subtype_t, byteorder byteorder: NXByteOrder, description description: UnsafePointer<Int8>) } ``` |

Modified data_in_code_entry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct data_in_code_entry {     var offset: UInt32     var length: UInt16     var kind: UInt16 } ``` |
| To | ``` struct data_in_code_entry {     var offset: UInt32     var length: UInt16     var kind: UInt16     init()     init(offset offset: UInt32, length length: UInt16, kind kind: UInt16) } ``` |

Modified dyld_all_image_infos [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dyld_all_image_infos {     var version: UInt32     var infoArrayCount: UInt32     var infoArray: UnsafePointer<dyld_image_info>     var notification: dyld_image_notifier     var processDetachedFromSharedRegion: Bool     var libSystemInitialized: Bool     var dyldImageLoadAddress: UnsafePointer<mach_header>     var jitInfo: UnsafeMutablePointer<Void>     var dyldVersion: UnsafePointer<Int8>     var errorMessage: UnsafePointer<Int8>     var terminationFlags: UInt     var coreSymbolicationShmPage: UnsafeMutablePointer<Void>     var systemOrderFlag: UInt     var uuidArrayCount: UInt     var uuidArray: UnsafePointer<dyld_uuid_info>     var dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos>     var initialImageCount: UInt     var errorKind: UInt     var errorClientOfDylibPath: UnsafePointer<Int8>     var errorTargetDylibPath: UnsafePointer<Int8>     var errorSymbol: UnsafePointer<Int8>     var sharedCacheSlide: UInt     var sharedCacheUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var reserved: (UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt) } ``` |
| To | ``` struct dyld_all_image_infos {     var version: UInt32     var infoArrayCount: UInt32     var infoArray: UnsafePointer<dyld_image_info>     var notification: dyld_image_notifier     var processDetachedFromSharedRegion: Bool     var libSystemInitialized: Bool     var dyldImageLoadAddress: UnsafePointer<mach_header>     var jitInfo: UnsafeMutablePointer<Void>     var dyldVersion: UnsafePointer<Int8>     var errorMessage: UnsafePointer<Int8>     var terminationFlags: UInt     var coreSymbolicationShmPage: UnsafeMutablePointer<Void>     var systemOrderFlag: UInt     var uuidArrayCount: UInt     var uuidArray: UnsafePointer<dyld_uuid_info>     var dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos>     var initialImageCount: UInt     var errorKind: UInt     var errorClientOfDylibPath: UnsafePointer<Int8>     var errorTargetDylibPath: UnsafePointer<Int8>     var errorSymbol: UnsafePointer<Int8>     var sharedCacheSlide: UInt     var sharedCacheUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var reserved: (UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt)     init()     init(version version: UInt32, infoArrayCount infoArrayCount: UInt32, infoArray infoArray: UnsafePointer<dyld_image_info>, notification notification: dyld_image_notifier, processDetachedFromSharedRegion processDetachedFromSharedRegion: Bool, libSystemInitialized libSystemInitialized: Bool, dyldImageLoadAddress dyldImageLoadAddress: UnsafePointer<mach_header>, jitInfo jitInfo: UnsafeMutablePointer<Void>, dyldVersion dyldVersion: UnsafePointer<Int8>, errorMessage errorMessage: UnsafePointer<Int8>, terminationFlags terminationFlags: UInt, coreSymbolicationShmPage coreSymbolicationShmPage: UnsafeMutablePointer<Void>, systemOrderFlag systemOrderFlag: UInt, uuidArrayCount uuidArrayCount: UInt, uuidArray uuidArray: UnsafePointer<dyld_uuid_info>, dyldAllImageInfosAddress dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos>, initialImageCount initialImageCount: UInt, errorKind errorKind: UInt, errorClientOfDylibPath errorClientOfDylibPath: UnsafePointer<Int8>, errorTargetDylibPath errorTargetDylibPath: UnsafePointer<Int8>, errorSymbol errorSymbol: UnsafePointer<Int8>, sharedCacheSlide sharedCacheSlide: UInt, sharedCacheUUID sharedCacheUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), reserved reserved: (UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt)) } ``` |

Modified dyld_image_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dyld_image_info {     var imageLoadAddress: UnsafePointer<mach_header>     var imageFilePath: UnsafePointer<Int8>     var imageFileModDate: UInt } ``` |
| To | ``` struct dyld_image_info {     var imageLoadAddress: UnsafePointer<mach_header>     var imageFilePath: UnsafePointer<Int8>     var imageFileModDate: UInt     init()     init(imageLoadAddress imageLoadAddress: UnsafePointer<mach_header>, imageFilePath imageFilePath: UnsafePointer<Int8>, imageFileModDate imageFileModDate: UInt) } ``` |

Modified dyld_info_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dyld_info_command {     var cmd: UInt32     var cmdsize: UInt32     var rebase_off: UInt32     var rebase_size: UInt32     var bind_off: UInt32     var bind_size: UInt32     var weak_bind_off: UInt32     var weak_bind_size: UInt32     var lazy_bind_off: UInt32     var lazy_bind_size: UInt32     var export_off: UInt32     var export_size: UInt32 } ``` |
| To | ``` struct dyld_info_command {     var cmd: UInt32     var cmdsize: UInt32     var rebase_off: UInt32     var rebase_size: UInt32     var bind_off: UInt32     var bind_size: UInt32     var weak_bind_off: UInt32     var weak_bind_size: UInt32     var lazy_bind_off: UInt32     var lazy_bind_size: UInt32     var export_off: UInt32     var export_size: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, rebase_off rebase_off: UInt32, rebase_size rebase_size: UInt32, bind_off bind_off: UInt32, bind_size bind_size: UInt32, weak_bind_off weak_bind_off: UInt32, weak_bind_size weak_bind_size: UInt32, lazy_bind_off lazy_bind_off: UInt32, lazy_bind_size lazy_bind_size: UInt32, export_off export_off: UInt32, export_size export_size: UInt32) } ``` |

Modified dyld_shared_cache_ranges [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dyld_shared_cache_ranges {     var sharedRegionsCount: UInt } ``` |
| To | ``` struct dyld_shared_cache_ranges {     var sharedRegionsCount: UInt     init() } ``` |

Modified dyld_uuid_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dyld_uuid_info {     var imageLoadAddress: UnsafePointer<mach_header>     var imageUUID: uuid_t } ``` |
| To | ``` struct dyld_uuid_info {     var imageLoadAddress: UnsafePointer<mach_header>     var imageUUID: uuid_t     init()     init(imageLoadAddress imageLoadAddress: UnsafePointer<mach_header>, imageUUID imageUUID: uuid_t) } ``` |

Modified dylib [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dylib {     var timestamp: UInt32     var current_version: UInt32     var compatibility_version: UInt32 } ``` |
| To | ``` struct dylib {     var name: lc_str     var timestamp: UInt32     var current_version: UInt32     var compatibility_version: UInt32     init()     init(name name: lc_str, timestamp timestamp: UInt32, current_version current_version: UInt32, compatibility_version compatibility_version: UInt32) } ``` |

Modified dylib_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dylib_command {     var cmd: UInt32     var cmdsize: UInt32     var dylib: dylib } ``` |
| To | ``` struct dylib_command {     var cmd: UInt32     var cmdsize: UInt32     var dylib: dylib     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, dylib dylib: dylib) } ``` |

Modified dylib_module [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dylib_module {     var module_name: UInt32     var iextdefsym: UInt32     var nextdefsym: UInt32     var irefsym: UInt32     var nrefsym: UInt32     var ilocalsym: UInt32     var nlocalsym: UInt32     var iextrel: UInt32     var nextrel: UInt32     var iinit_iterm: UInt32     var ninit_nterm: UInt32     var objc_module_info_addr: UInt32     var objc_module_info_size: UInt32 } ``` |
| To | ``` struct dylib_module {     var module_name: UInt32     var iextdefsym: UInt32     var nextdefsym: UInt32     var irefsym: UInt32     var nrefsym: UInt32     var ilocalsym: UInt32     var nlocalsym: UInt32     var iextrel: UInt32     var nextrel: UInt32     var iinit_iterm: UInt32     var ninit_nterm: UInt32     var objc_module_info_addr: UInt32     var objc_module_info_size: UInt32     init()     init(module_name module_name: UInt32, iextdefsym iextdefsym: UInt32, nextdefsym nextdefsym: UInt32, irefsym irefsym: UInt32, nrefsym nrefsym: UInt32, ilocalsym ilocalsym: UInt32, nlocalsym nlocalsym: UInt32, iextrel iextrel: UInt32, nextrel nextrel: UInt32, iinit_iterm iinit_iterm: UInt32, ninit_nterm ninit_nterm: UInt32, objc_module_info_addr objc_module_info_addr: UInt32, objc_module_info_size objc_module_info_size: UInt32) } ``` |

Modified dylib_module_64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dylib_module_64 {     var module_name: UInt32     var iextdefsym: UInt32     var nextdefsym: UInt32     var irefsym: UInt32     var nrefsym: UInt32     var ilocalsym: UInt32     var nlocalsym: UInt32     var iextrel: UInt32     var nextrel: UInt32     var iinit_iterm: UInt32     var ninit_nterm: UInt32     var objc_module_info_size: UInt32     var objc_module_info_addr: UInt64 } ``` |
| To | ``` struct dylib_module_64 {     var module_name: UInt32     var iextdefsym: UInt32     var nextdefsym: UInt32     var irefsym: UInt32     var nrefsym: UInt32     var ilocalsym: UInt32     var nlocalsym: UInt32     var iextrel: UInt32     var nextrel: UInt32     var iinit_iterm: UInt32     var ninit_nterm: UInt32     var objc_module_info_size: UInt32     var objc_module_info_addr: UInt64     init()     init(module_name module_name: UInt32, iextdefsym iextdefsym: UInt32, nextdefsym nextdefsym: UInt32, irefsym irefsym: UInt32, nrefsym nrefsym: UInt32, ilocalsym ilocalsym: UInt32, nlocalsym nlocalsym: UInt32, iextrel iextrel: UInt32, nextrel nextrel: UInt32, iinit_iterm iinit_iterm: UInt32, ninit_nterm ninit_nterm: UInt32, objc_module_info_size objc_module_info_size: UInt32, objc_module_info_addr objc_module_info_addr: UInt64) } ``` |

Modified dylib_table_of_contents [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dylib_table_of_contents {     var symbol_index: UInt32     var module_index: UInt32 } ``` |
| To | ``` struct dylib_table_of_contents {     var symbol_index: UInt32     var module_index: UInt32     init()     init(symbol_index symbol_index: UInt32, module_index module_index: UInt32) } ``` |

Modified dylinker_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dylinker_command {     var cmd: UInt32     var cmdsize: UInt32 } ``` |
| To | ``` struct dylinker_command {     var cmd: UInt32     var cmdsize: UInt32     var name: lc_str     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, name name: lc_str) } ``` |

Modified dysymtab_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dysymtab_command {     var cmd: UInt32     var cmdsize: UInt32     var ilocalsym: UInt32     var nlocalsym: UInt32     var iextdefsym: UInt32     var nextdefsym: UInt32     var iundefsym: UInt32     var nundefsym: UInt32     var tocoff: UInt32     var ntoc: UInt32     var modtaboff: UInt32     var nmodtab: UInt32     var extrefsymoff: UInt32     var nextrefsyms: UInt32     var indirectsymoff: UInt32     var nindirectsyms: UInt32     var extreloff: UInt32     var nextrel: UInt32     var locreloff: UInt32     var nlocrel: UInt32 } ``` |
| To | ``` struct dysymtab_command {     var cmd: UInt32     var cmdsize: UInt32     var ilocalsym: UInt32     var nlocalsym: UInt32     var iextdefsym: UInt32     var nextdefsym: UInt32     var iundefsym: UInt32     var nundefsym: UInt32     var tocoff: UInt32     var ntoc: UInt32     var modtaboff: UInt32     var nmodtab: UInt32     var extrefsymoff: UInt32     var nextrefsyms: UInt32     var indirectsymoff: UInt32     var nindirectsyms: UInt32     var extreloff: UInt32     var nextrel: UInt32     var locreloff: UInt32     var nlocrel: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, ilocalsym ilocalsym: UInt32, nlocalsym nlocalsym: UInt32, iextdefsym iextdefsym: UInt32, nextdefsym nextdefsym: UInt32, iundefsym iundefsym: UInt32, nundefsym nundefsym: UInt32, tocoff tocoff: UInt32, ntoc ntoc: UInt32, modtaboff modtaboff: UInt32, nmodtab nmodtab: UInt32, extrefsymoff extrefsymoff: UInt32, nextrefsyms nextrefsyms: UInt32, indirectsymoff indirectsymoff: UInt32, nindirectsyms nindirectsyms: UInt32, extreloff extreloff: UInt32, nextrel nextrel: UInt32, locreloff locreloff: UInt32, nlocrel nlocrel: UInt32) } ``` |

Modified encryption_info_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct encryption_info_command {     var cmd: UInt32     var cmdsize: UInt32     var cryptoff: UInt32     var cryptsize: UInt32     var cryptid: UInt32 } ``` |
| To | ``` struct encryption_info_command {     var cmd: UInt32     var cmdsize: UInt32     var cryptoff: UInt32     var cryptsize: UInt32     var cryptid: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, cryptoff cryptoff: UInt32, cryptsize cryptsize: UInt32, cryptid cryptid: UInt32) } ``` |

Modified encryption_info_command_64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct encryption_info_command_64 {     var cmd: UInt32     var cmdsize: UInt32     var cryptoff: UInt32     var cryptsize: UInt32     var cryptid: UInt32     var pad: UInt32 } ``` |
| To | ``` struct encryption_info_command_64 {     var cmd: UInt32     var cmdsize: UInt32     var cryptoff: UInt32     var cryptsize: UInt32     var cryptid: UInt32     var pad: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, cryptoff cryptoff: UInt32, cryptsize cryptsize: UInt32, cryptid cryptid: UInt32, pad pad: UInt32) } ``` |

Modified entry_point_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct entry_point_command {     var cmd: UInt32     var cmdsize: UInt32     var entryoff: UInt64     var stacksize: UInt64 } ``` |
| To | ``` struct entry_point_command {     var cmd: UInt32     var cmdsize: UInt32     var entryoff: UInt64     var stacksize: UInt64     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, entryoff entryoff: UInt64, stacksize stacksize: UInt64) } ``` |

Modified fat_arch [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fat_arch {     var cputype: cpu_type_t     var cpusubtype: cpu_subtype_t     var offset: UInt32     var size: UInt32     var align: UInt32 } ``` |
| To | ``` struct fat_arch {     var cputype: cpu_type_t     var cpusubtype: cpu_subtype_t     var offset: UInt32     var size: UInt32     var align: UInt32     init()     init(cputype cputype: cpu_type_t, cpusubtype cpusubtype: cpu_subtype_t, offset offset: UInt32, size size: UInt32, align align: UInt32) } ``` |

Modified fat_header [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fat_header {     var magic: UInt32     var nfat_arch: UInt32 } ``` |
| To | ``` struct fat_header {     var magic: UInt32     var nfat_arch: UInt32     init()     init(magic magic: UInt32, nfat_arch nfat_arch: UInt32) } ``` |

Modified fvmfile_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fvmfile_command {     var cmd: UInt32     var cmdsize: UInt32     var header_addr: UInt32 } ``` |
| To | ``` struct fvmfile_command {     var cmd: UInt32     var cmdsize: UInt32     var name: lc_str     var header_addr: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, name name: lc_str, header_addr header_addr: UInt32) } ``` |

Modified fvmlib [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fvmlib {     var minor_version: UInt32     var header_addr: UInt32 } ``` |
| To | ``` struct fvmlib {     var name: lc_str     var minor_version: UInt32     var header_addr: UInt32     init()     init(name name: lc_str, minor_version minor_version: UInt32, header_addr header_addr: UInt32) } ``` |

Modified fvmlib_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct fvmlib_command {     var cmd: UInt32     var cmdsize: UInt32     var fvmlib: fvmlib } ``` |
| To | ``` struct fvmlib_command {     var cmd: UInt32     var cmdsize: UInt32     var fvmlib: fvmlib     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, fvmlib fvmlib: fvmlib) } ``` |

Modified ident_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ident_command {     var cmd: UInt32     var cmdsize: UInt32 } ``` |
| To | ``` struct ident_command {     var cmd: UInt32     var cmdsize: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32) } ``` |

Modified linkedit_data_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct linkedit_data_command {     var cmd: UInt32     var cmdsize: UInt32     var dataoff: UInt32     var datasize: UInt32 } ``` |
| To | ``` struct linkedit_data_command {     var cmd: UInt32     var cmdsize: UInt32     var dataoff: UInt32     var datasize: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, dataoff dataoff: UInt32, datasize datasize: UInt32) } ``` |

Modified linker_option_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct linker_option_command {     var cmd: UInt32     var cmdsize: UInt32     var count: UInt32 } ``` |
| To | ``` struct linker_option_command {     var cmd: UInt32     var cmdsize: UInt32     var count: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, count count: UInt32) } ``` |

Modified load_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct load_command {     var cmd: UInt32     var cmdsize: UInt32 } ``` |
| To | ``` struct load_command {     var cmd: UInt32     var cmdsize: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32) } ``` |

Modified mach_header [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_header {     var magic: UInt32     var cputype: cpu_type_t     var cpusubtype: cpu_subtype_t     var filetype: UInt32     var ncmds: UInt32     var sizeofcmds: UInt32     var flags: UInt32 } ``` |
| To | ``` struct mach_header {     var magic: UInt32     var cputype: cpu_type_t     var cpusubtype: cpu_subtype_t     var filetype: UInt32     var ncmds: UInt32     var sizeofcmds: UInt32     var flags: UInt32     init()     init(magic magic: UInt32, cputype cputype: cpu_type_t, cpusubtype cpusubtype: cpu_subtype_t, filetype filetype: UInt32, ncmds ncmds: UInt32, sizeofcmds sizeofcmds: UInt32, flags flags: UInt32) } ``` |

Modified mach_header_64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mach_header_64 {     var magic: UInt32     var cputype: cpu_type_t     var cpusubtype: cpu_subtype_t     var filetype: UInt32     var ncmds: UInt32     var sizeofcmds: UInt32     var flags: UInt32     var reserved: UInt32 } ``` |
| To | ``` struct mach_header_64 {     var magic: UInt32     var cputype: cpu_type_t     var cpusubtype: cpu_subtype_t     var filetype: UInt32     var ncmds: UInt32     var sizeofcmds: UInt32     var flags: UInt32     var reserved: UInt32     init()     init(magic magic: UInt32, cputype cputype: cpu_type_t, cpusubtype cpusubtype: cpu_subtype_t, filetype filetype: UInt32, ncmds ncmds: UInt32, sizeofcmds sizeofcmds: UInt32, flags flags: UInt32, reserved reserved: UInt32) } ``` |

Modified nlist [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct nlist {     var n_type: UInt8     var n_sect: UInt8     var n_desc: Int16     var n_value: UInt32 } ``` |
| To | ``` struct nlist {     var n_type: UInt8     var n_sect: UInt8     var n_desc: Int16     var n_value: UInt32     init() } ``` |

Modified nlist_64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct nlist_64 {     var n_type: UInt8     var n_sect: UInt8     var n_desc: UInt16     var n_value: UInt64 } ``` |
| To | ``` struct nlist_64 {     var n_type: UInt8     var n_sect: UInt8     var n_desc: UInt16     var n_value: UInt64     init() } ``` |

Modified prebind_cksum_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct prebind_cksum_command {     var cmd: UInt32     var cmdsize: UInt32     var cksum: UInt32 } ``` |
| To | ``` struct prebind_cksum_command {     var cmd: UInt32     var cmdsize: UInt32     var cksum: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, cksum cksum: UInt32) } ``` |

Modified prebound_dylib_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct prebound_dylib_command {     var cmd: UInt32     var cmdsize: UInt32     var nmodules: UInt32 } ``` |
| To | ``` struct prebound_dylib_command {     var cmd: UInt32     var cmdsize: UInt32     var name: lc_str     var nmodules: UInt32     var linked_modules: lc_str     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, name name: lc_str, nmodules nmodules: UInt32, linked_modules linked_modules: lc_str) } ``` |

Modified ranlib [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ranlib {     var ran_off: UInt32 } ``` |
| To | ``` struct ranlib {     var ran_off: UInt32     init() } ``` |

Modified routines_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct routines_command {     var cmd: UInt32     var cmdsize: UInt32     var init_address: UInt32     var init_module: UInt32     var reserved1: UInt32     var reserved2: UInt32     var reserved3: UInt32     var reserved4: UInt32     var reserved5: UInt32     var reserved6: UInt32 } ``` |
| To | ``` struct routines_command {     var cmd: UInt32     var cmdsize: UInt32     var init_address: UInt32     var init_module: UInt32     var reserved1: UInt32     var reserved2: UInt32     var reserved3: UInt32     var reserved4: UInt32     var reserved5: UInt32     var reserved6: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, init_address init_address: UInt32, init_module init_module: UInt32, reserved1 reserved1: UInt32, reserved2 reserved2: UInt32, reserved3 reserved3: UInt32, reserved4 reserved4: UInt32, reserved5 reserved5: UInt32, reserved6 reserved6: UInt32) } ``` |

Modified routines_command_64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct routines_command_64 {     var cmd: UInt32     var cmdsize: UInt32     var init_address: UInt64     var init_module: UInt64     var reserved1: UInt64     var reserved2: UInt64     var reserved3: UInt64     var reserved4: UInt64     var reserved5: UInt64     var reserved6: UInt64 } ``` |
| To | ``` struct routines_command_64 {     var cmd: UInt32     var cmdsize: UInt32     var init_address: UInt64     var init_module: UInt64     var reserved1: UInt64     var reserved2: UInt64     var reserved3: UInt64     var reserved4: UInt64     var reserved5: UInt64     var reserved6: UInt64     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, init_address init_address: UInt64, init_module init_module: UInt64, reserved1 reserved1: UInt64, reserved2 reserved2: UInt64, reserved3 reserved3: UInt64, reserved4 reserved4: UInt64, reserved5 reserved5: UInt64, reserved6 reserved6: UInt64) } ``` |

Modified rpath_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct rpath_command {     var cmd: UInt32     var cmdsize: UInt32 } ``` |
| To | ``` struct rpath_command {     var cmd: UInt32     var cmdsize: UInt32     var path: lc_str     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, path path: lc_str) } ``` |

Modified section [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct section {     var sectname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var segname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var addr: UInt32     var size: UInt32     var offset: UInt32     var align: UInt32     var reloff: UInt32     var nreloc: UInt32     var flags: UInt32     var reserved1: UInt32     var reserved2: UInt32 } ``` |
| To | ``` struct section {     var sectname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var segname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var addr: UInt32     var size: UInt32     var offset: UInt32     var align: UInt32     var reloff: UInt32     var nreloc: UInt32     var flags: UInt32     var reserved1: UInt32     var reserved2: UInt32     init()     init(sectname sectname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), segname segname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), addr addr: UInt32, size size: UInt32, offset offset: UInt32, align align: UInt32, reloff reloff: UInt32, nreloc nreloc: UInt32, flags flags: UInt32, reserved1 reserved1: UInt32, reserved2 reserved2: UInt32) } ``` |

Modified section_64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct section_64 {     var sectname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var segname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var addr: UInt64     var size: UInt64     var offset: UInt32     var align: UInt32     var reloff: UInt32     var nreloc: UInt32     var flags: UInt32     var reserved1: UInt32     var reserved2: UInt32     var reserved3: UInt32 } ``` |
| To | ``` struct section_64 {     var sectname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var segname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var addr: UInt64     var size: UInt64     var offset: UInt32     var align: UInt32     var reloff: UInt32     var nreloc: UInt32     var flags: UInt32     var reserved1: UInt32     var reserved2: UInt32     var reserved3: UInt32     init()     init(sectname sectname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), segname segname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), addr addr: UInt64, size size: UInt64, offset offset: UInt32, align align: UInt32, reloff reloff: UInt32, nreloc nreloc: UInt32, flags flags: UInt32, reserved1 reserved1: UInt32, reserved2 reserved2: UInt32, reserved3 reserved3: UInt32) } ``` |

Modified segment_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct segment_command {     var cmd: UInt32     var cmdsize: UInt32     var segname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var vmaddr: UInt32     var vmsize: UInt32     var fileoff: UInt32     var filesize: UInt32     var maxprot: vm_prot_t     var initprot: vm_prot_t     var nsects: UInt32     var flags: UInt32 } ``` |
| To | ``` struct segment_command {     var cmd: UInt32     var cmdsize: UInt32     var segname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var vmaddr: UInt32     var vmsize: UInt32     var fileoff: UInt32     var filesize: UInt32     var maxprot: vm_prot_t     var initprot: vm_prot_t     var nsects: UInt32     var flags: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, segname segname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), vmaddr vmaddr: UInt32, vmsize vmsize: UInt32, fileoff fileoff: UInt32, filesize filesize: UInt32, maxprot maxprot: vm_prot_t, initprot initprot: vm_prot_t, nsects nsects: UInt32, flags flags: UInt32) } ``` |

Modified segment_command_64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct segment_command_64 {     var cmd: UInt32     var cmdsize: UInt32     var segname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var vmaddr: UInt64     var vmsize: UInt64     var fileoff: UInt64     var filesize: UInt64     var maxprot: vm_prot_t     var initprot: vm_prot_t     var nsects: UInt32     var flags: UInt32 } ``` |
| To | ``` struct segment_command_64 {     var cmd: UInt32     var cmdsize: UInt32     var segname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var vmaddr: UInt64     var vmsize: UInt64     var fileoff: UInt64     var filesize: UInt64     var maxprot: vm_prot_t     var initprot: vm_prot_t     var nsects: UInt32     var flags: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, segname segname: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), vmaddr vmaddr: UInt64, vmsize vmsize: UInt64, fileoff fileoff: UInt64, filesize filesize: UInt64, maxprot maxprot: vm_prot_t, initprot initprot: vm_prot_t, nsects nsects: UInt32, flags flags: UInt32) } ``` |

Modified source_version_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct source_version_command {     var cmd: UInt32     var cmdsize: UInt32     var version: UInt64 } ``` |
| To | ``` struct source_version_command {     var cmd: UInt32     var cmdsize: UInt32     var version: UInt64     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, version version: UInt64) } ``` |

Modified sub_client_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sub_client_command {     var cmd: UInt32     var cmdsize: UInt32 } ``` |
| To | ``` struct sub_client_command {     var cmd: UInt32     var cmdsize: UInt32     var client: lc_str     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, client client: lc_str) } ``` |

Modified sub_framework_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sub_framework_command {     var cmd: UInt32     var cmdsize: UInt32 } ``` |
| To | ``` struct sub_framework_command {     var cmd: UInt32     var cmdsize: UInt32     var umbrella: lc_str     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, umbrella umbrella: lc_str) } ``` |

Modified sub_library_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sub_library_command {     var cmd: UInt32     var cmdsize: UInt32 } ``` |
| To | ``` struct sub_library_command {     var cmd: UInt32     var cmdsize: UInt32     var sub_library: lc_str     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, sub_library sub_library: lc_str) } ``` |

Modified sub_umbrella_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sub_umbrella_command {     var cmd: UInt32     var cmdsize: UInt32 } ``` |
| To | ``` struct sub_umbrella_command {     var cmd: UInt32     var cmdsize: UInt32     var sub_umbrella: lc_str     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, sub_umbrella sub_umbrella: lc_str) } ``` |

Modified symseg_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct symseg_command {     var cmd: UInt32     var cmdsize: UInt32     var offset: UInt32     var size: UInt32 } ``` |
| To | ``` struct symseg_command {     var cmd: UInt32     var cmdsize: UInt32     var offset: UInt32     var size: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, offset offset: UInt32, size size: UInt32) } ``` |

Modified symtab_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct symtab_command {     var cmd: UInt32     var cmdsize: UInt32     var symoff: UInt32     var nsyms: UInt32     var stroff: UInt32     var strsize: UInt32 } ``` |
| To | ``` struct symtab_command {     var cmd: UInt32     var cmdsize: UInt32     var symoff: UInt32     var nsyms: UInt32     var stroff: UInt32     var strsize: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, symoff symoff: UInt32, nsyms nsyms: UInt32, stroff stroff: UInt32, strsize strsize: UInt32) } ``` |

Modified thread_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct thread_command {     var cmd: UInt32     var cmdsize: UInt32 } ``` |
| To | ``` struct thread_command {     var cmd: UInt32     var cmdsize: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32) } ``` |

Modified tlv_descriptor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tlv_descriptor {     var thunk: CFunctionPointer<((UnsafeMutablePointer<tlv_descriptor>) -> UnsafeMutablePointer<Void>)>     var key: UInt     var offset: UInt } ``` |
| To | ``` struct tlv_descriptor {     var thunk: CFunctionPointer<((UnsafeMutablePointer<tlv_descriptor>) -> UnsafeMutablePointer<Void>)>     var key: UInt     var offset: UInt     init()     init(thunk thunk: CFunctionPointer<((UnsafeMutablePointer<tlv_descriptor>) -> UnsafeMutablePointer<Void>)>, key key: UInt, offset offset: UInt) } ``` |

Modified twolevel_hints_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct twolevel_hints_command {     var cmd: UInt32     var cmdsize: UInt32     var offset: UInt32     var nhints: UInt32 } ``` |
| To | ``` struct twolevel_hints_command {     var cmd: UInt32     var cmdsize: UInt32     var offset: UInt32     var nhints: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, offset offset: UInt32, nhints nhints: UInt32) } ``` |

Modified unwind_info_compressed_second_level_page_header [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct unwind_info_compressed_second_level_page_header {     var kind: UInt32     var entryPageOffset: UInt16     var entryCount: UInt16     var encodingsPageOffset: UInt16     var encodingsCount: UInt16 } ``` |
| To | ``` struct unwind_info_compressed_second_level_page_header {     var kind: UInt32     var entryPageOffset: UInt16     var entryCount: UInt16     var encodingsPageOffset: UInt16     var encodingsCount: UInt16     init()     init(kind kind: UInt32, entryPageOffset entryPageOffset: UInt16, entryCount entryCount: UInt16, encodingsPageOffset encodingsPageOffset: UInt16, encodingsCount encodingsCount: UInt16) } ``` |

Modified unwind_info_regular_second_level_entry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct unwind_info_regular_second_level_entry {     var functionOffset: UInt32     var encoding: compact_unwind_encoding_t } ``` |
| To | ``` struct unwind_info_regular_second_level_entry {     var functionOffset: UInt32     var encoding: compact_unwind_encoding_t     init()     init(functionOffset functionOffset: UInt32, encoding encoding: compact_unwind_encoding_t) } ``` |

Modified unwind_info_regular_second_level_page_header [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct unwind_info_regular_second_level_page_header {     var kind: UInt32     var entryPageOffset: UInt16     var entryCount: UInt16 } ``` |
| To | ``` struct unwind_info_regular_second_level_page_header {     var kind: UInt32     var entryPageOffset: UInt16     var entryCount: UInt16     init()     init(kind kind: UInt32, entryPageOffset entryPageOffset: UInt16, entryCount entryCount: UInt16) } ``` |

Modified unwind_info_section_header [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct unwind_info_section_header {     var version: UInt32     var commonEncodingsArraySectionOffset: UInt32     var commonEncodingsArrayCount: UInt32     var personalityArraySectionOffset: UInt32     var personalityArrayCount: UInt32     var indexSectionOffset: UInt32     var indexCount: UInt32 } ``` |
| To | ``` struct unwind_info_section_header {     var version: UInt32     var commonEncodingsArraySectionOffset: UInt32     var commonEncodingsArrayCount: UInt32     var personalityArraySectionOffset: UInt32     var personalityArrayCount: UInt32     var indexSectionOffset: UInt32     var indexCount: UInt32     init()     init(version version: UInt32, commonEncodingsArraySectionOffset commonEncodingsArraySectionOffset: UInt32, commonEncodingsArrayCount commonEncodingsArrayCount: UInt32, personalityArraySectionOffset personalityArraySectionOffset: UInt32, personalityArrayCount personalityArrayCount: UInt32, indexSectionOffset indexSectionOffset: UInt32, indexCount indexCount: UInt32) } ``` |

Modified unwind_info_section_header_index_entry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct unwind_info_section_header_index_entry {     var functionOffset: UInt32     var secondLevelPagesSectionOffset: UInt32     var lsdaIndexArraySectionOffset: UInt32 } ``` |
| To | ``` struct unwind_info_section_header_index_entry {     var functionOffset: UInt32     var secondLevelPagesSectionOffset: UInt32     var lsdaIndexArraySectionOffset: UInt32     init()     init(functionOffset functionOffset: UInt32, secondLevelPagesSectionOffset secondLevelPagesSectionOffset: UInt32, lsdaIndexArraySectionOffset lsdaIndexArraySectionOffset: UInt32) } ``` |

Modified unwind_info_section_header_lsda_index_entry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct unwind_info_section_header_lsda_index_entry {     var functionOffset: UInt32     var lsdaOffset: UInt32 } ``` |
| To | ``` struct unwind_info_section_header_lsda_index_entry {     var functionOffset: UInt32     var lsdaOffset: UInt32     init()     init(functionOffset functionOffset: UInt32, lsdaOffset lsdaOffset: UInt32) } ``` |

Modified uuid_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct uuid_command {     var cmd: UInt32     var cmdsize: UInt32     var uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct uuid_command {     var cmd: UInt32     var cmdsize: UInt32     var uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, uuid uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified version_min_command [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct version_min_command {     var cmd: UInt32     var cmdsize: UInt32     var version: UInt32     var sdk: UInt32 } ``` |
| To | ``` struct version_min_command {     var cmd: UInt32     var cmdsize: UInt32     var version: UInt32     var sdk: UInt32     init()     init(cmd cmd: UInt32, cmdsize cmdsize: UInt32, version version: UInt32, sdk sdk: UInt32) } ``` |

Modified swap_dylib_reference(UnsafeMutablePointer<dylib_reference>, UInt32, NXByteOrder)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func swap_dylib_reference(_ refs: COpaquePointer, _ nrefs: UInt32, _ target_byte_sex: NXByteOrder) ``` | iOS 8.0 |
| To | ``` func swap_dylib_reference(_ refs: UnsafeMutablePointer<dylib_reference>, _ nrefs: UInt32, _ target_byte_sex: NXByteOrder) ``` | iOS 8.3 |

Modified swap_relocation_info(UnsafeMutablePointer<relocation_info>, UInt32, NXByteOrder)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func swap_relocation_info(_ relocs: COpaquePointer, _ nrelocs: UInt32, _ target_byte_order: NXByteOrder) ``` | iOS 8.0 |
| To | ``` func swap_relocation_info(_ relocs: UnsafeMutablePointer<relocation_info>, _ nrelocs: UInt32, _ target_byte_order: NXByteOrder) ``` | iOS 8.3 |

Modified swap_twolevel_hint(UnsafeMutablePointer<twolevel_hint>, UInt32, NXByteOrder)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func swap_twolevel_hint(_ hints: COpaquePointer, _ nhints: UInt32, _ target_byte_sex: NXByteOrder) ``` | iOS 8.0 |
| To | ``` func swap_twolevel_hint(_ hints: UnsafeMutablePointer<twolevel_hint>, _ nhints: UInt32, _ target_byte_sex: NXByteOrder) ``` | iOS 8.3 |

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
