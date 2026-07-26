---
title: 'validateDrop(info:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dropdelegate/validatedrop(info:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dropdelegate/validatedrop(info:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropdelegate/validatedrop%28info%3A%29.json'
content_hash: 'sha256:ad739a065ccd8353'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DropDelegate](../dropdelegate.md)

# validateDrop(info:)

<sub>Instance Method</sub>

Tells the delegate that a drop containing items conforming to one of the expected types entered a view that accepts drops.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func validateDrop(info: DropInfo) -> Bool
```

## Discussion

Specify the expected types when you apply the drop modifier to the view. The default implementation returns `true`.

## Default Implementations

### DropDelegate Implementations

- [validateDrop(info:)](<validatedrop(info_)-1hqfh.md>) — Tells the delegate that a drop containing items conforming to one of the expected types entered a view that accepts drops.

## See Also

### Receiving drop information

- [dropEntered(info:)](<dropentered(info_).md>) — Tells the delegate a validated drop has entered the modified view.
- [dropExited(info:)](<dropexited(info_).md>) — Tells the delegate a validated drop operation has exited the modified view.
- [dropUpdated(info:)](<dropupdated(info_).md>) — Tells the delegate that a validated drop moved inside the modified view.
- [performDrop(info:)](<performdrop(info_).md>) — Tells the delegate it can request the item provider data from the given information.
