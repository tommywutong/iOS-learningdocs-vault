---
title: 在列表、叠放、网格和自定布局中重新排列项目
framework: SwiftUI
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/reordering-items-in-lists-stacks-grids-and-custom-layouts
source_url: 'https://developer.apple.com/documentation/swiftui/reordering-items-in-lists-stacks-grids-and-custom-layouts'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/reordering-items-in-lists-stacks-grids-and-custom-layouts.json'
content_hash: 'sha256:8c65c868c53c9260'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [拖放](drag-and-drop.md)

# 在列表、叠放、网格和自定布局中重新排列项目

<sub>文章</sub>

使用重新排列修饰符为 SwiftUI 布局添加拖动重排交互。

## 概述

当你拥有一个或多个有序数据项集合，并且每个数据项都显示为_容器_（例如列表、叠放、网格或自定布局）中的一个视图时，SwiftUI 会提供重新排列功能。系统让用户可以选中代表某个数据项的视图并在容器内拖动它。当用户拖动该视图时，其他视图会移开，显示出一个占位空间，用户可以在那里放下该视图。

当用户将视图放到占位空间上时，系统会提供与移动中的视图相对应的数据项标识符以及这些视图的新位置。然后，你就可以在集合中移动与移动中的视图相对应的数据项，即使数组同时发生了其他更改（例如云同步）也是如此。

如果你将视图组织成由多个数据集合表示的分区，例如让用户把照片整理进相册的摄影 App，你可以配置重新排列功能，使其既在用户把照片移到相册内其他位置时生效，也在用户把照片从一个相册移到另一个相册时生效。

### 在单个集合中重新排列项目

当你的视图由单个有序数据项集合构建而成（例如摄影 App 中的一组照片）时，首先为数据项配置一个符合 [Hashable](../swift/hashable.md) 和 [Sendable](../swift/sendable.md) 的标识符。例如，使用符合 [Sendable](../swift/sendable.md) 的标识符数据类型，让你的数据项符合 [Identifiable](../swift/identifiable.md)。

接下来，通过向生成这些视图的 [ForEach](foreach.md) 声明添加 [reorderable()](<dynamicviewcontent/reorderable().md>) 修饰符，来指示你希望用户重新排列哪些视图，如下面的代码所示：

```swift
@State private var photos: [Photo] = loadPhotos()

var body: some View {
    VStack {
        ForEach(photos) { photo in
            PhotoView(photo: photo)
        }
        .reorderable()
    }
}
```

最后，通过向包裹它的列表、叠放、网格或自定布局容器添加 [reorderContainer(for:isEnabled:move:)](<view/reordercontainer(for_isenabled_move_).md>) 修饰符，定义界面中用户可以重新排列视图的区域，以指定要纳入重新排列的视图范围。在 `move` 闭包中，指定如何应用系统提供的用于描述集合更改的 [ReorderDifference](reorderdifference.md)，如下面的代码示例所示：

```swift
@State private var photos: [Photo] = loadPhotos()

var body: some View {
    VStack {
        ...
    }
    .reorderContainer(for: Photo.self) { difference in
        move(difference: difference)
    }
}
```

### 跨多个集合重新排列项目

当你把视图组织成由多个数据集合构建的分区时（例如摄影 App 中各自包含照片的相册），请向生成要重新排列视图的 [ForEach](foreach.md) 添加 [reorderable(collectionID:)](<dynamicviewcontent/reorderable(collectionid_).md>)。然后，为每个包含这些视图数据项的集合提供一个标识符，如下例所示：

```swift
ScrollView {
    LazyVStack {
        ForEach(model.albumSections) { albumSection in
            Section(albumSection.title) {
                ForEach(albumSection.items) { photo in
                    PhotoView(photo: photo)
                }
                .reorderable(collectionID: albumSection.id)
            }
        }
    }
}
```

接下来，通过向包含所有要重新排列的分区和视图的列表、叠放、网格或自定布局添加 [reorderContainer(for:in:isEnabled:move:)](<view/reordercontainer(for_in_isenabled_move_).md>) 来定义重新排列区域的范围：

```swift
ScrollView {
    LazyVStack {
        ...
    }
    .reorderContainer(
        for: Photo.self,
        in: AlbumSection.ID.self
    ) { difference in
        move(difference: difference)
    }
}
```

当用户在相册内移动视图，或把视图从一个相册移到另一个相册时，系统会提供一个 [ReorderDifference](reorderdifference.md) 实例，其中包含集合标识符和位置，你可以用它来移动视图对应的数据项。

### 支持容器外的拖放

向容器添加重新排列修饰符只支持在容器内移动视图。使用拖放修饰符来支持容器与你 App 的其他部分或其他 App 之间的拖放。

添加 [dragContainer(for:in:_:)](<view/dragcontainer(for_in___).md>) 修饰符，以便在用户把视图拖出你的容器时为这些视图提供传输表示。例如，下面的代码展示了当用户把照片拖到另一个窗口或 App 时，如何选择一个系统可用来获取传输表示的 `Photo` 实例：

