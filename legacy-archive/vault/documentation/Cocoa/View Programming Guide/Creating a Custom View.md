---
title: View Programming Guide
apple_id: TP40002978
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaViewsGuide/SubclassingNSView/SubclassingNSView.html
archived_at: '2026-07-15T07:13:23.453208Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [View Programming Guide](Introduction%20to%20View%20Programming%20Guide%20for%20Cocoa.md)


[Next](Advanced%20Custom%20View%20Tasks.md)[Previous](Working%20with%20the%20View%20Hierarchy.md)

# Creating a Custom View

The `NSView` class acts mainly as an abstract superclass; generally you create instances of its subclasses, not of `NSView` itself. `NSView` provides the general mechanism for displaying content on the screen and for handling mouse and keyboard events, but its instances lack the ability to actually draw anything. If your application needs to display content or handle mouse and keyboard events in a specific manner, you'll need to create a custom subclass of `NSView`.

In order to provide a concrete example, this chapter describes the implementation of `DraggableItemView`, a subclass of `NSView`. The `DraggableItemView` class displays a simple item and allows the user to drag it within the view. The view also supports moving the item by pressing the arrow keys and setting the color of the item. It provides key-value-coding compliance for the location of the item, its color, and the background color of the view. The class illustrates the following view programming tasks:

- Allocating and deallocating the view.
- Drawing the view content.
- Marking portions of the view for updating in response to value changes.
- Responding to user-initiated mouse events.
- Updating the cursor when the mouse is over the draggable item.
- Responding to user-initiated key press events.
- Implementing `NSResponder` action methods.
- Providing key-value-coding compliant accessors for its settable properties.

The _[DragItemAround](../../../samplecode/DragItemAround/DragItemAround.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojqga)_ source code is available through Apple Developer Connection.

Applications create a new instance of a view object using `initWithFrame:`, the designated initializer for the `NSView` class. A subclass can specify another method as its designated initializer, but the `initWithFrame:` method must provide the basic functionality required. As an example, the `NSTextView` implementation of `initWithFrame:` creates the entire collection of container objects associated with an `NSTextView` instance while the designated initializer, `initWithFrame:textContainer:` expects the underlying container objects to be provided explicitly. The `initWithFrame:` method creates the collection, and then calls `initWithFrame:textContainer:`. Your custom classes should take the same approach.

The `DraggableItemView` class overrides `initWithFrame:` and sets the exposed properties of the draggable item to the default values, as shown in Listing 4-1.

__Listing 4-1__  `DraggableItemView` implementation of `initWithFrame:`

```objc
- (id)initWithFrame:(NSRect)frame {
    self = [super initWithFrame:frame];
    if (self) {
          // setup the initial properties of the
          // draggable item
          [self setItemPropertiesToDefault:self];
       }
    return self;
}
```

The code for initializing the item color, background color, and location of the draggable item is factored into a separate method. This allows the item's properties to be reset to their default values, shown later. The implementation in Listing 4-2 simply calls the accessor methods for the properties, providing the default values.

__Listing 4-2__  `DraggableItemView` implementation of `setItemPropertiesToDefault:`

```objc
- (void)setItemPropertiesToDefault:sender
{
    [self setLocation:NSMakePoint(0.0,0.0)];
    [self setItemColor:[NSColor redColor]];
    [self setBackgroundColor:[NSColor whiteColor]];
}
```


View instances that are created in Interface Builder don't call `initWithFrame:` when their nib files are loaded, which often causes confusion. Remember that Interface Builder archives an object when it saves a nib file, so the view instance will already have been created and `initWithFrame:` will already have been called.

The `awakeFromNib` method provides an opportunity to provide initialization of a view when it is created as a result of a nib file being loaded. When a nib file that contains a view object is loaded, each view instance receives an `awakeFromNib` message when all the objects have been unarchived. This provides the object an opportunity to initialize any attributes that are not archived with the object in Interface Builder. The `DraggableItemView` class is extremely simple, and doesn't implement `awakeFromNib`.

There are two exceptions to the `initWithFrame:` behavior when creating view instances in Interface Builder. Its important to understand these exceptions to ensure that your views initialize properly.

