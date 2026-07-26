---
title: 'withLockIfAvailableUnchecked(_:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osallocatedunfairlock/withlockifavailableunchecked(_:)-15q0y'
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock/withlockifavailableunchecked(_:)-15q0y'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock/withlockifavailableunchecked%28_%3A%29-15q0y.json'
content_hash: 'sha256:37c525c3906ec109'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSAllocatedUnfairLock](../osallocatedunfairlock.md)

# withLockIfAvailableUnchecked(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withLockIfAvailableUnchecked<R>(_ body: (inout State) throws -> R) rethrows -> R?
```
