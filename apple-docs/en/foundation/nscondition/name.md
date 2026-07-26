---
title: name
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscondition/name
source_url: 'https://developer.apple.com/documentation/foundation/nscondition/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscondition/name.json'
content_hash: 'sha256:08a3b349dee8b24d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCondition](../nscondition.md)

# name

<sub>Instance Property</sub>

The name of the condition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var name: String? { get set }
```

## Discussion

You can use a name string to identify a condition object within your code. Cocoa also uses this name as part of any error descriptions involving the condition.
