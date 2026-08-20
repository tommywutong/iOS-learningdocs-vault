---
title: Managing custom drawing code in a compositing world
apple_id: DTS10003438
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2004-10-14'
source_url: https://developer.apple.com/library/archive/qa/qa1162/_index.html
archived_at: '2026-07-18T02:30:11.735487Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1162

# Managing custom drawing code in a compositing world

## Q:  In order to switch to HIViews, I have to make my windows compositing. But now, parts of my windows stop updating. What's happening? And how can I fix it?

A: In order to switch to HIViews, I have to make my windows compositing. But now, parts of my windows stop updating. What's happening? And how can I fix it?

Compositing windows are delegating all the content drawing to the `HIView` hierarchy so you will have to move your window update code into a view drawing architecture.

In a non-compositing window, content would be redrawn by the `UpdateControls` or `DrawControls` (or an iteration of `Draw1Control`) API and your own drawing code. Depending on the age of your application, that drawing code would be written using QuickDraw or Quartz, and would be called from either your `updateEvt` handling in a `WaitNextEvent` architecture (WNE), or from your `kEventWindowDrawContent` handler (or your `kEventWindowUpdate` handler in some special cases) in a Carbon Event architecture (CE).

For custom windows, your drawing code might be called from your handling of the `kWindowMsgDraw` message (classic) or your `kEventWindowPaint` handler (modern).

Wherever your drawing code may be, it will not be called anymore when the window is compositing because compositing window do not have a "content" anymore. What they have is a Content View (`kHIViewWindowContentID`) which embeds all children views. When a window is being drawn, the HIToolbox only draws its frame, and its title bar and widgets if required. Then the HIToolbox sends a `kEventControlDraw` event to the window's Content View which will be propagated to its children in the correct Z-order to take full advantage of the compositing model.

Since all controls are also HIViews, when you make your windows compositing, only the controls are being redrawn and all additional drawing is missing.

The simplest and best way to get your "Drawing Code" back is to create a custom `HIView` which only has to handle the `kEventControlDraw` event: you simply move all your "Drawing Code" to the `kEventControlDraw` handler, and you add this custom view, as first view, to the Content View of your window.

Additionally, if your window can be resized, install a handler to listen to the `kEventControlBoundsChanged` event of your view's parent view which is the Content View and, in this handler, just change your view's bounds and invalidate it with `HIViewSetNeedsDisplay` to force a redraw.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-10-14 | New document that explains why any custom drawing code must be handled by the kEventControlDraw handler of a custom HIView |

