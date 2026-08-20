---
title: CATiledLayer and UIKit graphics
apple_id: DTS40009212
resource_type: QA
platform: iOS
topic: Graphics & Animation
technology: null
published: '2011-02-15'
source_url: https://developer.apple.com/library/archive/qa/qa1637/_index.html
archived_at: '2026-07-18T02:33:02.850883Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1637

# CATiledLayer and UIKit graphics

## Q:  I'm using a `CATiledLayer` in my application and I occasionally see incorrect rendering or crashes, especially when I have multiple views on screen. What can I do to avoid this?

A: I'm using a `CATiledLayer` in my application and I occasionally see incorrect rendering or crashes, especially when I have multiple views on screen. What can I do to avoid this?

Therefore, on iOS 4.0 and later, you can override `-drawRect:` and do all your drawings as normal, but if you plan to support iOS prior to 4.0, you should still be aware of the issues raised in this document.

The `CATiledLayer` implements its drawing by using a background thread to fetch the contents of each tile, however the drawing functions provided by UIKit rely on a global context stack, and as such when a `CATiledLayer` starts rendering, using any of UIKit's drawing functions can result in a race condition.

Practically what this means is that you cannot use any UIKit's drawing methods when drawing to a `CATiledLayer`, and you cannot do your drawing inside of a `UIView`'s `-drawRect:` method. Instead you must implement `-drawLayer:inContext:` and draw only using Core Graphics and other thread-safe functions that accept a `CGContextRef` to target drawing to.

If your `-drawRect:` method uses `UIImage`'s draw methods, `UIColor`'s set methods, any string drawing method from `NSString(UIStringDrawing)` or any of the `UIRect` or `UIGraphics` functions provided by UIKit, then your `-drawLayer:inContext:` method must be rewritten to avoid using those methods, and instead use Core Graphics directly. Not all operations from `NSString(UIStringDrawing)` are trivially converted to Core Graphics, so you may wish to contact [Developer Technical Support](https://developer.apple.com/support/iphone/techsupport/).

As UIKit uses the existence of an override of `-drawRect:` to determine some functionality of a `UIView`, you should still implement the `-drawRect:` method, but it does not need to do anything (and will not be called due to your implementation of `-drawLayer:inContext:`). An example of a correct implementation of a `UIView` that uses a `CATiledLayer` is in Listing 1.

__Listing 1__  An implementation of a `UIView` subclass that uses a `CATiledLayer` for the layerClass.

```objc
#import <QuartzCore/QuartzCore.h> #import <UIKit/UIKit.h> #import "MyTiledView.h"  +(Class)layerClass {     return [CATiledLayer class]; }  -(void)drawRect:(CGRect)r {     // UIView uses the existence of -drawRect: to determine if should allow its CALayer     // to be invalidated, which would then lead to the layer creating a backing store and     // -drawLayer:inContext: being called.     // By implementing an empty -drawRect: method, we allow UIKit to continue to implement     // this logic, while doing our real drawing work inside of -drawLayer:inContext: }  -(void)drawLayer:(CALayer*)layer inContext:(CGContextRef)context {     // Do all your drawing here. Do not use UIGraphics to do any drawing, use Core Graphics instead. }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-02-15 | Added a note about changes for iPhone OS 4.0. |
| 2009-09-08 | New document that discusses thread safety issues when using a CATiledLayer on iOS |

