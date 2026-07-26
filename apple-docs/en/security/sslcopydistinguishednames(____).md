---
title: 'SSLCopyDistinguishedNames(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslcopydistinguishednames(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslcopydistinguishednames(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslcopydistinguishednames%28_%3A_%3A%29.json'
content_hash: 'sha256:7ec678badff892a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLCopyDistinguishedNames(_:_:)

<sub>Function</sub>

Retrieves the distinguished names of acceptable certification authorities.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLCopyDistinguishedNames(_ context: SSLContext, _ names: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `names` — On return, an array of `CFDataRef` objects, each representing one DER-encoded relative distinguished name of an acceptable certification authority. You must call the `CFRelease` function to release this array when you are finished with it.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

The list of distinguished names is provided by the server if the context reference represents a client; if the context reference represents a server, the list of distinguished names is specified with the [SSLSetCertificateAuthorities](<sslsetcertificateauthorities(______).md>) function.

The array retrieved by this function is suitable for use in finding a client identity (that is, a certificate and associated private key) that matches a server’s requirements.

## See Also

### Related Documentation

- [SSLSetCertificateAuthorities](<sslsetcertificateauthorities(______).md>) — Adds one or more certificates to a server’s list of certification authorities (CAs) acceptable for client authentication. _(deprecated)_
- [SSLCopyCertificateAuthorities](<sslcopycertificateauthorities(____).md>) — Retrieves the current list of certification authorities. _(deprecated)_
