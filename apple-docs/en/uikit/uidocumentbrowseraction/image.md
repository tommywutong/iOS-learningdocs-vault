---
title: image
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowseraction/image
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowseraction/image'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowseraction/image.json'
content_hash: 'sha256:3f7beb5cb194a421'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserAction](../uidocumentbrowseraction.md)

# image

<sub>Instance Property</sub>

The action’s image displayed in the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var image: UIImage? { get set }
```

## Discussion

This property is used only when the action is displayed in the navigation bar. By default, it is set to `nil`, and the navigation bar displays the value of the action’s [localizedTitle](localizedtitle.md) property.

If set, the navigation bar derives a bar button image from this image. Only the alpha values in the source image are used to create the bar button image—opaque values are ignored.

If this image is too large, it is scaled to fit. Typically, navigation bar images are 20 x 20 points.

## See Also

### Creating and configuring actions

- [- initWithIdentifier:localizedTitle:availability:handler:](<init(identifier_localizedtitle_availability_handler_).md>) — Instantiates and returns a new browser action item.
- [supportedContentTypes](supportedcontenttypes.md) — An array of uniform type identifiers that define the types of documents that the action supports.
- [supportsMultipleItems](supportsmultipleitems.md) — A Boolean value that determines whether the action can be triggered on more than one document at a time.
