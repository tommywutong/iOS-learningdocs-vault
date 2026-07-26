---
title: 'geocodeAddressString(_:in:preferredLocale:completionHandler:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（26.0 起废弃）, iPadOS 11.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.13+（26.0 起废弃）, tvOS 11.0+（26.0 起废弃）, watchOS 4.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/clgeocoder/geocodeaddressstring(_:in:preferredlocale:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/corelocation/clgeocoder/geocodeaddressstring(_:in:preferredlocale:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clgeocoder/geocodeaddressstring%28_%3Ain%3Apreferredlocale%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:d5eb170b787682c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLGeocoder](../clgeocoder.md)

# geocodeAddressString(_:in:preferredLocale:completionHandler:)

<sub>Instance Method</sub>

Submits a forward-geocoding requesting using the specified address string and locale information.

> [!warning] Deprecated
> Use MKGeocodingRequest

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func geocodeAddressString(_ addressString: String, in region: CLRegion?, preferredLocale locale: Locale?, completionHandler: @escaping @Sendable ([CLPlacemark]?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func geocodeAddressString(_ addressString: String, in region: CLRegion?, preferredLocale locale: Locale?) async throws -> [CLPlacemark]
```

## Parameters

- `addressString` — A string describing the location you want to look up. For example, you could specify the string “1 Infinite Loop, Cupertino, CA” to locate Apple headquarters.

- `region` — A geographical region to use as a hint when looking up the specified address. Specifying a region lets you prioritize the returned set of results to locations that are close to some specific geographical area, which is typically the user’s current location. If the application is authorized for location services and you specify `nil` for this parameter, the set of results is prioritized based on the user’s approximate location. Calling this method does not trigger a location services authorization request.

- `locale` — The locale of the address string. Specify `nil` to use the current locale of the user.

- `completionHandler` — The handler block to execute with the results. The geocoder executes this handler regardless of whether the request was successful or unsuccessful. For more information on the format of this block, see [CLGeocodeCompletionHandler](../clgeocodecompletionhandler.md).

## Discussion

> [!important] Important
> You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func geocodeAddressString(_ addressString: String, in region: CLRegion?, preferredLocale locale: Locale?) async throws -> [CLPlacemark]
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../swift/calling-objective-c-apis-asynchronously.md).

This method submits the specified location data to the geocoding server asynchronously and returns. When the request completes, the geocoder executes the provided completion handler on the main thread.

After initiating a forward-geocoding request, do not attempt to initiate another reverse- or forward-geocoding request. Geocoding requests are rate-limited for each app, so making too many requests in a short period of time may cause some of the requests to fail. When the maximum rate is exceeded, the geocoder passes an error object with the value [network](../clerror-swift.struct/network.md) to your completion handler.

## See Also

### Geocoding an address

- [- geocodeAddressString:completionHandler:](<geocodeaddressstring(__completionhandler_).md>) — Submits a forward-geocoding request using the specified string. _(deprecated)_
- [- geocodeAddressString:inRegion:completionHandler:](<geocodeaddressstring(__in_completionhandler_).md>) — Submits a forward-geocoding request using the specified string and region information. _(deprecated)_
- [- geocodePostalAddress:completionHandler:](<geocodepostaladdress(__completionhandler_).md>) — Submits a forward-geocoding requesting using the specified Contacts framework information. _(deprecated)_
- [- geocodePostalAddress:preferredLocale:completionHandler:](<geocodepostaladdress(__preferredlocale_completionhandler_).md>) — Submits a forward-geocoding requesting using the specified locale and Contacts framework information. _(deprecated)_
- [- geocodeAddressDictionary:completionHandler:](<geocodeaddressdictionary(__completionhandler_).md>) — Submits a forward-geocoding request using the specified address dictionary. _(deprecated)_
