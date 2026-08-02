---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Concepts/UsingPanels.html
archived_at: '2026-07-15T07:21:10.851660Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](How%20Window%20Controllers%20Work.md)[Previous](How%20Modal%20Windows%20Work.md)

# How Panels Work

A panel is a special kind of window, typically serving an auxiliary function in an application. The [NSPanel](https://developer.apple.com/documentation/appkit/nspanel) subclass of [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) adds a few special behaviors to windows in support of the role panels play:

- By default panels are not released when they’re closed, because they’re usually lightweight and often reused.
- Onscreen panels, except for alert dialogs, are removed from the screen when the application isn’t active and are restored when the application again becomes active. This reduces screen clutter.

  Specifically, the [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) implementation of the [hidesOnDeactivate](https://developer.apple.com/documentation/appkit/nswindow/1419777-hidesondeactivate) method returns `NO`, but the [NSPanel](https://developer.apple.com/documentation/appkit/nspanel) implementation of the same method returns `YES`.
- Panels can become the key window, but they cannot become the main window.
- If a panel is the key window and has a close button, it closes itself when the user presses the Escape key.

In addition to these automatic behaviors, the `NSPanel` class allows you to configure certain other behaviors common to some kinds of panels:

- You can prevent a panel from becoming the key window unless the user clicks in a view that responds to typing. This prevents the key window from shifting to the panel unnecessarily. The [setBecomesKeyOnlyIfNeeded:](https://developer.apple.com/documentation/appkit/nspanel/1528836-becomeskeyonlyifneeded) method controls this behavior.
- Palettes and similar panels can be made to float above standard windows and other panels. This prevents them from being covered and keeps them readily available to the user. The [setFloatingPanel:](https://developer.apple.com/documentation/appkit/nspanel/1531901-isfloatingpanel) method controls this behavior.
- A panel can be made to receive mouse and keyboard events even when another window or panel is being run modally or in a modal session. This permits actions in the panel to affect the modal window or panel. The [setWorksWhenModal:](https://developer.apple.com/documentation/appkit/nspanel/1525549-workswhenmodal) method controls this behavior. See [How Modal Windows Work](How%20Modal%20Windows%20Work.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgizdglkdjjbekqkeijaq) for more information on modal windows and panels.

[Next](How%20Window%20Controllers%20Work.md)[Previous](How%20Modal%20Windows%20Work.md)

