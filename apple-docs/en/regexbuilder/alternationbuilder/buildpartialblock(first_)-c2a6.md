---
title: 'buildPartialBlock(first:)'
framework: RegexBuilder
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/regexbuilder/alternationbuilder/buildpartialblock(first:)-c2a6'
source_url: 'https://developer.apple.com/documentation/regexbuilder/alternationbuilder/buildpartialblock(first:)-c2a6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/alternationbuilder/buildpartialblock%28first%3A%29-c2a6.json'
content_hash: 'sha256:daf79630c4bbd030'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [AlternationBuilder](../alternationbuilder.md)

# buildPartialBlock(first:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildPartialBlock<R, W, C1, C2, C3>(first regex: R) -> ChoiceOf<(W, C1?, C2?, C3?)> where R : RegexComponent, R.RegexOutput == (W, C1, C2, C3)
```
