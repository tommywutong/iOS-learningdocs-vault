---
title: setNeedsBodyUpdate()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/wkhostingcontroller/setneedsbodyupdate()
source_url: 'https://developer.apple.com/documentation/swiftui/wkhostingcontroller/setneedsbodyupdate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkhostingcontroller/setneedsbodyupdate%28%29.json'
content_hash: 'sha256:82fccd609adee66a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WKHostingController](../wkhostingcontroller.md)

# setNeedsBodyUpdate()

<sub>Instance Method</sub>

Invalidates the current SwiftUI views and triggers an update during the next cycle.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency func setNeedsBodyUpdate()
```

## Discussion

Call this method to mark the views of the hosting controller as needing an update. During the next update cycle, the hosting controller fetches an updated set of views from its [body](body.md) property.

## See Also

### Updating the root view

- [updateBodyIfNeeded()](<updatebodyifneeded().md>) — Updates the interface controller’s set of views immediately, if updates are pending.
