---
title: UIContextMenuConfiguration.ElementOrder
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontextmenuconfiguration/elementorder
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuconfiguration/elementorder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuconfiguration/elementorder.json'
content_hash: 'sha256:57fd3572b37dd881'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextMenuConfiguration](../uicontextmenuconfiguration.md)

# UIContextMenuConfiguration.ElementOrder

<sub>Enumeration</sub>

Constants that define the ordering strategy for menu elements in a context menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum ElementOrder
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIContextMenuConfigurationElementOrderAutomatic](elementorder/automatic.md) — A constant that allows the system to choose an ordering strategy according to the current context.
- [UIContextMenuConfigurationElementOrderPriority](elementorder/priority.md) — A constant that displays menu elements according to their priority.
- [UIContextMenuConfigurationElementOrderFixed](elementorder/fixed.md) — A constant that displays menu elements in a fixed order.

### Initializers

- [init(rawValue:)](<elementorder/init(rawvalue_).md>)

## See Also

### Specifying the order of menu elements

- [preferredMenuElementOrder](preferredmenuelementorder.md) — The preferred menu-element ordering strategy for the menu.
