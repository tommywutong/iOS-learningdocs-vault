---
title: NSTextViewportRenderingSurfaceKey
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextviewportrenderingsurfacekey
source_url: 'https://developer.apple.com/documentation/uikit/nstextviewportrenderingsurfacekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextviewportrenderingsurfacekey.json'
content_hash: 'sha256:aedd7ecdfde9f648'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextViewportRenderingSurfaceKey

<sub>Protocol</sub>

A protocol that lets you use an object to identify a rendering surface when storing or retrieving it.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
protocol NSTextViewportRenderingSurfaceKey : NSObjectProtocol
```

## Overview

When TextKit lays out text in a viewport, it can ask your delegate to store and retrieve rendering surfaces across layout passes. Objects that conform to `NSTextViewportRenderingSurfaceKey` act as the identifier for each surface — TextKit passes them to your delegate when it needs to store or look one up.

Two types conform to this protocol by default:

- **`NSTextLayoutFragment`** — Use a layout fragment as a key to cache a rendering surface per fragment. This is the most common approach.
- **`NSString`** — Use a string as a key when you want to associate a rendering surface with a name rather than a fragment.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [NSTextLayoutFragment](nstextlayoutfragment.md)

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
- [NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md) — A set of methods that define the orientation of text for an object.
