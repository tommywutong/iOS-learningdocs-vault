---
title: Spacer
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spacer
source_url: 'https://developer.apple.com/documentation/swiftui/spacer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spacer.json'
content_hash: 'sha256:3a40a01949aee2d0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Spacer

<sub>Structure</sub>

A flexible space that expands along the major axis of its containing stack layout, or on both axes if not contained in a stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Spacer
```

## Overview

A spacer creates an adaptive view with no content that expands as much as it can. For example, when placed within an [HStack](hstack.md), a spacer expands horizontally as much as the stack allows, moving sibling views out of the way, within the limits of the stack’s size. SwiftUI sizes a stack that doesn’t contain a spacer up to the combined ideal widths of the content of the stack’s child views.

The following example provides a simple checklist row to illustrate how you can use a spacer:

```swift
struct ChecklistRow: View {
    let name: String

    var body: some View {
        HStack {
            Image(systemName: "checkmark")
            Text(name)
        }
        .border(Color.blue)
    }
}
```

![A figure of a blue rectangular border that marks the boundary of an](../../../attachments/9df8ab78b8a87386da85f8d288f52f82/Spacer-1@2x.png)

Adding a spacer before the image creates an adaptive view with no content that expands to push the image and text to the right side of the stack. The stack also now expands to take as much space as the parent view allows, shown by the blue border that indicates the boundary of the stack:

```swift
struct ChecklistRow: View {
    let name: String

    var body: some View {
        HStack {
            Spacer()
            Image(systemName: "checkmark")
            Text(name)
        }
        .border(Color.blue)
    }
}
```

![A figure of a blue rectangular border that marks the boundary of an](../../../attachments/2d8b3cd23072e1610a707d4f205e9c63/Spacer-2@2x.png)

Moving the spacer between the image and the name pushes those elements to the left and right sides of the [HStack](hstack.md), respectively. Because the stack contains the spacer, it expands to take as much horizontal space as the parent view allows; the blue border indicates its size:

```swift
struct ChecklistRow: View {
    let name: String

    var body: some View {
        HStack {
            Image(systemName: "checkmark")
            Spacer()
            Text(name)
        }
        .border(Color.blue)
    }
}
```

![A figure of a blue rectangular border that marks the boundary of an](../../../attachments/2eb4db02232cd37f4fa9dbfc8a0baa36/Spacer-3@2x.png)

Adding two spacer views on the outside of the stack leaves the image and text together, while the stack expands to take as much horizontal space as the parent view allows:

```swift
struct ChecklistRow: View {
    let name: String

    var body: some View {
        HStack {
            Spacer()
            Image(systemName: "checkmark")
            Text(name)
            Spacer()
        }
        .border(Color.blue)
    }
}
```

![A figure of a blue rectangular border marks the boundary of an HStack,](../../../attachments/d046a0aef1a9b759f52414ff6b385341/Spacer-4@2x.png)

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](view.md)

## Topics

### Creating a spacer

- [init(minLength:)](<spacer/init(minlength_).md>)
- [minLength](spacer/minlength.md) — The minimum length this spacer can be shrunk to, along the axis or axes of expansion.

## See Also

### Separators

- [Divider](divider.md) — A visual element that can be used to separate other content.
