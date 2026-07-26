---
title: 'withLockIfAvailable(_:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osallocatedunfairlock/withlockifavailable(_:)-1rp3w'
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock/withlockifavailable(_:)-1rp3w'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock/withlockifavailable%28_%3A%29-1rp3w.json'
content_hash: 'sha256:d6625a71963036a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSAllocatedUnfairLock](../osallocatedunfairlock.md)

# withLockIfAvailable(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withLockIfAvailable<R>(_ body: @Sendable () throws -> R) rethrows -> R? where R : Sendable
```
