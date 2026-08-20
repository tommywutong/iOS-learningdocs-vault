---
title: Cocoa Event Handling Guide
apple_id: 10000060i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/MonitoringEvents/MonitoringEvents.html
archived_at: '2026-07-15T07:15:36.392657Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Event Handling Guide](Introduction.md)


[Next](Text%20System%20Defaults%20and%20Key%20Bindings.md)[Previous](Handling%20Trackpad%20Events.md)

# Monitoring Events

The AppKit framework allows you to install an event monitor, an object that looks for user-input events of a certain type (or types) as an application dispatches them in its [sendEvent:](https://developer.apple.com/documentation/appkit/nsapplication/1428359-sendevent) method. For example, a monitor could look for mouse-up, key-down, or swipe-gesture events, or even all events.

There are two kinds of event monitors, each differing in monitoring scope and capabilities:

- A _global event monitor_ looks for user-input events dispatched to applications other than the one in which it is installed. The monitor cannot modify an event or prevent its normal delivery. And it may only monitor key events if accessibility is enabled or if the application is trusted for accessibility.

  You install a global event monitor with the `NSEvent` class method [addGlobalMonitorForEventsMatchingMask:handler:](https://developer.apple.com/documentation/appkit/nsevent/1535472-addglobalmonitorforevents).
- A _local event monitor_ looks at user-input events that are being dispatched to the application in which the monitor is installed. For a given event object of interest, the local monitor can return the object unmodified, create and return a new `NSEvent` object, or return `nil` to stop the dispatching of the event.

  You install a local event monitor with the `NSEvent` class method [addLocalMonitorForEventsMatchingMask:handler:](https://developer.apple.com/documentation/appkit/nsevent/1534971-addlocalmonitorforeventsmatching).

The parameters of both monitor-installation methods are nearly identical. The first parameter is an event mask for specifying the events of interest by type. The second parameter defines a block that performs the handling of monitored events; it is called for each new event that matches one of the specified types. For both methods, an `NSEvent` object is the sole argument of the block. However, the block handler for [addLocalMonitorForEventsMatchingMask:handler:](https://developer.apple.com/documentation/appkit/nsevent/1534971-addlocalmonitorforeventsmatching) is typed to return an `NSEvent` object while the block handler for the global method returns `void`. The handlers are always called on the main thread. Both class methods return the monitor object, which the calling object does not own (and thus has no need to retain or release).

There are many scenarios where an event monitor might be useful to an application. One example is a pop-up window that acts like a menu. The application wants to know when the user clicks outside of that window so it can dismiss it. It also wants to know if the user presses the Escape key (to dismiss it without saving changes) or if the user presses the Enter key (to dismiss it and save changes). The _[AnimatedTableView](../../../samplecode/AnimatedTableView/AnimatedTableView.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobwgm)_ sample code project installs a local event monitor (in `ATColorTableController.m`) that performs these functions. Listing 9-1 shows how it does this.

__Listing 9-1__  Installing a local event monitor

```objc
- (void)editColor:(NSColor *)color locatedAtScreenRect:(NSRect)rect {

    // code unrelated to event monitoring deleted here.....

    // Start watching events to figure out when to close the window
    NSAssert(_eventMonitor == nil, @"_eventMonitor should not be created yet");
    _eventMonitor = [NSEvent addLocalMonitorForEventsMatchingMask:
            (NSLeftMouseDownMask | NSRightMouseDownMask | NSOtherMouseDownMask | NSKeyDownMask)
            handler:^(NSEvent *incomingEvent) {
        NSEvent *result = incomingEvent;
        NSWindow *targetWindowForEvent = [incomingEvent window];
        if (targetWindowForEvent != _window) {
            [self _closeAndSendAction:NO];
        } else if ([incomingEvent type] == NSKeyDown) {
            if ([incomingEvent keyCode] == 53) {
                // Escape
                [self _closeAndSendAction:NO];
                result = nil; // Don't process the event
            } else if ([incomingEvent keyCode] == 36) {
                // Enter
                [self _closeAndSendAction:YES];
                result = nil;
            }
        }
        return result;
    }];
}
```

When the window is closed, the application has no more need for the event monitor. So it posts a notification when it closes the window. The method in Listing 9-2 is invoked as a result of this notification, and the class implements it to remove the event monitor (among other things).

__Listing 9-2__  Removing an event monitor

```objc
- (void)_windowClosed:(NSNotification *)note {
    if (_eventMonitor) {
        [NSEvent removeMonitor:_eventMonitor];
        _eventMonitor = nil;
    }
    [[NSNotificationCenter defaultCenter] removeObserver:self name:NSWindowWillCloseNotification object:_window];
    [[NSNotificationCenter defaultCenter] removeObserver:self name:NSApplicationDidResignActiveNotification object:nil];
}
```

Although event monitoring can be the ideal solution for some problems, it might not be the best for other ones. For example, the _[AnimatedTableView](../../../samplecode/AnimatedTableView/AnimatedTableView.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobwgm)_ application installs a local event monitor, which can detect mouse events sent to the application but cannot detect mouse events sent to other applications. But the application needs to dismiss the window if the user clicks in another application. To do this, _AnimatedTableView_ observes the [NSApplicationDidResignActiveNotification](https://developer.apple.com/documentation/appkit/nsapplicationdidresignactivenotification) notification instead of installing a global event monitor. A global event monitor would not be able to detect Command-Tab or a system alert, both of which should cause the window to be dismissed. Event monitors should be used only when there is no other way to solve your problem.

[Next](Text%20System%20Defaults%20and%20Key%20Bindings.md)[Previous](Handling%20Trackpad%20Events.md)

