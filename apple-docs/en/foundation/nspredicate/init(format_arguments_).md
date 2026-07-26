---
title: 'init(format:arguments:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspredicate/init(format:arguments:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspredicate/init(format:arguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspredicate/init%28format%3Aarguments%3A%29.json'
content_hash: 'sha256:d5783b1b1e6a0e69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPredicate](../nspredicate.md)

# init(format:arguments:)

<sub>Initializer</sub>

Creates a predicate by substituting the values in an argument list into a format string and parsing the result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(format predicateFormat: String, arguments argList: CVaListPointer)
```

## Parameters

- `predicateFormat` — The format string for the new predicate.

- `argList` — The arguments to substitute into `predicateFormat`. Values are substituted in the order they appear in the argument list.

## Return Value

A new predicate by substituting the values in `argList` into `predicateFormat` and parsing the result.

## Discussion

For details of the format of the format string and of limitations on variable substitution, see [Predicate Format String Syntax](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/Articles/pSyntax.html#//apple_ref/doc/uid/TP40001795).

## See Also

### Creating a Predicate

- [+ predicateWithFormat:argumentArray:](<init(format_argumentarray_).md>) — Creates a predicate by substituting the values in a specified array into a format string and parsing the result.
- [init(format:_:)](<init(format___).md>) — Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [init(_:)](<init(__).md>) — Creates a predicate by converting an existing predicate.
- [- predicateWithSubstitutionVariables:](<withsubstitutionvariables(__).md>) — Returns a copy of the predicate and substitutes the predicates variables with specified values from a specified substitution variables dictionary.
- [+ predicateWithValue:](<init(value_).md>) — Creates and returns a predicate that always evaluates to a specified Boolean value.
- [+ predicateWithBlock:](<init(block_).md>) — Creates a predicate that evaluates using a specified block object and bindings dictionary.
- [+ predicateFromMetadataQueryString:](<init(frommetadataquerystring_).md>) — Creates a predicate with a metadata query string.
