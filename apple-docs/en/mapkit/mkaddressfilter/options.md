---
title: MKAddressFilter.Options
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkaddressfilter/options
source_url: 'https://developer.apple.com/documentation/mapkit/mkaddressfilter/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkaddressfilter/options.json'
content_hash: 'sha256:ca2e20d2c8ca7102'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAddressFilter](../mkaddressfilter.md)

# MKAddressFilter.Options

<sub>Structure</sub>

A structure that contains options for filtering results in a search.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Options
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Creating a filter result

- [init(rawValue:)](<options/init(rawvalue_).md>) — Creates a filter options object.

### Getting search filter options

- [MKAddressFilterOptionAdministrativeArea](options/administrativearea.md) — The primary administrative divisions of countries or regions.
- [MKAddressFilterOptionCountry](options/country.md) — Countries and regions.
- [MKAddressFilterOptionLocality](options/locality.md) — Local administrative divisions, postal cities, and populated places.
- [MKAddressFilterOptionPostalCode](options/postalcode.md) — An address code for mail sorting and delivery.
- [MKAddressFilterOptionSubAdministrativeArea](options/subadministrativearea.md) — The secondary administrative divisions of countries or regions.
- [MKAddressFilterOptionSubLocality](options/sublocality.md) — Local administrative subdivisions, postal city subdistricts, and neighborhoods.
- [MKAddressFilterOptionAdministrativeArea](options/administrativearea.md) — The primary administrative divisions of countries or regions.
- [MKAddressFilterOptionCountry](options/country.md) — Countries and regions.
- [MKAddressFilterOptionLocality](options/locality.md) — Local administrative divisions, postal cities, and populated places.
- [MKAddressFilterOptionPostalCode](options/postalcode.md) — An address code for mail sorting and delivery.
- [MKAddressFilterOptionSubAdministrativeArea](options/subadministrativearea.md) — The secondary administrative divisions of countries or regions.
- [MKAddressFilterOptionSubLocality](options/sublocality.md) — Local administrative subdivisions, postal city subdistricts, and neighborhoods.

## See Also

### Local search

- [Interacting with nearby points of interest](../interacting-with-nearby-points-of-interest.md) — Provide automatic search completions for a partial search query, search the map for relevant locations nearby, and retrieve details for selected points of interest.
- [MKLocalSearchRegionPriority](../mklocalsearchregionpriority.md) — A value that indicates the importance of the configured region.
- [ResultType](../mklocalsearch/resulttype.md) — Options that indicate types of search results.
- [MKLocalSearch](../mklocalsearch.md) — A utility object for initiating map-based searches and processing the results.
- [MKAddressFilter](../mkaddressfilter.md) — An object that filters which address options to include or exclude in search results.
- [ResultType](../mklocalsearchcompleter/resulttype.md) — Options that indicate types of search completions.
- [MKLocalSearchCompleter](../mklocalsearchcompleter.md) — A utility object for generating a list of completion strings based on a partial search string that you provide.
- [MKLocalSearchCompletion](../mklocalsearchcompletion.md) — A fully formed string that completes a partial string.
- [MKLocalPointsOfInterestRequest](../mklocalpointsofinterestrequest.md) — A structured request to use when searching for points of interest.
