---
title: 'background(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uihostingconfiguration/background(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingconfiguration/background(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingconfiguration/background%28content%3A%29.json'
content_hash: 'sha256:5d7ba3501d192a9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIHostingConfiguration](../uihostingconfiguration.md)

# background(content:)

<sub>Instance Method</sub>

Sets the background contents for the hosting configuration’s enclosing cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func background<B>(@ContentBuilder content: () -> B) -> UIHostingConfiguration<Content, B> where B : View
```

## Discussion

The following example sets a custom view to the background of the cell:

```swift
UIHostingConfiguration {
    Text("My Contents")
}
.background {
    MyBackgroundView()
}
```

## See Also

### Setting the background

- [background(_:)](<background(__).md>) — Sets the background contents for the hosting configuration’s enclosing cell.
