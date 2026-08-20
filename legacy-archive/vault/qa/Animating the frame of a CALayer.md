---
title: Animating the frame of a CALayer.
apple_id: DTS40008060
resource_type: QA
platform: iOS|macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2011-02-08'
source_url: https://developer.apple.com/library/archive/qa/qa1620/_index.html
archived_at: '2026-07-18T02:32:58.054300Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1620

# Animating the frame of a CALayer.

## Q:  When I try to animate the `frame` of a `CALayer` nothing happens. Why?

A: The `frame` property of a `CALayer` is a derived property, dependent on the `position`, `anchorPoint`, `bounds` and `transform` of the layer. Instead of animating the `frame`, you should instead animate the `position` or `bounds`, depending on what effect you are trying to accomplish.

To move a layer, you can animate the `position` as shown in Listing 1.

__Listing 1__  Animating the `position` of a layer.

```objc
-(void)moveLayer:(CALayer*)layer to:(CGPoint)point
{
    // Prepare the animation from the current position to the new position
    CABasicAnimation *animation = [CABasicAnimation animationWithKeyPath:@"position"];
    animation.fromValue = [layer valueForKey:@"position"];

    // NSValue/+valueWithPoint:(NSPoint)point is available on Mac OS X
    // NSValue/+valueWithCGPoint:(CGPoint)point is available on iOS
    // comment/uncomment the corresponding lines depending on which platform you're targeting

    // Mac OS X
    animation.toValue = [NSValue valueWithPoint:NSPointFromCGPoint(point)];
    // iOS
    //animation.toValue = [NSValue valueWithCGPoint:point];

    // Update the layer's position so that the layer doesn't snap back when the animation completes.
    layer.position = point;

    // Add the animation, overriding the implicit animation.
    [layer addAnimation:animation forKey:@"position"];
}
```

To resize a layer, you would animate the `bounds` parameter as shown in Listing 2.

__Listing 2__  Animating the size of a layer.

```objc
-(void)resizeLayer:(CALayer*)layer to:(CGSize)size
{
    // Prepare the animation from the old size to the new size
    CGRect oldBounds = layer.bounds;
    CGRect newBounds = oldBounds;
    newBounds.size = size;
    CABasicAnimation *animation = [CABasicAnimation animationWithKeyPath:@"bounds"];

    // NSValue/+valueWithRect:(NSRect)rect is available on Mac OS X
    // NSValue/+valueWithCGRect:(CGRect)rect is available on iOS
    // comment/uncomment the corresponding lines depending on which platform you're targeting

    // Mac OS X
    animation.fromValue = [NSValue valueWithRect:NSRectFromCGRect(oldBounds)];
    animation.toValue = [NSValue valueWithRect:NSRectFromCGRect(newBounds)];
    // iOS
    //animation.fromValue = [NSValue valueWithCGRect:oldBounds];
    //animation.toValue = [NSValue valueWithCGRect:newBounds];

    // Update the layer's bounds so the layer doesn't snap back when the animation completes.
    layer.bounds = newBounds;

    // Add the animation, overriding the implicit animation.
    [layer addAnimation:animation forKey:@"bounds"];
}
```

You can combine these animations using a `CAAnimationGroup` if you need to move and resize a layer at the same time. For more information you will want to read the _Core Animation Programming Guide_, specifically the sections on _Layer Geometry and Transforms_ , _Animation_, and _Core Animation Extensions To Key-Value Coding_ as well as the appropriate reference documents. Finally, the _[Core Animation Cookbook](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreAnimation_Cookbook/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005410)_ offers sample code for common tasks that you can drop directly into your application.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-02-08 | Updated for compatibility on Mac OS X and iOS. |
| 2010-05-27 | Updated the presented technique. |
| 2008-10-24 | New document that explains how the frame property of a layer interacts with animations. |

