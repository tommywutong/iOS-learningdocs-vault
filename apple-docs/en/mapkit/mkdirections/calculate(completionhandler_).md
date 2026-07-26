---
title: 'calculate(completionHandler:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkdirections/calculate(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/calculate(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/calculate%28completionhandler%3A%29.json'
content_hash: 'sha256:665f70cbb584b6b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKDirections](../mkdirections.md)

# calculate(completionHandler:)

<sub>Instance Method</sub>

Begins calculating the requested route information asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func calculate(completionHandler: @escaping @Sendable (MKDirections.Response?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func calculate() async throws -> MKDirections.Response
```

## Parameters

- `completionHandler` — The block to execute when the directions are ready or when an error occurs. This parameter can’t be `nil`.

## Discussion

This method initiates the request for directions and calls your completion handler block with the results. The method executes your completion handler on your app’s main thread. The implementation of your handler needs to check for errors and then incorporate the response data as appropriate.

If you call this method while a previous request is in process, this method calls your completion handler with an error. You can determine whether a request is in process by checking the value of the [calculating](iscalculating.md) property. You can also cancel a request as necessary.

## See Also

### Related Documentation

- [calculating](iscalculating.md) — A Boolean value that indicates whether a request is in process.
- [- cancel](<cancel().md>) — Cancels a pending request.

### Getting the directions

- [DirectionsHandler](directionshandler.md) — The block to use for processing the requested route information.
- [Response](response.md) — The route information that Apple servers return in response to your request for directions.
