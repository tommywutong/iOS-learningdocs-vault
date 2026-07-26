---
title: 'buildIf(_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontentbuilder/buildif(_:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontentbuilder/buildif(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontentbuilder/buildif%28_%3A%29.json'
content_hash: 'sha256:6ffbf611cd5efb2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContentBuilder](../chartcontentbuilder.md)

# buildIf(_:)

<sub>Type Method</sub>

Builds a partial result that’s conditionally present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildIf<T>(_ content: T?) -> T? where T : ChartContent
```

## Parameters

- `content` — The content to use if the condition is `true`.

## Discussion

This method provides support for `if` statements. It produces optional chart content that is visible only when the condition evaluates to `true`.

## See Also

### Building conditionally

- [buildEither(first:)](<buildeither(first_).md>) — Builds a partial result from a condition that’s true.
- [buildEither(second:)](<buildeither(second_).md>) — Builds a partial result from a condition that’s false.
