---
title: 'init(set:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/init(set:)-7a7ws'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/init(set:)-7a7ws'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/init%28set%3A%29-7a7ws.json'
content_hash: 'sha256:d3948f7abf598a08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# init(set:)

<sub>Initializer</sub>

Initializes a newly allocated set and adds to it objects from another given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc convenience init(set anSet: NSSet)
```

## Return Value

An initialized objects set containing the objects from `set`. The returned set might be different than the original receiver.
