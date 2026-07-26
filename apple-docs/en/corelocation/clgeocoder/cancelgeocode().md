---
title: cancelGeocode()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（26.0 起废弃）, iPadOS 5.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.8+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）, watchOS 2.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clgeocoder/cancelgeocode()
source_url: 'https://developer.apple.com/documentation/corelocation/clgeocoder/cancelgeocode()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clgeocoder/cancelgeocode%28%29.json'
content_hash: 'sha256:2f0a93eae687d291'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLGeocoder](../clgeocoder.md)

# cancelGeocode()

<sub>Instance Method</sub>

Cancels a pending geocoding request.

> [!warning] Deprecated
> Use MKGeocodingRequest

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancelGeocode()
```

## Discussion

You can use this method to cancel a pending request and free up the resources associated with that request. Canceling a pending request causes the completion handler block to be called.

If the request is not pending, because it has already returned or has not yet begun, this method does nothing.

## See Also

### Managing geocoding requests

- [geocoding](isgeocoding.md) — A Boolean value indicating whether the receiver is in the middle of geocoding its value. _(deprecated)_
