---
title: main()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/widgetbundle/main()
source_url: 'https://developer.apple.com/documentation/swiftui/widgetbundle/main()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetbundle/main%28%29.json'
content_hash: 'sha256:87c50b73ca36d2a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetBundle](../widgetbundle.md)

# main()

<sub>Type Method</sub>

Initializes and runs the widget bundle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency static func main()
```

## Overview

Because you precede your [WidgetBundle](../widgetbundle.md) conformer’s declaration with the [@main](https://docs.swift.org/swift-book/ReferenceManual/Attributes.html#ID626) attribute, the system calls your widget bundle’s `main()` method to launch the widget bundle. SwiftUI provides a default implementation of the method that manages the launch process in a platform-appropriate way.

## See Also

### Running a widget bundle

- [init()](<init().md>) — Creates a widget bundle using the bundle’s body as its content.
