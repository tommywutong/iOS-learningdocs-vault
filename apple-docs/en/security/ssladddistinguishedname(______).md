---
title: 'SSLAddDistinguishedName(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.4+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/ssladddistinguishedname(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/ssladddistinguishedname(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ssladddistinguishedname%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:b85e3893d218e610'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLAddDistinguishedName(_:_:_:)

<sub>Function</sub>

Adds a DER-encoded distinguished name to a list of acceptable names to be specified in requests for client certificates.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLAddDistinguishedName(_ context: SSLContext, _ derDN: UnsafeRawPointer?, _ derDNLen: Int) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `derDN` — A pointer to a buffer containing a DER-encoded distinguished name.

- `derDNLen` — A value of type `size_t` representing the size of the buffer pointed to by the parameter `derDN`.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).
