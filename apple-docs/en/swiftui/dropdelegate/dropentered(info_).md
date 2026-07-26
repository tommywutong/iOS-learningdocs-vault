---
title: 'dropEntered(info:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dropdelegate/dropentered(info:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dropdelegate/dropentered(info:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropdelegate/dropentered%28info%3A%29.json'
content_hash: 'sha256:43b8f57c5c0c8d43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DropDelegate](../dropdelegate.md)

# dropEntered(info:)

<sub>Instance Method</sub>

Tells the delegate a validated drop has entered the modified view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func dropEntered(info: DropInfo)
```

## Discussion

The default implementation does nothing.

## Default Implementations

### DropDelegate Implementations

- [dropEntered(info:)](<dropentered(info_)-2tqut.md>) — Tells the delegate a validated drop has entered the modified view.

## See Also

### Receiving drop information

- [dropExited(info:)](<dropexited(info_).md>) — Tells the delegate a validated drop operation has exited the modified view.
- [dropUpdated(info:)](<dropupdated(info_).md>) — Tells the delegate that a validated drop moved inside the modified view.
- [validateDrop(info:)](<validatedrop(info_).md>) — Tells the delegate that a drop containing items conforming to one of the expected types entered a view that accepts drops.
- [performDrop(info:)](<performdrop(info_).md>) — Tells the delegate it can request the item provider data from the given information.
