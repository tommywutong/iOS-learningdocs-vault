---
title: Accessibility Programming Guidelines for Mac
apple_id: 10000118i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Accessibility/cocoaAXNotifications/cocoaAXnotifications.html
archived_at: '2026-07-15T05:25:25.771780Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Accessibility Programming Guidelines for Mac](Introduction%20to%20Accessibility%20Programming%20Guidelines%20for%20Cocoa.md)


[Next](Access%20Enabling%20a%20Cocoa%20Application.md)[Previous](Hit-Testing%20and%20Keyboard%20Focus.md)

# Accessibility Notifications

Assistive applications need to be notified when something in the user interface of your application changes, such as a new window appearing or a control changing its value. An assistive application can then query an accessibility object in your application for its new state and present the information to the user.

NSAccessibility defines a number of notifications such as `NSAccessibilityWindowResizedNotification` and `NSAccessibilityFocusedUIElementChangedNotification`. The assistive application can register to receive notifications coming from a particular accessibility object or from any accessibility object in your application.

NSAccessibility notifications require special handling, so they cannot be sent using an NSNotificationCenter like regular notifications. Instead, notifications are sent with the following function:

```
void NSAccessibilityPostNotification( id element, NSString *notification );
```

The _element_ argument is the affected accessibility object and _notification_ is the notification name describing the event.

If you implement custom objects, you may need to send the `NSAccessibilityValueChangedNotification`; it is not likely you will ever need to send any others.

[Next](Access%20Enabling%20a%20Cocoa%20Application.md)[Previous](Hit-Testing%20and%20Keyboard%20Focus.md)

