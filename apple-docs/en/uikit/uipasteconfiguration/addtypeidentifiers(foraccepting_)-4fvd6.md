---
title: 'addTypeIdentifiers(forAccepting:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteconfiguration/addtypeidentifiers(foraccepting:)-4fvd6'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteconfiguration/addtypeidentifiers(foraccepting:)-4fvd6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteconfiguration/addtypeidentifiers%28foraccepting%3A%29-4fvd6.json'
content_hash: 'sha256:1c8f3df5ff40af4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteConfiguration](../uipasteconfiguration.md)

# addTypeIdentifiers(forAccepting:)

<sub>Instance Method</sub>

Expands the array of accepted UTIs for a paste configuration, based on those declared as supported by a specified class.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func addTypeIdentifiers(forAccepting aClass: any NSItemProviderReading.Type)
```

## Parameters

- `aClass` — A class conforming to the [NSItemProviderReading](../../foundation/nsitemproviderreading.md) protocol.

## Discussion

This method uses the property [readableTypeIdentifiersForItemProvider](../../foundation/nsitemproviderreading/readabletypeidentifiersforitemprovider.md), implemented on `aClass`, to determine the uniform type identifiers (UTIs) to add to the paste configuration’s [acceptableTypeIdentifiers](acceptabletypeidentifiers.md) array.

## See Also

### Adding acceptable type identifiers

- [- addAcceptableTypeIdentifiers:](<addacceptabletypeidentifiers(__).md>) — Adds an array of UTI strings to a paste configuration, increasing the variety of types the paste configuration accepts.
- [addTypeIdentifiers(forAccepting:)](<addtypeidentifiers(foraccepting_)-8af7o.md>)
