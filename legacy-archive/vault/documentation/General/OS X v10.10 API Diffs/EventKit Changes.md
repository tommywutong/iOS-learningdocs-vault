---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/EventKit.html
archived_at: '2026-07-15T07:34:45.496723Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# EventKit Changes

## EventKit

EKCalendar.hModified [EKCalendar.source](https://developer.apple.com/documentation/eventkit/ekcalendar/1507288-source)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) EKSource *source ``` |
| To | ``` @property(nonatomic, strong) EKSource *source ``` |

EKCalendarItem.hModified [EKCalendarItem.calendar](https://developer.apple.com/documentation/eventkit/ekcalendaritem/1507169-calendar)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) EKCalendar *calendar ``` |
| To | ``` @property(nonatomic, strong) EKCalendar *calendar ``` |

EKStructuredLocation.hModified [EKStructuredLocation.geoLocation](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507110-geolocation)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) CLLocation *geoLocation ``` |
| To | ``` @property(nonatomic, strong) CLLocation *geoLocation ``` |

Modified [EKStructuredLocation.title](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/1507137-title)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSString *title ``` |
| To | ``` @property(nonatomic, strong) NSString *title ``` |

EventKitDefines.hAdded [DATETIME_COMPONENTS_DO_NOT_USE()](https://developer.apple.com/documentation/eventkit/1507496-datetime_components_do_not_use)Added [DATE_COMPONENTS_DO_NOT_USE()](https://developer.apple.com/documentation/eventkit/1507535-date_components_do_not_use)Added [EK_LOSE_FRACTIONAL_SECONDS_DO_NOT_USE()](https://developer.apple.com/documentation/eventkit/1507322-ek_lose_fractional_seconds_do_no)

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
