---
title: readableTypeIdentifiersForItemProvider
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemproviderreading/readabletypeidentifiersforitemprovider
source_url: 'https://developer.apple.com/documentation/foundation/nsitemproviderreading/readabletypeidentifiersforitemprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemproviderreading/readabletypeidentifiersforitemprovider.json'
content_hash: 'sha256:f16ffe4ff24b075f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProviderReading](../nsitemproviderreading.md)

# readableTypeIdentifiersForItemProvider

<sub>Type Property</sub>

An array of UTI strings representing the data types supported by the class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var readableTypeIdentifiersForItemProvider: [String] { get }
```

## Discussion

Provide uniform type identifiers (UTIs) in order from highest fidelity to lowest. If your app employs a native data representation, place that first in the array.
