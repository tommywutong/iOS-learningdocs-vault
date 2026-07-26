---
title: 'buildEither(first:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontentbuilder/buildeither(first:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontentbuilder/buildeither(first:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontentbuilder/buildeither%28first%3A%29.json'
content_hash: 'sha256:e6269b4d9171eae6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContentBuilder](../chartcontentbuilder.md)

# buildEither(first:)

<sub>Type Method</sub>

Builds a partial result from a condition that’s true.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildEither<T1, T2>(first: T1) -> BuilderConditional<T1, T2> where T1 : ChartContent, T2 : ChartContent
```

## Parameters

- `first` — The content to use if the condition is `true`.

## Discussion

This method provides support for `if` statements with an `else` clause and `switch` statements. It produces optional chart content that is visible when the condition evaluates to `true`.

## See Also

### Building conditionally

- [buildIf(_:)](<buildif(__).md>) — Builds a partial result that’s conditionally present.
- [buildEither(second:)](<buildeither(second_).md>) — Builds a partial result from a condition that’s false.
