---
title: DynamicTypeSize
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dynamictypesize
source_url: 'https://developer.apple.com/documentation/swiftui/dynamictypesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dynamictypesize.json'
content_hash: 'sha256:933669a98dd0aa28'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DynamicTypeSize

<sub>Enumeration</sub>

A Dynamic Type size, which specifies how large scalable content should be.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum DynamicTypeSize
```

## Overview

For more information, see [Typography](../design/human-interface-guidelines/typography.md) in the Human Interface Guidelines.

## Relationships

- **Conforms To**: [CaseIterable](../swift/caseiterable.md), [Comparable](../swift/comparable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting type sizes

- [DynamicTypeSize.xSmall](dynamictypesize/xsmall.md) — An extra small size.
- [DynamicTypeSize.small](dynamictypesize/small.md) — A small size.
- [DynamicTypeSize.medium](dynamictypesize/medium.md) — A medium size.
- [DynamicTypeSize.large](dynamictypesize/large.md) — A large size.
- [DynamicTypeSize.xLarge](dynamictypesize/xlarge.md) — An extra large size.
- [DynamicTypeSize.xxLarge](dynamictypesize/xxlarge.md) — An extra extra large size.
- [DynamicTypeSize.xxxLarge](dynamictypesize/xxxlarge.md) — An extra extra extra large size.

### Getting accessibility type sizes

- [DynamicTypeSize.accessibility1](dynamictypesize/accessibility1.md) — The first accessibility size.
- [DynamicTypeSize.accessibility2](dynamictypesize/accessibility2.md) — The second accessibility size.
- [DynamicTypeSize.accessibility3](dynamictypesize/accessibility3.md) — The third accessibility size.
- [DynamicTypeSize.accessibility4](dynamictypesize/accessibility4.md) — The fourth accessibility size.
- [DynamicTypeSize.accessibility5](dynamictypesize/accessibility5.md) — The fifth accessibility size.
- [isAccessibilitySize](dynamictypesize/isaccessibilitysize.md) — A Boolean value indicating whether the size is one that is associated with accessibility.

### Creating a type size

- [init(_:)](<dynamictypesize/init(__).md>) — Create a Dynamic Type size from its `UIContentSizeCategory` equivalent.

## See Also

### Adjusting text size

- [textScale(_:isEnabled:)](<view/textscale(__isenabled_).md>) — Applies a text scale to text in the view.
- [dynamicTypeSize(_:)](<view/dynamictypesize(__).md>) — Sets the Dynamic Type size within the view to the given value.
- [dynamicTypeSize](environmentvalues/dynamictypesize.md) — The current Dynamic Type size.
- [ScaledMetric](scaledmetric.md) — A dynamic property that scales a numeric value.
- [TextVariantPreference](textvariantpreference.md) — A protocol for controlling the size variant of text views.
- [FixedTextVariant](fixedtextvariant.md) — The default text variant preference that chooses the largest available variant.
- [SizeDependentTextVariant](sizedependenttextvariant.md) — The size dependent variant preference allows the text to take the available space into account when choosing the variant to display.
