---
title: NSWritingDirection
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nswritingdirection
source_url: 'https://developer.apple.com/documentation/uikit/nswritingdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nswritingdirection.json'
content_hash: 'sha256:2e90b5fa78bdb41a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSWritingDirection

<sub>Enumeration</sub>

Constants that specify the writing direction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
enum NSWritingDirection
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [NSWritingDirectionNatural](nswritingdirection/natural.md) — The writing direction of the current script that the system determines using the Unicode Bidi Algorithm rules P2 and P3.
- [NSWritingDirectionLeftToRight](nswritingdirection/lefttoright.md) — The writing direction is left to right.
- [NSWritingDirectionRightToLeft](nswritingdirection/righttoleft.md) — The writing direction is right to left.

### Initializers

- [init(rawValue:)](<nswritingdirection/init(rawvalue_).md>)

## See Also

### Determining writing direction

- [+ defaultWritingDirectionForLanguage:](<nsparagraphstyle/defaultwritingdirection(forlanguage_).md>) — Returns the default writing direction for the specified language.
- [baseWritingDirection](nsparagraphstyle/basewritingdirection.md) — The base writing direction for the paragraph.
