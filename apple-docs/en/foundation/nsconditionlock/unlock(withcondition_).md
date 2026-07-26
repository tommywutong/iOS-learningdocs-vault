---
title: 'unlock(withCondition:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsconditionlock/unlock(withcondition:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsconditionlock/unlock(withcondition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconditionlock/unlock%28withcondition%3A%29.json'
content_hash: 'sha256:6ae935fc098007f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConditionLock](../nsconditionlock.md)

# unlock(withCondition:)

<sub>Instance Method</sub>

Relinquishes the lock and sets the receiver’s condition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func unlock(withCondition condition: Int)
```

## Parameters

- `condition` — The user-defined condition for the lock. The value of `condition` is user-defined; see the class description for more information.

## See Also

### Acquiring and Releasing a Lock

- [- lockBeforeDate:](<lock(before_).md>) — Attempts to acquire a lock before a specified moment in time.
- [- lockWhenCondition:](<lock(whencondition_).md>) — Attempts to acquire a lock.
- [- lockWhenCondition:beforeDate:](<lock(whencondition_before_).md>) — Attempts to acquire a lock before a specified moment in time.
- [- tryLock](<try().md>) — Attempts to acquire a lock without regard to the receiver’s condition.
- [- tryLockWhenCondition:](<trylock(whencondition_).md>) — Attempts to acquire a lock if the receiver’s condition is equal to the specified condition.
