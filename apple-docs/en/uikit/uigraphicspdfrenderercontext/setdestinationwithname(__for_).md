---
title: 'setDestinationWithName(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicspdfrenderercontext/setdestinationwithname(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/setdestinationwithname(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicspdfrenderercontext/setdestinationwithname%28_%3Afor%3A%29.json'
content_hash: 'sha256:2bda05a98836de0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsPDFRendererContext](../uigraphicspdfrenderercontext.md)

# setDestinationWithName(_:for:)

<sub>Instance Method</sub>

Creates a link rectangle in the current page that jumps the PDF viewer to the named destination when clicked.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setDestinationWithName(_ name: String, for rect: CGRect)
```

## Parameters

- `name` — The name of the destination point to which the PDF viewer jumps.

- `rect` — The region on the current page that becomes the active link area, specified in points in the PDF coordinate space.

## Discussion

Use this method in conjunction with the [- addDestinationWithName:atPoint:](<adddestination(withname_at_).md>) method to create internal links within a PDF. This method represents the creation of the links that, when clicked, jump the user to a named destination, created using the [- addDestinationWithName:atPoint:](<adddestination(withname_at_).md>) method.

> [!note] Note
> Specify the `rect` value in the PDF coordinate space, not the Core Graphics coordinate space. This means the origin is in the bottom-left corner of the context rather than the top-left, and the y-axis increases in an upwards direction. Use the [userSpaceToDeviceSpaceTransform](../../coregraphics/cgcontext/userspacetodevicespacetransform.md) property on [CGContext](../../coregraphics/cgcontext.md) to map between the two.

For an example of how to use internal links, including mapping between coordinate spaces, see  [Creating internal links](../uigraphicspdfrenderer.md#Creating-internal-links) in [UIGraphicsPDFRenderer](../uigraphicspdfrenderer.md).

## See Also

### Managing destinations

- [- addDestinationWithName:atPoint:](<adddestination(withname_at_).md>) — Creates a named destination point in the current PDF page.
- [- setURL:forRect:](<seturl(__for_).md>) — Creates a link to an external resource defined by a URL
