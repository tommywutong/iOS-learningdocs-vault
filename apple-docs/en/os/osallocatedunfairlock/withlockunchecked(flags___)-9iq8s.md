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
doc_path: '/documentation/os/osallocatedunfairlock/withlockunchecked(flags:_:)-9iq8s'
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock/withlockunchecked(flags:_:)-9iq8s'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock/withlockunchecked%28flags%3A_%3A%29-9iq8s.json'
content_hash: 'sha256:f5f1ededea2bfb6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSAllocatedUnfairLock](../osallocatedunfairlock.md)

# withLockUnchecked(flags:_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withLockUnchecked<R>(flags: OSAllocatedUnfairLockFlags, _ body: () throws -> R) rethrows -> R
```
