---
title: 'buildPartialBlock(accumulated:next:)'
framework: RegexBuilder
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/regexbuilder/alternationbuilder/buildpartialblock(accumulated:next:)-2q3in'
source_url: 'https://developer.apple.com/documentation/regexbuilder/alternationbuilder/buildpartialblock(accumulated:next:)-2q3in'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/alternationbuilder/buildpartialblock%28accumulated%3Anext%3A%29-2q3in.json'
content_hash: 'sha256:02a0b05b8faf9c9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [AlternationBuilder](../alternationbuilder.md)

# buildPartialBlock(accumulated:next:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildPartialBlock<W1, C1, C2, C3, C4, C5>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1?, C2?, C3?, C4?, C5?)>
```
