---
title: Why isn't my ColorSync CMM recognized on Mac OS X 10.5?
apple_id: DTS10004497
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2007-10-26'
source_url: https://developer.apple.com/library/archive/qa/qa1557/_index.html
archived_at: '2026-07-18T02:32:18.178459Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1557

# Why isn't my ColorSync CMM recognized on Mac OS X 10.5?

## Q:  I've successfully written and deployed a color management module (CMM) on Mac OS X 10.4. However, when I install my CMM on Mac OS X 10.5 it is no longer called. Please explain.

A: I've successfully written and deployed a color management module (CMM) on Mac OS X 10.4. However, when I install my CMM on Mac OS X 10.5 it is no longer called. Please explain.

ColorSync has defined new CMM interfaces for Mac OS X 10.5. These can be found in the CMMComponent.h interface file. You'll need to update your CMM with these new interfaces in order for it to work properly on Mac OS X 10.5.

However, it is possible to create a __single__ CMM that will work on both Mac OS X 10.4 & Mac OS X 10.5 simply by implementing both sets of interfaces. See the DemoCMM sample code (`/Developer/Examples/ColorSync/DemoCMM`) for such an example. This sample is available as part of the Xcode 3.0 Developer Tools installation on Mac OS X 10.5.

- [Advanced Color Imaging On the Mac OS](https://developer.apple.com/dev/techsupport/insidemac/ACI/ACI-2.html)
- [TN 2035 ColorSync On Mac OS X](https://developer.apple.com/technotes/tn/tn2035.html)
- DemoCMM sample code (`/Developer/Examples/ColorSync/DemoCMM`) installed as part of the [Xcode Tools](https://developer.apple.com/tools/xcode/index.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-10-26 | New document that discusses how to upgrade your ColorSync CMM to run on Mac OS X 10.5 |

