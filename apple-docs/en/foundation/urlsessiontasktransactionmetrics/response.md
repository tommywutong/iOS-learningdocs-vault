---
title: response
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontasktransactionmetrics/response
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/response'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontasktransactionmetrics/response.json'
content_hash: 'sha256:cec53128700015b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskTransactionMetrics](../urlsessiontasktransactionmetrics.md)

# response

<sub>Instance Property</sub>

The transaction response.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var response: URLResponse? { get }
```

## Discussion

This property is `nil` if an error occurred and no response was generated.

## See Also

### Accessing request and response

- [request](request.md) — The transaction request.
