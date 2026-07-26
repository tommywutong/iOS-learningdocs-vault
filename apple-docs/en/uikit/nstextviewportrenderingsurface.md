---
title: NSTextViewportRenderingSurface
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/nstextviewportrenderingsurface
source_url: 'https://developer.apple.com/documentation/uikit/nstextviewportrenderingsurface'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextviewportrenderingsurface.json'
content_hash: 'sha256:c6ac9a031283807c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextViewportRenderingSurface

<sub>Protocol</sub>

A protocol that identifies a view or layer as a drawable element for a text layout fragment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
protocol NSTextViewportRenderingSurface : NSObjectProtocol
```

## Overview

Conform a view or layer to `NSTextViewportRenderingSurface` to associate it with an [NSTextLayoutFragment](nstextlayoutfragment.md) during viewport layout. TextKit uses this to track, configure, and reuse visual elements across layout passes.

This protocol has no required methods. It gives TextKit a way to identify and manage the visual elements your delegate provides through [NSTextViewportLayoutControllerDelegate](nstextviewportlayoutcontrollerdelegate.md).

### Implement a rendering surface

You can conform any `UIView`, `NSView`, or `CALayer` subclass to this protocol:

```swift
class TextFragmentView: UIView, NSTextViewportRenderingSurface {
    var layoutFragment: NSTextLayoutFragment?
}
```

Return instances from [- textViewportLayoutController:configureRenderingSurfaceForTextLayoutFragment:](<nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(__configurerenderingsurfacefor_).md>) so TextKit can manage them during layout.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

### Layout

- [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md) — Interact with text by managing text selection and inserting custom text elements.
- [Display text with a custom layout](display-text-with-a-custom-layout.md) — Lay out text in a custom-shaped container and apply glyph substitutions.
- [Managing viewport layout and attachment reuse in text views](managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md) — Customize layout and preserve attachment views in your text view subclass.
- [NSTextLayoutManager](nstextlayoutmanager.md) — The primary class that you use to manage text layout and presentation for custom text displays.
- [NSTextContainer](nstextcontainer.md) — A region where text layout occurs.
- [NSTextLayoutFragment](nstextlayoutfragment.md) — A class that represents the layout fragment typically corresponding to a rendering surface, such as a layer or view subclass.
- [NSTextLineFragment](nstextlinefragment.md) — A class that represents a line fragment as a single textual layout and rendering unit inside a text layout fragment.
- [NSTextViewportLayoutController](nstextviewportlayoutcontroller.md) — Manages the layout process inside the viewport interacting with its delegate.
- [NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md) — A protocol that lets you use an object to identify a rendering surface when storing or retrieving it.
- [NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md) — A set of methods that define the orientation of text for an object.
