---
title: Using TextKit 2 to interact with text
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, Xcode 14.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/using-textkit-2-to-interact-with-text
source_url: 'https://developer.apple.com/documentation/uikit/using-textkit-2-to-interact-with-text'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/using-textkit-2-to-interact-with-text.json'
content_hash: 'sha256:379b4b12f79ae5f1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [TextKit](textkit.md)

# Using TextKit 2 to interact with text

<sub>Sample Code</sub>

Interact with text by managing text selection and inserting custom text elements.

## Overview

> [!note] Note
> This sample code project is associated with WWDC21 session [10061: Meet TextKit 2](https://developer.apple.com/wwdc21/10061/).

## See Also

### Layout

- [Display text with a custom layout](display-text-with-a-custom-layout.md) — Lay out text in a custom-shaped container and apply glyph substitutions.
- [Managing viewport layout and attachment reuse in text views](managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md) — Customize layout and preserve attachment views in your text view subclass.
- [NSTextLayoutManager](nstextlayoutmanager.md) — The primary class that you use to manage text layout and presentation for custom text displays.
- [NSTextContainer](nstextcontainer.md) — A region where text layout occurs.
- [NSTextLayoutFragment](nstextlayoutfragment.md) — A class that represents the layout fragment typically corresponding to a rendering surface, such as a layer or view subclass.
- [NSTextLineFragment](nstextlinefragment.md) — A class that represents a line fragment as a single textual layout and rendering unit inside a text layout fragment.
- [NSTextViewportLayoutController](nstextviewportlayoutcontroller.md) — Manages the layout process inside the viewport interacting with its delegate.
- [NSTextViewportRenderingSurface](nstextviewportrenderingsurface.md) — A protocol that identifies a view or layer as a drawable element for a text layout fragment. _(beta)_
- [NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md) — A protocol that lets you use an object to identify a rendering surface when storing or retrieving it.
- [NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md) — A set of methods that define the orientation of text for an object.

## Download

- [UsingTextKit2ToInteractWithText.zip](https://docs-assets.developer.apple.com/published/806998142c63/UsingTextKit2ToInteractWithText.zip)
