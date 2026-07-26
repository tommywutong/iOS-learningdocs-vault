---
title: 'addAcceptableTypeIdentifiers(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteconfiguration/addacceptabletypeidentifiers(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteconfiguration/addacceptabletypeidentifiers(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteconfiguration/addacceptabletypeidentifiers%28_%3A%29.json'
content_hash: 'sha256:c96986026baf405b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteConfiguration](../uipasteconfiguration.md)

# addAcceptableTypeIdentifiers(_:)

<sub>Instance Method</sub>

Adds an array of UTI strings to a paste configuration, increasing the variety of types the paste configuration accepts.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func addAcceptableTypeIdentifiers(_ acceptableTypeIdentifiers: [String])
```

## Parameters

- `acceptableTypeIdentifiers` — An array of uniform type identifier (UTI) strings.

## Discussion

List the acceptable UTIs in descending order of fidelity. The UTI that provides the richest data representation should be first in the list. For instance, if the data to paste is contact information, list the vCard UTI first, followed by the plain text UTI.

## See Also

### Adding acceptable type identifiers

- [- addTypeIdentifiersForAcceptingClass:](<addtypeidentifiers(foraccepting_)-4fvd6.md>) — Expands the array of accepted UTIs for a paste configuration, based on those declared as supported by a specified class.
- [addTypeIdentifiers(forAccepting:)](<addtypeidentifiers(foraccepting_)-8af7o.md>)
