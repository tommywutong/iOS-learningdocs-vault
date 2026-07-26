---
title: kCLErrorUserInfoAlternateRegionKey
framework: Core Location
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/kclerroruserinfoalternateregionkey
source_url: 'https://developer.apple.com/documentation/corelocation/kclerroruserinfoalternateregionkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/kclerroruserinfoalternateregionkey.json'
content_hash: 'sha256:9f32dfec97c53386'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# kCLErrorUserInfoAlternateRegionKey

<sub>Global Variable</sub>

A key in the user information dictionary of an error relating to a delayed region-monitoring response.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let kCLErrorUserInfoAlternateRegionKey: String
```

## Discussion

This key is included in an error of type [regionMonitoringResponseDelayed](clerror-swift.struct/regionmonitoringresponsedelayed.md). The value is a [CLRegion](clregion.md) object containing the region that location services can monitor more effectively.

## See Also

### Errors

- [CLError](clerror-swift.struct.md) — A Core Location error.
- [kCLErrorDomain](kclerrordomain.md) — The domain for Core Location errors.
