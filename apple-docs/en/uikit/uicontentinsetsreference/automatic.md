---
title: UIContentInsetsReference.automatic
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentinsetsreference/automatic
source_url: 'https://developer.apple.com/documentation/uikit/uicontentinsetsreference/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentinsetsreference/automatic.json'
content_hash: 'sha256:384774531b820743'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentInsetsReference](../uicontentinsetsreference.md)

# UIContentInsetsReference.automatic

<sub>Case</sub>

Content insets use the system default reference point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case automatic
```

## Discussion

When you set this value on a section in a collection view, the section defaults to using the content insets reference value of the collection view.

## See Also

### Constants

- [UIContentInsetsReferenceNone](none.md) — Content insets don’t have a reference point in relation to other insets.
- [UIContentInsetsReferenceSafeArea](safearea.md) — Content insets use a reference point in relation to the safe area.
- [UIContentInsetsReferenceLayoutMargins](layoutmargins.md) — Content insets use a reference point in relation to the layout margins.
- [UIContentInsetsReferenceReadableContent](readablecontent.md) — Content insets use a reference point in relation to the readable content guide.
