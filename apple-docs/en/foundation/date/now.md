---
title: now
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/now
source_url: 'https://developer.apple.com/documentation/foundation/date/now'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/now.json'
content_hash: 'sha256:1dd98c75ca78c6e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# now

<sub>Type Property</sub>

Returns a date instance that represents the current date and time, at the moment of access.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: macOS 12, iOS 15, tvOS 15, watchOS 8)
static var now: Date { get }
```

## Discussion

This property is equivalent to calling [init()](<init().md>). If you assign this value to a variable or property, the assigned value doesn’t automatically update as time passes.
