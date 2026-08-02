---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/MachO.html
archived_at: '2026-07-18T02:53:38.561346Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# MachO Changes for Swift

### MachO

Removed dyld_all_image_infos.init(version: UInt32, infoArrayCount: UInt32, infoArray: UnsafePointer<dyld_image_info>, notification: dyld_image_notifier, processDetachedFromSharedRegion: Bool, libSystemInitialized: Bool, dyldImageLoadAddress: UnsafePointer<mach_header>, jitInfo: UnsafeMutablePointer<Void>, dyldVersion: UnsafePointer<Int8>, errorMessage: UnsafePointer<Int8>, terminationFlags: UInt, coreSymbolicationShmPage: UnsafeMutablePointer<Void>, systemOrderFlag: UInt, uuidArrayCount: UInt, uuidArray: UnsafePointer<dyld_uuid_info>, dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos>, initialImageCount: UInt, errorKind: UInt, errorClientOfDylibPath: UnsafePointer<Int8>, errorTargetDylibPath: UnsafePointer<Int8>, errorSymbol: UnsafePointer<Int8>, sharedCacheSlide: UInt, sharedCacheUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), reserved: (UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt))Removed DYLD_BOOL.init(_: UInt32)Removed DYLD_BOOL.valueRemoved dyld_image_mode.valueRemoved NSLinkEditErrorHandlers.init(undefined: CFunctionPointer<((UnsafePointer<Int8>) -> Void)>, multiple: CFunctionPointer<((NSSymbol, NSModule, NSModule) -> NSModule)>, linkEdit: CFunctionPointer<((NSLinkEditErrors, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Void)>)Removed NSLinkEditErrors.valueRemoved NSObjectFileImageReturnCode.valueRemoved NSOtherErrorNumbers.valueRemoved reloc_type_generic.valueRemoved tlv_descriptor.init(thunk: CFunctionPointer<((UnsafeMutablePointer<tlv_descriptor>) -> UnsafeMutablePointer<Void>)>, key: UInt, offset: UInt)Added dyld_all_image_infos.init(version: UInt32, infoArrayCount: UInt32, infoArray: UnsafePointer<dyld_image_info>, notification: dyld_image_notifier!, processDetachedFromSharedRegion: Bool, libSystemInitialized: Bool, dyldImageLoadAddress: UnsafePointer<mach_header>, jitInfo: UnsafeMutablePointer<Void>, dyldVersion: UnsafePointer<Int8>, errorMessage: UnsafePointer<Int8>, terminationFlags: UInt, coreSymbolicationShmPage: UnsafeMutablePointer<Void>, systemOrderFlag: UInt, uuidArrayCount: UInt, uuidArray: UnsafePointer<dyld_uuid_info>, dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos>, initialImageCount: UInt, errorKind: UInt, errorClientOfDylibPath: UnsafePointer<Int8>, errorTargetDylibPath: UnsafePointer<Int8>, errorSymbol: UnsafePointer<Int8>, sharedCacheSlide: UInt, sharedCacheUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), reserved: (UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt))Added dyld_image_mode.init(rawValue: UInt32)Added dyld_image_mode.rawValueAdded NSLinkEditErrorHandlers.init(undefined: ((UnsafePointer<Int8>) -> Void)!, multiple: ((NSSymbol, NSModule, NSModule) -> NSModule)!, linkEdit: ((NSLinkEditErrors, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Void)!)Added NSLinkEditErrors.init(rawValue: UInt32)Added NSLinkEditErrors.rawValueAdded NSObjectFileImageReturnCode.init(rawValue: UInt32)Added NSObjectFileImageReturnCode.rawValueAdded NSOtherErrorNumbers.init(rawValue: UInt32)Added NSOtherErrorNumbers.rawValueAdded reloc_type_generic.init(rawValue: UInt32)Added reloc_type_generic.rawValueAdded tlv_descriptor.init(thunk: ((UnsafeMutablePointer<tlv_descriptor>) -> UnsafeMutablePointer<Void>)!, key: UInt, offset: UInt)Added LC_VERSION_MIN_WATCHOSAdded N_ASTModified dyld_all_image_infos [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dyld_all_image_infos {     var version: UInt32     var infoArrayCount: UInt32     var infoArray: UnsafePointer<dyld_image_info>     var notification: dyld_image_notifier     var processDetachedFromSharedRegion: Bool     var libSystemInitialized: Bool     var dyldImageLoadAddress: UnsafePointer<mach_header>     var jitInfo: UnsafeMutablePointer<Void>     var dyldVersion: UnsafePointer<Int8>     var errorMessage: UnsafePointer<Int8>     var terminationFlags: UInt     var coreSymbolicationShmPage: UnsafeMutablePointer<Void>     var systemOrderFlag: UInt     var uuidArrayCount: UInt     var uuidArray: UnsafePointer<dyld_uuid_info>     var dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos>     var initialImageCount: UInt     var errorKind: UInt     var errorClientOfDylibPath: UnsafePointer<Int8>     var errorTargetDylibPath: UnsafePointer<Int8>     var errorSymbol: UnsafePointer<Int8>     var sharedCacheSlide: UInt     var sharedCacheUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var reserved: (UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt)     init()     init(version version: UInt32, infoArrayCount infoArrayCount: UInt32, infoArray infoArray: UnsafePointer<dyld_image_info>, notification notification: dyld_image_notifier, processDetachedFromSharedRegion processDetachedFromSharedRegion: Bool, libSystemInitialized libSystemInitialized: Bool, dyldImageLoadAddress dyldImageLoadAddress: UnsafePointer<mach_header>, jitInfo jitInfo: UnsafeMutablePointer<Void>, dyldVersion dyldVersion: UnsafePointer<Int8>, errorMessage errorMessage: UnsafePointer<Int8>, terminationFlags terminationFlags: UInt, coreSymbolicationShmPage coreSymbolicationShmPage: UnsafeMutablePointer<Void>, systemOrderFlag systemOrderFlag: UInt, uuidArrayCount uuidArrayCount: UInt, uuidArray uuidArray: UnsafePointer<dyld_uuid_info>, dyldAllImageInfosAddress dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos>, initialImageCount initialImageCount: UInt, errorKind errorKind: UInt, errorClientOfDylibPath errorClientOfDylibPath: UnsafePointer<Int8>, errorTargetDylibPath errorTargetDylibPath: UnsafePointer<Int8>, errorSymbol errorSymbol: UnsafePointer<Int8>, sharedCacheSlide sharedCacheSlide: UInt, sharedCacheUUID sharedCacheUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), reserved reserved: (UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt)) } ``` |
| To | ``` struct dyld_all_image_infos {     var version: UInt32     var infoArrayCount: UInt32     var infoArray: UnsafePointer<dyld_image_info>     var notification: dyld_image_notifier!     var processDetachedFromSharedRegion: Bool     var libSystemInitialized: Bool     var dyldImageLoadAddress: UnsafePointer<mach_header>     var jitInfo: UnsafeMutablePointer<Void>     var dyldVersion: UnsafePointer<Int8>     var errorMessage: UnsafePointer<Int8>     var terminationFlags: UInt     var coreSymbolicationShmPage: UnsafeMutablePointer<Void>     var systemOrderFlag: UInt     var uuidArrayCount: UInt     var uuidArray: UnsafePointer<dyld_uuid_info>     var dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos>     var initialImageCount: UInt     var errorKind: UInt     var errorClientOfDylibPath: UnsafePointer<Int8>     var errorTargetDylibPath: UnsafePointer<Int8>     var errorSymbol: UnsafePointer<Int8>     var sharedCacheSlide: UInt     var sharedCacheUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     var reserved: (UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt)     init()     init(version version: UInt32, infoArrayCount infoArrayCount: UInt32, infoArray infoArray: UnsafePointer<dyld_image_info>, notification notification: dyld_image_notifier!, processDetachedFromSharedRegion processDetachedFromSharedRegion: Bool, libSystemInitialized libSystemInitialized: Bool, dyldImageLoadAddress dyldImageLoadAddress: UnsafePointer<mach_header>, jitInfo jitInfo: UnsafeMutablePointer<Void>, dyldVersion dyldVersion: UnsafePointer<Int8>, errorMessage errorMessage: UnsafePointer<Int8>, terminationFlags terminationFlags: UInt, coreSymbolicationShmPage coreSymbolicationShmPage: UnsafeMutablePointer<Void>, systemOrderFlag systemOrderFlag: UInt, uuidArrayCount uuidArrayCount: UInt, uuidArray uuidArray: UnsafePointer<dyld_uuid_info>, dyldAllImageInfosAddress dyldAllImageInfosAddress: UnsafeMutablePointer<dyld_all_image_infos>, initialImageCount initialImageCount: UInt, errorKind errorKind: UInt, errorClientOfDylibPath errorClientOfDylibPath: UnsafePointer<Int8>, errorTargetDylibPath errorTargetDylibPath: UnsafePointer<Int8>, errorSymbol errorSymbol: UnsafePointer<Int8>, sharedCacheSlide sharedCacheSlide: UInt, sharedCacheUUID sharedCacheUUID: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8), reserved reserved: (UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt, UInt)) } ``` |

Modified dyld_all_image_infos.notification

|  | Declaration |
| --- | --- |
| From | ``` var notification: dyld_image_notifier ``` |
| To | ``` var notification: dyld_image_notifier! ``` |

Modified DYLD_BOOL [enum]

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct DYLD_BOOL {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum DYLD_BOOL : UInt32 {     case FALSE     case TRUE } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | UInt32 |

Modified DYLD_BOOL.FALSE

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var FALSE: DYLD_BOOL { get } ``` | OS X 10.10 |
| To | ``` case FALSE ``` | OS X 10.11 |

