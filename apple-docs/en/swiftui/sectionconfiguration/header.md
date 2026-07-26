---
title: header
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectionconfiguration/header
source_url: 'https://developer.apple.com/documentation/swiftui/sectionconfiguration/header'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionconfiguration/header.json'
content_hash: 'sha256:a2359c48bbf40432'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SectionConfiguration](../sectionconfiguration.md)

# header

<sub>Instance Property</sub>

The contents of the section header.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var header: SubviewsCollection { get }
```

## Discussion

Notably, the section’s header is a `SubviewsCollection`, not a `Subview`, as it can be made up of multiple subviews. That means in most cases, the subviews collection should be treated as a collection (either indexed into, or used with a `ForEach`), or the subviews collection should be wrapped in a container view, like a layout, or other custom container:

```swift
ForEach(sections: content) {
    VStack {
        HStack { section.header }
        HStack { section.footer }
    }
}
```

Here, we surround the header and footer in an `HStack` layout to avoid vertically stacking the subviews of the header and footer which we want visually grouped together. Additionally, we surround the `ForEach` body in a VStack, so it is treated as a single view by containers it gets passed to.
