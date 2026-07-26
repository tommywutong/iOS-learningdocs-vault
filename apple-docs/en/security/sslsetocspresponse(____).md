---
title: 'SSLSetOCSPResponse(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 11.0+（13.0 起废弃）, iPadOS 11.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.13+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslsetocspresponse(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslsetocspresponse(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetocspresponse%28_%3A_%3A%29.json'
content_hash: 'sha256:695e0821b6df421b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetOCSPResponse(_:_:)

<sub>Function</sub>

Sets the OCSP response for the given SSL session.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLSetOCSPResponse(_ context: SSLContext, _ response: CFData) -> OSStatus
```

## Parameters

- `context` — A session context.

- `response` — A non-`NULL` [CFData](../corefoundation/cfdata.md) instance containing the bytes of the OCSP response.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).
