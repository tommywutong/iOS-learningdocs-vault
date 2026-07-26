---
title: 'SSLSetClientSideAuthenticate(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslsetclientsideauthenticate(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslsetclientsideauthenticate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetclientsideauthenticate%28_%3A_%3A%29.json'
content_hash: 'sha256:1e469528898555f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetClientSideAuthenticate(_:_:)

<sub>Function</sub>

Specifies the requirements for client-side authentication.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLSetClientSideAuthenticate(_ context: SSLContext, _ auth: SSLAuthenticate) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `auth` — A flag setting the requirements for client-side authentication. See [SSLAuthenticate](sslauthenticate.md) for possible values.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

This function can be called only by servers. Use of this function is optional. The default authentication requirement is [kNeverAuthenticate](sslauthenticate/neverauthenticate.md). This function may be called only when no session is active.
