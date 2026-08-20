---
title: View Programming Guide
apple_id: TP40002978
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaViewsGuide/Optimizing/Optimizing.html
archived_at: '2026-07-15T07:13:23.421966Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [View Programming Guide](Introduction%20to%20View%20Programming%20Guide%20for%20Cocoa.md)


[Next](Document%20Revision%20History.md)[Previous](Advanced%20Custom%20View%20Tasks.md)

# Optimizing View Drawing

Drawing is often a processor intensive operation. The CPU, graphics system, window server, kernel, and physical memory must all contribute resources when an application draws something to the screen. The high expense of drawing makes it an attractive candidate for optimization. This chapter describes design choices and techniques you can apply in your custom views to eliminate redundant or unnecessary drawing and improve drawing performance.

`NSView` offers tremendous flexibility in managing the content of your windows and provides the basic canvas for drawing your application’s content. However, when you consider the design of your windows, think carefully about how you use views. Although views are a convenient way to organize content inside a window, if you create a complex, deeply nested hierarchy of views, you might experience performance problems.

Although Cocoa windows can manage a relatively large number of views (around one hundred) without suffering noticeable performance problems, this number includes both your custom views and the standard system controls and subviews you use. If your window has hundreds of custom visual elements, you probably do not want to implement them all as subclasses of `NSView`. Instead, you should consider writing your own custom classes that can be managed by a higher-level `NSView` subclass. The drawing code of your `NSView` subclass can then be optimized to handle your custom objects.

A good example of when to use custom objects is a photo browser that displays thumbnail images of hundreds or even thousands of photos. Wrapping each photo in an `NSView` instance would both be prohibitively expensive and inefficient. Instead, you would be better off by creating a lightweight class to manage one or more photos and a custom view to manage that lightweight class.

If you implement a custom subclass of `NSView`, you can accelerate the drawing performance by declaring your view object as opaque. An opaque view is one that fills all the pixels within its content using opaque colors. The Cocoa drawing system does not need to send update messages to a superview for areas covered by one or more opaque subviews.

The `isOpaque` method of `NSView` returns `NO` by default. To declare your custom view object as opaque, override this method and return `YES`. If you create an opaque view, remember that your view object is responsible for filling all the pixels within its bounding rectangle using opaque colors. See [View Opacity](Creating%20a%20Custom%20View.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzyfvbuqnznknlte) for an example implementation of `isOpaque`.

Cocoa provides two techniques for redrawing the content of your views. The first technique is to draw the content immediately using `display`, `displayRect:`, or related methods. The second is to draw the content at a later time by marking portions of your view as dirty and in need of an update. This second technique offers significantly better performance and is appropriate for most situations.

`NSView` defines the methods `setNeedsDisplay:` and `setNeedsDisplayInRect:` for marking portions of your view as dirty. Cocoa collects the dirty rectangles and saves them until the top of your run loop is reached, at which point your view is told to redraw itself. The rectangle passed into your `drawRect:` routine is a union of the dirty rectangles, but applications running OS X version 10.3 and later can get a list of the individual rectangles, as described in [Constraining Drawing to Improve Performance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzyfvbuqmjrfvjvona).

In general, you should avoid calling the `display` family of methods to redraw your views. If you must call them, do so infrequently. Because they cause an immediate call to your `drawRect:` routine, they can cause performance to slow down significantly by preempting other pending operations. They also preclude the ability to coalesce other changes and then redraw those changes all at once.

The sole parameter of the `drawRect:` method is a rectangle (specifically, an `NSRect` structure) that encloses the area of a view that the view is being asked to draw. This rectangle is the union of the rectangles that have been marked as needing updating since the view instance last received a `display` message. The view may still draw anywhere within its own bounds because the Application Kit automatically clips out any drawing that falls outside the rectangle passed into `drawRect:`. The view can improve its drawing performance, however, by attempting to draw only those parts of its content that fall completely or partly within the clipped rectangle.

