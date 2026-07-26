---
title: NSExpressionDescription
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsexpressiondescription
source_url: 'https://developer.apple.com/documentation/coredata/nsexpressiondescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsexpressiondescription.json'
content_hash: 'sha256:89499c13b4cb9d5c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSExpressionDescription

<sub>Class</sub>

An object that describes an expression to include with a fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSExpressionDescription
```

## Overview

An expression description describes a value that a fetch request returns, which doesn’t appear as an attribute or relationship on an entity. For example, expressions can aggregate data, or  transform an attribute’s value. You add expression descriptions to a fetch request using the [propertiesToFetch](nsfetchrequest/propertiestofetch.md) method.

> [!important] Important
> Don’t add expression descriptions to the [properties](nsentitydescription/properties.md) array of [NSEntityDescription](nsentitydescription.md).

## Relationships

- **Inherits From**: [NSPropertyDescription](nspropertydescription.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the Expression Description

- [expression](nsexpressiondescription/expression.md) — The expression to evaluate.
- [resultType](nsexpressiondescription/resulttype.md) — The attribute type of the expression’s result.
- [expressionResultType](nsexpressiondescription/expressionresulttype.md) — The attribute type of the expression’s result. _(deprecated)_

### Deprecated

- [Deprecated Symbols](nsexpressiondescription-deprecated-symbols.md) — Review unsupported symbols and their replacements.

## See Also

### Specifying Fetch Constraints

- [predicate](nsfetchrequest/predicate.md) — The predicate of the fetch request.
- [fetchLimit](nsfetchrequest/fetchlimit.md) — The fetch limit of the fetch request.
- [fetchOffset](nsfetchrequest/fetchoffset.md) — The fetch offset of the fetch request.
- [fetchBatchSize](nsfetchrequest/fetchbatchsize.md) — The batch size of the objects specified in the fetch request.
- [affectedStores](nsfetchrequest/affectedstores.md) — An array of persistent stores specified for the fetch request.
- [NSFetchRequestExpression](nsfetchrequestexpression.md) — An expression that evaluates the result of a fetch request on a managed object context.
- [NSFetchedPropertyDescription](nsfetchedpropertydescription.md) — A description object used to define which properties are fetched from Core Data.
