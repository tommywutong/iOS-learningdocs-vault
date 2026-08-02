---
title: Why does my app launch to a black screen on iOS 4?
apple_id: DTS40010216
resource_type: QA
platform: iOS|macOS
topic: User Experience
technology: null
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/qa/qa1709/_index.html
archived_at: '2026-07-18T02:34:16.780016Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1709

# Why does my app launch to a black screen on iOS 4?

## Q:  Why does my app launch to a black screen on iOS 4?

A: Why does my app launch to a black screen on iOS 4?

While setting your main window to be visible at launch has always been a requirement, earlier versions of iOS didn't strictly enforce this. In iOS 4, not setting your main window to be visible at launch will result in your application launching to a black screen and your main window not becoming the first responder.

If your app is launching to a black screen, make sure you have one of the following methods implemented.

In the App Delegate's `-applicationDidFinishLaunching:` or `-application:didFinishLaunchingWithOptions:` method, make sure you call `[window makeKeyAndVisible]`.

This will set the main window as visible on launch and will make it the first responder.

If you have no need to use `-applicationDidFinishLaunching:` or `-application:didFinishLaunchingWithOptions:`, or you would rather set the window to be visible and the first responder in Interface Builder:

1. Open MainWindow.xib in Interface Builder.
2. Select the Window object in the Document window (see Figure 1).
3. On the Attributes tab of the Inspector palette, set the "Visible at Launch" checkbox to __checked__ (see Figure 2).
4. Save MainWindow.xib.

Setting your main window to "Visible at Launch" in Interface Builder is the same as calling `makeKeyAndVisible` on the window in Xcode. There is no need to have it set in both places. Choose the one that makes the most sense for your needs.

__Figure 1__  The Document window with the Window object selected.

!

__Figure 2__  The Inspector palette with "Visible at Launch" checked.

!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-07-28 | New document that shows how to resolve a black screen on launch by making your main window the first responder and visible on launch. |

