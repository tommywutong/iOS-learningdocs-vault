---
title: UIContentSizeCategory
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentsizecategory
source_url: 'https://developer.apple.com/documentation/uikit/uicontentsizecategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentsizecategory.json'
content_hash: 'sha256:4866980b43b6f0d7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContentSizeCategory

<sub>Structure</sub>

Constants that indicate the preferred size of your content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UIContentSizeCategory
```

## Relationships

- **Conforms To**: [Comparable](../swift/comparable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Font sizes

- [UIContentSizeCategoryUnspecified](uicontentsizecategory/unspecified.md) — An unspecified font size.
- [UIContentSizeCategoryExtraSmall](uicontentsizecategory/extrasmall.md) — An extra-small font.
- [UIContentSizeCategorySmall](uicontentsizecategory/small.md) — A small font.
- [UIContentSizeCategoryMedium](uicontentsizecategory/medium.md) — A medium-sized font.
- [UIContentSizeCategoryLarge](uicontentsizecategory/large.md) — A large font.
- [UIContentSizeCategoryExtraLarge](uicontentsizecategory/extralarge.md) — An extra-large font.
- [UIContentSizeCategoryExtraExtraLarge](uicontentsizecategory/extraextralarge.md) — A font that is larger than the extra-large font but smaller than the largest font size available.
- [UIContentSizeCategoryExtraExtraExtraLarge](uicontentsizecategory/extraextraextralarge.md) — The largest font size.

### Accessibility sizes

- [UIContentSizeCategoryAccessibilityMedium](uicontentsizecategory/accessibilitymedium.md) — A medium font size that reflects the current accessibility settings.
- [UIContentSizeCategoryAccessibilityLarge](uicontentsizecategory/accessibilitylarge.md) — A large font size that reflects the current accessibility settings.
- [UIContentSizeCategoryAccessibilityExtraLarge](uicontentsizecategory/accessibilityextralarge.md) — An extra-large font size that reflects the current accessibility settings.
- [UIContentSizeCategoryAccessibilityExtraExtraLarge](uicontentsizecategory/accessibilityextraextralarge.md) — A font that is larger than the extra-large font but not the largest available, reflecting the current accessibility settings.
- [UIContentSizeCategoryAccessibilityExtraExtraExtraLarge](uicontentsizecategory/accessibilityextraextraextralarge.md) — The largest font size that reflects the current accessibility settings.
- [isAccessibilityCategory](uicontentsizecategory/isaccessibilitycategory.md) — A Boolean value that indicates whether the content size category is associated with accessibility.

### Font size change notifications

- [UIContentSizeCategoryDidChangeNotification](uicontentsizecategory/didchangenotification.md) — A notification that posts when the user changes the preferred content size setting.
- [UIContentSizeCategoryNewValueKey](uicontentsizecategory/newvalueuserinfokey.md) — A key that reflects the new preferred content size.

### Font size category creation

- [init(rawValue:)](<uicontentsizecategory/init(rawvalue_).md>) — Creates a new instance with the specified raw value.
- [init(_:)](<uicontentsizecategory/init(__)-9l1kn.md>) — Creates a content size category from the specified SwiftUI content size category.
- [init(_:)](<uicontentsizecategory/init(__)-abz4.md>) — Creates a content size category from the specified SwiftUI Dynamic Type size.

### Structures

- [DidChangeMessage](uicontentsizecategory/didchangemessage.md)

## See Also

### Managing the preferred content size

- [preferredContentSizeCategory](uiapplication/preferredcontentsizecategory.md) — The font sizing option preferred by the user.
- [UIContentSizeCategoryAdjusting](uicontentsizecategoryadjusting.md) — A collection of methods that give controls an easy way to adopt automatic adjustment to content category changes.
- [UIContentSizeCategoryDidChangeNotification](uicontentsizecategory/didchangenotification.md) — A notification that posts when the user changes the preferred content size setting.
- [UIContentSizeCategoryNewValueKey](uicontentsizecategory/newvalueuserinfokey.md) — A key that reflects the new preferred content size.
