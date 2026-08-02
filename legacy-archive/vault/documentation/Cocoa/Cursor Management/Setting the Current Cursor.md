---
title: Cursor Management
apple_id: 10000066i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CursorMgmt/Tasks/ChangingCursors.html
archived_at: '2026-07-15T07:14:33.414978Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cursor Management](Introduction%20to%20Cursor%20Management.md)


[Next](Document%20Revision%20History.md)[Previous](About%20Cursors.md)

# Setting the Current Cursor

An application may use several cursor instances—for example, one that looks like an arrow and one that looks like an I-beam. The instance that currently appears on the screen is called the “current cursor,” and is referenced by the `currentCursor` class method. You can set the current cursor in several ways:

- You can send a set message to the cursor.
- You can manage cursors in a stack, using the `push` and `pop` methods of `NSCursor`. The stack’s top cursor is the current cursor.
- You can tell a cursor to become current when the mouse enters a region in a view known as the cursor rectangle. The `NSView` class provides methods to support using cursor rectangles to change the cursor image. For more information, see _[Cocoa Event Handling Guide](../Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_.
- You can tell a cursor to set itself when the mouse exits a view’s cursor rectangle.

The cursor rectangle is a region inside an `NSView` that triggers a change in the current cursor. To create a cursor rectangle, use the `addCursorRect:cursor:` method of `NSView` to associate a region of the view with the cursor, as shown in the example that follows. To make the association persistent, you can call `addCursorRect:cursor:` from within an override of `resetCursorRects` method of `NSView`, as described in _[Cocoa Event Handling Guide](../Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_.

```
[aView addCursorRect:aRect cursor:aCursor];
[aCursor setOnMouseEntered:YES];
```

This assignment means that when the mouse enters _aRect_, _aCursor_ receives a `mouseEntered:` event message, which the cursor uses to make itself the current cursor. However, before the cursor can acknowledge the `mouseEntered:` message, you must invoke the cursor’s `setOnMouseEntered:` method. Alternatively, you can set the cursor when the mouse leaves the cursor rectangle by invoking the `setOnMouseExited:` method instead of `setOnMouseEntered:`. A cursor that sets itself upon leaving the cursor rectangle receives a `mouseExited:` event message to instigate the change.

The Application Kit provides two ready-made cursors for commonly used cursor images. You can retrieve these cursors by using the `arrowCursor` and `IBeamCursor` class methods. There is no `NSCursor` instance for the wait cursor, because the system automatically displays it at the appropriate times.

[Next](Document%20Revision%20History.md)[Previous](About%20Cursors.md)

