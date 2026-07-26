---
title: 'withLock(flags:_:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osallocatedunfairlock/withlock(flags:_:)-1ub4c'
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock/withlock(flags:_:)-1ub4c'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock/withlock%28flags%3A_%3A%29-1ub4c.json'
content_hash: 'sha256:f87be2a8dc55e16b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSAllocatedUnfairLock](../osallocatedunfairlock.md)

# withLock(flags:_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withLock<R>(flags: OSAllocatedUnfairLockFlags, _ body: @Sendable (inout State) throws -> R) rethrows -> R where R : Sendable
```
