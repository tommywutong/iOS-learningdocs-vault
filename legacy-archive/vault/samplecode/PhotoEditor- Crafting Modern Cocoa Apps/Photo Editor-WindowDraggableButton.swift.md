---
title: 'PhotoEditor: Crafting Modern Cocoa Apps'
apple_id: TP40017384
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoEditor/Listings/Photo_Editor_WindowDraggableButton_swift.html
archived_at: '2026-07-18T03:18:49.830185Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoEditor: Crafting Modern Cocoa Apps](PhotoEditor-%20Crafting%20Modern%20Cocoa%20Apps.md)


[Next](Photo%20Editor-CanvasView.swift.md)[Previous](Photo%20Editor-CanvasScrollView.swift.md)

# Photo Editor/WindowDraggableButton.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 WindowDraggableButton is an NSButton subclass that allows the button to behave like a normal button when clicked, but begins a system drag when the user clicks and drags a certain distance inside the button.
 */

import Cocoa

class WindowDraggableButton: NSButton {

    // Allow the window to still be dragged from this button
    override func mouseDown(with mouseDownEvent: NSEvent) {
        let window = self.window!
        let startingPoint = mouseDownEvent.locationInWindow

        highlight(true)

        // Track events until the mouse is up (in which we interpret as a click), or a drag starts (in which we pass off to the Window Server to perform the drag)
        var shouldCallSuper = false

        // trackEvents won't return until after the tracking all ends
        window.trackEvents(matching: [.leftMouseDragged, .leftMouseUp], timeout:NSEventDurationForever, mode: .defaultRunLoopMode) { event, stop in
            switch event.type {
                case .leftMouseUp:
                    // Stop on a mouse up; post it back into the queue and call super so it can handle it
                    shouldCallSuper = true
                    NSApp.postEvent(event, atStart: false)
                    stop.pointee = true

                case .leftMouseDragged:
                    // track mouse drags, and if more than a few points are moved we start a drag
                    let currentPoint = event.locationInWindow
                    if (fabs(currentPoint.x - startingPoint.x) >= 5 || fabs(currentPoint.y - startingPoint.y) >= 5) {
                        self.highlight(false)
                        stop.pointee = true
                        window.performDrag(with: event)
                    }

                default:
                    break
            }
        }

        if (shouldCallSuper) {
            super.mouseDown(with: mouseDownEvent)
        }
    }

}
```

[Next](Photo%20Editor-CanvasView.swift.md)[Previous](Photo%20Editor-CanvasScrollView.swift.md)

