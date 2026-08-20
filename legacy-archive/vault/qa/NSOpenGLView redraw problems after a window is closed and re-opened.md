---
title: NSOpenGLView redraw problems after a window is closed and re-opened.
apple_id: DTS10003326
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2004-12-03'
source_url: https://developer.apple.com/library/archive/qa/qa1353/_index.html
archived_at: '2026-07-18T02:30:25.869890Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1353

# NSOpenGLView redraw problems after a window is closed and re-opened.

## Q:  I have an instance of an NSOpenGLView subclass that doesn't draw correctly after I close and then re-open its window. What's happening, and how can I fix it?

A: In Mac OS X, version 10.3 and earlier, NSOpenGLView doesn't redraw properly after the window it's in has been closed and re-opened. One easy work-around is to remove the view from the view hierarchy, and then re-insert it.

In the code below, MyOpenGLView registers itself for the notification that its window will close. In the `-prepareForWindowClosing:` method, the view also registers itself for the NSWindowDidUpdateNotification, which will be sent when the window is re-opened.

The `-windowReopened:` method retains the view, removes it from the view hierarchy, then re-inserts it and balances the `-retain` message with a `-release` message.

__Listing 1__  Resetting NSOpenGLView's drawing environment

```objc
@implementation MyOpenGLView

- (void) awakeFromNib
{
    [[NSNotificationCenter defaultCenter]
      addObserver: self
         selector: @selector(prepareForWindowClosing:)
             name: NSWindowWillCloseNotification
           object: [self window]];
}

- (void) prepareForWindowClosing:(NSNotification *) notification
{
      // we'll need to know the next time the window updates,
      // which will be when it's re-opened.
    [[NSNotificationCenter defaultCenter]
      addObserver: self
         selector: @selector(windowReopened:)
             name: NSWindowDidUpdateNotification
           object: [self window]];

      // Make sure we draw right away when the window is re-opened.
    [self setNeedsDisplay:YES];
}

- (void) windowReopened:(NSNotification *)aNotification
{
      // Fix up the state of the NSOpenGLView by removing it from and
      // re-adding it to the view hierarchy
    NSView *superviewStash = [self superview];

    [self retain]; // Must retain before removing from superview
    [self removeFromSuperview];
    [superviewStash addSubview:self];
    [self release]; // Must balance all -retain and -release messages.

      // After this, we don't care about window exposed notifications, so
      // we'll stop listening for them
    [[NSNotificationCenter defaultCenter]
      removeObserver:self
                name:NSWindowDidUpdateNotification
              object:[self window]];
}

- (void)dealloc
{
    [[NSNotificationCenter defaultCenter] removeObserver:self];
    [super dealloc];
}

@end
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-03-06 | Workaround for NSOpenGLView failure to draw after its window is closed and re-opened. |
| 2004-12-03 | New document that workaround for NSOpenGLView failure to draw after its window is closed and re-opened. |

