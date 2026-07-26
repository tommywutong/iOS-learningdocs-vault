---
title: 'viewProvider(for:location:textContainer:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextattachmentlayout/viewprovider(for:location:textcontainer:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachmentlayout/viewprovider(for:location:textcontainer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachmentlayout/viewprovider%28for%3Alocation%3Atextcontainer%3A%29.json'
content_hash: 'sha256:3503464b4752e4bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachmentLayout](../nstextattachmentlayout.md)

# viewProvider(for:location:textContainer:)

<sub>Instance Method</sub>

Returns the text attachment view provider corresponding to the file type.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func viewProvider(for parentView: UIView?, location: any NSTextLocation, textContainer: NSTextContainer?) -> NSTextAttachmentViewProvider?
```

## Parameters

- `parentView` — The parent view.

- `location` — An [NSTextLocation](../nstextlocation.md) that indicates that start of the string.

- `textContainer` — The [NSTextContainer](../nstextcontainer.md) that contains the source text.

## Return Value

An [NSTextAttachmentViewProvider](../nstextattachmentviewprovider.md).

## Discussion

The default implementation queries the text attachment view provider class using the [+ textAttachmentViewProviderClassForFileType:](<../nstextattachment/textattachmentviewproviderclass(forfiletype_).md>) method of [NSTextAttachment](../nstextattachment.md). When non-`nil`, it instantiates a view, then, fills properties declared in `NSTextAttachmentViewProvider` if implemented.

## See Also

### Determining the characteristics of an attachment

- [- attachmentBoundsForAttributes:location:textContainer:proposedLineFragment:position:](<attachmentbounds(for_location_textcontainer_proposedlinefragment_position_).md>) — Returns the layout bounds of the attachment you specify.
- [- imageForBounds:attributes:location:textContainer:](<image(for_attributes_location_textcontainer_).md>) — Returns the image object rendered at the bounds and inside the text container you specify.
