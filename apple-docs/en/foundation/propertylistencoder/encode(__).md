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
doc_path: '/documentation/foundation/propertylistencoder/encode(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/propertylistencoder/encode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistencoder/encode%28_%3A%29.json'
content_hash: 'sha256:8889683a933ad61b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PropertyListEncoder](../propertylistencoder.md)

# encode(_:)

<sub>Instance Method</sub>

Returns a property list that represents an encoded version of the value you supply.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode<Value>(_ value: Value) throws -> Data where Value : Encodable
```

## Parameters

- `value` — The value to encode as a property list.

## Discussion

If there’s a problem encoding the value you supply, this method throws an error based on the type of problem:

- The value fails to encode, or contains a nested value that fails to encode—this method throws the corresponding error.
- The value can’t be encoded as a property list—this method throws the [EncodingError.invalidValue(_:_:)](<../../swift/encodingerror/invalidvalue(____).md>) error.

## See Also

### Encoding

- [init()](<init().md>) — Creates a new, reusable property list encoder with the default formatting settings.
- [encode(_:configuration:)](<encode(__configuration_)-4biuh.md>)
- [encode(_:configuration:)](<encode(__configuration_)-5ee8q.md>)
