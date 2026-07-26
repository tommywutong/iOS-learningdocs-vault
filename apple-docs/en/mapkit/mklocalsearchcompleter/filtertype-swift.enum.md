---
title: MKLocalSearchCompleter.FilterType
framework: MapKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.3+（13.0 起废弃）, iPadOS 9.3+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.11.4+（10.15 起废弃）, tvOS 9.2+（13.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mklocalsearchcompleter/filtertype-swift.enum
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/filtertype-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchcompleter/filtertype-swift.enum.json'
content_hash: 'sha256:5f1517cfe78ae1e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearchCompleter](../mklocalsearchcompleter.md)

# MKLocalSearchCompleter.FilterType

<sub>Enumeration</sub>

Constants indicating the types of search completions to return.

> [!warning] Deprecated
> Use [ResultType](resulttype.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum FilterType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [MKSearchCompletionFilterTypeLocationsAndQueries](filtertype-swift.enum/locationsandqueries.md) — Points of interest and query suggestions. Specify this value when you want both map-based points of interest and common query terms used to find locations. For example, the search string `cof` yields a completion for _coffee_. _(deprecated)_
- [MKSearchCompletionFilterTypeLocationsOnly](filtertype-swift.enum/locationsonly.md) — Points of interest only. Specify this value when you want the search string to yield completions that correspond to a specific point-of-interest on the map. _(deprecated)_
- [MKSearchCompletionFilterTypeLocationsAndQueries](filtertype-swift.enum/locationsandqueries.md) — Points of interest and query suggestions. Specify this value when you want both map-based points of interest and common query terms used to find locations. For example, the search string `cof` yields a completion for _coffee_. _(deprecated)_
- [MKSearchCompletionFilterTypeLocationsOnly](filtertype-swift.enum/locationsonly.md) — Points of interest only. Specify this value when you want the search string to yield completions that correspond to a specific point-of-interest on the map. _(deprecated)_

### Initializers

- [init(rawValue:)](<filtertype-swift.enum/init(rawvalue_).md>) _(deprecated)_

## See Also

### Enumerations

- [MKMapType](../mkmaptype.md) — The type of map to display. _(deprecated)_
- [MKPinAnnotationColor](../mkpinannotationcolor.md) — The supported colors for pin annotations. _(deprecated)_
