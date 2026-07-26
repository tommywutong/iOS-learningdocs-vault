---
title: lockIfAvailable()
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/osallocatedunfairlock/lockifavailable()
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock/lockifavailable()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock/lockifavailable%28%29.json'
content_hash: 'sha256:1e6251818fea7ad1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSAllocatedUnfairLock](../osallocatedunfairlock.md)

# lockIfAvailable()

<sub>Instance Method</sub>

Attempts to acquire a lock.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func lockIfAvailable() -> Bool
```

## Return Value

[true](../../swift/true.md) if successful; otherwise, [false](../../swift/false.md).

## See Also

### Using locks

- [lock()](<lock().md>) — Acquires a lock.
- [unlock()](<unlock().md>) — Ends the lock.
