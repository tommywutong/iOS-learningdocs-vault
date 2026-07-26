---
title: 'withSubstitutionVariables(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspredicate/withsubstitutionvariables(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspredicate/withsubstitutionvariables(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspredicate/withsubstitutionvariables%28_%3A%29.json'
content_hash: 'sha256:ab9653d9df4e59fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPredicate](../nspredicate.md)

# withSubstitutionVariables(_:)

<sub>Instance Method</sub>

Returns a copy of the predicate and substitutes the predicates variables with specified values from a specified substitution variables dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withSubstitutionVariables(_ variables: [String : Any]) -> Self
```

## Parameters

- `variables` — The substitution variables dictionary. The dictionary must contain key-value pairs for all variables in the receiver.

## Return Value

A copy of the receiver with the predicate’s variables substituted by values specified in `variables`.

## Discussion

The predicate itself is not modified by this method, so you can reuse it for any number of substitutions.

## See Also

### Creating a Predicate

- [+ predicateWithFormat:argumentArray:](<init(format_argumentarray_).md>) — Creates a predicate by substituting the values in a specified array into a format string and parsing the result.
- [+ predicateWithFormat:arguments:](<init(format_arguments_).md>) — Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [init(format:_:)](<init(format___).md>) — Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [init(_:)](<init(__).md>) — Creates a predicate by converting an existing predicate.
- [+ predicateWithValue:](<init(value_).md>) — Creates and returns a predicate that always evaluates to a specified Boolean value.
- [+ predicateWithBlock:](<init(block_).md>) — Creates a predicate that evaluates using a specified block object and bindings dictionary.
- [+ predicateFromMetadataQueryString:](<init(frommetadataquerystring_).md>) — Creates a predicate with a metadata query string.
