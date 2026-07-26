---
title: UIDynamicItemGroup
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicitemgroup
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicitemgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicitemgroup.json'
content_hash: 'sha256:076d70f92212f20c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDynamicItemGroup

<sub>Class</sub>

A dynamic item that comprises multiple other dynamic items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIDynamicItemGroup
```

## Overview

Use groups to manipulate a group of dynamic items together and treat them as a single unit for the purpose of collisions. The group can contain dynamic items but cannot contain other [UIDynamicItemGroup](uidynamicitemgroup.md) objects. You can add a group to any [UIDynamicBehavior](uidynamicbehavior.md) object.

The attributes of the dynamic item group are derived from the items of the group itself. The group’s bounds rectangle is the rectangle that encloses all of the contained dynamic items, and the center point of the group is the center point of the bounds rectangle.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIDynamicItem](uidynamicitem.md)

## Topics

### Initializing a group

- [- initWithItems:](<uidynamicitemgroup/init(items_).md>) — Initializes and returns a group containing the specified items.

### Getting the dynamic items in a group

- [items](uidynamicitemgroup/items.md) — The dynamic items in the group.

## See Also

### Dynamic items

- [UIDynamicItem](uidynamicitem.md) — A set of methods that can make a custom object eligible to participate in UIKit Dynamics.
- [UIDynamicItemBehavior](uidynamicitembehavior.md) — A base dynamic animation configuration for one or more dynamic items.
