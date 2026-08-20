---
title: Scroll View Programming Guide for Mac
apple_id: TP40003221
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2010-06-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSScrollViewGuide/Articles/Creating.html
archived_at: '2026-07-15T07:16:53.391680Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Scroll View Programming Guide for Mac](Introduction%20to%20Scroll%20View%20Programming%20Guide%20for%20Cocoa.md)


[Next](Scrolling%20the%20Document%20View.md)[Previous](How%20Scroll%20Views%20Work.md)

# Creating and Configuring a Scroll View

Scroll views can be created and configured programmatically or in Interface Builder. This article describes both procedures.

Creating a scroll view in Interface Builder is straightforward.

1. Create the view, or views, that will be the document view of the scroll view.
2. Select that view, or views, that will be the scroll view's document view.
3. Choose Layout > Make subviews of > Scroll View. This creates a new `NSScrollView` instance with the selected view, or views, as its document view.
4. Open the inspector and configure the visible scrollers, background color, and line and page scroll amounts.

Applications often create scroll views programmatically. Instances of `NSScrollView` are created using the `initWithFrame:` method, specifying the position and size of the scroll view's frame rectangle. After initializing the `NSScrollView` instance you must, at a minimum, set the document view using the method `setDocumentView:`.

The example code in Listing 1 demonstrates how to create a scroll view for an `NSImageView` instance that is large enough to display the entire image.

__Listing 1__  Creating a scroll view instance programmatically

```
// theWindow is an IBOutlet that is connected to a window
// theImage is assumed to be declared and populated already

// determine the image size as a rectangle
// theImage is assumed to be declared elsewhere
NSRect imageRect=NSMakeRect(0.0,0.0,[theImage size].width,[theImage size].height);


// create the image view with a frame the size of the image
NSImageView *theImageView=[[NSImageView alloc] initWithFrame:imageRect];
[theImageView setBounds:imageRect];

// set the image for the image view
[theImageView setImage:theImage];

// create the scroll view so that it fills the entire window
// to do that we'll grab the frame of the window's contentView
// theWindow is an outlet connected to a window instance in Interface Builder
NSScrollView *scrollView = [[NSScrollView alloc] initWithFrame:
                                        [[theWindow contentView] frame]];

// the scroll view should have both horizontal
// and vertical scrollers
[scrollView setHasVerticalScroller:YES];
[scrollView setHasHorizontalScroller:YES];

// configure the scroller to have no visible border
[scrollView setBorderType:NSNoBorder];

// set the autoresizing mask so that the scroll view will
// resize with the window
[scrollView setAutoresizingMask:NSViewWidthSizable|NSViewHeightSizable];

// set theImageView as the documentView of the scroll view
[scrollView setDocumentView:theImageView];

// setting the documentView retains theImageView
// so we can now release the imageView
[theImageView release];

// set the scrollView as the window's contentView
// this replaces the existing contentView and retains
// the scrollView, so we can release it now
[theWindow setContentView:scrollView];
[scrollView release];


// display the window
[theWindow makeKeyAndOrderFront:nil];
}
```

When created programmatically, scroll views have no scrollers. You specify that a scroll view should display scrollers by passing an argument of `YES` to the methods `setHasVerticalScroller:` and `setHasHorizontalScroller:`. The scroll view allocates and displays the scrollers automatically. You can configure a scroll view to display its scrollers only when the document view is sufficiently large to require scrolling using the method `setAutohidesScrollers:`, passing `YES` as the parameter.

It is difficult to calculate the frame size of a scroll view if you know only the required size of the content view. `NSScrollView` provides the convenience class method `frameSizeForContentSize:hasHorizontalScroller:hasVerticalScroller:borderType:` to determine the scroll view's frame size based on the content area, presence of scroll bars, and the scroll view's border type. The method returns a rectangle that is suitable for using with `initWithFrame:`.

`NSScrollView` defines two levels of incremental scrolling: a line scroll increment and a page scroll increment. Each of these values can be configured separately for a scroll view's horizontal and vertical scrolling directions.

The line scroll increment moves the document view by a small amount, often in response to the user clicking the scroll buttons of a scroller. The line scroll increment is set for both horizontal and vertical directions using the `setLineScroll:` method. Alternatively, you can specify line scroll increment for the vertical and horizontal scrollers separately using the `setVerticalLineScroll:` and `setHorizontalLineScroll:` methods, respectively.

Scrolling by page moves the document view by a larger amount, typically the size of the document view's visible region. The page scroll amount is specified using the `setPageScroll:` method or separately using the `setVerticalPageScroll:` and `setHorizontalPageScroll:` methods. The page scroll amount differs from the line scroll increment in that the page scroll values specify the amount of visible view content that will remain when the document view scrolls. Setting the page scroll value to 0.0 implies that the entire visible portion of the document view is replaced when a page scroll occurs.

Users scroll directly to a location in the document by dragging a scroller’s knob. By default, a scroll view updates the contents dynamically as it scrolls. You disable dynamic scrolling by sending the `setScrollsDynamically:` method to the scroll view, passing `NO` as the parameter. In dynamic scrolling is turned off, updates occur only when the user releases the mouse.

[Next](Scrolling%20the%20Document%20View.md)[Previous](How%20Scroll%20Views%20Work.md)

