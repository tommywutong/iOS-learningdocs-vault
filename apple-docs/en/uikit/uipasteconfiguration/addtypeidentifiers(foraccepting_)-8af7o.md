---
title: 'addTypeIdentifiers(forAccepting:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteconfiguration/addtypeidentifiers(foraccepting:)-8af7o'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteconfiguration/addtypeidentifiers(foraccepting:)-8af7o'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteconfiguration/addtypeidentifiers%28foraccepting%3A%29-8af7o.json'
content_hash: 'sha256:0e798451ed384f4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteConfiguration](../uipasteconfiguration.md)

# addTypeIdentifiers(forAccepting:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency func addTypeIdentifiers<T>(forAccepting aClass: T.Type) where T : _ObjectiveCBridgeable, T._ObjectiveCType : NSItemProviderReading
```

## See Also

### Adding acceptable type identifiers

- [- addAcceptableTypeIdentifiers:](<addacceptabletypeidentifiers(__).md>) — Adds an array of UTI strings to a paste configuration, increasing the variety of types the paste configuration accepts.
- [- addTypeIdentifiersForAcceptingClass:](<addtypeidentifiers(foraccepting_)-4fvd6.md>) — Expands the array of accepted UTIs for a paste configuration, based on those declared as supported by a specified class.
