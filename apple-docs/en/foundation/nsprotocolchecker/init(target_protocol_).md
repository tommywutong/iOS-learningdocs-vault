---
title: 'init(target:protocol:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsprotocolchecker/init(target:protocol:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsprotocolchecker/init(target:protocol:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsprotocolchecker/init%28target%3Aprotocol%3A%29.json'
content_hash: 'sha256:3f2f2551e58f813d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSProtocolChecker](../nsprotocolchecker.md)

# init(target:protocol:)

<sub>Initializer</sub>

Initializes a newly allocated `NSProtocolChecker` instance that will forward any messages in `aProtocol` to `anObject`, the protocol checker’s target.

<sub>Mac Catalyst, macOS</sub>

```swift
init(target anObject: NSObject, protocol aProtocol: Protocol)
```

## Discussion

Thus, the checker can be vended in lieu of `anObject` to restrict the messages that can be sent to `anObject`. If `anObject` is allowed to be freed or dereferenced by clients, the `free` method should be included in `aProtocol`.
