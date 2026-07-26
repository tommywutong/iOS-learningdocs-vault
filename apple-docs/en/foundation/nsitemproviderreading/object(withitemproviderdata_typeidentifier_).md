---
title: 'object(withItemProviderData:typeIdentifier:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemproviderreading/object(withitemproviderdata:typeidentifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemproviderreading/object(withitemproviderdata:typeidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemproviderreading/object%28withitemproviderdata%3Atypeidentifier%3A%29.json'
content_hash: 'sha256:2b61a57b3a85ba7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProviderReading](../nsitemproviderreading.md)

# object(withItemProviderData:typeIdentifier:)

<sub>Type Method</sub>

Creates a new instance of a class using the given data and UTI string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func object(withItemProviderData data: Data, typeIdentifier: String) throws -> Self
```

## Parameters

- `data` — The data used to create the object.

- `typeIdentifier` — The uniform type identifier (UTI) representing the data type of `data`.

## Return Value

An object created from the given data.
