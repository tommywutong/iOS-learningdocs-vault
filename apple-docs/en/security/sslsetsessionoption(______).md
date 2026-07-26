---
title: 'SSLSetSessionOption(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+（13.0 起废弃）, iPadOS 5.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.6+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sslsetsessionoption(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sslsetsessionoption(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslsetsessionoption%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:b815088faffe6808'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLSetSessionOption(_:_:_:)

<sub>Function</sub>

Specifies options for a specific session.

> [!warning] Deprecated
> No longer supported. Use Network.framework.

<sub>Mac Catalyst, macOS</sub>

```swift
func SSLSetSessionOption(_ context: SSLContext, _ option: SSLSessionOption, _ value: Bool) -> OSStatus
```

## Parameters

- `context` — An SSL session context reference.

- `option` — An SSL session option. Possible values are listed in [SSLSessionOption](sslsessionoption.md).

- `value` — Set to [true](../swift/true.md) to enable the option, or [false](../swift/false.md) to disable it.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

This function must be called prior to the [SSLHandshake](<sslhandshake(__).md>) function; consequently, this function can be called only when no session is active.
