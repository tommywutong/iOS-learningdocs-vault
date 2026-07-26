---
title: kSecAttrSynchronizableAny
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrsynchronizableany
source_url: 'https://developer.apple.com/documentation/security/ksecattrsynchronizableany'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrsynchronizableany.json'
content_hash: 'sha256:07669f9bbe1d48f9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrSynchronizableAny

<sub>Global Variable</sub>

Specifies that both synchronizable and non-synchronizable results should be returned from a query.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrSynchronizableAny: CFString
```

## Discussion

This may be used as a value for the [kSecAttrSynchronizable](ksecattrsynchronizable.md) dictionary key (in place of `kCFBooleanTrue` or `kCFBooleanFalse`) in a call to [SecItemCopyMatching](<secitemcopymatching(____).md>), [SecItemUpdate](<secitemupdate(____).md>), or [SecItemDelete](<secitemdelete(__).md>).
