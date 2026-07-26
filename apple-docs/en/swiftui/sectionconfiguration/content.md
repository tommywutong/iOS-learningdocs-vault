---
title: content
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectionconfiguration/content
source_url: 'https://developer.apple.com/documentation/swiftui/sectionconfiguration/content'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionconfiguration/content.json'
content_hash: 'sha256:37070cc088381d0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SectionConfiguration](../sectionconfiguration.md)

# content

<sub>Instance Property</sub>

The contents of the section body.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var content: SubviewsCollection { get }
```

## Discussion

Notably, the section’s content is a `SubviewsCollection`, not a `Subview`, as it can be made up of multiple subviews. That means in most cases, the subviews collection should be treated as a collection (either indexed into, or used with a `ForEach`), or the subviews collection should be wrapped in a container view, like a layout, or other custom container:

```swift
PinboardSectionsLayout {
    ForEach(sections: content) { section in
        VStack {
            section.content
        }
    }
}
```

Here, we want to create one view for `PinboardSectionsLayout` to place per section in content. To do that, we surround the `ForEach` body in another container, a `VStack` layout, ensuring the different subviews of section.content are treated as a single view by the surrounding layout.
