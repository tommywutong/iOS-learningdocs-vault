---
title: NSTextLayoutOrientationProvider
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutorientationprovider
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutorientationprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutorientationprovider.json'
content_hash: 'sha256:7515419a5a78a590'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextLayoutOrientationProvider

<sub>Protocol</sub>

A set of methods that define the orientation of text for an object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol NSTextLayoutOrientationProvider
```

## Overview

In macOS, the [NSTextContainer](nstextcontainer.md) and [NSTextView](../appkit/nstextview.md) classes adopt this protocol; in iOS, only the [NSTextContainer](nstextcontainer.md) class implements it. An [NSTextContainer](nstextcontainer.md) object returns the value from its associated text view when present; otherwise, it returns [NSTextLayoutOrientationHorizontal](nslayoutmanager/textlayoutorientation/horizontal.md) by default. If you define a custom [NSTextContainer](nstextcontainer.md) object, you can override this method and return [NSTextLayoutOrientationVertical](nslayoutmanager/textlayoutorientation/vertical.md) to support laying out text vertically.

## Relationships

- **Conforming Types**: [NSTextContainer](nstextcontainer.md)

## Topics

### Getting layout orientation

- [layoutOrientation](nstextlayoutorientationprovider/layoutorientation.md) — The default layout orientation.
- [TextLayoutOrientation](nslayoutmanager/textlayoutorientation.md) — Constants that describe the text layout orientation.

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
- [NSTextViewportRenderingSurface](nstextviewportrenderingsurface.md) — A protocol that identifies a view or layer as a drawable element for a text layout fragment. _(beta)_
- [NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md) — A protocol that lets you use an object to identify a rendering surface when storing or retrieving it.
