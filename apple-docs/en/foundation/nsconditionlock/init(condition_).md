---
title: 'init(condition:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsconditionlock/init(condition:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsconditionlock/init(condition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconditionlock/init%28condition%3A%29.json'
content_hash: 'sha256:755fec7c6f5ef238'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConditionLock](../nsconditionlock.md)

# init(condition:)

<sub>Initializer</sub>

Initializes a newly allocated `NSConditionLock` object and sets its condition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(condition: Int)
```

## Parameters

- `condition` — The user-defined condition for the lock. The value of `condition` is user-defined; see the class description for more information.

## Return Value

An initialized condition lock object; may be different than the original receiver.

## See Also

### Related Documentation

- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
