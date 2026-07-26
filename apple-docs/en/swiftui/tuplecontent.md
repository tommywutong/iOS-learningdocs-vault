---
title: TupleContent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tuplecontent
source_url: 'https://developer.apple.com/documentation/swiftui/tuplecontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tuplecontent.json'
content_hash: 'sha256:e7f2b29f126ff599'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TupleContent

<sub>Structure</sub>

Content created from a tuple of content to be treated as siblings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct TupleContent<each Content>
```

## Overview

You will rarely, if ever, need to create a `TupleContent` directly. Instead, `TupleContent` will be constructed on your behalf when using a `ContentBuilder`.

This type should be conformed to builder DSL protocols to represent tuple content in that DSL.

`TupleContent` defines a `body` property of type `Never` to improve the ergonomics of conforming to multiple DSL protocols, which should all use `Never` as the universal “primitive body” type.

## Relationships

- **Conforms To**: [AccessibilityRotorContent](accessibilityrotorcontent.md), [ChartContent](../charts/chartcontent.md), [Commands](commands.md), [Copyable](../swift/copyable.md), [CustomizableToolbarContent](customizabletoolbarcontent.md), [Escapable](../swift/escapable.md), [SceneAccessoryContent](sceneaccessorycontent.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [ToolbarContent](toolbarcontent.md), [View](view.md)

## Topics

### Creating tuple content

- [init(_:)](<tuplecontent/init(__).md>)

### Getting tuple content

- [content](tuplecontent/content.md)

## See Also

### Supporting content types

- [EmptyContent](emptycontent.md) — Content which contains nothing.
