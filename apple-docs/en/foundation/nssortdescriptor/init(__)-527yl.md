---
title: 'init(_:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nssortdescriptor/init(_:)-527yl'
source_url: 'https://developer.apple.com/documentation/foundation/nssortdescriptor/init(_:)-527yl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssortdescriptor/init%28_%3A%29-527yl.json'
content_hash: 'sha256:edc9e145f6d0a6cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSortDescriptor](../nssortdescriptor.md)

# init(_:)

<sub>Initializer</sub>

Creates an `NSSortDescriptor` representing the same sort as the given `SortDescriptor`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 17, macOS 14, tvOS 17, watchOS 10)
convenience init<Compared>(_ sortDescriptor: SortDescriptor<Compared>) where Compared : NSObject
```

## Parameters

- `sortDescriptor` — The `SortDescriptor` to convert.
