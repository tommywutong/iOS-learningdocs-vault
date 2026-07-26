---
title: ForEach
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/foreach
source_url: 'https://developer.apple.com/documentation/swiftui/foreach'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/foreach.json'
content_hash: 'sha256:fb3b373ab509eca1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ForEach

<sub>Structure</sub>

A structure that computes views on demand from an underlying collection of identified data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ForEach<Data, ID, Content> where Data : RandomAccessCollection, ID : Hashable
```

## Overview

Use `ForEach` to provide views based on a [RandomAccessCollection](../swift/randomaccesscollection.md) of some data type. Either the collection’s elements must conform to [Identifiable](../swift/identifiable.md) or you need to provide an `id` parameter to the `ForEach` initializer.

The following example creates a `NamedFont` type that conforms to [Identifiable](../swift/identifiable.md), and an array of this type called `namedFonts`. A `ForEach` instance iterates over the array, producing new [Text](text.md) instances that display examples of each SwiftUI [Font](font.md) style provided in the array.

```swift
private struct NamedFont: Identifiable {
    let name: String
    let font: Font
    var id: String { name }
}

private let namedFonts: [NamedFont] = [
    NamedFont(name: "Large Title", font: .largeTitle),
    NamedFont(name: "Title", font: .title),
    NamedFont(name: "Headline", font: .headline),
    NamedFont(name: "Body", font: .body),
    NamedFont(name: "Caption", font: .caption)
]

var body: some View {
    ForEach(namedFonts) { namedFont in
        Text(namedFont.name)
            .font(namedFont.font)
    }
}
```

![A vertically arranged stack of labels showing various standard fonts,](../../../attachments/9819873f850b2cba7a4174a869ad369f/SwiftUI-ForEach-fonts@2x.png)

Some containers like [List](list.md) or [LazyVStack](lazyvstack.md) will query the elements within a for each lazily. To obtain maximal performance, ensure that the view created from each element in the collection represents a constant number of views.

For example, the following view uses an if statement which means each element of the collection can represent either 1 or 0 views, a non-constant number.

```swift
ForEach(namedFonts) { namedFont in
    if namedFont.name.count != 2 {
        Text(namedFont.name)
    }
}
```

You can make the above view represent a constant number of views by wrapping the condition in a [VStack](vstack.md), an [HStack](hstack.md), or a [ZStack](zstack.md).

```swift
ForEach(namedFonts) { namedFont in
    VStack {
        if namedFont.name.count != 2 {
            Text(namedFont.name)
        }
    }
}
```

When enabling the following launch argument, SwiftUI will log when it encounters a view that produces a non-constant number of views in these containers:

```swift
-LogForEachSlowPath YES
```

## Relationships

- **Conforms To**: [AccessibilityRotorContent](accessibilityrotorcontent.md), [AttachmentContent](../realitykit/attachmentcontent.md), [Chart3DContent](../charts/chart3dcontent.md), [ChartContent](../charts/chartcontent.md), [Copyable](../swift/copyable.md), [CustomizableToolbarContent](customizabletoolbarcontent.md), [DynamicMapContent](../mapkit/dynamicmapcontent.md), [DynamicTableRowContent](dynamictablerowcontent.md), [DynamicViewContent](dynamicviewcontent.md), [Escapable](../swift/escapable.md), [MapContent](../mapkit/mapcontent.md), [SceneAccessoryContent](sceneaccessorycontent.md), [TabContent](tabcontent.md), [TableRowContent](tablerowcontent.md), [ToolbarContent](toolbarcontent.md), [View](view.md)

## Topics

### Creating a collection

- [init(_:)](<foreach/init(__).md>) — Creates an instance that uniquely identifies and creates table rows across updates based on the identity of the underlying data.
- [init(_:content:)](<foreach/init(__content_).md>) — Creates an instance that uniquely identifies and creates map content across updates based on the identity of the underlying data.
- [init(_:id:content:)](<foreach/init(__id_content_).md>) — Creates an instance that uniquely identifies and creates map content across updates based on the provided key path to the underlying data’s identifier.
- [init(sections:content:)](<foreach/init(sections_content_).md>) — Creates an instance that uniquely identifies and creates views across updates based on the sections of a given view.
- [init(subviews:content:)](<foreach/init(subviews_content_).md>) — Creates an instance that uniquely identifies and creates views across updates based on the subviews of a given view.

### Creating an editable collection

- [init(_:editActions:content:)](<foreach/init(__editactions_content_).md>) — Creates an instance that uniquely identifies and creates views across updates based on the identity of the underlying data.
- [init(_:id:editActions:content:)](<foreach/init(__id_editactions_content_).md>) — Creates an instance that uniquely identifies and creates views across updates based on the identity of the underlying data.

### Accessing content

- [content](foreach/content.md) — A function to create content on demand using the underlying data.
- [data](foreach/data.md) — The collection of underlying identified data that SwiftUI uses to create views dynamically.

## See Also

### Iterating over dynamic data

- [ForEachSectionCollection](foreachsectioncollection.md) — A collection which allows a view to be treated as a collection of its sections in a for each loop.
- [ForEachSubviewCollection](foreachsubviewcollection.md) — A collection which allows a view to be treated as a collection of its subviews in a for each loop.
- [DynamicViewContent](dynamicviewcontent.md) — A type of view that generates views from an underlying collection of data.
