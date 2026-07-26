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
doc_path: '/documentation/foundation/objectivecconvertibleattributedstringkey/objectivecvalue(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/objectivecconvertibleattributedstringkey/objectivecvalue(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/objectivecconvertibleattributedstringkey/objectivecvalue%28for%3A%29.json'
content_hash: 'sha256:b95828bfb5e43f0c'
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

## Default Implementations

### ObjectiveCConvertibleAttributedStringKey Implementations

- [objectiveCValue(for:)](<objectivecvalue(for_)-7whjv.md>) — Returns an Objective-C typed value for a given value of this key’s type.
- [objectiveCValue(for:)](<objectivecvalue(for_)-97cif.md>) — Returns an Objective-C typed value for a given value of this key’s type.

## See Also

### Converting between Swift and Objective-C Types

- [value(for:)](<value(for_).md>) — Returns a value of this key’s type for a given Objective-C value.
