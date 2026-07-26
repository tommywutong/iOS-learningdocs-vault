---
title: title
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nshostingscenebridgingoptions/title
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingscenebridgingoptions/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingscenebridgingoptions/title.json'
content_hash: 'sha256:9313917e0136877f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingSceneBridgingOptions](../nshostingscenebridgingoptions.md)

# title

<sub>Type Property</sub>

The hosting view’s associated window will have its title and subtitle populated with the values provided to the `navigationTitle(_:)` and `navigationSubtitle(_:)` modifiers, respectively.

<sub>macOS</sub>

```swift
static let title: NSHostingSceneBridgingOptions
```

## Discussion

Title bars populated in this manner overwrite any values set using AppKit.

## See Also

### Geting bridging options

- [all](all.md) — The hosting view’s associated window will have both its title bars and toolbars populated with values from their respective modifiers.
- [toolbars](toolbars.md) — The hosting view’s associated window will have its toolbar populated with any items provided to the `toolbar(content:)` modifier.
