---
title: 'extractValues(as:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/anyregexoutput/extractvalues(as:)'
source_url: 'https://developer.apple.com/documentation/swift/anyregexoutput/extractvalues(as:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyregexoutput/extractvalues%28as%3A%29.json'
content_hash: 'sha256:92d88b1b1afa27e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyRegexOutput](../anyregexoutput.md)

# extractValues(as:)

<sub>Instance Method</sub>

Returns strongly-typed match output by converting this type-erased output to the specified type, if possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func extractValues<Output>(as outputType: Output.Type = Output.self) -> Output?
```

## Parameters

- `outputType` — The expected output type.

## Return Value

The output, if the underlying value can be converted to `outputType`; otherwise, `nil`.
