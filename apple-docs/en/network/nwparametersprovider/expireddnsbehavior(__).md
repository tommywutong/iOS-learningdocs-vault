---
title: 'expiredDNSBehavior(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparametersprovider/expireddnsbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwparametersprovider/expireddnsbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparametersprovider/expireddnsbehavior%28_%3A%29.json'
content_hash: 'sha256:de8d9ce84e78b221'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParametersProvider](../nwparametersprovider.md)

# expiredDNSBehavior(_:)

<sub>Instance Method</sub>

Allow or prohibit the use of expired DNS answers during connection establishment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func expiredDNSBehavior(_ behavior: NWParameters.ExpiredDNSBehavior) -> Self
```

## Parameters

- `behavior` — The expired DNS behavior to use.

## Discussion

If allowed, a DNS answer that was previously returned may be re-used for new connections even after the answers are considered expired. A query for fresh answers will be sent in parallel, and the fresh answers will be used as alternate addresses in case the expired answers do not result in successful connections.

By default, this value is `.systemDefault`, which allows the system to determine if it is appropriate to use expired answers.

## Default Implementations

### NWParametersProvider Implementations

- [expiredDNSBehavior(_:)](<expireddnsbehavior(__)-3w6lp.md>) — Allow or prohibit the use of expired DNS answers during connection establishment.
