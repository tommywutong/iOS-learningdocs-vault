---
title: 'calculateETA(completionHandler:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkdirections/calculateeta(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/calculateeta(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/calculateeta%28completionhandler%3A%29.json'
content_hash: 'sha256:189dd27adeae5895'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKDirections](../mkdirections.md)

# calculateETA(completionHandler:)

<sub>Instance Method</sub>

Begins calculating the requested travel-time information asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func calculateETA(completionHandler: @escaping @Sendable (MKDirections.ETAResponse?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func calculateETA() async throws -> MKDirections.ETAResponse
```

## Parameters

- `completionHandler` — The block to execute when the travel-time estimate is ready or when an error occurs. This parameter can’t be `nil`.

## Discussion

This method initiates a request for a travel-time estimate and calls your completion handler block with the results. Travel-time estimates take much less time to generate than directions, so use this method in situations where you want a time estimate only. The method executes your completion handler on your app’s main thread. The implementation of your handler needs to check for errors and then incorporate the response data as appropriate.

If you call this method while a previous request is in process, this method calls your completion handler with an error. You can determine whether a request is in process by checking the value of the [calculating](iscalculating.md) property. You can also cancel a request as necessary.

## See Also

### Getting the ETA

- [ETAHandler](etahandler.md) — The block to use for processing travel-time information.
- [ETAResponse](etaresponse.md) — The travel-time information that Apple servers return.
