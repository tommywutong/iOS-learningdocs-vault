---
title: 'transformedValue(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/valuetransformer/transformedvalue(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/valuetransformer/transformedvalue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/valuetransformer/transformedvalue%28_%3A%29.json'
content_hash: 'sha256:d6fbecbb03b4e9af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ValueTransformer](../valuetransformer.md)

# transformedValue(_:)

<sub>Instance Method</sub>

Returns the result of transforming a given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func transformedValue(_ value: Any?) -> Any?
```

## Parameters

- `value` — The value to transform.

## Return Value

The result of transforming `value`.

The default implementation simply returns `value`.

## Discussion

A subclass should override this method to transform and return an object based on `value`.

## See Also

### Transforming Values

- [- reverseTransformedValue:](<reversetransformedvalue(__).md>) — Returns the result of the reverse transformation of a given value.
