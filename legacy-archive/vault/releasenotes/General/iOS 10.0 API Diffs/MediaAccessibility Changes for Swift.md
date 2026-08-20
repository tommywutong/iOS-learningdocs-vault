---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/MediaAccessibility.html
archived_at: '2026-07-18T02:55:31.617393Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# MediaAccessibility Changes for Swift

### MediaAccessibility

Modified [MACaptionAppearanceBehavior [enum]](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancebehavior)

|  | Declaration |
| --- | --- |
| From | ``` enum MACaptionAppearanceBehavior : CFIndex {     case UseValue     case UseContentIfAvailable } ``` |
| To | ``` enum MACaptionAppearanceBehavior : CFIndex {     case useValue     case useContentIfAvailable } ``` |

Modified [MACaptionAppearanceBehavior.useContentIfAvailable](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancebehavior/usecontentifavailable)

|  | Declaration |
| --- | --- |
| From | ``` case UseContentIfAvailable ``` |
| To | ``` case useContentIfAvailable ``` |

Modified [MACaptionAppearanceBehavior.useValue](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancebehavior/kmacaptionappearancebehaviorusevalue)

|  | Declaration |
| --- | --- |
| From | ``` case UseValue ``` |
| To | ``` case useValue ``` |

Modified [MACaptionAppearanceDisplayType [enum]](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancedisplaytype)

|  | Declaration |
| --- | --- |
| From | ``` enum MACaptionAppearanceDisplayType : CFIndex {     case ForcedOnly     case Automatic     case AlwaysOn } ``` |
| To | ``` enum MACaptionAppearanceDisplayType : CFIndex {     case forcedOnly     case automatic     case alwaysOn } ``` |

Modified [MACaptionAppearanceDisplayType.alwaysOn](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancedisplaytype/kmacaptionappearancedisplaytypealwayson)

|  | Declaration |
| --- | --- |
| From | ``` case AlwaysOn ``` |
| To | ``` case alwaysOn ``` |

Modified [MACaptionAppearanceDisplayType.automatic](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancedisplaytype/kmacaptionappearancedisplaytypeautomatic)

|  | Declaration |
| --- | --- |
| From | ``` case Automatic ``` |
| To | ``` case automatic ``` |

Modified [MACaptionAppearanceDisplayType.forcedOnly](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancedisplaytype/forcedonly)

|  | Declaration |
| --- | --- |
| From | ``` case ForcedOnly ``` |
| To | ``` case forcedOnly ``` |

Modified [MACaptionAppearanceDomain [enum]](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancedomain)

|  | Declaration |
| --- | --- |
| From | ``` enum MACaptionAppearanceDomain : CFIndex {     case Default     case User } ``` |
| To | ``` enum MACaptionAppearanceDomain : CFIndex {     case `default`     case user } ``` |

Modified [MACaptionAppearanceDomain.default](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancedomain/kmacaptionappearancedomaindefault)

|  | Declaration |
| --- | --- |
| From | ``` case Default ``` |
| To | ``` case `default` ``` |

Modified [MACaptionAppearanceDomain.user](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancedomain/kmacaptionappearancedomainuser)

|  | Declaration |
| --- | --- |
| From | ``` case User ``` |
| To | ``` case user ``` |

Modified [MACaptionAppearanceFontStyle [enum]](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle)

|  | Declaration |
| --- | --- |
| From | ``` enum MACaptionAppearanceFontStyle : CFIndex {     case Default     case MonospacedWithSerif     case ProportionalWithSerif     case MonospacedWithoutSerif     case ProportionalWithoutSerif     case Casual     case Cursive     case SmallCapital } ``` |
| To | ``` enum MACaptionAppearanceFontStyle : CFIndex {     case `default`     case monospacedWithSerif     case proportionalWithSerif     case monospacedWithoutSerif     case proportionalWithoutSerif     case casual     case cursive     case smallCapital } ``` |

Modified [MACaptionAppearanceFontStyle.casual](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle/kmacaptionappearancefontstylecasual)

|  | Declaration |
| --- | --- |
| From | ``` case Casual ``` |
| To | ``` case casual ``` |

Modified [MACaptionAppearanceFontStyle.cursive](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle/cursive)

|  | Declaration |
| --- | --- |
| From | ``` case Cursive ``` |
| To | ``` case cursive ``` |

Modified [MACaptionAppearanceFontStyle.default](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle/kmacaptionappearancefontstyledefault)

