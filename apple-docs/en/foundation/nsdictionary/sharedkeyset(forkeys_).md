---
title: 'sharedKeySet(forKeys:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/sharedkeyset(forkeys:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/sharedkeyset(forkeys:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/sharedkeyset%28forkeys%3A%29.json'
content_hash: 'sha256:a7f3f3372e6be925'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# sharedKeySet(forKeys:)

<sub>Type Method</sub>

Creates a shared key set object for the specified keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func sharedKeySet(forKeys keys: [any NSCopying]) -> Any
```

## Parameters

- `keys` — The array of keys. If the parameter is nil, an exception is thrown. If the array of keys is empty, an empty key set is returned.

## Return Value

A shared key set object.

## Discussion

The array of `keys` may contain duplicates which are quietly ignored. Duplicate hash values of the keys are quietly allowed, but may cause lower performance and increase memory usage.

Typically you would create a shared key set for a given set of keys once, before creating shared key dictionaries, and retain and save the result of this method for use with the [NSMutableDictionary](../nsmutabledictionary.md) class method `dictionaryWithSharedKeySet:.`
