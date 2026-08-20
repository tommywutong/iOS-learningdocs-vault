---
title: Why does my app launch to a black screen on iPad?
apple_id: DTS40013496
resource_type: QA
platform: iOS
topic: Xcode
technology: null
published: '2013-07-25'
source_url: https://developer.apple.com/library/archive/qa/qa1780/_index.html
archived_at: '2026-07-18T02:34:43.817439Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1780

# Why does my app launch to a black screen on iPad?

## Q:  Why does my app launch to a black screen on iPad?

A: Apps that have been designed only for iPhone may launch to a blank screen when run on an iPad. This is caused by the presence of an empty iPad specific storyboard in the app bundle as well as an iPad specific  `UIMainStoryboardFile` key in the app's Information Property List (`Info.plist`) file. Both are automatically created by the various Xcode template projects if the __Universal__ option is selected.

If your iPhone app is launching to a black screen on iPad, follow these steps to remove the extraneous iPad specific resources.

__In Xcode__

Look for a file named `MainStoryboard_iPad.storyboard` in the file navigator. If this file is present, remove it from your project.

__In In your app's Information Property List__

Look for a key named `Main storyboard file base name (iPad)` or `UIMainStoryboardFile~ipad`. If this key is present, remove it. You should also remove any other key suffixed with `(iPad)` or `~ipad`.

Finally, test your app on an iPad or in the iPad simulator and verify that it behaves as expected.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-07-25 | New document that shows how to determine if an extraneous storyboard is causing your app to launch to a blank screen. |

