---
title: iconOnly
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/labelstyle/icononly
source_url: 'https://developer.apple.com/documentation/swiftui/labelstyle/icononly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/labelstyle/icononly.json'
content_hash: 'sha256:dd3a1016dedd4d9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LabelStyle](../labelstyle.md)

# iconOnly

<sub>Type Property</sub>

A label style that only displays the icon of the label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated static var iconOnly: IconOnlyLabelStyle { get }
```

## Discussion

The title of the label is still used for non-visual descriptions, such as VoiceOver.

## See Also

### Getting built-in label styles

- [automatic](automatic.md) — A label style that resolves its appearance automatically based on the current context.
- [titleAndIcon](titleandicon.md) — A label style that shows both the title and icon of the label using a system-standard layout.
- [titleOnly](titleonly.md) — A label style that only displays the title of the label.
