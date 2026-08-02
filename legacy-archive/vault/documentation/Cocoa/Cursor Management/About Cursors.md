---
title: Cursor Management
apple_id: 10000066i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CursorMgmt/Concepts/AboutCursors.html
archived_at: '2026-07-15T07:14:32.415616Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cursor Management](Introduction%20to%20Cursor%20Management.md)


[Next](Setting%20the%20Current%20Cursor.md)[Previous](Introduction%20to%20Cursor%20Management.md)

# About Cursors

Instances of the `NSCursor` class manage the appearance of the cursor. When you initialize a cursor—the designated initializer is `initWithImage:hotSpot:`—you assign it an `NSImage` object and a point to be the hot spot. The image is usually a small, opaque icon—for example, a pair of cross-hairs—surrounded by transparent pixels. The pixels in the cursor image are mapped on a flipped coordinate system with the upper left pixel being (0,0).

To determine exactly when the mouse is inside a particular cursor rectangle, the Application Kit tracks a single pixel in the cursor image. This pixel is known as the hot spot, and you can reference it using the `hotSpot` method. By definition, the location of the current cursor’s hot spot is the location of the mouse; when the hot spot is inside a cursor rectangle, so is the mouse. The hot spot is useful not only for determining which cursor is current, but for determining where a mouse click should have its effect.

An `NSCursor` object is immutable: you cannot change its hot spot or image after it’s created. Instead, use `initWithImage:hotSpot:` to create a new one with the new settings.

[Next](Setting%20the%20Current%20Cursor.md)[Previous](Introduction%20to%20Cursor%20Management.md)

