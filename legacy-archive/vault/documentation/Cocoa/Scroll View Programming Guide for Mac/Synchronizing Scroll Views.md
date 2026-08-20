---
title: Scroll View Programming Guide for Mac
apple_id: TP40003221
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2010-06-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSScrollViewGuide/Articles/SynchroScroll.html
archived_at: '2026-07-15T07:16:53.416419Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Scroll View Programming Guide for Mac](Introduction%20to%20Scroll%20View%20Programming%20Guide%20for%20Cocoa.md)


[Next](Document%20Revision%20History.md)[Previous](Scrolling%20the%20Document%20View.md)

# Synchronizing Scroll Views

An application user interface may require that scrolling of one scroll view causes synchronized scrolling in another scroll view. You synchronize the scrolling of two scroll view's by having the views register to receive notifications of the changes in the other's content view bounds.

For example, an interface has two adjacent scroll views: right and left scroll views. The right scroll view registers to receive bounds notifications sent by the content view of the left scroll view. Similarly, the left scroll view registers for bounds notification changes sent by the right scroll view's content view. When a scroll view receives a bounds change notification, it determines which content view changed by examining the object returned by sending the notification an object method. It then checks to see if its origin is already at the origin of the content view bounds and if it is not, it scrolls to that location. This check ensures that the scroll view doesn't scroll if it is already at the correct location, preventing notifications being sent to the other scroll view and causing an infinite loop.

Implementing this synchronizing in a generic way is best done by subclassing `NSScrollView`. The `SynchroScrollView` class example synchronizes scrolling only in the vertical plane and requires the following:

- An instance variable that tracks the synchronized view (`synchronizedScrollView`)
- A method to set the view to synchronize with (`setSynchronizedScrollView:`)
- A method to break synchronization (`stopSynchronizing`)
- A method that receives the bounds change notifications (`synchronizedViewContentBoundsDidChange:`)

The `SynchroScrollView` implementation relies on the scroll view being retained by some other object, typically the view hierarchy itself. It is the application's responsibility to break the synchronization between the views before the views are deallocated.

Listing 1 shows the class declaration.

__Listing 1__  `SynchroScrollView.h` class declaration

```objc
@interface SynchroScrollView : NSScrollView {
    NSScrollView* synchronizedScrollView; // not retained
}

- (void)setSynchronizedScrollView:(NSScrollView*)scrollview;
- (void)stopSynchronizing;
- (void)synchronizedViewContentBoundsDidChange:(NSNotification *)notification;

@end
```

The `synchronizedScrollView` variable is used to track the synchronized scroll view. Both scroll views that are synchronized are set as each other's `synchronizedScrollView`. As a result, the `synchronizedScrollView` is a weak reference and it is not retained.

An application initiates synchronization by sending both scroll view's a `setSynchronizedScrollView:` message, passing the other scroll view as the parameter. Listing 2 shows the `SynchroScrollView` implementation of `setSynchronizedScrollView:`.

__Listing 2__  `SynchroScrollView.m` implementation of `setSynchronizedScrollView:`

```objc
- (void)setSynchronizedScrollView:(NSScrollView*)scrollview
{
    NSView *synchronizedContentView;

    // stop an existing scroll view synchronizing
    [self stopSynchronizing];

    // don't retain the watched view, because we assume that it will
    // be retained by the view hierarchy for as long as we're around.
    synchronizedScrollView = scrollview;

    // get the content view of the
    synchronizedContentView=[synchronizedScrollView contentView];

    // Make sure the watched view is sending bounds changed
    // notifications (which is probably does anyway, but calling
    // this again won't hurt).
    [synchronizedContentView setPostsBoundsChangedNotifications:YES];

    // a register for those notifications on the synchronized content view.
    [[NSNotificationCenter defaultCenter] addObserver:self
                         selector:@selector(synchronizedViewContentBoundsDidChange:)
                         name:NSViewBoundsDidChangeNotification
                           object:synchronizedContentView];
}
```

This method first stops any existing synchronization by calling `stopSynchronizing`. It then keeps a reference to the new scroll view in `synchronizedScrollView`. Finally, it registers to receive bounds change notifications for the content view of the `synchronizedScrollView`. The change notifications are sent to the `synchronizedViewContentBoundsDidChange:` method, shown in Listing 3.

__Listing 3__  `SynchroScrollView.m` implementation of `synchronizedViewContentBoundsDidChange:`

```objc
- (void)synchronizedViewContentBoundsDidChange:(NSNotification *)notification
{
    // get the changed content view from the notification
    NSClipView *changedContentView=[notification object];

    // get the origin of the NSClipView of the scroll view that
    // we're watching
    NSPoint changedBoundsOrigin = [changedContentView documentVisibleRect].origin;;

    // get our current origin
    NSPoint curOffset = [[self contentView] bounds].origin;
    NSPoint newOffset = curOffset;

    // scrolling is synchronized in the vertical plane
    // so only modify the y component of the offset
    newOffset.y = changedBoundsOrigin.y;

    // if our synced position is different from our current
    // position, reposition our content view
    if (!NSEqualPoints(curOffset, changedBoundsOrigin))
    {
    // note that a scroll view watching this one will
    // get notified here
    [[self contentView] scrollToPoint:newOffset];
    // we have to tell the NSScrollView to update its
    // scrollers
    [self reflectScrolledClipView:[self contentView]];
    }
}
```

The view that triggered the change notification is determined by sending the notification an `object` message. The origin of that content view is determined and the new origin that the receiving scroll view should reflect is determined. If the two locations differ, the receiver scrolls to the new origin. This test is necessary to prevent the scroll view that originated the scrolling action from acting on the change in the other scroll view's content view, causing an infinite loop.

The `stopSynchronizing` method, shown in Listing 4, causes the receiver to stop listening for bounds-change notifications in the synchronized scroll view's content view and sets the `synchronizedScrollView` instance variable to `nil`.

__Listing 4__  `SynchroScrollView.m` implementation of `stopSynchronizing`

```objc
- (void)stopSynchronizing
{
    if (synchronizedScrollView != nil) {
    NSView* synchronizedContentView = [synchronizedScrollView contentView];

    // remove any existing notification registration
    [[NSNotificationCenter defaultCenter] removeObserver:self
                            name:NSViewBoundsDidChangeNotification
                              object:synchronizedContentView];

    // set synchronizedScrollView to nil
    synchronizedScrollView=nil;
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](Scrolling%20the%20Document%20View.md)

