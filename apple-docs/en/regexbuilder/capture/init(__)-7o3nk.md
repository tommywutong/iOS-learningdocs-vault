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
doc_path: '/documentation/regexbuilder/capture/init(_:)-7o3nk'
source_url: 'https://developer.apple.com/documentation/regexbuilder/capture/init(_:)-7o3nk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/capture/init%28_%3A%29-7o3nk.json'
content_hash: 'sha256:3b64e664d0669afd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Capture](../capture.md)

# init(_:)

<sub>Initializer</sub>

Creates a capture for the given component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<W, C1, C2, C3, C4, C5, C6>(@RegexComponentBuilder _ componentBuilder: () -> some RegexComponent) where Output == (Substring, W, C1, C2, C3, C4, C5, C6)
```

## Parameters

- `componentBuilder` — A builder closure that generates a regex component to capture.
