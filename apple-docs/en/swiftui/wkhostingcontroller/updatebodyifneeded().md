---
title: updateBodyIfNeeded()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/wkhostingcontroller/updatebodyifneeded()
source_url: 'https://developer.apple.com/documentation/swiftui/wkhostingcontroller/updatebodyifneeded()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkhostingcontroller/updatebodyifneeded%28%29.json'
content_hash: 'sha256:368d573d04b18496'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WKHostingController](../wkhostingcontroller.md)

# updateBodyIfNeeded()

<sub>Instance Method</sub>

Updates the interface controller’s set of views immediately, if updates are pending.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency func updateBodyIfNeeded()
```

## Discussion

Calling this method forces the hosting controller to update its current set of views, but only if there are pending changes. If there are no pending changes, this method does nothing.

To mark the interface controller as needing an update, call [setNeedsBodyUpdate()](<setneedsbodyupdate().md>).

## See Also

### Updating the root view

- [setNeedsBodyUpdate()](<setneedsbodyupdate().md>) — Invalidates the current SwiftUI views and triggers an update during the next cycle.
