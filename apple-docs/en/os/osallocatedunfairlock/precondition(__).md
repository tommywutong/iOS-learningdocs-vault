---
title: 'precondition(_:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osallocatedunfairlock/precondition(_:)'
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock/precondition(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock/precondition%28_%3A%29.json'
content_hash: 'sha256:709eebcd62048a43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSAllocatedUnfairLock](../osallocatedunfairlock.md)

# precondition(_:)

<sub>Instance Method</sub>

Asserts if the lock object fails to meet specified ownership requirements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func precondition(_ condition: OSAllocatedUnfairLock<State>.Ownership)
```

## Parameters

- `condition` — The ownership status to check.

## Discussion

Call this function to ensure the ownership state of the lock is what your code requires. For example, if you call this function and pass [OSAllocatedUnfairLock.Ownership.owner](ownership/owner.md), the app terminates if the object is locked, but the calling code doesn’t own the lock. Similarly, if you call it and pass [OSAllocatedUnfairLock.Ownership.notOwner](ownership/notowner.md), the app terminates if the calling code doesn’t own the lock, or if the object isn’t locked.

## See Also

### Determining lock ownership

- [Ownership](ownership.md) — An enumeration that represents the ownership status of an unfair lock.
