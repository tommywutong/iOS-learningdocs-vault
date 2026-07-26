---
title: 'image(for:attributes:location:textContainer:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextattachmentlayout/image(for:attributes:location:textcontainer:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachmentlayout/image(for:attributes:location:textcontainer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachmentlayout/image%28for%3Aattributes%3Alocation%3Atextcontainer%3A%29.json'
content_hash: 'sha256:4b9043770f214b6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachmentLayout](../nstextattachmentlayout.md)

# image(for:attributes:location:textContainer:)

<sub>Instance Method</sub>

Returns the image object rendered at the bounds and inside the text container you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func image(for bounds: CGRect, attributes: [NSAttributedString.Key : Any] = [:], location: any NSTextLocation, textContainer: NSTextContainer?) -> UIImage?
```

## Parameters

- `bounds` — The [CGRect](../../corefoundation/cgrect.md) that presents the image boundaries inside `textContainer`.

- `attributes` — A dictionary of [NSAttributedString.Key](../../foundation/nsattributedstring/key.md) attributes.

- `location` — An [NSTextLocation](../nstextlocation.md) that indicates that start of the string.

- `textContainer` — The [NSTextContainer](../nstextcontainer.md) that contains the source text.

## Return Value

An optional image object.

## Discussion

A custom implementation should return an image appropriate for the target rendering context that you derive by arguments to this method. The default [NSTextAttachment](../nstextattachment.md) implementation returns the contents of the `image` property when non-`nil`. If the `image` property is `nil`, it returns an image based on the `contents` and `fileType` properties.

## See Also

### Determining the characteristics of an attachment

- [- attachmentBoundsForAttributes:location:textContainer:proposedLineFragment:position:](<attachmentbounds(for_location_textcontainer_proposedlinefragment_position_).md>) — Returns the layout bounds of the attachment you specify.
- [- viewProviderForParentView:location:textContainer:](<viewprovider(for_location_textcontainer_).md>) — Returns the text attachment view provider corresponding to the file type.
