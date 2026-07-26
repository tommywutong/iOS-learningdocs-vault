---
title: 'init(addressString:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkgeocodingrequest/init(addressstring:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkgeocodingrequest/init(addressstring:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgeocodingrequest/init%28addressstring%3A%29.json'
content_hash: 'sha256:c7c5dcf63003babf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKGeocodingRequest](../mkgeocodingrequest.md)

# init(addressString:)

<sub>Initializer</sub>

Initializes a new geocoder request object with the provided address string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(addressString: String)
```

## Parameters

- `addressString` — An address string.

## Return Value

An initialized geocoder, or `nil` if the provided `addressString` is empty.
