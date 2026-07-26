---
title: 'init(fromMetadataQueryString:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspredicate/init(frommetadataquerystring:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspredicate/init(frommetadataquerystring:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspredicate/init%28frommetadataquerystring%3A%29.json'
content_hash: 'sha256:07bfdacaa87c0c2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPredicate](../nspredicate.md)

# init(fromMetadataQueryString:)

<sub>Initializer</sub>

Creates a predicate with a metadata query string.

<sub>macOS</sub>

```swift
init?(fromMetadataQueryString queryString: String)
```

## Parameters

- `queryString` — A metadata query string.

## Discussion

For details of the format of the query string, see [File Metadata Query Expression Syntax](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/QueryFormat.html#//apple_ref/doc/uid/TP40001849).

## See Also

### Creating a Predicate

- [+ predicateWithFormat:argumentArray:](<init(format_argumentarray_).md>) — Creates a predicate by substituting the values in a specified array into a format string and parsing the result.
- [+ predicateWithFormat:arguments:](<init(format_arguments_).md>) — Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [init(format:_:)](<init(format___).md>) — Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [init(_:)](<init(__).md>) — Creates a predicate by converting an existing predicate.
- [- predicateWithSubstitutionVariables:](<withsubstitutionvariables(__).md>) — Returns a copy of the predicate and substitutes the predicates variables with specified values from a specified substitution variables dictionary.
- [+ predicateWithValue:](<init(value_).md>) — Creates and returns a predicate that always evaluates to a specified Boolean value.
- [+ predicateWithBlock:](<init(block_).md>) — Creates a predicate that evaluates using a specified block object and bindings dictionary.
