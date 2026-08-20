---
title: What is the correct drawing model and the correct event model for my NPAPI
  plug-in?
apple_id: DTS40011304
resource_type: QA
platform: Safari|macOS
topic: General
technology: WebKit
published: '2011-09-30'
source_url: https://developer.apple.com/library/archive/qa/qa1755/_index.html
archived_at: '2026-07-18T02:34:35.742079Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1755

# What is the correct drawing model and the correct event model for my NPAPI plug-in?

## Q:  What is the correct drawing model and the correct event model for my NPAPI plug-in?

A: NPAPI plug-ins now support the Core Graphics and Core Animation drawing models. If your plug-in does very little drawing or a small amount of simple drawing, you should use the Core Graphics drawing model. If your plug-in plays video or does complex drawing (including 3D graphics), then you should use the Core Animation drawing model.

As of Safari 4, the QuickDraw drawing model is no longer supported. 64-bit NPAPI plug-ins will use the Core Graphics drawing model by default, when no drawing model is explicitly specified. 32-bit NPAPI plug-ins will use QuickDraw by default, when no drawing model is explicitly specified. If a plug-in selects the QuickDraw drawing model — either explicitly, or by default when no drawing model is specified — then the plug-in is immediately destroyed. This means that your 32-bit NPAPI plug-in must explicitly select the Core Graphics or Core Animation drawing model in order to load and function in Safari 4 and later.

The Cocoa event model is also supported as of Safari 4. Since the semantics of the Cocoa event model closely match Cocoa NSEvents, using this event model lets you write code that is cleaner and more modern than code which uses the legacy Carbon event model. The Cocoa event model is compatible with both 32-bit and 64-bit plug-ins, and is the recommended event model for NPAPI plug-ins in Safari.

Listing 1 shows how to enable the Core Graphics drawing model and Cocoa event model.

__Listing 1__  Enabling the Core Graphics drawing model and Cocoa event model.

```swift
/* Ask the browser if it supports the CoreGraphics drawing model */
NPBool supportsCoreGraphics;
if (browser->getvalue(instance, NPNVsupportsCoreGraphicsBool, &supportsCoreGraphics) != NPERR_NO_ERROR)
    supportsCoreGraphics = FALSE;

if (!supportsCoreGraphics)
    return NPERR_INCOMPATIBLE_VERSION_ERROR;

/* If the browser supports the CoreGraphics drawing model, enable it. */
browser->setvalue(instance, NPPVpluginDrawingModel, (void *)NPDrawingModelCoreGraphics);

/* Ask the browser if it supports the Cocoa event model */
NPBool supportsCocoa;
if (browser->getvalue(instance, NPNVsupportsCocoaBool, &supportsCocoa) != NPERR_NO_ERROR)
    supportsCocoa = FALSE;

if (!supportsCocoa)
    return NPERR_INCOMPATIBLE_VERSION_ERROR;

/* If the browser supports the Cocoa event model, enable it. */
browser->setvalue(instance, NPPVpluginEventModel, (void *)NPEventModelCocoa);
```

Plug-ins that use the Core Animation drawing model must use the Cocoa event model. Listing 2 shows how to enable the Core Animation drawing model and the Cocoa event model, when these are available.

__Listing 2__  Enabling the Core Animation drawing model and Cocoa event model.

```swift
/* Ask the browser if it supports the Core Animation drawing model */
NPBool supportsCoreAnimation;
if (browser->getvalue(instance, NPNVsupportsCoreAnimationBool, &supportsCoreAnimation) != NPERR_NO_ERROR)
    supportsCoreAnimation = FALSE;

if (!supportsCoreAnimation)
    return NPERR_INCOMPATIBLE_VERSION_ERROR;

/* If the browser supports the Core Animation drawing model, enable it. */
browser->setvalue(instance, NPPVpluginDrawingModel, (void *)NPDrawingModelCoreAnimation);

/* Ask the browser if it supports the Cocoa event model */
NPBool supportsCocoa;
if (browser->getvalue(instance, NPNVsupportsCocoaBool, &supportsCocoa) != NPERR_NO_ERROR)
    supportsCocoa = FALSE;

if (!supportsCocoa)
    return NPERR_INCOMPATIBLE_VERSION_ERROR;

/* If the browser supports the Cocoa event model, enable it. */
browser->setvalue(instance, NPPVpluginEventModel, (void *)NPEventModelCocoa);
```

For more information on drawing models, see the the [Core Graphics Drawing model specification](https://wiki.mozilla.org/NPAPI:CoreGraphicsDrawing) and the [Core Animation Drawing model specification](https://wiki.mozilla.org/NPAPI:CoreAnimationDrawingModel).

For more information on Cocoa events, see the [Cocoa Event model specification](https://wiki.mozilla.org/NPAPI:CocoaEventModel).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-09-30 | New document that gives guidelines and describes default behavior for drawing and event models in NPAPI plug-ins. |

