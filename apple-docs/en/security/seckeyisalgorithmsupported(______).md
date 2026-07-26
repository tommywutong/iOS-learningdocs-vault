---
title: 'SecKeyIsAlgorithmSupported(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seckeyisalgorithmsupported(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeyisalgorithmsupported(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyisalgorithmsupported%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:f4f29ab94e4104a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyIsAlgorithmSupported(_:_:_:)

<sub>Function</sub>

Returns a Boolean indicating whether a key is suitable for an operation using a certain algorithm.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyIsAlgorithmSupported(_ key: SecKey, _ operation: SecKeyOperationType, _ algorithm: SecKeyAlgorithm) -> Bool
```

## Parameters

- `key` — The key whose suitability you want to test.

- `operation` — The operation that you want to perform with the key. Use one of the values from [SecKeyOperationType](seckeyoperationtype.md).

- `algorithm` — The algorithm that you want to perform with the key. Use one of the values from [SecKeyAlgorithm](seckeyalgorithm.md).

## Return Value

A Boolean indicating whether the key can be used for the given operation and algorithm.
