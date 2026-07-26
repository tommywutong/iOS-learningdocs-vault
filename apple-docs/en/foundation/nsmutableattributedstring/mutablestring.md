---
title: mutableString
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutableattributedstring/mutablestring
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/mutablestring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/mutablestring.json'
content_hash: 'sha256:9eaaaabd4eb329f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# mutableString

<sub>Instance Property</sub>

The character contents of the receiver as a mutable string object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mutableString: NSMutableString { get }
```

## Return Value

The mutable string object.

## Discussion

The receiver tracks changes to this string and keeps its attribute mappings up to date.

## See Also

### Related Documentation

- [Attributed String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AttributedStrings/AttributedStrings.html#//apple_ref/doc/uid/10000036i)
