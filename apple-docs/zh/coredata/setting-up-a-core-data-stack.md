---
title: 配置 Core Data 栈
framework: Core Data
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/setting-up-a-core-data-stack
source_url: 'https://developer.apple.com/documentation/coredata/setting-up-a-core-data-stack'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/setting-up-a-core-data-stack.json'
content_hash: 'sha256:47330c722fa5de3e'
translated: true
---

> 导航：[技术](../technologies.md) · [Core Data](../coredata.md)

# 配置 Core Data 栈

<sub>文章</sub>

设置用于管理并持久化 App 内对象的类。

## 概述

按照[创建 Core Data 模型](creating-a-core-data-model.md)中的说明创建数据模型文件后，请设置协同支持 App 模型层的各个类。这些类统称为 Core Data 栈。

![](../../../attachments/5ae3a13612ee984aac0a82870723ef9d/media-3122928@2x.png)

<sub>示意图显示：一个持久化容器实例包含了托管对象模型、托管对象上下文以及一个连接到 App 各存储区的持久化存储协调器的引用。</sub>

- [NSManagedObjectModel](nsmanagedobjectmodel.md) 的一个实例代表 App 的模型文件，描述 App 中的类型、属性和关系。
- [NSManagedObjectContext](nsmanagedobjectcontext.md) 的一个实例追踪 App 类型实例的变化。
- [NSPersistentStoreCoordinator](nspersistentstorecoordinator.md) 的一个实例负责从存储区中保存和获取 App 类型的实例。
- [NSPersistentContainer](nspersistentcontainer.md) 的一个实例一次性完成模型、上下文和存储协调器的设置。

### 初始化持久化容器

通常你会将 Core Data 栈初始化为一个单例：

```swift
// 定义一个可观察类以封装所有 Core Data 相关功能。
class CoreDataStack: ObservableObject {
    static let shared = CoreDataStack()
    
    // 创建一个持久化容器作为惰性变量，以推迟实例化直到首次使用。
    lazy var persistentContainer: NSPersistentContainer = {
        
        // 将数据模型文件名传递给容器的初始化方法。
        let container = NSPersistentContainer(name: "DataModel")
        
        // 加载所有持久化存储，若不存在存储则创建一个。
        container.loadPersistentStores { _, error in
            if let error {
                // 妥善处理错误。但在开发过程中，使用
                // `fatalError(_:file:line:)` 会很有帮助。
                fatalError("Failed to load persistent stores: \(error.localizedDescription)")
            }
        }
        return container
    }()
        
    private init() { }
}
```

创建后，持久化容器会将其 [managedObjectModel](nspersistentcontainer/managedobjectmodel.md)、[viewContext](nspersistentcontainer/viewcontext.md) 和 [persistentStoreCoordinator](nspersistentcontainer/persistentstorecoordinator.md) 属性分别指向模型、上下文和存储协调器实例。

现在你可以在整个 App 中使用这个 Core Data 栈了。

### 注入托管对象上下文

创建一个 Core Data 栈的实例，并将其托管对象上下文注入到 App 环境中：

```swift
@main
struct ShoppingListApp: App {
    // 创建一个 Core Data 栈的可观察实例。
    @StateObject private var coreDataStack = CoreDataStack.shared
    
    var body: some Scene {
        WindowGroup {
            ContentView()
            // 将持久化容器的托管对象上下文
            // 注入到环境中。
                .environment(\.managedObjectContext,
                              coreDataStack.persistentContainer.viewContext)
        }
    }
}
```

在视图中使用环境属性包装器来访问托管对象上下文：

```swift
//#-code-listing(AccessManagedObjectContext) [Access the managed object context]
struct ContentView: View {
    // 从环境中获取托管对象上下文的引用。
    @Environment(\.managedObjectContext) private var viewContext

    // 用户界面的其余实现。
}
```

### 为栈添加功能

Core Data 栈是放置相关代码的便利位置，例如保存更改和删除持久化存储区中托管对象的方法：

```swift
extension CoreDataStack {
    // 添加一个便捷方法来提交对存储区的更改。
    func save() {
        // 验证上下文是否有未提交的更改。
        guard persistentContainer.viewContext.hasChanges else { return }
        
        do {
            // 尝试保存更改。
            try persistentContainer.viewContext.save()
        } catch {
            // 妥善处理错误。
            print("Failed to save the context:", error.localizedDescription)
        }
    }
    
    func delete(item: ShoppingItem) {
        persistentContainer.viewContext.delete(item)
        save()
    }
}
```

`save` 方法仅在存在变化时保存上下文，从而提升性能。

## 主题

### 旧式栈设置

- [手动配置 Core Data 栈](setting-up-a-core-data-stack-manually.md) — 手动创建 Core Data 所需各组件，以支持较早版本的 Apple 操作系统。

## 另请参阅

### 基础

- [创建 Core Data 模型](creating-a-core-data-model.md) — 使用数据模型文件定义 App 的对象结构。
- [Core Data 栈](core-data-stack.md) — 管理并持久化 App 的模型层。
- [处理 Core Data 中的不同数据类型](handling-different-data-types-in-core-data.md) — 为多种数据类型创建、存储和展示记录。
- [在两个 Core Data 存储区之间链接数据](linking-data-between-two-core-data-stores.md) — 将数据组织到两个不同的存储区中，并在它们之间建立链接。
