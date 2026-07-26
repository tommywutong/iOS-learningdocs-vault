---
title: DragConfiguration.OperationsOutsideApp
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dragconfiguration/operationsoutsideapp-swift.struct
source_url: 'https://developer.apple.com/documentation/swiftui/dragconfiguration/operationsoutsideapp-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dragconfiguration/operationsoutsideapp-swift.struct.json'
content_hash: 'sha256:7a930aa507a34568'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DragConfiguration](../dragconfiguration.md)

# DragConfiguration.OperationsOutsideApp

<sub>Structure</sub>

Describes the suggested drag operations to other applications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct OperationsOutsideApp
```

## Overview

To create a default configuration, initialize it without parameters.

On iOS, the default behavior is to disallow drag outside the application. On macOS—support drag-to-copy to destinations both within the application and to other apps.

In addition to `copy`, add `move` operation support by specifying that in the initializer:

```swift
struct DraggableBookView: View {
    var id: UUID

    var body: some View {
        BookView()
            .draggable(Book(id: id))
            .dragConfiguration(makeConfiguration())
    }

    func makeConfiguration() -> DragConfiguration {
        let operations = OperationsOutsideApp(
            allowCopy: true, allowMove: true
        )
        return DragConfiguration(operationsOutsideApp: operations)
    }
}
```

In the example above, an application provides operations that will be suggested to other applications. Drags to destinations within the app will use the default behavior: suggest operation `copy` to drag destinations.

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(allowCopy:)](<operationsoutsideapp-swift.struct/init(allowcopy_).md>) — Creates a value that describes the operations allowed for drags to other applications.
- [init(allowCopy:allowMove:allowDelete:)](<operationsoutsideapp-swift.struct/init(allowcopy_allowmove_allowdelete_).md>) — Creates a value that describes the operations allowed for drags to other applications.

### Instance Properties

- [allowAlias](operationsoutsideapp-swift.struct/allowalias.md) — A Boolean value indicating if the drag operation supports creating aliases to the dropped items.
