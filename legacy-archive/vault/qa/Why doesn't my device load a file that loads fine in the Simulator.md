---
title: Why doesn't my device load a file that loads fine in the Simulator?
apple_id: DTS40010041
resource_type: QA
platform: iOS
topic: General
technology: null
published: '2010-06-01'
source_url: https://developer.apple.com/library/archive/qa/qa1697/_index.html
archived_at: '2026-07-18T02:34:12.179806Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1697

# Why doesn't my device load a file that loads fine in the Simulator?

## Q:  Why doesn't my device load a file that loads fine in the Simulator?

A: Why doesn't my device load a file that loads fine in the Simulator?

Two things should be kept in mind when accessing files in application bundles using the Simulator versus a device.

__Case-sensitivity:__ iPhone OS uses a case-sensitive file system, unlike the Simulator which uses a case-insensitive file system by default. Make sure the case-sensitivity of resources accessed within code matches the filename case-sensitivity.

For example, if our filename is "YourExampleImage.png":

- Good: `[UIImage imageNamed:@"YourExampleImage.png"]`
- Bad: `[UIImage imageNamed:@"YourExampleImage.PNG"]`
- Bad: `[UIImage imageNamed:@"yourexampleimage.png"]`

__Location:__ Methods that require a path should be accessed using the `-[pathForResource:ofType:inDirectory:]` method of `NSBundle`. They should not be accessed using a string representation of the filename.

__Listing 1__  Accessing Default.png from within an application bundle.

```
UIImage *defaultImage = [UIImage imageWithContentsOfFile:[[NSBundle mainBundle] pathForResource:@"Default" ofType:@"png" inDirectory:nil]];
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-06-01 | New document that shows how to avoid issues where an app's resources load fine in the Simulator, but not on a device. |