Modified DYLD_BOOL.TRUE

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var TRUE: DYLD_BOOL { get } ``` | OS X 10.10 |
| To | ``` case TRUE ``` | OS X 10.11 |

Modified dyld_image_mode [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct dyld_image_mode {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct dyld_image_mode : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified NSLinkEditErrorHandlers [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct NSLinkEditErrorHandlers {     var undefined: CFunctionPointer<((UnsafePointer<Int8>) -> Void)>     var multiple: CFunctionPointer<((NSSymbol, NSModule, NSModule) -> NSModule)>     var linkEdit: CFunctionPointer<((NSLinkEditErrors, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Void)>     init()     init(undefined undefined: CFunctionPointer<((UnsafePointer<Int8>) -> Void)>, multiple multiple: CFunctionPointer<((NSSymbol, NSModule, NSModule) -> NSModule)>, linkEdit linkEdit: CFunctionPointer<((NSLinkEditErrors, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Void)>) } ``` |
| To | ``` struct NSLinkEditErrorHandlers {     var undefined: ((UnsafePointer<Int8>) -> Void)!     var multiple: ((NSSymbol, NSModule, NSModule) -> NSModule)!     var linkEdit: ((NSLinkEditErrors, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Void)!     init()     init(undefined undefined: ((UnsafePointer<Int8>) -> Void)!, multiple multiple: ((NSSymbol, NSModule, NSModule) -> NSModule)!, linkEdit linkEdit: ((NSLinkEditErrors, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Void)!) } ``` |

