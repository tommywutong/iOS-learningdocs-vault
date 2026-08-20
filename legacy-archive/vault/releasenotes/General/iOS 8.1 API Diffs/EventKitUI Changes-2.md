---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/EventKitUI.html
archived_at: '2026-07-18T02:56:11.848893Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# EventKitUI Changes

## EventKitUI

Modified EKCalendarChooser

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified EKCalendarChooser.init(selectionStyle: EKCalendarChooserSelectionStyle, displayStyle: EKCalendarChooserDisplayStyle, entityType: EKEntityType, eventStore: EKEventStore!)

|  | Declaration |
| --- | --- |
| From | ``` init(selectionStyle style: EKCalendarChooserSelectionStyle, displayStyle displayStyle: EKCalendarChooserDisplayStyle, entityType entityType: EKEntityType, eventStore eventStore: EKEventStore!) ``` |
| To | ``` init!(selectionStyle style: EKCalendarChooserSelectionStyle, displayStyle displayStyle: EKCalendarChooserDisplayStyle, entityType entityType: EKEntityType, eventStore eventStore: EKEventStore!) ``` |

Modified EKCalendarChooser.init(selectionStyle: EKCalendarChooserSelectionStyle, displayStyle: EKCalendarChooserDisplayStyle, eventStore: EKEventStore!)

|  | Declaration |
| --- | --- |
| From | ``` init(selectionStyle selectionStyle: EKCalendarChooserSelectionStyle, displayStyle displayStyle: EKCalendarChooserDisplayStyle, eventStore eventStore: EKEventStore!) ``` |
| To | ``` init!(selectionStyle selectionStyle: EKCalendarChooserSelectionStyle, displayStyle displayStyle: EKCalendarChooserDisplayStyle, eventStore eventStore: EKEventStore!) ``` |

Modified EKEventEditViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified EKEventViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified EKEventViewController.delegate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified EKEventViewDelegate.eventViewController(EKEventViewController!, didCompleteWithAction: EKEventViewAction)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

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
