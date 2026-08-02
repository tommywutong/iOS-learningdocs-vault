---
title: Drawing Performance Guidelines
apple_id: 10000151i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/Drawing/Articles/CocoaDrawingTips.html
archived_at: '2026-07-18T01:47:11.887178Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Drawing Performance Guidelines](Introduction%20to%20Drawing%20Performance%20Guidelines.md)


[Next](Measuring%20Drawing%20Performance.md)[Previous](Introduction%20to%20Drawing%20Performance%20Guidelines.md)

# Cocoa Drawing Tips

This section includes some general tips for improving the drawing performance of Cocoa applications.

Poor drawing performance is often caused by an application drawing content unnecessarily. Whenever your application receives an event asking it to redraw content, it should pay attention to the drawing rectangle it receives and limit itself to this rectangle. The bounding rectangle is passed as a parameter to your view’s `drawRect:` method.

In OS X version 10.3 and later, Cocoa applications have two ways of obtaining a more refined version of the drawing rectangle. The rectangle passed into an NSView `drawRect:` method is formed by creating a union of all the dirty rectangles. However, if updated areas are small and far apart, the union area can often be much larger and contain a lot of unchanged content. Instead of using this rectangle, you can instead call the view’s `getRectsBeingDrawn:count:` method to get an array of the individual rectangles representing the exact update region. You can also call the `needsToDrawRect:` method to determine if a particular rectangle needs to be redrawn.

You can use the Quartz Debug tool to see where your application is drawing and to find areas where it is drawing content redundantly. For more information, see [Using Quartz Debug](Measuring%20Drawing%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3tkljzg44dini).

Live window resizing tends to put a greater strain on your drawing code than any other update operation. During a few seconds, your drawing code might receive dozens of events to update large portions of your window content. If your drawing code is not fast enough to keep up with this onslaught of events, your application may seem visibly sluggish to the user.

If you know you are in the middle of a live resize operation, consider ways to simplify your redrawing code. Cache data whenever possible or include special cases in your drawing code that favor speed over precision.

The live resizing of windows is one place where users notice poor performance. When done right, resizing a window should feel smooth and go unnoticed by the user. When done wrongly, window resizing can feel choppy and sluggish.

The key to optimizing live resize code is to draw as little as possible while still maintaining an acceptable look for your window. This usually means drawing only the L-shaped region exposed by resizing plus a few controls such as scrollbars and custom widgets. However, some applications may need to draw more content. For example, an application may need to do more redrawing if it dynamically reflows its window content based on the window width and height.

Your application’s drawing code gets called frequently to make sure your interface is up-to-date. During a live resizing operation, the system may call your drawing routines many times a second to display uncovered regions of your window. Because they can be called frequently, your drawing routines should focus solely on drawing. They should not attempt to calculate data values or do anything that is not necessary for drawing content. For example, if you are developing a game, you should not use your drawing routine to perform collision detection. You should perform those calculations outside of your main drawing routines.

Whenever you render content, the system keeps track of the regions you modify and coalesces them into an update region to be flushed to the window buffer. If your drawing code updates a large area of the screen using several shorter drawing calls, you may want to notify the window server of the total update region in advance. Invalidating a larger region in advance removes the need to calculate this region with each successive rendering call.

Use the `setNeedsDisplay:` or `setNeedsDisplayInRect:` methods to invalidate the appropriate area of your view. Be careful not to coalesce your updates if the resulting region would contain unchanged content. You can determine if you are redrawing unchanged content using the Quartz Debug application. See [Measuring Drawing Performance](Measuring%20Drawing%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3tklkdjjbeursjirca) for more information.

If you implement a custom subclass of NSView, you can accelerate the drawing performance by declaring your view object as opaque. An opaque view is one that fills its entire bounding rectangle with content. The Cocoa drawing system does not send update messages to a superview for areas covered by one or more opaque subviews.

The `isOpaque` method of NSView returns `NO` by default. To declare your custom view object as opaque, override this method and return `YES`. If you create an opaque view, remember that your view object is responsible for filling its bounding rectangle with content.

In OS X version 10.3 and later, Cocoa applications can minimize drawing by hiding views that are not needed at the moment. Hiding a view eliminates the need to call that view’s drawing code altogether. Hiding a parent view eliminates the need to draw the parent and all of its children.

Use the `setHidden:` method of NSView to mark a view has hidden or shown. By default, views are shown. To determine if a view is hidden, use the `isHiddenOrHasHiddenAncestor` method. If the current view or any of its parent views is hidden, this method returns true. If you need to know if your specific view is hidden, use the `isHidden` method instead.

In OS X version 10.3 and later, Cocoa applications can disable the default clipping region processing to improve performance. You might want to do this if you already plan to manage the clipping region inside of your own drawing code. To disable clipping, override the `wantsDefaultClipping` method of your NSView object and return `NO`. 

[Next](Measuring%20Drawing%20Performance.md)[Previous](Introduction%20to%20Drawing%20Performance%20Guidelines.md)

