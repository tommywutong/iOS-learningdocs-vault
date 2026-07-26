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
doc_path: '/documentation/os/osallocatedunfairlock/withlock(flags:_:)-u2xj'
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock/withlock(flags:_:)-u2xj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock/withlock%28flags%3A_%3A%29-u2xj.json'
content_hash: 'sha256:e0b4b3dcc6ec64cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSAllocatedUnfairLock](../osallocatedunfairlock.md)

# withLock(flags:_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withLock<R>(flags: OSAllocatedUnfairLockFlags, _ body: @Sendable () throws -> R) rethrows -> R where R : Sendable
```
