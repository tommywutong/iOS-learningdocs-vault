---
title: NSTextWritingDirection.embedding
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+（9.0 起废弃）, iPadOS 7.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/nstextwritingdirection/embedding
source_url: 'https://developer.apple.com/documentation/uikit/nstextwritingdirection/embedding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextwritingdirection/embedding.json'
content_hash: 'sha256:227b4426ea9aeeee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextWritingDirection](../nstextwritingdirection.md)

# NSTextWritingDirection.embedding

<sub>Case</sub>

Text is embedded in text with another writing direction.

> [!warning] Deprecated
> Use [NSWritingDirectionEmbedding](../nswritingdirectionformattype/embedding.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
case embedding
```

## Overview

For example, an English quotation in the middle of an Arabic sentence could be marked as being embedded left-to-right text.

## See Also

### Constants

- [NSTextWritingDirectionOverride](override.md) — Enables character types with inherent directionality to be overridden when required for special cases, such as for part numbers made of mixed English, digits, and Hebrew letters to be written from right to left. _(deprecated)_
