---
title: NSTextAttachmentContainer
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextattachmentcontainer
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachmentcontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachmentcontainer.json'
content_hash: 'sha256:44afb7a07d95ebbb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextAttachmentContainer

<sub>Protocol</sub>

A set of methods that defines the interface to text attachment objects from a layout manager.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol NSTextAttachmentContainer : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [NSTextAttachment](nstextattachment.md)

## Topics

### Getting the bounds

- [- attachmentBoundsForTextContainer:proposedLineFragment:glyphPosition:characterIndex:](<nstextattachmentcontainer/attachmentbounds(for_proposedlinefragment_glyphposition_characterindex_).md>) — Returns the layout bounds of the text attachment to the layout manager.

### Getting the image

- [- imageForBounds:textContainer:characterIndex:](<nstextattachmentcontainer/image(forbounds_textcontainer_characterindex_).md>) — Returns the image object that the layout manager renders in the specified image bounds rectangle inside the text container.

## See Also

### Attachments

- [NSTextAttachment](nstextattachment.md) — The values for the attachment characteristics of attributed strings and related objects.
- [NSTextAttachmentViewProvider](nstextattachmentviewprovider.md) — A container object that associates a text attachment at a particular document location with a view object.
- [NSAdaptiveImageGlyph](nsadaptiveimageglyph.md) — A data object for an emoji-like image that can appear in attributed text.
- [NSTextAttachmentLayout](nstextattachmentlayout.md) — A set of methods that defines the interface to attachment objects from a text layout manager.
