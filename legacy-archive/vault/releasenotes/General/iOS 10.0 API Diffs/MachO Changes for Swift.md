---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/MachO.html
archived_at: '2026-07-18T02:55:30.994001Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# MachO Changes for Swift

### MachO

Removed dyld_all_image_infos.init(version: UInt32, infoArrayCount: UInt32, infoArray: UnsafePointer<dyld_image_info>, notification: dyld_image_notifier!, processDetachedFromSharedRegion: Bool, libSystemInitialized: Bool, dyldImageLoadAddress: UnsafePointer<mach_header>, jitInfo: UnsafeMutablePointer<Void>, dyldVersion: UnsafePointer<Int8>, errorMessage: UnsafePointer<Int8>, terminationFlags: UInt, coreSymbolicationShmPage: UnsafeMutablePointer<Void>, systemOrderFlag: UInt, uuidArrayCount: UInt, uuidArray: UnsafePointer<dyld_uuid_info>, dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos>, initialImageCount: UInt, errorKind: UInt, errorClientOfDylibPath: UnsafePointer<Int8>, errorTargetDylibPath: UnsafePointer<Int8>, errorSymbol: UnsafePointer<Int8>, sharedCacheSlide: UInt, sharedCacheUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), reserved: (UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt))Removed dyld_image_info.init(imageLoadAddress: UnsafePointer<mach_header>, imageFilePath: UnsafePointer<Int8>, imageFileModDate: UInt)Removed dyld_uuid_info.init(imageLoadAddress: UnsafePointer<mach_header>, imageUUID: uuid_t)Removed lc_str.init(ptr: UnsafeMutablePointer<Int8>)Removed lc_str.ptrRemoved NSLinkEditErrorHandlers.init(undefined: ((UnsafePointer<Int8>) -> Void)!, multiple: ((NSSymbol, NSModule, NSModule) -> NSModule)!, linkEdit: ((NSLinkEditErrors, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Void)!)Removed NXArchInfo.init(name: UnsafePointer<Int8>, cputype: cpu_type_t, cpusubtype: cpu_subtype_t, byteorder: NXByteOrder, description: UnsafePointer<Int8>)Removed tlv_descriptor.init(thunk: ((UnsafeMutablePointer<tlv_descriptor>) -> UnsafeMutablePointer<Void>)!, key: UInt, offset: UInt)Added dyld_all_image_infos.dyldPathAdded dyld_all_image_infos.infoArrayChangeTimestampAdded dyld_all_image_infos.init(version: UInt32, infoArrayCount: UInt32, infoArray: UnsafePointer<dyld_image_info>!, notification: MachO.dyld_image_notifier!, processDetachedFromSharedRegion: Bool, libSystemInitialized: Bool, dyldImageLoadAddress: UnsafePointer<mach_header>!, jitInfo: UnsafeMutableRawPointer!, dyldVersion: UnsafePointer<Int8>!, errorMessage: UnsafePointer<Int8>!, terminationFlags: UInt, coreSymbolicationShmPage: UnsafeMutableRawPointer!, systemOrderFlag: UInt, uuidArrayCount: UInt, uuidArray: UnsafePointer<dyld_uuid_info>!, dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos>!, initialImageCount: UInt, errorKind: UInt, errorClientOfDylibPath: UnsafePointer<Int8>!, errorTargetDylibPath: UnsafePointer<Int8>!, errorSymbol: UnsafePointer<Int8>!, sharedCacheSlide: UInt, sharedCacheUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), sharedCacheBaseAddress: UInt, infoArrayChangeTimestamp: UInt64, dyldPath: UnsafePointer<Int8>!, notifyPorts: (mach_port_t, mach_port_t, mach_port_t, mach_port_t, mach_port_t, mach_port_t, mach_port_t, mach_port_t), reserved: (UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt))Added dyld_all_image_infos.notifyPortsAdded dyld_all_image_infos.sharedCacheBaseAddressAdded dyld_image_info.init(imageLoadAddress: UnsafePointer<mach_header>!, imageFilePath: UnsafePointer<Int8>!, imageFileModDate: UInt)Added dyld_uuid_info.init(imageLoadAddress: UnsafePointer<mach_header>!, imageUUID: Darwin.uuid_t)Added fat_arch_64 [struct]Added fat_arch_64.alignAdded fat_arch_64.cpusubtypeAdded fat_arch_64.cputypeAdded fat_arch_64.init()Added fat_arch_64.init(cputype: cpu_type_t, cpusubtype: cpu_subtype_t, offset: UInt64, size: UInt64, align: UInt32, reserved: UInt32)Added fat_arch_64.offsetAdded fat_arch_64.reservedAdded fat_arch_64.sizeAdded NSLinkEditErrorHandlers.init(undefined: ( (UnsafePointer<Int8>?) -> Swift.Void)!, multiple: ( (NSSymbol?, NSModule?, NSModule?) -> NSModule?)!, linkEdit: ( (NSLinkEditErrors, Int32, UnsafePointer<Int8>?, UnsafePointer<Int8>?) -> Swift.Void)!)Added NXArchInfo.init(name: UnsafePointer<Int8>!, cputype: cpu_type_t, cpusubtype: cpu_subtype_t, byteorder: NXByteOrder, description: UnsafePointer<Int8>!)Added ranlib_64 [struct]Added ranlib_64.init()Added ranlib_64.init(ran_un: ranlib_64.__Unnamed_union_ran_un, ran_off: UInt64)Added ranlib_64.ran_offAdded ranlib_64.ran_unAdded tlv_descriptor.init(thunk: ( (UnsafeMutablePointer<tlv_descriptor>?) -> UnsafeMutableRawPointer?)!, key: UInt, offset: UInt)Added DYLD_MAX_PROCESS_INFO_NOTIFY_COUNTAdded FAT_CIGAM_64Added FAT_MAGIC_64Added NXFindBestFatArch_64(_: cpu_type_t, _: cpu_subtype_t, _: UnsafeMutablePointer<fat_arch_64>!, _: UInt32) -> UnsafeMutablePointer<fat_arch_64>!Added swap_fat_arch_64(_: UnsafeMutablePointer<fat_arch_64>!, _: UInt32, _: NXByteOrder)Added swap_ranlib_64(_: UnsafeMutablePointer<ranlib_64>!, _: UInt64, _: NXByteOrder)Added SYMDEF_64Added SYMDEF_64_SORTEDModified dyld_all_image_infos [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dyld_all_image_infos {     var version: UInt32     var infoArrayCount: UInt32     var infoArray: UnsafePointer<dyld_image_info>     var notification: dyld_image_notifier!     var processDetachedFromSharedRegion: Bool     var libSystemInitialized: Bool     var dyldImageLoadAddress: UnsafePointer<mach_header>     var jitInfo: UnsafeMutablePointer<Void>     var dyldVersion: UnsafePointer<Int8>     var errorMessage: UnsafePointer<Int8>     var terminationFlags: UInt     var coreSymbolicationShmPage: UnsafeMutablePointer<Void>     var systemOrderFlag: UInt     var uuidArrayCount: UInt     var uuidArray: UnsafePointer<dyld_uuid_info>     var dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos>     var initialImageCount: UInt     var errorKind: UInt     var errorClientOfDylibPath: UnsafePointer<Int8>     var errorTargetDylibPath: UnsafePointer<Int8>     var errorSymbol: UnsafePointer<Int8>     var sharedCacheSlide: UInt     var sharedCacheUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var reserved: (UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt)     init()     init(version version: UInt32, infoArrayCount infoArrayCount: UInt32, infoArray infoArray: UnsafePointer<dyld_image_info>, notification notification: dyld_image_notifier!, processDetachedFromSharedRegion processDetachedFromSharedRegion: Bool, libSystemInitialized libSystemInitialized: Bool, dyldImageLoadAddress dyldImageLoadAddress: UnsafePointer<mach_header>, jitInfo jitInfo: UnsafeMutablePointer<Void>, dyldVersion dyldVersion: UnsafePointer<Int8>, errorMessage errorMessage: UnsafePointer<Int8>, terminationFlags terminationFlags: UInt, coreSymbolicationShmPage coreSymbolicationShmPage: UnsafeMutablePointer<Void>, systemOrderFlag systemOrderFlag: UInt, uuidArrayCount uuidArrayCount: UInt, uuidArray uuidArray: UnsafePointer<dyld_uuid_info>, dyldAllImageInfosAddress dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos>, initialImageCount initialImageCount: UInt, errorKind errorKind: UInt, errorClientOfDylibPath errorClientOfDylibPath: UnsafePointer<Int8>, errorTargetDylibPath errorTargetDylibPath: UnsafePointer<Int8>, errorSymbol errorSymbol: UnsafePointer<Int8>, sharedCacheSlide sharedCacheSlide: UInt, sharedCacheUUID sharedCacheUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), reserved reserved: (UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt)) } ``` |
| To | ``` struct dyld_all_image_infos {     var version: UInt32     var infoArrayCount: UInt32     var infoArray: UnsafePointer<dyld_image_info>!     var notification: MachO.dyld_image_notifier!     var processDetachedFromSharedRegion: Bool     var libSystemInitialized: Bool     var dyldImageLoadAddress: UnsafePointer<mach_header>!     var jitInfo: UnsafeMutableRawPointer!     var dyldVersion: UnsafePointer<Int8>!     var errorMessage: UnsafePointer<Int8>!     var terminationFlags: UInt     var coreSymbolicationShmPage: UnsafeMutableRawPointer!     var systemOrderFlag: UInt     var uuidArrayCount: UInt     var uuidArray: UnsafePointer<dyld_uuid_info>!     var dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos>!     var initialImageCount: UInt     var errorKind: UInt     var errorClientOfDylibPath: UnsafePointer<Int8>!     var errorTargetDylibPath: UnsafePointer<Int8>!     var errorSymbol: UnsafePointer<Int8>!     var sharedCacheSlide: UInt     var sharedCacheUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var sharedCacheBaseAddress: UInt     var infoArrayChangeTimestamp: UInt64     var dyldPath: UnsafePointer<Int8>!     var notifyPorts: (mach_port_t, mach_port_t, mach_port_t, mach_port_t, mach_port_t, mach_port_t, mach_port_t, mach_port_t)     var reserved: (UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt)     init()     init(version version: UInt32, infoArrayCount infoArrayCount: UInt32, infoArray infoArray: UnsafePointer<dyld_image_info>!, notification notification: MachO.dyld_image_notifier!, processDetachedFromSharedRegion processDetachedFromSharedRegion: Bool, libSystemInitialized libSystemInitialized: Bool, dyldImageLoadAddress dyldImageLoadAddress: UnsafePointer<mach_header>!, jitInfo jitInfo: UnsafeMutableRawPointer!, dyldVersion dyldVersion: UnsafePointer<Int8>!, errorMessage errorMessage: UnsafePointer<Int8>!, terminationFlags terminationFlags: UInt, coreSymbolicationShmPage coreSymbolicationShmPage: UnsafeMutableRawPointer!, systemOrderFlag systemOrderFlag: UInt, uuidArrayCount uuidArrayCount: UInt, uuidArray uuidArray: UnsafePointer<dyld_uuid_info>!, dyldAllImageInfosAddress dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos>!, initialImageCount initialImageCount: UInt, errorKind errorKind: UInt, errorClientOfDylibPath errorClientOfDylibPath: UnsafePointer<Int8>!, errorTargetDylibPath errorTargetDylibPath: UnsafePointer<Int8>!, errorSymbol errorSymbol: UnsafePointer<Int8>!, sharedCacheSlide sharedCacheSlide: UInt, sharedCacheUUID sharedCacheUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), sharedCacheBaseAddress sharedCacheBaseAddress: UInt, infoArrayChangeTimestamp infoArrayChangeTimestamp: UInt64, dyldPath dyldPath: UnsafePointer<Int8>!, notifyPorts notifyPorts: (mach_port_t, mach_port_t, mach_port_t, mach_port_t, mach_port_t, mach_port_t, mach_port_t, mach_port_t), reserved reserved: (UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt)) } ``` |

Modified dyld_all_image_infos.coreSymbolicationShmPage

|  | Declaration |
| --- | --- |
| From | ``` var coreSymbolicationShmPage: UnsafeMutablePointer<Void> ``` |
| To | ``` var coreSymbolicationShmPage: UnsafeMutableRawPointer! ``` |

Modified dyld_all_image_infos.dyldAllImageInfosAddress

|  | Declaration |
| --- | --- |
| From | ``` var dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos> ``` |
| To | ``` var dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos>! ``` |

Modified dyld_all_image_infos.dyldImageLoadAddress

|  | Declaration |
| --- | --- |
| From | ``` var dyldImageLoadAddress: UnsafePointer<mach_header> ``` |
| To | ``` var dyldImageLoadAddress: UnsafePointer<mach_header>! ``` |

Modified dyld_all_image_infos.dyldVersion

|  | Declaration |
| --- | --- |
| From | ``` var dyldVersion: UnsafePointer<Int8> ``` |
| To | ``` var dyldVersion: UnsafePointer<Int8>! ``` |

Modified dyld_all_image_infos.errorClientOfDylibPath

|  | Declaration |
| --- | --- |
| From | ``` var errorClientOfDylibPath: UnsafePointer<Int8> ``` |
| To | ``` var errorClientOfDylibPath: UnsafePointer<Int8>! ``` |

Modified dyld_all_image_infos.errorMessage

|  | Declaration |
| --- | --- |
| From | ``` var errorMessage: UnsafePointer<Int8> ``` |
| To | ``` var errorMessage: UnsafePointer<Int8>! ``` |

Modified dyld_all_image_infos.errorSymbol

|  | Declaration |
| --- | --- |
| From | ``` var errorSymbol: UnsafePointer<Int8> ``` |
| To | ``` var errorSymbol: UnsafePointer<Int8>! ``` |

Modified dyld_all_image_infos.errorTargetDylibPath

|  | Declaration |
| --- | --- |
| From | ``` var errorTargetDylibPath: UnsafePointer<Int8> ``` |
| To | ``` var errorTargetDylibPath: UnsafePointer<Int8>! ``` |

Modified dyld_all_image_infos.infoArray

|  | Declaration |
| --- | --- |
| From | ``` var infoArray: UnsafePointer<dyld_image_info> ``` |
| To | ``` var infoArray: UnsafePointer<dyld_image_info>! ``` |

Modified dyld_all_image_infos.jitInfo

|  | Declaration |
| --- | --- |
| From | ``` var jitInfo: UnsafeMutablePointer<Void> ``` |
| To | ``` var jitInfo: UnsafeMutableRawPointer! ``` |

Modified dyld_all_image_infos.notification

|  | Declaration |
| --- | --- |
| From | ``` var notification: dyld_image_notifier! ``` |
| To | ``` var notification: MachO.dyld_image_notifier! ``` |

Modified dyld_all_image_infos.reserved

|  | Declaration |
| --- | --- |
| From | ``` var reserved: (UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt) ``` |
| To | ``` var reserved: (UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt) ``` |

Modified dyld_all_image_infos.uuidArray

|  | Declaration |
| --- | --- |
| From | ``` var uuidArray: UnsafePointer<dyld_uuid_info> ``` |
| To | ``` var uuidArray: UnsafePointer<dyld_uuid_info>! ``` |

Modified dyld_image_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dyld_image_info {     var imageLoadAddress: UnsafePointer<mach_header>     var imageFilePath: UnsafePointer<Int8>     var imageFileModDate: UInt     init()     init(imageLoadAddress imageLoadAddress: UnsafePointer<mach_header>, imageFilePath imageFilePath: UnsafePointer<Int8>, imageFileModDate imageFileModDate: UInt) } ``` |
| To | ``` struct dyld_image_info {     var imageLoadAddress: UnsafePointer<mach_header>!     var imageFilePath: UnsafePointer<Int8>!     var imageFileModDate: UInt     init()     init(imageLoadAddress imageLoadAddress: UnsafePointer<mach_header>!, imageFilePath imageFilePath: UnsafePointer<Int8>!, imageFileModDate imageFileModDate: UInt) } ``` |

