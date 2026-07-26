---
title: toolbars
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nshostingscenebridgingoptions/toolbars
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingscenebridgingoptions/toolbars'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingscenebridgingoptions/toolbars.json'
content_hash: 'sha256:c330359e68f04fa8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingSceneBridgingOptions](../nshostingscenebridgingoptions.md)

# toolbars

<sub>Type Property</sub>

The hosting view’s associated window will have its toolbar populated with any items provided to the `toolbar(content:)` modifier.

<sub>macOS</sub>

```swift
static let toolbars: NSHostingSceneBridgingOptions
```

## Discussion

Toolbars populated in this manner overwrite any toolbar set on the window using AppKit.

## See Also

### Geting bridging options

- [all](all.md) — The hosting view’s associated window will have both its title bars and toolbars populated with values from their respective modifiers.
- [title](title.md) — The hosting view’s associated window will have its title and subtitle populated with the values provided to the `navigationTitle(_:)` and `navigationSubtitle(_:)` modifiers, respectively.
