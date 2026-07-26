---
title: 'objectiveCValue(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/objectivecconvertibleattributedstringkey/objectivecvalue(for:)-97cif'
source_url: 'https://developer.apple.com/documentation/foundation/objectivecconvertibleattributedstringkey/objectivecvalue(for:)-97cif'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/objectivecconvertibleattributedstringkey/objectivecvalue%28for%3A%29-97cif.json'
content_hash: 'sha256:6130ff91a14766b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ObjectiveCConvertibleAttributedStringKey](../objectivecconvertibleattributedstringkey.md)

# objectiveCValue(for:)

<sub>Type Method</sub>

Returns an Objective-C typed value for a given value of this key’s type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func objectiveCValue(for value: Self.Value) throws -> Self.ObjectiveCValue
```

## Parameters

- `value` — The value to convert.

## Return Value

`value`, expressed as the Objective-C type defined by [ObjectiveCValue](objectivecvalue.md).
