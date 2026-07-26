---
title: isStationary
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+（17.0 起废弃）, iPadOS 17.0+（17.0 起废弃）, Mac Catalyst 17.0+（17.0 起废弃）, macOS 14.0+（14.0 起废弃）, tvOS 17.0+（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 10.0+（10.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clupdate/isstationary
source_url: 'https://developer.apple.com/documentation/corelocation/clupdate/isstationary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clupdate/isstationary.json'
content_hash: 'sha256:487428e4587826d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLUpdate](../clupdate.md)

# isStationary

<sub>Instance Property</sub>

A Boolean value that indicates whether the device is stationary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly) BOOL isStationary;
```

## Discussion

Updates may stop flowing temporarily for several reasons including if the app is no longer authorized to receive location updates or if its location becomes unknown. If Core Location stops delivering updates because the device is stationary, then it sets `isStationary` to [true](../../swift/true.md); otherwise, it’s [false](../../swift/false.md).

If `isStationary` is [true](../../swift/true.md), then the framework can suspend updates until the person starts moving, or their location becomes unknown.

## See Also

### Update properties

- [location](location.md) — A person’s location, if available.
