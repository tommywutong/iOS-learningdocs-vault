---
title: CLGeocodeCompletionHandler
framework: Core Location
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clgeocodecompletionhandler
source_url: 'https://developer.apple.com/documentation/corelocation/clgeocodecompletionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clgeocodecompletionhandler.json'
content_hash: 'sha256:c34b805b99136d92'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLGeocodeCompletionHandler

<sub>Type Alias</sub>

A block to be called when a geocoding request is complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CLGeocodeCompletionHandler = ([CLPlacemark]?, (any Error)?) -> Void
```

## Discussion

Upon completion of a geocoding request, a block of this form is called to give you a chance to process the results. The parameters of this block are as follows:

- **`placemark`** — Contains an array of [CLPlacemark](clplacemark.md) objects. For most geocoding requests, this array should contain only one entry. However, forward-geocoding requests may return multiple placemark objects in situations where the specified address could not be resolved to a single location.

If the request was canceled or there was an error in obtaining the placemark information, this parameter is `nil`.

- **`error`** — Contains `nil` or an error object indicating why the placemark data was not returned. For a list of possible error codes, see [Code](clerror-swift.struct/code.md).

## See Also

### Reverse geocoding a location

- [- reverseGeocodeLocation:preferredLocale:completionHandler:](<clgeocoder/reversegeocodelocation(__preferredlocale_completionhandler_).md>) — Submits a reverse-geocoding request for the specified location and locale. _(deprecated)_
- [- reverseGeocodeLocation:completionHandler:](<clgeocoder/reversegeocodelocation(__completionhandler_).md>) — Submits a reverse-geocoding request for the specified location. _(deprecated)_
