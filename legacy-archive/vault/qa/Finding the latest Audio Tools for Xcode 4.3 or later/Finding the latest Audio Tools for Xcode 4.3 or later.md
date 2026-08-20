---
title: Finding the latest Audio Tools for Xcode 4.3 or later
apple_id: DTS40011954
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2012-10-04'
source_url: https://developer.apple.com/library/archive/qa/qa1731/_index.html
archived_at: '2026-07-18T02:34:30.163286Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1731

# Finding the latest Audio Tools for Xcode 4.3 or later

## Q:  I'm looking for AU Lab and the Public Utility sources to build CoreAudio samples, where do I find the latest Audio Tools?

A: AU Lab and HALLab are now part of the "Audio Tools for Xcode" disk image download.

Developers may download the latest Audio Tools for Xcode directly from inside of Xcode by selecting the menu item "More Developer Tools..." in Xcode as shown in Figure 1.

__Figure 1__  Selecting More Developer Tools from the Xcode->Open Developer Tool Menu.

!

For more information, see the [Xcode Release Notes](https://developer.apple.com/library/ios/documentation/DeveloperTools/Conceptual/WhatsNewXcode/WhatsNewXcode.pdf)

The CoreAudio folder containing the latest version of the Public Utility sources (PublicUtility folder) as well as base classes required for codec and audio unit development may be found in either the OS X Developer Library or the iOS Developer Library under Sample Code Resources.

[Core Audio Utility Classes](https://developer.apple.com/library/mac/#samplecode/CoreAudioUtilityClasses/Introduction/Intro.html#//apple_ref/doc/uid/DTS40012328)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-10-04 | Updated for Xcode 4.5 |
| 2012-03-08 | Editorial |
| 2012-03-06 | New document that describes how to download the latest Audio Tools for Xcode 4.3 or later |

