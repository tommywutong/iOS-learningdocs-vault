---
title: KeyboardShortcut.Localization
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/keyboardshortcut/localization-swift.struct
source_url: 'https://developer.apple.com/documentation/swiftui/keyboardshortcut/localization-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keyboardshortcut/localization-swift.struct.json'
content_hash: 'sha256:05e4a2ff071aa73d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [KeyboardShortcut](../keyboardshortcut.md)

# KeyboardShortcut.Localization

<sub>Structure</sub>

Options for how a keyboard shortcut participates in automatic localization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct Localization
```

## Overview

A shortcut’s `key` that is defined on an US-English keyboard layout might not be reachable on international layouts. For example the shortcut `⌘[` works well for the US layout but is hard to reach for German users. On the German keyboard layout, pressing `⌥5` will produce `[`, which causes the shortcut to become `⌥⌘5`. If configured, which is the default behavior, automatic shortcut remapping will convert it to `⌘Ö`.

In addition to that, some keyboard shortcuts carry information about directionality. Right-aligning a block of text or seeking forward in context of music playback are such examples. These kinds of shortcuts benefit from the option [withoutMirroring](localization-swift.struct/withoutmirroring.md) to tell the system that they won’t be flipped when running in a right-to-left context.

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting localization strategies

- [automatic](localization-swift.struct/automatic.md) — Remap shortcuts to their international counterparts, mirrored for right-to-left usage if appropriate.
- [custom](localization-swift.struct/custom.md) — Don’t use automatic shortcut remapping.
- [withoutMirroring](localization-swift.struct/withoutmirroring.md) — Don’t mirror shortcuts.

## See Also

### Creating a localized shortcut

- [init(_:modifiers:localization:)](<init(__modifiers_localization_).md>) — Creates a new keyboard shortcut with the given key equivalent and set of modifier keys.
- [localization](localization-swift.property.md) — The localization strategy to apply to this shortcut.
