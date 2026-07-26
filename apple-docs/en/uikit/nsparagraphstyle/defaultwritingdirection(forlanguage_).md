---
title: 'defaultWritingDirection(forLanguage:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsparagraphstyle/defaultwritingdirection(forlanguage:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsparagraphstyle/defaultwritingdirection(forlanguage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsparagraphstyle/defaultwritingdirection%28forlanguage%3A%29.json'
content_hash: 'sha256:266c6f08873c8a88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSParagraphStyle](../nsparagraphstyle.md)

# defaultWritingDirection(forLanguage:)

<sub>Type Method</sub>

Returns the default writing direction for the specified language.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class func defaultWritingDirection(forLanguage languageName: String?) -> NSWritingDirection
```

## Parameters

- `languageName` — The language specified in ISO language region format. Can be `nil` to return a default writing direction derived from the user’s defaults database.

## Return Value

The default writing direction.

## See Also

### Determining writing direction

- [baseWritingDirection](basewritingdirection.md) — The base writing direction for the paragraph.
- [NSWritingDirection](../nswritingdirection.md) — Constants that specify the writing direction.
