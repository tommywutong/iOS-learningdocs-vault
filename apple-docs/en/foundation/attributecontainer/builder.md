---
title: AttributeContainer.Builder
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributecontainer/builder
source_url: 'https://developer.apple.com/documentation/foundation/attributecontainer/builder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributecontainer/builder.json'
content_hash: 'sha256:29778a8f0bbfba96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeContainer](../attributecontainer.md)

# AttributeContainer.Builder

<sub>Structure</sub>

A type that iteratively builds attribute containers by setting attribute values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Builder<T> where T : AttributedStringKey
```

## Overview

The [Builder](builder.md) type lets you build [AttributeContainer](../attributecontainer.md) instances by chaining together several attributes in one expression. The following example shows this approach:

```swift
// An attribute container with the link and backgroundColor attributes.
let myContainer = AttributeContainer().link(myURL).backgroundColor(.yellow)
```

The first part of this expression, `AttributeContainer().link(URL(myURL))`, creates a builder to apply the [link](../attributescopes/foundationattributes/link.md) attribute to the empty [AttributeContainer](../attributecontainer.md). The builder’s [callAsFunction(_:)](<builder/callasfunction(__).md>) returns a new [AttributeContainer](../attributecontainer.md) with this attribute set. Then the `backgroundColor(.yellow)` creates a second builder to modify the just-returned [AttributeContainer](../attributecontainer.md) by adding the [backgroundColor](../attributescopes/swiftuiattributes/backgroundcolor.md) attribute. The result is an [AttributeContainer](../attributecontainer.md) with both attributes set.

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Calling Builder Functions

- [callAsFunction(_:)](<builder/callasfunction(__).md>) — Builds an attribute container by setting an attribute and returning a modified attribute container.

## See Also

### Accessing Attributes

- [subscript(_:)](<subscript(__).md>) — Returns the attribute that corresponds to a specified key.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-657oj.md>) — Returns the attribute that corresponds to a specified key path.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-3jcvx.md>) — Returns the attribute container that corresponds to a specified key path.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-60ps5.md>) — Returns a modified attribute container as part of building a chain of attributes.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-swift.type.subscript.md>) — Returns a modified attribute container as part of building a chain of attributes, for use as a static method.
- [AttributedStringKey](../attributedstringkey.md) — A type that defines an attribute’s name and type.
