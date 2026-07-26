---
title: propagatesDeletesAtEndOfEvent
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/propagatesdeletesatendofevent
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/propagatesdeletesatendofevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/propagatesdeletesatendofevent.json'
content_hash: 'sha256:2457abc8f7df9232'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# propagatesDeletesAtEndOfEvent

<sub>Instance Property</sub>

A Boolean value that indicates whether the context propagates deletes at the end of the event in which a change was made.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var propagatesDeletesAtEndOfEvent: Bool { get set }
```

## Discussion

[true](../../swift/true.md) if the receiver propagates deletes at the end of the event in which a change was made, [false](../../swift/false.md) if it propagates deletes only during a save operation. The default is [true](../../swift/true.md).
