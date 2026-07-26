---
title: deferredCanceled
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clerror-swift.struct/deferredcanceled
source_url: 'https://developer.apple.com/documentation/corelocation/clerror-swift.struct/deferredcanceled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clerror-swift.struct/deferredcanceled.json'
content_hash: 'sha256:e9d3b70da96e6fd8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLError](../clerror-swift.struct.md)

# deferredCanceled

<sub>Type Property</sub>

A constant that indicates your app or the location manager canceled the request for deferred updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var deferredCanceled: CLError.Code { get }
```

## Discussion

This error is returned if you call the [- disallowDeferredLocationUpdates](<../cllocationmanager/disallowdeferredlocationupdates().md>) method or schedule a new deferred update before the previous deferred update request is processed. The location manager may also report this error too. For example, if the app is in the foreground when a new location is determined, the location manager cancels deferred updates and delivers the location data to your app.

## See Also

### Getting deferred location update errors

- [deferredFailed](deferredfailed.md) — A constant that indicates the location manager didn’t enter deferred mode for an unknown reason.
- [deferredAccuracyTooLow](deferredaccuracytoolow.md) — A constant that indicates deferred mode isn’t supported for the requested accuracy.
- [deferredDistanceFiltered](deferreddistancefiltered.md) — A constant that indicates deferred mode doesn’t support distance filters.
- [deferredNotUpdatingLocation](deferrednotupdatinglocation.md) — A constant that indicates the location manager didn’t enter deferred mode because location updates were already disabled or paused.
