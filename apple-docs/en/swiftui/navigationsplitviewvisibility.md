---
title: NavigationSplitViewVisibility
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/navigationsplitviewvisibility
source_url: 'https://developer.apple.com/documentation/swiftui/navigationsplitviewvisibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationsplitviewvisibility.json'
content_hash: 'sha256:10368574cc12a872'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NavigationSplitViewVisibility

<sub>Structure</sub>

The visibility of the leading columns in a navigation split view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NavigationSplitViewVisibility
```

## Overview

Use a value of this type to control the visibility of the columns of a [NavigationSplitView](navigationsplitview.md). Create a [State](state.md) property with a value of this type, and pass a [Binding](binding.md) to that state to the [init(columnVisibility:sidebar:detail:)](<navigationsplitview/init(columnvisibility_sidebar_detail_).md>) or [init(columnVisibility:sidebar:content:detail:)](<navigationsplitview/init(columnvisibility_sidebar_content_detail_).md>) initializer when you create the navigation split view. You can then modify the value elsewhere in your code to:

- Hide all but the trailing column with [detailOnly](navigationsplitviewvisibility/detailonly.md).
- Hide the leading column of a three-column navigation split view with [doubleColumn](navigationsplitviewvisibility/doublecolumn.md).
- Show all the columns with [all](navigationsplitviewvisibility/all.md).
- Rely on the automatic behavior for the current context with [automatic](navigationsplitviewvisibility/automatic.md).

> [!note] Note
> Some platforms don’t respect every option. For example, macOS always displays the content column.

## Relationships

- **Conforms To**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting visibilities

- [automatic](navigationsplitviewvisibility/automatic.md) — Use the default leading column visibility for the current device.
- [all](navigationsplitviewvisibility/all.md) — Show all the columns of a three-column navigation split view.
- [doubleColumn](navigationsplitviewvisibility/doublecolumn.md) — Show the content column and detail area of a three-column navigation split view, or the sidebar column and detail area of a two-column navigation split view.
- [detailOnly](navigationsplitviewvisibility/detailonly.md) — Hide the leading two columns of a three-column navigation split view, so that just the detail area shows.

## See Also

### Presenting views in columns

- [Bringing robust navigation structure to your SwiftUI app](bringing-robust-navigation-structure-to-your-swiftui-app.md) — Use navigation links, stacks, destinations, and paths to provide a streamlined experience for all platforms, as well as behaviors such as deep linking and state restoration.
- [Migrating to new navigation types](migrating-to-new-navigation-types.md) — Improve navigation behavior in your app by replacing navigation views with navigation stacks and navigation split views.
- [NavigationSplitView](navigationsplitview.md) — A view that presents views in two or three columns, where selections in leading columns control presentations in subsequent columns.
- [navigationSplitViewStyle(_:)](<view/navigationsplitviewstyle(__).md>) — Sets the style for navigation split views within this view.
- [navigationSplitViewColumnWidth(_:)](<view/navigationsplitviewcolumnwidth(__).md>) — Sets a fixed, preferred width for the column containing this view.
- [navigationSplitViewColumnWidth(min:ideal:max:)](<view/navigationsplitviewcolumnwidth(min_ideal_max_).md>) — Sets a flexible, preferred width for the column containing this view.
- [NavigationLink](navigationlink.md) — A view that controls a navigation presentation.