If you have not created an Interface Builder palette for your custom view, there are two techniques you can use to create instances of your subclass within Interface Builder. The first is using the _Custom View_ proxy item in the Interface Builder containers palette. This view is a stand-in for your custom view, allowing you to position and size the view relative to other views. You then specify the subclass of `NSView` that the view represents using the inspector. When the nib file is loaded by the application, the custom view proxy creates a new instance of the specified view subclass and initializes it using the `initWithFrame:` method, passing along any autoresizing flags as necessary. The view instance then receives an `awakeFromNib` message.

The second technique applies when your custom subclass inherits from a view that Interface Builder provides direct support for. To take advantage of Interface Builder’s built-in support, create an instance of the view that Interface Builder has direct support for, and then use the inspector to change the class name to your custom subclass. For example, you can create an `NSScrollView` instance in Interface Builder and specify that a custom subclass (`MyScrollView`) should be used instead, again using the inspector. In this case, when the nib file is loaded by the application, the view instance has already been created and the `MyScrollView` implementation of `initWithFrame:` is never called. The `MyScrollView` instance receives an `awakeFromNib` message and can configure itself accordingly.

Rather than drawing immediately when it determines that drawing is necessary, Cocoa uses a deferred drawing mechanism. An application typically marks a view or a portion of a view as requiring update. At the end of the event loop or in response to an explicit display request, the view machinery locks focus on the view and calls the view's `drawRect:` method to cause the view to be redrawn. By coalescing update requests in this manner, an application can reduce redundant drawing, increasing performance.

If you need to force immediate drawing of a view, send the view one of the `display...` messages declared by both `NSView` and `NSWindow`. You can also lock focus on a view yourself, draw something, and then unlock focus. However, posting deferred drawing requests through the `setNeedsDisplay:` or `setNeedsDisplayInRect:` methods is the preferred approach because it is more efficient.

In addition to drawing to the screen, views are responsible for providing the content when printing. As with displaying to the screen, the Application Kit locks focus on the view and calls the view's `drawRect:` method. While it is drawing a view can determine if it is drawing to the screen or another device and customize its output appropriately. Views can also customize their printed output by adding headers and footers as well as customizing pagination. See _[Printing Programming Guide for Mac](../Printing%20Programming%20Guide%20for%20Mac/About%20Printing%20on%20the%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4dg2i)_ for more information on the Cocoa printing architecture and views.

In order for a concrete subclass of `NSView` to display any kind of content, it need only implement the `drawRect:` method. This method is invoked during the display process to generate code that’s rendered by the window server into a raster image. `drawRect:` takes a single argument, a rectangle describing the area that needs to be drawn in the receiver’s own coordinate system.

The `DraggableItemView` implementation of `drawRect:` fills the bounds of the view with the specified background color. It then calculates the bounds of the draggable item (Listing 4-3) and fills it with the specified color.

__Listing 4-3__  `DraggableItemView` implementation of `calculatedItemBounds:`

```objc
- (NSRect)calculatedItemBounds
{
    NSRect calculatedRect;

    // calculate the bounds of the draggable item
    // relative to the location
    calculatedRect.origin=location;

    // the example assumes that the width and height
    // are fixed values
    calculatedRect.size.width=60.0;
    calculatedRect.size.height=20.0;

    return calculatedRect;
}
```

The complete implementation of `drawRect:` is shown in Listing 4-4.

__Listing 4-4__  `DraggableItemView` implementation of `drawRect:`

```objc
- (void)drawRect:(NSRect)rect
{
    // erase the background by drawing white
    [[NSColor whiteColor] set];
    [NSBezierPath fillRect:rect];

    // set the current color for the draggable item
    [[self itemColor] set];

    // draw the draggable item
    [NSBezierPath fillRect:[self calculatedItemBounds]];
}
```

Sending drawing instructions and data to the window server has a cost, and it’s best to minimize that cost where possible. You can do this by testing whether a particular graphic shape intersects the rectangle that the `drawRect:` method is asked to draw. See [Optimizing View Drawing](Optimizing%20View%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzyfvbuqmjrfvjvomi) for more information, as well as additional performance recommendations.

The most common way of causing a view to redisplay is to tell it that its image is invalid. On each pass through the event loop, all views that need to redisplay do so. `NSView` defines two methods for marking a view’s image as invalid: `setNeedsDisplay:`, which invalidates the view’s entire bounds rectangle, and `setNeedsDisplayInRect:`, which invalidates a portion of the view. The automatic display of views is controlled by their window; you can turn this behavior off using the `NSWindow` `setAutodisplay:` method. You should rarely need to do this, however; the autodisplay mechanism is well suited to most kinds of update and redisplay.

