---
title: 'init(center:radius:identifier:)'
framework: Core Location
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/clcircularregion/init(center:radius:identifier:)'
source_url: 'https://developer.apple.com/documentation/corelocation/clcircularregion/init(center:radius:identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clcircularregion/init%28center%3Aradius%3Aidentifier%3A%29.json'
content_hash: 'sha256:94785ef7796db873'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLCircularRegion](../clcircularregion.md)

# init(center:radius:identifier:)

<sub>Initializer</sub>

Creates and returns a region object defining a circular geographic area.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
init(center: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String)
```

## Parameters

- `center` — The center point of the geographic region to monitor.

- `radius` — The distance (measured in meters) from the center point of the geographic region to the edge of the circular boundary.

- `identifier` — A unique identifier to associate with the region object. You use this identifier to differentiate regions within your app. This value can’t be `nil`.

## Return Value

An initialized region object.

## Discussion

When defining a geographic region, remember that the location manager doesn’t generate notifications immediately upon crossing a region boundary. Instead, it applies time and distance criteria to ensure that the crossing is intentional and needs to trigger a notification. So choose a center point and radius that are appropriate and give you enough time to alert the user. For more information, see the information about region monitoring in [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497).
