---
title: NSTextAttachmentViewProvider
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextattachmentviewprovider
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachmentviewprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachmentviewprovider.json'
content_hash: 'sha256:fadcf4e639b638bb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextAttachmentViewProvider

<sub>Class</sub>

A container object that associates a text attachment at a particular document location with a view object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class NSTextAttachmentViewProvider
```

## Overview

Use `NSTextAttachmentViewProvider` when you need to represent document locations in terms of an [NSTextLocation](nstextlocation.md) or an [NSTextRange](nstextrange.md) or you want to support view-based text attachments. The view provider controls the view placement and layout without requiring view classes to be aware of the text attachment coordination using a [NSTextLayoutManager](nstextlayoutmanager.md) in macOS 12 or iOS 15 and later.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a text attachment view

- [- initWithTextAttachment:parentView:textLayoutManager:location:](<nstextattachmentviewprovider/init(textattachment_parentview_textlayoutmanager_location_).md>) — Creates a new text attachment view whose content starts at the location you provide.

### Defining the contents

- [location](nstextattachmentviewprovider/location.md) — The location that indicates the start of the text attachment.
- [textAttachment](nstextattachmentviewprovider/textattachment.md) — The text attachment for this view.
- [textLayoutManager](nstextattachmentviewprovider/textlayoutmanager.md) — The text layout manager for this view.
- [tracksTextAttachmentViewBounds](nstextattachmentviewprovider/trackstextattachmentviewbounds.md) — A Boolean value that determines the text attachment’s bounds policy.
- [view](nstextattachmentviewprovider/view.md) — The text attachment’s view.

### Defining a custom view hierarchy

- [- loadView](<nstextattachmentviewprovider/loadview().md>) — Draws the custom view hierarchy that text attachment view subclasses implement.

### Determining the Attachment’s Bounds

- [- attachmentBoundsForAttributes:location:textContainer:proposedLineFragment:position:](<nstextattachmentviewprovider/attachmentbounds(for_location_textcontainer_proposedlinefragment_position_).md>) — Returns the layout bounds for an attachment at a specific text location that contains the text attributes you specify.

## See Also

### Attachments

- [NSTextAttachment](nstextattachment.md) — The values for the attachment characteristics of attributed strings and related objects.
- [NSAdaptiveImageGlyph](nsadaptiveimageglyph.md) — A data object for an emoji-like image that can appear in attributed text.
- [NSTextAttachmentContainer](nstextattachmentcontainer.md) — A set of methods that defines the interface to text attachment objects from a layout manager.
- [NSTextAttachmentLayout](nstextattachmentlayout.md) — A set of methods that defines the interface to attachment objects from a text layout manager.
