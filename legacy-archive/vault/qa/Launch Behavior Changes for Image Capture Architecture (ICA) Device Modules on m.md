---
title: Launch Behavior Changes for Image Capture Architecture (ICA) Device Modules
  on macOS Sierra 10.12
apple_id: DTS40017582
resource_type: QA
platform: macOS
topic: General
technology: ImageCaptureCore
published: '2016-12-06'
source_url: https://developer.apple.com/library/archive/qa/qa1946/_index.html
archived_at: '2026-07-18T02:37:25.159123Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1946

# Launch Behavior Changes for Image Capture Architecture (ICA) Device Modules on macOS Sierra 10.12

## Q:  I’ve installed my ICA device module to /Library/Image Capture/Devices/ on macOS Sierra 10.12. However, when macOS detects a compatible device is available (for example, when the user connects a device to the Mac via USB cable), my device module is not automatically launched. What’s going on?

A: For performance reasons, on macOS Sierra 10.12 and later, device modules are only launched on-demand, when the user is interested in using the particular hardware.

For example, a device module will be launched when the Image Capture app is opened by the user and the device is selected. When the device is deselected, or the user has closed the application using the hardware, the device module will terminate.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-12-06 | New document that discusses changes to Image Capture Architecture (ICA) Device Modules launch behavior on macOS Sierra 10.12. |

