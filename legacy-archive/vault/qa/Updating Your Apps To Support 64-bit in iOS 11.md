---
title: Updating Your Apps To Support 64-bit in iOS 11
apple_id: DTS40017691
resource_type: QA
platform: iOS
topic: General
technology: null
published: '2017-10-30'
source_url: https://developer.apple.com/library/archive/qa/qa1971/_index.html
archived_at: '2026-07-18T02:38:01.040386Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1971

# Updating Your Apps To Support 64-bit in iOS 11

## Q:  I see the message "The developer of this app needs to update it to work with IOS 11," and my app won't launch. What does this mean?

A: This message indicates that your app is built for 32-bit devices, and does not fully support 64-bit devices. Support for 32-bit apps is not available in iOS 11, and all 32-bit apps previously installed on a user’s device will not launch. We recommend submitting an update so your users can continue to run your app on iOS 11.

For assistance in performing this upgrade, please consult the following technical resources:

- _[64-Bit Transition Guide for Cocoa Touch](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaTouch64BitGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40013501)_
- _[Resolving Compatibility Problems on New OS Releases](https://developer.apple.com/library/archive/technotes/tn2456/_index.html#//apple_ref/doc/uid/DTS40017626)_
- [WWDC 2017: Platforms State of the Union](https://developer.apple.com/videos/play/wwdc2017/102/?time=192)

If you’ve hired or contracted a developer to build your app on your behalf, or you’re using a third-party tool or service to build the app, please contact your developer or the support team for the tool or service to perform this update.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-10-30 | New document that describes the 64-bit requirement for apps on iOS 11 |

