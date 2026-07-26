---
title: DismissBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dismissbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/dismissbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dismissbehavior.json'
content_hash: 'sha256:a4f3343d0a155cce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DismissBehavior

<sub>Structure</sub>

Programmatic window dismissal behaviors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct DismissBehavior
```

## Overview

Use values of this type to control window dismissal during the current transaction.

For example, to dismiss windows showing a modal presentation that would otherwise prohibit dismissal, use the [destructive](dismissbehavior/destructive.md) behavior:

```swift
struct DismissWindowButton: View {
    @Environment(\.dismissWindow) private var dismissWindow

    var body: some View {
        Button("Close Auxiliary Window") {
            withTransaction(\.dismissBehavior, .destructive) {
                dismissWindow(id: "auxiliary")
            }
        }
    }
}
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting behaviors

- [destructive](dismissbehavior/destructive.md) — The destructive dismiss behavior.
- [interactive](dismissbehavior/interactive.md) — The interactive dismiss behavior.

## See Also

### Closing windows

- [dismissWindow](environmentvalues/dismisswindow.md) — A window dismissal action stored in a view’s environment.
- [DismissWindowAction](dismisswindowaction.md) — An action that dismisses a window associated to a particular scene.
- [dismiss](environmentvalues/dismiss.md) — An action that dismisses the current presentation.
- [DismissAction](dismissaction.md) — An action that dismisses a presentation.
