---
title: 'init(orPredicateWithSubpredicates:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscompoundpredicate/init(orpredicatewithsubpredicates:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscompoundpredicate/init(orpredicatewithsubpredicates:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscompoundpredicate/init%28orpredicatewithsubpredicates%3A%29.json'
content_hash: 'sha256:310cd7529555c858'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCompoundPredicate](../nscompoundpredicate.md)

# init(orPredicateWithSubpredicates:)

<sub>Initializer</sub>

Returns a new predicate that you form using an OR operation on the predicates in a specified array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(orPredicateWithSubpredicates subpredicates: [NSPredicate])
```

## Parameters

- `subpredicates` — An array of `NSPredicate` objects.

## Return Value

A new predicate formed by OR-ing the predicates specified by `subpredicates`.

## Discussion

An OR predicate with no subpredicates evaluates to FALSE.

### Special Considerations

For applications linked on macOS 10.5 or later, the `subpredicates` array is copied. For applications linked on OS X v10.4, the `subpredicates` array is retained (for binary compatibility).

## See Also

### Creating Compound Predicates

- [+ andPredicateWithSubpredicates:](<init(andpredicatewithsubpredicates_).md>) — Returns a new predicate that you form using an AND operation on the predicates in a specified array.
- [+ notPredicateWithSubpredicate:](<init(notpredicatewithsubpredicate_).md>) — Returns a new predicate that you form using a NOT operation on a specified predicate.
- [- initWithType:subpredicates:](<init(type_subpredicates_).md>) — Returns the receiver that a specified type initializes using predicates from a specified array.
- [- initWithCoder:](<init(coder_).md>) — Creates a predicate by decoding from the coder you specify.
