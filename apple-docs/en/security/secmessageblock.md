---
title: SecMessageBlock
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secmessageblock
source_url: 'https://developer.apple.com/documentation/security/secmessageblock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secmessageblock.json'
content_hash: 'sha256:484fa0abe7885010'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecMessageBlock

<sub>Type Alias</sub>

A block that delivers messages during asynchronous operations.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias SecMessageBlock = (CFTypeRef?, CFError?, Bool) -> Void
```

## Parameters

- `message` — A CFType containing the message. This is where either intermediate or final results are returned.

- `error` — If an error occurred, this will contain a CFErrorRef, otherwise this will be NULL. If not NULL the caller is responsible for releasing the CFErrorRef.

- `isFinal` — If set the message returned is the final result otherwise it is an intermediate result.
