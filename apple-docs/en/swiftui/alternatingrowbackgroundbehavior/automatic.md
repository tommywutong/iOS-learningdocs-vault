---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/alternatingrowbackgroundbehavior/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/alternatingrowbackgroundbehavior/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/alternatingrowbackgroundbehavior/automatic.json'
content_hash: 'sha256:805db16c52141de2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AlternatingRowBackgroundBehavior](../alternatingrowbackgroundbehavior.md)

# automatic

<sub>Type Property</sub>

The automatic alternating row background behavior.

<sub>macOS</sub>

```swift
static let automatic: AlternatingRowBackgroundBehavior
```

## Discussion

This defers to default component behavior for alternating row backgrounds. Some components, such as `Table` on macOS, will default to having alternating row backgrounds; while List does not.

## See Also

### Getting alternating row background behavior

- [enabled](enabled.md) — Alternating rows will be enabled for applicable views.
- [disabled](disabled.md) — Alternating rows will be disabled for applicable views.
