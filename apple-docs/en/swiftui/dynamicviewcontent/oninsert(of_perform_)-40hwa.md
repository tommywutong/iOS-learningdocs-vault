---
title: 'onInsert(of:perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/dynamicviewcontent/oninsert(of:perform:)-40hwa'
source_url: 'https://developer.apple.com/documentation/swiftui/dynamicviewcontent/oninsert(of:perform:)-40hwa'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dynamicviewcontent/oninsert%28of%3Aperform%3A%29-40hwa.json'
content_hash: 'sha256:51d3dfe1149ff069'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DynamicViewContent](../dynamicviewcontent.md)

# onInsert(of:perform:)

<sub>Instance Method</sub>

Sets the insert action for the dynamic view.

> [!warning] Deprecated
> Use [onInsert(of:perform:)](<oninsert(of_perform_)-418bq.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func onInsert(of acceptedTypeIdentifiers: [String], perform action: @escaping (Int, [NSItemProvider]) -> Void) -> some DynamicViewContent

```

## Parameters

- `acceptedTypeIdentifiers` — An array of UTI types that the dynamic view supports.

- `action` — A closure that SwiftUI invokes when elements are added to the view. The closure takes two arguments: The first argument is the offset relative to the dynamic view’s underlying collection of data. The second argument is an array of `NSItemProvider` that represents the data that you want to insert.

## Return Value

A view that calls `action` when elements are inserted into the original view.
