---
title: NSURLRequest.Attribution.user
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/attribution-swift.enum/user
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/attribution-swift.enum/user'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/attribution-swift.enum/user.json'
content_hash: 'sha256:13cfc62681ffd1af'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSURLRequest](../../nsurlrequest.md) · [Attribution](../attribution-swift.enum.md)

# NSURLRequest.Attribution.user

<sub>Case</sub>

The user explicitly directs the app to make a network request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case user
```

## Discussion

Use this value for the [attribution](../../urlrequest/attribution-swift.property.md) parameter of a URL request that satisfies a user request to access an explicit, unmodified URL. In all other cases, use the [NSURLRequestAttributionDeveloper](developer.md) value instead.

## See Also

### Request sources

- [NSURLRequestAttributionDeveloper](developer.md) — A developer-initiated network request.
