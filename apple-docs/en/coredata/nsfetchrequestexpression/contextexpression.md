---
title: contextExpression
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequestexpression/contextexpression
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequestexpression/contextexpression'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequestexpression/contextexpression.json'
content_hash: 'sha256:1ec53120319a4146'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequestExpression](../nsfetchrequestexpression.md)

# contextExpression

<sub>Instance Property</sub>

The expression for the receiver’s managed object context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var contextExpression: NSExpression { get }
```

## Discussion

The expression must evaluate to an [NSManagedObjectContext](../nsmanagedobjectcontext.md) object.

## See Also

### Examining a Fetch Request Expression

- [requestExpression](requestexpression.md) — The expression for the receiver’s fetch request.
- [countOnlyRequest](iscountonlyrequest.md) — Returns a Boolean value that indicates whether the receiver represents a count-only fetch request.
