---
title: 'subscript(_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributecontainer/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributecontainer/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributecontainer/subscript%28_%3A%29.json'
content_hash: 'sha256:1dc4ea0995f26fd7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeContainer](../attributecontainer.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns the attribute that corresponds to a specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency subscript<T>(_: T.Type) -> T.Value? where T : AttributedStringKey, T.Value : Sendable { get set }
```

## See Also

### Accessing Attributes

- [subscript(dynamicMember:)](<subscript(dynamicmember_)-657oj.md>) — Returns the attribute that corresponds to a specified key path.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-3jcvx.md>) — Returns the attribute container that corresponds to a specified key path.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-60ps5.md>) — Returns a modified attribute container as part of building a chain of attributes.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-swift.type.subscript.md>) — Returns a modified attribute container as part of building a chain of attributes, for use as a static method.
- [AttributedStringKey](../attributedstringkey.md) — A type that defines an attribute’s name and type.
- [Builder](builder.md) — A type that iteratively builds attribute containers by setting attribute values.
