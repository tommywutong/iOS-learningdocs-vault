---
title: Drawing Performance Guidelines
apple_id: 10000151i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/Drawing/NSBezierPathTips.html
archived_at: '2026-07-18T01:47:14.752339Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Drawing Performance Guidelines](Introduction%20to%20Drawing%20Performance%20Guidelines.md)


[Next](Document%20Revision%20History.md)[Previous](Cocoa%20Live%20Window%20Resizing.md)

# Improving NSBezierPath Rendering Times

If you are using the NSBezierPath object to draw paths in a Cocoa application and you are not as interested in the absolute correctness of the rendered paths, there are ways to speed up the rendering times for complex paths. Prior to rendering an NSBezierPath object, the Core Graphics engine searches the path for any intersecting line segments. For each intersection it finds, the engine then rasterizes the line joint according to the chosen settings. If the NSBezierPath object contains a large number of intersecting line segments, the cost of these operations can become significant. If you do not need these intersections to be rendered precisely, you might try adding fewer line segments to your NSBezierPath objects prior to rendering.

If you are drawing many rectangles, you might want to avoid using NSBezierPath altogether. NSBezierPath contains the convenience method `strokeRect:` for drawing rectangles. However, the path created by this method consists of four intersecting line segments, with properly rendered corners. If you do not need the rectangle to be drawn so precisely, you might want to use the `NSFrameRect` family of functions instead. These functions draw the sides of a rectangle using four nonintersecting lines, which can be drawn much faster. The `NSFrameRect` family of functions consist of the following functions, declared in `NSGraphics.h`.

```
void NSFrameRect(NSRect aRect);
void NSFrameRectWithWidth(NSRect aRect, float frameWidth);
void NSFrameRectWithWidthUsingOperation(NSRect aRect, float frameWidth, NSCompositingOperation op);
```

Keep in mind that using these techniques involves a correctness-versus-efficiency trade-off. You should not make this trade-off unless you are trying to solve a specific performance problem.

[Next](Document%20Revision%20History.md)[Previous](Cocoa%20Live%20Window%20Resizing.md)

