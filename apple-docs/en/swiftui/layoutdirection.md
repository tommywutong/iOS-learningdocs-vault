---
title: LayoutDirection
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/layoutdirection
source_url: 'https://developer.apple.com/documentation/swiftui/layoutdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layoutdirection.json'
content_hash: 'sha256:5e924b16d498cbf7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# LayoutDirection

<sub>Enumeration</sub>

A direction in which SwiftUI can lay out content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum LayoutDirection
```

## Overview

SwiftUI supports both left-to-right and right-to-left directions for laying out content to support different languages and locales. The system sets the value based on the user’s locale, but you can also use the [environment(_:_:)](<view/environment(____).md>) modifier to override the direction for a view and its child views:

```swift
MyView()
    .environment(\.layoutDirection, .rightToLeft)
```

You can also read the [layoutDirection](environmentvalues/layoutdirection.md) environment value to find out which direction applies to a particular environment. However, in many cases, you don’t need to take any action based on this value. SwiftUI horizontally flips the x position of each view within its parent, so layout calculations automatically produce the desired effect for both modes without any changes.

## Relationships

- **Conforms To**: [CaseIterable](../swift/caseiterable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting layout directions

- [LayoutDirection.leftToRight](layoutdirection/lefttoright.md) — A left-to-right layout direction.
- [LayoutDirection.rightToLeft](layoutdirection/righttoleft.md) — A right-to-left layout direction.

### Creating a layout direction

- [init(_:)](<layoutdirection/init(__).md>) — Create a direction from its UITraitEnvironmentLayoutDirection equivalent.

## See Also

### Setting a layout direction

- [layoutDirectionBehavior(_:)](<view/layoutdirectionbehavior(__).md>) — Sets the behavior of this view for different layout directions.
- [LayoutDirectionBehavior](layoutdirectionbehavior.md) — A description of what should happen when the layout direction changes.
- [layoutDirection](environmentvalues/layoutdirection.md) — The layout direction associated with the current environment.
- [LayoutRotationUnaryLayout](layoutrotationunarylayout.md)
