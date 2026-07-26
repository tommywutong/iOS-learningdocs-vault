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
doc_path: '/documentation/regexbuilder/regexcomponentbuilder/buildpartialblock(accumulated:next:)-2p8bg'
source_url: 'https://developer.apple.com/documentation/regexbuilder/regexcomponentbuilder/buildpartialblock(accumulated:next:)-2p8bg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/regexcomponentbuilder/buildpartialblock%28accumulated%3Anext%3A%29-2p8bg.json'
content_hash: 'sha256:922e36bd45eb8536'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [RegexComponentBuilder](../regexcomponentbuilder.md)

# buildPartialBlock(accumulated:next:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildPartialBlock<W0, W1, C1, C2>(accumulated: some RegexComponent, next: some RegexComponent) -> Regex<(Substring, C1, C2)>
```
