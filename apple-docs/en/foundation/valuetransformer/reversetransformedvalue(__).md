---
title: 'reverseTransformedValue(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/valuetransformer/reversetransformedvalue(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/valuetransformer/reversetransformedvalue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/valuetransformer/reversetransformedvalue%28_%3A%29.json'
content_hash: 'sha256:0590af371353dc0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ValueTransformer](../valuetransformer.md)

# reverseTransformedValue(_:)

<sub>Instance Method</sub>

Returns the result of the reverse transformation of a given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func reverseTransformedValue(_ value: Any?) -> Any?
```

## Parameters

- `value` — The value to reverse transform.

## Return Value

The reverse transformation of `value`.

## Discussion

The default implementation raises an exception if [+ allowsReverseTransformation](<allowsreversetransformation().md>) returns [false](../../swift/false.md); otherwise it will invoke [- transformedValue:](<transformedvalue(__).md>) with `value`.

A subclass should override this method if they require a reverse transformation that is not the same as simply reapplying the original transform (as would be the case with negation, for example). For example, if a value transformer converts a value in Fahrenheit to Celsius, this method would converts a value from Celsius to Fahrenheit.

## See Also

### Transforming Values

- [- transformedValue:](<transformedvalue(__).md>) — Returns the result of transforming a given value.
