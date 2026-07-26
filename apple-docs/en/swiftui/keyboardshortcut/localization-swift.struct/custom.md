---
title: custom
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/keyboardshortcut/localization-swift.struct/custom
source_url: 'https://developer.apple.com/documentation/swiftui/keyboardshortcut/localization-swift.struct/custom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keyboardshortcut/localization-swift.struct/custom.json'
content_hash: 'sha256:922fab752f7a007b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [KeyboardShortcut](../../keyboardshortcut.md) · [Localization](../localization-swift.struct.md)

# custom

<sub>Type Property</sub>

Don’t use automatic shortcut remapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let custom: KeyboardShortcut.Localization
```

## Discussion

When you use this mode, you have to take care of international use-cases separately.

## See Also

### Getting localization strategies

- [automatic](automatic.md) — Remap shortcuts to their international counterparts, mirrored for right-to-left usage if appropriate.
- [withoutMirroring](withoutmirroring.md) — Don’t mirror shortcuts.
