---
title: 'SecKeyCreateWithData(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seckeycreatewithdata(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeycreatewithdata(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeycreatewithdata%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:adc70dc4ce49b50a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyCreateWithData(_:_:_:)

<sub>Function</sub>

Restores a key from an external representation of that key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyCreateWithData(_ keyData: CFData, _ attributes: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?
```

## Parameters

- `keyData` — Data representing the key. The format of the data depends on the type of key being created. See the description of the return value of the [SecKeyCopyExternalRepresentation](<seckeycopyexternalrepresentation(____).md>) function for details.

- `attributes` — A dictionary containing attributes describing the key to be imported. This dictionary must include at least the following keys: - [kSecAttrKeyType](ksecattrkeytype.md) - [kSecAttrKeyClass](ksecattrkeyclass.md)

- `error` — The address of a [CFError](../corefoundation/cferror.md) object. If an error occurs, this is set to point at an error instance that describes the failure.

## Return Value

The restored key or `NULL` on failure. In Objective-C, call [CFRelease](../corefoundation/cfrelease.md) to free the key’s memory when you are done with it.
