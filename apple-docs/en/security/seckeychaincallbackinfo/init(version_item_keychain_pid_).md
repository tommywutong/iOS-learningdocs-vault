---
title: 'init(version:item:keychain:pid:)'
framework: Security
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/security/seckeychaincallbackinfo/init(version:item:keychain:pid:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychaincallbackinfo/init(version:item:keychain:pid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaincallbackinfo/init%28version%3Aitem%3Akeychain%3Apid%3A%29.json'
content_hash: 'sha256:64a918e3c1262e32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainCallbackInfo](../seckeychaincallbackinfo.md)

# init(version:item:keychain:pid:)

<sub>Initializer</sub>

Creates a new keychain callback information structure.

<sub>macOS</sub>

```swift
init(version: UInt32, item: Unmanaged<SecKeychainItem>, keychain: Unmanaged<SecKeychain>, pid: pid_t)
```
