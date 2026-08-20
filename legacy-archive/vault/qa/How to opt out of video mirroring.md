---
title: How to opt out of video mirroring
apple_id: DTS40010848
resource_type: QA
platform: iOS
topic: User Experience
technology: null
published: '2011-04-04'
source_url: https://developer.apple.com/library/archive/qa/qa1738/_index.html
archived_at: '2026-07-18T02:34:32.327159Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1738

# How to opt out of video mirroring

## Q:  How do I opt out of video mirroring when using the Apple Digital AV Adapter with a compatible iOS device?

A: On compatible devices, iOS will automatically mirror the display when an external screen is attached. If you do not wish your application's contents to be mirrored, your application must present alternate content on the external display in place of the default content. To do so, use the normal process for displaying content on an external display as described in [Displaying Content on an External Display](https://developer.apple.com/library/ios/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/CreatingWindows/CreatingWindows.html#//apple_ref/doc/uid/TP40009503-CH4-SW9) in the [View Programming Guide for iOS](https://developer.apple.com/library/ios/#documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009503-CH1-SW2).

We recommend you display appropriate content so the user isn't simply greeted by a black screen. For example, show auxiliary information about the video, or at minimum, a static image or suitable text ("Video mirroring is not supported by this application" or similar).

The [ExternalDisplay sample code](https://developer.apple.com/library/ios/#samplecode/ExternalDisplay/Introduction/Intro.html) also demonstrates how to detect the presence of an external display, determine the available display resolutions, select a resolution, and show content on the display.

For example, to determine if the display is being mirrored, use the `respondsToSelector` method on the screen object to see if it responds to the `mirroredScreen` property as shown in Listing 1.

__Listing 1__  Using the `mirroredScreen` property to determine if the display is being mirrored.

```
UIScreen *aScreen;  NSArray *screens = [UIScreen screens]; for (aScreen in screens)  {     if ([aScreen respondsToSelector:@selector(mirroredScreen)]                && [aScreen mirroredScreen] == [UIScreen mainScreen])      {         // The main screen is being mirrored.     }     else      {         // The main screen is not being mirrored, or         // you are not running on a compatible device.     } }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-04-04 | New document that describes how to opt out of video mirroring. |

