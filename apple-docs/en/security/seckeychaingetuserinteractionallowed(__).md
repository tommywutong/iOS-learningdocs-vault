---
title: 'SecKeychainGetUserInteractionAllowed(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychaingetuserinteractionallowed(_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychaingetuserinteractionallowed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaingetuserinteractionallowed%28_%3A%29.json'
content_hash: 'sha256:23d56076904eca08'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainGetUserInteractionAllowed(_:)

<sub>Function</sub>

Indicates whether keychain services functions that normally display a user interaction are allowed to do so.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainGetUserInteractionAllowed(_ state: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus
```

## Parameters

- `state` — On return, a Boolean value indicating whether user interaction is permitted. If [true](../swift/true.md), user interaction is allowed, and keychain services functions that display a user interface can do so as appropriate.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
