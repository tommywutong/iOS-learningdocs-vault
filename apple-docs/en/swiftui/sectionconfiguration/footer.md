---
title: footer
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectionconfiguration/footer
source_url: 'https://developer.apple.com/documentation/swiftui/sectionconfiguration/footer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionconfiguration/footer.json'
content_hash: 'sha256:8bf15d21fb5a52d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SectionConfiguration](../sectionconfiguration.md)

# footer

<sub>Instance Property</sub>

The contents of the section footer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var footer: SubviewsCollection { get }
```

## Discussion

Notably, the section’s footer is a `SubviewsCollection`, not a `Subview`, as it can be made up of multiple subviews. That means in most cases, the subviews collection should be treated as a collection (either indexed into, or used with a `ForEach`), or the subviews collection should be wrapped in a container view, like a layout, or other custom container:

```swift
ForEach(sections: content) {
    VStack {
        HStack { section.header }
        HStack { section.footer }
    }
}
```

Here, we surround the header and footer in an `HStack` layout to avoid vertically stacking the subviews of the header and footer which we want visually grouped together. Additionally, we surround the `ForEach` body in a VStack, so it is treated as a single view by containers it gets passed to.
