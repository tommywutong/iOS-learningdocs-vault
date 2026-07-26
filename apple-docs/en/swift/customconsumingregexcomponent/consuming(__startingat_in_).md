---
title: 'consuming(_:startingAt:in:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/customconsumingregexcomponent/consuming(_:startingat:in:)'
source_url: 'https://developer.apple.com/documentation/swift/customconsumingregexcomponent/consuming(_:startingat:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/customconsumingregexcomponent/consuming%28_%3Astartingat%3Ain%3A%29.json'
content_hash: 'sha256:92695b281c825d9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CustomConsumingRegexComponent](../customconsumingregexcomponent.md)

# consuming(_:startingAt:in:)

<sub>Instance Method</sub>

Process the input string within the specified bounds, beginning at the given index, and return the end position (upper bound) of the match and the produced output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func consuming(_ input: String, startingAt index: String.Index, in bounds: Range<String.Index>) throws -> (upperBound: String.Index, output: Self.RegexOutput)?
```

## Parameters

- `input` — The string in which the match is performed.

- `index` — An index of `input` at which to begin matching.

- `bounds` — The bounds in `input` in which the match is performed.

## Return Value

The upper bound where the match terminates and a matched instance, or `nil` if there isn’t a match.
