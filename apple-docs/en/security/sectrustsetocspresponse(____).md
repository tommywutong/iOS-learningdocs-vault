---
title: 'SecTrustSetOCSPResponse(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustsetocspresponse(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustsetocspresponse(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsetocspresponse%28_%3A_%3A%29.json'
content_hash: 'sha256:f26feec3e3bab46c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSetOCSPResponse(_:_:)

<sub>Function</sub>

Attaches Online Certificate Status Protocol (OSCP) response data to a trust object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecTrustSetOCSPResponse(_ trust: SecTrust, _ responseData: CFTypeRef?) -> OSStatus
```

## Parameters

- `trust` — The trust evaluation object to modify.

- `responseData` — Either a [CFData](../corefoundation/cfdata.md) object containing a single DER-encoded OCSPResponse (per [RFC2560](https://tools.ietf.org/html/rfc2560)), or a [CFArray](../corefoundation/cfarray.md) of these.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This function allows the caller to provide OCSPResponse data (which may be obtained during a TLS/SSL handshake, per [RFC3546](https://tools.ietf.org/html/rfc3546)) as input to a trust evaluation. If this data is available, it can obviate the need to contact an OCSP server for current revocation information.