The autodisplay mechanism invokes various methods that actually do the work of displaying. You can also use these methods to force a view to redisplay itself immediately when necessary. `display` and `displayRect:` are the counterparts to the methods mentioned above; both cause the receiver to redisplay itself regardless of whether it needs to or not. Two additional methods, `displayIfNeeded` and `displayIfNeededInRect:`, redisplay invalidated rectangles in the receiver if it’s been marked invalid with the methods above. The rectangles that actually get drawn are guaranteed to be at least those marked as invalid, but the view may coalesce them into larger rectangles to save multiple invocations of `drawRect:`.

If you want to exclude background views from drawing when forcing display to occur unconditionally, you can use `NSView` methods that explicitly omit backing up to an opaque ancestor. These methods, are `displayRectIgnoringOpacity:`, `displayIfNeededIgnoringOpacity`, and `displayIfNeededInRectIgnoringOpacity:`.

In the `DraggableItemView` example, `setNeedsDisplayInRect:` is called when the draggable item's location is set explicitly, when the location is being offset, and when the item's color is changed. When the background color is set, the entire view is marked as needing display.

From a design perspective, especially with the Model-View-Controller pattern in mind, it is best to ensure that calls to the `display...` methods be generated by the view itself, its superview, or a subview, rather than a controller or model object. It is better to inform the view that a model value is about to change, change the model value, and then inform the view that the change has occurred. This allows the view to invalidate the appropriate rectangles before and after the changes. Key-value observing and its change notification design is tailor-made for this use. See _[Key-Value Observing Programming Guide](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)_ for more information.

The `display...` methods must find an opaque background behind the view that requires displaying and begin drawing from there forward. The `display...` methods search up the view hierarchy to locate the first view that responds `YES` to an `isOpaque` message, bringing the invalidated rectangles along.

If a view instance can guarantee that it will fill all the pixels within its bounds using opaque colors, it should implement the method `isOpaque`, returning `YES`. The `NSView` implementation of `isOpaque` returns `NO`. Subclasses should override this method to return `YES` if all pixels within the view's content will be drawn opaquely.

The `isOpaque` method is called during drawing, and may be called several times for a given view in a drawing pass. Subclasses should avoid computationally intensive calculations in their implementation of the `isOpaque` method. Simple tests–for example determining if the background color is opaque as the `DraggableItemView` does–are acceptable. The `DraggableItemView` implementation is shown in Listing 4-5.

__Listing 4-5__  `DraggableItemView` implementation of `isOpaque`

```objc
- (BOOL)isOpaque
{
    // If the background color is opaque, return YES
    // otherwise, return NO
    return [[self backgroundColor] alphaComponent] >= 1.0 ? YES : NO;
}
```


