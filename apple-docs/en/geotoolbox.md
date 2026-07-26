---
title: GeoToolbox
framework: GeoToolbox
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/geotoolbox
source_url: 'https://developer.apple.com/documentation/geotoolbox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/geotoolbox.json'
content_hash: 'sha256:9f9510bc2eaae10b'
translated: false
---

> Navigation: [Technologies](technologies.md)

# GeoToolbox

<sub>Framework</sub>

Determine place descriptor information for map coordinates.

## Overview

Use `GeoToolbox` to create `PlaceDescriptor` structures for use across Maps technologies and third-party mapping systems.

## Topics

### Getting rich information about a place

- [PlaceDescriptor](geotoolbox/placedescriptor.md) — A structure that contains identifying information about a place that a mapping service may use to attempt to find rich place information such as phone numbers, websites, and so on.

### Creating a place descriptor

- [init(item:)](<geotoolbox/placedescriptor/init(item_).md>) — Creates a place descriptor from a map item.
- [init(representations:commonName:supportingRepresentations:)](<geotoolbox/placedescriptor/init(representations_commonname_supportingrepresentations_).md>) — Creates a place descriptor, suitable for use when searching or retrieving rich data about a place.

### Values that describe places and mapping service providers

- [PlaceRepresentation](geotoolbox/placedescriptor/placerepresentation.md) — Values that represent a physical place, suitable for use when searching or retrieving rich data.
- [SupportingPlaceRepresentation](geotoolbox/placedescriptor/supportingplacerepresentation.md) — Values that describe the representation of a physical place using proprietary attributes, such as an alphanumeric location identifier from a mapping service provider.
