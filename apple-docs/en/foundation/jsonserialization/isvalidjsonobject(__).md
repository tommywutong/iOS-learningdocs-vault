---
title: 'isValidJSONObject(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/jsonserialization/isvalidjsonobject(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/jsonserialization/isvalidjsonobject(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonserialization/isvalidjsonobject%28_%3A%29.json'
content_hash: 'sha256:292fec5e942ce29a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONSerialization](../jsonserialization.md)

# isValidJSONObject(_:)

<sub>Type Method</sub>

Returns a Boolean value that indicates whether the serializer can convert a given object to JSON data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func isValidJSONObject(_ obj: Any) -> Bool
```

## Parameters

- `obj` — The object to test.

## Return Value

`true` if `obj` can be converted to JSON data; otherwise, `false`.

## See Also

### Creating JSON Data

- [+ dataWithJSONObject:options:error:](<data(withjsonobject_options_).md>) — Returns JSON data from a Foundation object.
- [+ writeJSONObject:toStream:options:error:](<writejsonobject(__to_options_error_).md>) — Writes a given JSON object to a stream.
- [WritingOptions](writingoptions.md) — Options for writing JSON data.
