---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/CalendarStore.html
archived_at: '2026-07-18T02:52:56.539697Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CalendarStore Changes for Objective-C

### CalendarStore

#### CalAlarm.h

Modified CalAlarm.absoluteTrigger

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSDate *absoluteTrigger ``` |
| To | ``` @property(copy, nonatomic) NSDate *absoluteTrigger ``` |

Modified CalAlarm.action

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *action ``` |
| To | ``` @property(copy, nonatomic) NSString *action ``` |

Modified CalAlarm.emailAddress

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *emailAddress ``` |
| To | ``` @property(copy, nonatomic) NSString *emailAddress ``` |

Modified CalAlarm.relativeTrigger

|  | Declaration |
| --- | --- |
| From | ``` @property NSTimeInterval relativeTrigger ``` |
| To | ``` @property(nonatomic) NSTimeInterval relativeTrigger ``` |

Modified CalAlarm.sound

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *sound ``` |
| To | ``` @property(copy, nonatomic) NSString *sound ``` |

Modified CalAlarm.url

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSURL *url ``` |
| To | ``` @property(copy, nonatomic) NSURL *url ``` |

#### CalEvent.h

Modified CalEvent.occurrence

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSDate *occurrence ``` |
| To | ``` @property(copy, readonly, nonatomic) NSDate *occurrence ``` |

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
