---
title: UIContentInsetsReference
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentinsetsreference
source_url: 'https://developer.apple.com/documentation/uikit/uicontentinsetsreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentinsetsreference.json'
content_hash: 'sha256:7c9e1a894b0e550c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContentInsetsReference

<sub>Enumeration</sub>

Constants that describe the reference point of the content insets.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIContentInsetsReference
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIContentInsetsReferenceAutomatic](uicontentinsetsreference/automatic.md) — Content insets use the system default reference point.
- [UIContentInsetsReferenceNone](uicontentinsetsreference/none.md) — Content insets don’t have a reference point in relation to other insets.
- [UIContentInsetsReferenceSafeArea](uicontentinsetsreference/safearea.md) — Content insets use a reference point in relation to the safe area.
- [UIContentInsetsReferenceLayoutMargins](uicontentinsetsreference/layoutmargins.md) — Content insets use a reference point in relation to the layout margins.
- [UIContentInsetsReferenceReadableContent](uicontentinsetsreference/readablecontent.md) — Content insets use a reference point in relation to the readable content guide.

### Initializers

- [init(rawValue:)](<uicontentinsetsreference/init(rawvalue_).md>)

## See Also

### Configuring section spacing

- [interGroupSpacing](nscollectionlayoutsection/intergroupspacing.md) — The amount of space between the groups in the section.
- [contentInsets](nscollectionlayoutsection/contentinsets.md) — The amount of space between the content of the section and its boundaries.
- [contentInsetsReference](nscollectionlayoutsection/contentinsetsreference.md) — The boundary to reference when defining content insets.
- [supplementaryContentInsetsReference](nscollectionlayoutsection/supplementarycontentinsetsreference.md) — The reference boundary for content insets on boundary supplementary items.
