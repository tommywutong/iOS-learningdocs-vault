---
title: Allowing OpenGL applications to utilize the integrated GPU
apple_id: DTS40010791
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2013-01-31'
source_url: https://developer.apple.com/library/archive/qa/qa1734/_index.html
archived_at: '2026-07-18T02:34:31.476369Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1734

# Allowing OpenGL applications to utilize the integrated GPU

## Q:  The 15-inch and 17-inch MacBook Pro models shipped Early 2011 and after come standard with 2 GPUs, one integrated and one discrete. How can I run my OpenGL application on the integrated GPU if it is possible?

A: Starting with OS X 10.7, you may choose to run your OpenGL application on the integrated GPU on the dual-GPU MacBook Pros shipped Early 2011 and after.

By default, once your application creates an OpenGL context (by either calling OpenGL directly or an API that relies on OpenGL such as Core Animation, Core Image, etc), the MacBook Pro automatically switches to the higher-end discrete GPU for performance concerns and won't switch back until the application quits. On OS X 10.6 and earlier, you are not allowed to choose to run on the integrated GPU instead. Starting with OS X 10.7, you may utilize the integrated GPU on the MacBook Pros if you want to, for example, to save battery life.

On OS X 10.7 and later, there is a new attribute called `NSSupportsAutomaticGraphicsSwitching`. To allow your OpenGL application to utilize the integrated GPU, you must add in the Info.plist of your application this key with a `Boolean` value of `true`, as shown in the following:

__Figure 1__  Adding the `NSSupportsAutomaticGraphicsSwitching` key in Info.plist.

!

Additionally, you must make sure that your application works correctly with multiple GPUs or else the system may continue forcing your application to use the discrete GPU. [TN2229 Supporting Multiple GPUs on Mac OS X](https://developer.apple.com/library/mac/#technotes/tn2008/tn2229.html) discusses in detail the required steps that you need to follow. You're highly recommended to check it out.

Features that are available on the discrete GPU may not be available on the integrated GPU. You must check that features you desire to use exist on the GPU you are using. For a complete listing of supported features by GPU class, please see: [OpenGL Capabilities Tables](https://developer.apple.com/graphicsimaging/opengl/capabilities/).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-01-31 | Updated to include dual-GPU MBPs shipped after Feb 2011. |
| 2011-04-05 | Added the link to OpenGL Capabilities Tables. |
| 2011-03-18 | New document that describes the required steps to allow OpenGL applications to utilize the integrated GPU on Mac OS X Lion and later. |

