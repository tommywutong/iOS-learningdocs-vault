---
title: run()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsspellserver/run()
source_url: 'https://developer.apple.com/documentation/foundation/nsspellserver/run()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsspellserver/run%28%29.json'
content_hash: 'sha256:ebc432d30bb06e90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSpellServer](../nsspellserver.md)

# run()

<sub>Instance Method</sub>

Causes the receiver to start listening for spell-checking requests.

<sub>Mac Catalyst, macOS</sub>

```swift
func run()
```

## Discussion

This method starts a loop that never returns; you need to set the `NSSpellServer` object’s delegate before sending this message.

## See Also

### Related Documentation

- [delegate](delegate.md) — Returns the receiver’s delegate.

### Providing Spelling Services

- [- registerLanguage:byVendor:](<registerlanguage(__byvendor_).md>) — Notifies the receiver of a language your spelling checker can check.
