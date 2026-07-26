---
title: 'addDestination(withName:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicspdfrenderercontext/adddestination(withname:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/adddestination(withname:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicspdfrenderercontext/adddestination%28withname%3Aat%3A%29.json'
content_hash: 'sha256:47e14022aed3381a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsPDFRendererContext](../uigraphicspdfrenderercontext.md)

# addDestination(withName:at:)

<sub>Instance Method</sub>

Creates a named destination point in the current PDF page.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addDestination(withName name: String, at point: CGPoint)
```

## Parameters

- `name` — The name of the destination, used as a reference by the [- setDestinationWithName:forRect:](<setdestinationwithname(__for_).md>) method.

- `point` — The location of the destination point, in the PDF coordinate space.

## Discussion

Use this method in conjunction with the [- setDestinationWithName:forRect:](<setdestinationwithname(__for_).md>) method to create internal links within a PDF. This method represents the creation of the points to which the PDF viewer will jump when a user clicks a link.

> [!note] Note
> Specify the `point` value in the PDF coordinate space, not the Core Graphics context coordinate space. This means that the origin is in the bottom-left corner of the context rather than the top-left, and the y-axis increases in an upwards direction. Use the [userSpaceToDeviceSpaceTransform](../../coregraphics/cgcontext/userspacetodevicespacetransform.md) property on [CGContext](../../coregraphics/cgcontext.md) to map between the two.

For an example of how to use internal links, including mapping between coordinate spaces, see  [Creating internal links](../uigraphicspdfrenderer.md#Creating-internal-links) in [UIGraphicsPDFRenderer](../uigraphicspdfrenderer.md).

## See Also

### Managing destinations

- [- setDestinationWithName:forRect:](<setdestinationwithname(__for_).md>) — Creates a link rectangle in the current page that jumps the PDF viewer to the named destination when clicked.
- [- setURL:forRect:](<seturl(__for_).md>) — Creates a link to an external resource defined by a URL
