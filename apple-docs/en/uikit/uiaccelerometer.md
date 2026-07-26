---
title: UIAccelerometer
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: []
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiaccelerometer
source_url: 'https://developer.apple.com/documentation/uikit/uiaccelerometer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccelerometer.json'
content_hash: 'sha256:c2f674fad6dcf7cf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccelerometer

<sub>Class</sub>

An object that lets you register to receive acceleration-related data from the onboard hardware.

> [!warning] Deprecated
> Use the [Core Motion](../coremotion.md) framework instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UIAccelerometer : NSObject
```

## Overview

As a device moves, its hardware reports linear acceleration changes along the primary axes in three-dimensional space. You can use this data to detect both the current orientation of the device (relative to the ground) and any instantaneous changes to that orientation. You might use instantaneous changes as input to a game or to initiate some action in your application.

You don’t create accelerometer objects directly. Instead, you use the shared `UIAccelerometer` object to specify the interval at which you want to receive events and then set its [delegate](uiaccelerometer/delegate.md) property. Upon assigning your delegate object, the accelerometer object begins delivering acceleration events to your delegate immediately at the specified interval. Events are always delivered on the main thread of your application.

The maximum frequency for accelerometer updates is based on the available hardware. You can request updates less frequently but can’t request them more frequently than the hardware maximum. Once you assign your delegate, however, updates are delivered regularly at the frequency you requested, whether or not the acceleration data actually changed. Your delegate is responsible for filtering out any unwanted updates and for ensuring that the amount of change is significant enough to warrant taking action.

For more information about the data delivered to your observer, see [UIAcceleration](uiacceleration.md). For information about implementing your delegate object, see [UIAccelerometerDelegate](uiaccelerometerdelegate.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Getting the shared accelerometer object

- [sharedAccelerometer](uiaccelerometer/sharedaccelerometer.md) — Returns the shared accelerometer object for the system. _(deprecated)_

### Accessing the accelerometer properties

- [updateInterval](uiaccelerometer/updateinterval.md) — The interval at which to deliver acceleration data to the delegate. _(deprecated)_
- [delegate](uiaccelerometer/delegate.md) — The delegate object you want to receive acceleration events. _(deprecated)_

## See Also

### Deprecated classes

- [UIAcceleration](uiacceleration.md) — An acceleration event that represents immediate, three-dimensional acceleration data. _(deprecated)_
- [UIActionSheet](uiactionsheet.md) — A view that presents a set of alternatives for how to proceed with a task. _(deprecated)_
- [UIAlertView](uialertview.md) — A view that displays an alert message. _(deprecated)_
- [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md) — A list of all the available document providers for a given file type and mode, in addition to custom menu items that you add. _(deprecated)_
- [UILocalNotification](uilocalnotification.md) — A notification that an app can schedule for presentation at a specific date and time. _(deprecated)_
- [UIMenuController](uimenucontroller.md) — The menu interface for the Cut, Copy, Paste, Select, Select All, and Delete commands. _(deprecated)_
- [UIMenuItem](uimenuitem.md) — A custom item in the editing menu managed by the menu controller. _(deprecated)_
- [UIMutableUserNotificationAction](uimutableusernotificationaction.md) — A modifiable version of the user notification action class. _(deprecated)_
- [UIMutableUserNotificationCategory](uimutableusernotificationcategory.md) — Information about custom actions that your app can perform in response to a local or push notification. _(deprecated)_
- [UIPopoverController](uipopovercontroller.md) — An object that manages the presentation of content in a popover. _(deprecated)_
- [UIPreviewAction](uipreviewaction.md) — A preview action, or _peek quick action_, that displays below a peek when a user swipes the peek upward. _(deprecated)_
- [UIPreviewActionGroup](uipreviewactiongroup.md) — A group of one or more child quick actions, each an instance of the preview action class. _(deprecated)_
- [UISearchDisplayController](uisearchdisplaycontroller.md) — An object that manages the display of a search bar, along with a table view that displays search results. _(deprecated)_
- [UIStoryboardPopoverSegue](uistoryboardpopoversegue.md) — A specific type of segue for presenting content in a popover. _(deprecated)_
- [UIWebView](uiwebview.md) — A view that embeds web content in your app. _(deprecated)_
