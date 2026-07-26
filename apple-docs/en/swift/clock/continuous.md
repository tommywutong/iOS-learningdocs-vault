---
title: continuous
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/clock/continuous
source_url: 'https://developer.apple.com/documentation/swift/clock/continuous'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/clock/continuous.json'
content_hash: 'sha256:0097186f84927655'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Clock](../clock.md)

# continuous

<sub>Type Property</sub>

A clock that measures time that always increments but does not stop incrementing while the system is asleep.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var continuous: ContinuousClock { get }
```

## Discussion

```swift
  try await Task.sleep(until: .now + .seconds(3), clock: .continuous)
```
