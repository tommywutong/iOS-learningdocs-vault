---
title: MKPointOfInterestFilter
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkpointofinterestfilter
source_url: 'https://developer.apple.com/documentation/mapkit/mkpointofinterestfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpointofinterestfilter.json'
content_hash: 'sha256:0e052c4ad6d8c5ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKPointOfInterestFilter

<sub>Class</sub>

A filter that includes or excludes point of interest categories from a map view, local search, or local search completer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKPointOfInterestFilter
```

## Overview

You can apply a point of interest filter in a map view ([pointOfInterestFilter](mkmapview/pointofinterestfilter.md)), a local search request ([pointOfInterestFilter](mklocalsearchcompleter/pointofinterestfilter.md)), a search completer ([pointOfInterestFilter](mklocalsearchcompleter/pointofinterestfilter.md)), and in snapshot options ([pointOfInterestFilter](mkmapsnapshotter/options/pointofinterestfilter.md)).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating filters

- [filterExcludingAllCategories](mkpointofinterestfilter/excludingall.md) — A filter that excludes all point of interest categories.
- [filterIncludingAllCategories](mkpointofinterestfilter/includingall.md) — A filter that includes all point of interest categories.
- [- initExcludingCategories:](<mkpointofinterestfilter/init(excluding_).md>) — Initialize the point of interest filter with a list of categories to exclude.
- [- initIncludingCategories:](<mkpointofinterestfilter/init(including_).md>) — Initialize the point of interest filter with a list of categories to include.

### Querying filter behavior

- [- excludesCategory:](<mkpointofinterestfilter/excludes(__).md>) — Returns a Boolean value indicating whether the filter excludes the point of interest category.
- [- includesCategory:](<mkpointofinterestfilter/includes(__).md>) — Returns a Boolean value indicating whether the filter includes the point of interest category.

### Initializers

- [init(coder:)](<mkpointofinterestfilter/init(coder_).md>)
- [init(excludingCategories:)](<mkpointofinterestfilter/init(excludingcategories_).md>)
- [init(includingCategories:)](<mkpointofinterestfilter/init(includingcategories_).md>)

## See Also

### Points of interest

- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md) — Obtain information about a point of interest that persists over its lifetime.
- [MKMapFeatureAnnotation](mkmapfeatureannotation.md) — A class that describes an annotation element on the map’s display such as a point of interest, territorial boundary, or physical feature.
- [MKMapFeatureOptions](mkmapfeatureoptions.md) — A structure you use to tell the map which kinds of features users can interact with.
- [MKMapItemRequest](mkmapitemrequest.md) — A utility class you use to request additional information about a map feature.
- [MKIconStyle](mkiconstyle.md) — A class you use to customize the annotation view icon of a point of interest (POI) on the map.
- [MKPointOfInterestCategory](mkpointofinterestcategory.md) — A point of interest category.
