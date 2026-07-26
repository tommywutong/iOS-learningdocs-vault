---
title: DragConfiguration.OperationsWithinApp
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dragconfiguration/operationswithinapp-swift.struct
source_url: 'https://developer.apple.com/documentation/swiftui/dragconfiguration/operationswithinapp-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dragconfiguration/operationswithinapp-swift.struct.json'
content_hash: 'sha256:6b35955bcdef3791'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DragConfiguration](../dragconfiguration.md)

# DragConfiguration.OperationsWithinApp

<sub>Structure</sub>

Describes the drag operations suggested to destinations within the app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct OperationsWithinApp
```

## Overview

To create a default configuration, initialize it without parameters.

On iOS, the default behavior is to allow drag-to-copy within the application. On macOS, the default configuration is to support drag-to-copy to destinations both within the application and to other apps.

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
        let operations = OperationsWithinApp(allowMove: true)
        return DragConfiguration(operationsWithinApp: operations)
    }
}
```

In the example above, an application provides operations that will be suggested to destinations within the app. Drags to other apps will use the default behavior: suggest operation `copy` to drag destinations on macOS, and forbid drags on iOS.

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(allowCopy:allowMove:allowDelete:)](<operationswithinapp-swift.struct/init(allowcopy_allowmove_allowdelete_).md>) — Creates a value that describes the operations allowed for drags that end within the application.
- [init(allowMove:)](<operationswithinapp-swift.struct/init(allowmove_).md>) — Creates a value that describes the operations allowed for drags that end within the application. Copy operation is always allowed.

### Instance Properties

- [allowAlias](operationswithinapp-swift.struct/allowalias.md) — A Boolean value indicating if the drag operation supports creating aliases to the dropped items.
