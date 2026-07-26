---
title: NSLayoutManager.TypesetterBehavior
framework: AppKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nslayoutmanager/typesetterbehavior-swift.enum
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/typesetterbehavior-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/typesetterbehavior-swift.enum.json'
content_hash: 'sha256:03404f83b0fbc7c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# NSLayoutManager.TypesetterBehavior

<sub>Enumeration</sub>

Constants that determine the layout manager’s behavior during layout.

<sub>macOS</sub>

```swift
enum TypesetterBehavior
```

## Overview

These constants define the behavior of `NSLayoutManager` and `NSTypesetter` when laying out lines. They are used by [typesetterBehavior](typesetterbehavior-swift.property.md) to control the compatibility level of the typesetter.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Behaviors

- [NSTypesetterLatestBehavior](typesetterbehavior-swift.enum/latestbehavior.md) — The current typesetter behavior in the current operating system.
- [NSTypesetterOriginalBehavior](typesetterbehavior-swift.enum/originalbehavior.md) — The original typesetter behavior, as shipped with macOS 10.1 and earlier.
- [NSTypesetterBehavior_10_2_WithCompatibility](typesetterbehavior-swift.enum/behavior_10_2_withcompatibility.md) — The macOS 10.2 typesetting behavior that is still compatible with the original typesetter behavior.
- [NSTypesetterBehavior_10_2](typesetterbehavior-swift.enum/behavior_10_2.md) — The typesetter behavior introduced in macOS 10.2.
- [NSTypesetterBehavior_10_3](typesetterbehavior-swift.enum/behavior_10_3.md) — The typesetter behavior introduced in macOS 10.3.
- [NSTypesetterBehavior_10_4](typesetterbehavior-swift.enum/behavior_10_4.md) — The typesetter behavior introduced in macOS 10.4.

### Initializers

- [init(rawValue:)](<typesetterbehavior-swift.enum/init(rawvalue_).md>)

## See Also

### Managing the typesetter

- [typesetter](typesetter.md) — The current typesetter.
- [typesetterBehavior](typesetterbehavior-swift.property.md) — The default typesetter behavior.
- [- defaultLineHeightForFont:](<defaultlineheight(for_).md>) — Returns the default line height for a line of text that uses a specified font.
- [- defaultBaselineOffsetForFont:](<defaultbaselineoffset(for_).md>) — Returns the default baseline offset that the layout manager’s typesetter uses for the specified font.
