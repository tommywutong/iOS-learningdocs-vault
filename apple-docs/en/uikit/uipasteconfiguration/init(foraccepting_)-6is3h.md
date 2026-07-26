---
title: 'init(forAccepting:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteconfiguration/init(foraccepting:)-6is3h'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteconfiguration/init(foraccepting:)-6is3h'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteconfiguration/init%28foraccepting%3A%29-6is3h.json'
content_hash: 'sha256:9be040b8c58d8932'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteConfiguration](../uipasteconfiguration.md)

# init(forAccepting:)

<sub>Initializer</sub>

Initializes a new paste configuration with the UTIs declared as supported by a specified class.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(forAccepting aClass: any NSItemProviderReading.Type)
```

## Parameters

- `aClass` — A class conforming to the [NSItemProviderReading](../../foundation/nsitemproviderreading.md) protocol.

## Return Value

A paste configuration initialized with acceptable uniform type identifiers (UTIs) supported by the specified class.

## Discussion

When you use this initializer, the property [readableTypeIdentifiersForItemProvider](../../foundation/nsitemproviderreading/readabletypeidentifiersforitemprovider.md), implemented on `aClass`, is used to determine the acceptable UTIs.

## See Also

### Initializing a paste configuration

- [- init](<init().md>) — Initializes a new paste configuration.
- [- initWithAcceptableTypeIdentifiers:](<init(acceptabletypeidentifiers_).md>) — Initializes a new paste configuration with a specified array of acceptable UTIs.
- [init(forAccepting:)](<init(foraccepting_)-84r2r.md>)
