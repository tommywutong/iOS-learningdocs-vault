---
title: 'init(_:as:)'
framework: RegexBuilder
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/regexbuilder/capture/init(_:as:)-82c2j'
source_url: 'https://developer.apple.com/documentation/regexbuilder/capture/init(_:as:)-82c2j'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/capture/init%28_%3Aas%3A%29-82c2j.json'
content_hash: 'sha256:45dcc4e1ea69961c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Capture](../capture.md)

# init(_:as:)

<sub>Initializer</sub>

Creates a capture for the given component using the specified reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<W>(_ component: some RegexComponent, as reference: Reference<W>) where Output == (Substring, W)
```

## Parameters

- `component` — The regex component to capture.

- `reference` — The reference to use for anything captured by `component`.
