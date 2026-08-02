---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/MediaAccessibility.html
archived_at: '2026-07-18T02:56:14.495742Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# MediaAccessibility Changes

## MediaAccessibility

Modified MACaptionAppearanceBehavior [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceDisplayType [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceDomain [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceFontStyle [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceTextEdgeStyle [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceAddSelectedLanguage(MACaptionAppearanceDomain, CFString!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceCopyBackgroundColor(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> Unmanaged<CGColor>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceCopyFontDescriptorForStyle(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>, MACaptionAppearanceFontStyle) -> Unmanaged<CTFontDescriptor>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceCopyForegroundColor(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> Unmanaged<CGColor>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics(MACaptionAppearanceDomain) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceCopySelectedLanguages(MACaptionAppearanceDomain) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceCopyWindowColor(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> Unmanaged<CGColor>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceGetBackgroundOpacity(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceGetDisplayType(MACaptionAppearanceDomain) -> MACaptionAppearanceDisplayType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceGetForegroundOpacity(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceGetRelativeCharacterSize(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceGetTextEdgeStyle(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> MACaptionAppearanceTextEdgeStyle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceGetWindowOpacity(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceGetWindowRoundedCornerRadius(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MACaptionAppearanceSetDisplayType(MACaptionAppearanceDomain, MACaptionAppearanceDisplayType)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MAMediaCharacteristicDescribesMusicAndSoundForAccessibility

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MAMediaCharacteristicTranscribesSpokenDialogForAccessibility

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

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
