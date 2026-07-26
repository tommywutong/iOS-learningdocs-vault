---
title: derivationExpression
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsderivedattributedescription/derivationexpression
source_url: 'https://developer.apple.com/documentation/coredata/nsderivedattributedescription/derivationexpression'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsderivedattributedescription/derivationexpression.json'
content_hash: 'sha256:40900495960e8c59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSDerivedAttributeDescription](../nsderivedattributedescription.md)

# derivationExpression

<sub>Instance Property</sub>

An expression for generating derived data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var derivationExpression: NSExpression? { get set }
```

## Discussion

When using derived attributes in an SQL store, this expression should be

- a keypath expression (including @operation components)

a function expression using one of the predefined functions defined in [NSExpression](../../foundation/nsexpression.md)

Any keypaths used in the expression must be accessible from the entity on which the derived attribute is specified.

If you try to add a store to a coordinator whose model contains derived attributes of a type not supported by the store, the add fails and throws an error.
