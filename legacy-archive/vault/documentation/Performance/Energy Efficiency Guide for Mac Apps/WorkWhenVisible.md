---
title: Energy Efficiency Guide for Mac Apps
apple_id: TP40013929
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/WorkWhenVisible.html
archived_at: '2026-07-18T01:50:31.559119Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for Mac Apps](index.md)



## Notify Your App When Visibility Changes

As soon as your app or any of its windows becomes hidden, your app should immediately halt any work that is no longer useful. A good example of this is Photo Booth, which turns off the camera and stops rendering graphical effects when its window is completely covered, or _occluded_. When your app becomes visible again, it can immediately refresh its content and resume any power-intensive operations.

### What Makes an App Hidden

Your app is considered hidden from the user when:

- Windows of other apps occlude the windows of your app
- The screen saver is on (thereby occluding all apps’ windows)
- Your app is in a Mission Control space where the user isn’t working

### Register for App-Level Occlusion Notifications

To receive notifications about changes in your app’s visibility, implement the [applicationDidChangeOcclusionState:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428362-applicationdidchangeocclusionsta) method in your app delegate (see [NSApplicationDelegate](https://developer.apple.com/documentation/appkit/nsapplicationdelegate) and Listing 5-1). Upon receiving a notification from this method, your app should check whether the [NSApplicationOcclusionStateVisible](https://developer.apple.com/documentation/appkit/nsapplicationocclusionstate/nsapplicationocclusionstatevisible) constant is set.

__Listing 5-1__Checking for app visibility with the `applicationDidChangeOcclusionState` method

Objective-C

1. `- (void)applicationDidChangeOcclusionState:(NSNotification *)notification`
2. `{`
3. `if ([NSApp occlusionState] & NSApplicationOcclusionStateVisible) {`
4. `// The app is visible; continue doing work`
5. `} else {`
6. `// The app is not visible; stop doing work }`
7. `}`

Swift

1. `func applicationDidChangeOcclusionState(notification: NSNotification)`
2. `{`
3. `if (NSApp.occlusionState & NSApplicationOcclusionStateVisible != nil) {`
4. `// The app is visible; continue doing work`
5. `} else {`
6. `// The app is not visible; stop doing work }`
7. `}`

If the `NSApplicationOcclusionStateVisible` constant is set (`TRUE`), it means that at least part of a window owned by your app is visible, so your app can continue working. If this constant is not set (`FALSE`), it means that no part of any window owned by your app is visible. Your app should halt its operations and calculations because the user won’t be able to see the results.

> [!NOTE]
> 

### Register for Window-Level Occlusion Notifications

Implement the [windowDidChangeOcclusionState:](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419424-windowdidchangeocclusionstate) method in your window delegates to receive notifications about changes in individual window visibility, as shown in Listing 5-2. On receiving notifications, your app should check whether the [NSWindowOcclusionStateVisible](https://developer.apple.com/documentation/appkit/nswindowocclusionstate/nswindowocclusionstatevisible) constant is set. If it’s set, at least part of the window is visible. If the constant is not set, no part of the window is visible and your app should halt all work performed in that window.

__Listing 5-2__Checking for window visibility with the `windowDidChangeOcclusionState` method

Objective-C

1. `- (void)windowDidChangeOcclusionState:(NSNotification *)notification`
2. `{`
3. `if ([self.window occlusionState] & NSWindowOcclusionStateVisible) {`
4. `// The window is visible; continue doing work`
5. `} else {`
6. `// The window is not visible; stop doing work }`
7. `}`

Swift

1. `func windowDidChangeOcclusionState(notification: NSNotification)`
2. `{`
3. `if (self.window.occlusionState & NSWindowOcclusionStateVisible != nil) {`
4. `// The window is visible; continue doing work`
5. `} else {`
6. `// The window is not visible; stop doing work }`
7. `}`

> [!NOTE]
> 

[Notify Your App When Active State Changes](WorkWhenActive.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmjxfvjvomi)

[Minimize I/O](MinimizingIO.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmrwfvjvomi)
