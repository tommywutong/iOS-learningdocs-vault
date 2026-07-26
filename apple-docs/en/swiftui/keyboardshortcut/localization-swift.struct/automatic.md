---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/keyboardshortcut/localization-swift.struct/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/keyboardshortcut/localization-swift.struct/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keyboardshortcut/localization-swift.struct/automatic.json'
content_hash: 'sha256:7cd03c302f9efc13'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [KeyboardShortcut](../../keyboardshortcut.md) · [Localization](../localization-swift.struct.md)

# automatic

<sub>Type Property</sub>

Remap shortcuts to their international counterparts, mirrored for right-to-left usage if appropriate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let automatic: KeyboardShortcut.Localization
```

## Discussion

This is the default configuration.

## See Also

### Getting localization strategies

- [custom](custom.md) — Don’t use automatic shortcut remapping.
- [withoutMirroring](withoutmirroring.md) — Don’t mirror shortcuts.
