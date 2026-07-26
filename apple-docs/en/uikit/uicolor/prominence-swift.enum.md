---
title: UIColor.Prominence
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicolor/prominence-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/prominence-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/prominence-swift.enum.json'
content_hash: 'sha256:2c03baaf061f89ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# UIColor.Prominence

<sub>Enumeration</sub>

A type that indicates the prominence of a color in the interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Prominence
```

## Overview

Interface elements, such as text labels, can have a different level of prominence in the UI. For example, a title label appears more prominently than a subtitle or caption. When you specify a label’s color, you can pass one of the [Prominence](prominence-swift.enum.md) constants to [- colorWithProminence:](<withprominence(__).md>) to communicate how prominently to display that color in the UI.

The following code creates a label with a secondary, vibrant red color:

```swift
let label = UILabel()
label.preferredVibrancy = .automatic
label.textColor = .systemRed.withProminence(.secondary) 
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIColorProminencePrimary](prominence-swift.enum/primary.md) — A color with a primary prominence, the most prominent in the interface.
- [UIColorProminenceSecondary](prominence-swift.enum/secondary.md) — A color with a secondary prominence.
- [UIColorProminenceTertiary](prominence-swift.enum/tertiary.md) — A color with a tertiary prominence.
- [UIColorProminenceQuaternary](prominence-swift.enum/quaternary.md) — A color with a quaternary prominence, the least prominent in the interface.

### Initializers

- [init(rawValue:)](<prominence-swift.enum/init(rawvalue_).md>)

## See Also

### Working with color prominence

- [prominence](prominence-swift.property.md)
- [- colorWithProminence:](<withprominence(__).md>) — Returns the version of the current color that results from applying the specified prominence.
