---
title: 'withLock(_:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osallocatedunfairlock/withlock(_:)-hple'
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock/withlock(_:)-hple'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock/withlock%28_%3A%29-hple.json'
content_hash: 'sha256:f459f13e21cc048c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSAllocatedUnfairLock](../osallocatedunfairlock.md)

# withLock(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withLock<R>(_ body: @Sendable () throws -> R) rethrows -> R where R : Sendable
```
