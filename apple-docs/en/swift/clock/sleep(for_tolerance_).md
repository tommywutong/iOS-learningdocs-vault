---
title: 'sleep(for:tolerance:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/clock/sleep(for:tolerance:)'
source_url: 'https://developer.apple.com/documentation/swift/clock/sleep(for:tolerance:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/clock/sleep%28for%3Atolerance%3A%29.json'
content_hash: 'sha256:cdd65ddf0f36da1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Clock](../clock.md)

# sleep(for:tolerance:)

<sub>Instance Method</sub>

Suspends for the given duration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sleep(for duration: Self.Instant.Duration, tolerance: Self.Instant.Duration? = nil) async throws
```

## Discussion

Prefer to use the `sleep(until:tolerance:)` method on `Clock` if you have access to an absolute instant.
