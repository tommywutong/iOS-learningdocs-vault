---
title: supportedContentTypes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowseraction/supportedcontenttypes
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowseraction/supportedcontenttypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowseraction/supportedcontenttypes.json'
content_hash: 'sha256:e501e5f779eae665'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserAction](../uidocumentbrowseraction.md)

# supportedContentTypes

<sub>Instance Property</sub>

An array of uniform type identifiers that define the types of documents that the action supports.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var supportedContentTypes: [String] { get set }
```

## Discussion

The action can be triggered only on documents that are allowed by both the action’s [supportedContentTypes](supportedcontenttypes.md) property and the document browser’s [allowedContentTypes](../uidocumentbrowserviewcontroller/allowedcontenttypes.md) property.

By default, this property contains only the `public.item` uniform type identifier (UTI)—indicating that there are no additional restrictions on document types.

To further restrict the supported documents, assign an array that contains a more restricted set of UTIs. These UTIs should define a subset of the UTIs supported by the document browser.

For more about UTIs, see [Uniform Type Identifiers Reference](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/UTIRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009257).

## See Also

### Creating and configuring actions

- [- initWithIdentifier:localizedTitle:availability:handler:](<init(identifier_localizedtitle_availability_handler_).md>) — Instantiates and returns a new browser action item.
- [image](image.md) — The action’s image displayed in the navigation bar.
- [supportsMultipleItems](supportsmultipleitems.md) — A Boolean value that determines whether the action can be triggered on more than one document at a time.
