---
title: deleteRule
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsrelationshipdescription/deleterule
source_url: 'https://developer.apple.com/documentation/coredata/nsrelationshipdescription/deleterule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsrelationshipdescription/deleterule.json'
content_hash: 'sha256:6da2be015327d801'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSRelationshipDescription](../nsrelationshipdescription.md)

# deleteRule

<sub>Instance Property</sub>

The rule to apply when you delete the relationship’s owning managed object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var deleteRule: NSDeleteRule { get set }
```

## Discussion

The default value is [NSNullifyDeleteRule](../nsdeleterule/nullifydeleterule.md). For possible values, see [NSDeleteRule](../nsdeleterule.md).

## See Also

### Configuring Delete Behavior

- [NSDeleteRule](../nsdeleterule.md) — Constants that determine what happens when you delete a relationship’s owning managed object.
