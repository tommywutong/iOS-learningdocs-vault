---
title: ToolbarItemVisibilityPriority
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 26.1+, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbaritemvisibilitypriority
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemvisibilitypriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemvisibilitypriority.json'
content_hash: 'sha256:ae18c382780277c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarItemVisibilityPriority

<sub>Structure</sub>

A value that defines the visibility priority of a toolbar item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ToolbarItemVisibilityPriority
```

## Overview

When a toolbar runs out of space, it moves items into an overflow menu. Visibility priority controls the order in which that happens: items with a lower priority move first, keeping higher-priority items visible longer as the window shrinks.

Use values of this type with the [visibilityPriority(_:)](<toolbarcontent/visibilitypriority(__).md>) modifier. For example, to keep a share button visible longer than an archive button:

```swift
struct RootView: View {
    var body: some View {
        ContentView()
            .toolbar {
                ToolbarItem {
                    SecondaryControl()
                }
                ToolbarItem {
                    PrimaryControl()
                }
                .visibilityPriority(.high)
            }
    }
}
```

## Relationships

- **Conforms To**: [Comparable](../swift/comparable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting system priorities

- [automatic](toolbaritemvisibilitypriority/automatic.md) — The default priority that lets the system determine the item’s visibility in the toolbar.
- [low](toolbaritemvisibilitypriority/low.md) — A priority that moves the item to the overflow menu before items with the default or high priority.
- [high](toolbaritemvisibilitypriority/high.md) — A priority that keeps the item in the toolbar longer than items with the default or low priority.

### Creating custom priorities

- [init(lowerThan:)](<toolbaritemvisibilitypriority/init(lowerthan_).md>) — Creates a priority lower than the specified value. _(beta)_
- [init(higherThan:)](<toolbaritemvisibilitypriority/init(higherthan_).md>) — Creates a priority higher than the specified value. _(beta)_

## See Also

### Controlling item visibility

- [visibilityPriority(_:)](<toolbarcontent/visibilitypriority(__).md>) — Defines the visibility priority for a toolbar item.
