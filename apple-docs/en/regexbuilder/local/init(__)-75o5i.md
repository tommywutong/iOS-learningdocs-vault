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
doc_path: '/documentation/regexbuilder/local/init(_:)-75o5i'
source_url: 'https://developer.apple.com/documentation/regexbuilder/local/init(_:)-75o5i'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/local/init%28_%3A%29-75o5i.json'
content_hash: 'sha256:d32c8c5b1d64940b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Local](../local.md)

# init(_:)

<sub>Initializer</sub>

Creates an atomic group with the given regex component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(@RegexComponentBuilder _ componentBuilder: () -> some RegexComponent) where Output == Substring
```

## Parameters

- `componentBuilder` — A builder closure that generates a regex component to wrap in an atomic group.
