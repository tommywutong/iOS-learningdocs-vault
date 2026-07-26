---
title: 'init(block:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspredicate/init(block:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspredicate/init(block:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspredicate/init%28block%3A%29.json'
content_hash: 'sha256:9e8f609e88723b80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPredicate](../nspredicate.md)

# init(block:)

<sub>Initializer</sub>

Creates a predicate that evaluates using a specified block object and bindings dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(block: @escaping (Any?, [String : Any]?) -> Bool)
```

## Parameters

- `block` — The block is applied to the object to be evaluated. The block takes two arguments: - **evaluatedObject** — The object to be evaluated. - **bindings** — The substitution variables dictionary. The dictionary must contain key-value pairs for all variables in the receiver. The block returns [true](../../swift/true.md) if the `evaluatedObject` evaluates to true, otherwise [false](../../swift/false.md).

## Return Value

A new predicate by that evaluates objects using `block`.

## Discussion

In macOS 10.6 and later, Core Data supports block-based predicates in the in-memory and atomic stores, but not in the SQLite-based store.

## See Also

### Creating a Predicate

- [+ predicateWithFormat:argumentArray:](<init(format_argumentarray_).md>) — Creates a predicate by substituting the values in a specified array into a format string and parsing the result.
- [+ predicateWithFormat:arguments:](<init(format_arguments_).md>) — Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [init(format:_:)](<init(format___).md>) — Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [init(_:)](<init(__).md>) — Creates a predicate by converting an existing predicate.
- [- predicateWithSubstitutionVariables:](<withsubstitutionvariables(__).md>) — Returns a copy of the predicate and substitutes the predicates variables with specified values from a specified substitution variables dictionary.
- [+ predicateWithValue:](<init(value_).md>) — Creates and returns a predicate that always evaluates to a specified Boolean value.
- [+ predicateFromMetadataQueryString:](<init(frommetadataquerystring_).md>) — Creates a predicate with a metadata query string.
