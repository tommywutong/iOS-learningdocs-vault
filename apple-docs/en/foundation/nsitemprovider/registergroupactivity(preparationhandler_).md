---
title: 'registerGroupActivity(preparationHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/registergroupactivity(preparationhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registergroupactivity(preparationhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registergroupactivity%28preparationhandler%3A%29.json'
content_hash: 'sha256:16ee9f6f65dd29b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registerGroupActivity(preparationHandler:)

<sub>Instance Method</sub>

Registers a group activity instance asynchronously with the specified options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@nonobjc func registerGroupActivity<ActivityType>(preparationHandler: @escaping () async throws -> ActivityType) where ActivityType : GroupActivity
```

## Parameters

- `preparationHandler` — The handler the service invokes when it registers the `GroupActivity`.

## See Also

### Registering group activities

- [registerGroupActivity(_:)](<registergroupactivity(__).md>) — Registers a group activity instance with the specificed options.
