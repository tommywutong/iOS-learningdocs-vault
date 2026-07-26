---
title: 'encode(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/jsonencoder/encode(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/jsonencoder/encode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonencoder/encode%28_%3A%29.json'
content_hash: 'sha256:db9b29b922c0ec6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONEncoder](../jsonencoder.md)

# encode(_:)

<sub>Instance Method</sub>

Returns a JSON-encoded representation of the value you supply.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode<T>(_ value: T) throws -> Data where T : Encodable
```

## Parameters

- `value` — The value to encode as JSON.

## Return Value

The encoded JSON data.

## Discussion

If there’s a problem encoding the value you supply, this method throws an error based on the type of problem:

- The value fails to encode, or contains a nested value that fails to encode—this method throws the corresponding error.
- The value isn’t encodable as a JSON array or JSON object—this method throws the [EncodingError.invalidValue(_:_:)](<../../swift/encodingerror/invalidvalue(____).md>) error.
- The value contains an exceptional floating-point number (such as [infinity](../../swift/floatingpoint/infinity.md) or [nan](../../swift/floatingpoint/nan.md)) and you’re using the default [NonConformingFloatEncodingStrategy](nonconformingfloatencodingstrategy-swift.enum.md) — this method throws the [EncodingError.invalidValue(_:_:)](<../../swift/encodingerror/invalidvalue(____).md>) error.

## See Also

### First Steps

- [init()](<init().md>) — Creates a new, reusable JSON encoder with the default formatting settings and encoding strategies.
