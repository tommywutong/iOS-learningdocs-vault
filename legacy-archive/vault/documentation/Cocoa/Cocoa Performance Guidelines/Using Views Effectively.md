---
title: Cocoa Performance Guidelines
apple_id: TP40001448
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2009-08-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaPerformance/Articles/CustomViews.html
archived_at: '2026-07-15T07:13:17.179696Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Performance Guidelines](Introduction%20to%20Cocoa%20Performance%20Guidelines.md)


[Next](Cocoa%20Live%20Window%20Resizing.md)[Previous](Unblocking%20Your%20User%20Interface.md)

# Using Views Effectively

Cocoa views provide extensive support for drawing and managing visual content. However, as with any object, improper use can lead to performance degradation. The following sections offer guidelines on how to get the most out of your custom views.

If you implement a custom subclass of NSView, you can accelerate the drawing performance by declaring your view object as opaque. An opaque view is one that fills its entire bounding rectangle with content. The Cocoa drawing system does not send update messages to a superview for areas covered by one or more opaque subviews.

The `isOpaque` method of NSView returns `NO` by default. To declare your custom view object as opaque, override this method and return `YES`. If you create an opaque view, remember that your view object is responsible for filling its bounding rectangle with content.

Poor drawing performance is often caused by an application doing too much work. The `drawRect:` method of NSView receives a rectangle that identifies the area that needs to be redrawn. In your implementation of this method, you should always check the rectangle and avoid drawing content that lies outside its boundaries.

Although checking your content against the bounding rectangle passed into `drawRect:` is a good start, Cocoa does provide additional methods for determining what needs to be redrawn. The availability of these methods depends on the running version of OS X though, so you might need to check to make sure a method is available before attempting to use it.

In OS X version 10.3 and later, Cocoa applications have two ways of obtaining a more refined version of the drawing rectangle. The rectangle passed into an NSView `drawRect:` method is formed by creating a union of all the dirty rectangles. However, if updated areas are small and far apart, the union area can often be much larger and contain a lot of unchanged content. Instead of using this rectangle, you can instead call the view’s `getRectsBeingDrawn:count:` method to get an array of the individual update rectangles and use the `NSIntersectsRect` function to compare them to the bounding rectangle of your object. An even simpler way to do this is to call the `needsToDrawRect:` method, which performs both of these steps for you.

The following example shows a simple `drawRect:` method that draws the objects in a custom view. In this example, the MyDrawableThing class does not descend from NSView but instead defines an object with a bounding rectangle and some content that the view knows how to draw.

```objc
- (void) drawRect:(NSRect)aRect
{
    NSEnumerator* myEnumerator = [myArray objectEnumerator];
    MyDrawableThing* currentThing;

    while (currentThing = [myEnumerator nextObject])
    {
        // Draw the thing if it is in one of the update rectangles.
        if ([self needsToDrawRect:[currentThing bounds]])
        {
            [self drawThing:currentThing];
        }
    }
}
```

You can use the Quartz Debug tool to see where your application is drawing and to find areas where it is drawing content redundantly. For more information, see “[Measuring Drawing Performance](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/Drawing/Articles/MeasuringPerformance.html#//apple_ref/doc/uid/20001875)” in _[Drawing Performance Guidelines](../../Performance/Drawing%20Performance%20Guidelines/Introduction%20to%20Drawing%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tc2i)_.

Cocoa provides two techniques for redrawing the content of your views. The first technique is to draw the content immediately using the `display`, `displayRect:`, or related methods. The second is to draw the content at a later time by marking portions of your view as dirty and in need of an update. This second technique offers significantly better performance and is appropriate for most situations.

NSView defines the methods `setNeedsDisplay:` and `setNeedsDisplayInRect:` for marking portions of your view as dirty. Cocoa collects the dirty rectangles and saves them until the top of your run loop is reached, at which point your view is told to redraw itself. The rectangle passed into your `drawRect:` routine is a union of the dirty rectangles, but applications running on OS X version 10.3 and later can get a list of the individual rectangles, as described in [Drawing Content](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbtfuytcmrtgmyq).

In general, you should avoid calling the `display` family of methods to redraw your views. If you must call them, do so infrequently. Because they cause an immediate call to your `drawRect:` routine, they can cause performance to slow down significantly by preempting other pending operations. They also preclude the ability to coalesce other changes and then redraw those changes all at once.

NSView offers tremendous flexibility in managing the content of your windows and provides the basic canvas for drawing your application’s content. However, when you consider the design of your windows, think carefully about how you use views. While views are a convenient way to organize content inside a window, if you create a complex, deeply nested hierarchy of views, you might experience performance problems.

Although Cocoa windows can manage a relatively large number of views (around one hundred) without suffering performance noticeable problems, this number includes both your custom views and the standard system controls and subviews you use. If your window has hundreds of custom visual elements, you probably do not want to implement them all as subclasses of NSView. Instead, you should consider writing your own custom classes that can be managed by a higher-level NSView subclass. The drawing code of your NSView subclass can then be optimized to handle your custom objects.

A good example of when to use custom objects is a photo browser that displays thumbnail images of hundreds or even thousands of photos. Wrapping each photo in an NSView would both be prohibitively expensive and inefficient. Instead, you would be better off by creating a lightweight class to manage one or more photos and a custom view to manage that lightweight class. 

[Next](Cocoa%20Live%20Window%20Resizing.md)[Previous](Unblocking%20Your%20User%20Interface.md)

