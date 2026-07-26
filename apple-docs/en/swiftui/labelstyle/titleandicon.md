---
title: titleAndIcon
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 11.3+, tvOS 14.5+, visionOS 1.0+, watchOS 7.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/labelstyle/titleandicon
source_url: 'https://developer.apple.com/documentation/swiftui/labelstyle/titleandicon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/labelstyle/titleandicon.json'
content_hash: 'sha256:936db0268ceff9e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LabelStyle](../labelstyle.md)

# titleAndIcon

<sub>Type Property</sub>

A label style that shows both the title and icon of the label using a system-standard layout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated static var titleAndIcon: TitleAndIconLabelStyle { get }
```

## Discussion

In most cases, labels show both their title and icon by default. However, some containers might apply a different default label style to their content, such as only showing icons within toolbars on macOS and iOS. To opt in to showing both the title and the icon, you can apply the title and icon label style:

```swift
Label("Lightning", systemImage: "bolt.fill")
    .labelStyle(.titleAndIcon)
```

To apply the title and icon style to a group of labels, apply the style to the view hierarchy that contains the labels:

```swift
VStack {
    Label("Rain", systemImage: "cloud.rain")
    Label("Snow", systemImage: "snow")
    Label("Sun", systemImage: "sun.max")
}
.labelStyle(.titleAndIcon)
```

The relative layout of the title and icon is dependent on the context it is displayed in. In most cases, however, the label is arranged horizontally with the icon leading.

## See Also

### Getting built-in label styles

- [automatic](automatic.md) — A label style that resolves its appearance automatically based on the current context.
- [iconOnly](icononly.md) — A label style that only displays the icon of the label.
- [titleOnly](titleonly.md) — A label style that only displays the title of the label.
