---
title: LegibilityWeight
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/legibilityweight
source_url: 'https://developer.apple.com/documentation/swiftui/legibilityweight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/legibilityweight.json'
content_hash: 'sha256:19e4a8bf4e38ab5d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# LegibilityWeight

<sub>Enumeration</sub>

The Accessibility Bold Text user setting options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum LegibilityWeight
```

## Overview

The app can’t override the user’s choice before iOS 16, tvOS 16 or watchOS 9.0.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting weights

- [LegibilityWeight.regular](legibilityweight/regular.md) — Use regular font weight (no Accessibility Bold).
- [LegibilityWeight.bold](legibilityweight/bold.md) — Use heavier font weight (force Accessibility Bold).

### Creating a weight

- [init(_:)](<legibilityweight/init(__).md>) — Creates a legibility weight from its UILegibilityWeight equivalent.

## See Also

### Improving legibility

- [accessibilityShowButtonShapes](environmentvalues/accessibilityshowbuttonshapes.md) — Whether the system preference for Show Button Shapes is enabled. _(deprecated)_
- [accessibilityReduceTransparency](environmentvalues/accessibilityreducetransparency.md) — Whether the system preference for Reduce Transparency is enabled.
- [legibilityWeight](environmentvalues/legibilityweight.md) — The font weight to apply to text.
