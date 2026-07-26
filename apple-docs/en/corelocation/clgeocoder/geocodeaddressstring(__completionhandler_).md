---
title: 'geocodeAddressString(_:completionHandler:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（26.0 起废弃）, iPadOS 5.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.8+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）, watchOS 2.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/clgeocoder/geocodeaddressstring(_:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/corelocation/clgeocoder/geocodeaddressstring(_:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clgeocoder/geocodeaddressstring%28_%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:0ef935c5de5fb3a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLGeocoder](../clgeocoder.md)

# geocodeAddressString(_:completionHandler:)

<sub>Instance Method</sub>

Submits a forward-geocoding request using the specified string.

> [!warning] Deprecated
> Use MKGeocodingRequest

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func geocodeAddressString(_ addressString: String, completionHandler: @escaping @Sendable ([CLPlacemark]?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func geocodeAddressString(_ addressString: String) async throws -> [CLPlacemark]
```

## Parameters

- `addressString` — A string describing the location you want to look up. For example, you could specify the string “1 Infinite Loop, Cupertino, CA” to locate Apple headquarters.

- `completionHandler` — The handler block to execute with the results. The geocoder executes this handler regardless of whether the request was successful or unsuccessful. For more information on the format of this block, see [CLGeocodeCompletionHandler](../clgeocodecompletionhandler.md).

## Discussion

> [!important] Important
> You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func geocodeAddressString(_ addressString: String) async throws -> [CLPlacemark]
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../swift/calling-objective-c-apis-asynchronously.md).

This method submits the specified location data to the geocoding server asynchronously and returns. Your completion handler block will be executed on the main thread.

After initiating a forward-geocoding request, do not attempt to initiate another forward- or reverse-geocoding request. Geocoding requests are rate-limited for each app, so making too many requests in a short period of time may cause some of the requests to fail. When the maximum rate is exceeded, the geocoder passes an error object with the value [kCLErrorNetwork](../clerror-swift.struct/code/network.md) to your completion handler.

## See Also

### Geocoding an address

- [- geocodeAddressString:inRegion:preferredLocale:completionHandler:](<geocodeaddressstring(__in_preferredlocale_completionhandler_).md>) — Submits a forward-geocoding requesting using the specified address string and locale information. _(deprecated)_
- [- geocodeAddressString:inRegion:completionHandler:](<geocodeaddressstring(__in_completionhandler_).md>) — Submits a forward-geocoding request using the specified string and region information. _(deprecated)_
- [- geocodePostalAddress:completionHandler:](<geocodepostaladdress(__completionhandler_).md>) — Submits a forward-geocoding requesting using the specified Contacts framework information. _(deprecated)_
- [- geocodePostalAddress:preferredLocale:completionHandler:](<geocodepostaladdress(__preferredlocale_completionhandler_).md>) — Submits a forward-geocoding requesting using the specified locale and Contacts framework information. _(deprecated)_
- [- geocodeAddressDictionary:completionHandler:](<geocodeaddressdictionary(__completionhandler_).md>) — Submits a forward-geocoding request using the specified address dictionary. _(deprecated)_
