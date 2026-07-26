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
doc_path: '/documentation/regexbuilder/lookahead/init(_:)-4s5w2'
source_url: 'https://developer.apple.com/documentation/regexbuilder/lookahead/init(_:)-4s5w2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/lookahead/init%28_%3A%29-4s5w2.json'
content_hash: 'sha256:6a7e00f5eaebfccd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Lookahead](../lookahead.md)

# init(_:)

<sub>Initializer</sub>

Creates a lookahead from the given regex component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<R>(_ component: R) where Output == R.RegexOutput, R : RegexComponent
```
