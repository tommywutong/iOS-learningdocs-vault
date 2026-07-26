---
title: SSLDisposeContext
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/ssldisposecontext
source_url: 'https://developer.apple.com/documentation/security/ssldisposecontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ssldisposecontext.json'
content_hash: 'sha256:2a4e57ec9639c809'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLDisposeContext

<sub>Function</sub>

Disposes of a Secure Sockets Layer (SSL) session context.

> [!warning] Deprecated
> You use this function to dispose of a context that you create with [SSLNewContext](sslnewcontext.md), but that function is deprecated. Instead, use [SSLCreateContext](<sslcreatecontext(______).md>) to create a new context and use [CFRelease](../corefoundation/cfrelease.md) to dispose of that context.

<sub>macOS</sub>

```objc
OSStatus SSLDisposeContext(SSLContextRef context);
```

## Parameters

- `context` — A reference to the SSL session context to dispose.

## Return Value

A result code. See [Secure Transport Result Codes](secure-transport-result-codes.md).

## Discussion

When you are completely finished with a secure session, you should dispose of the SSL session context in order to release the memory associated with the session.
