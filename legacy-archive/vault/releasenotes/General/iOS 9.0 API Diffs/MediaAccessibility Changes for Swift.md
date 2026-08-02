---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/MediaAccessibility.html
archived_at: '2026-07-18T02:56:54.412019Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# MediaAccessibility Changes for Swift

### MediaAccessibility

Modified [kMAAudibleMediaSettingsChangedNotification](https://developer.apple.com/documentation/mediaaccessibility/kmaaudiblemediasettingschangednotification)

|  | Declaration |
| --- | --- |
| From | ``` let kMAAudibleMediaSettingsChangedNotification: CFString! ``` |
| To | ``` let kMAAudibleMediaSettingsChangedNotification: CFString ``` |

Modified [kMACaptionAppearanceSettingsChangedNotification](https://developer.apple.com/documentation/mediaaccessibility/kmacaptionappearancesettingschangednotification)

|  | Declaration |
| --- | --- |
| From | ``` let kMACaptionAppearanceSettingsChangedNotification: CFString! ``` |
| To | ``` let kMACaptionAppearanceSettingsChangedNotification: CFString ``` |

Modified [MAAudibleMediaCopyPreferredCharacteristics() -> Unmanaged<CFArray>](https://developer.apple.com/documentation/mediaaccessibility/1464885-maaudiblemediacopypreferredchara)

|  | Declaration |
| --- | --- |
| From | ``` func MAAudibleMediaCopyPreferredCharacteristics() -> Unmanaged<CFArray>! ``` |
| To | ``` func MAAudibleMediaCopyPreferredCharacteristics() -> Unmanaged<CFArray> ``` |

Modified [MACaptionAppearanceAddSelectedLanguage(_: MACaptionAppearanceDomain, _: CFString) -> Bool](https://developer.apple.com/documentation/mediaaccessibility/1464869-macaptionappearanceaddselectedla)

|  | Declaration |
| --- | --- |
| From | ``` func MACaptionAppearanceAddSelectedLanguage(_ domain: MACaptionAppearanceDomain, _ language: CFString!) -> Bool ``` |
| To | ``` func MACaptionAppearanceAddSelectedLanguage(_ domain: MACaptionAppearanceDomain, _ language: CFString) -> Bool ``` |

Modified [MACaptionAppearanceCopyBackgroundColor(_: MACaptionAppearanceDomain, _: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> Unmanaged<CGColor>](https://developer.apple.com/documentation/mediaaccessibility/1464822-macaptionappearancecopybackgroun)

|  | Declaration |
| --- | --- |
| From | ``` func MACaptionAppearanceCopyBackgroundColor(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> Unmanaged<CGColor>! ``` |
| To | ``` func MACaptionAppearanceCopyBackgroundColor(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> Unmanaged<CGColor> ``` |

Modified [MACaptionAppearanceCopyFontDescriptorForStyle(_: MACaptionAppearanceDomain, _: UnsafeMutablePointer<MACaptionAppearanceBehavior>, _: MACaptionAppearanceFontStyle) -> Unmanaged<CTFontDescriptor>](https://developer.apple.com/documentation/mediaaccessibility/1464816-macaptionappearancecopyfontdescr)

|  | Declaration |
| --- | --- |
| From | ``` func MACaptionAppearanceCopyFontDescriptorForStyle(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>, _ fontStyle: MACaptionAppearanceFontStyle) -> Unmanaged<CTFontDescriptor>! ``` |
| To | ``` func MACaptionAppearanceCopyFontDescriptorForStyle(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>, _ fontStyle: MACaptionAppearanceFontStyle) -> Unmanaged<CTFontDescriptor> ``` |

Modified [MACaptionAppearanceCopyForegroundColor(_: MACaptionAppearanceDomain, _: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> Unmanaged<CGColor>](https://developer.apple.com/documentation/mediaaccessibility/1464828-macaptionappearancecopyforegroun)

|  | Declaration |
| --- | --- |
| From | ``` func MACaptionAppearanceCopyForegroundColor(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> Unmanaged<CGColor>! ``` |
| To | ``` func MACaptionAppearanceCopyForegroundColor(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> Unmanaged<CGColor> ``` |

Modified [MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics(_: MACaptionAppearanceDomain) -> Unmanaged<CFArray>](https://developer.apple.com/documentation/mediaaccessibility/1464881-macaptionappearancecopypreferred)

|  | Declaration |
| --- | --- |
| From | ``` func MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics(_ domain: MACaptionAppearanceDomain) -> Unmanaged<CFArray>! ``` |
| To | ``` func MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics(_ domain: MACaptionAppearanceDomain) -> Unmanaged<CFArray> ``` |

Modified [MACaptionAppearanceCopySelectedLanguages(_: MACaptionAppearanceDomain) -> Unmanaged<CFArray>](https://developer.apple.com/documentation/mediaaccessibility/1464855-macaptionappearancecopyselectedl)

|  | Declaration |
| --- | --- |
| From | ``` func MACaptionAppearanceCopySelectedLanguages(_ domain: MACaptionAppearanceDomain) -> Unmanaged<CFArray>! ``` |
| To | ``` func MACaptionAppearanceCopySelectedLanguages(_ domain: MACaptionAppearanceDomain) -> Unmanaged<CFArray> ``` |

Modified [MACaptionAppearanceCopyWindowColor(_: MACaptionAppearanceDomain, _: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> Unmanaged<CGColor>](https://developer.apple.com/documentation/mediaaccessibility/1464842-macaptionappearancecopywindowcol)

|  | Declaration |
| --- | --- |
| From | ``` func MACaptionAppearanceCopyWindowColor(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> Unmanaged<CGColor>! ``` |
| To | ``` func MACaptionAppearanceCopyWindowColor(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> Unmanaged<CGColor> ``` |

Modified [MAMediaCharacteristicDescribesMusicAndSoundForAccessibility](https://developer.apple.com/documentation/mediaaccessibility/mamediacharacteristicdescribesmusicandsoundforaccessibility)

|  | Declaration |
| --- | --- |
| From | ``` let MAMediaCharacteristicDescribesMusicAndSoundForAccessibility: CFString! ``` |
| To | ``` let MAMediaCharacteristicDescribesMusicAndSoundForAccessibility: CFString ``` |

Modified [MAMediaCharacteristicDescribesVideoForAccessibility](https://developer.apple.com/documentation/mediaaccessibility/mamediacharacteristicdescribesvideoforaccessibility)

|  | Declaration |
| --- | --- |
| From | ``` let MAMediaCharacteristicDescribesVideoForAccessibility: CFString! ``` |
| To | ``` let MAMediaCharacteristicDescribesVideoForAccessibility: CFString ``` |

Modified [MAMediaCharacteristicTranscribesSpokenDialogForAccessibility](https://developer.apple.com/documentation/mediaaccessibility/mamediacharacteristictranscribesspokendialogforaccessibility)

|  | Declaration |
| --- | --- |
| From | ``` let MAMediaCharacteristicTranscribesSpokenDialogForAccessibility: CFString! ``` |
| To | ``` let MAMediaCharacteristicTranscribesSpokenDialogForAccessibility: CFString ``` |

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
