---
title: 'init(before:addition:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/commandgroup/init(before:addition:)'
source_url: 'https://developer.apple.com/documentation/swiftui/commandgroup/init(before:addition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commandgroup/init%28before%3Aaddition%3A%29.json'
content_hash: 'sha256:d66df637b66176c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CommandGroup](../commandgroup.md)

# init(before:addition:)

<sub>Initializer</sub>

A value describing the addition of the given views to the beginning of the indicated group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(before group: CommandGroupPlacement, @ContentBuilder addition: () -> Content)
```

## See Also

### Creating a command group

- [init(after:addition:)](<init(after_addition_).md>) — A value describing the addition of the given views to the end of the indicated group.
- [init(replacing:addition:)](<init(replacing_addition_).md>) — A value describing the complete replacement of the contents of the indicated group with the given views.
