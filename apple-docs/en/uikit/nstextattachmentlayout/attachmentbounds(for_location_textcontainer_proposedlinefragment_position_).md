---
title: 'attachmentBounds(for:location:textContainer:proposedLineFragment:position:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextattachmentlayout/attachmentbounds(for:location:textcontainer:proposedlinefragment:position:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachmentlayout/attachmentbounds(for:location:textcontainer:proposedlinefragment:position:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachmentlayout/attachmentbounds%28for%3Alocation%3Atextcontainer%3Aproposedlinefragment%3Aposition%3A%29.json'
content_hash: 'sha256:3bd221bcd7ec4e92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachmentLayout](../nstextattachmentlayout.md)

# attachmentBounds(for:location:textContainer:proposedLineFragment:position:)

<sub>Instance Method</sub>

Returns the layout bounds of the attachment you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func attachmentBounds(for attributes: [NSAttributedString.Key : Any], location: any NSTextLocation, textContainer: NSTextContainer?, proposedLineFragment: CGRect, position: CGPoint) -> CGRect
```

## Parameters

- `attributes` — A dictionary of [NSAttributedString.Key](../../foundation/nsattributedstring/key.md) attributes.

- `location` — An [NSTextLocation](../nstextlocation.md) that indicates that start of the string.

- `textContainer` — The [NSTextContainer](../nstextcontainer.md) that contains the source text.

- `proposedLineFragment` — A [CGRect](../../corefoundation/cgrect.md) that describes the boundaries of the line fragment.

- `position` — A [CGPoint](../../corefoundation/cgpoint.md) inside `proposedLineFragment`.

## Return Value

Returns a [CGRect](../../corefoundation/cgrect.md) that describes the boundaries of the attachment, or `CGRectZero.`

## Discussion

The framework interprets the bounds origin to match `position` inside `proposedLineFragment`. The default [NSTextAttachment](../nstextattachment.md) implementation returns bounds if the value isn’t equivalent to [CGRectZero](../../coregraphics/cgrectzero.md); otherwise, it derives the bounds value from `image.size`. Conforming objects can implement more sophisticated logic for negotiating the frame size based on the available container space and proposed line fragment rectangle.

## See Also

### Determining the characteristics of an attachment

- [- imageForBounds:attributes:location:textContainer:](<image(for_attributes_location_textcontainer_).md>) — Returns the image object rendered at the bounds and inside the text container you specify.
- [- viewProviderForParentView:location:textContainer:](<viewprovider(for_location_textcontainer_).md>) — Returns the text attachment view provider corresponding to the file type.
