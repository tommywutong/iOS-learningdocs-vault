---
title: 'lock(whenCondition:before:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsconditionlock/lock(whencondition:before:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsconditionlock/lock(whencondition:before:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconditionlock/lock%28whencondition%3Abefore%3A%29.json'
content_hash: 'sha256:c35d1aba9450add3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConditionLock](../nsconditionlock.md)

# lock(whenCondition:before:)

<sub>Instance Method</sub>

Attempts to acquire a lock before a specified moment in time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func lock(whenCondition condition: Int, before limit: Date) -> Bool
```

## Parameters

- `condition` — The condition to match on.

- `limit` — The date by which the lock must be acquired or the attempt will time out.

## Return Value

[true](../../swift/true.md) if the lock is acquired within the time limit, [false](../../swift/false.md) otherwise.

## Discussion

The receiver’s condition must be equal to `condition` before the locking operation will succeed. This method blocks the thread’s execution until the lock can be acquired or `limit` is reached.

## See Also

### Acquiring and Releasing a Lock

- [- lockBeforeDate:](<lock(before_).md>) — Attempts to acquire a lock before a specified moment in time.
- [- lockWhenCondition:](<lock(whencondition_).md>) — Attempts to acquire a lock.
- [- tryLock](<try().md>) — Attempts to acquire a lock without regard to the receiver’s condition.
- [- tryLockWhenCondition:](<trylock(whencondition_).md>) — Attempts to acquire a lock if the receiver’s condition is equal to the specified condition.
- [- unlockWithCondition:](<unlock(withcondition_).md>) — Relinquishes the lock and sets the receiver’s condition.
