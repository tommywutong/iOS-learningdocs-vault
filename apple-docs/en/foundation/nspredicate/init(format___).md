---
title: 'init(format:_:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspredicate/init(format:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspredicate/init(format:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspredicate/init%28format%3A_%3A%29.json'
content_hash: 'sha256:f0d61b37d9b96273'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPredicate](../nspredicate.md)

# init(format:_:)

<sub>Initializer</sub>

Creates a predicate by substituting the values in an argument list into a format string and parsing the result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(format predicateFormat: String, _ args: any CVarArg...)
```

## Parameters

- `predicateFormat` — The format string for the new predicate.

- `args` — The arguments to substitute into `predicateFormat`.

## See Also

### Creating a Predicate

- [+ predicateWithFormat:argumentArray:](<init(format_argumentarray_).md>) — Creates a predicate by substituting the values in a specified array into a format string and parsing the result.
- [+ predicateWithFormat:arguments:](<init(format_arguments_).md>) — Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [init(_:)](<init(__).md>) — Creates a predicate by converting an existing predicate.
- [- predicateWithSubstitutionVariables:](<withsubstitutionvariables(__).md>) — Returns a copy of the predicate and substitutes the predicates variables with specified values from a specified substitution variables dictionary.
- [+ predicateWithValue:](<init(value_).md>) — Creates and returns a predicate that always evaluates to a specified Boolean value.
- [+ predicateWithBlock:](<init(block_).md>) — Creates a predicate that evaluates using a specified block object and bindings dictionary.
- [+ predicateFromMetadataQueryString:](<init(frommetadataquerystring_).md>) — Creates a predicate with a metadata query string.
