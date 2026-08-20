---
title: Core Animation Cookbook
apple_id: TP40005406
resource_type: Guide
platform: iOS|macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreAnimation_Cookbook/Articles/Drawing.html
archived_at: '2026-07-15T07:35:28.365192Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Animation Cookbook](Core%20Animation%20Cookbook.md)


[Next](Timing.md)[Previous](Core%20Animation%20Cookbook.md)

# Drawing

This chapter discusses drawing issues when using Core Animation and other technologies.

Core Animation `CALayer` class defines a delegate method, `drawLayer:inContext:`, that you can implement and draw your layer content using Quartz 2D drawing functions. However, Cocoa developers who have complete and working drawing solutions based on the Application Kit drawing classes may wish to continue using that code.

Listing 1 shows an implementation of the CALayer delegate method `drawLayer:inContext:` that creates an `NSGraphicsContext` from the `CGContextRef` passed as the _inContext:_ parameter. Layer delegates can use this technique to display content created using `NSBezierPath`, `NSColor`, `NSImage` and other Application Kit classes.

__Listing 1__  Drawing into a layer using Application Kit classes

```objc

- (void)drawLayer:(CALayer *)layer inContext:(CGContextRef)ctx
{
   NSGraphicsContext *nsGraphicsContext;
   nsGraphicsContext = [NSGraphicsContext graphicsContextWithGraphicsPort:ctx
                                                                  flipped:NO];
   [NSGraphicsContext saveGraphicsState];
   [NSGraphicsContext setCurrentContext:nsGraphicsContext];

   // ...Draw content using NS APIs...
   NSRect aRect=NSMakeRect(10.0,10.0,30.0,30.0);
   NSBezierPath *thePath=[NSBezierPath bezierPathWithRect:aRect];
   [[NSColor redColor] set];
   [thePath fill];

   [NSGraphicsContext restoreGraphicsState];
}
```

[Next](Timing.md)[Previous](Core%20Animation%20Cookbook.md)

