---
title: Finding an NSView's current magnification.
apple_id: DTS10003322
resource_type: QA
platform: macOS
topic: User Experience
technology: null
published: '2009-07-24'
source_url: https://developer.apple.com/library/archive/qa/qa1346/_index.html
archived_at: '2026-07-18T02:30:25.545302Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1346

# Finding an NSView's current magnification.

## Q:  How can I find out what the current scale of an NSView's coordinate space is, if it's been changed from the default?

A: How can I find out what the current scale of an NSView's coordinate space is, if it's been changed from the default?

NSView provides a method, `-convertSize:fromView:`, to convert sizes between the coordinate spaces of various views in a window. If you convert a known size from the window's base coordinate space to that of the NSView, the result is the current zoom level.

Another NSView method, `-scaleUnitSquareToSize:`, sets the magnification relative to the view's existing coordinate system. By using an Objective-C category to add a few methods to NSView, we can provide a convenient API to scale NSView instances in absolute terms.

__Listing 1__  ScaleUtilities category declaration

```objc
@interface NSView (ScaleUtilities) @property (assign) NSSize scale; - (void)resetScaling; @end
```


__Listing 2__  ScaleUtilities category implementation

```objc
@implementation NSView (ScaleUtilities)  static const NSSize unitSize = {1.0, 1.0};  // Returns the scale of the receiver's coordinate system, relative to the window's base coordinate system. - (NSSize)scale; {     return [self convertSize:unitSize toView:nil]; }  // Sets the scale in absolute terms. - (void)setScale:(NSSize)newScale; {     [self resetScaling]; // First, match our scaling to the window's coordinate system     [self scaleUnitSquareToSize:newScale]; // Then, set the scale.     [self setNeedsDisplay:YES]; // Finally, mark the view as needing to be redrawn }  // Makes the scaling of the receiver equal to the window's base coordinate system. - (void)resetScaling; {     [self scaleUnitSquareToSize:[self convertSize:unitSize fromView:nil]]; }  @end
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-07-24 | Updated code to use properties, width-agnostic scalars, and whitespace. Moved setNeedsDisplay: to "setScale:" and removed "scalePercent" property. |
| 2005-03-08 | Fixed a typo in the captions for the listings. |
| 2004-12-13 | There was a mistake in the implementation of -resetScaling. I was doing a -convertSize:toView: that should have been a -convertSize:fromView: |
| 2004-10-14 | New document that explains how to discover the current magnification (zoom level) of any NSView. |