|  | Declaration |
| --- | --- |
| From | ``` case Default ``` |
| To | ``` case `default` ``` |

Modified [MACaptionAppearanceFontStyle.monospacedWithoutSerif](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle/monospacedwithoutserif)

|  | Declaration |
| --- | --- |
| From | ``` case MonospacedWithoutSerif ``` |
| To | ``` case monospacedWithoutSerif ``` |

Modified [MACaptionAppearanceFontStyle.monospacedWithSerif](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle/monospacedwithserif)

|  | Declaration |
| --- | --- |
| From | ``` case MonospacedWithSerif ``` |
| To | ``` case monospacedWithSerif ``` |

Modified [MACaptionAppearanceFontStyle.proportionalWithoutSerif](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle/kmacaptionappearancefontstyleproportionalwithoutserif)

|  | Declaration |
| --- | --- |
| From | ``` case ProportionalWithoutSerif ``` |
| To | ``` case proportionalWithoutSerif ``` |

Modified [MACaptionAppearanceFontStyle.proportionalWithSerif](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle/kmacaptionappearancefontstyleproportionalwithserif)

|  | Declaration |
| --- | --- |
| From | ``` case ProportionalWithSerif ``` |
| To | ``` case proportionalWithSerif ``` |

Modified [MACaptionAppearanceFontStyle.smallCapital](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancefontstyle/kmacaptionappearancefontstylesmallcapital)

|  | Declaration |
| --- | --- |
| From | ``` case SmallCapital ``` |
| To | ``` case smallCapital ``` |

Modified [MACaptionAppearanceTextEdgeStyle [enum]](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancetextedgestyle)

|  | Declaration |
| --- | --- |
| From | ``` enum MACaptionAppearanceTextEdgeStyle : CFIndex {     case Undefined     case None     case Raised     case Depressed     case Uniform     case DropShadow } ``` |
| To | ``` enum MACaptionAppearanceTextEdgeStyle : CFIndex {     case undefined     case none     case raised     case depressed     case uniform     case dropShadow } ``` |

Modified [MACaptionAppearanceTextEdgeStyle.depressed](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancetextedgestyle/depressed)

|  | Declaration |
| --- | --- |
| From | ``` case Depressed ``` |
| To | ``` case depressed ``` |

Modified [MACaptionAppearanceTextEdgeStyle.dropShadow](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancetextedgestyle/kmacaptionappearancetextedgestyledropshadow)

|  | Declaration |
| --- | --- |
| From | ``` case DropShadow ``` |
| To | ``` case dropShadow ``` |

