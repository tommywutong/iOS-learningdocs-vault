---
title: LayoutDirectionBehavior
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/layoutdirectionbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/layoutdirectionbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layoutdirectionbehavior.json'
content_hash: 'sha256:e727db882d2588e9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# LayoutDirectionBehavior

<sub>Enumeration</sub>

A description of what should happen when the layout direction changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum LayoutDirectionBehavior
```

## Overview

A `LayoutDirectionBehavior` can be used with the `layoutDirectionBehavior` view modifier or the `layoutDirectionBehavior` property of `Shape`.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting behaviors

- [LayoutDirectionBehavior.fixed](layoutdirectionbehavior/fixed.md) — A behavior that doesn’t mirror when the layout direction changes.
- [mirrors](layoutdirectionbehavior/mirrors.md) — A behavior that mirrors when the layout direction is right-to-left.
- [LayoutDirectionBehavior.mirrors(in:)](<layoutdirectionbehavior/mirrors(in_).md>) — A behavior that mirrors when the layout direction has the specified value.

## See Also

### Setting a layout direction

- [layoutDirectionBehavior(_:)](<view/layoutdirectionbehavior(__).md>) — Sets the behavior of this view for different layout directions.
- [layoutDirection](environmentvalues/layoutdirection.md) — The layout direction associated with the current environment.
- [LayoutDirection](layoutdirection.md) — A direction in which SwiftUI can lay out content.
- [LayoutRotationUnaryLayout](layoutrotationunarylayout.md)
