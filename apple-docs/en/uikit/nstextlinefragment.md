---
title: NSTextLineFragment
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlinefragment
source_url: 'https://developer.apple.com/documentation/uikit/nstextlinefragment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlinefragment.json'
content_hash: 'sha256:6cdce1e29f43f60a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextLineFragment

<sub>Class</sub>

A class that represents a line fragment as a single textual layout and rendering unit inside a text layout fragment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class NSTextLineFragment
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating line fragments

- [- initWithAttributedString:range:](<nstextlinefragment/init(attributedstring_range_).md>) — Creates a new line fragment from the attributed string for the range of characters you specify.
- [- initWithCoder:](<nstextlinefragment/init(coder_).md>) — Creates a new line fragment with from data in an unarchiver.
- [- initWithString:attributes:range:](<nstextlinefragment/init(string_attributes_range_).md>) — Creates a new line fragment using the string, attributes, and range you provide.

### Line fragment characteristics

- [attributedString](nstextlinefragment/attributedstring.md) — The source attributed string.
- [characterRange](nstextlinefragment/characterrange.md) — The string range for the source attributed string that corresponds to this line fragment.
- [glyphOrigin](nstextlinefragment/glyphorigin.md) — Rendering origin for the left-most glyph in the line fragment coordinate system.
- [typographicBounds](nstextlinefragment/typographicbounds.md) — The typographic bounds that specifies the dimensions of the line fragment for laying out line fragments to each other.

### Finding specific text

- [- characterIndexForPoint:](<nstextlinefragment/characterindex(for_).md>) — Returns character index for a point inside the line fragment coordinate system.
- [- fractionOfDistanceThroughGlyphForPoint:](<nstextlinefragment/fractionofdistancethroughglyph(for_).md>) — Returns character index for a point inside the line fragment coordinate system.
- [- locationForCharacterAtIndex:](<nstextlinefragment/locationforcharacter(at_).md>) — Returns the location of the character at the specified index.

### Drawing

- [- drawAtPoint:inContext:](<nstextlinefragment/draw(at_in_).md>) — Renders the line fragment contents at the rendering origin.

## See Also

### Layout

- [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md) — Interact with text by managing text selection and inserting custom text elements.
- [Display text with a custom layout](display-text-with-a-custom-layout.md) — Lay out text in a custom-shaped container and apply glyph substitutions.
- [Managing viewport layout and attachment reuse in text views](managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md) — Customize layout and preserve attachment views in your text view subclass.
- [NSTextLayoutManager](nstextlayoutmanager.md) — The primary class that you use to manage text layout and presentation for custom text displays.
- [NSTextContainer](nstextcontainer.md) — A region where text layout occurs.
- [NSTextLayoutFragment](nstextlayoutfragment.md) — A class that represents the layout fragment typically corresponding to a rendering surface, such as a layer or view subclass.
- [NSTextViewportLayoutController](nstextviewportlayoutcontroller.md) — Manages the layout process inside the viewport interacting with its delegate.
- [NSTextViewportRenderingSurface](nstextviewportrenderingsurface.md) — A protocol that identifies a view or layer as a drawable element for a text layout fragment. _(beta)_
- [NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md) — A protocol that lets you use an object to identify a rendering surface when storing or retrieving it.
- [NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md) — A set of methods that define the orientation of text for an object.
