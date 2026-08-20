---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/Accelerate.html
archived_at: '2026-07-18T02:57:05.776309Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# Accelerate Changes for Swift

### Accelerate

Modified CBLAS_DIAG [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CBLAS_DIAG : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct CBLAS_DIAG : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified CBLAS_ORDER [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CBLAS_ORDER : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct CBLAS_ORDER : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified CBLAS_SIDE [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CBLAS_SIDE : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct CBLAS_SIDE : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified CBLAS_TRANSPOSE [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CBLAS_TRANSPOSE : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct CBLAS_TRANSPOSE : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified CBLAS_UPLO [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CBLAS_UPLO : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct CBLAS_UPLO : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified [sparse_matrix_property [struct]](https://developer.apple.com/documentation/accelerate/sparse_matrix_property)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct sparse_matrix_property : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct sparse_matrix_property : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified [sparse_norm [struct]](https://developer.apple.com/documentation/accelerate/sparse_norm)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct sparse_norm : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct sparse_norm : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified [sparse_status [struct]](https://developer.apple.com/documentation/accelerate/sparse_status)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct sparse_status : RawRepresentable {     init(_ rawValue: Int32)     init(rawValue rawValue: Int32)     var rawValue: Int32 } ``` | RawRepresentable |
| To | ``` struct sparse_status : RawRepresentable, Equatable {     init(_ rawValue: Int32)     init(rawValue rawValue: Int32)     var rawValue: Int32 } ``` | Equatable, RawRepresentable |

Modified vDSP_DCT_Type [enum]

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [vDSP_DFT_Direction [enum]](https://developer.apple.com/documentation/accelerate/vdsp_dft_direction)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [vImage_InterpolationMethod [struct]](https://developer.apple.com/documentation/accelerate/vimage_interpolationmethod)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct vImage_InterpolationMethod : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct vImage_InterpolationMethod : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified [vImageARGBType [struct]](https://developer.apple.com/documentation/accelerate/vimageargbtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct vImageARGBType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct vImageARGBType : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified [vImageMDTableUsageHint [struct]](https://developer.apple.com/documentation/accelerate/vimagemdtableusagehint)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct vImageMDTableUsageHint : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct vImageMDTableUsageHint : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified [vImageYpCbCrType [struct]](https://developer.apple.com/documentation/accelerate/vimageypcbcrtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct vImageYpCbCrType : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct vImageYpCbCrType : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

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
