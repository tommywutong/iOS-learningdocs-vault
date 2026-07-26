---
title: 'init(as:_:)'
framework: RegexBuilder
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/regexbuilder/capture/init(as:_:)-3d6el'
source_url: 'https://developer.apple.com/documentation/regexbuilder/capture/init(as:_:)-3d6el'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/capture/init%28as%3A_%3A%29-3d6el.json'
content_hash: 'sha256:20c4098820b91b2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Capture](../capture.md)

# init(as:_:)

<sub>Initializer</sub>

Creates a capture for the given component using the specified reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<W, C1, C2, C3, C4, C5, C6, C7, C8>(as reference: Reference<W>, @RegexComponentBuilder _ componentBuilder: () -> some RegexComponent) where Output == (Substring, W, C1, C2, C3, C4, C5, C6, C7, C8)
```

## Parameters

- `reference` — The reference to use for anything captured by `component`.

- `componentBuilder` — A builder closure that generates a regex component to capture.
