---
title: default
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsparagraphstyle/default
source_url: 'https://developer.apple.com/documentation/uikit/nsparagraphstyle/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsparagraphstyle/default.json'
content_hash: 'sha256:dcdb4d942b1df985'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSParagraphStyle](../nsparagraphstyle.md)

# default

<sub>Type Property</sub>

The default paragraph style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying class var `default`: NSParagraphStyle { get }
```

## Discussion

The default paragraph style has the following default values:

| Subattribute | Default |
|---|---|
| Alignment | `NSNaturalTextAlignment` |
| Tab stops | 12 left-aligned tabs, spaced by `28.0` points |
| Line break mode | `NSLineBreakByWordWrapping` |
| All others | `0.0` |

See individual method descriptions for explanations of each subattribute.
