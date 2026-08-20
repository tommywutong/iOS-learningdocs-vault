---
title: Text System User Interface Layer Programming Guide
apple_id: 10000090i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextUILayer/Tasks/CreateTextViewProg.html
archived_at: '2026-07-15T07:20:34.226753Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text System User Interface Layer Programming Guide](Introduction%20to%20Text%20System%20User%20Interface%20Layer.md)


[Next](Putting%20an%20NSTextView%20Object%20in%20an%20NSScrollView.md)[Previous](Creating%20an%20NSTextView%20Object.md)

# Creating an NSTextView Object Programmatically

At times, you may need to assemble the text system programmatically. You can do this in either of two ways: by creating an `NSTextView` object and letting it create its network of supporting objects or by building the network of objects yourself. In most cases, you’ll find it sufficient to create an `NSTextView` object and let it create the underlying network of text-handling objects, as discussed in this article. If your application has complex text-layout requirements, you’ll have to create the network yourself; see “Creating Text System Objects” in _[Cocoa Text Architecture Guide](../../Cocoa%20Text%20Architecture%20Guide/About%20the%20Cocoa%20Text%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tinjz)_ for information.

You create an `NSTextView` object programmatically in the usual way: by sending the `alloc` and `init...` messages. You can also create an `NSTextView` object using either of these methods:

- `initWithFrame:textContainer:` (the designated initializer)
- `initWithFrame:`

The method that takes one argument, `initWithFrame:`, is the simplest way to obtain an `NSTextView` object—it creates all the other components of the text system for you. If you use the method that takes two arguments, `initWithFrame:textContainer:`, you must create the other components yourself.

Listing 1 shows how you can create an `NSTextView` object, given an `NSWindow` object represented here by `aWindow`.

__Listing 1__  Creating an NSTextView object programmatically

```
/* determine the size for the NSTextView */
NSRect cFrame =[[aWindow contentView] frame];

/* create the NSTextView and add it to the window */
NSTextView *theTextView = [[NSTextView alloc] initWithFrame:cFrame];
[aWindow setContentView:theTextView];
[aWindow makeKeyAndOrderFront:nil];
[aWindow makeFirstResponder:theTextView];
```

This code determines the size for the text view’s frame rectangle by asking `aWindow` for the size of its content view. The `NSTextView` is then created and made the content view of `aWindow` using `setContentView:`. Finally, the `makeKeyAndOrderFront:` and `makeFirstResponder:` messages display the window and cause the text view to prepare to accept keyboard input.

The `initWithFrame:` method not only initializes the receiving `NSTextView` object, it causes the object to create and interconnect the other components of the text system. This is a convenience that frees you from having to create and interconnect them yourself.

[Next](Putting%20an%20NSTextView%20Object%20in%20an%20NSScrollView.md)[Previous](Creating%20an%20NSTextView%20Object.md)

