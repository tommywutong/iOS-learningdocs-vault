---
title: break()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdistributedlock/break()
source_url: 'https://developer.apple.com/documentation/foundation/nsdistributedlock/break()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdistributedlock/break%28%29.json'
content_hash: 'sha256:5a73daf58cf0e79a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDistributedLock](../nsdistributedlock.md)

# break()

<sub>Instance Method</sub>

Forces the lock to be relinquished.

<sub>Mac Catalyst, macOS</sub>

```swift
func `break`()
```

## Discussion

This method always succeeds unless the lock has been damaged. If another process has already unlocked or broken the lock, this method has no effect. You should generally use [- unlock](<unlock().md>) rather than [- breakLock](<break().md>) to relinquish a lock.

> [!warning] Warning
> Because `breakLock` can release another process’s lock, it should be used with great caution.

Even if you break a lock, there’s no guarantee that you will then be able to acquire the lock—another process might get it before your [- tryLock](<try().md>) is invoked.

Raises an `NSGenericException` if the lock could not be removed.

## See Also

### Relinquishing a Lock

- [- unlock](<unlock().md>) — Relinquishes the receiver.
