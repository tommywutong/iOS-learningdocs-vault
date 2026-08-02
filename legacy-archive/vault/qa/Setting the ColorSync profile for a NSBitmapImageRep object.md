---
title: Setting the ColorSync profile for a NSBitmapImageRep object
apple_id: DTS10003387
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/qa/qa1369/_index.html
archived_at: '2026-07-18T02:30:26.579224Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1369

# Setting the ColorSync profile for a NSBitmapImageRep object

## Q:  I'd like to associate a ColorSync profile with a given `NSBitmapImageRep` object for color-matching purposes. Is there a simple way to do this?

A: I'd like to associate a ColorSync profile with a given `NSBitmapImageRep` object for color-matching purposes. Is there a simple way to do this?

You can associate a ColorSync profile with a [NSBitmapImageRep](https://developer.apple.com/documentation/Cocoa/Reference/ApplicationKit/ObjC_classic/Classes/NSBitmapImageRep.html) object containing pixel data produced by decoding a TIFF, JPEG, GIF or PNG file using the `-setProperty:` method and the `NSImageColorSyncProfileData` property.

Here's a short code snippet showing how it's done:

__Listing 1__  Setting the ColorSync profile for a `NSBitmapImageRep` object.

```
// // imageRepWithProfileAtPath // // Associate a given file-based ColorSync profile with // a NSBitmapImageRep object // // Inputs: // //    aPath - file path for a ColorSync profile // // Outputs: // // - returns a new NSBitmapImageRep object, created  //    by copying the receiver and applying the ColorSync  //    profile.  @implementation NSBitmapImageRep (MoreColorMethods)  - (NSBitmapImageRep *) imageRepWithProfileAtPath:(NSString *) pathToProfile {     id result = [self copy];          // build a NSData object for our ColorSync profile file     id profile = [NSData dataWithContentsOfFile: pathToProfile];          // now set the ColorSync profile for the object     [result setProperty:NSImageColorSyncProfileData withValue:profile];      return [result autorelease]; }  @end
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2018-06-04 | Moved to Retired Documents Library. |
| 2004-09-08 | New document that setting the ColorSync profile for a NSBitmapImageRep object |

