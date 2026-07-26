---
title: 'anchorsMatchLineEndings(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regex/anchorsmatchlineendings(_:)'
source_url: 'https://developer.apple.com/documentation/swift/regex/anchorsmatchlineendings(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex/anchorsmatchlineendings%28_%3A%29.json'
content_hash: 'sha256:d85aa24c48e23a75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Regex](../regex.md)

# anchorsMatchLineEndings(_:)

<sub>Instance Method</sub>

Returns a regular expression where the start and end of input anchors (`^` and `$`) also match against the start and end of a line.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func anchorsMatchLineEndings(_ matchLineEndings: Bool = true) -> Regex<Regex<Output>.RegexOutput>
```

## Parameters

- `matchLineEndings` — A Boolean value indicating whether `^` and `$` should match the start and end of lines, respectively.

## Return Value

The modified regular expression.

## Discussion

This method corresponds to applying the `m` option in regex syntax. For this behavior in the `RegexBuilder` syntax, see `Anchor.startOfLine`, `Anchor.endOfLine`, `Anchor.startOfSubject`, and `Anchor.endOfSubject`.
