---
title: Displaying an Indoor Map
framework: MapKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.6+, iPadOS 17.6+, Mac Catalyst 17.6+, Xcode 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/displaying-an-indoor-map
source_url: 'https://developer.apple.com/documentation/mapkit/displaying-an-indoor-map'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/displaying-an-indoor-map.json'
content_hash: 'sha256:4a3a0ff47a880fd3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md) · [MapKit for AppKit and UIKit](mapkit-for-appkit-and-uikit.md)

# Displaying an Indoor Map

<sub>Sample Code</sub>

Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest.

## Overview

The sample app demonstrates decoding, rendering, and styling of a small subset of the IMDF feature types and their properties. Use these examples to create your own indoor map with a style that’s consistent with your app’s design. You’ll need to handle feature categories that are specific to your venue, and configure the map style using your own colors, icons, and level picker.

> [!note] Note
> This sample code project is associated with WWDC 2019 session [241: Adding Indoor Maps to your App and Website](https://developer.apple.com/wwdc19/241).

## See Also

### Geographical features

- [MKGeoJSONDecoder](mkgeojsondecoder.md) — An object that decodes GeoJSON objects into MapKit types.
- [MKGeoJSONFeature](mkgeojsonfeature.md) — The decoded representation of a GeoJSON feature.
- [MKGeoJSONObject](mkgeojsonobject.md) — Objects that the GeoJSON decoder can return.

## Download

- [DisplayingAnIndoorMap.zip](https://docs-assets.developer.apple.com/published/bd14bb210dcb/DisplayingAnIndoorMap.zip)
