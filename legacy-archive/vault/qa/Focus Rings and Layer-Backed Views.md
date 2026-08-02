---
title: Focus Rings and Layer-Backed Views
apple_id: DTS40013936
resource_type: QA
platform: macOS
topic: User Experience
technology: AppKit
published: '2018-02-21'
source_url: https://developer.apple.com/library/archive/qa/qa1785/_index.html
archived_at: '2026-07-18T02:34:45.354843Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1785

# Focus Rings and Layer-Backed Views

## Q:  Why is my custom layer-backed view's focus ring drawn incorrectly? How can I fix this?

A: Before OS X 10.7, you would draw your view's focus ring by implementing NSView's `-drawRect:` method and using for example `NSSetFocusRingStyle`/`NSRectFill`. When a view draws a focus ring, it draws it as part of its drawRect method. When the drawing is being targeted into a layer, however, the focus ring cannot extend outside of that layer. This result is a thin, incorrect focus ring in layer-backed mode.

Starting with OS X 10.7 you can use AppKit APIs to draw your focus ring to automatically ensure consistent focus ring erasure and redraw. Focus rings are drawn separate from its view drawing. So now it is much easier to draw focus rings using the following:

__Listing 1__  The OS X 10.7 APIs for drawing focus rings in Objective-C.

```objc
- (void)drawFocusRingMask;
- (NSRect)focusRingMaskBounds;
- (void)noteFocusRingMaskChanged;
```


__Listing 2__  The OS X 10.7 APIs for drawing focus rings in Swift.

```objc
- (void)drawFocusRingMask;
@property(readonly) NSRect focusRingMaskBounds;
- (void)noteFocusRingMaskChanged;
```

Any layer-backed views that need to draw "together" needs to be in the same backing space.

Both a custom view and its window's contentView need to be layer-backed in the same location so one won't clip the other.

A custom view that wants a focus ring to be shown when it is the active first responder, and that doesn't inherit that behavior from a superclass, needs only specify a focus ring mask shape.

To opt-in for the OS X 10.7 focus ring drawing model, a view simply overrides the `-drawFocusRingMask` method to draw the shape whose outline should serve as the template for the focus ring, and `-focusRingMaskBounds` to return the bounding box of the entire element (expressed in the view's interior bounds coordinate space). For a view with a single item, that can be the entire view bounds. For a view that is a multi-part item like a matrix or a segmented control that manages it's own focus changes, it should be a bounds that encloses the sub-element so the changes get the animation effect.

If your control that has more complex appearance, you use the bounds to determine the edge of your focus ring and use a mask to draw the focus of the elements within.

For example, a simple rectangular focus ring surrounding a view's frame would be requested by implementing:

__Listing 3__  Code example to draw the focus ring in Objective-C.

```objc
- (void)drawFocusRingMask {
    NSRectFill([self bounds]);
}

- (NSRect)focusRingMaskBounds {
    return [self bounds];
}
```


__Listing 4__  Code example to draw the focus ring in Swift.

```swift
override func drawFocusRingMask() {
    let rect = bounds;
    rect.fill()
}

override var focusRingMaskBounds: NSRect {
    return bounds
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2018-02-21 | Editorial update. |
| 2013-11-12 | New document that explains how to draw focus rings around custom NSViews. |