In OS X version 10.3 and later, views can constrain their drawing even further by using the `NSView` methods `getRectsBeingDrawn:count:` and `needsToDrawRect:`. These methods provide direct and indirect access, respectively, to the detailed representation of a view’s invalid areas—that is, its list of non-overlapping rectangles—that the Application Kit maintains for each `NSView` instance. The Application Kit automatically enforces clipping to this list of rectangles, and you can further improve performance in views that do complex or expensive drawing by having them limit their drawing to objects that intersect any of the rectangles in this list.

A view can invoke the method `getRectsBeingDrawn:count:` in its `drawRect:` implementation to retrieve a list of non-overlapping rectangles that define the area the view is being asked to draw. It can then iterate through this list of rectangles, performing intersection tests against its content to determine what actually needs drawing. By eliminating those objects, the view can avoid unnecessary drawing work and improve the drawing efficiency of the application.

Listing 6-1 shows the basic usage of `getRectsBeingDrawn:count:`. It and the following code example (Listing 6-2)) illustrate techniques for intersection-testing the list of rectangles against drawable objects within a view. For intersection testing, you can use the functions declared in the Foundation framework’s `NSGeometry.h` header file. The `NSIntersectsRect` function is particularly useful.

__Listing 6-1__  Explicit intersection testing of known regions against dirty rectangles

```
 (void) drawRect:(NSRect)aRect {
    const NSRect *rects;
    int count, i;
    id thing;
    NSEnumerator *thingEnumerator = [[self arrayOfAllThingsIDraw] objectEnumerator];
    [self getRectsBeingDrawn:&rects count:&count];
    while (thing = [thingEnumerator nextObject]) {
        // First test against coalesced rect.
        if (NSIntersectsRect([thing bounds], aRect)) {
        // Then test per dirty rect
            for (i = 0; i < count; i++) {
                if (NSIntersectsRect([thing bounds], rects[i])) {
                    [self drawThing:thing];
                    break;
                }
            }
        }
    }
}
```

For each object that the view can potentially draw, this `drawRect:` implementation first tests the object’s bounding rectangle against the `drawRect:` method’s parameter (_aRect_). If the two intersect, the view then determines whether the object’s bounds intersect any of the rectangles in the list retrieved by `getRectsBeingDrawn:count:`. If it does intersect, the view draws the object (or asks it to draw itself).

Because it is common for a view to render its content by drawing a set of individually positioned items, the `NSView` class provides a convenience method that essentially does much of the work in Listing 6-1 for you. This method, `needsToDrawRect:`, does not require you to fetch the list of dirty rectangles with `getRectsBeingDrawn:count:` or perform an inner loop for intersection testing. The resulting code, as illustrated in Listing 6-2, is much cleaner and simpler.

__Listing 6-2__  Simplified intersection testing using `needsToDrawRect:`

```objc
- (void) drawRect:(NSRect)aRect {
    id thing;
    NSEnumerator *thingEnumerator = [[self arrayOfAllThingsIDraw] objectEnumerator];
    while (thing = [thingEnumerator nextObject]) {
        if ([self needsToDrawRect:[thing bounds]]) {
            [self drawThing:thing];
        }
    }
}
```

The `needsToDrawRect:` method is optimized to efficiently reject objects that lie entirely outside the bounds of the area being drawn by employing the same “trivial rejection” test as that used in Listing 6-1.

By default, Cocoa automatically clips drawing done in a `drawRect:` method to the area that the view is being asked to draw. If a view draws in a region that doesn’t fall within the clipped boundaries, none of that drawing finds its way to the screen. For most kinds of views, this is appropriate behavior as it prevents drawing in window areas owned by other views and does so without requiring the view to meticulously restrict its drawing. But in some circumstances, it might not be what you want. Clipping incurs set-up, enforcement, and clean-up costs that you might want to avoid if you can.

In these situations, your custom view can override the `NSView` method `wantsDefaultClipping` and return `NO`:

```objc
- (BOOL)wantsDefaultClipping {
    return NO;
}
```

Obviously, the absence of enforced clipping presents dangers as well as opportunities. You must not draw outside the list of rectangles returned by `getRectsBeingDrawn:count:` as this could corrupt drawing in other views.

