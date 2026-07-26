---
title: 'init(dictionary:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/init(dictionary:)-4gc13'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/init(dictionary:)-4gc13'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/init%28dictionary%3A%29-4gc13.json'
content_hash: 'sha256:691bd65836ced214'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# init(dictionary:)

<sub>Initializer</sub>

Initializes a newly allocated dictionary and adds to it objects from another given dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@objc(__swiftInitWithDictionary_NSDictionary:) dynamic convenience init(dictionary otherDictionary: NSDictionary)
```

## Return Value

An initialized dictionary–which might be different than the original receiver–containing the keys and values found in `otherDictionary`.
