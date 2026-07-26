---
title: 'init(data:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shaderlibrary/init(data:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shaderlibrary/init(data:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shaderlibrary/init%28data%3A%29.json'
content_hash: 'sha256:9940b24c2b3a2fe0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShaderLibrary](../shaderlibrary.md)

# init(data:)

<sub>Initializer</sub>

Creates a new Metal shader library from `data`, which must be the contents of precompiled Metal library. Functions compiled from the returned library will only be cached as long as the returned library exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(data: Data)
```

## See Also

### Creating a shader library

- [init(url:)](<init(url_).md>) — Creates a new Metal shader library from the contents of `url`, which must be the location  of precompiled Metal library. Functions compiled from the returned library will only be cached as long as the returned library exists.
