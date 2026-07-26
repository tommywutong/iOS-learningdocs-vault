---
title: CLError.Code.deferredAccuracyTooLow
framework: Core Location
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clerror-swift.struct/code/deferredaccuracytoolow
source_url: 'https://developer.apple.com/documentation/corelocation/clerror-swift.struct/code/deferredaccuracytoolow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clerror-swift.struct/code/deferredaccuracytoolow.json'
content_hash: 'sha256:ef36809ba98dc5cb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Location](../../../corelocation.md) · [CLError](../../clerror-swift.struct.md) · [Code](../code.md)

# CLError.Code.deferredAccuracyTooLow

<sub>Case</sub>

A constant that indicates deferred mode isn’t supported for the requested accuracy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case deferredAccuracyTooLow
```

## Discussion

The accuracy must be set to [kCLLocationAccuracyBest](../../kcllocationaccuracybest.md) or [kCLLocationAccuracyBestForNavigation](../../kcllocationaccuracybestfornavigation.md).

## See Also

### Getting deferred location update errors

- [kCLErrorDeferredFailed](deferredfailed.md) — A constant that indicates the location manager didn’t enter deferred mode for an unknown reason.
- [kCLErrorDeferredCanceled](deferredcanceled.md) — A constant that indicates your app or the location manager canceled the request for deferred updates.
- [kCLErrorDeferredDistanceFiltered](deferreddistancefiltered.md) — A constant that indicates deferred mode doesn’t support distance filters.
- [kCLErrorDeferredNotUpdatingLocation](deferrednotupdatinglocation.md) — A constant that indicates the location manager didn’t enter deferred mode because location updates were already disabled or paused.
