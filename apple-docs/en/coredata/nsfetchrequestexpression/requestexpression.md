---
title: requestExpression
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequestexpression/requestexpression
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequestexpression/requestexpression'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequestexpression/requestexpression.json'
content_hash: 'sha256:f7f2f591c4502cc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequestExpression](../nsfetchrequestexpression.md)

# requestExpression

<sub>Instance Property</sub>

The expression for the receiver’s fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var requestExpression: NSExpression { get }
```

## Discussion

The expression must evaluate to an [NSFetchRequest](../nsfetchrequest.md) object.

## See Also

### Examining a Fetch Request Expression

- [contextExpression](contextexpression.md) — The expression for the receiver’s managed object context.
- [countOnlyRequest](iscountonlyrequest.md) — Returns a Boolean value that indicates whether the receiver represents a count-only fetch request.
