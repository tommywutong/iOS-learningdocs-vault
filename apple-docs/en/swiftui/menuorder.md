---
title: MenuOrder
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/menuorder
source_url: 'https://developer.apple.com/documentation/swiftui/menuorder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menuorder.json'
content_hash: 'sha256:37190f3c05c28c82'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# MenuOrder

<sub>Structure</sub>

The order in which a menu presents its content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MenuOrder
```

## Overview

You can configure the preferred menu order using the [menuOrder(_:)](<view/menuorder(__).md>) view modifier.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting menu orders

- [automatic](menuorder/automatic.md) — The ordering of the menu chosen by the system for the current context.
- [fixed](menuorder/fixed.md) — Order items from top to bottom.
- [priority](menuorder/priority.md) — Keep the first items closest to user’s interaction point.

## See Also

### Setting a preferred order

- [menuOrder(_:)](<view/menuorder(__).md>) — Sets the preferred order of items for menus presented from this view.
- [menuOrder](environmentvalues/menuorder.md) — The preferred order of items for menus presented from this view.
