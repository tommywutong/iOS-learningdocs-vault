---
title: 'init(coder:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscompoundpredicate/init(coder:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscompoundpredicate/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscompoundpredicate/init%28coder%3A%29.json'
content_hash: 'sha256:cf676efe67afb81a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCompoundPredicate](../nscompoundpredicate.md)

# init(coder:)

<sub>Initializer</sub>

Creates a predicate by decoding from the coder you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(coder: NSCoder)
```

## Parameters

- `coder` — The coder to read data from.

## See Also

### Creating Compound Predicates

- [+ andPredicateWithSubpredicates:](<init(andpredicatewithsubpredicates_).md>) — Returns a new predicate that you form using an AND operation on the predicates in a specified array.
- [+ notPredicateWithSubpredicate:](<init(notpredicatewithsubpredicate_).md>) — Returns a new predicate that you form using a NOT operation on a specified predicate.
- [+ orPredicateWithSubpredicates:](<init(orpredicatewithsubpredicates_).md>) — Returns a new predicate that you form using an OR operation on the predicates in a specified array.
- [- initWithType:subpredicates:](<init(type_subpredicates_).md>) — Returns the receiver that a specified type initializes using predicates from a specified array.
