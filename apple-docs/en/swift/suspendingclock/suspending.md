---
title: suspending
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/suspendingclock/suspending
source_url: 'https://developer.apple.com/documentation/swift/suspendingclock/suspending'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/suspendingclock/suspending.json'
content_hash: 'sha256:4a643413cb68bda4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SuspendingClock](../suspendingclock.md)

# suspending

<sub>Type Property</sub>

A clock that measures time that always increments but stops incrementing while the system is asleep.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var suspending: SuspendingClock { get }
```

## Discussion

```swift
  try await Task.sleep(until: .now + .seconds(3), clock: .suspending)
```