Modified dyld_image_info.imageFilePath

|  | Declaration |
| --- | --- |
| From | ``` var imageFilePath: UnsafePointer<Int8> ``` |
| To | ``` var imageFilePath: UnsafePointer<Int8>! ``` |

Modified dyld_image_info.imageLoadAddress

|  | Declaration |
| --- | --- |
| From | ``` var imageLoadAddress: UnsafePointer<mach_header> ``` |
| To | ``` var imageLoadAddress: UnsafePointer<mach_header>! ``` |

Modified dyld_uuid_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dyld_uuid_info {     var imageLoadAddress: UnsafePointer<mach_header>     var imageUUID: uuid_t     init()     init(imageLoadAddress imageLoadAddress: UnsafePointer<mach_header>, imageUUID imageUUID: uuid_t) } ``` |
| To | ``` struct dyld_uuid_info {     var imageLoadAddress: UnsafePointer<mach_header>!     var imageUUID: Darwin.uuid_t     init()     init(imageLoadAddress imageLoadAddress: UnsafePointer<mach_header>!, imageUUID imageUUID: Darwin.uuid_t) } ``` |

Modified dyld_uuid_info.imageLoadAddress

|  | Declaration |
| --- | --- |
| From | ``` var imageLoadAddress: UnsafePointer<mach_header> ``` |
| To | ``` var imageLoadAddress: UnsafePointer<mach_header>! ``` |

Modified dyld_uuid_info.imageUUID

|  | Declaration |
| --- | --- |
| From | ``` var imageUUID: uuid_t ``` |
| To | ``` var imageUUID: Darwin.uuid_t ``` |

Modified lc_str [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct lc_str {     var offset: UInt32     var ptr: UnsafeMutablePointer<Int8>     init(offset offset: UInt32)     init(ptr ptr: UnsafeMutablePointer<Int8>)     init() } ``` |
| To | ``` struct lc_str {     var offset: UInt32     init(offset offset: UInt32)     init() } ``` |

