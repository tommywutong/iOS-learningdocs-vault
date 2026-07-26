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
doc_path: /documentation/swift/continuousclock/continuous
source_url: 'https://developer.apple.com/documentation/swift/continuousclock/continuous'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/continuousclock/continuous.json'
content_hash: 'sha256:9d649e58526a83be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ContinuousClock](../continuousclock.md)

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
