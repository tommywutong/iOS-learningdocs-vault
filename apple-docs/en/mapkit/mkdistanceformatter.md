---
title: MKDistanceFormatter
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdistanceformatter
source_url: 'https://developer.apple.com/documentation/mapkit/mkdistanceformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdistanceformatter.json'
content_hash: 'sha256:69634018a53db879'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKDistanceFormatter

<sub>Class</sub>

A utility object that converts between a geographic distance and a string-based expression of that distance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKDistanceFormatter
```

## Overview

Use a distance formatter to display distances to the user or to parse user-specified text to obtain a numerical value for a distance. When formatting strings containing distances, a distance formatter object takes into account the user’s locale and language settings. You can also specify a custom locale or custom units for any distances that you format.

## Relationships

- **Inherits From**: [Formatter](../foundation/formatter.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Converting distances

- [- stringFromDistance:](<mkdistanceformatter/string(fromdistance_).md>) — Creates a string representation of the specified distance.
- [- distanceFromString:](<mkdistanceformatter/distance(from_).md>) — Returns the distance value parsed from the specified string.

### Specifying the format

- [locale](mkdistanceformatter/locale.md) — The locale to use when formatting strings.
- [units](mkdistanceformatter/units-swift.property.md) — The measuring system — imperial or metric — to use for units.
- [Units](mkdistanceformatter/units-swift.enum.md) — Constants that reflect the type of units to use in the string.
- [unitStyle](mkdistanceformatter/unitstyle.md) — The preferred style for units.
- [DistanceUnitStyle](mkdistanceformatter/distanceunitstyle.md) — Constants that indicate the format style to use for strings.

## See Also

### Map coordinates

- [MKCoordinateRegion](mkcoordinateregion.md) — A rectangular geographic region that centers around a specific latitude and longitude.
- [MKCoordinateSpan](mkcoordinatespan.md) — The width and height of a map region.
- [MKMapRect](mkmaprect.md) — A rectangular area on a two-dimensional map projection.
- [MKMapPoint](mkmappoint.md) — A point on a two-dimensional map projection.
- [MKMapSize](mkmapsize.md) — Width and height information on a two-dimensional map projection.
