---
title: Calendar and Reminders Programming Guide
apple_id: TP40009765
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Data Management
technology: EventKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/EventKitProgGuide/UsingEventViewControllers.html
archived_at: '2026-07-27T06:57:07.535051Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Calendar and Reminders Programming Guide](Introduction%20to%20Calendars%20and%20Reminders.md)


[Next](Document%20Revision%20History.md)[Previous](Observing%20External%20Changes%20to%20the%20Calendar%20Database.md)

# Providing Interfaces for Events

__Important:__ The EventKit UI framework, as referenced by this chapter, is available for iOS only. If you are developing for OS X, you are responsible for constructing your own event view controllers; for more information, read _[NSViewController Class Reference](https://developer.apple.com/documentation/appkit/nsviewcontroller)_.

The EventKit UI framework provides two types of view controllers for manipulating events:

- [EKEventViewController](https://developer.apple.com/documentation/eventkitui/ekeventviewcontroller): use this class if you have an existing event you want to display.
- [EKEventEditViewController](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller): use this class to allow the user to create, edit, or delete events.

## Displaying Event Data

To use the `EKEventViewController` class, you must have an existing event you obtained from an event store. You need to set the `event` property and any other display options before presenting this type of view controller. Listing 6-1 shows how to create an event view controller and add it to a navigation controller, assuming `myEvent` already exists. If you don’t allow the user to edit the event, set the `allowsEditing` property to `NO`.

__Listing 6-1__  Editing an existing event

```
    EKEventViewController *eventViewController = [[EKEventViewController alloc] init];
    eventViewController.event = myEvent;
    eventViewController.allowsEditing = YES;
    navigationController = [[UINavigationController alloc] initWithRootViewController:eventViewController];
```

You need to assign a delegate to an event view controller to receive a notification when the user finishes viewing the event. The delegate conforms to the [EKEventViewDelegate](https://developer.apple.com/documentation/eventkitui/ekeventviewdelegate) protocol and must implement the [eventViewController:didCompleteWithAction:](https://developer.apple.com/documentation/eventkitui/ekeventviewdelegate/1613925-eventviewcontroller) method.

## Modifying Event Data

To allow the user to create, edit, or delete events, use the `EKEventEditViewController` class and the `EKEventEditViewDelegate` protocol. You create an event edit view controller similar to an event view controller, except you must set the `eventStore` property (setting the `event` property is optional).

- If the `event` property is `nil` when you present the view controller, the user creates a new event in the default calendar and saves it to the specified event store.
- If the `event` property is not `nil`, the user edits an existing event. The event must reside in the specified event store—otherwise, an exception is raised.

Instances of the `EKEventEditViewController` class are designed to be presented modally, as shown in Listing 6-2. In this code fragment, `self` is the top view controller of a navigation controller. For details on modal view controllers, read Presenting a View Controller Modally.

__Listing 6-2__  Presenting an event edit view controller modally

```
    EKEventEditViewController* controller = [[EKEventEditViewController alloc] init];
    controller.eventStore = myEventStore;
    controller.editViewDelegate = self;
    [self presentModalViewController:controller animated:YES];
```

You must also specify a delegate to receive notification when the user finishes editing the event. The delegate conforms to the `EKEventEditViewDelegate` protocol and must implement the `eventEditViewController:didCompleteWithAction:` method to dismiss the modal view controller, as shown in Listing 6-3. In general, the object that presents a view controller modally is responsible for dismissing it.

__Listing 6-3__  The delegate dismisses the modal view

```objc
- (void)eventEditViewController:(EKEventEditViewController *)controller
          didCompleteWithAction:(EKEventEditViewAction)action
{
    [self dismissModalViewControllerAnimated:YES];
}
```

The delegate is also passed the action the user took when finishing the edit. The user can either cancel the changes, save the event, or delete the event. If you need to execute more code after the user dismisses the modal view, implement the [eventEditViewController:didCompleteWithAction:](https://developer.apple.com/documentation/eventkitui/ekeventeditviewdelegate/1613928-eventeditviewcontroller) delegate method.

[Next](Document%20Revision%20History.md)[Previous](Observing%20External%20Changes%20to%20the%20Calendar%20Database.md)
