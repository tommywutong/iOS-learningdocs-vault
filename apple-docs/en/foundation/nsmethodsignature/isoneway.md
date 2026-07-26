---
title: isOneway
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmethodsignature/isoneway
source_url: 'https://developer.apple.com/documentation/foundation/nsmethodsignature/isoneway'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmethodsignature/isoneway.json'
content_hash: 'sha256:cf7a436d67ed81bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMethodSignature](../nsmethodsignature.md)

# isOneway

<sub>Instance Method</sub>

Whether the receiver is asynchronous when invoked through distributed objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (BOOL) isOneway;
```

## Return Value

[true](../../swift/true.md) if the receiver is asynchronous when invoked through distributed objects, otherwise [false](../../swift/false.md).

## Discussion

If the method is `oneway`, the sender of the remote message doesn’t block awaiting a reply.
