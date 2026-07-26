---
title: 'attachmentBounds(for:location:textContainer:proposedLineFragment:position:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextattachmentviewprovider/attachmentbounds(for:location:textcontainer:proposedlinefragment:position:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachmentviewprovider/attachmentbounds(for:location:textcontainer:proposedlinefragment:position:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachmentviewprovider/attachmentbounds%28for%3Alocation%3Atextcontainer%3Aproposedlinefragment%3Aposition%3A%29.json'
content_hash: 'sha256:901a049ab131a682'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachmentViewProvider](../nstextattachmentviewprovider.md)

# attachmentBounds(for:location:textContainer:proposedLineFragment:position:)

<sub>Instance Method</sub>

Returns the layout bounds for an attachment at a specific text location that contains the text attributes you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func attachmentBounds(for attributes: [NSAttributedString.Key : Any], location: any NSTextLocation, textContainer: NSTextContainer?, proposedLineFragment: CGRect, position: CGPoint) -> CGRect
```

## Parameters

- `attributes` — A dictionary that contains a list of key and attribute pairs that describe the customization of the string.

- `location` — An [NSTextLocation](../nstextlocation.md) that indicates that start of the string.

- `textContainer` — The [NSTextContainer](../nstextcontainer.md) that contains the source string.

- `proposedLineFragment` — A [CGRect](../../corefoundation/cgrect.md) that describes the boundaries of the line fragment.

- `position` — A [CGPoint](../../corefoundation/cgpoint.md) inside `proposedLineFragment`.

## Return Value

Returns a [CGRect](../../corefoundation/cgrect.md) that describes the bounds of the attachment.
