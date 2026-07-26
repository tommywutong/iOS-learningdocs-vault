---
title: init()
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread/init()
source_url: 'https://developer.apple.com/documentation/foundation/thread/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/init%28%29.json'
content_hash: 'sha256:9c65c50fc30d00ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# init()

<sub>Initializer</sub>

Returns an initialized `NSThread` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Return Value

An initialized `NSThread` object.

## Discussion

This is the designated initializer for `NSThread`.

## See Also

### Related Documentation

- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
- [- start](<start().md>) — Starts the receiver.

### Initializing an NSThread Object

- [- initWithTarget:selector:object:](<init(target_selector_object_).md>) — Returns an `NSThread` object initialized with the given arguments.
