---
title: kSecReturnData
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecreturndata
source_url: 'https://developer.apple.com/documentation/security/ksecreturndata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecreturndata.json'
content_hash: 'sha256:bfa24158bf70b3aa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecReturnData

<sub>Global Variable</sub>

A key whose value is a Boolean that indicates whether or not to return item data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecReturnData: CFString
```

## Discussion

The corresponding value is of type [CFBoolean](../corefoundation/cfboolean.md). A value of [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md) indicates that the function needs to return the item’s data as a [CFData](../corefoundation/cfdata.md) object.

For keys and password items, data is secret (encrypted) and might require the user to enter a password for access. For key items, the resulting data has the same format as the return value of the function [SecKeyCopyExternalRepresentation](<seckeycopyexternalrepresentation(____).md>). However, the key data might not be extractable (for example, if it’s protected by the Secure Enclave), so prefer to use [SecKeyCopyExternalRepresentation](<seckeycopyexternalrepresentation(____).md>) for keys and check the `error` parameter if it returns `nil`.
