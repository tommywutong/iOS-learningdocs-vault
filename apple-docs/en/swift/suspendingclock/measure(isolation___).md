---
title: 'measure(isolation:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/suspendingclock/measure(isolation:_:)'
source_url: 'https://developer.apple.com/documentation/swift/suspendingclock/measure(isolation:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/suspendingclock/measure%28isolation%3A_%3A%29.json'
content_hash: 'sha256:5fded5b471b19cae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SuspendingClock](../suspendingclock.md)

# measure(isolation:_:)

<sub>Instance Method</sub>

> [!warning] Deprecated
> Replaced by nonisolated(nonsending) overload

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func measure(isolation: isolated (any Actor)? = #isolation, _ work: () async throws -> Void) async rethrows -> Self.Instant.Duration
```
