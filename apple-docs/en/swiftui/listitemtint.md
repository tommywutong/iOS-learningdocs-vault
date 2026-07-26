---
title: ListItemTint
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/listitemtint
source_url: 'https://developer.apple.com/documentation/swiftui/listitemtint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/listitemtint.json'
content_hash: 'sha256:fdd2268a9f2191fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ListItemTint

<sub>Structure</sub>

A tint effect configuration that you can apply to content in a list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ListItemTint
```

## Overview

Use one of these tint values with the [listItemTint(_:)](<view/listitemtint(__).md>) view modifier. The containing list applies the tint in a platform-specific way. On iOS and macOS, sidebars apply the tint color to [Label](label.md) icons, which otherwise use the app’s accent color by default.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting list item tint options

- [monochrome](listitemtint/monochrome.md) — A standard grayscale tint effect.
- [fixed(_:)](<listitemtint/fixed(__).md>) — An explicit tint color.
- [preferred(_:)](<listitemtint/preferred(__).md>) — An explicit tint color that the system can override.

## See Also

### Configuring rows

- [listItemTint(_:)](<view/listitemtint(__).md>) — Sets a fixed tint color for content in a list.
