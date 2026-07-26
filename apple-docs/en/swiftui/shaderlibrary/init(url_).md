---
title: 'init(url:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shaderlibrary/init(url:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shaderlibrary/init(url:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shaderlibrary/init%28url%3A%29.json'
content_hash: 'sha256:48cff257b668b678'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShaderLibrary](../shaderlibrary.md)

# init(url:)

<sub>Initializer</sub>

Creates a new Metal shader library from the contents of `url`, which must be the location  of precompiled Metal library. Functions compiled from the returned library will only be cached as long as the returned library exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(url: URL)
```

## See Also

### Creating a shader library

- [init(data:)](<init(data_).md>) — Creates a new Metal shader library from `data`, which must be the contents of precompiled Metal library. Functions compiled from the returned library will only be cached as long as the returned library exists.
