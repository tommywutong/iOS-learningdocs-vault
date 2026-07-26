---
title: evaluate()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspositionalspecifier/evaluate()
source_url: 'https://developer.apple.com/documentation/foundation/nspositionalspecifier/evaluate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspositionalspecifier/evaluate%28%29.json'
content_hash: 'sha256:e38ce5bec1d85f2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPositionalSpecifier](../nspositionalspecifier.md)

# evaluate()

<sub>Instance Method</sub>

Causes the receiver to evaluate its position.

<sub>Mac Catalyst, macOS</sub>

```swift
func evaluate()
```

## Discussion

Calling [insertionContainer](insertioncontainer.md), [insertionKey](insertionkey.md), [insertionIndex](insertionindex.md), or [insertionReplaces](insertionreplaces.md) also causes the receiver to be evaluated, if it hasn’t already been evaluated.
