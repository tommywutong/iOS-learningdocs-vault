---
title: 'SecTrustGetNetworkFetchAllowed(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustgetnetworkfetchallowed(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustgetnetworkfetchallowed(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustgetnetworkfetchallowed%28_%3A_%3A%29.json'
content_hash: 'sha256:d18ef8a177462ae0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustGetNetworkFetchAllowed(_:_:)

<sub>Function</sub>

Indicates whether a trust evaluation is permitted to fetch missing intermediate certificates from the network.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustGetNetworkFetchAllowed(_ trust: SecTrust, _ allowFetch: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus
```

## Parameters

- `trust` — The trust evaluation object to query.

- `allowFetch` — A pointer to a Boolean that the function sets to true to indicate that the trust evaluation process is permitted to download missing certificates from the network, or false otherwise.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

By default, network fetch of missing certificates is enabled if the trust evaluation includes the SSL policy. Otherwise it is disabled.
