---
title: AnyLayout
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/anylayout
source_url: 'https://developer.apple.com/documentation/swiftui/anylayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anylayout.json'
content_hash: 'sha256:c4d8c00c1dca0a81'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AnyLayout

<sub>Structure</sub>

A type-erased instance of the layout protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AnyLayout
```

## Overview

Use an `AnyLayout` instance to enable dynamically changing the type of a layout container without destroying the state of the subviews. For example, you can create a layout that changes between horizontal and vertical layouts based on the current Dynamic Type setting:

```swift
struct DynamicLayoutExample: View {
    @Environment(\.dynamicTypeSize) var dynamicTypeSize

    var body: some View {
        let layout = dynamicTypeSize <= .medium ?
            AnyLayout(HStackLayout()) : AnyLayout(VStackLayout())

        layout {
            Text("First label")
            Text("Second label")
        }
    }
}
```

The types that you use with `AnyLayout` must conform to the [Layout](layout.md) protocol. The above example chooses between the [HStackLayout](hstacklayout.md) and [VStackLayout](vstacklayout.md) types, which are versions of the built-in [HStack](hstack.md) and [VStack](vstack.md) containers that conform to the protocol. You can also use custom layout types that you define.

## Relationships

- **Conforms To**: [Animatable](animatable.md), [Layout](layout.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating the layout

- [init(_:)](<anylayout/init(__).md>) — Creates a type-erased value that wraps the specified layout.

## See Also

### Transitioning between layout types

- [HStackLayout](hstacklayout.md) — A horizontal container that you can use in conditional layouts.
- [VStackLayout](vstacklayout.md) — A vertical container that you can use in conditional layouts.
- [ZStackLayout](zstacklayout.md) — An overlaying container that you can use in conditional layouts.
- [GridLayout](gridlayout.md) — A grid that you can use in conditional layouts.
