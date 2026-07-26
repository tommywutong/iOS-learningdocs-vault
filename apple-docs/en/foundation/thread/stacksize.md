---
title: stackSize
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread/stacksize
source_url: 'https://developer.apple.com/documentation/foundation/thread/stacksize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/stacksize.json'
content_hash: 'sha256:d54abd549cb902de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# stackSize

<sub>Instance Property</sub>

The stack size of the receiver, in bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var stackSize: Int { get set }
```

## Discussion

This value must be in bytes and a multiple of 4KB.

To change the stack size, you must set this property before starting your thread. Setting the stack size after the thread has started changes the attribute size (which is reflected by the [stackSize](stacksize.md) method), but it does not affect the actual number of pages set aside for the thread.

## See Also

### Working with Thread Properties

- [threadDictionary](threaddictionary.md) — The thread object’s dictionary.
- [NSAssertionHandlerKey](../nsassertionhandlerkey.md) — A key with a corresponding value in the thread dictionary.
- [name](name.md) — The name of the receiver.
