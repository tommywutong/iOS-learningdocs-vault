---
title: watchOS 2.1 API Diffs
apple_id: TP40016636
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS21APIDiffs/Swift/ClockKit.html
archived_at: '2026-07-18T02:58:07.664817Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.1 API Diffs](watchOS%202.0%20to%20watchOS%202.1%20API%20Differences.md)


# ClockKit Changes for Swift

### ClockKit

Added [CLKComplicationColumnAlignment.Leading](https://developer.apple.com/documentation/clockkit/clkcomplicationcolumnalignment/clkcomplicationcolumnalignmentleading)Added [CLKComplicationColumnAlignment.Trailing](https://developer.apple.com/documentation/clockkit/clkcomplicationcolumnalignment/clkcomplicationcolumnalignmenttrailing)Modified [CLKComplication](https://developer.apple.com/documentation/clockkit/clkcomplication)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [CLKComplicationColumnAlignment [enum]](https://developer.apple.com/documentation/clockkit/clkcomplicationcolumnalignment)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum CLKComplicationColumnAlignment : Int {     case Left     case Right } ``` | Equatable, Hashable, RawRepresentable |
| To | ``` enum CLKComplicationColumnAlignment : Int {     case Leading     case Trailing     static var Left: CLKComplicationColumnAlignment { get }     static var Right: CLKComplicationColumnAlignment { get } } ``` | -- |

Modified [CLKComplicationColumnAlignment.Left](https://developer.apple.com/documentation/clockkit/clkcomplicationcolumnalignment/1628104-left)

|  | Declaration |
| --- | --- |
| From | ``` case Left ``` |
| To | ``` static var Left: CLKComplicationColumnAlignment { get } ``` |

Modified [CLKComplicationColumnAlignment.Right](https://developer.apple.com/documentation/clockkit/clkcomplicationcolumnalignment/1627996-right)

|  | Declaration |
| --- | --- |
| From | ``` case Right ``` |
| To | ``` static var Right: CLKComplicationColumnAlignment { get } ``` |

Modified [CLKComplicationFamily [enum]](https://developer.apple.com/documentation/clockkit/clkcomplicationfamily)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CLKComplicationPrivacyBehavior [enum]](https://developer.apple.com/documentation/clockkit/clkcomplicationprivacybehavior)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CLKComplicationRingStyle [enum]](https://developer.apple.com/documentation/clockkit/clkcomplicationringstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CLKComplicationServer](https://developer.apple.com/documentation/clockkit/clkcomplicationserver)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplate](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplate)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [CLKComplicationTemplateCircularSmallRingImage](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallringimage)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateCircularSmallRingText](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallringtext)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateCircularSmallSimpleImage](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallsimpleimage)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateCircularSmallSimpleText](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallsimpletext)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateCircularSmallStackImage](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallstackimage)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateCircularSmallStackText](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallstacktext)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateModularLargeColumns](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargecolumns)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateModularLargeStandardBody](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargestandardbody)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateModularLargeTable](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargetable)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateModularLargeTallBody](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargetallbody)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateModularSmallColumnsText](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallcolumnstext)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateModularSmallRingImage](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallringimage)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateModularSmallRingText](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallringtext)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateModularSmallSimpleImage](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallsimpleimage)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateModularSmallSimpleText](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallsimpletext)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateModularSmallStackImage](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallstackimage)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateModularSmallStackText](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallstacktext)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateUtilitarianLargeFlat](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitarianlargeflat)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateUtilitarianSmallFlat](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitariansmallflat)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateUtilitarianSmallRingImage](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitariansmallringimage)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateUtilitarianSmallRingText](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitariansmallringtext)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTemplateUtilitarianSmallSquare](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitariansmallsquare)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKComplicationTimelineAnimationBehavior [enum]](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineanimationbehavior)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CLKComplicationTimelineEntry](https://developer.apple.com/documentation/clockkit/clkcomplicationtimelineentry)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKDateTextProvider](https://developer.apple.com/documentation/clockkit/clkdatetextprovider)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKImageProvider](https://developer.apple.com/documentation/clockkit/clkimageprovider)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [CLKRelativeDateStyle [enum]](https://developer.apple.com/documentation/clockkit/clkrelativedatestyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CLKRelativeDateTextProvider](https://developer.apple.com/documentation/clockkit/clkrelativedatetextprovider)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKSimpleTextProvider](https://developer.apple.com/documentation/clockkit/clksimpletextprovider)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKTextProvider](https://developer.apple.com/documentation/clockkit/clktextprovider)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [CLKTimeIntervalTextProvider](https://developer.apple.com/documentation/clockkit/clktimeintervaltextprovider)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CLKTimeTextProvider](https://developer.apple.com/documentation/clockkit/clktimetextprovider)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

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
