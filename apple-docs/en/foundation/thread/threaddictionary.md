---
title: threadDictionary
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread/threaddictionary
source_url: 'https://developer.apple.com/documentation/foundation/thread/threaddictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/threaddictionary.json'
content_hash: 'sha256:fda4943f39b7563f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# threadDictionary

<sub>Instance Property</sub>

The thread object’s dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var threadDictionary: NSMutableDictionary { get }
```

## Discussion

You can use the returned dictionary to store thread-specific data. The thread dictionary is not used during any manipulations of the `NSThread` object—it is simply a place where you can store any interesting data. For example, Foundation uses it to store the thread’s default `NSConnection` and `NSAssertionHandler` instances. You may define your own keys for the dictionary.

## See Also

### Working with Thread Properties

- [NSAssertionHandlerKey](../nsassertionhandlerkey.md) — A key with a corresponding value in the thread dictionary.
- [name](name.md) — The name of the receiver.
- [stackSize](stacksize.md) — The stack size of the receiver, in bytes.
