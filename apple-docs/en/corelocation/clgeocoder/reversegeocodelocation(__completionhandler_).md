---
title: 'reverseGeocodeLocation(_:completionHandler:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（26.0 起废弃）, iPadOS 5.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.8+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）, watchOS 2.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/clgeocoder/reversegeocodelocation(_:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/corelocation/clgeocoder/reversegeocodelocation(_:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clgeocoder/reversegeocodelocation%28_%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:fc006b160736c439'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLGeocoder](../clgeocoder.md)

# reverseGeocodeLocation(_:completionHandler:)

<sub>Instance Method</sub>

Submits a reverse-geocoding request for the specified location.

> [!warning] Deprecated
> Use MKReverseGeocodingRequest

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func reverseGeocodeLocation(_ location: CLLocation, completionHandler: @escaping @Sendable ([CLPlacemark]?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func reverseGeocodeLocation(_ location: CLLocation) async throws -> [CLPlacemark]
```

## Parameters

- `location` — The location object containing the coordinate data to look up.

- `completionHandler` — The handler block to execute with the results. The geocoder executes this handler regardless of whether the request was successful or unsuccessful. For more information on the format of this block, see [CLGeocodeCompletionHandler](../clgeocodecompletionhandler.md).

## Discussion

> [!important] Important
> You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func reverseGeocodeLocation(_ location: CLLocation) async throws -> [CLPlacemark]
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../swift/calling-objective-c-apis-asynchronously.md).

This method submits the specified location data to the geocoding server asynchronously and returns. When the request completes, the geocoder executes the provided completion handler on the main thread.

After initiating a reverse-geocoding request, do not attempt to initiate another reverse- or forward-geocoding request. Geocoding requests are rate-limited for each app, so making too many requests in a short period of time may cause some of the requests to fail. When the maximum rate is exceeded, the geocoder passes an error object with the value [kCLErrorNetwork](../clerror-swift.struct/code/network.md) to your completion handler.

## See Also

### Reverse geocoding a location

- [- reverseGeocodeLocation:preferredLocale:completionHandler:](<reversegeocodelocation(__preferredlocale_completionhandler_).md>) — Submits a reverse-geocoding request for the specified location and locale. _(deprecated)_
- [CLGeocodeCompletionHandler](../clgeocodecompletionhandler.md) — A block to be called when a geocoding request is complete.
