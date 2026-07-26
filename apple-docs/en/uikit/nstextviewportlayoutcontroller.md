---
title: NSTextViewportLayoutController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextviewportlayoutcontroller
source_url: 'https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextviewportlayoutcontroller.json'
content_hash: 'sha256:c5004f799b14b324'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextViewportLayoutController

<sub>Class</sub>

Manages the layout process inside the viewport interacting with its delegate.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class NSTextViewportLayoutController
```

## Overview

A viewport is a rectangular area within a flipped coordinate system expanding along the y-axis. With text contents, lines advance expanding the view in the current writing direction. The viewport defines the active area where the framework lays out text fragments. In most cases, the area corresponds to the user visible area with an additional over-scroll region.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a viewport layout controller

- [- initWithTextLayoutManager:](<nstextviewportlayoutcontroller/init(textlayoutmanager_).md>) — Creates a new instance with the text layout manager you provide.

### Accessing the layout manager

- [textLayoutManager](nstextviewportlayoutcontroller/textlayoutmanager.md) — Returns the text layout manager for this viewport layout controller.

### Responding to changes in viewport layout

- [delegate](nstextviewportlayoutcontroller/delegate.md) — The delegate for the text layout manager object.
- [NSTextViewportLayoutControllerDelegate](nstextviewportlayoutcontrollerdelegate.md) — Optional methods that delegates implement to respond to viewport layout changes.

### Accessing the viewport characteristics

- [viewportBounds](nstextviewportlayoutcontroller/viewportbounds.md) — Returns the visible bounds of the view, plus the overdraw area.
- [viewportRange](nstextviewportlayoutcontroller/viewportrange.md) — Returns the text range of the current viewport layout.
- [- adjustViewportByVerticalOffset:](<nstextviewportlayoutcontroller/adjustviewport(byverticaloffset_).md>) — Adjusts the viewport rect by the specified offset if needed.
- [- layoutViewport](<nstextviewportlayoutcontroller/layoutviewport().md>) — Performs layout in the viewport.
- [- relocateViewportToTextLocation:](<nstextviewportlayoutcontroller/relocateviewport(to_).md>) — Relocates the viewport to the location you specify.

## See Also

### Layout

- [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md) — Interact with text by managing text selection and inserting custom text elements.
- [Display text with a custom layout](display-text-with-a-custom-layout.md) — Lay out text in a custom-shaped container and apply glyph substitutions.
- [Managing viewport layout and attachment reuse in text views](managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md) — Customize layout and preserve attachment views in your text view subclass.
- [NSTextLayoutManager](nstextlayoutmanager.md) — The primary class that you use to manage text layout and presentation for custom text displays.
- [NSTextContainer](nstextcontainer.md) — A region where text layout occurs.
- [NSTextLayoutFragment](nstextlayoutfragment.md) — A class that represents the layout fragment typically corresponding to a rendering surface, such as a layer or view subclass.
- [NSTextLineFragment](nstextlinefragment.md) — A class that represents a line fragment as a single textual layout and rendering unit inside a text layout fragment.
- [NSTextViewportRenderingSurface](nstextviewportrenderingsurface.md) — A protocol that identifies a view or layer as a drawable element for a text layout fragment. _(beta)_
- [NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md) — A protocol that lets you use an object to identify a rendering surface when storing or retrieving it.
- [NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md) — A set of methods that define the orientation of text for an object.
