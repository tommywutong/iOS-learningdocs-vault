---
title: location
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clupdate/location
source_url: 'https://developer.apple.com/documentation/corelocation/clupdate/location'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clupdate/location.json'
content_hash: 'sha256:efb4cc73f7d012db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLUpdate](../clupdate.md)

# location

<sub>Instance Property</sub>

A person’s location, if available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) CLLocation * location;
```

## Discussion

If the location isn’t available, the value is `nil`.

## See Also

### Update properties

- [isStationary](isstationary.md) — A Boolean value that indicates whether the device is stationary. _(deprecated)_
