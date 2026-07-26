---
title: 'registerGroupActivity(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/registergroupactivity(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registergroupactivity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registergroupactivity%28_%3A%29.json'
content_hash: 'sha256:39c41cca0606195a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registerGroupActivity(_:)

<sub>Instance Method</sub>

Registers a group activity instance with the specificed options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@nonobjc func registerGroupActivity<ActivityType>(_ activity: ActivityType) where ActivityType : GroupActivity
```

## Parameters

- `activity` — The `GroupActivity` to register.

## See Also

### Registering group activities

- [registerGroupActivity(preparationHandler:)](<registergroupactivity(preparationhandler_).md>) — Registers a group activity instance asynchronously with the specified options.
