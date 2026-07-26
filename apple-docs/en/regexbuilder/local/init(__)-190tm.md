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
doc_path: '/documentation/regexbuilder/local/init(_:)-190tm'
source_url: 'https://developer.apple.com/documentation/regexbuilder/local/init(_:)-190tm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/local/init%28_%3A%29-190tm.json'
content_hash: 'sha256:3ee0620a3c2df1f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Local](../local.md)

# init(_:)

<sub>Initializer</sub>

Creates an atomic group with the given regex component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ component: some RegexComponent) where Output == Substring
```

## Parameters

- `component` — The regex component to wrap in an atomic group.
