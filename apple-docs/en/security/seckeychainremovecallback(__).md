---
title: 'SecKeychainRemoveCallback(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainremovecallback(_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainremovecallback(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainremovecallback%28_%3A%29.json'
content_hash: 'sha256:ca16fa9fe5896fe1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainRemoveCallback(_:)

<sub>Function</sub>

Unregisters your keychain event callback function.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainRemoveCallback(_ callbackFunction: SecKeychainCallback) -> OSStatus
```

## Parameters

- `callbackFunction` — The callback function pointer to remove.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Once removed, keychain events are not sent to the owner of the callback.
