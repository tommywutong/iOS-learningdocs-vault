---
title: 'subscript(dynamicMember:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributecontainer/subscript(dynamicmember:)-657oj'
source_url: 'https://developer.apple.com/documentation/foundation/attributecontainer/subscript(dynamicmember:)-657oj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributecontainer/subscript%28dynamicmember%3A%29-657oj.json'
content_hash: 'sha256:ec229a6dddbf7977'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeContainer](../attributecontainer.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Returns the attribute that corresponds to a specified key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency subscript<K>(dynamicMember keyPath: KeyPath<AttributeDynamicLookup, K>) -> K.Value? where K : AttributedStringKey, K.Value : Sendable { get set }
```

## See Also

### Accessing Attributes

- [subscript(_:)](<subscript(__).md>) — Returns the attribute that corresponds to a specified key.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-3jcvx.md>) — Returns the attribute container that corresponds to a specified key path.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-60ps5.md>) — Returns a modified attribute container as part of building a chain of attributes.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-swift.type.subscript.md>) — Returns a modified attribute container as part of building a chain of attributes, for use as a static method.
- [AttributedStringKey](../attributedstringkey.md) — A type that defines an attribute’s name and type.
- [Builder](builder.md) — A type that iteratively builds attribute containers by setting attribute values.
