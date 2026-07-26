---
title: 'withLockUnchecked(_:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osallocatedunfairlock/withlockunchecked(_:)-7qywq'
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock/withlockunchecked(_:)-7qywq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock/withlockunchecked%28_%3A%29-7qywq.json'
content_hash: 'sha256:a4ef3a5251423263'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSAllocatedUnfairLock](../osallocatedunfairlock.md)

# withLockUnchecked(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withLockUnchecked<R>(_ body: (inout State) throws -> R) rethrows -> R
```
