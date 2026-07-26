---
title: optionsResolvesNaturalAlignmentWithBaseWritingDirection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsstringdrawingoptions/optionsresolvesnaturalalignmentwithbasewritingdirection
source_url: 'https://developer.apple.com/documentation/uikit/nsstringdrawingoptions/optionsresolvesnaturalalignmentwithbasewritingdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsstringdrawingoptions/optionsresolvesnaturalalignmentwithbasewritingdirection.json'
content_hash: 'sha256:0cef7fbe79144ef3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSStringDrawingOptions](../nsstringdrawingoptions.md)

# optionsResolvesNaturalAlignmentWithBaseWritingDirection

<sub>Type Property</sub>

Specifies the behavior for resolving [NSTextAlignmentNatural](../nstextalignment/natural.md) to the visual alignment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static var optionsResolvesNaturalAlignmentWithBaseWritingDirection: NSStringDrawingOptions { get }
```

## Discussion

When set, the resolved visual alignment is determined by the resolved base writing direction; otherwise, it is using the user’s preferred language.
