---
title: ForEachSubviewCollection
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/foreachsubviewcollection
source_url: 'https://developer.apple.com/documentation/swiftui/foreachsubviewcollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/foreachsubviewcollection.json'
content_hash: 'sha256:6618a8e93bca8942'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ForEachSubviewCollection

<sub>Structure</sub>

A collection which allows a view to be treated as a collection of its subviews in a for each loop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ForEachSubviewCollection<Content> where Content : View
```

## Relationships

- **Conforms To**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [Collection](../swift/collection.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [Sequence](../swift/sequence.md)

## See Also

### Iterating over dynamic data

- [ForEach](foreach.md) — A structure that computes views on demand from an underlying collection of identified data.
- [ForEachSectionCollection](foreachsectioncollection.md) — A collection which allows a view to be treated as a collection of its sections in a for each loop.
- [DynamicViewContent](dynamicviewcontent.md) — A type of view that generates views from an underlying collection of data.
