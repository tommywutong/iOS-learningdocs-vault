---
title: 'SecCodeCreateWithXPCMessage(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccodecreatewithxpcmessage(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccodecreatewithxpcmessage(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodecreatewithxpcmessage%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:e912716c4c82088f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCodeCreateWithXPCMessage(_:_:_:)

<sub>Function</sub>

<sub>macOS</sub>

```swift
func SecCodeCreateWithXPCMessage(_ message: xpc_object_t, _ flags: SecCSFlags, _ target: UnsafeMutablePointer<SecCode?>) -> OSStatus
```
