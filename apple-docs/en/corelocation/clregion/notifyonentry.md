---
title: notifyOnEntry
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clregion/notifyonentry
source_url: 'https://developer.apple.com/documentation/corelocation/clregion/notifyonentry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clregion/notifyonentry.json'
content_hash: 'sha256:ecbcb496967aac8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLRegion](../clregion.md)

# notifyOnEntry

<sub>Instance Property</sub>

A Boolean indicating that notifications are generated upon entry into the region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var notifyOnEntry: Bool { get set }
```

## Discussion

When this property is [true](../../swift/true.md), a device crossing from outside the region to inside the region triggers the delivery of a notification. If the property is [false](../../swift/false.md), a notification is not generated. The default value of this property is [true](../../swift/true.md).

If the app is not running when a boundary crossing occurs, the system launches the app into the background to handle it. Upon launch, your app must configure new location manager and delegate objects to receive the notification. The notification is sent to your delegate’s [- locationManager:didEnterRegion:](<../cllocationmanagerdelegate/locationmanager(__didenterregion_).md>) method.

## See Also

### Specifying the notification conditions

- [notifyOnExit](notifyonexit.md) — A Boolean indicating that notifications are generated upon exit from the region.
