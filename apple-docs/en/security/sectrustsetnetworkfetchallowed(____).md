---
title: 'SecTrustSetNetworkFetchAllowed(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustsetnetworkfetchallowed(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustsetnetworkfetchallowed(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsetnetworkfetchallowed%28_%3A_%3A%29.json'
content_hash: 'sha256:2efbab41ec4c682b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSetNetworkFetchAllowed(_:_:)

<sub>Function</sub>

Specifies whether a trust evaluation is permitted to fetch missing intermediate certificates from the network.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustSetNetworkFetchAllowed(_ trust: SecTrust, _ allowFetch: Bool) -> OSStatus
```

## Parameters

- `trust` — The trust evaluation object to modify.

- `allowFetch` — If true, and a certificate’s issuer is not present in the trust reference but its network location is known, the evaluation is permitted to attempt to download it automatically. Pass false to disable network fetch for this trust evaluation.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

By default, network fetch of missing certificates is enabled if the trust evaluation includes the SSL policy. Otherwise it is disabled.
