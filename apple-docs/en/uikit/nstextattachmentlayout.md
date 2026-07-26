---
title: NSTextAttachmentLayout
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextattachmentlayout
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachmentlayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachmentlayout.json'
content_hash: 'sha256:3ea63b9dc4cb6c30'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextAttachmentLayout

<sub>Protocol</sub>

A set of methods that defines the interface to attachment objects from a text layout manager.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
protocol NSTextAttachmentLayout : NSObjectProtocol
```

## Overview

The `NSTextAttachmentLayout` protocol is the interface for working with attachment objects with an [NSTextAttachmentViewProvider](nstextattachmentviewprovider.md) using a [NSTextLayoutManager](nstextlayoutmanager.md) in macOS 12 and iOS 15 and later.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [NSTextAttachment](nstextattachment.md)

## Topics

### Determining the characteristics of an attachment

- [- attachmentBoundsForAttributes:location:textContainer:proposedLineFragment:position:](<nstextattachmentlayout/attachmentbounds(for_location_textcontainer_proposedlinefragment_position_).md>) — Returns the layout bounds of the attachment you specify.
- [- imageForBounds:attributes:location:textContainer:](<nstextattachmentlayout/image(for_attributes_location_textcontainer_).md>) — Returns the image object rendered at the bounds and inside the text container you specify.
- [- viewProviderForParentView:location:textContainer:](<nstextattachmentlayout/viewprovider(for_location_textcontainer_).md>) — Returns the text attachment view provider corresponding to the file type.

## See Also

### Attachments

- [NSTextAttachment](nstextattachment.md) — The values for the attachment characteristics of attributed strings and related objects.
- [NSTextAttachmentViewProvider](nstextattachmentviewprovider.md) — A container object that associates a text attachment at a particular document location with a view object.
- [NSAdaptiveImageGlyph](nsadaptiveimageglyph.md) — A data object for an emoji-like image that can appear in attributed text.
- [NSTextAttachmentContainer](nstextattachmentcontainer.md) — A set of methods that defines the interface to text attachment objects from a layout manager.
