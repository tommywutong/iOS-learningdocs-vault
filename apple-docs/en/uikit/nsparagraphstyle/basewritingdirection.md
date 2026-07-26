---
title: baseWritingDirection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsparagraphstyle/basewritingdirection
source_url: 'https://developer.apple.com/documentation/uikit/nsparagraphstyle/basewritingdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsparagraphstyle/basewritingdirection.json'
content_hash: 'sha256:d08cfd297629d0bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSParagraphStyle](../nsparagraphstyle.md)

# baseWritingDirection

<sub>Instance Property</sub>

The base writing direction for the paragraph.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var baseWritingDirection: NSWritingDirection { get }
```

## Discussion

If you the value of this property is [NSWritingDirectionNatural](../nswritingdirection/natural.md), the receiver resolves the writing direction to either [NSWritingDirectionLeftToRight](../nswritingdirection/lefttoright.md) or [NSWritingDirectionRightToLeft](../nswritingdirection/righttoleft.md), depending on the direction for the user’s language preference setting.

## See Also

### Determining writing direction

- [+ defaultWritingDirectionForLanguage:](<defaultwritingdirection(forlanguage_).md>) — Returns the default writing direction for the specified language.
- [NSWritingDirection](../nswritingdirection.md) — Constants that specify the writing direction.
