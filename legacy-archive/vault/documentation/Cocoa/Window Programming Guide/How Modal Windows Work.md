---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Concepts/UsingModalWindows.html
archived_at: '2026-07-15T07:21:10.362438Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](How%20Panels%20Work.md)[Previous](How%20a%20Window%20is%20Displayed.md)

# How Modal Windows Work

You can make a whole window or panel run in application-modal fashion, using the application’s normal event loop machinery but restricting input to the modal window or panel. Modal operation is useful for windows and panels that require the user’s attention before an action can proceed. Examples include error messages and warnings, as well as operations that require input, such as open dialogs, or dialogs that apply to multiple windows.

There are two mechanisms for operating an application-modal window or panel. The first, and simpler, is to invoke the [runModalForWindow:](https://developer.apple.com/documentation/appkit/nsapplication/1428436-runmodal) method of [NSApplication](https://developer.apple.com/documentation/appkit/nsapplication), which monopolizes events for the specified window until one of [stopModal](https://developer.apple.com/documentation/appkit/nsapplication/1428489-stopmodal), [abortModal](https://developer.apple.com/documentation/appkit/nsapplication/1428753-abortmodal), or [stopModalWithCode:](https://developer.apple.com/documentation/appkit/nsapplication/1428748-stopmodalwithcode) is invoked, typically by a button’s action method. The `stopModal` method ends the modal status of the window or panel from within the event loop. It doesn’t work if invoked from a method invoked by a timer or by a distributed object because those mechanisms operate outside of the event loop. To terminate the modal loop in these situations, you can use `abortModal`. The `stopModal` method is typically invoked when the user clicks the OK button (or equivalent), `abortModal` when the user clicks the Cancel button (or presses the Escape key). These two methods are equivalent to `stopModalWithCode:` with the appropriate argument.

The second mechanism for operating a modal window or panel, called a _modal session_, allows the application to perform a long operation while it still sends events to the window or panel. Modal sessions are particularly useful for panels that allow the user to cancel or modify an operation. To begin a modal session, invoke [beginModalSessionForWindow:](https://developer.apple.com/documentation/appkit/nsapplication/1428418-beginmodalsession) on the application, which sets the window up for the session and returns an identifier used for other session-controlling methods. At this point, the application can run in a loop that performs the operation, invoking [runModalSession:](https://developer.apple.com/documentation/appkit/nsapplication/1428590-runmodalsession) on the application object on each pass so that pending events can be dispatched to the modal window. This method returns a code indicating whether the operation should continue, stop, or abort, which is typically established by the methods described above for `runModalForWindow:`. After the loop concludes, you can remove the window from the screen and invoke [endModalSession:](https://developer.apple.com/documentation/appkit/nsapplication/1428438-endmodalsession) on the application to restore the normal event loop.

The normal behavior of a modal window or session is to exclude all other windows and panels from receiving events. For windows and panels that serve as general auxiliary controls, such as menus and the Font panel, this behavior is overly restrictive. The user must be able to use menu key equivalents (such as those for Cut and for Paste) and change the font of text in the modal window, and this requires that non-modal panels be able to receive events. To support this behavior, an `NSWindow` subclass overrides the [worksWhenModal](https://developer.apple.com/documentation/appkit/nswindow/1419220-workswhenmodal) method to return `YES`. This allows the window to receive mouse and keyboard events even when a modal window is present. If a subclass needs to work when a modal window is present, it should generally be a subclass of [NSPanel](https://developer.apple.com/documentation/appkit/nspanel), not of [NSWindow](https://developer.apple.com/documentation/appkit/nswindow).

Modal windows and modal sessions provide different levels of control to the application and the user. Modal windows restrict all action to the window itself and any methods invoked from the window. Modal sessions allow the application to continue an operation while accepting input only through the modal session window. Beyond this, you can use distributed objects to perform background operations in a separate thread, while allowing the user to perform other actions with any part of the application. The background thread can communicate with the main thread, allowing the application to display the status of the operation in a non-modal panel, perhaps including controls to stop or affect the operation as it occurs. Note that because AppKit isn’t thread-safe, the background thread should communicate with a designated object in the main thread that in turn interacts with the AppKit.

Before OS X version 10.6, if a modal window was open, application termination would be prevented if the user attempted to terminate that window’s application. Beginning in OS X version 10.6, you can call [setPreventsApplicationTerminationWhenModal:](https://developer.apple.com/documentation/appkit/nswindow/1419743-preventsapplicationterminationwh) with a value of `NO`, and the window will not prevent application termination when modal. The current value of this property may be accessed by calling [preventsApplicationTerminationWhenModal](https://developer.apple.com/documentation/appkit/nswindow/1419743-preventsapplicationterminationwh). The default value is `NO`.

[Next](How%20Panels%20Work.md)[Previous](How%20a%20Window%20is%20Displayed.md)

