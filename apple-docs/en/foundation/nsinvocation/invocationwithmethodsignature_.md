---
title: 'invocationWithMethodSignature:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsinvocation/invocationwithmethodsignature:'
source_url: 'https://developer.apple.com/documentation/foundation/nsinvocation/invocationwithmethodsignature:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinvocation/invocationwithmethodsignature%3A.json'
content_hash: 'sha256:abb9df9f791edba4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSInvocation](../nsinvocation.md)

# invocationWithMethodSignature:

<sub>Type Method</sub>

Returns an `NSInvocation` object able to construct messages using a given method signature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSInvocation *) invocationWithMethodSignature:(NSMethodSignature *) sig;
```

## Parameters

- `sig` — An object encapsulating a method signature.

## Discussion

The new object must have its selector set with [NSInvocation](../nsinvocation.md) and its arguments set with [setArgument:atIndex:](setargument_atindex_.md) before it can be invoked. Do not use the [alloc](../../objectivec/nsobject-swift.class/alloc.md)/[init()](<../../objectivec/nsobject-swift.class/init().md>) approach to create `NSInvocation` objects.

## See Also

### Related Documentation

- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
