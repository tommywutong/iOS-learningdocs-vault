---
title: 'init(_:count:)'
framework: RegexBuilder
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/regexbuilder/repeat/init(_:count:)-82evl'
source_url: 'https://developer.apple.com/documentation/regexbuilder/repeat/init(_:count:)-82evl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/repeat/init%28_%3Acount%3A%29-82evl.json'
content_hash: 'sha256:3c30a28d184db46c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Repeat](../repeat.md)

# init(_:count:)

<sub>Initializer</sub>

Creates a regex component that matches the given component repeated the specified number of times.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ component: some RegexComponent, count: Int) where Output == Substring
```

## Parameters

- `component` — The regex component to repeat.

- `count` — The number of times to repeat `component`. `count` must be greater than or equal to zero.
