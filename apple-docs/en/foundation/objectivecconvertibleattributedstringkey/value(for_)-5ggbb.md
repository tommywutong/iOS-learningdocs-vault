---
title: 'value(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/objectivecconvertibleattributedstringkey/value(for:)-5ggbb'
source_url: 'https://developer.apple.com/documentation/foundation/objectivecconvertibleattributedstringkey/value(for:)-5ggbb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/objectivecconvertibleattributedstringkey/value%28for%3A%29-5ggbb.json'
content_hash: 'sha256:7adbe4217eee435f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ObjectiveCConvertibleAttributedStringKey](../objectivecconvertibleattributedstringkey.md)

# value(for:)

<sub>Type Method</sub>

Returns a value of this key’s type for a given Objective-C value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func value(for object: Self.ObjectiveCValue) throws -> Self.Value
```

## Parameters

- `object` — The Objective-C value to convert.

## Return Value

`object`, expressed as this key’s type.