You can take one of two (responsible) approaches:

- You can draw very carefully.
- You can provide your own clipping.

One possible implementation strategy for `drawRect:` in this case is to iterate over the list of rectangles being drawn. Clip to each and draw the contents, one rectangle at a time. Whether such a strategy improves or diminishes drawing performance in your view depends a great deal on the view’s content and typical drawing behavior.

Live window resizing is an area where poorly optimized drawing code becomes particularly apparent. When the user resizes your window, the movement of the window should be smooth. If your code tries to do too much work during this time, the window movement may seem choppy and unresponsive to the user.

The following sections introduce you to several options for improving your live resizing code. Depending on which versions of OS X you are targeting, you might use one or more of these options in your implementation.

When a live resize operation is in progress, speed is imperative. The simplest way to improve speed is to do less work. Because quality is generally less important during a live resize operation, you can take some shortcuts to speed up drawing. For example, if your drawing code normally performs high-precision calculations to determine the location of items, you could replace those calculations with quick approximations during a live resize operation.

`NSView` provides the `inLiveResize` method to let you know when a live resize operation is taking place. You can use this method inside your `drawRect:` routine to do conditional drawing, as shown in the following example:

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

You can use the `viewWillStartLiveResize` and `viewDidEndLiveResize` methods of `NSView` to help optimize your live resize code. Cocoa calls these methods immediately before and immediately after a live resize operation takes place. You can use the `viewWillStartLiveResize` method to cache data or do any other initialization that can help speed up your live resize code. You use the `viewDidEndLiveResize` method to clean up your caches and return your view to its normal state.

Cocoa calls `viewWillStartLiveResize` and `viewDidEndLiveResize` for every view in your window’s hierarchy. This message is sent only once to each view. Views added during the middle of a live resize operation do not receive the message. Similarly, if you remove views before the resizing operation ends, those views do not receive the `viewDidEndLiveResize` message.

If you use these methods to create a low-resolution approximation of your content, you might want to invalidate the content of your view in your `viewDidEndLiveResize` method. Invalidating the view causes it be redrawn at full resolution outside of the live resize loop.

If you override either `viewWillStartLiveResize` or `viewDidEndLiveResize`, make sure to send the message to `super` to allow subviews to prepare for the resize operation as well. If you need to add views before the resize operation begins, make sure to do so before calling `super` if you want that view to receive the `viewWillStartLiveResize` message.

In OS X v10.4 and later, Cocoa offers you a way to be even smarter about updating your content during a live resize operation. Both `NSWindow` and `NSView` include support for preserving content during the operation. This technique lets you decide what content is really invalid and needs to be redrawn.

To support the preservation of content, you must do the following:

1. 

   Override the `preservesContentDuringLiveResize` method in your custom view. Your implementation should return `YES` to indicate that the view supports content preservation.
2. Override your view’s `setFrameSize:` method. Your implementation should invalidate any portions of your view that need to be redrawn. Typically, this includes only the rectangular areas that were exposed when the view size increased.

To find the areas of your view that were exposed during resizing, `NSView` provides two methods. The `rectPreservedDuringLiveResize` method returns the rectangular area of your view that did not change. The `getRectsExposedDuringLiveResize:count:` method returns the list of rectangles representing any newly exposed areas. For most views, you need only pass the rectangles returned by this second method to `setNeedsDisplayInRect:`. The first method is provided in case you still need to invalidate the rest of your view.

The following example provides a default implementation you can use for your `setFrameSize:` method. In the example below, the implementation checks to see if the view is being resized. If it is, and if any rectangles were exposed by the resizing operation, it gets the newly exposed rectangles and invalidates them. If the view size shrunk, this method does nothing.

```objc
- (void) setFrameSize:(NSSize)newSize
{
    [super setFrameSize:newSize];

    // A change in size has required the view to be invalidated.
    if ([self inLiveResize])
    {
        NSRect rects[4];
        int count;
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

[Next](Document%20Revision%20History.md)[Previous](Advanced%20Custom%20View%20Tasks.md)

