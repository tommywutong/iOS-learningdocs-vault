---
title: 'isValid(within:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/range/isvalid(within:)-2fba2'
source_url: 'https://developer.apple.com/documentation/swift/range/isvalid(within:)-2fba2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/isvalid%28within%3A%29-2fba2.json'
content_hash: 'sha256:02139a05c735bc00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

# isValid(within:)

<sub>Instance Method</sub>

Indicates whether the range is valid for use with the provided attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isValid(within text: some AttributedStringProtocol) -> Bool
```

## Parameters

- `text` — An attributed string used to validate the range.

## Return Value

`true` when the range is valid for use with the provided attributed string; otherwise, false. A range is valid if its lower and upper bounds are each either valid in the attributed string or equivalent to the string’s `endIndex`.
