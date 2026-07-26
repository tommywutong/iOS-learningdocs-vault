---
title: 'setURL(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicspdfrenderercontext/seturl(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/seturl(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicspdfrenderercontext/seturl%28_%3Afor%3A%29.json'
content_hash: 'sha256:72cb6590e0fd8b17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsPDFRendererContext](../uigraphicspdfrenderercontext.md)

# setURL(_:for:)

<sub>Instance Method</sub>

Creates a link to an external resource defined by a URL

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setURL(_ url: URL, for rect: CGRect)
```

## Parameters

- `url` — The external URL that the user is directed to on clicking the link.

- `rect` — The region of the current page that becomes the active link area, specified in points in the PDF coordinate space.

## Discussion

Use this method to create links to external resources in the current page of a PDF. The URL is interpreted by the PDF viewer.

> [!note] Note
> Specify the `rect` value in the PDF coordinate space, not the Core Graphics context coordinate space. This means that the origin is in the bottom-left rather than the top-left, and the y-axis increases in an upwards direction. Use the [userSpaceToDeviceSpaceTransform](../../coregraphics/cgcontext/userspacetodevicespacetransform.md) property on [CGContext](../../coregraphics/cgcontext.md) to map between the two.

To create internal links within the current PDF document, use [- addDestinationWithName:atPoint:](<adddestination(withname_at_).md>) and [- setDestinationWithName:forRect:](<setdestinationwithname(__for_).md>).

## See Also

### Managing destinations

- [- addDestinationWithName:atPoint:](<adddestination(withname_at_).md>) — Creates a named destination point in the current PDF page.
- [- setDestinationWithName:forRect:](<setdestinationwithname(__for_).md>) — Creates a link rectangle in the current page that jumps the PDF viewer to the named destination when clicked.
