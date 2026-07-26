---
title: all
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nshostingscenebridgingoptions/all
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingscenebridgingoptions/all'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingscenebridgingoptions/all.json'
content_hash: 'sha256:b71a9588082ab7aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingSceneBridgingOptions](../nshostingscenebridgingoptions.md)

# all

<sub>Type Property</sub>

The hosting view’s associated window will have both its title bars and toolbars populated with values from their respective modifiers.

<sub>macOS</sub>

```swift
static let all: NSHostingSceneBridgingOptions
```

## See Also

### Geting bridging options

- [title](title.md) — The hosting view’s associated window will have its title and subtitle populated with the values provided to the `navigationTitle(_:)` and `navigationSubtitle(_:)` modifiers, respectively.
- [toolbars](toolbars.md) — The hosting view’s associated window will have its toolbar populated with any items provided to the `toolbar(content:)` modifier.
