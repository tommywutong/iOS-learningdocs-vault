---
title: Responding to screen capture in iOS 11.
apple_id: DTS40017687
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: ReplayKit
published: '2017-10-25'
source_url: https://developer.apple.com/library/archive/qa/qa1970/_index.html
archived_at: '2026-07-18T02:38:00.986361Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1970

# Responding to screen capture in iOS 11.

## Q:  How can I prevent my application's content from being captured by screen recording, AirPlay, or Screen Mirroring?

A: The iOS 11 SDK introduces new APIs on `UIScreen` that applications can use to know when the screen is being captured:

- [UIScreen.isCaptured Instance Property](https://developer.apple.com/documentation/uikit/uiscreen/2921651-iscaptured)

  When the value of this property is `true`, the contents of this screen are actively being recorded, mirrored, or sent over AirPlay. This property will return `true` in the following cases:

  - If the screen is being recorded using the Screen Recording Control in the iOS Control Center as discussed in the following support document: [How to record the screen on your iPhone, iPad, or iPod touch](https://support.apple.com/en-us/HT207935).
  - If the screen is being recorded using QuickTime Player over a Lightning cable as discussed in the following support document: [How to use QuickTime Player](https://support.apple.com/en-us/HT201066).
  - If the screen is being displayed using AirPlay or Screen Mirroring as discussed in the following support document: [Use AirPlay or Screen Mirroring on your iPhone, iPad, or iPod touch](https://support.apple.com/en-us/HT204289).
  - If the screen is being cloned to another destination.
- [UIScreenCapturedDidChange Notification Type Property](https://developer.apple.com/documentation/foundation/nsnotification.name/2921652-uiscreencaptureddidchange)

  UIKit sends the `UIScreenCapturedDidChange` notification when the capture status of the screen changes.

  The object of the notification is the `UIScreen` object whose `isCaptured` property changed. There is no `userInfo` dictionary.

Your application can then handle this change and prevent your application content from being captured in whatever way is appropriate for your use.

For example, if you are a media application you would observe changes to `UIScreen.isCaptured` and if its value is `true` you could stop playback and present a useful dialog to the user letting them know that playback was paused due to being captured.

If your application uses FairPlay Streaming (FPS) your video content will automatically not be captured by the iOS 11 screen recording feature or QuickTime Player on macOS. The portion of your application that is playing the content will be blacked out.

To learn more about FairPlay Streaming see the [FairPlay Streaming](https://developer.apple.com/streaming/fps/) page on the Apple Developer website.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-10-25 | New document that this document discusses how applications can use new APIs in the iOS 11 SDK to respond to being captured by AirPlay Mirroring and screen recording. |