Modified nlist [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct nlist {     struct __Unnamed_union_n_un {         var n_name: UnsafeMutablePointer<Int8>         var n_strx: UInt32         init(n_name n_name: UnsafeMutablePointer<Int8>)         init(n_strx n_strx: UInt32)         init()     }     var n_un: nlist.__Unnamed_union_n_un     var n_type: UInt8     var n_sect: UInt8     var n_desc: Int16     var n_value: UInt32     init()     init(n_un n_un: nlist.__Unnamed_union_n_un, n_type n_type: UInt8, n_sect n_sect: UInt8, n_desc n_desc: Int16, n_value n_value: UInt32) } ``` |
| To | ``` struct nlist {     struct __Unnamed_union_n_un {         var n_strx: UInt32         init(n_strx n_strx: UInt32)         init()     }     var n_un: nlist.__Unnamed_union_n_un     var n_type: UInt8     var n_sect: UInt8     var n_desc: Int16     var n_value: UInt32     init()     init(n_un n_un: nlist.__Unnamed_union_n_un, n_type n_type: UInt8, n_sect n_sect: UInt8, n_desc n_desc: Int16, n_value n_value: UInt32) } ``` |

Modified NSLinkEditErrorHandlers [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSLinkEditErrorHandlers {     var undefined: ((UnsafePointer<Int8>) -> Void)!     var multiple: ((NSSymbol, NSModule, NSModule) -> NSModule)!     var linkEdit: ((NSLinkEditErrors, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Void)!     init()     init(undefined undefined: ((UnsafePointer<Int8>) -> Void)!, multiple multiple: ((NSSymbol, NSModule, NSModule) -> NSModule)!, linkEdit linkEdit: ((NSLinkEditErrors, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Void)!) } ``` |
| To | ``` struct NSLinkEditErrorHandlers {     var undefined: ((UnsafePointer<Int8>?) -> Swift.Void)!     var multiple: ((NSSymbol?, NSModule?, NSModule?) -> NSModule?)!     var linkEdit: ((NSLinkEditErrors, Int32, UnsafePointer<Int8>?, UnsafePointer<Int8>?) -> Swift.Void)!     init()     init(undefined undefined: (@escaping (UnsafePointer<Int8>?) -> Swift.Void)!, multiple multiple: (@escaping (NSSymbol?, NSModule?, NSModule?) -> NSModule?)!, linkEdit linkEdit: (@escaping (NSLinkEditErrors, Int32, UnsafePointer<Int8>?, UnsafePointer<Int8>?) -> Swift.Void)!) } ``` |

Modified NSLinkEditErrorHandlers.linkEdit

|  | Declaration |
| --- | --- |
| From | ``` var linkEdit: ((NSLinkEditErrors, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Void)! ``` |
| To | ``` var linkEdit: ((NSLinkEditErrors, Int32, UnsafePointer<Int8>?, UnsafePointer<Int8>?) -> Swift.Void)! ``` |

Modified NSLinkEditErrorHandlers.multiple

|  | Declaration |
| --- | --- |
| From | ``` var multiple: ((NSSymbol, NSModule, NSModule) -> NSModule)! ``` |
| To | ``` var multiple: ((NSSymbol?, NSModule?, NSModule?) -> NSModule?)! ``` |

Modified NSLinkEditErrorHandlers.undefined

|  | Declaration |
| --- | --- |
| From | ``` var undefined: ((UnsafePointer<Int8>) -> Void)! ``` |
| To | ``` var undefined: ((UnsafePointer<Int8>?) -> Swift.Void)! ``` |

Modified NXArchInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NXArchInfo {     var name: UnsafePointer<Int8>     var cputype: cpu_type_t     var cpusubtype: cpu_subtype_t     var byteorder: NXByteOrder     var description: UnsafePointer<Int8>     init()     init(name name: UnsafePointer<Int8>, cputype cputype: cpu_type_t, cpusubtype cpusubtype: cpu_subtype_t, byteorder byteorder: NXByteOrder, description description: UnsafePointer<Int8>) } ``` |
| To | ``` struct NXArchInfo {     var name: UnsafePointer<Int8>!     var cputype: cpu_type_t     var cpusubtype: cpu_subtype_t     var byteorder: NXByteOrder     var description: UnsafePointer<Int8>!     init()     init(name name: UnsafePointer<Int8>!, cputype cputype: cpu_type_t, cpusubtype cpusubtype: cpu_subtype_t, byteorder byteorder: NXByteOrder, description description: UnsafePointer<Int8>!) } ``` |

Modified NXArchInfo.description

|  | Declaration |
| --- | --- |
| From | ``` var description: UnsafePointer<Int8> ``` |
| To | ``` var description: UnsafePointer<Int8>! ``` |

Modified NXArchInfo.name

|  | Declaration |
| --- | --- |
| From | ``` var name: UnsafePointer<Int8> ``` |
| To | ``` var name: UnsafePointer<Int8>! ``` |

Modified ranlib [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct ranlib {     struct __Unnamed_union_ran_un {         var ran_strx: UInt32         var ran_name: UnsafeMutablePointer<Int8>         init(ran_strx ran_strx: UInt32)         init(ran_name ran_name: UnsafeMutablePointer<Int8>)         init()     }     var ran_un: ranlib.__Unnamed_union_ran_un     var ran_off: UInt32     init()     init(ran_un ran_un: ranlib.__Unnamed_union_ran_un, ran_off ran_off: UInt32) } ``` |
| To | ``` struct ranlib {     struct __Unnamed_union_ran_un {         var ran_strx: UInt32         init(ran_strx ran_strx: UInt32)         init()     }     var ran_un: ranlib.__Unnamed_union_ran_un     var ran_off: UInt32     init()     init(ran_un ran_un: ranlib.__Unnamed_union_ran_un, ran_off ran_off: UInt32) } ``` |

Modified tlv_descriptor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tlv_descriptor {     var thunk: ((UnsafeMutablePointer<tlv_descriptor>) -> UnsafeMutablePointer<Void>)!     var key: UInt     var offset: UInt     init()     init(thunk thunk: ((UnsafeMutablePointer<tlv_descriptor>) -> UnsafeMutablePointer<Void>)!, key key: UInt, offset offset: UInt) } ``` |
| To | ``` struct tlv_descriptor {     var thunk: ((UnsafeMutablePointer<tlv_descriptor>?) -> UnsafeMutableRawPointer?)!     var key: UInt     var offset: UInt     init()     init(thunk thunk: (@escaping (UnsafeMutablePointer<tlv_descriptor>?) -> UnsafeMutableRawPointer?)!, key key: UInt, offset offset: UInt) } ``` |

Modified tlv_descriptor.thunk

|  | Declaration |
| --- | --- |
| From | ``` var thunk: ((UnsafeMutablePointer<tlv_descriptor>) -> UnsafeMutablePointer<Void>)! ``` |
| To | ``` var thunk: ((UnsafeMutablePointer<tlv_descriptor>?) -> UnsafeMutableRawPointer?)! ``` |

Modified dyld_image_notifier

|  | Declaration |
| --- | --- |
| From | ``` typealias dyld_image_notifier = (dyld_image_mode, UInt32, UnsafePointer<dyld_image_info>) -> Void ``` |
| To | ``` typealias dyld_image_notifier = (dyld_image_mode, UInt32, UnsafePointer<dyld_image_info>?) -> Swift.Void ``` |

Modified getsectbyname(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> UnsafePointer<section_64>!

|  | Declaration |
| --- | --- |
| From | ``` func getsectbyname(_ segname: UnsafePointer<Int8>, _ sectname: UnsafePointer<Int8>) -> UnsafePointer<section> ``` |
| To | ``` func getsectbyname(_ segname: UnsafePointer<Int8>!, _ sectname: UnsafePointer<Int8>!) -> UnsafePointer<section_64>! ``` |

Modified getsectbynamefromheader(_: UnsafePointer<mach_header>!, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> UnsafePointer<section>!

|  | Declaration |
| --- | --- |
| From | ``` func getsectbynamefromheader(_ mhp: UnsafePointer<mach_header>, _ segname: UnsafePointer<Int8>, _ sectname: UnsafePointer<Int8>) -> UnsafePointer<section> ``` |
| To | ``` func getsectbynamefromheader(_ mhp: UnsafePointer<mach_header>!, _ segname: UnsafePointer<Int8>!, _ sectname: UnsafePointer<Int8>!) -> UnsafePointer<section>! ``` |

Modified getsectbynamefromheader_64(_: UnsafePointer<mach_header_64>!, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!) -> UnsafePointer<section_64>!

|  | Declaration |
| --- | --- |
| From | ``` func getsectbynamefromheader_64(_ mhp: UnsafePointer<mach_header_64>, _ segname: UnsafePointer<Int8>, _ sectname: UnsafePointer<Int8>) -> UnsafePointer<section_64> ``` |
| To | ``` func getsectbynamefromheader_64(_ mhp: UnsafePointer<mach_header_64>!, _ segname: UnsafePointer<Int8>!, _ sectname: UnsafePointer<Int8>!) -> UnsafePointer<section_64>! ``` |

Modified getsectbynamefromheaderwithswap(_: UnsafeMutablePointer<mach_header>!, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int32) -> UnsafePointer<section>!

|  | Declaration |
| --- | --- |
| From | ``` func getsectbynamefromheaderwithswap(_ mhp: UnsafeMutablePointer<mach_header>, _ segname: UnsafePointer<Int8>, _ sectname: UnsafePointer<Int8>, _ fSwap: Int32) -> UnsafePointer<section> ``` |
| To | ``` func getsectbynamefromheaderwithswap(_ mhp: UnsafeMutablePointer<mach_header>!, _ segname: UnsafePointer<Int8>!, _ sectname: UnsafePointer<Int8>!, _ fSwap: Int32) -> UnsafePointer<section>! ``` |

Modified getsectbynamefromheaderwithswap_64(_: UnsafeMutablePointer<mach_header_64>!, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: Int32) -> UnsafePointer<section>!

|  | Declaration |
| --- | --- |
| From | ``` func getsectbynamefromheaderwithswap_64(_ mhp: UnsafeMutablePointer<mach_header_64>, _ segname: UnsafePointer<Int8>, _ sectname: UnsafePointer<Int8>, _ fSwap: Int32) -> UnsafePointer<section> ``` |
| To | ``` func getsectbynamefromheaderwithswap_64(_ mhp: UnsafeMutablePointer<mach_header_64>!, _ segname: UnsafePointer<Int8>!, _ sectname: UnsafePointer<Int8>!, _ fSwap: Int32) -> UnsafePointer<section>! ``` |

Modified getsectdata(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UInt>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func getsectdata(_ segname: UnsafePointer<Int8>, _ sectname: UnsafePointer<Int8>, _ size: UnsafeMutablePointer<UInt>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func getsectdata(_ segname: UnsafePointer<Int8>!, _ sectname: UnsafePointer<Int8>!, _ size: UnsafeMutablePointer<UInt>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified getsectdatafromFramework(_: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UInt>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func getsectdatafromFramework(_ FrameworkName: UnsafePointer<Int8>, _ segname: UnsafePointer<Int8>, _ sectname: UnsafePointer<Int8>, _ size: UnsafeMutablePointer<UInt>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func getsectdatafromFramework(_ FrameworkName: UnsafePointer<Int8>!, _ segname: UnsafePointer<Int8>!, _ sectname: UnsafePointer<Int8>!, _ size: UnsafeMutablePointer<UInt>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified getsectdatafromheader(_: UnsafePointer<mach_header>!, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func getsectdatafromheader(_ mhp: UnsafePointer<mach_header>, _ segname: UnsafePointer<Int8>, _ sectname: UnsafePointer<Int8>, _ size: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func getsectdatafromheader(_ mhp: UnsafePointer<mach_header>!, _ segname: UnsafePointer<Int8>!, _ sectname: UnsafePointer<Int8>!, _ size: UnsafeMutablePointer<UInt32>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified getsectdatafromheader_64(_: UnsafePointer<mach_header_64>!, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UInt64>!) -> UnsafeMutablePointer<Int8>!

|  | Declaration |
| --- | --- |
| From | ``` func getsectdatafromheader_64(_ mhp: UnsafePointer<mach_header_64>, _ segname: UnsafePointer<Int8>, _ sectname: UnsafePointer<Int8>, _ size: UnsafeMutablePointer<UInt64>) -> UnsafeMutablePointer<Int8> ``` |
| To | ``` func getsectdatafromheader_64(_ mhp: UnsafePointer<mach_header_64>!, _ segname: UnsafePointer<Int8>!, _ sectname: UnsafePointer<Int8>!, _ size: UnsafeMutablePointer<UInt64>!) -> UnsafeMutablePointer<Int8>! ``` |

Modified getsectiondata(_: UnsafePointer<mach_header_64>!, _: UnsafePointer<Int8>!, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UInt>!) -> UnsafeMutablePointer<UInt8>!

|  | Declaration |
| --- | --- |
| From | ``` func getsectiondata(_ mhp: UnsafePointer<mach_header>, _ segname: UnsafePointer<Int8>, _ sectname: UnsafePointer<Int8>, _ size: UnsafeMutablePointer<UInt>) -> UnsafeMutablePointer<UInt8> ``` |
| To | ``` func getsectiondata(_ mhp: UnsafePointer<mach_header_64>!, _ segname: UnsafePointer<Int8>!, _ sectname: UnsafePointer<Int8>!, _ size: UnsafeMutablePointer<UInt>!) -> UnsafeMutablePointer<UInt8>! ``` |

Modified getsegbyname(_: UnsafePointer<Int8>!) -> UnsafePointer<segment_command_64>!

|  | Declaration |
| --- | --- |
| From | ``` func getsegbyname(_ segname: UnsafePointer<Int8>) -> UnsafePointer<segment_command> ``` |
| To | ``` func getsegbyname(_ segname: UnsafePointer<Int8>!) -> UnsafePointer<segment_command_64>! ``` |

Modified getsegmentdata(_: UnsafePointer<mach_header_64>!, _: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UInt>!) -> UnsafeMutablePointer<UInt8>!

|  | Declaration |
| --- | --- |
| From | ``` func getsegmentdata(_ mhp: UnsafePointer<mach_header>, _ segname: UnsafePointer<Int8>, _ size: UnsafeMutablePointer<UInt>) -> UnsafeMutablePointer<UInt8> ``` |
| To | ``` func getsegmentdata(_ mhp: UnsafePointer<mach_header_64>!, _ segname: UnsafePointer<Int8>!, _ size: UnsafeMutablePointer<UInt>!) -> UnsafeMutablePointer<UInt8>! ``` |

Modified nlist(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<nlist>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func nlist(_ filename: UnsafePointer<Int8>, _ list: UnsafeMutablePointer<nlist>) -> Int32 ``` |
| To | ``` func nlist(_ filename: UnsafePointer<Int8>!, _ list: UnsafeMutablePointer<nlist>!) -> Int32 ``` |

Modified NSModule

|  | Declaration |
| --- | --- |
| From | ``` typealias NSModule = COpaquePointer ``` |
| To | ``` typealias NSModule = OpaquePointer ``` |

Modified NSObjectFileImage

|  | Declaration |
| --- | --- |
| From | ``` typealias NSObjectFileImage = COpaquePointer ``` |
| To | ``` typealias NSObjectFileImage = OpaquePointer ``` |

Modified NSSymbol

|  | Declaration |
| --- | --- |
| From | ``` typealias NSSymbol = COpaquePointer ``` |
| To | ``` typealias NSSymbol = OpaquePointer ``` |

Modified NSVersionOfLinkTimeLibrary(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func NSVersionOfLinkTimeLibrary(_ libraryName: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func NSVersionOfLinkTimeLibrary(_ libraryName: UnsafePointer<Int8>!) -> Int32 ``` |

Modified NSVersionOfRunTimeLibrary(_: UnsafePointer<Int8>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func NSVersionOfRunTimeLibrary(_ libraryName: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func NSVersionOfRunTimeLibrary(_ libraryName: UnsafePointer<Int8>!) -> Int32 ``` |

Modified NXFindBestFatArch(_: cpu_type_t, _: cpu_subtype_t, _: UnsafeMutablePointer<fat_arch>!, _: UInt32) -> UnsafeMutablePointer<fat_arch>!

|  | Declaration |
| --- | --- |
| From | ``` func NXFindBestFatArch(_ cputype: cpu_type_t, _ cpusubtype: cpu_subtype_t, _ fat_archs: UnsafeMutablePointer<fat_arch>, _ nfat_archs: UInt32) -> UnsafeMutablePointer<fat_arch> ``` |
| To | ``` func NXFindBestFatArch(_ cputype: cpu_type_t, _ cpusubtype: cpu_subtype_t, _ fat_archs: UnsafeMutablePointer<fat_arch>!, _ nfat_archs: UInt32) -> UnsafeMutablePointer<fat_arch>! ``` |

Modified NXGetAllArchInfos() -> UnsafePointer<NXArchInfo>!

|  | Declaration |
| --- | --- |
| From | ``` func NXGetAllArchInfos() -> UnsafePointer<NXArchInfo> ``` |
| To | ``` func NXGetAllArchInfos() -> UnsafePointer<NXArchInfo>! ``` |

Modified NXGetArchInfoFromCpuType(_: cpu_type_t, _: cpu_subtype_t) -> UnsafePointer<NXArchInfo>!

|  | Declaration |
| --- | --- |
| From | ``` func NXGetArchInfoFromCpuType(_ cputype: cpu_type_t, _ cpusubtype: cpu_subtype_t) -> UnsafePointer<NXArchInfo> ``` |
| To | ``` func NXGetArchInfoFromCpuType(_ cputype: cpu_type_t, _ cpusubtype: cpu_subtype_t) -> UnsafePointer<NXArchInfo>! ``` |

Modified NXGetArchInfoFromName(_: UnsafePointer<Int8>!) -> UnsafePointer<NXArchInfo>!

|  | Declaration |
| --- | --- |
| From | ``` func NXGetArchInfoFromName(_ name: UnsafePointer<Int8>) -> UnsafePointer<NXArchInfo> ``` |
| To | ``` func NXGetArchInfoFromName(_ name: UnsafePointer<Int8>!) -> UnsafePointer<NXArchInfo>! ``` |

Modified NXGetLocalArchInfo() -> UnsafePointer<NXArchInfo>!

|  | Declaration |
| --- | --- |
| From | ``` func NXGetLocalArchInfo() -> UnsafePointer<NXArchInfo> ``` |
| To | ``` func NXGetLocalArchInfo() -> UnsafePointer<NXArchInfo>! ``` |

Modified swap_dyld_info_command(_: UnsafeMutablePointer<dyld_info_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_dyld_info_command(_ ed: UnsafeMutablePointer<dyld_info_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_dyld_info_command(_ ed: UnsafeMutablePointer<dyld_info_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_dylib_command(_: UnsafeMutablePointer<dylib_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_dylib_command(_ dl: UnsafeMutablePointer<dylib_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_dylib_command(_ dl: UnsafeMutablePointer<dylib_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_dylib_module(_: UnsafeMutablePointer<dylib_module>!, _: UInt32, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_dylib_module(_ mods: UnsafeMutablePointer<dylib_module>, _ nmods: UInt32, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_dylib_module(_ mods: UnsafeMutablePointer<dylib_module>!, _ nmods: UInt32, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_dylib_module_64(_: UnsafeMutablePointer<dylib_module_64>!, _: UInt32, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_dylib_module_64(_ mods: UnsafeMutablePointer<dylib_module_64>, _ nmods: UInt32, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_dylib_module_64(_ mods: UnsafeMutablePointer<dylib_module_64>!, _ nmods: UInt32, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_dylib_reference(_: UnsafeMutablePointer<dylib_reference>!, _: UInt32, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_dylib_reference(_ refs: UnsafeMutablePointer<dylib_reference>, _ nrefs: UInt32, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_dylib_reference(_ refs: UnsafeMutablePointer<dylib_reference>!, _ nrefs: UInt32, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_dylib_table_of_contents(_: UnsafeMutablePointer<dylib_table_of_contents>!, _: UInt32, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_dylib_table_of_contents(_ tocs: UnsafeMutablePointer<dylib_table_of_contents>, _ ntocs: UInt32, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_dylib_table_of_contents(_ tocs: UnsafeMutablePointer<dylib_table_of_contents>!, _ ntocs: UInt32, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_dylinker_command(_: UnsafeMutablePointer<dylinker_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_dylinker_command(_ dyld: UnsafeMutablePointer<dylinker_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_dylinker_command(_ dyld: UnsafeMutablePointer<dylinker_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_dysymtab_command(_: UnsafeMutablePointer<dysymtab_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_dysymtab_command(_ dyst: UnsafeMutablePointer<dysymtab_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_dysymtab_command(_ dyst: UnsafeMutablePointer<dysymtab_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_encryption_command(_: UnsafeMutablePointer<encryption_info_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_encryption_command(_ ec: UnsafeMutablePointer<encryption_info_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_encryption_command(_ ec: UnsafeMutablePointer<encryption_info_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_encryption_command_64(_: UnsafeMutablePointer<encryption_info_command_64>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_encryption_command_64(_ ec: UnsafeMutablePointer<encryption_info_command_64>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_encryption_command_64(_ ec: UnsafeMutablePointer<encryption_info_command_64>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_entry_point_command(_: UnsafeMutablePointer<entry_point_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_entry_point_command(_ ep: UnsafeMutablePointer<entry_point_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_entry_point_command(_ ep: UnsafeMutablePointer<entry_point_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_fat_arch(_: UnsafeMutablePointer<fat_arch>!, _: UInt32, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_fat_arch(_ fat_archs: UnsafeMutablePointer<fat_arch>, _ nfat_arch: UInt32, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_fat_arch(_ fat_archs: UnsafeMutablePointer<fat_arch>!, _ nfat_arch: UInt32, _ target_byte_order: NXByteOrder) ``` |

Modified swap_fat_header(_: UnsafeMutablePointer<fat_header>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_fat_header(_ fat_header: UnsafeMutablePointer<fat_header>, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_fat_header(_ fat_header: UnsafeMutablePointer<fat_header>!, _ target_byte_order: NXByteOrder) ``` |

Modified swap_fvmfile_command(_: UnsafeMutablePointer<fvmfile_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_fvmfile_command(_ ff: UnsafeMutablePointer<fvmfile_command>, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_fvmfile_command(_ ff: UnsafeMutablePointer<fvmfile_command>!, _ target_byte_order: NXByteOrder) ``` |

Modified swap_fvmlib_command(_: UnsafeMutablePointer<fvmlib_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_fvmlib_command(_ fl: UnsafeMutablePointer<fvmlib_command>, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_fvmlib_command(_ fl: UnsafeMutablePointer<fvmlib_command>!, _ target_byte_order: NXByteOrder) ``` |

Modified swap_ident_command(_: UnsafeMutablePointer<ident_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_ident_command(_ ident: UnsafeMutablePointer<ident_command>, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_ident_command(_ ident: UnsafeMutablePointer<ident_command>!, _ target_byte_order: NXByteOrder) ``` |

Modified swap_indirect_symbols(_: UnsafeMutablePointer<UInt32>!, _: UInt32, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_indirect_symbols(_ indirect_symbols: UnsafeMutablePointer<UInt32>, _ nindirect_symbols: UInt32, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_indirect_symbols(_ indirect_symbols: UnsafeMutablePointer<UInt32>!, _ nindirect_symbols: UInt32, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_linkedit_data_command(_: UnsafeMutablePointer<linkedit_data_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_linkedit_data_command(_ ld: UnsafeMutablePointer<linkedit_data_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_linkedit_data_command(_ ld: UnsafeMutablePointer<linkedit_data_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_linker_option_command(_: UnsafeMutablePointer<linker_option_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_linker_option_command(_ lo: UnsafeMutablePointer<linker_option_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_linker_option_command(_ lo: UnsafeMutablePointer<linker_option_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_load_command(_: UnsafeMutablePointer<load_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_load_command(_ lc: UnsafeMutablePointer<load_command>, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_load_command(_ lc: UnsafeMutablePointer<load_command>!, _ target_byte_order: NXByteOrder) ``` |

Modified swap_mach_header(_: UnsafeMutablePointer<mach_header>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_mach_header(_ mh: UnsafeMutablePointer<mach_header>, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_mach_header(_ mh: UnsafeMutablePointer<mach_header>!, _ target_byte_order: NXByteOrder) ``` |

Modified swap_mach_header_64(_: UnsafeMutablePointer<mach_header_64>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_mach_header_64(_ mh: UnsafeMutablePointer<mach_header_64>, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_mach_header_64(_ mh: UnsafeMutablePointer<mach_header_64>!, _ target_byte_order: NXByteOrder) ``` |

Modified swap_nlist(_: UnsafeMutablePointer<nlist>!, _: UInt32, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_nlist(_ symbols: UnsafeMutablePointer<nlist>, _ nsymbols: UInt32, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_nlist(_ symbols: UnsafeMutablePointer<nlist>!, _ nsymbols: UInt32, _ target_byte_order: NXByteOrder) ``` |

Modified swap_nlist_64(_: UnsafeMutablePointer<nlist_64>!, _: UInt32, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_nlist_64(_ symbols: UnsafeMutablePointer<nlist_64>, _ nsymbols: UInt32, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_nlist_64(_ symbols: UnsafeMutablePointer<nlist_64>!, _ nsymbols: UInt32, _ target_byte_order: NXByteOrder) ``` |

Modified swap_prebind_cksum_command(_: UnsafeMutablePointer<prebind_cksum_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_prebind_cksum_command(_ cksum_cmd: UnsafeMutablePointer<prebind_cksum_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_prebind_cksum_command(_ cksum_cmd: UnsafeMutablePointer<prebind_cksum_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_prebound_dylib_command(_: UnsafeMutablePointer<prebound_dylib_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_prebound_dylib_command(_ pbdylib: UnsafeMutablePointer<prebound_dylib_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_prebound_dylib_command(_ pbdylib: UnsafeMutablePointer<prebound_dylib_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_ranlib(_: UnsafeMutablePointer<ranlib>!, _: UInt32, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_ranlib(_ ranlibs: UnsafeMutablePointer<ranlib>, _ nranlibs: UInt32, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_ranlib(_ ranlibs: UnsafeMutablePointer<ranlib>!, _ nranlibs: UInt32, _ target_byte_order: NXByteOrder) ``` |

Modified swap_relocation_info(_: UnsafeMutablePointer<relocation_info>!, _: UInt32, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_relocation_info(_ relocs: UnsafeMutablePointer<relocation_info>, _ nrelocs: UInt32, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_relocation_info(_ relocs: UnsafeMutablePointer<relocation_info>!, _ nrelocs: UInt32, _ target_byte_order: NXByteOrder) ``` |

Modified swap_routines_command(_: UnsafeMutablePointer<routines_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_routines_command(_ r_cmd: UnsafeMutablePointer<routines_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_routines_command(_ r_cmd: UnsafeMutablePointer<routines_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_routines_command_64(_: UnsafeMutablePointer<routines_command_64>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_routines_command_64(_ r_cmd: UnsafeMutablePointer<routines_command_64>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_routines_command_64(_ r_cmd: UnsafeMutablePointer<routines_command_64>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_rpath_command(_: UnsafeMutablePointer<rpath_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_rpath_command(_ rpath_cmd: UnsafeMutablePointer<rpath_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_rpath_command(_ rpath_cmd: UnsafeMutablePointer<rpath_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_section(_: UnsafeMutablePointer<section>!, _: UInt32, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_section(_ s: UnsafeMutablePointer<section>, _ nsects: UInt32, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_section(_ s: UnsafeMutablePointer<section>!, _ nsects: UInt32, _ target_byte_order: NXByteOrder) ``` |

Modified swap_section_64(_: UnsafeMutablePointer<section_64>!, _: UInt32, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_section_64(_ s: UnsafeMutablePointer<section_64>, _ nsects: UInt32, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_section_64(_ s: UnsafeMutablePointer<section_64>!, _ nsects: UInt32, _ target_byte_order: NXByteOrder) ``` |

Modified swap_segment_command(_: UnsafeMutablePointer<segment_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_segment_command(_ sg: UnsafeMutablePointer<segment_command>, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_segment_command(_ sg: UnsafeMutablePointer<segment_command>!, _ target_byte_order: NXByteOrder) ``` |

Modified swap_segment_command_64(_: UnsafeMutablePointer<segment_command_64>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_segment_command_64(_ sg: UnsafeMutablePointer<segment_command_64>, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_segment_command_64(_ sg: UnsafeMutablePointer<segment_command_64>!, _ target_byte_order: NXByteOrder) ``` |

Modified swap_source_version_command(_: UnsafeMutablePointer<source_version_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_source_version_command(_ sv: UnsafeMutablePointer<source_version_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_source_version_command(_ sv: UnsafeMutablePointer<source_version_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_sub_client_command(_: UnsafeMutablePointer<sub_client_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_sub_client_command(_ csub: UnsafeMutablePointer<sub_client_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_sub_client_command(_ csub: UnsafeMutablePointer<sub_client_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_sub_framework_command(_: UnsafeMutablePointer<sub_framework_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_sub_framework_command(_ sub: UnsafeMutablePointer<sub_framework_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_sub_framework_command(_ sub: UnsafeMutablePointer<sub_framework_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_sub_library_command(_: UnsafeMutablePointer<sub_library_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_sub_library_command(_ lsub: UnsafeMutablePointer<sub_library_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_sub_library_command(_ lsub: UnsafeMutablePointer<sub_library_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_sub_umbrella_command(_: UnsafeMutablePointer<sub_umbrella_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_sub_umbrella_command(_ usub: UnsafeMutablePointer<sub_umbrella_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_sub_umbrella_command(_ usub: UnsafeMutablePointer<sub_umbrella_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_symseg_command(_: UnsafeMutablePointer<symseg_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_symseg_command(_ ss: UnsafeMutablePointer<symseg_command>, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_symseg_command(_ ss: UnsafeMutablePointer<symseg_command>!, _ target_byte_order: NXByteOrder) ``` |

Modified swap_symtab_command(_: UnsafeMutablePointer<symtab_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_symtab_command(_ st: UnsafeMutablePointer<symtab_command>, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_symtab_command(_ st: UnsafeMutablePointer<symtab_command>!, _ target_byte_order: NXByteOrder) ``` |

Modified swap_thread_command(_: UnsafeMutablePointer<thread_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_thread_command(_ ut: UnsafeMutablePointer<thread_command>, _ target_byte_order: NXByteOrder) ``` |
| To | ``` func swap_thread_command(_ ut: UnsafeMutablePointer<thread_command>!, _ target_byte_order: NXByteOrder) ``` |

Modified swap_twolevel_hint(_: UnsafeMutablePointer<twolevel_hint>!, _: UInt32, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_twolevel_hint(_ hints: UnsafeMutablePointer<twolevel_hint>, _ nhints: UInt32, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_twolevel_hint(_ hints: UnsafeMutablePointer<twolevel_hint>!, _ nhints: UInt32, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_twolevel_hints_command(_: UnsafeMutablePointer<twolevel_hints_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_twolevel_hints_command(_ hints_cmd: UnsafeMutablePointer<twolevel_hints_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_twolevel_hints_command(_ hints_cmd: UnsafeMutablePointer<twolevel_hints_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_uuid_command(_: UnsafeMutablePointer<uuid_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_uuid_command(_ uuid_cmd: UnsafeMutablePointer<uuid_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_uuid_command(_ uuid_cmd: UnsafeMutablePointer<uuid_command>!, _ target_byte_sex: NXByteOrder) ``` |

Modified swap_version_min_command(_: UnsafeMutablePointer<version_min_command>!, _: NXByteOrder)

|  | Declaration |
| --- | --- |
| From | ``` func swap_version_min_command(_ ver_cmd: UnsafeMutablePointer<version_min_command>, _ target_byte_sex: NXByteOrder) ``` |
| To | ``` func swap_version_min_command(_ ver_cmd: UnsafeMutablePointer<version_min_command>!, _ target_byte_sex: NXByteOrder) ``` |

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
