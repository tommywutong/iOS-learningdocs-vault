---
title: isStationary
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationupdate/isstationary
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationupdate/isstationary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationupdate/isstationary.json'
content_hash: 'sha256:843abbdf997c797e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationUpdate](../cllocationupdate.md)

# isStationary

<sub>Instance Property</sub>

A Boolean value that indicates whether the user is stationary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isStationary: Bool { get }
```

## Discussion

Updates may stop flowing temporarily for several reasons including if the app is no longer authorized to receive location updates or if its location becomes unknown. If Core Location stops delivering updates because the device is stationary, then it sets `isStationary` to [true](../../swift/true.md); otherwise, it’s [false](../../swift/false.md).

If `isStationary` is [true](../../swift/true.md), the framework can suspend updates until the person starts moving, or their location becomes unknown.

## See Also

### Determining movement and location

- [location](location.md) — The user’s location, if available.
