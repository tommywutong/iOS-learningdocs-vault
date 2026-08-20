---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/EventKitUI.html
archived_at: '2026-07-18T02:56:48.878030Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# EventKitUI Changes for Swift

### EventKitUI

Removed EKCalendarChooserDisplayStyle [struct]Removed EKCalendarChooserDisplayStyle.init(_: UInt32)Removed EKCalendarChooserDisplayStyle.valueRemoved EKCalendarChooserSelectionStyle [struct]Removed EKCalendarChooserSelectionStyle.init(_: UInt32)Removed EKCalendarChooserSelectionStyle.valueRemoved EKEventEditViewAction [struct]Removed EKEventEditViewAction.init(_: UInt32)Removed EKEventEditViewAction.valueRemoved EKEventViewAction [struct]Removed EKEventViewAction.init(_: UInt32)Removed EKEventViewAction.valueRemoved EKCalendarChooserDisplayAllCalendarsRemoved EKCalendarChooserDisplayWritableCalendarsOnlyRemoved EKCalendarChooserSelectionStyleMultipleRemoved EKCalendarChooserSelectionStyleSingleRemoved EKEventEditViewActionCanceledRemoved EKEventEditViewActionCancelledRemoved EKEventEditViewActionDeletedRemoved EKEventEditViewActionSavedRemoved EKEventViewActionDeletedRemoved EKEventViewActionDoneRemoved EKEventViewActionRespondedAdded [EKCalendarChooserDisplayStyle [enum]](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdisplaystyle)Added [EKCalendarChooserDisplayStyle.AllCalendars](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdisplaystyle/ekcalendarchooserdisplayallcalendars)Added [EKCalendarChooserDisplayStyle.WritableCalendarsOnly](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdisplaystyle/writablecalendarsonly)Added [EKCalendarChooserSelectionStyle [enum]](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserselectionstyle)Added [EKCalendarChooserSelectionStyle.Multiple](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserselectionstyle/ekcalendarchooserselectionstylemultiple)Added [EKCalendarChooserSelectionStyle.Single](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserselectionstyle/single)Added [EKEventEditViewAction [enum]](https://developer.apple.com/documentation/eventkitui/ekeventeditviewaction)Added [EKEventEditViewAction.Canceled](https://developer.apple.com/documentation/eventkitui/ekeventeditviewaction/canceled)Added [EKEventEditViewAction.Cancelled](https://developer.apple.com/documentation/eventkitui/ekeventeditviewaction/1613968-cancelled)Added [EKEventEditViewAction.Deleted](https://developer.apple.com/documentation/eventkitui/ekeventeditviewaction/ekeventeditviewactiondeleted)Added [EKEventEditViewAction.Saved](https://developer.apple.com/documentation/eventkitui/ekeventeditviewaction/saved)Added [EKEventViewAction [enum]](https://developer.apple.com/documentation/eventkitui/ekeventviewaction)Added [EKEventViewAction.Deleted](https://developer.apple.com/documentation/eventkitui/ekeventviewaction/ekeventviewactiondeleted)Added [EKEventViewAction.Done](https://developer.apple.com/documentation/eventkitui/ekeventviewaction/ekeventviewactiondone)Added [EKEventViewAction.Responded](https://developer.apple.com/documentation/eventkitui/ekeventviewaction/ekeventviewactionresponded)Modified [EKCalendarChooser](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser)

|  | Declaration |
| --- | --- |
| From | ``` class EKCalendarChooser : UIViewController {     init!(selectionStyle selectionStyle: EKCalendarChooserSelectionStyle, displayStyle displayStyle: EKCalendarChooserDisplayStyle, eventStore eventStore: EKEventStore!)     init!(selectionStyle style: EKCalendarChooserSelectionStyle, displayStyle displayStyle: EKCalendarChooserDisplayStyle, entityType entityType: EKEntityType, eventStore eventStore: EKEventStore!)     var selectionStyle: EKCalendarChooserSelectionStyle { get }     weak var delegate: EKCalendarChooserDelegate!     var showsDoneButton: Bool     var showsCancelButton: Bool     var selectedCalendars: Set<NSObject>! } ``` |
| To | ``` class EKCalendarChooser : UIViewController {     init(selectionStyle selectionStyle: EKCalendarChooserSelectionStyle, displayStyle displayStyle: EKCalendarChooserDisplayStyle, eventStore eventStore: EKEventStore)     init(selectionStyle style: EKCalendarChooserSelectionStyle, displayStyle displayStyle: EKCalendarChooserDisplayStyle, entityType entityType: EKEntityType, eventStore eventStore: EKEventStore)     var selectionStyle: EKCalendarChooserSelectionStyle { get }     weak var delegate: EKCalendarChooserDelegate?     var showsDoneButton: Bool     var showsCancelButton: Bool     var selectedCalendars: Set<EKCalendar> } ``` |

Modified [EKCalendarChooser.delegate](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser/1613949-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: EKCalendarChooserDelegate! ``` |
| To | ``` weak var delegate: EKCalendarChooserDelegate? ``` |

Modified [EKCalendarChooser.init(selectionStyle: EKCalendarChooserSelectionStyle, displayStyle: EKCalendarChooserDisplayStyle, entityType: EKEntityType, eventStore: EKEventStore)](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser/1613977-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(selectionStyle style: EKCalendarChooserSelectionStyle, displayStyle displayStyle: EKCalendarChooserDisplayStyle, entityType entityType: EKEntityType, eventStore eventStore: EKEventStore!) ``` |
| To | ``` init(selectionStyle style: EKCalendarChooserSelectionStyle, displayStyle displayStyle: EKCalendarChooserDisplayStyle, entityType entityType: EKEntityType, eventStore eventStore: EKEventStore) ``` |

Modified [EKCalendarChooser.init(selectionStyle: EKCalendarChooserSelectionStyle, displayStyle: EKCalendarChooserDisplayStyle, eventStore: EKEventStore)](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser/1613974-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(selectionStyle selectionStyle: EKCalendarChooserSelectionStyle, displayStyle displayStyle: EKCalendarChooserDisplayStyle, eventStore eventStore: EKEventStore!) ``` |
| To | ``` init(selectionStyle selectionStyle: EKCalendarChooserSelectionStyle, displayStyle displayStyle: EKCalendarChooserDisplayStyle, eventStore eventStore: EKEventStore) ``` |

Modified [EKCalendarChooser.selectedCalendars](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser/1613926-selectedcalendars)

|  | Declaration |
| --- | --- |
| From | ``` var selectedCalendars: Set<NSObject>! ``` |
| To | ``` var selectedCalendars: Set<EKCalendar> ``` |

Modified [EKCalendarChooserDelegate](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol EKCalendarChooserDelegate : NSObjectProtocol {     optional func calendarChooserSelectionDidChange(_ calendarChooser: EKCalendarChooser!)     optional func calendarChooserDidFinish(_ calendarChooser: EKCalendarChooser!)     optional func calendarChooserDidCancel(_ calendarChooser: EKCalendarChooser!) } ``` |
| To | ``` protocol EKCalendarChooserDelegate : NSObjectProtocol {     optional func calendarChooserSelectionDidChange(_ calendarChooser: EKCalendarChooser)     optional func calendarChooserDidFinish(_ calendarChooser: EKCalendarChooser)     optional func calendarChooserDidCancel(_ calendarChooser: EKCalendarChooser) } ``` |

Modified [EKCalendarChooserDelegate.calendarChooserDidCancel(_: EKCalendarChooser)](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdelegate/1613941-calendarchooserdidcancel)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func calendarChooserDidCancel(_ calendarChooser: EKCalendarChooser!) ``` | iOS 8.0 |
| To | ``` optional func calendarChooserDidCancel(_ calendarChooser: EKCalendarChooser) ``` | iOS 5.0 |

Modified [EKCalendarChooserDelegate.calendarChooserDidFinish(_: EKCalendarChooser)](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdelegate/1613979-calendarchooserdidfinish)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func calendarChooserDidFinish(_ calendarChooser: EKCalendarChooser!) ``` | iOS 8.0 |
| To | ``` optional func calendarChooserDidFinish(_ calendarChooser: EKCalendarChooser) ``` | iOS 5.0 |

Modified [EKCalendarChooserDelegate.calendarChooserSelectionDidChange(_: EKCalendarChooser)](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdelegate/1613924-calendarchooserselectiondidchang)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func calendarChooserSelectionDidChange(_ calendarChooser: EKCalendarChooser!) ``` | iOS 8.0 |
| To | ``` optional func calendarChooserSelectionDidChange(_ calendarChooser: EKCalendarChooser) ``` | iOS 5.0 |

Modified [EKEventEditViewController](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class EKEventEditViewController : UINavigationController {     weak var editViewDelegate: EKEventEditViewDelegate!     var eventStore: EKEventStore!     var event: EKEvent!     func cancelEditing() } ``` |
| To | ``` class EKEventEditViewController : UINavigationController {     weak var editViewDelegate: EKEventEditViewDelegate?     var eventStore: EKEventStore     var event: EKEvent?     func cancelEditing() } ``` |

Modified [EKEventEditViewController.editViewDelegate](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller/1613954-editviewdelegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var editViewDelegate: EKEventEditViewDelegate! ``` |
| To | ``` weak var editViewDelegate: EKEventEditViewDelegate? ``` |

Modified [EKEventEditViewController.event](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller/1613936-event)

|  | Declaration |
| --- | --- |
| From | ``` var event: EKEvent! ``` |
| To | ``` var event: EKEvent? ``` |

Modified [EKEventEditViewController.eventStore](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller/1613981-eventstore)

|  | Declaration |
| --- | --- |
| From | ``` var eventStore: EKEventStore! ``` |
| To | ``` var eventStore: EKEventStore ``` |

Modified [EKEventEditViewDelegate](https://developer.apple.com/documentation/eventkitui/ekeventeditviewdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol EKEventEditViewDelegate : NSObjectProtocol {     func eventEditViewController(_ controller: EKEventEditViewController!, didCompleteWithAction action: EKEventEditViewAction)     optional func eventEditViewControllerDefaultCalendarForNewEvents(_ controller: EKEventEditViewController!) -> EKCalendar! } ``` |
| To | ``` protocol EKEventEditViewDelegate : NSObjectProtocol {     func eventEditViewController(_ controller: EKEventEditViewController, didCompleteWithAction action: EKEventEditViewAction)     optional func eventEditViewControllerDefaultCalendarForNewEvents(_ controller: EKEventEditViewController) -> EKCalendar } ``` |

Modified [EKEventEditViewDelegate.eventEditViewController(_: EKEventEditViewController, didCompleteWithAction: EKEventEditViewAction)](https://developer.apple.com/documentation/eventkitui/ekeventeditviewdelegate/1613928-eventeditviewcontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func eventEditViewController(_ controller: EKEventEditViewController!, didCompleteWithAction action: EKEventEditViewAction) ``` | iOS 8.0 |
| To | ``` func eventEditViewController(_ controller: EKEventEditViewController, didCompleteWithAction action: EKEventEditViewAction) ``` | iOS 4.0 |

Modified [EKEventEditViewDelegate.eventEditViewControllerDefaultCalendarForNewEvents(_: EKEventEditViewController) -> EKCalendar](https://developer.apple.com/documentation/eventkitui/ekeventeditviewdelegate/1613932-eventeditviewcontrollerdefaultca)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func eventEditViewControllerDefaultCalendarForNewEvents(_ controller: EKEventEditViewController!) -> EKCalendar! ``` | iOS 8.0 |
| To | ``` optional func eventEditViewControllerDefaultCalendarForNewEvents(_ controller: EKEventEditViewController) -> EKCalendar ``` | iOS 4.0 |

Modified [EKEventViewController](https://developer.apple.com/documentation/eventkitui/ekeventviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class EKEventViewController : UIViewController {     weak var delegate: EKEventViewDelegate!     var event: EKEvent!     var allowsEditing: Bool     var allowsCalendarPreview: Bool } ``` |
| To | ``` class EKEventViewController : UIViewController {     weak var delegate: EKEventViewDelegate?     var event: EKEvent     var allowsEditing: Bool     var allowsCalendarPreview: Bool } ``` |

Modified [EKEventViewController.delegate](https://developer.apple.com/documentation/eventkitui/ekeventviewcontroller/1613939-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: EKEventViewDelegate! ``` |
| To | ``` weak var delegate: EKEventViewDelegate? ``` |

Modified [EKEventViewController.event](https://developer.apple.com/documentation/eventkitui/ekeventviewcontroller/1613929-event)

|  | Declaration |
| --- | --- |
| From | ``` var event: EKEvent! ``` |
| To | ``` var event: EKEvent ``` |

Modified [EKEventViewDelegate](https://developer.apple.com/documentation/eventkitui/ekeventviewdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol EKEventViewDelegate : NSObjectProtocol {     func eventViewController(_ controller: EKEventViewController!, didCompleteWithAction action: EKEventViewAction) } ``` |
| To | ``` protocol EKEventViewDelegate : NSObjectProtocol {     func eventViewController(_ controller: EKEventViewController, didCompleteWithAction action: EKEventViewAction) } ``` |

Modified [EKEventViewDelegate.eventViewController(_: EKEventViewController, didCompleteWithAction: EKEventViewAction)](https://developer.apple.com/documentation/eventkitui/ekeventviewdelegate/1613925-eventviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func eventViewController(_ controller: EKEventViewController!, didCompleteWithAction action: EKEventViewAction) ``` |
| To | ``` func eventViewController(_ controller: EKEventViewController, didCompleteWithAction action: EKEventViewAction) ``` |

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
