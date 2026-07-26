---
title: UITextWritingDirection
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 3.2+（13.0 起废弃）, iPadOS 3.2+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uitextwritingdirection
source_url: 'https://developer.apple.com/documentation/uikit/uitextwritingdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextwritingdirection.json'
content_hash: 'sha256:6772efbc15407386'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextWritingDirection

<sub>Type Alias</sub>

The writing direction of the text for the language.

> [!warning] Deprecated
> Use [NSWritingDirection](nswritingdirection.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
typealias UITextWritingDirection = NSWritingDirection
```

## Discussion

Constants of this type are returned from the [- baseWritingDirectionForPosition:inDirection:](<uitextinput/basewritingdirection(for_in_).md>) method and are used as arguments of the [- setBaseWritingDirection:forRange:](<uitextinput/setbasewritingdirection(__for_).md>) method.

## See Also

### Deprecated

- [Style dictionary keys](style-dictionary-keys.md) — A dictionary that contains properties that define text style characteristics.
