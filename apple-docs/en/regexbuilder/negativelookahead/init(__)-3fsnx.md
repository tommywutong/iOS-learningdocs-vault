---
title: 'init(_:)'
framework: RegexBuilder
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/regexbuilder/negativelookahead/init(_:)-3fsnx'
source_url: 'https://developer.apple.com/documentation/regexbuilder/negativelookahead/init(_:)-3fsnx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/negativelookahead/init%28_%3A%29-3fsnx.json'
content_hash: 'sha256:f331fca8a5e6deae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [NegativeLookahead](../negativelookahead.md)

# init(_:)

<sub>Initializer</sub>

Creates a negative lookahead from the given regex component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<R>(_ component: R) where Output == R.RegexOutput, R : RegexComponent
```
