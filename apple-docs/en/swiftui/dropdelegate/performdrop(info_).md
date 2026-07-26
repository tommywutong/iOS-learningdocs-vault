---
title: 'performDrop(info:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dropdelegate/performdrop(info:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dropdelegate/performdrop(info:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropdelegate/performdrop%28info%3A%29.json'
content_hash: 'sha256:7ba78c6a0871cae3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DropDelegate](../dropdelegate.md)

# performDrop(info:)

<sub>Instance Method</sub>

Tells the delegate it can request the item provider data from the given information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func performDrop(info: DropInfo) -> Bool
```

## Return Value

A Boolean that is `true` if the drop was successful, `false` otherwise.

## Discussion

Incorporate the received data into your app’s data model as appropriate.

Make sure to start loading the contents of `NSItemProvider` instances from [DropInfo](../dropinfo.md) within the scope of this method. Do not perform loading asynchronously on a different actor. Loading the contents may finish later, but it must start here. For security reasons, the drop receiver can access the dropped payload only before this method returns.

## See Also

### Receiving drop information

- [dropEntered(info:)](<dropentered(info_).md>) — Tells the delegate a validated drop has entered the modified view.
- [dropExited(info:)](<dropexited(info_).md>) — Tells the delegate a validated drop operation has exited the modified view.
- [dropUpdated(info:)](<dropupdated(info_).md>) — Tells the delegate that a validated drop moved inside the modified view.
- [validateDrop(info:)](<validatedrop(info_).md>) — Tells the delegate that a drop containing items conforming to one of the expected types entered a view that accepts drops.
