---
title: NSTextSelectionNavigation.WritingDirection
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextselectionnavigation/writingdirection
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectionnavigation/writingdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectionnavigation/writingdirection.json'
content_hash: 'sha256:7c82b00fc5ba6119'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionNavigation](../nstextselectionnavigation.md)

# NSTextSelectionNavigation.WritingDirection

<sub>Enumeration</sub>

Values that describe the writing direction inside a text selection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum WritingDirection
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Writing directions

- [NSTextSelectionNavigationWritingDirectionLeftToRight](writingdirection/lefttoright.md) — The value that defines the left to right writing direction.
- [NSTextSelectionNavigationWritingDirectionRightToLeft](writingdirection/righttoleft.md) — The value that defines the right to left writing direction.

### Initializers

- [init(rawValue:)](<writingdirection/init(rawvalue_).md>)

## See Also

### Changing the characteristics of the selection

- [- baseWritingDirectionAtLocation:](<../nstextselectiondatasource/basewritingdirection(at_).md>) — Returns the base writing direction at the location you specify.
- [- textLayoutOrientationAtLocation:](<../nstextselectiondatasource/textlayoutorientation(at_).md>) — Returns the layout orientation at the location you specify.
- [LayoutOrientation](layoutorientation.md) — Values that describe the possible layout orientations.
