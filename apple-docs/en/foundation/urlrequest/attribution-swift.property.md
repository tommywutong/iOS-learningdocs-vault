---
title: attribution
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlrequest/attribution-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/urlrequest/attribution-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlrequest/attribution-swift.property.json'
content_hash: 'sha256:a74b672a7ffb0573'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLRequest](../urlrequest.md)

# attribution

<sub>Instance Property</sub>

The entity that initiates the network request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var attribution: URLRequest.Attribution { get set }
```

## Discussion

If you don’t set this value, the system assumes a value of [NSURLRequestAttributionDeveloper](../nsurlrequest/attribution-swift.enum/developer.md). Use this default value for any network request that your app makes that isn’t explicitly from the user. This includes requests that you make to your own server, even when you load user data. It also includes links that the user selects, but that you modify in any way — including by adding HTTP headers — before loading the content.

Set this value to [NSURLRequestAttributionUser](../nsurlrequest/attribution-swift.enum/user.md) only for requests that the user explicitly makes, like when the user enters a URL or taps or clicks a URL that they can read, and only if your app loads and displays the data without altering the request.

## See Also

### Indicating the source of the request

- [Attribution](attribution-swift.typealias.md) — A type that indicates the entities that can make a network request.