Views are typically the receivers of most event and action messages. An `NSView` subclass overrides the appropriate event handling methods declared by the `NSResponder` class. When an instance of the custom view instance is the first responder, it receives the event messages as they are posted, before other objects. Similarly, by implementing the action methods, often sent by other user interface objects such as menu items, when the custom view instance is the first responder, it receives those messages. See _[Cocoa Event Handling Guide](../Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_ for a complete discussion on event handling and the responder chain.

Event messages are passed up the responder chain from the first responder. For all views, with the exception of a window's content view, a view's next responder is its superview. When view instances are inserted into the view hierarchy the next responder is set automatically. You should never send the `setNextResponder:` message directly to a view object. If you need to add objects to the responder chain, you should add them at the top of a window's responder chain—by subclassing `NSWindow` itself if it has no delegate, or the delegate class if it does.

As the class that handles display, `NSView` is typically the recipient of mouse and keyboard events. Mouse events start at the view that the click occurs in, and are passed up the responder chain. Keyboard events start at the first responder and are passed up the responder chain.

A view that is the first responder receives key events and action messages before other objects. Views can advertise that they can become the first responder by overriding the `acceptsFirstResponder` message and returning `YES`. The default `NSResponder` implementation returns `NO`. If a view is not the first responder it receives only mouse-down messages. Because the `DraggableItemView` object responds to basic key-down events, as well as the `NSResponder` action messages that are generated in response to pressing the arrow keys, it returns `YES` for `acceptsFirstResponder` as shown in Listing 4-6.

__Listing 4-6__  `DraggableItemView` implementation of `acceptsFirstResponder`

```objc
- (BOOL)acceptsFirstResponder
{
    return YES;
}
```

A view receives a `becomeFirstResponder` message when the window attempts to make the view first responder. The default implementation of this method always returns `YES`. Similarly, when a view will resign as first responder it receives a `resignFirstResponder` message. To resign first responder status, `resignFirstResponder` returns `YES`. There may be valid reasons for a view to decline resigning first responder status, for example if an action is incomplete.

If a view becomes the first responder specifically to accept key events or `NSResponder` actions, it should reflect this by drawing a focus ring. The focus ring informs the user which object is the current first responder for key events.

Views that can become first responder and handle key events typically take part in the key view loop of a window. The key-view loop allows the user to switch between views in a window by pressing the Tab or Shift-Tab keys. `NSView` provides a number of methods for setting and getting the views in the key-view loop. Most often the key-view loop ordering is set in Interface Builder by connecting a view to another view's `nextKeyView` outlet.

Custom view subclasses can interpret mouse events in any way that is appropriate. Button type views send a target-action message, whereas clicking in a drawing view might select a graphic. There are four basic types of mouse events passed to a view: mouse down, mouse dragging, mouse up, and mouse movement.

By default a view does not receive mouse-down events if it isn't in the frontmost window, referred to as the key window. By overriding the `acceptsFirstMouse:` method and returning `YES`, the window becomes the key window immediately and acts upon the mouse-down.

Mouse-down events are sent when the user presses the mouse button while the cursor is in a view. If the window containing the view is not the key window, the window becomes the key window and discards the mouse-down event. An application can change this behavior, causing the initial mouse-down to make the window key and be passed to the appropriate view by overriding the `acceptsFirstMouse:` method and returning `YES`.

The window determines which view in the view hierarchy to send the mouse-down event using the `NSView` method `hitTest:`. Once the correct view is located, it is sent a `mouseDown:` event. There are corresponding mouse-down events posted for actions made with the right mouse button, as well as with other mouse buttons using the `rightMouseDown:` and `otherMouseDown:` methods respectively. The location of the mouse event in the coordinate system of the receiver's window is returned by sending the event object passed to the `mouseDown:` method a `locationInWindow` message. To translate the point to the view's coordinate system, use the method `convertPoint:fromView:` passing `nil` as the view parameter. Listing 4-7 illustrates the `DraggableItemView` subclass's implementation of the `mouseDown:` method.

__Listing 4-7__  `DraggableItemView` implementation of `mouseDown:`

```objc
-(void)mouseDown:(NSEvent *)event
{
    NSPoint clickLocation;
    BOOL itemHit=NO;

    // convert the mouse-down location into the view coords
    clickLocation = [self convertPoint:[event locationInWindow]
                  fromView:nil];

    // did the mouse-down occur in the item?
    itemHit = [self isPointInItem:clickLocation];

    // Yes it did, note that we're starting to drag
    if (itemHit) {
    // flag the instance variable that indicates
    // a drag was actually started
    dragging=YES;

    // store the starting mouse-down location;
    lastDragLocation=clickLocation;

    // set the cursor to the closed hand cursor
    // for the duration of the drag
    [[NSCursor closedHandCursor] push];
    }
}
```

This implementation gets the mouse-down location and converts it to the view's coordinate system. Since the dragging item subclass allows the user to drag the item only when the mouse-down event occurs in the draggable rectangle, the implementation calls the `isPointInItem:` method, shown in Listing 4-8 to test whether the mouse-down was within the draggable item's bounds. If it is, the dragging instance variable is set to `YES` to note that the view should not ignore `mouseDragged:` events. To better reflect to the user that a drag is in progress the cursor is set to the closed hand cursor.

__Listing 4-8__  `DraggableItemView` implementation of `isPointInItem:`

```objc
- (BOOL)isPointInItem:(NSPoint)testPoint
{
    BOOL itemHit=NO;

    // test first if we're in the rough bounds
    itemHit = NSPointInRect(testPoint,[self calculatedItemBounds]);

    // yes, lets further refine the testing
    if (itemHit) {
    // if this was a non-rectangular shape, you would refine
    // the hit testing here
    }

    return itemHit;
}
```

Notice that the `mouseDown:` implementation in Listing 4-7 does not call the super implementation. The `NSView` class's default implementation for the mouse handling events are inherited from `NSResponder` and pass the event up the responder chain for handling, bypassing the view in question entirely. Typically a custom `NSView` subclass should not call the super implementation of any of the mouse-event methods.

Views often need to track the dragging of the mouse after a mouse-down event is received. While the mouse button is held down and the mouse moves, the view receives `mouseDragged:` messages. The `DraggableItemView` implementation of `mouseDragged:` is shown in Listing 4-9.

__Listing 4-9__  `DraggableItemView` implementation of `mouseDragged`:

```objc
-(void)mouseDragged:(NSEvent *)event
{
    if (dragging) {
       NSPoint newDragLocation=[self convertPoint:[event locationInWindow]
                                         fromView:nil];


       // offset the item by the change in mouse movement
       // in the event
       [self offsetLocationByX:(newDragLocation.x-lastDragLocation.x)
                          andY:(newDragLocation.y-lastDragLocation.y)];

       // save the new drag location for the next drag event
       lastDragLocation=newDragLocation;

       // support automatic scrolling during a drag
       // by calling NSView's autoscroll: method
       [self autoscroll:event];
    }
}
```

The view instance receives all the mouse-dragged notifications for the view, but the subclass is only interested in drag events that were initiated by mouse-down events in the draggable item itself. By testing the instance variable `dragging`, the view can determine whether the drag should be acted upon. If so, then the draggable item is offset by the change in mouse location since the last mouse event, which is tracked by the class's instance variable `lastDragLocation`.

The `offsetLocationByX:andY:` method called by the `mouseDragged:` method is shown in Listing 4-10. It marks the draggable item's area as needing display before and after altering the item's location by the requested amount. If the view returns `YES` when sent an `isFlipped` message, the offset in the vertical direction is multiplied by -1 to correspond to the flipped view coordinates. In the `DraggableItemView` implementation the code is factored into its own method because it will be reused later.

__Listing 4-10__  `DraggableItemView` implementation of `offsetLocationByX:andY:`

```objc
- (void)offsetLocationByX:(float)x andY:(float)y
{
    // tell the display to redraw the old rect
    [self setNeedsDisplayInRect:[self calculatedItemBounds]];

    // since the offset can be generated by both mouse moves
    // and moveUp:, moveDown:, etc.. actions, we'll invert
    // the deltaY amount based on if the view is flipped or
    // not.
    int invertDeltaY = [self isFlipped] ? -1: 1;

    location.x=location.x+x;
    location.y=location.y+y*invertDeltaY;

    // invalidate the new rect location so that it'll
    // be redrawn
    [self setNeedsDisplayInRect:[self calculatedItemBounds]];

}
```

Finally, when the mouse button is released, the view receives a `mouseUp:` message. The `DraggableItemView` implementation shown in Listing 4-11 updates the dragging instance variable to indicate that the dragging action has completed and resets the cursor. The `invalidateCursorRectsForView:` message is discussed at the end of this section.

__Listing 4-11__  `DraggableItemView` implementation of `mouseUp:`

```objc
-(void)mouseUp:(NSEvent *)event
{
    dragging=NO;

    // finished dragging, restore the cursor
    [NSCursor pop];

    // the item has moved, we need to reset our cursor
    // rectangle
    [[self window] invalidateCursorRectsForView:self];
}
```

A second technique for handling mouse dragging is sometimes used, commonly referred to as “short circuiting” the event loop. An application can implement the `mouseDown:` method and loop continuously, collecting mouse-dragged events until the mouse-up event is received. Events that do not match the event mask remain in the event queue and are handled when the loop exists.

If the `DraggableItemView` class were to implement the same behavior using this technique, it would only implement the `mouseDown:` method, eliminating the `mouseDragged:` and `mouseUp:` method implementations. The `mouseDown:` implementation shown in Listing 4-12 uses the “short circuiting” technique.

__Listing 4-12__  Alternate `mouseDown:` implementation

```objc
-(void)mouseDown:(NSEvent *)event
{
    BOOL loop = YES;

    NSPoint clickLocation;

    // convert the initial mouse-down location into the view coords
    clickLocation = [self convertPoint:[event locationInWindow]
                  fromView:nil];

    // did the mouse-down occur in the draggable item?
    if ([self isPointInItem:clickLocation]) {
        // we're dragging, so let's set the cursor
    // to the closed hand
    [[NSCursor closedHandCursor] push];

    NSPoint newDragLocation;

    // the tight event loop pattern doesn't require the use
    // of any instance variables, so we'll use a local
    // variable localLastDragLocation instead.
    NSPoint localLastDragLocation;

    // save the starting location as the first relative point
    localLastDragLocation=clickLocation;

    while (loop) {
        // get the next event that is a mouse-up or mouse-dragged event
        NSEvent *localEvent;
        localEvent= [[self window] nextEventMatchingMask:NSLeftMouseUpMask | NSLeftMouseDraggedMask];


        switch ([localEvent type]) {
        case NSLeftMouseDragged:

            // convert the new drag location into the view coords
            newDragLocation = [self convertPoint:[localEvent locationInWindow]
                        fromView:nil];


            // offset the item and update the display
            [self offsetLocationByX:(newDragLocation.x-localLastDragLocation.x)
                       andY:(newDragLocation.y-localLastDragLocation.y)];

            // update the relative drag location;
            localLastDragLocation=newDragLocation;

            // support automatic scrolling during a drag
            // by calling NSView's autoscroll: method
            [self autoscroll:localEvent];

            break;
        case NSLeftMouseUp:
            // mouse up has been detected,
            // we can exit the loop
            loop = NO;

            // finished dragging, restore the cursor
            [NSCursor pop];

            // the rectangle has moved, we need to reset our cursor
            // rectangle
            [[self window] invalidateCursorRectsForView:self];

            break;
        default:
            // Ignore any other kind of event.
            break;
        }
    }
    };
    return;
}
```


In addition to mouse-down, mouse-dragged, and mouse-up events, a view can also receive mouse-moved events. Mouse-moved events allow the view to track the location of the cursor whenever it is located above the view. By default, views don't receive mouse-moved events because they can occur very often, as a result clogging the event queue.

Mouse-moved events are initiated by the `NSWindow` instance that contains a view. In order for a view to receive mouse-moved events, it must explicitly request them by sending its window a `setAcceptsMouseMovedEvents:` message, passing `YES` as the parameter. When enabled, a view receives `mouseMoved:` events whenever the cursor is located within the view. Unfortunately, it is not possible to enable mouse-moved events for a single view using this technique.

The `NSView` class allows a view instance to register tracking rectangles. Registering an object as the owner of a tracking rectangle causes the owner to receive `mouseEntered:` and `mouseExited:` messages as the cursor enters and exists the rectangle. An application registers tracking rectangles using the `NSView` method `addTrackingRect:owner:userData:assumeInside:`. The tracking rectangle is provided in the view's coordinate system, and the owner is the object that will receive the `mouseEntered:` and `mouseExited:` messages. The `userData` parameter is any arbitrary object that will be provided as the `userData` object in the `NSEvent` object passed to the `mouseEntered:` and `mouseExited:` methods. The `assumeInside` parameter indicates whether the cursor should be assumed to be inside the tracking rectangle initially. The method returns a tracking tag that identifies the tracking rectangle, and the tracking tag is used to unregister the owner for tracking notifications using the method `removeTrackingRect:`. An application can register tracking rectangles only for views that are currently displayed in a window.

Although tracking rectangles are created and used by views, they are actually maintained by a view's window. As a result, tracking rectangles do not automatically move or resize when the view does. It is a subclass's responsibility to remove and re-register tracking rectangles when the frame of the view changes or it is inserted as a subview. This is commonly done by overriding the `NSView` method `resetCursorRects`.

`NSView` also provides methods to support a common use of tracking rectangles; changing the cursor as a result of the mouse entering a rectangle. The `addCursorRect:cursor:` method allows you to register a rectangle using the view's coordinate system and specify the cursor that should be displayed while the mouse is over that rectangle. Cursor rectangles are volatile. When the view's window resizes, the frame or bounds of a view changes, the view is moved in the hierarchy, or the view is scrolled, the view receives a `resetCursorRects` message. Subclasses should override `resetCursorRects` and register any required cursor rectangles and tracking rectangles in that method. The `removeCursorRect:cursor:` method allows you to explicitly remove a cursor rectangle that matches the provided parameters exactly. The `discardCursorRects` method removes all the cursor rectangles for a view.

The `DraggableItemView` provides visual feedback that the cursor is over the draggable item by changing the cursor to the open handle. The implementation of `resetCursorRects`, shown in Listing 4-13, discards all the current cursor rectangles and adds a new cursor rectangle for the draggable item's bounds.

__Listing 4-13__  `DraggableItemView` implementation of `resetCursorRects`

```objc
-(void)resetCursorRects
{
    // remove the existing cursor rects
    [self discardCursorRects];

    // add the draggable item's bounds as a cursor rect

    // clip the draggable item's bounds to the view's visible rect
    NSRect clippedItemBounds = NSIntersectionRect([self visibleRect], [self calculatedItemBounds]);

    // if the clipped item bounds isn't empty then the item is at least partially
    // in the visible rect. Register the clipped item bounds
    if (!NSIsEmptyRect(clippedItemBounds)) {
         [self addCursorRect:clippedItemBounds cursor:[NSCursor openHandCursor]];
    }
}
```

Adding a cursor rectangle for a view does not automatically restrict the cursor rectangle to the visible area of the view. You must do this yourself by finding the intersection of the proposed cursor rectangle with the view's visible rectangle. If the resulting rectangle is not empty it should be passed as the first argument to the `addCursorRect:cursor:` method.

You should never call `resetCursorRects` directly; instead send the view's window an `invalidateCursorRectsForView:` message, passing the appropriate view. The `DraggableItemView` object needs to reset its cursor rectangle each time the draggable item moves. The `mouseUp:` implementation shown in [Listing 4-11](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzyfvbuqnznknltcmi) sends the view's window an `invalidateCursorRectsForView:` message, passing the view itself as the parameter. Likewise, in the version of `mouseDown:` that short circuits the event loop, shown in [Listing 4-12](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzyfvbuqnznknltcmq), the `invalidateCursorRectsForView:` message is sent when the mouse-up event is detected.

As discussed in Becoming First Responder, a view receives key-down events only if it overrides `acceptsFirstResponder` and returns `YES`. Because the `DraggableItemView` object responds to user key-presses, the class overrides this method and returns `YES`.

There are two key-down related methods provided by `NSResponder`: the methods `keyDown:` and `performKeyEquivalent:`. `NSResponder` also declares a number of responder actions that are triggered by key-down events. These actions map specific keystrokes to common actions. By implementing the appropriate action methods, you can bypass overriding the more complicated `keyDown:` method.

Your custom view should override the `performKeyEquivalent:` method if your view reacts to simple key equivalents. An example usage of a key equivalent is setting the Return key as the key equivalent of a button. When the user presses Return, the button acts as though it had been clicked. A subclass's implementation of `performKeyEquivalent:` should return `YES` if it has handled the key event, `NO` if it should be passed up the event chain. If a view implements `performKeyEquivalent:`, it typically does not also implement `keyDown:`.

The `DraggableItemView` class overrides the `keyDown:` method, shown in Listing 4-14, which allows the user to press the R key to reset the position of the draggable rectangle to the origin of the view.

__Listing 4-14__  `DraggableItemView` implementation of `keyDown:`

```objc
- (void)keyDown:(NSEvent *)event
{
    BOOL handled = NO;
    NSString  *characters;

    // get the pressed key
    characters = [event charactersIgnoringModifiers];

    // is the "r" key pressed?
    if ([characters isEqual:@"r"]) {
        // Yes, it is
        handled = YES;

        // reset the rectangle
        [self setItemPropertiesToDefault:self];
    }
    if (!handled)
        [super keyDown:event];

}
```

A view handles the `NSResponder` action methods by simply implementing the appropriate method. The `DraggableItemView` class implements four of these methods, corresponding to the up, down, left, and right movement actions. The implementations are shown in Listing 4-15.

__Listing 4-15__  `DraggableItemView` implementation of `moveUp:`, `moveDown:`, `moveLeft:`, and `moveRight:` actions

```objc
-(void)moveUp:(id)sender
{
    [self offsetLocationByX:0 andY: 10.0];
    [[self window] invalidateCursorRectsForView:self];
}

-(void)moveDown:(id)sender
{
    [self offsetLocationByX:0 andY:-10.0];
    [[self window] invalidateCursorRectsForView:self];
}

-(void)moveLeft:(id)sender
{
    [self offsetLocationByX:-10.0 andY:0.0];
    [[self window] invalidateCursorRectsForView:self];
}

-(void)moveRight:(id)sender
{
    [self offsetLocationByX:10.0 andY:0.0];
    [[self window] invalidateCursorRectsForView:self];
}
```

Each of the methods in Listing 4-15 offset the draggable item's location in the appropriate direction using the `offsetLocationByX:andY:` method, passing the amount to offset the rectangle. The vertical offset is adjusted by the `offsetLocationByX:andY:` implementation as appropriate if the view is flipped. After moving the rectangle, each method invalidates the cursor rectangles. This functionality could also have been implemented in `keyDown:` directly by examining the Unicode character of the pressed key, detecting the arrow keys, and acting accordingly. However, using the responder action methods allow the commands to be remapped by the user.

`NSResponder` isn't the only class that can generate events on the responder chain. Any control that implements target-action methods can send those actions through the responder chain rather than to a specific object by connecting the control to the first responder proxy in Interface Builder and specifying the action. A detailed discussion of sending action messages through the responder chain is available in "[The Responder Chain](../Cocoa%20Event%20Handling%20Guide/Event%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2jninedglktk4za)" in _[Cocoa Event Handling Guide](../Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_.

The `DraggableItemView` class implements the `changeColor:` method that is sent through the responder chain when the color is changed in a Color panel. Listing 4-16 shows the `DraggableItemView` implementation of `changeColor:`.

__Listing 4-16__  `DraggableItemView` implementation of `changeColor:`

```objc
- (void)changeColor:(id)sender
{
    // Set the color in response
    // to the color changing in the Color panel.
    // get the new color by asking the sender, the Color panel
    [self setItemColor:[sender color]];
}
```

When the Color panel is visible and an instance of the `DraggableItemView` class is the first responder, changing the color in the Color panel causes the rectangle to change color.

Classes should provide key-value-coding-compliant accessor methods for all their public properties. This provides a published interface to other objects that need to set the various display aspects of the view. Accessor methods also enforce good design and encapsulate memory management issues, which greatly reduces the chance of memory leaks and crashes.

The `DraggableItemView` class implements getter and setter accessor methods for the following properties: `itemColor`, `backgroundColor`, and `location`. Each of the setter accessor methods test to see if the new value is different from the current value and, if it is, saves the new value and marks the view as needing to redisplay the appropriate portion. In addition, the `setLocation:` method also invalidates the cursor tracking rectangle when the location changes.

__Listing 4-17__  `DraggableItemView` accessor methods

```objc
- (void)setItemColor:(NSColor *)aColor
{
    if (![itemColor isEqual:aColor]) {
        [itemColor release];
        itemColor = [aColor retain];

        // if the colors are not equal, mark the
        // draggable rect as needing display
        [self setNeedsDisplayInRect:[self calculatedItemBounds]];
    }
}


- (NSColor *)itemColor
{
    return [[itemColor retain] autorelease];
}

- (void)setBackgroundColor:(NSColor *)aColor
{
    if (![backgroundColor isEqual:aColor]) {
        [backgroundColor release];
        backgroundColor = [aColor retain];

        // if the colors are not equal, mark the
        // draggable rect as needing display
        [self setNeedsDisplayInRect:[self calculatedItemBounds]];
    }
}


- (NSColor *)backgroundColor
{
    return [[backgroundColor retain] autorelease];
}

- (void)setLocation:(NSPoint)point
{
    // test to see if the point actually changed
    if (!NSEqualPoints(point,location)) {
        // tell the display to redraw the old rect
        [self setNeedsDisplayInRect:[self calculatedItemBounds]];

        // reassign the rect
        location=point;

        // display the new rect
        [self setNeedsDisplayInRect:[self calculatedItemBounds]];

        // invalidate the cursor rects
        [[self window] invalidateCursorRectsForView:self];
    }
}

- (NSPoint)location {
    return location;
}
```


The `dealloc` method is called when a view's retain count is zero. Your application should never call `dealloc` explicitly. The autorelease mechanism calls it when appropriate.

The `DraggableItemView` implementation of `dealloc` releases the display color object and calls the super implementation of `dealloc`.

```objc
- (void)dealloc
{
    [color release];
    color=nil;
    [super dealloc];
}
```

[Next](Advanced%20Custom%20View%20Tasks.md)[Previous](Working%20with%20the%20View%20Hierarchy.md)

