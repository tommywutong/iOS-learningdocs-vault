---
title: NSFetchRequestExpression
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequestexpression
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequestexpression'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequestexpression.json'
content_hash: 'sha256:90101ae482dc8552'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSFetchRequestExpression

<sub>Class</sub>

An expression that evaluates the result of a fetch request on a managed object context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSFetchRequestExpression
```

## Overview

`NSFetchRequestExpression` inherits from [NSExpression](../foundation/nsexpression.md), which provides most of the basic behavior. The first argument must be an expression which evaluates to an `NSFetchRequest` object, and the second must be an expression which evaluates to an `NSManagedObjectContext` object. If you simply want the count for the request, the `countOnly` argument should be [true](../swift/true.md).

## Relationships

- **Inherits From**: [NSExpression](../foundation/nsexpression.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Fetch Request Expression

- [+ expressionForFetch:context:countOnly:](<nsfetchrequestexpression/expression(forfetch_context_countonly_).md>) — Returns an expression which will evaluate to the result of executing a fetch request on a context.

### Examining a Fetch Request Expression

- [requestExpression](nsfetchrequestexpression/requestexpression.md) — The expression for the receiver’s fetch request.
- [contextExpression](nsfetchrequestexpression/contextexpression.md) — The expression for the receiver’s managed object context.
- [countOnlyRequest](nsfetchrequestexpression/iscountonlyrequest.md) — Returns a Boolean value that indicates whether the receiver represents a count-only fetch request.

### Constants

- [NSFetchRequestExpressionType](nsfetchrequestexpressiontype.md) — This constant specifies the fetch request expression type.

## See Also

### Specifying Fetch Constraints

- [predicate](nsfetchrequest/predicate.md) — The predicate of the fetch request.
- [fetchLimit](nsfetchrequest/fetchlimit.md) — The fetch limit of the fetch request.
- [fetchOffset](nsfetchrequest/fetchoffset.md) — The fetch offset of the fetch request.
- [fetchBatchSize](nsfetchrequest/fetchbatchsize.md) — The batch size of the objects specified in the fetch request.
- [affectedStores](nsfetchrequest/affectedstores.md) — An array of persistent stores specified for the fetch request.
- [NSExpressionDescription](nsexpressiondescription.md) — An object that describes an expression to include with a fetch request.
- [NSFetchedPropertyDescription](nsfetchedpropertydescription.md) — A description object used to define which properties are fetched from Core Data.
