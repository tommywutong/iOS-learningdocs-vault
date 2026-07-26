---
title: NSViewRepresentableContext
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nsviewrepresentablecontext
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewrepresentablecontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewrepresentablecontext.json'
content_hash: 'sha256:c966b573e9e36eb8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NSViewRepresentableContext

<sub>Structure</sub>

Contextual information about the state of the system that you use to create and update your AppKit view.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency struct NSViewRepresentableContext<View> where View : NSViewRepresentable
```

## Overview

An [NSViewRepresentableContext](nsviewrepresentablecontext.md) structure contains details about the current state of the system. When creating and updating your view, the system creates one of these structures and passes it to the appropriate method of your custom [NSViewRepresentable](nsviewrepresentable.md) instance. Use the information in this structure to configure your view. For example, use the provided environment values to configure the appearance of your view. Don’t create this structure yourself.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Coordinating view-related interactions

- [coordinator](nsviewrepresentablecontext/coordinator.md) — An instance you use to communicate your AppKit view’s behavior and state out to SwiftUI objects.
- [transaction](nsviewrepresentablecontext/transaction.md) — The current transaction.

### Getting the current environment data

- [environment](nsviewrepresentablecontext/environment.md) — Environment data that describes the current state of the system.

### Instance Methods

- [animate(changes:completion:)](<nsviewrepresentablecontext/animate(changes_completion_).md>) — Animates changes using the animation in the current transaction.

## See Also

### Adding AppKit views to SwiftUI view hierarchies

- [NSViewRepresentable](nsviewrepresentable.md) — A wrapper that you use to integrate an AppKit view into your SwiftUI view hierarchy.
- [NSViewControllerRepresentable](nsviewcontrollerrepresentable.md) — A wrapper that you use to integrate an AppKit view controller into your SwiftUI interface.
- [NSViewControllerRepresentableContext](nsviewcontrollerrepresentablecontext.md) — Contextual information about the state of the system that you use to create and update your AppKit view controller.
