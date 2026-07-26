---
title: cancel()
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdirections/cancel()
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/cancel%28%29.json'
content_hash: 'sha256:7fe705f253f523ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKDirections](../mkdirections.md)

# cancel()

<sub>Instance Method</sub>

Cancels a pending request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel()
```

## Discussion

After canceling a request, you can call the [- calculateDirectionsWithCompletionHandler:](<calculate(completionhandler_).md>) method again (if you want) to restart the request process.

## See Also

### Managing the request

- [calculating](iscalculating.md) — A Boolean value that indicates whether a request is in process.
