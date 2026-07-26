---
title: lockDate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdistributedlock/lockdate
source_url: 'https://developer.apple.com/documentation/foundation/nsdistributedlock/lockdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdistributedlock/lockdate.json'
content_hash: 'sha256:2f7e043780cf8bc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDistributedLock](../nsdistributedlock.md)

# lockDate

<sub>Instance Property</sub>

Returns the time the receiver was acquired by any of the `NSDistributedLock` objects using the same path.

<sub>Mac Catalyst, macOS</sub>

```swift
var lockDate: Date { get }
```

## Return Value

The time the receiver was acquired by any of the `NSDistributedLock` objects using the same path. Returns `nil` if the lock doesn’t exist.

## Discussion

This method is potentially useful to applications that want to use an age heuristic to decide if a lock is too old and should be broken.

If the creation date on the lock isn’t the date on which you locked it, you’ve lost the lock: it’s been broken since you last checked it.
