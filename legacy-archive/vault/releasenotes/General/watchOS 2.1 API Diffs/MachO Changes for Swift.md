---
title: watchOS 2.1 API Diffs
apple_id: TP40016636
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS21APIDiffs/Swift/MachO.html
archived_at: '2026-07-18T02:58:09.009222Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.1 API Diffs](watchOS%202.0%20to%20watchOS%202.1%20API%20Differences.md)


# MachO Changes for Swift

### MachO

Added dylib_reference.flagsAdded dylib_reference.init(isym: UInt32, flags: UInt32)Added dylib_reference.isymAdded lc_str.init(offset: UInt32)Added lc_str.init(ptr: UnsafeMutablePointer<Int8>)Added lc_str.offsetAdded lc_str.ptrAdded relocation_info.init(r_address: Int32, r_symbolnum: UInt32, r_pcrel: UInt32, r_length: UInt32, r_extern: UInt32, r_type: UInt32)Added relocation_info.r_externAdded relocation_info.r_lengthAdded relocation_info.r_pcrelAdded relocation_info.r_symbolnumAdded relocation_info.r_typeAdded scattered_relocation_info.init(r_address: UInt32, r_type: UInt32, r_length: UInt32, r_pcrel: UInt32, r_scattered: UInt32, r_value: Int32)Added scattered_relocation_info.r_addressAdded scattered_relocation_info.r_lengthAdded scattered_relocation_info.r_pcrelAdded scattered_relocation_info.r_scatteredAdded scattered_relocation_info.r_typeAdded twolevel_hint.init(isub_image: UInt32, itoc: UInt32)Added twolevel_hint.isub_imageAdded twolevel_hint.itocAdded LC_VERSION_MIN_TVOSModified DYLD_BOOL [enum]

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified dyld_image_mode [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct dyld_image_mode : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct dyld_image_mode : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified dylib_reference [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct dylib_reference {     init() } ``` |
| To | ``` struct dylib_reference {     var isym: UInt32     var flags: UInt32     init()     init(isym isym: UInt32, flags flags: UInt32) } ``` |

Modified lc_str [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct lc_str {     init() } ``` |
| To | ``` struct lc_str {     var offset: UInt32     var ptr: UnsafeMutablePointer<Int8>     init(offset offset: UInt32)     init(ptr ptr: UnsafeMutablePointer<Int8>)     init() } ``` |

Modified NSLinkEditErrors [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSLinkEditErrors : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct NSLinkEditErrors : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified NSObjectFileImageReturnCode [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSObjectFileImageReturnCode : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct NSObjectFileImageReturnCode : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified NSOtherErrorNumbers [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct NSOtherErrorNumbers : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct NSOtherErrorNumbers : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified reloc_type_generic [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct reloc_type_generic : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct reloc_type_generic : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified relocation_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct relocation_info {     var r_address: Int32     init() } ``` |
| To | ``` struct relocation_info {     var r_address: Int32     var r_symbolnum: UInt32     var r_pcrel: UInt32     var r_length: UInt32     var r_extern: UInt32     var r_type: UInt32     init()     init(r_address r_address: Int32, r_symbolnum r_symbolnum: UInt32, r_pcrel r_pcrel: UInt32, r_length r_length: UInt32, r_extern r_extern: UInt32, r_type r_type: UInt32) } ``` |

Modified scattered_relocation_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct scattered_relocation_info {     var r_value: Int32     init() } ``` |
| To | ``` struct scattered_relocation_info {     var r_address: UInt32     var r_type: UInt32     var r_length: UInt32     var r_pcrel: UInt32     var r_scattered: UInt32     var r_value: Int32     init()     init(r_address r_address: UInt32, r_type r_type: UInt32, r_length r_length: UInt32, r_pcrel r_pcrel: UInt32, r_scattered r_scattered: UInt32, r_value r_value: Int32) } ``` |

Modified twolevel_hint [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct twolevel_hint {     init() } ``` |
| To | ``` struct twolevel_hint {     var isub_image: UInt32     var itoc: UInt32     init()     init(isub_image isub_image: UInt32, itoc itoc: UInt32) } ``` |

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
