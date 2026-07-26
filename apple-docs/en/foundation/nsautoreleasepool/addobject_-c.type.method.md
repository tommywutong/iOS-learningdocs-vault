---
title: 'addObject:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsautoreleasepool/addobject:-c.type.method'
source_url: 'https://developer.apple.com/documentation/foundation/nsautoreleasepool/addobject:-c.type.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsautoreleasepool/addobject%3A-c.type.method.json'
content_hash: 'sha256:2ed71b0247f30b47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAutoreleasePool](../nsautoreleasepool.md)

# addObject:

<sub>Type Method</sub>

Adds a given object to the active autorelease pool in the current thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (void) addObject:(id) anObject;
```

## Parameters

- `anObject` — The object to add to the active autorelease pool in the current thread.

## Discussion

The same object may be added several times to the active pool and, when the pool is deallocated, it will receive a [release](../../objectivec/nsobject-c.protocol/release.md) message for each time it was added.

Normally you don’t invoke this method directly—you send [autorelease](../../objectivec/nsobject-c.protocol/autorelease.md) to `object` instead.

## See Also

### Adding an Object to a Pool

- [addObject:](addobject_-c.method.md) — Adds a given object to the receiver
