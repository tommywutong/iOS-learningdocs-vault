---
title: NSTextWritingDirection
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+（9.0 起废弃）, iPadOS 7.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/nstextwritingdirection
source_url: 'https://developer.apple.com/documentation/uikit/nstextwritingdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextwritingdirection.json'
content_hash: 'sha256:5519a3127a64ad8d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextWritingDirection

<sub>Enumeration</sub>

Options for specifying text-writing direction.

> [!warning] Deprecated
> Use [NSWritingDirectionFormatType](nswritingdirectionformattype.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
enum NSTextWritingDirection
```

## Overview

You can use the logical OR operator to combine these constants with [NSWritingDirectionLeftToRight](nswritingdirection/lefttoright.md) or [NSWritingDirectionRightToLeft](nswritingdirection/righttoleft.md) when used with [`writingDirection`](../foundation/nsattributedstring/key/writingdirection.md) to specify formatting controls defined by the Unicode Bidirectional Algorithm in [Unicode Standard Annex #9](http://unicode.org/reports/tr9/).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [NSTextWritingDirectionEmbedding](nstextwritingdirection/embedding.md) — Text is embedded in text with another writing direction. _(deprecated)_
- [NSTextWritingDirectionOverride](nstextwritingdirection/override.md) — Enables character types with inherent directionality to be overridden when required for special cases, such as for part numbers made of mixed English, digits, and Hebrew letters to be written from right to left. _(deprecated)_

### Initializers

- [init(rawValue:)](<nstextwritingdirection/init(rawvalue_).md>) _(deprecated)_
