---
title: Window Programming Guide
apple_id: 10000031i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-11-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Articles/SettingWindowCollectionBehavior.html
archived_at: '2026-07-15T07:21:07.849182Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Window Programming Guide](Introduction.md)


[Next](Sizing%20and%20Placing%20Windows.md)[Previous](Window%20Layers%20and%20Levels.md)

# Setting Window Collection Behavior

The are a number of different options that can be set regarding the window collection behavior of a window. They include a window’s behavior when using Spaces, Exposé, and the “Cycle Through Windows” command. These options can be set using the [setCollectionBehavior:](https://developer.apple.com/documentation/appkit/nswindow/1419471-collectionbehavior) method of [NSWindow](https://developer.apple.com/documentation/appkit/nswindow), by passing in at most one constant from each group, combined using bitwise or operators. The current options may be accessed via the [collectionBehavior](https://developer.apple.com/documentation/appkit/nswindow/1419471-collectionbehavior) method.

There are three options that can be set for a window’s Spaces collection behavior. The default is [NSWindowCollectionBehaviorDefault](https://developer.apple.com/documentation/appkit/nswindowcollectionbehavior/nswindowcollectionbehaviordefault), which allows the window to be associated with one space at a time. The second option is [NSWindowCollectionBehaviorCanJoinAllSpaces](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior/1419246-canjoinallspaces). This option causes the window to appear on all spaces, like the menu bar. The third option is [NSWindowCollectionBehaviorMoveToActiveSpace](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior/1419120-movetoactivespace). This causes the window to switch to the active space when it is made active. Only one of these options may be used at a time.

If a window is currently associated with the active space, [isOnActiveSpace](https://developer.apple.com/documentation/appkit/nswindow/1419707-onactivespace) returns `YES`. Otherwise, it returns `NO`. Additionally, you can get an array of the window numbers of windows on one or all spaces using the method [windowNumbersWithOptions:](https://developer.apple.com/documentation/appkit/nswindow/1419678-windownumbers) and specified your desired options. The possible options are specified by [NSWindowNumberListOptions](https://developer.apple.com/documentation/appkit/nswindownumberlistoptions).

There are also three options that can be set for a window’s Exposé collection behavior. If a window has a window level of [NSNormalWindowLevel](https://developer.apple.com/documentation/appkit/nsnormalwindowlevel), the default behavior is [NSWindowCollectionBehaviorManaged](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior/1419505-managed), which causes the window to participate in both Spaces and Exposé. [NSWindowCollectionBehaviorTransient](https://developer.apple.com/documentation/appkit/nswindowcollectionbehavior/nswindowcollectionbehaviortransient) causes the window to float in Spaces and be hidden in Exposé. This is the default behavior if the window level is not [NSNormalWindowLevel](https://developer.apple.com/documentation/appkit/nsnormalwindowlevel). The final option is [NSWindowCollectionBehaviorStationary](https://developer.apple.com/documentation/appkit/nswindowcollectionbehavior/nswindowcollectionbehaviorstationary), which causes the window to be unaffected by Exposé; i.e. it stays visible and does not move, like the desktop window. Only one of these options may be used at a time.

There are two options: [NSWindowCollectionBehaviorParticipatesInCycle](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior/1419250-participatesincycle) and [NSWindowCollectionBehaviorIgnoresCycle](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior/1419396-ignorescycle). These options cause the window to participate in the window cycle for the “Cycle Through Windows” menu option or not participate in it, respectively.

[Next](Sizing%20and%20Placing%20Windows.md)[Previous](Window%20Layers%20and%20Levels.md)

