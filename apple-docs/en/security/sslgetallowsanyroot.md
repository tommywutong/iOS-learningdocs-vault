---
title: SSLGetAllowsAnyRoot
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslgetallowsanyroot
source_url: 'https://developer.apple.com/documentation/security/sslgetallowsanyroot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslgetallowsanyroot.json'
content_hash: 'sha256:53cba5633b63bf1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLGetAllowsAnyRoot

<sub>Function</sub>

Obtains a value specifying whether an unknown root is allowed.

> [!warning] Deprecated
> See the replacement procedure for allowing arbitrary root certificates in the deprecation summary of [SSLSetAllowsAnyRoot](sslsetallowsanyroot.md).

<sub>macOS</sub>

```objc
OSStatus SSLGetAllowsAnyRoot(SSLContextRef context, Boolean *anyRoot);
```

## Parameters

- `context` — An SSL session context reference.

- `anyRoot` — On return, a Boolean indicating the current setting of the `anyRoot` flag.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

Use the [SSLSetAllowsAnyRoot](sslsetallowsanyroot.md) function to set the value of the `anyRoot` flag. The effect and meaning of this flag is described in the discussion of the [SSLSetAllowsAnyRoot](sslsetallowsanyroot.md) function.
