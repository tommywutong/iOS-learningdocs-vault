---
title: 'dropUpdated(info:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dropdelegate/dropupdated(info:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dropdelegate/dropupdated(info:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropdelegate/dropupdated%28info%3A%29.json'
content_hash: 'sha256:15656a40daf7080d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DropDelegate](../dropdelegate.md)

# dropUpdated(info:)

<sub>Instance Method</sub>

Tells the delegate that a validated drop moved inside the modified view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func dropUpdated(info: DropInfo) -> DropProposal?
```

## Discussion

Use this method to return a drop proposal containing the operation the delegate intends to perform at the drop [location](../dropinfo/location.md). The default implementation of this method returns `nil`, which tells the drop to use the last valid returned value or else [DropOperation.copy](../dropoperation/copy.md).

## Default Implementations

### DropDelegate Implementations

- [dropUpdated(info:)](<dropupdated(info_)-2mktz.md>) — Tells the delegate that a validated drop moved inside the modified view.

## See Also

### Receiving drop information

- [dropEntered(info:)](<dropentered(info_).md>) — Tells the delegate a validated drop has entered the modified view.
- [dropExited(info:)](<dropexited(info_).md>) — Tells the delegate a validated drop operation has exited the modified view.
- [validateDrop(info:)](<validatedrop(info_).md>) — Tells the delegate that a drop containing items conforming to one of the expected types entered a view that accepts drops.
- [performDrop(info:)](<performdrop(info_).md>) — Tells the delegate it can request the item provider data from the given information.
