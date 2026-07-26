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
doc_path: '/documentation/foundation/attributecontainer/subscript(dynamicmember:)-3jcvx'
source_url: 'https://developer.apple.com/documentation/foundation/attributecontainer/subscript(dynamicmember:)-3jcvx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributecontainer/subscript%28dynamicmember%3A%29-3jcvx.json'
content_hash: 'sha256:191d991f63313f55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeContainer](../attributecontainer.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Returns the attribute container that corresponds to a specified key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<S>(dynamicMember keyPath: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S> where S : AttributeScope { get set }
```

## Discussion

Use this subscript when you need to work with an explicit attribute scope. For example, the SwiftUI [foregroundColor](../attributescopes/swiftuiattributes/foregroundcolor.md) attribute overrides the attribute in the AppKit and UIKit scopes with the same name. If you work with both the SwiftUI and UIKit scopes, you can use the syntax `myAttributeContainer.uiKit.foregroundColor` to disambiguate and explicitly use the UIKit attribute.

## See Also

### Accessing Attributes

- [subscript(_:)](<subscript(__).md>) — Returns the attribute that corresponds to a specified key.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-657oj.md>) — Returns the attribute that corresponds to a specified key path.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-60ps5.md>) — Returns a modified attribute container as part of building a chain of attributes.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-swift.type.subscript.md>) — Returns a modified attribute container as part of building a chain of attributes, for use as a static method.
- [AttributedStringKey](../attributedstringkey.md) — A type that defines an attribute’s name and type.
- [Builder](builder.md) — A type that iteratively builds attribute containers by setting attribute values.
