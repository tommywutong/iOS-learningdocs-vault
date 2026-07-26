---
title: 'lock(whenCondition:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsconditionlock/lock(whencondition:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsconditionlock/lock(whencondition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconditionlock/lock%28whencondition%3A%29.json'
content_hash: 'sha256:cece7cb481e3055f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConditionLock](../nsconditionlock.md)

# lock(whenCondition:)

<sub>Instance Method</sub>

Attempts to acquire a lock.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func lock(whenCondition condition: Int)
```

## Parameters

- `condition` — The condition to match on.

## Discussion

The receiver’s condition must be equal to `condition` before the locking operation will succeed. This method blocks the thread’s execution until the lock can be acquired.

## See Also

### Acquiring and Releasing a Lock

- [- lockBeforeDate:](<lock(before_).md>) — Attempts to acquire a lock before a specified moment in time.
- [- lockWhenCondition:beforeDate:](<lock(whencondition_before_).md>) — Attempts to acquire a lock before a specified moment in time.
- [- tryLock](<try().md>) — Attempts to acquire a lock without regard to the receiver’s condition.
- [- tryLockWhenCondition:](<trylock(whencondition_).md>) — Attempts to acquire a lock if the receiver’s condition is equal to the specified condition.
- [- unlockWithCondition:](<unlock(withcondition_).md>) — Relinquishes the lock and sets the receiver’s condition.
