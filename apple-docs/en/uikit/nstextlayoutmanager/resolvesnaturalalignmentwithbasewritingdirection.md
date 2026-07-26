---
title: resolvesNaturalAlignmentWithBaseWritingDirection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutmanager/resolvesnaturalalignmentwithbasewritingdirection
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/resolvesnaturalalignmentwithbasewritingdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/resolvesnaturalalignmentwithbasewritingdirection.json'
content_hash: 'sha256:04c6a2cb009cd82c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# resolvesNaturalAlignmentWithBaseWritingDirection

<sub>Instance Property</sub>

Specifies the behavior for resolving [NSTextAlignmentNatural](../nstextalignment/natural.md) to the visual alignment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var resolvesNaturalAlignmentWithBaseWritingDirection: Bool { get set }
```

## Discussion

When set to `true`, the resolved visual alignment is determined by the resolved base writing direction; otherwise, it is using the user’s preferred language. The default value is `true`.
