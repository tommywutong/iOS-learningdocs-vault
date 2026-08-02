---
title: Launch Image Doesn't Show Up for iPhone Apps
apple_id: DTS40010233
resource_type: QA
platform: iOS
topic: User Experience
technology: null
published: '2013-08-06'
source_url: https://developer.apple.com/library/archive/qa/qa1700/_index.html
archived_at: '2026-07-18T02:34:12.331303Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1700

# Launch Image Doesn't Show Up for iPhone Apps

## Q:  Why does my Default-Landscape.png not show up as the landscape launch image for my iPhone app?

A: iPhone apps, as well as universal apps running on iPhone, always launch in portrait. After launch, the system rotates the app's interface to a supported orientation before displaying the first view controller if it determines that the app does not support portrait orientation. For this reason, launch images with orientation modifiers are unnecessary and are ignored on iPhone. If your app starts in an orientation other than portrait, you should use your preferred graphics editing software to rotate the content of the app's iPhone launch image while keeping the image's size consistent with a portrait launch image (height > width).

For more information on configuring your app to launch in landscape see [TN2244: Launching your Application in Landscape](https://developer.apple.com/library/ios/#technotes/tn2244/_index.html).

For more information on providing launch images, see "Provide Launch Images" on [QA1588: Automatic orientation support for iPhone and iPad apps](https://developer.apple.com/library/ios/#qa/qa1588/_index.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-08-06 | Fixed a broken link. |
| 2013-06-06 | Editorial changes to remove ambiguity. |
| 2010-08-06 | New document that explains why launch images may not show up for iPhone Apps. |

