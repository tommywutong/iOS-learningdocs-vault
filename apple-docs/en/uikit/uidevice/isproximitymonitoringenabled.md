---
title: isProximityMonitoringEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidevice/isproximitymonitoringenabled
source_url: 'https://developer.apple.com/documentation/uikit/uidevice/isproximitymonitoringenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidevice/isproximitymonitoringenabled.json'
content_hash: 'sha256:14b349b42a2ac30b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDevice](../uidevice.md)

# isProximityMonitoringEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether proximity monitoring is enabled.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isProximityMonitoringEnabled: Bool { get set }
```

## Discussion

Enable proximity monitoring only when your application needs to be notified of changes to the proximity state. Otherwise, disable proximity monitoring. The default value is [false](../../swift/false.md).

Not all iOS devices have proximity sensors. To determine if proximity monitoring is available, attempt to enable it. If the value of the [proximityMonitoringEnabled](isproximitymonitoringenabled.md) property remains [false](../../swift/false.md), proximity monitoring isn’t available.

## See Also

### Using the proximity sensor

- [proximityState](proximitystate.md) — A Boolean value that indicates whether the proximity sensor is close to the user.
