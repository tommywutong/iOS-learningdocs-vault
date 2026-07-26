---
title: 'minSize(width:height:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uihostingconfiguration/minsize(width:height:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingconfiguration/minsize(width:height:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingconfiguration/minsize%28width%3Aheight%3A%29.json'
content_hash: 'sha256:97a42a7e3e77d0c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIHostingConfiguration](../uihostingconfiguration.md)

# minSize(width:height:)

<sub>Instance Method</sub>

Sets the minimum size for the configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func minSize(width: CGFloat? = nil, height: CGFloat? = nil) -> UIHostingConfiguration<Content, Background>
```

## Parameters

- `width` — The value to use for the width dimension. A value of `nil` indicates that the system default should be used.

- `height` — The value to use for the height dimension. A value of `nil` indicates that the system default should be used.

## Discussion

Use this modifier to indicate that a configuration’s associated cell can be resized to a specific minimum. The following example allows the cell to be compressed to zero size:

```swift
UIHostingConfiguration {
    Text("My Contents")
}
.minSize(width: 0, height: 0)
```

## See Also

### Setting a size

- [minSize()](<minsize().md>) — Sets the minimum size for the configuration. _(deprecated)_
