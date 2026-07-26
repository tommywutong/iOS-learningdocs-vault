---
title: MKReverseGeocoderDelegate
framework: MapKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 3.0+（5.0 起废弃）, iPadOS 3.0+（5.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkreversegeocoderdelegate
source_url: 'https://developer.apple.com/documentation/mapkit/mkreversegeocoderdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkreversegeocoderdelegate.json'
content_hash: 'sha256:c8b8dda135b37560'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKReverseGeocoderDelegate

<sub>Protocol</sub>

Defines the interface for receiving messages from an [MKReverseGeocoder](mkreversegeocoder.md) object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@protocol MKReverseGeocoderDelegate <NSObject>
```

## Overview

You use this protocol to receive the placemark information for a given coordinate or to retrieve any errors that occurred during the reverse-geocoding process.

Delegates must implement both methods of this protocol.

The Google terms of service require that the reverse geocoding service be used in conjunction with a Google map; take this into account when designing your application’s user interface.

Each Map Kit application has a limited amount of reverse geocoding capacity, so it is to your advantage to use reverse geocode requests sparingly. For more information about when to initiate reverse-geocoding requests, see [MKReverseGeocoder](mkreversegeocoder.md).

This protocol is deprecated in iOS 5.0. Use the [CLGeocoder](../corelocation/clgeocoder.md) class instead.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Processing placemark searches

- [reverseGeocoder:didFindPlacemark:](mkreversegeocoderdelegate/reversegeocoder_didfindplacemark_.md) — Tells the delegate that a reverse geocoder successfully obtained placemark information for its coordinate. _(deprecated)_
- [reverseGeocoder:didFailWithError:](mkreversegeocoderdelegate/reversegeocoder_didfailwitherror_.md) — Tells the delegate that the specified reverse geocoder failed to obtain information about its coordinate. _(deprecated)_