Modified NSLinkEditErrorHandlers.linkEdit

|  | Declaration |
| --- | --- |
| From | ``` var linkEdit: CFunctionPointer<((NSLinkEditErrors, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var linkEdit: ((NSLinkEditErrors, Int32, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Void)! ``` |

Modified NSLinkEditErrorHandlers.multiple

|  | Declaration |
| --- | --- |
| From | ``` var multiple: CFunctionPointer<((NSSymbol, NSModule, NSModule) -> NSModule)> ``` |
| To | ``` var multiple: ((NSSymbol, NSModule, NSModule) -> NSModule)! ``` |

Modified NSLinkEditErrorHandlers.undefined

|  | Declaration |
| --- | --- |
| From | ``` var undefined: CFunctionPointer<((UnsafePointer<Int8>) -> Void)> ``` |
| To | ``` var undefined: ((UnsafePointer<Int8>) -> Void)! ``` |

Modified NSLinkEditErrors [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSLinkEditErrors {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct NSLinkEditErrors : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified NSObjectFileImageReturnCode [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSObjectFileImageReturnCode {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct NSObjectFileImageReturnCode : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified NSOtherErrorNumbers [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSOtherErrorNumbers {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct NSOtherErrorNumbers : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified reloc_type_generic [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct reloc_type_generic {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct reloc_type_generic : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified tlv_descriptor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct tlv_descriptor {     var thunk: CFunctionPointer<((UnsafeMutablePointer<tlv_descriptor>) -> UnsafeMutablePointer<Void>)>     var key: UInt     var offset: UInt     init()     init(thunk thunk: CFunctionPointer<((UnsafeMutablePointer<tlv_descriptor>) -> UnsafeMutablePointer<Void>)>, key key: UInt, offset offset: UInt) } ``` |
| To | ``` struct tlv_descriptor {     var thunk: ((UnsafeMutablePointer<tlv_descriptor>) -> UnsafeMutablePointer<Void>)!     var key: UInt     var offset: UInt     init()     init(thunk thunk: ((UnsafeMutablePointer<tlv_descriptor>) -> UnsafeMutablePointer<Void>)!, key key: UInt, offset offset: UInt) } ``` |

Modified tlv_descriptor.thunk

|  | Declaration |
| --- | --- |
| From | ``` var thunk: CFunctionPointer<((UnsafeMutablePointer<tlv_descriptor>) -> UnsafeMutablePointer<Void>)> ``` |
| To | ``` var thunk: ((UnsafeMutablePointer<tlv_descriptor>) -> UnsafeMutablePointer<Void>)! ``` |

Modified dyld_image_notifier

|  | Declaration |
| --- | --- |
| From | ``` typealias dyld_image_notifier = CFunctionPointer<((dyld_image_mode, UInt32, UnsafePointer<dyld_image_info>) -> Void)> ``` |
| To | ``` typealias dyld_image_notifier = (dyld_image_mode, UInt32, UnsafePointer<dyld_image_info>) -> Void ``` |

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
