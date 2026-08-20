---
title: Text System User Interface Layer Programming Guide
apple_id: 10000090i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextUILayer/Tasks/TextInScrollView.html
archived_at: '2026-07-15T07:20:39.765568Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text System User Interface Layer Programming Guide](Introduction%20to%20Text%20System%20User%20Interface%20Layer.md)


[Next](Using%20Multiple%20NSTextViews.md)[Previous](Creating%20an%20NSTextView%20Object%20Programmatically.md)

# Putting an NSTextView Object in an NSScrollView

A scrolling text view is commonly required in applications, and Interface Builder provides an NSTextView configured just for this purpose. However, at times you may need to create a scrolling text view programmatically.

The process consists of three steps: setting up the NSScrollView, setting up the NSTextView, and assembling the pieces. This article describes these steps in terms of a typical text view configured with a vertical scroll bar only, then shows alternate statements used to configure a horizontal scroll bar.

Assuming an object has the variable `theWindow` that represents the window where the scrolling view is displayed, you can set up the NSScrollView using the code in Listing 1.

__Listing 1__  Setting up the scroll view

```
NSScrollView *scrollview = [[NSScrollView alloc]
            initWithFrame:[[theWindow contentView] frame]];
NSSize contentSize = [scrollview contentSize];

[scrollview setBorderType:NSNoBorder];
[scrollview setHasVerticalScroller:YES];
[scrollview setHasHorizontalScroller:NO];
[scrollview setAutoresizingMask:NSViewWidthSizable |
            NSViewHeightSizable];
```

Note that the code creates an NSScrollView that completely covers the content area of the window it’s displayed in. It also specifies a vertical scroll bar but no horizontal scroll bar, since this scrolling text view wraps text within the horizontal extent of the NSTextView, but lets text flow beyond the vertical extent of the NSTextView. To use a horizontal scroll bar, you must configure the scroll view and text view slightly differently, as described in [Setting Up a Horizontal Scroll Bar](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqheztqljrgy2dmnjs).

Finally, the code sets how the NSScrollView reacts when the window it’s displayed in changes size. Turning on the NSViewWidthSizable and NSViewHeightSizable bits of its resizing mask ensures that the NSScrollView grows and shrinks to match the window’s dimensions.

The next step is to create and configure an NSTextView to fit in the NSScrollView. Listing 2 shows the statements that accomplish this step.

__Listing 2__  Setting up the text view

```
theTextView = [[NSTextView alloc] initWithFrame:NSMakeRect(0, 0,
            contentSize.width, contentSize.height)];
[theTextView setMinSize:NSMakeSize(0.0, contentSize.height)];
[theTextView setMaxSize:NSMakeSize(FLT_MAX, FLT_MAX)];
[theTextView setVerticallyResizable:YES];
[theTextView setHorizontallyResizable:NO];
[theTextView setAutoresizingMask:NSViewWidthSizable];

[[theTextView textContainer]
            setContainerSize:NSMakeSize(contentSize.width, FLT_MAX)];
[[theTextView textContainer] setWidthTracksTextView:YES];
```

Listing 2 specifies that the NSTextView’s width and height initially match those of the content area of the NSScrollView. The `setMinSize:` message tells the NSTextView that it can get arbitrarily small in width, but no smaller than its initial height. The `setMaxSize:` message allows the receiver to grow arbitrarily in either dimension. These limits are used by the NSLayoutManager when it resizes the NSTextView to fit the text laid out.

The next three messages determine how the NSTextView’s dimensions change in response to additions or deletions of text and to changes in the scroll view’s size. The NSTextView is set to grow vertically as text is added but not horizontally. Its resizing mask is set to allow it to change width in response to changes in the width of its `superview`. Since, except for the minimum and maximum values, the NSTextView’s height is determined by the amount of text it has in it, its height should not change with that of its superview.

The last two messages in this step are to the NSTextContainer, not the NSTextView. One message sets the text container’s initial width to that of the scroll view and its height to the maximum size of the text view. The last message tells the NSTextContainer to resize its width according to the width of the NSTextView. Recall that the text system lays out text according to the dimensions stored in NSTextContainer objects. An NSTextView provides a place for the text to be displayed, but its dimensions and those of its NSTextContainer can be quite different. The `setWidthTracksTextView:YES` message ensures that as the NSTextView is resized, the width dimension stored in its NSTextContainer is likewise resized, causing the text to be laid out within the new boundaries.

The last step is to assemble and display the pieces. Listing 3 shows the statements that accomplish this step.

__Listing 3__  Assembling the pieces

```
[scrollview setDocumentView:theTextView];
[theWindow setContentView:scrollview];
[theWindow makeKeyAndOrderFront:nil];
[theWindow makeFirstResponder:theTextView];
```


To set up both horizontal and vertical scroll bars, use the statements in Listing 4 in place of the corresponding statements in the previous listings.

__Listing 4__  Setting up a horizontal scroll bar

```
[[theTextView enclosingScrollView] setHasHorizontalScroller:YES];
[theTextView setHorizontallyResizable:YES];
[theTextView setAutoresizingMask:(NSViewWidthSizable | NSViewHeightSizable)];
[[theTextView textContainer] setContainerSize:NSMakeSize(FLT_MAX, FLT_MAX)];
[[theTextView textContainer] setWidthTracksTextView:NO];
```

This code fragment adds the horizontal scroll bar to the scroll view and makes the text view horizontally resizable so it can display text of any width. The code sets the text view’s resizing mask so that it changes in both width and height in response to corresponding changes in its superview. The next-to-last message sets both dimensions of the text container to an arbitrarily large value, which essentially means the text is laid out in one long line, and the last message ensures that the text container does not resize horizontally with the text view.

[Next](Using%20Multiple%20NSTextViews.md)[Previous](Creating%20an%20NSTextView%20Object%20Programmatically.md)

