---
title: ScopedAttributeContainer
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/scopedattributecontainer
source_url: 'https://developer.apple.com/documentation/foundation/scopedattributecontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/scopedattributecontainer.json'
content_hash: 'sha256:583af5d3f501c671'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ScopedAttributeContainer

<sub>Structure</sub>

An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@dynamicMemberLookup struct ScopedAttributeContainer<S> where S : AttributeScope
```

## Overview

Use a [ScopedAttributeContainer](scopedattributecontainer.md) when you need to disambiguate between attributes that exist in several attribute scopes that your app uses.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing Attribute Keys

- [subscript(dynamicMember:)](<scopedattributecontainer/subscript(dynamicmember_).md>) — Returns the value of the attribute that the specified key path indicates.

## See Also

### Using Defined Attributes

- [AttributeScopes](attributescopes.md) — Collections of attributes that system frameworks define.
- [AttributeDynamicLookup](attributedynamiclookup.md) — A type to support dynamic member lookup of attributes and containers.
