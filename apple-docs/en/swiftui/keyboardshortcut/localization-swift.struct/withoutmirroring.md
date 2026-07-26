---
title: withoutMirroring
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/keyboardshortcut/localization-swift.struct/withoutmirroring
source_url: 'https://developer.apple.com/documentation/swiftui/keyboardshortcut/localization-swift.struct/withoutmirroring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keyboardshortcut/localization-swift.struct/withoutmirroring.json'
content_hash: 'sha256:229bfa59230aa7d6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [KeyboardShortcut](../../keyboardshortcut.md) · [Localization](../localization-swift.struct.md)

# withoutMirroring

<sub>Type Property</sub>

Don’t mirror shortcuts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let withoutMirroring: KeyboardShortcut.Localization
```

## Discussion

Use this for shortcuts that always have a specific directionality, like aligning something on the right.

Don’t use this option for navigational shortcuts like “Go Back” because navigation is flipped in right-to-left contexts.

## See Also

### Getting localization strategies

- [automatic](automatic.md) — Remap shortcuts to their international counterparts, mirrored for right-to-left usage if appropriate.
- [custom](custom.md) — Don’t use automatic shortcut remapping.
