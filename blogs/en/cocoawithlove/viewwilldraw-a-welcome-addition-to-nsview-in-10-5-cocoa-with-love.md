---
title: 'viewWillDraw - a welcome addition to NSView in 10.5 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/04/viewwilldraw-welcome-addition-to-nsview.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:5b6f0c83e4dd7524'
translated: false
---

> 原文：[viewWillDraw - a welcome addition to NSView in 10.5 | Cocoa with Love](https://www.cocoawithlove.com/2008/04/viewwilldraw-welcome-addition-to-nsview.html)　·　Cocoa with Love (Matt Gallagher)

A method named viewWillDraw appeared in NSView in Mac OS X 10.5. If you have cause to use it, this method replaces 6 other methods from earlier versions of Mac OS X. Read more to find out if you should use it and how it helps.

## Drawing in NSView

Drawing in Cocoa happens in the NSView method drawRect:. Almost all programs perform some form of custom drawing, so this is one of the most commonly overridden methods in Cocoa.

The general procedure to follow in this method is:

- Determine what needs to be drawn
- For each component that needs to be drawn, draw the component

But what happens if, in the course of determining what needs to be drawn, you need to alter the area being updated? If, after determining what needs to be drawn, we realize that a different region needs to be updated, it's too late — the drawing rectangle can't be changed from inside drawRect:.

## Layout code

The above described problem is exactly what is faced by deferred or pending layout code.

Layout code deferred until drawInRect: is unable to change the bounds for drawing and must a separate drawRect: invocation. This can create pauses in display, tearing or other drawing problems.

Let me be clear here: when I say "layout", I don't mean the arrangement of NSViews in a window (these will handle themselves). "Layout" in this sense means graphical objects within a single view which may need to be arranged in some way (i.e. column alignment, animation or other procedural generation or positioning).

Deferred layout isn't very common (since drawing is normally triggered after layout is performed) but there may be cases where drawing begins while layout updates are still pending and you want to block the current drawRect: invocation until the layout update is complete. If those layout updates alter the bounds of objects being drawn, we'll want the current invocation of -[NSView drawRect:] to update those bounds, to avoid drawing glitches.

## The old solution

The solution to this problem is to perform the layout required for drawing slightly earlier than drawRect: — before the NSView is locked into drawing a fixed rectangle. This gets around the limitation that drawRect: can only update the area it is given.

Previously, this meant performing pending layout in these NSView methods:

- displayIfNeeded
- displayIfNeededIgnoringOpacity
- _recursiveDisplayAllDirtyWithLockFocus:visRect:
- _recursiveDisplayRectIfNeededIgnoringOpacity:isVisibleRect:rectIsVisibleRectForView:topView:
- _recursiveDisplayRectIfNeededIgnoringOpacity:inContext:topView:
- _lightWeightRecursiveDisplayInRect

These are all the immediate predecessor methods to drawRect:. When these methods are invoked, it is early enough to extend the drawing region by invoking setNeedsDisplayInRect: and the new drawing region will get included when drawRect: is invoked.

Unfortunately, only the first two other these methods are documented. The remainder are undocumented and Apple is free to change them without notice — potentially messing up your program. So "the old solution" was not a good solution.

## Conclusion: the Leopard solution

Fortunately, Mac OS X 10.5 gives a much cleaner function to override before drawRect: is invoked &mdash viewWillDraw. This method is the perfect spot to perform deferred or pending layout. You can alter the bounds that need to be updated and this new altered region will be included on the very next update. This means no tearing and no holes in your drawing.
