---
title: 'init(value:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspredicate/init(value:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspredicate/init(value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspredicate/init%28value%3A%29.json'
content_hash: 'sha256:8f3dd385d4048b69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPredicate](../nspredicate.md)

# init(value:)

<sub>Initializer</sub>

Creates and returns a predicate that always evaluates to a specified Boolean value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(value: Bool)
```

## Parameters

- `value` — The Boolean value to which the new predicate should evaluate.

## Return Value

A predicate that always evaluates to `value`.

## See Also

### Creating a Predicate

- [+ predicateWithFormat:argumentArray:](<init(format_argumentarray_).md>) — Creates a predicate by substituting the values in a specified array into a format string and parsing the result.
- [+ predicateWithFormat:arguments:](<init(format_arguments_).md>) — Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [init(format:_:)](<init(format___).md>) — Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [init(_:)](<init(__).md>) — Creates a predicate by converting an existing predicate.
- [- predicateWithSubstitutionVariables:](<withsubstitutionvariables(__).md>) — Returns a copy of the predicate and substitutes the predicates variables with specified values from a specified substitution variables dictionary.
- [+ predicateWithBlock:](<init(block_).md>) — Creates a predicate that evaluates using a specified block object and bindings dictionary.
- [+ predicateFromMetadataQueryString:](<init(frommetadataquerystring_).md>) — Creates a predicate with a metadata query string.
