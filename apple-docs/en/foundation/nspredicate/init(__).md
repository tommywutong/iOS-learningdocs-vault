---
title: 'init(_:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspredicate/init(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspredicate/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspredicate/init%28_%3A%29.json'
content_hash: 'sha256:824359aef38cc559'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPredicate](../nspredicate.md)

# init(_:)

<sub>Initializer</sub>

Creates a predicate by converting an existing predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?<Input>(_ predicate: Predicate<Input>) where Input : NSObject
```

## Parameters

- `predicate` — The predicate to convert.

## Return Value

The converted predicate, or `nil` if conversion fails.

## Discussion

Only a subset of predicates that can be expressed by [Predicate](../predicate.md) are convertible to [NSPredicate](../nspredicate.md). Predicates that include operations like the following can’t be converted:

- Accessing key paths for properties that aren’t exposed to the Objective-C runtime.
- Capturing values of types that aren’t supported by `NSPredicate`, like custom Swift structures.
- Using some functions or operators, like performing collection operations on a nonstring value.

## See Also

### Creating a Predicate

- [+ predicateWithFormat:argumentArray:](<init(format_argumentarray_).md>) — Creates a predicate by substituting the values in a specified array into a format string and parsing the result.
- [+ predicateWithFormat:arguments:](<init(format_arguments_).md>) — Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [init(format:_:)](<init(format___).md>) — Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [- predicateWithSubstitutionVariables:](<withsubstitutionvariables(__).md>) — Returns a copy of the predicate and substitutes the predicates variables with specified values from a specified substitution variables dictionary.
- [+ predicateWithValue:](<init(value_).md>) — Creates and returns a predicate that always evaluates to a specified Boolean value.
- [+ predicateWithBlock:](<init(block_).md>) — Creates a predicate that evaluates using a specified block object and bindings dictionary.
- [+ predicateFromMetadataQueryString:](<init(frommetadataquerystring_).md>) — Creates a predicate with a metadata query string.
