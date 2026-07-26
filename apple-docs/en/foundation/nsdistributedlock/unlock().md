---
title: unlock()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdistributedlock/unlock()
source_url: 'https://developer.apple.com/documentation/foundation/nsdistributedlock/unlock()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdistributedlock/unlock%28%29.json'
content_hash: 'sha256:b6ab36ce2b8e1704'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDistributedLock](../nsdistributedlock.md)

# unlock()

<sub>Instance Method</sub>

Relinquishes the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func unlock()
```

## Discussion

You should generally use the [- unlock](<unlock().md>) method rather than [- breakLock](<break().md>) to release a lock.

An `NSGenericException` is raised if the receiver doesn’t already exist.

## See Also

### Relinquishing a Lock

- [- breakLock](<break().md>) — Forces the lock to be relinquished.
