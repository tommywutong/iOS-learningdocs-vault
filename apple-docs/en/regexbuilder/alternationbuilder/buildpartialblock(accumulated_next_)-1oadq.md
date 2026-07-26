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
doc_path: '/documentation/regexbuilder/alternationbuilder/buildpartialblock(accumulated:next:)-1oadq'
source_url: 'https://developer.apple.com/documentation/regexbuilder/alternationbuilder/buildpartialblock(accumulated:next:)-1oadq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/alternationbuilder/buildpartialblock%28accumulated%3Anext%3A%29-1oadq.json'
content_hash: 'sha256:b83b762039cff501'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [AlternationBuilder](../alternationbuilder.md)

# buildPartialBlock(accumulated:next:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildPartialBlock<W0, C1, W1, C2>(accumulated: some RegexComponent, next: some RegexComponent) -> ChoiceOf<(Substring, C1, C2?)>
```
