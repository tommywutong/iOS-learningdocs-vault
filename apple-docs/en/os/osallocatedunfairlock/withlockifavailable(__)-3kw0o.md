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
doc_path: '/documentation/os/osallocatedunfairlock/withlockifavailable(_:)-3kw0o'
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock/withlockifavailable(_:)-3kw0o'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock/withlockifavailable%28_%3A%29-3kw0o.json'
content_hash: 'sha256:bb1bf489cb0d9a91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSAllocatedUnfairLock](../osallocatedunfairlock.md)

# withLockIfAvailable(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withLockIfAvailable<R>(_ body: @Sendable (inout State) throws -> R) rethrows -> R? where R : Sendable
```
