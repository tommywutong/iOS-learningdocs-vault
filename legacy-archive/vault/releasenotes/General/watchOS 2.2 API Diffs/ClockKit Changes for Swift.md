---
title: watchOS 2.2 API Diffs
apple_id: TP40016663
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS22APIDiffs/Swift/ClockKit.html
archived_at: '2026-07-18T02:58:10.529884Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.2 API Diffs](watchOS%202.1%20to%20watchOS%202.2%20API%20Differences.md)


# ClockKit Changes for Swift

### ClockKit

Modified [CLKComplicationServer](https://developer.apple.com/documentation/clockkit/clkcomplicationserver)

|  | Declaration |
| --- | --- |
| From | ``` class CLKComplicationServer : NSObject {     class func sharedInstance() -> Self!     var activeComplications: [CLKComplication]! { get }     var earliestTimeTravelDate: NSDate! { get }     var latestTimeTravelDate: NSDate! { get }     func reloadTimelineForComplication(_ complication: CLKComplication!)     func extendTimelineForComplication(_ complication: CLKComplication!) } ``` |
| To | ``` class CLKComplicationServer : NSObject {     class func sharedInstance() -> Self     var activeComplications: [CLKComplication]? { get }     var earliestTimeTravelDate: NSDate { get }     var latestTimeTravelDate: NSDate { get }     func reloadTimelineForComplication(_ complication: CLKComplication)     func extendTimelineForComplication(_ complication: CLKComplication) } ``` |

Modified [CLKComplicationServer.activeComplications](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/1627893-activecomplications)

|  | Declaration |
| --- | --- |
| From | ``` var activeComplications: [CLKComplication]! { get } ``` |
| To | ``` var activeComplications: [CLKComplication]? { get } ``` |

Modified [CLKComplicationServer.earliestTimeTravelDate](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/1627896-earliesttimetraveldate)

|  | Declaration |
| --- | --- |
| From | ``` var earliestTimeTravelDate: NSDate! { get } ``` |
| To | ``` var earliestTimeTravelDate: NSDate { get } ``` |

Modified [CLKComplicationServer.extendTimelineForComplication(_: CLKComplication)](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/1627895-extendtimeline)

|  | Declaration |
| --- | --- |
| From | ``` func extendTimelineForComplication(_ complication: CLKComplication!) ``` |
| To | ``` func extendTimelineForComplication(_ complication: CLKComplication) ``` |

Modified [CLKComplicationServer.latestTimeTravelDate](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/1627890-latesttimetraveldate)

|  | Declaration |
| --- | --- |
| From | ``` var latestTimeTravelDate: NSDate! { get } ``` |
| To | ``` var latestTimeTravelDate: NSDate { get } ``` |

Modified [CLKComplicationServer.reloadTimelineForComplication(_: CLKComplication)](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/1627891-reloadtimeline)

|  | Declaration |
| --- | --- |
| From | ``` func reloadTimelineForComplication(_ complication: CLKComplication!) ``` |
| To | ``` func reloadTimelineForComplication(_ complication: CLKComplication) ``` |

Modified [CLKComplicationServer.sharedInstance() -> Self [class]](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/1627894-sharedinstance)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedInstance() -> Self! ``` |
| To | ``` class func sharedInstance() -> Self ``` |

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
