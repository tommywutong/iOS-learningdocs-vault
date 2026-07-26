---
title: main()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/widget/main()
source_url: 'https://developer.apple.com/documentation/swiftui/widget/main()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widget/main%28%29.json'
content_hash: 'sha256:9fc46f7761387f48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Widget](../widget.md)

# main()

<sub>Type Method</sub>

Initializes and runs the widget.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency static func main()
```

## Overview

Because you precede your [Widget](../widget.md) conformer’s declaration with the [@main](https://docs.swift.org/swift-book/ReferenceManual/Attributes.html#ID626) attribute, the system calls your widget’s `main()` method to launch the widget. SwiftUI provides a default implementation of the method that manages the launch process in a platform-appropriate way.

## See Also

### Running a widget

- [init()](<init().md>) — Creates a widget using `body` as its content.
