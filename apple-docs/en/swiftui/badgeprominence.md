---
title: BadgeProminence
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/badgeprominence
source_url: 'https://developer.apple.com/documentation/swiftui/badgeprominence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/badgeprominence.json'
content_hash: 'sha256:1534c59554d720a8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# BadgeProminence

<sub>Structure</sub>

The visual prominence of a badge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct BadgeProminence
```

## Overview

Badges can be used for different kinds of information, from the passive number of items in a container to the number of required actions. The prominence of badges in Lists can be adjusted to reflect this and be made to draw more or less attention to themselves.

Badges will default to `standard` prominence unless specified.

The following example shows a [List](list.md) displaying a list of folders with an informational badge with lower prominence, showing the number of items in the folder.

```swift
List(folders) { folder in
    Text(folder.name)
        .badge(folder.numberOfItems)
}
.badgeProminence(.decreased)
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting background prominence

- [standard](badgeprominence/standard.md) — The standard level of prominence for a badge.
- [increased](badgeprominence/increased.md) — The highest level of prominence for a badge.
- [decreased](badgeprominence/decreased.md) — The lowest level of prominence for a badge.

## See Also

### Displaying a badge on a list item

- [badge(_:)](<view/badge(__).md>) — Generates a badge for the view from a localized string resource.
- [badgeProminence(_:)](<view/badgeprominence(__).md>) — Specifies the prominence of badges created by this view.
- [badgeProminence](environmentvalues/badgeprominence.md) — The prominence to apply to badges associated with this environment.
