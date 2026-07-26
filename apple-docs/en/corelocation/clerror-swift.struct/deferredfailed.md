---
title: deferredFailed
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clerror-swift.struct/deferredfailed
source_url: 'https://developer.apple.com/documentation/corelocation/clerror-swift.struct/deferredfailed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clerror-swift.struct/deferredfailed.json'
content_hash: 'sha256:37a944951430d4be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLError](../clerror-swift.struct.md)

# deferredFailed

<sub>Type Property</sub>

A constant that indicates the location manager didn’t enter deferred mode for an unknown reason.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var deferredFailed: CLError.Code { get }
```

## Discussion

This error can occur if GPS is unavailable, not active, or is temporarily interrupted. If you get this error on a device that has GPS hardware, the solution is to try again.

## See Also

### Getting deferred location update errors

- [deferredCanceled](deferredcanceled.md) — A constant that indicates your app or the location manager canceled the request for deferred updates.
- [deferredAccuracyTooLow](deferredaccuracytoolow.md) — A constant that indicates deferred mode isn’t supported for the requested accuracy.
- [deferredDistanceFiltered](deferreddistancefiltered.md) — A constant that indicates deferred mode doesn’t support distance filters.
- [deferredNotUpdatingLocation](deferrednotupdatinglocation.md) — A constant that indicates the location manager didn’t enter deferred mode because location updates were already disabled or paused.
