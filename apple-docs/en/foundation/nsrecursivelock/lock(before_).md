---
title: 'lock(before:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsrecursivelock/lock(before:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsrecursivelock/lock(before:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsrecursivelock/lock%28before%3A%29.json'
content_hash: 'sha256:38742e5e96280f5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRecursiveLock](../nsrecursivelock.md)

# lock(before:)

<sub>Instance Method</sub>

Attempts to acquire a lock before a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func lock(before limit: Date) -> Bool
```

## Parameters

- `limit` — The time before which the lock should be acquired.

## Return Value

[true](../../swift/true.md) if the lock is acquired before `limit`, otherwise [false](../../swift/false.md).

## Discussion

The thread is blocked until the receiver acquires the lock or `limit` is reached.

## See Also

### Related Documentation

- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)

### Acquiring a Lock

- [- tryLock](<try().md>) — Attempts to acquire a lock, and immediately returns a Boolean value that indicates whether the attempt was successful.
