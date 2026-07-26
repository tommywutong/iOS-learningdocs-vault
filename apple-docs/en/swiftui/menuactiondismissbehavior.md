---
title: MenuActionDismissBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/menuactiondismissbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/menuactiondismissbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menuactiondismissbehavior.json'
content_hash: 'sha256:71c786df89e35d68'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# MenuActionDismissBehavior

<sub>Structure</sub>

The set of menu dismissal behavior options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MenuActionDismissBehavior
```

## Overview

Configure the menu dismissal behavior for a view hierarchy using the [menuActionDismissBehavior(_:)](<view/menuactiondismissbehavior(__).md>) view modifier.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Getting dismiss behaviors

- [automatic](menuactiondismissbehavior/automatic.md) — Use the a dismissal behavior that’s appropriate for the given context.
- [disabled](menuactiondismissbehavior/disabled.md) — Never dismiss the presented menu after performing an action.
- [enabled](menuactiondismissbehavior/enabled.md) — Always dismiss the presented menu after performing an action.

## See Also

### Configuring menu dismissal

- [menuActionDismissBehavior(_:)](<view/menuactiondismissbehavior(__).md>) — Tells a menu whether to dismiss after performing an action.
