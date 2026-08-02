---
title: How to take an image snapshot of the screen on Mac OS X Lion
apple_id: DTS40011008
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2011-08-10'
source_url: https://developer.apple.com/library/archive/qa/qa1741/_index.html
archived_at: '2026-07-18T02:34:32.506194Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1741

# How to take an image snapshot of the screen on Mac OS X Lion

## Q:  How do I take an image snapshot of the screen on Mac OS X Lion?

A: On Mac OS X Lion, the way to make an image snapshot from the screen is by employing [Quartz Display Services](https://developer.apple.com/library/mac/#documentation/GraphicsImaging/Reference/Quartz_Services_Ref/Reference/reference.html).

Make sure you add the ApplicationServices framework in your Xcode project and import the `ApplicationServices/ApplicationServices.h` header file.

Given a display ID (of `CGDirectDisplayID` type), you can call `CGDisplayCreateImage` to create a CGImage from the entire screen or `CGDisplayCreateImageForRect` from a rectangular portion of it.

If you always capture from the main display, you may simply pass `kCGDirectMainDisplay` to either function as shown in Listing 1. It is a shorthand for specifying the current main display.

If you might capture from a secondary display, then you can go through the list of active displays returned from `CGGetActiveDisplayList` and find the one you want to capture. See Listing 2 for an example.

__Listing 1__  Creating an image from the entire main display

```
CGImageRef image = CGDisplayCreateImage(kCGDirectMainDisplay);
```


__Listing 2__  Creating images from multiple displays

```
CGDisplayCount displayCount; CGDirectDisplayID displays[32];  // grab the active displays CGGetActiveDisplayList(32, displays, &displayCount);  // go through the list for (int i=0; i<displayCount; i++)  {     // make a snapshot of the current display     CGImageRef image = CGDisplayCreateImage(displays[i]);      // do something with the snapshot image }
```

Check out the dedicated sample code, [ScreenSnapshot](https://developer.apple.com/library/mac/#samplecode/ScreenSnapshot/Introduction/Intro.html), for more information. It demonstrates how to use Quartz Display Services to obtain an image containing the contents of any of the connected displays and allows the user to save the image to a file on disk.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-08-10 | Corrected a link. Added information about the ScreenSnapshot sample. |
| 2011-05-13 | New document that shows how to take an image snapshot of the screen on Mac OS X Lion |

