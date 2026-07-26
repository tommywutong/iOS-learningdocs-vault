---
title: 'withLockUnchecked(flags:_:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osallocatedunfairlock/withlockunchecked(flags:_:)-8cv64'
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock/withlockunchecked(flags:_:)-8cv64'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock/withlockunchecked%28flags%3A_%3A%29-8cv64.json'
content_hash: 'sha256:84e77499672dd8f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSAllocatedUnfairLock](../osallocatedunfairlock.md)

# withLockUnchecked(flags:_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withLockUnchecked<R>(flags: OSAllocatedUnfairLockFlags, _ body: (inout State) throws -> R) rethrows -> R
```
