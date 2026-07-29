---
title: 从你的 App 中删除持久化数据
framework: SwiftData
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, Xcode 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/deleting-persistent-data-from-your-app
source_url: 'https://developer.apple.com/documentation/swiftdata/deleting-persistent-data-from-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/deleting-persistent-data-from-your-app.json'
content_hash: 'sha256:f149ae1b1cdb1b7b'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftData](../swiftdata.md)

# 从你的 App 中删除持久化数据

<sub>示例代码</sub>

探索使用 SwiftData 删除持久化数据的不同方式。

## 概述

数据驱动型 App 通常提供一种供用户删除数据的方式，本示例也不例外。它展示了从 SwiftData 模型容器中移除已存储数据的三种方式：

- 滑动删除
- 确认后删除
- 全部删除

> [!note] 注意
> 如果你想要了解如何使用 SwiftData 添加和编辑数据，请参阅[在你的 App 中添加和编辑持久化数据](adding-and-editing-persistent-data-in-your-app.md)。

## 滑动删除

该示例 App 展示了一个动物列表。用户可以通过滑动手势删除某个动物。例如，以下代码通过在 [`ForEach`](../swiftui/foreach.md) 上应用 [`onDelete(perform:)`](../swiftui/dynamicviewcontent/ondelete(perform_).md) 修饰符，为 `AnimalList` 视图添加了滑动删除选项：

```swift
private struct AnimalList: View {
    @Environment(NavigationContext.self) private var navigationContext
    @Environment(\.modelContext) private var modelContext
    @Query(sort: \Animal.name) private var animals: [Animal]

    var body: some View {
        @Bindable var navigationContext = navigationContext
        List(selection: $navigationContext.selectedAnimal) {
            ForEach(animals) { animal in
                NavigationLink(animal.name, value: animal)
            }
            .onDelete(perform: removeAnimals)
        }
    }
}
```

上述代码中的 [`onDelete(perform:)`](../swiftui/dynamicviewcontent/ondelete(perform_).md) 修饰符调用了自定义方法 `removeAnimals` 来从列表中移除一个或多个动物。该方法接收一个 [`IndexSet`](../foundation/indexset.md) 类型的参数，该参数标识了要删除的动物。然后，该方法遍历该索引集合，通过 [`ModelContext`](modelcontext.md) 的 [`delete(_:)`](<modelcontext/delete(__).md>) 方法删除每个动物。

```swift
private func removeAnimals(at indexSet: IndexSet) {
    for index in indexSet {
        modelContext.delete(animals[index])
    }
}
```

然而，该示例 App 的用户有可能删除当前选中的动物，因此 `removeAnimals` 方法需要在删除前取消选中该动物。更新后的 `removeAnimals` 方法使用 [`persistentModelID`](persistentmodel/persistentmodelid.md) 来判断要删除的动物是否也是当前选中的动物。如果是，则将选中的动物设为 `nil`。

```swift
private func removeAnimals(at indexSet: IndexSet) {
    for index in indexSet {
        let animalToDelete = animals[index]
        if navigationContext.selectedAnimal?.persistentModelID == animalToDelete.persistentModelID {
            navigationContext.selectedAnimal = nil
        }
        modelContext.delete(animalToDelete)
    }
}
```

该示例使用了 SwiftData 的自动保存功能，该功能在使用 [`modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)`](<../swiftui/view/modelcontainer(for_inmemory_isautosaveenabled_isundoenabled_onsetup_)-18hhy.md>) 修饰符创建 [`ModelContainer`](modelcontainer.md) 时默认为启用状态。如果禁用了此功能，则 `removeAnimals` 方法需要通过调用 [`ModelContext`](modelcontext.md) 的 [`save()`](<modelcontext/save().md>) 方法显式地保存更改，例如：

```swift
private func removeAnimals(at indexSet: IndexSet) {
    do {
	    for index in indexSet {
	        let animalToDelete = animals[index]
	        if navigationContext.selectedAnimal?.persistentModelID == animalToDelete.persistentModelID {
	            navigationContext.selectedAnimal = nil
	        }
	        modelContext.delete(animalToDelete)
	    }
        try modelContext.save()
    } catch {
        // 处理错误。
    }
}
```

> [!note] 注意
> 要禁用自动保存功能，在使用 [`modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)`](<../swiftui/view/modelcontainer(for_inmemory_isautosaveenabled_isundoenabled_onsetup_)-18hhy.md>) 修饰符创建模型容器时，将 `isAutoSaveEnabled` 参数设置为 `false`。你也可以通过将模型上下文的 [`autosaveEnabled`](modelcontext/autosaveenabled.md) 属性设置为 `false` 来禁用自动保存。

## 确认后删除

该示例 App 还允许用户通过点击 `AnimalDetailView` 在其工具栏中显示的“废纸篓”按钮来删除选中的动物。

