---
title: AttributeDynamicLookup
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedynamiclookup
source_url: 'https://developer.apple.com/documentation/foundation/attributedynamiclookup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedynamiclookup.json'
content_hash: 'sha256:e7d772cd158b6f16'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# AttributeDynamicLookup

<sub>Enumeration</sub>

A type to support dynamic member lookup of attributes and containers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@dynamicMemberLookup @frozen enum AttributeDynamicLookup
```

## Overview

This type allows attribute owners to add extensions that enable dynamic member lookup access to attributes. Supporting types — including [AttributedString](attributedstring.md), [AttributedSubstring](attributedsubstring.md), and [AttributeContainer](attributecontainer.md) — gain dynamic lookup support by extending this type.

You can enable dynamic member lookup for your own [AttributedStringKey](attributedstringkey.md) attributes by defining them as implementations, collecting them into an [AttributeScope](attributescope.md) and extending [AttributeDynamicLookup](attributedynamiclookup.md), like in the following example:

```swift
public extension AttributeDynamicLookup {
    subscript<T: AttributedStringKey>(dynamicMember keyPath: KeyPath<AttributeScopes.MyFrameworkAttributes, T>) -> T {
        return self[T.self]
    }
}
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md)

## Topics

### Accessing Key Values

- [subscript(_:)](<attributedynamiclookup/subscript(__).md>) — Returns an attributed string key that corresponds to a specified type.

### Accessing Framework Attribute Scopes

- [subscript(dynamicMember:)](<attributedynamiclookup/subscript(dynamicmember_)-3nor6.md>) — Returns the attributed string key for a specified Foundation key path.
- [subscript(dynamicMember:)](<attributedynamiclookup/subscript(dynamicmember_)-3neai.md>) — Returns the attributed string key for a specified Foundation number format key path.
- [subscript(dynamicMember:)](<attributedynamiclookup/subscript(dynamicmember_)-3q4ap.md>) — Returns the attributed string key for a specified SwiftUI key path.
- [subscript(dynamicMember:)](<attributedynamiclookup/subscript(dynamicmember_)-4yyyo.md>) — Returns the attributed string key for a specified UIKit key path.
- [subscript(dynamicMember:)](<attributedynamiclookup/subscript(dynamicmember_)-3v1cn.md>) — Returns the attributed string key for a specified AppKit key path.

### Subscripts

- [subscript(dynamicMember:)](<attributedynamiclookup/subscript(dynamicmember_)-30vmv.md>)
- [subscript(dynamicMember:)](<attributedynamiclookup/subscript(dynamicmember_)-3ft4y.md>)
- [subscript(dynamicMember:)](<attributedynamiclookup/subscript(dynamicmember_)-4n6dp.md>) — Provides dynamic member lookup for translation attributes.
- [subscript(dynamicMember:)](<attributedynamiclookup/subscript(dynamicmember_)-7vcf2.md>)

## See Also

### Using Defined Attributes

- [AttributeScopes](attributescopes.md) — Collections of attributes that system frameworks define.
- [ScopedAttributeContainer](scopedattributecontainer.md) — An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.
