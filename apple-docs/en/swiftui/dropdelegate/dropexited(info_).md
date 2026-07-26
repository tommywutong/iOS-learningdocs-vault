---
title: 'dropExited(info:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dropdelegate/dropexited(info:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dropdelegate/dropexited(info:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropdelegate/dropexited%28info%3A%29.json'
content_hash: 'sha256:429378d5f72e5268'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DropDelegate](../dropdelegate.md)

# dropExited(info:)

<sub>Instance Method</sub>

Tells the delegate a validated drop operation has exited the modified view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func dropExited(info: DropInfo)
```

## Discussion

The default implementation does nothing.

## Default Implementations

### DropDelegate Implementations

- [dropExited(info:)](<dropexited(info_)-7w9t2.md>) — Tells the delegate a validated drop operation has exited the modified view.

## See Also

### Receiving drop information

- [dropEntered(info:)](<dropentered(info_).md>) — Tells the delegate a validated drop has entered the modified view.
- [dropUpdated(info:)](<dropupdated(info_).md>) — Tells the delegate that a validated drop moved inside the modified view.
- [validateDrop(info:)](<validatedrop(info_).md>) — Tells the delegate that a drop containing items conforming to one of the expected types entered a view that accepts drops.
- [performDrop(info:)](<performdrop(info_).md>) — Tells the delegate it can request the item provider data from the given information.
