---
title: objCType
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsvalue/objctype
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/objctype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/objctype.json'
content_hash: 'sha256:fbd8b984b17fb9a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# objCType

<sub>Instance Property</sub>

A C string containing the Objective-C type of the data contained in the value object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var objCType: UnsafePointer<CChar> { get }
```

## Discussion

This property provides the same string produced by the `@encode()` compiler directive.

## See Also

### Working with Raw Values

- [- initWithBytes:objCType:](<init(bytes_objctype_).md>) — Initializes a value object to contain the specified value, interpreted with the specified Objective-C type.
- [+ value:withObjCType:](<init(__withobjctype_).md>) — Creates a value object containing the specified value, interpreted with the specified Objective-C type.
- [- getValue:](<getvalue(__).md>) — Copies the value into the specified buffer. _(deprecated)_
