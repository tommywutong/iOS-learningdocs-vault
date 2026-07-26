---
title: CLError.Code
framework: Core Location
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clerror-swift.struct/code
source_url: 'https://developer.apple.com/documentation/corelocation/clerror-swift.struct/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clerror-swift.struct/code.json'
content_hash: 'sha256:bc28b8cf7ee08aea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLError](../clerror-swift.struct.md)

# CLError.Code

<sub>Enumeration</sub>

Error codes returned by the location manager object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Code
```

## Overview

Instances of [NSError](../../foundation/nserror.md) object delivered to the delegate use these error codes for the [code](../../foundation/nserror/code.md) property of the error object.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting general errors

- [kCLErrorLocationUnknown](code/locationunknown.md) — A constant that indicates the location manager was unable to obtain a location value right now.
- [kCLErrorDenied](code/denied.md) — A constant that indicates the user denied access to the location service.
- [kCLErrorPromptDeclined](code/promptdeclined.md) — A constant that indicates the user didn’t grant the requested temporary authorization.
- [kCLErrorNetwork](code/network.md) — A constant that indicates the network was unavailable or a network error occurred.
- [kCLErrorHeadingFailure](code/headingfailure.md) — A constant that indicates the location manager can’t determine the heading.
- [kCLErrorRangingUnavailable](code/rangingunavailable.md) — A constant that indicates ranging is disabled.
- [kCLErrorRangingFailure](code/rangingfailure.md) — A constant that indicates a general ranging error occurred.

### Getting region monitoring errors

- [kCLErrorRegionMonitoringDenied](code/regionmonitoringdenied.md) — A constant that indicates the user denied access to the region monitoring service.
- [kCLErrorRegionMonitoringFailure](code/regionmonitoringfailure.md) — A constant that indicates the location manager failed to monitor a registered region.
- [kCLErrorRegionMonitoringSetupDelayed](code/regionmonitoringsetupdelayed.md) — A constant that indicates Core Location failed to initialize the region monitoring feature.
- [kCLErrorRegionMonitoringResponseDelayed](code/regionmonitoringresponsedelayed.md) — A constant that indicates Core Location will deliver events but they may be delayed.

### Getting geocoding errors

- [kCLErrorGeocodeCanceled](code/geocodecanceled.md) — A constant that indicates the geocode request was canceled.
- [kCLErrorGeocodeFoundNoResult](code/geocodefoundnoresult.md) — A constant that indicates the geocode request yielded no result.
- [kCLErrorGeocodeFoundPartialResult](code/geocodefoundpartialresult.md) — A constant that indicates the geocode request yielded a partial result.

### Getting deferred location update errors

- [kCLErrorDeferredFailed](code/deferredfailed.md) — A constant that indicates the location manager didn’t enter deferred mode for an unknown reason.
- [kCLErrorDeferredCanceled](code/deferredcanceled.md) — A constant that indicates your app or the location manager canceled the request for deferred updates.
- [kCLErrorDeferredAccuracyTooLow](code/deferredaccuracytoolow.md) — A constant that indicates deferred mode isn’t supported for the requested accuracy.
- [kCLErrorDeferredDistanceFiltered](code/deferreddistancefiltered.md) — A constant that indicates deferred mode doesn’t support distance filters.
- [kCLErrorDeferredNotUpdatingLocation](code/deferrednotupdatinglocation.md) — A constant that indicates the location manager didn’t enter deferred mode because location updates were already disabled or paused.

### Enumeration cases

- [kCLErrorHistoricalLocationError](code/historicallocationerror.md)

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)

## See Also

### Getting general errors

- [locationUnknown](locationunknown.md) — A constant that indicates the location manager was unable to obtain a location value right now.
- [denied](denied.md) — A constant that indicates the user denied access to the location service.
- [promptDeclined](promptdeclined.md) — A constant that indicates the user didn’t grant the requested temporary authorization.
- [network](network.md) — A constant that indicates the network was unavailable or a network error occurred.
- [headingFailure](headingfailure.md) — A constant that indicates the location manager can’t determine the heading.
- [rangingUnavailable](rangingunavailable.md) — A constant that indicates ranging is disabled.
- [rangingFailure](rangingfailure.md) — A constant that indicates a general ranging error occurred.