```swift
@State private var photos: [Photo] = loadPhotos()

var body: some View {
    VStack {
        ...
    }
    .reorderContainer(for: Photo.self) { difference in
        move(difference: difference)
    }
    .dragContainer(for: Photo.self) { photoID in
        guard let photo = photos.first(where: { $0.id == photoID }) else {
            return []
        }
        return [photo]
    }
}
```

在 [reorderContainer(for:isEnabled:move:)](<view/reordercontainer(for_isenabled_move_).md>) 修饰符之后添加 [dropDestination(for:isEnabled:action:)](<view/dropdestination(for_isenabled_action_).md>) 修饰符，以处理来自你 App 其他部分或其他 App 的放置操作。当放置目标修饰符包裹重新排列容器修饰符时，容器会处理容器内的拖放重排操作，而放置目标则处理用户在容器外发起的拖放操作。

在放置操作闭包内，调用 [reorderDestination(for:in:)](<dropsession/reorderdestination(for_in_).md>) 来查找用户相对于现有视图放置视图的位置。在下面的示例中，当该方法返回 [ReorderDifference.Destination.Position.before(_:)](<reorderdifference/destination-swift.struct/position-swift.enum/before(__).md>) 时，表示用户把一个或多个 `Photo` 表示放在了 `index` 处 `Photo` 实例所代表的视图之前。在这种情况下，你把放入的项目插到 `index` 处的项目之前。当该方法返回 [ReorderDifference.Destination.Position.end](reorderdifference/destination-swift.struct/position-swift.enum/end.md) 时，表示用户把一个或多个 `Photo` 表示放在了最后一个视图之后，因此你把放入的项目追加到集合末尾。下面的代码演示了这两种情况：

```swift
@State private var photos: [Photo] = loadPhotos()

var body: some View {
    VStack {
        ...
    }
    .reorderContainer(for: Photo.self) { difference in
        move(difference: difference)
    }
    .dragContainer(for: Photo.self) { photoID in
        guard let photo = photos.first(where: { $0.id == photoID }) else {
            return []
        }
        return [photo]
    }
    .dropDestination(for: Photo.self) { items, session in
        if let destination = session.reorderDestination(for: Photo.ID.self),
           let index = model.index(for: destination) {
            photos.insert(contentsOf: items, at: index)
        } else {
            photos.append(contentsOf: items)
        }
        return true
    }
}
```

### 支持拖放到可重新排列容器中的单个项目上

将 [dropDestination(for:isEnabled:action:)](<view/dropdestination(for_isenabled_action_).md>) 修饰符添加到某个项目的视图上，让用户可以把其他 App 的项目直接放到你容器中的特定项目上。下面的代码展示了如何把放置目标添加到 `ForEach` 内部且同样配置为可重新排列的 `ItemView` 上：

```swift
HStack {
    ForEach(items) { item in
        ItemView(item)
            .dropDestination(for: Item.self, isEnabled: item.isFolder) { newItems, destination in ... }
    }
    .reorderable()
}
.reorderContainer(for: Item.self) { difference in ... }
```

使用 [dropDestination(for:isEnabled:action:)](<view/dropdestination(for_isenabled_action_).md>) 修饰符的 `isEnabled` 参数来限制放置目标接受哪些项目。上面的代码示例展示了如何只在项目的 `isFolder` 属性为 `true` 时才接受放置。

在 [dropDestination(for:isEnabled:action:)](<view/dropdestination(for_isenabled_action_).md>) 修饰符的 `action` 闭包中添加代码来用放入的项目更新你的模型，因为这可能与你在 [reorderContainer(for:isEnabled:move:)](<view/reordercontainer(for_isenabled_move_).md>) 闭包中处理重排模型更新的方式不同。当你的放置目标接受来自重新排列容器的项目时，请务必在把项目移动到该项目的数据集合时，将它们从源数据集合中移除。

### 动态启用和禁用重新排列

在通过网络同步更新时，或者在进行其他会让重新排列复杂化的视图更新时，你可能希望禁用重新排列。为此，请使用带有 `isEnabled` 参数的重新排列容器修饰符变体，并向该参数传递一个布尔属性来跟踪重新排列是否启用，如下例所示：

```swift
ScrollView {
    LazyVStack {
        ...
    }
    .reorderContainer(
        for: Photo.self,
        isEnabled: !model.isSaving
    ) { difference in
        model.apply(difference: difference)
    }
}
```

在该示例中，当 `isSaving` 为 `true` 时禁用重新排列。当模型完成保存并将 `isSaving` 改为 `false` 时，重新排列重新启用。

## 另请参阅

### 基础

- [使用 SwiftUI 采用拖放](adopting-drag-and-drop-using-swiftui.md) — 在列表、表格和自定视图中启用拖放交互。
- [让视图成为拖动源](making-a-view-into-a-drag-source.md) — 采用 draggable API 为拖放操作提供项目。