```swift
struct AnimalDetailView: View {
    var animal: Animal?
    @State private var isDeleting = false
    @Environment(\.modelContext) private var modelContext
    @Environment(NavigationContext.self) private var navigationContext

    var body: some View {
        if let animal {
            AnimalDetailContentView(animal: animal)
                .navigationTitle("\(animal.name)")
                .toolbar {
                    Button { isDeleting = true } label: {
                        Label("Delete \(animal.name)", systemImage: "trash")
                            .help("Delete the animal")
                    }
                }
        } else {
            ContentUnavailableView("Select an animal", systemImage: "pawprint")
        }
    }
}
```

该按钮的动作将状态变量 `isDeleting` 设置为 `true`，从而显示如下代码描述的删除确认提示框：

```swift
.alert("Delete \(animal.name)?", isPresented: $isDeleting) {
    Button("Yes, delete \(animal.name)", role: .destructive) {
        delete(animal)
    }
}
```

确认删除请求后，确认按钮的动作调用自定义的 `delete` 方法。该方法将选中的动物设为 `nil`，然后通过调用 [`delete(_:)`](<modelcontext/delete(__).md>) 方法从模型上下文中删除该动物。

```swift
private func delete(_ animal: Animal) {
    navigationContext.selectedAnimal = nil
    modelContext.delete(animal)
}
```

如果 SwiftData 的自动保存功能已被禁用，则 `delete` 方法需要通过调用 `ModelContext` 的 [`save()`](<modelcontext/save().md>) 方法显式地保存更改，例如：

```swift
private func delete(_ animal: Animal) {
    do {
        navigationContext.selectedAnimal = nil
        modelContext.delete(animal)
        try modelContext.save()
    } catch {
        // 处理错误。
    }
}
```

## 全部删除

在数据驱动型 App 中，删除特定模型类型的所有项目并不常见，但有时拥有这个选项会很有帮助。例如，该示例 App 允许用户重新加载 App 自带的示例数据。重新加载示例数据会删除持久化存储中的所有动物分类和动物。

要删除特定模型类型的所有项目，请使用 [`ModelContext`](modelcontext.md) 的 [`delete(model:where:includeSubclasses:)`](<modelcontext/delete(model_where_includesubclasses_).md>) 方法。例如，以下代码在重新加载示例数据前删除了所有动物分类：

```swift
static func reloadSampleData(modelContext: ModelContext) {
    do {
        try modelContext.delete(model: AnimalCategory.self)
        insertSampleData(modelContext: modelContext)
    } catch {
        fatalError(error.localizedDescription)
    }
}
```

当删除所有动物分类时，SwiftData 也会删除这些分类中的所有动物。SwiftData 之所以知道要执行此级联删除，是因为 `AnimalCategory` 和 `Animal` 之间的关系使用了 [`Schema.Relationship.DeleteRule.cascade`](schema/relationship/deleterule-swift.enum/cascade.md) 删除规则。（有关完整的删除规则列表，请参阅 [`DeleteRule`](schema/relationship/deleterule-swift.enum.md)。）

```swift
import SwiftData

@Model
final class AnimalCategory {
    @Attribute(.unique) var name: String
    // `.cascade` tells SwiftData to delete all animals contained in the 
    // category when deleting it.
    @Relationship(deleteRule: .cascade, inverse: \Animal.category)
    var animals = [Animal]()
    
    init(name: String) {
        self.name = name
    }
}
```

要从你的 App 中删除所有持久化数据（而不仅仅是特定模型类型的数据），请使用 [`ModelContainer`](modelcontainer.md) 的 [`deleteAllData()`](<modelcontainer/deletealldata().md>) 方法。

## 另请参阅

### 模型生命周期

- [`ModelContainer`](modelcontainer.md) — 一个管理 App 架构和模型存储配置的对象。
- [`ModelContext`](modelcontext.md) — 一个使你能够获取、插入和删除模型，并将任何更改保存到磁盘的对象。
- [获取和筛选基于时间的模型更改](fetching-and-filtering-time-based-model-changes.md) — 跟踪数据存储中发生的所有插入、更新和删除操作，并将它们作为一系列按时间顺序排列的事务进行处理。
- [`HistoryDescriptor`](historydescriptor.md) — 一个描述获取历史数据时使用的条件以及（可选）排序顺序的类型。
- [使用撤销管理器还原数据更改](reverting-data-changes-using-the-undo-manager.md) — 自动记录用户在 SwiftUI App 中执行的数据更改操作，并允许他们撤销和重做这些更改。
- [在用户设备间同步模型数据](syncing-model-data-across-a-persons-devices.md) — 添加所需的功能并定义兼容的架构，以使 SwiftData 能够使用 iCloud 自动同步你的 App 模型数据。
- [并发支持](concurrencysupport.md) — 你用来以安全和隔离的方式访问模型属性并执行存储相关任务的类型。

## 下载

- [SwiftDataAnimals.zip](https://docs-assets.developer.apple.com/published/f84bac78ac34/SwiftDataAnimals.zip)
