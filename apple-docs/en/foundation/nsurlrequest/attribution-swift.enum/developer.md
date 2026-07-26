---
title: NSURLRequest.Attribution.developer
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/attribution-swift.enum/developer
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/attribution-swift.enum/developer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/attribution-swift.enum/developer.json'
content_hash: 'sha256:e3e709acb37203ac'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSURLRequest](../../nsurlrequest.md) · [Attribution](../attribution-swift.enum.md)

# NSURLRequest.Attribution.developer

<sub>Case</sub>

A developer-initiated network request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case developer
```

## Discussion

Use this value for the [attribution](../../urlrequest/attribution-swift.property.md) parameter of a URL request that your app makes for any purpose other than when the user explicitly accesses a link. This includes requests that your app makes to get user data. This is the default value.

For cases where the user enters a URL, like in the navigation bar of a web browser, or taps or clicks a URL to load the content it represents, use the [NSURLRequestAttributionUser](user.md) value instead.

## See Also

### Request sources

- [NSURLRequestAttributionUser](user.md) — The user explicitly directs the app to make a network request.
