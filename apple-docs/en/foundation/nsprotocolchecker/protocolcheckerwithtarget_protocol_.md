---
title: 'protocolCheckerWithTarget:protocol:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsprotocolchecker/protocolcheckerwithtarget:protocol:'
source_url: 'https://developer.apple.com/documentation/foundation/nsprotocolchecker/protocolcheckerwithtarget:protocol:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsprotocolchecker/protocolcheckerwithtarget%3Aprotocol%3A.json'
content_hash: 'sha256:129b903c87c2d1df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSProtocolChecker](../nsprotocolchecker.md)

# protocolCheckerWithTarget:protocol:

<sub>Type Method</sub>

Allocates and initializes an `NSProtocolChecker` instance that will forward any messages in `aProtocol` to `anObject`, the protocol checker’s target.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (instancetype) protocolCheckerWithTarget:(NSObject *) anObject protocol:(Protocol *) aProtocol;
```

## Discussion

Thus, the checker can be vended in lieu of `anObject` to restrict the messages that can be sent to `anObject`. Returns the new instance.

## See Also

### Related Documentation

- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)

### Creating a checker

- [- initWithTarget:protocol:](<init(target_protocol_).md>) — Initializes a newly allocated `NSProtocolChecker` instance that will forward any messages in `aProtocol` to `anObject`, the protocol checker’s target.
