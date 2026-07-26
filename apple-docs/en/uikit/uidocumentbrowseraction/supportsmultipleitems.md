---
title: supportsMultipleItems
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowseraction/supportsmultipleitems
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowseraction/supportsmultipleitems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowseraction/supportsmultipleitems.json'
content_hash: 'sha256:21d37f6b4ca3d577'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserAction](../uidocumentbrowseraction.md)

# supportsMultipleItems

<sub>Instance Property</sub>

A Boolean value that determines whether the action can be triggered on more than one document at a time.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var supportsMultipleItems: Bool { get set }
```

## Discussion

This property defaults to [true](../../swift/true.md).

## See Also

### Creating and configuring actions

- [- initWithIdentifier:localizedTitle:availability:handler:](<init(identifier_localizedtitle_availability_handler_).md>) — Instantiates and returns a new browser action item.
- [image](image.md) — The action’s image displayed in the navigation bar.
- [supportedContentTypes](supportedcontenttypes.md) — An array of uniform type identifiers that define the types of documents that the action supports.
