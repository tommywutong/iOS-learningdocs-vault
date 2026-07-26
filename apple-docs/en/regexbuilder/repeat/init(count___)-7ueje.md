---
title: 'init(count:_:)'
framework: RegexBuilder
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/regexbuilder/repeat/init(count:_:)-7ueje'
source_url: 'https://developer.apple.com/documentation/regexbuilder/repeat/init(count:_:)-7ueje'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/repeat/init%28count%3A_%3A%29-7ueje.json'
content_hash: 'sha256:61b67c1fcc2f1093'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Repeat](../repeat.md)

# init(count:_:)

<sub>Initializer</sub>

Creates a regex component that matches the given component repeated the specified number of times.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<W, C1, C2, C3, C4, C5, C6, C7>(count: Int, @RegexComponentBuilder _ componentBuilder: () -> some RegexComponent) where Output == (Substring, C1?, C2?, C3?, C4?, C5?, C6?, C7?)
```

## Parameters

- `count` — The number of times to repeat `component`. `count` must be greater than or equal to zero.

- `componentBuilder` — A builder closure that creates the regex component to repeat.
