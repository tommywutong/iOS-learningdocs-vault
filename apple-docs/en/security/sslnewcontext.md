---
title: SSLNewContext
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sslnewcontext
source_url: 'https://developer.apple.com/documentation/security/sslnewcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslnewcontext.json'
content_hash: 'sha256:3a756c0c377ff392'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLNewContext

<sub>Function</sub>

Creates a new Secure Sockets Layer (SSL) session context.

> [!warning] Deprecated
> Use [SSLCreateContext](<sslcreatecontext(______).md>) instead.

<sub>macOS</sub>

```objc
OSStatus SSLNewContext(Boolean isServer, SSLContextRef*contextPtr);
```

## Parameters

- `isServer` — Set `true` if the calling process is a server.

- `contextPtr` — On return, points to a new SSL session context reference.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

The SSL session context is an opaque data structure that identifies a session and stores session information. You must pass this object to every other function in the Secure Transport API.
