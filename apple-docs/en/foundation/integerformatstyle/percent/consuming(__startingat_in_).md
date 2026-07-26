---
title: 'consuming(_:startingAt:in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/integerformatstyle/percent/consuming(_:startingat:in:)'
source_url: 'https://developer.apple.com/documentation/foundation/integerformatstyle/percent/consuming(_:startingat:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerformatstyle/percent/consuming%28_%3Astartingat%3Ain%3A%29.json'
content_hash: 'sha256:ba3719007eb363f6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [IntegerFormatStyle](../../integerformatstyle.md) · [Percent](../percent.md)

# consuming(_:startingAt:in:)

<sub>Instance Method</sub>

Process the input string within the specified bounds, beginning at the given index, and return the end position (upper bound) of the match and the produced output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func consuming(_ input: String, startingAt index: String.Index, in bounds: Range<String.Index>) throws -> (upperBound: String.Index, output: Value)?
```

## Parameters

- `input` — An input string to match against.

- `index` — The index within `input` at which to begin searching.

- `bounds` — The bounds within `input` in which to search.

## Return Value

The upper bound where the match terminates and a matched instance, or `nil` if there isn’t a match.