Modified [MACaptionAppearanceTextEdgeStyle.none](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancetextedgestyle/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [MACaptionAppearanceTextEdgeStyle.raised](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancetextedgestyle/raised)

|  | Declaration |
| --- | --- |
| From | ``` case Raised ``` |
| To | ``` case raised ``` |

Modified [MACaptionAppearanceTextEdgeStyle.undefined](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancetextedgestyle/kmacaptionappearancetextedgestyleundefined)

|  | Declaration |
| --- | --- |
| From | ``` case Undefined ``` |
| To | ``` case undefined ``` |

Modified [MACaptionAppearanceTextEdgeStyle.uniform](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancetextedgestyle/kmacaptionappearancetextedgestyleuniform)

|  | Declaration |
| --- | --- |
| From | ``` case Uniform ``` |
| To | ``` case uniform ``` |

Modified [MACaptionAppearanceCopyBackgroundColor(_: MACaptionAppearanceDomain, _: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> Unmanaged<CGColor>](https://developer.apple.com/documentation/mediaaccessibility/1464822-macaptionappearancecopybackgroun)

|  | Declaration |
| --- | --- |
| From | ``` func MACaptionAppearanceCopyBackgroundColor(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> Unmanaged<CGColor> ``` |
| To | ``` func MACaptionAppearanceCopyBackgroundColor(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> Unmanaged<CGColor> ``` |

Modified [MACaptionAppearanceCopyFontDescriptorForStyle(_: MACaptionAppearanceDomain, _: UnsafeMutablePointer<MACaptionAppearanceBehavior>?, _: MACaptionAppearanceFontStyle) -> Unmanaged<CTFontDescriptor>](https://developer.apple.com/documentation/mediaaccessibility/1464816-macaptionappearancecopyfontdescr)

|  | Declaration |
| --- | --- |
| From | ``` func MACaptionAppearanceCopyFontDescriptorForStyle(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>, _ fontStyle: MACaptionAppearanceFontStyle) -> Unmanaged<CTFontDescriptor> ``` |
| To | ``` func MACaptionAppearanceCopyFontDescriptorForStyle(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>?, _ fontStyle: MACaptionAppearanceFontStyle) -> Unmanaged<CTFontDescriptor> ``` |

Modified [MACaptionAppearanceCopyForegroundColor(_: MACaptionAppearanceDomain, _: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> Unmanaged<CGColor>](https://developer.apple.com/documentation/mediaaccessibility/1464828-macaptionappearancecopyforegroun)

|  | Declaration |
| --- | --- |
| From | ``` func MACaptionAppearanceCopyForegroundColor(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> Unmanaged<CGColor> ``` |
| To | ``` func MACaptionAppearanceCopyForegroundColor(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> Unmanaged<CGColor> ``` |

Modified [MACaptionAppearanceCopyWindowColor(_: MACaptionAppearanceDomain, _: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> Unmanaged<CGColor>](https://developer.apple.com/documentation/mediaaccessibility/1464842-macaptionappearancecopywindowcol)

|  | Declaration |
| --- | --- |
| From | ``` func MACaptionAppearanceCopyWindowColor(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> Unmanaged<CGColor> ``` |
| To | ``` func MACaptionAppearanceCopyWindowColor(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> Unmanaged<CGColor> ``` |

Modified [MACaptionAppearanceGetBackgroundOpacity(_: MACaptionAppearanceDomain, _: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat](https://developer.apple.com/documentation/mediaaccessibility/1464840-macaptionappearancegetbackground)

|  | Declaration |
| --- | --- |
| From | ``` func MACaptionAppearanceGetBackgroundOpacity(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> CGFloat ``` |
| To | ``` func MACaptionAppearanceGetBackgroundOpacity(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat ``` |

Modified [MACaptionAppearanceGetForegroundOpacity(_: MACaptionAppearanceDomain, _: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat](https://developer.apple.com/documentation/mediaaccessibility/1464887-macaptionappearancegetforeground)

|  | Declaration |
| --- | --- |
| From | ``` func MACaptionAppearanceGetForegroundOpacity(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> CGFloat ``` |
| To | ``` func MACaptionAppearanceGetForegroundOpacity(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat ``` |

Modified [MACaptionAppearanceGetRelativeCharacterSize(_: MACaptionAppearanceDomain, _: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat](https://developer.apple.com/documentation/mediaaccessibility/1464820-macaptionappearancegetrelativech)

|  | Declaration |
| --- | --- |
| From | ``` func MACaptionAppearanceGetRelativeCharacterSize(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> CGFloat ``` |
| To | ``` func MACaptionAppearanceGetRelativeCharacterSize(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat ``` |

Modified [MACaptionAppearanceGetTextEdgeStyle(_: MACaptionAppearanceDomain, _: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> MACaptionAppearanceTextEdgeStyle](https://developer.apple.com/documentation/mediaaccessibility/1464824-macaptionappearancegettextedgest)

|  | Declaration |
| --- | --- |
| From | ``` func MACaptionAppearanceGetTextEdgeStyle(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> MACaptionAppearanceTextEdgeStyle ``` |
| To | ``` func MACaptionAppearanceGetTextEdgeStyle(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> MACaptionAppearanceTextEdgeStyle ``` |

Modified [MACaptionAppearanceGetWindowOpacity(_: MACaptionAppearanceDomain, _: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat](https://developer.apple.com/documentation/mediaaccessibility/1464844-macaptionappearancegetwindowopac)

|  | Declaration |
| --- | --- |
| From | ``` func MACaptionAppearanceGetWindowOpacity(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> CGFloat ``` |
| To | ``` func MACaptionAppearanceGetWindowOpacity(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat ``` |

Modified [MACaptionAppearanceGetWindowRoundedCornerRadius(_: MACaptionAppearanceDomain, _: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat](https://developer.apple.com/documentation/mediaaccessibility/1464826-macaptionappearancegetwindowroun)

|  | Declaration |
| --- | --- |
| From | ``` func MACaptionAppearanceGetWindowRoundedCornerRadius(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>) -> CGFloat ``` |
| To | ``` func MACaptionAppearanceGetWindowRoundedCornerRadius(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat ``` |

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
