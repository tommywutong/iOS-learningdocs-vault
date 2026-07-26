---
title: NSLocale.LanguageDirection
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslocale/languagedirection
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/languagedirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/languagedirection.json'
content_hash: 'sha256:e66bbac1fd4d680d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# NSLocale.LanguageDirection

<sub>Enumeration</sub>

The directions that a language may take across a page of text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum LanguageDirection
```

## Overview

Use these constants with the methods [+ lineDirectionForLanguage:](<linedirection(forlanguage_).md>) and [+ characterDirectionForLanguage:](<characterdirection(forlanguage_).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSLocaleLanguageDirectionUnknown](languagedirection/unknown.md) — The direction of the language is unknown.
- [NSLocaleLanguageDirectionLeftToRight](languagedirection/lefttoright.md) — The language direction is from left to right.
- [NSLocaleLanguageDirectionRightToLeft](languagedirection/righttoleft.md) — The language direction is from right to left.
- [NSLocaleLanguageDirectionTopToBottom](languagedirection/toptobottom.md) — The language direction is from top to bottom.
- [NSLocaleLanguageDirectionBottomToTop](languagedirection/bottomtotop.md) — The language direction is from bottom to top.

### Initializers

- [init(rawValue:)](<languagedirection/init(rawvalue_).md>)

## See Also

### Getting line and character direction for a language

- [characterDirection(forLanguage:)](<../locale/characterdirection(forlanguage_).md>) — Returns the character direction for a specified language code. _(deprecated)_
- [lineDirection(forLanguage:)](<../locale/linedirection(forlanguage_).md>) — Returns the line direction for a specified language code. _(deprecated)_
- [LanguageDirection](../locale/languagedirection.md) — An alias for the standard set of language directions.
