---
title: 'tryLock(whenCondition:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsconditionlock/trylock(whencondition:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsconditionlock/trylock(whencondition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconditionlock/trylock%28whencondition%3A%29.json'
content_hash: 'sha256:ac7ed328ad913f5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConditionLock](../nsconditionlock.md)

# tryLock(whenCondition:)

<sub>Instance Method</sub>

Attempts to acquire a lock if the receiver’s condition is equal to the specified condition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryLock(whenCondition condition: Int) -> Bool
```

## Return Value

[true](../../swift/true.md) if the lock could be acquired, [false](../../swift/false.md) otherwise.

## Discussion

As part of its implementation, this method invokes [- lockWhenCondition:beforeDate:](<lock(whencondition_before_).md>). This method returns immediately.

## See Also

### Acquiring and Releasing a Lock

- [- lockBeforeDate:](<lock(before_).md>) — Attempts to acquire a lock before a specified moment in time.
- [- lockWhenCondition:](<lock(whencondition_).md>) — Attempts to acquire a lock.
- [- lockWhenCondition:beforeDate:](<lock(whencondition_before_).md>) — Attempts to acquire a lock before a specified moment in time.
- [- tryLock](<try().md>) — Attempts to acquire a lock without regard to the receiver’s condition.
- [- unlockWithCondition:](<unlock(withcondition_).md>) — Relinquishes the lock and sets the receiver’s condition.
