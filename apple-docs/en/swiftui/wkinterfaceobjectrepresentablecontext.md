---
title: WKInterfaceObjectRepresentableContext
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/wkinterfaceobjectrepresentablecontext
source_url: 'https://developer.apple.com/documentation/swiftui/wkinterfaceobjectrepresentablecontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkinterfaceobjectrepresentablecontext.json'
content_hash: 'sha256:048f5a2679ac5427'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WKInterfaceObjectRepresentableContext

<sub>Structure</sub>

Contextual information about the state of the system that you use to create and update your WatchKit interface object.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency struct WKInterfaceObjectRepresentableContext<Representable> where Representable : WKInterfaceObjectRepresentable
```

## Overview

A [WKInterfaceObjectRepresentableContext](wkinterfaceobjectrepresentablecontext.md) structure contains details about the current state of the system. When creating and updating your interface objects, the system creates one of these structures and passes it to the appropriate method of your custom [WKInterfaceObjectRepresentable](wkinterfaceobjectrepresentable.md) instance. Use the information in this structure to configure your object. Don’t create this structure yourself.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Coordinating interactions

- [coordinator](wkinterfaceobjectrepresentablecontext/coordinator.md) — The view’s associated coordinator.
- [transaction](wkinterfaceobjectrepresentablecontext/transaction.md) — The current transaction.

### Getting the current environment data

- [environment](wkinterfaceobjectrepresentablecontext/environment.md) — The current environment.

## See Also

### Adding WatchKit views to SwiftUI view hierarchies

- [WKInterfaceObjectRepresentable](wkinterfaceobjectrepresentable.md) — A view that represents a WatchKit interface object.
