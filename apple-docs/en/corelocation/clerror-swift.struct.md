---
title: CLError
framework: Core Location
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clerror-swift.struct
source_url: 'https://developer.apple.com/documentation/corelocation/clerror-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clerror-swift.struct.json'
content_hash: 'sha256:07019c72929acdae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLError

<sub>Structure</sub>

A Core Location error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CLError
```

## Overview

Instances of [NSError](../foundation/nserror.md) object delivered to the delegate use these error codes for the [code](../foundation/nserror/code.md) property of the error object.

## Relationships

- **Conforms To**: [CustomNSError](../foundation/customnserror.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting general errors

- [locationUnknown](clerror-swift.struct/locationunknown.md) — A constant that indicates the location manager was unable to obtain a location value right now.
- [denied](clerror-swift.struct/denied.md) — A constant that indicates the user denied access to the location service.
- [promptDeclined](clerror-swift.struct/promptdeclined.md) — A constant that indicates the user didn’t grant the requested temporary authorization.
- [network](clerror-swift.struct/network.md) — A constant that indicates the network was unavailable or a network error occurred.
- [headingFailure](clerror-swift.struct/headingfailure.md) — A constant that indicates the location manager can’t determine the heading.
- [rangingUnavailable](clerror-swift.struct/rangingunavailable.md) — A constant that indicates ranging is disabled.
- [rangingFailure](clerror-swift.struct/rangingfailure.md) — A constant that indicates a general ranging error occurred.
- [Code](clerror-swift.struct/code.md) — Error codes returned by the location manager object.

### Getting region monitoring errors

- [regionMonitoringDenied](clerror-swift.struct/regionmonitoringdenied.md) — A constant that indicates the user denied access to the region monitoring service.
- [regionMonitoringFailure](clerror-swift.struct/regionmonitoringfailure.md) — A constant that indicates the location manager failed to monitor a registered region.
- [regionMonitoringSetupDelayed](clerror-swift.struct/regionmonitoringsetupdelayed.md) — A constant that indicates Core Location couldn’t initialize the region monitoring feature immediately.
- [regionMonitoringResponseDelayed](clerror-swift.struct/regionmonitoringresponsedelayed.md) — A constant that indicates Core Location will deliver events but they may be delayed.

### Getting geocoding errors

- [geocodeCanceled](clerror-swift.struct/geocodecanceled.md) — A constant that indicates the geocode request was canceled.
- [geocodeFoundNoResult](clerror-swift.struct/geocodefoundnoresult.md) — A constant that indicates the geocode request yielded no result.
- [geocodeFoundPartialResult](clerror-swift.struct/geocodefoundpartialresult.md) — A constant that indicates the geocode request yielded a partial result.

### Getting deferred location update errors

- [deferredFailed](clerror-swift.struct/deferredfailed.md) — A constant that indicates the location manager didn’t enter deferred mode for an unknown reason.
- [deferredCanceled](clerror-swift.struct/deferredcanceled.md) — A constant that indicates your app or the location manager canceled the request for deferred updates.
- [deferredAccuracyTooLow](clerror-swift.struct/deferredaccuracytoolow.md) — A constant that indicates deferred mode isn’t supported for the requested accuracy.
- [deferredDistanceFiltered](clerror-swift.struct/deferreddistancefiltered.md) — A constant that indicates deferred mode doesn’t support distance filters.
- [deferredNotUpdatingLocation](clerror-swift.struct/deferrednotupdatinglocation.md) — A constant that indicates the location manager didn’t enter deferred mode because location updates were already disabled or paused.

### Getting the error details

- [alternateRegion](clerror-swift.struct/alternateregion.md) — A region that location services can monitor more effectively.

### Type Properties

- [historicalLocationError](clerror-swift.struct/historicallocationerror.md)
- [errorDomain](clerror-swift.struct/errordomain.md)

## See Also

### Errors

- [kCLErrorDomain](kclerrordomain.md) — The domain for Core Location errors.
- [kCLErrorUserInfoAlternateRegionKey](kclerroruserinfoalternateregionkey.md) — A key in the user information dictionary of an error relating to a delayed region-monitoring response.
