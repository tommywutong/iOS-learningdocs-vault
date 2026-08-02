---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/MediaAccessibility.html
archived_at: '2026-07-18T02:53:09.882576Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# MediaAccessibility Changes for Objective-C

### MediaAccessibility

#### MAAudibleMedia.h

Modified [MAAudibleMediaCopyPreferredCharacteristics()](https://developer.apple.com/documentation/mediaaccessibility/1464885-maaudiblemediacopypreferredchara)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef MAAudibleMediaCopyPreferredCharacteristics (     void ); ``` |
| To | ``` CFArrayRef _Nonnull MAAudibleMediaCopyPreferredCharacteristics (     void ); ``` |

#### MACaptionAppearance.h

Modified [MACaptionAppearanceAddSelectedLanguage()](https://developer.apple.com/documentation/mediaaccessibility/1464869-macaptionappearanceaddselectedla)

|  | Declaration |
| --- | --- |
| From | ``` bool MACaptionAppearanceAddSelectedLanguage (     MACaptionAppearanceDomain domain,     CFStringRef language ); ``` |
| To | ``` bool MACaptionAppearanceAddSelectedLanguage (     MACaptionAppearanceDomain domain,     CFStringRef _Nonnull language ); ``` |

Modified [MACaptionAppearanceCopyBackgroundColor()](https://developer.apple.com/documentation/mediaaccessibility/1464822-macaptionappearancecopybackgroun)

|  | Declaration |
| --- | --- |
| From | ``` CGColorRef MACaptionAppearanceCopyBackgroundColor (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior *behavior ); ``` |
| To | ``` CGColorRef _Nonnull MACaptionAppearanceCopyBackgroundColor (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior * _Nullable behavior ); ``` |

Modified [MACaptionAppearanceCopyFontDescriptorForStyle()](https://developer.apple.com/documentation/mediaaccessibility/1464816-macaptionappearancecopyfontdescr)

|  | Declaration |
| --- | --- |
| From | ``` CTFontDescriptorRef MACaptionAppearanceCopyFontDescriptorForStyle (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior *behavior,     MACaptionAppearanceFontStyle fontStyle ); ``` |
| To | ``` CTFontDescriptorRef _Nonnull MACaptionAppearanceCopyFontDescriptorForStyle (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior * _Nullable behavior,     MACaptionAppearanceFontStyle fontStyle ); ``` |

Modified [MACaptionAppearanceCopyForegroundColor()](https://developer.apple.com/documentation/mediaaccessibility/1464828-macaptionappearancecopyforegroun)

|  | Declaration |
| --- | --- |
| From | ``` CGColorRef MACaptionAppearanceCopyForegroundColor (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior *behavior ); ``` |
| To | ``` CGColorRef _Nonnull MACaptionAppearanceCopyForegroundColor (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior * _Nullable behavior ); ``` |

Modified [MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics()](https://developer.apple.com/documentation/mediaaccessibility/1464881-macaptionappearancecopypreferred)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics (     MACaptionAppearanceDomain domain ); ``` |
| To | ``` CFArrayRef _Nonnull MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics (     MACaptionAppearanceDomain domain ); ``` |

Modified [MACaptionAppearanceCopySelectedLanguages()](https://developer.apple.com/documentation/mediaaccessibility/1464855-macaptionappearancecopyselectedl)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef MACaptionAppearanceCopySelectedLanguages (     MACaptionAppearanceDomain domain ); ``` |
| To | ``` CFArrayRef _Nonnull MACaptionAppearanceCopySelectedLanguages (     MACaptionAppearanceDomain domain ); ``` |

Modified [MACaptionAppearanceCopyWindowColor()](https://developer.apple.com/documentation/mediaaccessibility/1464842-macaptionappearancecopywindowcol)

|  | Declaration |
| --- | --- |
| From | ``` CGColorRef MACaptionAppearanceCopyWindowColor (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior *behavior ); ``` |
| To | ``` CGColorRef _Nonnull MACaptionAppearanceCopyWindowColor (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior * _Nullable behavior ); ``` |

Modified [MACaptionAppearanceGetBackgroundOpacity()](https://developer.apple.com/documentation/mediaaccessibility/1464840-macaptionappearancegetbackground)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat MACaptionAppearanceGetBackgroundOpacity (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior *behavior ); ``` |
| To | ``` CGFloat MACaptionAppearanceGetBackgroundOpacity (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior * _Nullable behavior ); ``` |

Modified [MACaptionAppearanceGetForegroundOpacity()](https://developer.apple.com/documentation/mediaaccessibility/1464887-macaptionappearancegetforeground)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat MACaptionAppearanceGetForegroundOpacity (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior *behavior ); ``` |
| To | ``` CGFloat MACaptionAppearanceGetForegroundOpacity (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior * _Nullable behavior ); ``` |

Modified [MACaptionAppearanceGetRelativeCharacterSize()](https://developer.apple.com/documentation/mediaaccessibility/1464820-macaptionappearancegetrelativech)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat MACaptionAppearanceGetRelativeCharacterSize (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior *behavior ); ``` |
| To | ``` CGFloat MACaptionAppearanceGetRelativeCharacterSize (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior * _Nullable behavior ); ``` |

Modified [MACaptionAppearanceGetTextEdgeStyle()](https://developer.apple.com/documentation/mediaaccessibility/1464824-macaptionappearancegettextedgest)

|  | Declaration |
| --- | --- |
| From | ``` MACaptionAppearanceTextEdgeStyle MACaptionAppearanceGetTextEdgeStyle (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior *behavior ); ``` |
| To | ``` MACaptionAppearanceTextEdgeStyle MACaptionAppearanceGetTextEdgeStyle (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior * _Nullable behavior ); ``` |

Modified [MACaptionAppearanceGetWindowOpacity()](https://developer.apple.com/documentation/mediaaccessibility/1464844-macaptionappearancegetwindowopac)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat MACaptionAppearanceGetWindowOpacity (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior *behavior ); ``` |
| To | ``` CGFloat MACaptionAppearanceGetWindowOpacity (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior * _Nullable behavior ); ``` |

Modified [MACaptionAppearanceGetWindowRoundedCornerRadius()](https://developer.apple.com/documentation/mediaaccessibility/1464826-macaptionappearancegetwindowroun)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat MACaptionAppearanceGetWindowRoundedCornerRadius (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior *behavior ); ``` |
| To | ``` CGFloat MACaptionAppearanceGetWindowRoundedCornerRadius (     MACaptionAppearanceDomain domain,     MACaptionAppearanceBehavior * _Nullable behavior ); ``` |

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
