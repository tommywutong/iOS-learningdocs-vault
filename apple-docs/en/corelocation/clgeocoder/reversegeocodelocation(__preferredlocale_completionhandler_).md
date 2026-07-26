---
title: 'reverseGeocodeLocation(_:preferredLocale:completionHandler:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（26.0 起废弃）, iPadOS 11.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.13+（26.0 起废弃）, tvOS 11.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）, watchOS 4.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/clgeocoder/reversegeocodelocation(_:preferredlocale:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/corelocation/clgeocoder/reversegeocodelocation(_:preferredlocale:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clgeocoder/reversegeocodelocation%28_%3Apreferredlocale%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:5fb2834e73ff01e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLGeocoder](../clgeocoder.md)

# reverseGeocodeLocation(_:preferredLocale:completionHandler:)

<sub>Instance Method</sub>

Submits a reverse-geocoding request for the specified location and locale.

> [!warning] Deprecated
> Use MKReverseGeocodingRequest

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func reverseGeocodeLocation(_ location: CLLocation, preferredLocale locale: Locale?, completionHandler: @escaping @Sendable ([CLPlacemark]?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func reverseGeocodeLocation(_ location: CLLocation, preferredLocale locale: Locale?) async throws -> [CLPlacemark]
```

## Parameters

- `location` — The location object containing the coordinate data to look up.

- `locale` — The locale to use when returning the address information. You might specify a value for this parameter when you want the address returned in a locale that differs from the user’s current language settings. Specify `nil` to use the user’s default locale information.

- `completionHandler` — The handler block to execute with the results. The geocoder executes this handler regardless of whether the request was successful or unsuccessful. For more information on the format of this block, see [CLGeocodeCompletionHandler](../clgeocodecompletionhandler.md).

## Discussion

> [!important] Important
> You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func reverseGeocodeLocation(_ location: CLLocation, preferredLocale locale: Locale?) async throws -> [CLPlacemark]
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../swift/calling-objective-c-apis-asynchronously.md).

This method submits the specified location data to the geocoding server asynchronously and returns. When the request completes, the geocoder executes the provided completion handler on the main thread.

After initiating a reverse-geocoding request, do not attempt to initiate another reverse- or forward-geocoding request. Geocoding requests are rate-limited for each app, so making too many requests in a short period of time may cause some of the requests to fail. When the maximum rate is exceeded, the geocoder passes an error object with the value [network](../clerror-swift.struct/network.md) to your completion handler.

## See Also

### Reverse geocoding a location

- [- reverseGeocodeLocation:completionHandler:](<reversegeocodelocation(__completionhandler_).md>) — Submits a reverse-geocoding request for the specified location. _(deprecated)_
- [CLGeocodeCompletionHandler](../clgeocodecompletionhandler.md) — A block to be called when a geocoding request is complete.
