---
title: 'SecKeyCopyAttributes(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seckeycopyattributes(_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeycopyattributes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeycopyattributes%28_%3A%29.json'
content_hash: 'sha256:b1b9a348731222e4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyCopyAttributes(_:)

<sub>Function</sub>

Gets the attributes of a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyCopyAttributes(_ key: SecKey) -> CFDictionary?
```

## Parameters

- `key` — The key whose attributes you want.

## Return Value

A dictionary containing the key’s attributes. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free this dictionary’s memory when you are done with it.
