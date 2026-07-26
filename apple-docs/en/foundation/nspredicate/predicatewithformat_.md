---
title: 'predicateWithFormat:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspredicate/predicatewithformat:'
source_url: 'https://developer.apple.com/documentation/foundation/nspredicate/predicatewithformat:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspredicate/predicatewithformat%3A.json'
content_hash: 'sha256:c92a7cd948181f72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPredicate](../nspredicate.md)

# predicateWithFormat:

<sub>Type Method</sub>

Creates and returns a new predicate formed by creating a new string with a specified format and parsing the result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSPredicate *) predicateWithFormat:(NSString *) predicateFormat;
```

## Parameters

- `predicateFormat` — The format string for the new predicate.

## Return Value

A new predicate formed by creating a new string with `format` and parsing the result.

## Discussion

Pass a comma-separated list of trailing variadic arguments to substitute into `format`.

For details of the format of the format string and of limitations on variable substitution, see [Predicate Format String Syntax](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/Articles/pSyntax.html#//apple_ref/doc/uid/TP40001795).

## See Also

### Related Documentation

- [Predicate Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789)

### Creating a Predicate

- [+ predicateWithFormat:argumentArray:](<init(format_argumentarray_).md>) — Creates a predicate by substituting the values in a specified array into a format string and parsing the result.
- [+ predicateWithFormat:arguments:](<init(format_arguments_).md>) — Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [- predicateWithSubstitutionVariables:](<withsubstitutionvariables(__).md>) — Returns a copy of the predicate and substitutes the predicates variables with specified values from a specified substitution variables dictionary.
- [+ predicateWithValue:](<init(value_).md>) — Creates and returns a predicate that always evaluates to a specified Boolean value.
- [+ predicateWithBlock:](<init(block_).md>) — Creates a predicate that evaluates using a specified block object and bindings dictionary.
- [+ predicateFromMetadataQueryString:](<init(frommetadataquerystring_).md>) — Creates a predicate with a metadata query string.
