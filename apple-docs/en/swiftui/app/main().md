---
title: main()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/app/main()
source_url: 'https://developer.apple.com/documentation/swiftui/app/main()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/app/main%28%29.json'
content_hash: 'sha256:353af62170762529'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [App](../app.md)

# main()

<sub>Type Method</sub>

Initializes and runs the app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency static func main()
```

## Discussion

If you precede your [App](../app.md) conformer’s declaration with the [@main](https://docs.swift.org/swift-book/ReferenceManual/Attributes.html#ID626) attribute, the system calls the conformer’s `main()` method to launch the app. SwiftUI provides a default implementation of the method that manages the launch process in a platform-appropriate way.

## See Also

### Running an app

- [init()](<init().md>) — Creates an instance of the app using the body that you define for its content.
