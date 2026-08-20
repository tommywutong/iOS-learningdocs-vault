---
title: Cocoa Performance Guidelines
apple_id: TP40001448
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2009-08-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaPerformance/Articles/CocoaLiveResize.html
archived_at: '2026-07-15T07:13:16.681425Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Performance Guidelines](Introduction%20to%20Cocoa%20Performance%20Guidelines.md)


[Next](Cocoa%20Bindings%20Tips.md)[Previous](Using%20Views%20Effectively.md)

# Cocoa Live Window Resizing

Live window resizing is an area where poorly optimized drawing code becomes particularly apparent. When the user resizes your window, the movement of the window should be smooth. If your code tries to do too much work during this time, the window movement may seem choppy and unresponsive to the user.

The following sections introduce you to several options for improving your live resizing code. Depending on which versions of OS X you are targeting, you might use one or more of these options in your implementation.

When a live resize operation is in progress, speed is imperative. The simplest way to improve speed is to do less work. Because quality is generally less important during a live resize operation, you can take some shortcuts to speed up drawing. For example, if your drawing code normally performs high-precision calculations to determine the location of items, you could replace those calculations with quick approximations during a live resize operation.

NSView provides the `inLiveResize` method to let you know when a live resize operation is taking place. You can use this method inside your `drawRect:` routine to do conditional drawing, as shown in the following example:

```objc
- (void) drawRect:(NSRect)rect
{
    if ([self inLiveResize])
    {
        // Draw a quick approximation
    }
    else
    {
        // Draw with full detail
    }
}
```

Another way to minimize work is to redraw only those areas of your view that were exposed during the resize operation. If you are targeting your application for OS X version 10.3, you can use the `getRectsBeingDrawn:count:` method to retrieve the rectangles that were exposed. If you are targeting OS X version 10.4 or later, the `getRectsExposedDuringLiveResize:count:` method is provided to return only the rectangles that were exposed by resizing.

Starting with OS X v10.1, you can use the `viewWillStartLiveResize` and `viewDidEndLiveResize` methods of NSView to help optimize your live resize code. Cocoa calls these methods immediately before and immediately after a live resize operation takes place. You can use the `viewWillStartLiveResize` method to cache data or do any other initialization that can help speed up your live resize code. You use the `viewDidEndLiveResize` method to clean up your caches and return your view to its normal state.

Cocoa calls `viewWillStartLiveResize` and `viewDidEndLiveResize` for every view in your window’s hierarchy. This message is sent only once to each view. Views added during the middle of a live resize operation do not receive the message. Similarly, if you remove views before the resizing operation ends, those views do not receive the `viewDidEndLiveResize` message.

If you use these methods to create a low-resolution approximation of your content, you might want to invalidate the content of your view in your `viewDidEndLiveResize` method. Invalidating the view causes it be redrawn at full resolution outside of the live resize loop.

If you override either `viewWillStartLiveResize` or `viewDidEndLiveResize`, make sure to send the message to `super` to allow subviews to prepare for the resize operation as well. If you need to add views before the resize operation begins, make sure to do so before calling `super` if you want that view to receive the `viewWillStartLiveResize` message.

In OS X v10.4 and later, Cocoa offers you a way to be even smarter about updating your content during a live resize operation. Both NSWindow and NSView include support for preserving content during the operation. This technique lets you decide what content is really invalid and needs to be redrawn.

To support the preservation of content, you must do the following:

1. 

   [Override](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57) the `preservesContentDuringLiveResize` method in your custom view. Your implementation should return `YES` to indicate that the view supports content preservation.
2. Override your view’s `setFrameSize:` method. Your implementation should invalidate any portions of your view that need to be redrawn. Typically, this includes only the rectangular areas that were exposed when the view size increased.

To find the areas of your view that were exposed during resizing, NSView provides two methods. The `rectPreservedDuringLiveResize` method returns the rectangular area of your view that did not change. The `getRectsExposedDuringLiveResize:count:` method returns the list of rectangles representing any newly exposed areas. For most views, you need only pass the rectangles returned by this second method to `setNeedsDisplayInRect:`. The first method is provided in case you still need to invalidate the rest of your view.

The following example provides a default implementation you can use for your `setFrameSize:` method. In the example below, the implementation checks to see if the view is being resized. If it is, and if any rectangles were exposed by the resizing operation, it gets the newly exposed rectangles and invalidates them. If the view size shrunk, this method does nothing.

```objc
- (void) setFrameSize:(NSSize)newSize
{
    [super setFrameSize:newSize];

    // A change in size has required the view to be invalidated.
    if ([self inLiveResize])
    {
        NSRect rects[4];
        NSInteger count;
        [self getRectsExposedDuringLiveResize:rects count:&count];
        while (count-- > 0)
        {
            [self setNeedsDisplayInRect:rects[count]];
        }
    }
    else
    {
        [self setNeedsDisplay:YES];
    }
}
```

[Next](Cocoa%20Bindings%20Tips.md)[Previous](Using%20Views%20Effectively.md)

