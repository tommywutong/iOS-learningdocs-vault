---
title: NSTextLayoutFragment
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutfragment
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutfragment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutfragment.json'
content_hash: 'sha256:dfdecf5e74c592a5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextLayoutFragment

<sub>Class</sub>

A class that represents the layout fragment typically corresponding to a rendering surface, such as a layer or view subclass.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class NSTextLayoutFragment
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md)

## Topics

### Creating a layout fragment

- [- initWithCoder:](<nstextlayoutfragment/init(coder_).md>) — Creates a new layout fragment with the coder you provide.
- [- initWithTextElement:range:](<nstextlayoutfragment/init(textelement_range_).md>) — Create a new layout fragment using the provided text element and range.

### Getting line fragments

- [textLineFragments](nstextlayoutfragment/textlinefragments.md) — An array of text line fragments.
- [EnumerationOptions](nstextlayoutfragment/enumerationoptions.md) — Values that describe options for enumerating text layout fragments.
- [- textLineFragmentForTextLocation:isUpstreamAffinity:](<nstextlayoutfragment/textlinefragment(for_isupstreamaffinity_).md>) — Returns a text line fragment from a specific text location in the document.
- [- textLineFragmentForVerticalOffset:requiresExactMatch:](<nstextlayoutfragment/textlinefragment(forverticaloffset_requiresexactmatch_).md>) — Returns the text line fragment for the vertical offset you provide, or the closest text line fragment beyond the vertical offset.

### Getting element information

- [state](nstextlayoutfragment/state-swift.property.md) — The layout information state.
- [State](nstextlayoutfragment/state-swift.enum.md) — Values that describe the possible layout states.
- [rangeInElement](nstextlayoutfragment/rangeinelement.md) — The range inside the text element relative to the document origin.
- [textElement](nstextlayoutfragment/textelement.md) — The parent text element.

### Accessing the layout manager

- [textLayoutManager](nstextlayoutfragment/textlayoutmanager.md) — The layout manager for this text layout fragment.

### Drawing the fragment and attachments

- [layoutFragmentFrame](nstextlayoutfragment/layoutfragmentframe.md) — The rectangle the framework uses for tiling the layout fragment inside the target layout coordinate system.
- [renderingSurfaceBounds](nstextlayoutfragment/renderingsurfacebounds.md) — The bounds defining the area required for rendering the contents.
- [- drawAtPoint:inContext:](<nstextlayoutfragment/draw(at_in_).md>) — Renders the visual representation of this element in the specified graphics context.
- [- invalidateLayout](<nstextlayoutfragment/invalidatelayout().md>) — Invalidates any layout information associated with the text layout fragment.
- [textAttachmentViewProviders](nstextlayoutfragment/textattachmentviewproviders.md) — The attachment view provider associated with the text layout fragment.
- [- frameForTextAttachmentAtLocation:](<nstextlayoutfragment/framefortextattachment(at_).md>) — Returns the frame in the text layout fragment coordinate system for the attachment at the location you specify.

### Accessing the layout processing queue

- [layoutQueue](nstextlayoutfragment/layoutqueue.md) — The queue on which the framework dispatches layout operations.

### Defining margins and padding

- [bottomMargin](nstextlayoutfragment/bottommargin.md) — The amount of space reserved during paragraph layout between the bottom of the last line in the paragraph and the bottom of the text layout fragment.
- [leadingPadding](nstextlayoutfragment/leadingpadding.md) — The amount of margin space reserved during paragraph layout between the leading edge of the text layout fragment and the start of the lines in the paragraph.
- [topMargin](nstextlayoutfragment/topmargin.md) — The amount of space reserved during paragraph layout between the top of the text layout fragment and the top of the first line in the paragraph.
- [trailingPadding](nstextlayoutfragment/trailingpadding.md) — The amount of margin space reserved during paragraph layout between the end of the lines in the paragraph and the trailing edge of the text layout fragment.

## See Also

### Layout

- [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md) — Interact with text by managing text selection and inserting custom text elements.
- [Display text with a custom layout](display-text-with-a-custom-layout.md) — Lay out text in a custom-shaped container and apply glyph substitutions.
- [Managing viewport layout and attachment reuse in text views](managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md) — Customize layout and preserve attachment views in your text view subclass.
- [NSTextLayoutManager](nstextlayoutmanager.md) — The primary class that you use to manage text layout and presentation for custom text displays.
- [NSTextContainer](nstextcontainer.md) — A region where text layout occurs.
- [NSTextLineFragment](nstextlinefragment.md) — A class that represents a line fragment as a single textual layout and rendering unit inside a text layout fragment.
- [NSTextViewportLayoutController](nstextviewportlayoutcontroller.md) — Manages the layout process inside the viewport interacting with its delegate.
- [NSTextViewportRenderingSurface](nstextviewportrenderingsurface.md) — A protocol that identifies a view or layer as a drawable element for a text layout fragment. _(beta)_
- [NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md) — A protocol that lets you use an object to identify a rendering surface when storing or retrieving it.
- [NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md) — A set of methods that define the orientation of text for an object.
