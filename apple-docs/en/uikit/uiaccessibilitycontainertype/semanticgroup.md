---
title: UIAccessibilityContainerType.semanticGroup
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitycontainertype/semanticgroup
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycontainertype/semanticgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycontainertype/semanticgroup.json'
content_hash: 'sha256:0e3727bb9728227a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityContainerType](../uiaccessibilitycontainertype.md)

# UIAccessibilityContainerType.semanticGroup

<sub>Case</sub>

A semantic group of data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
case semanticGroup
```

## Discussion

Assistive technologies might query the accessibility properties set on the container, such as the `accessibilityLabel`, in order to output appropriate information about the semantic group to the user.

## See Also

### Constants

- [UIAccessibilityContainerTypeNone](none.md) — No additional data.
- [UIAccessibilityContainerTypeDataTable](datatable.md) — A table that contains structured data.
- [UIAccessibilityContainerTypeList](list.md) — A list of data.
- [UIAccessibilityContainerTypeLandmark](landmark.md) — Landmark data.
