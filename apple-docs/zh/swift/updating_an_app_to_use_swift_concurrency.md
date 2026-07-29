---
title: 更新 App 以使用 Swift 并发
framework: swift
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 15.0+, iPadOS 15.0+, Xcode 14.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/updating_an_app_to_use_swift_concurrency
source_url: 'https://developer.apple.com/documentation/swift/updating_an_app_to_use_swift_concurrency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/updating_an_app_to_use_swift_concurrency.json'
content_hash: 'sha256:9b9954d427819358'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md)

# 更新 App 以使用 Swift 并发

<sub>示例代码</sub>

通过重构代码以利用 Swift 中的异步函数，提升 App 的性能。

## 概述

> [!note] 注意
> 本示例代码项目与 WWDC21 讲座 [10194: Swift 并发：更新示例 App](../https_/developer.apple.com/wwdc21/10194.md) 相关联。

Swift 并发提供了一套标准的语言工具和技术用于并发编程。不过，你可能已经有一个使用其他框架和技术构建的现有并发项目。你不必一次性转换所有代码；相反，你可以使用特定的重构技术，逐段转换代码。

本示例提供了 Coffee Tracker App 的两个独立版本：

- 原始版本使用完成处理程序（completion handler）来查询 HealthKit SDK 以及响应 `CLKComplicationDataSource` 调用，并使用调度队列（dispatch queue）来隔离对内存的并发访问。有关原始版本的更多信息，请参阅[创建和更新复杂功能的时间线](../clockkit/creating-and-updating-a-complication-s-timeline.md)。
- 更新后的版本使用了 Swift 的并发特性，以提供更清晰的代码，并在编译时进行更好的错误检查。它将完成处理程序替换为 `async` 函数，并使用 Actor 来确保数据的安全访问。

观看讲座以了解逐步过程，然后比较这两个项目以查看差异。

### 配置示例代码项目

要将复杂功能添加到当前表盘，请先在模拟器中构建并运行示例代码项目，然后按照以下步骤操作：

1. 点击数码旋钮（Digital Crown）以退出 App 并返回表盘。
2. 使用触控板，用力按压表盘以进入编辑模式，然后轻点“自定”。
3. 向左滑动，直到配置屏幕高亮显示复杂功能。选择要修改的复杂功能。
4. 滚动到 Coffee Tracker 复杂功能，然后再次点击数码旋钮以保存更改。
5. 轻点 Coffee Tracker 复杂功能以返回 App。

有关设置表盘的更多信息，请参阅[在 Apple Watch 上更改表盘](../https_/support.apple.com/en-us/ht205536.md)。

配置并运行 Coffee Tracker App 后，你可以测试后台更新。确保 Coffee Tracker 复杂功能出现在当前表盘上。然后在模拟器中构建并运行 App，并按照以下步骤操作：

1. 使用 App 的主视图添加一种或多种饮品。
2. 点击数码旋钮将 App 发送到后台。
3. 打开“设置”，向下滚动到“健康”>“健康数据”>“营养”>“咖啡因”，以查看你添加到 App 的所有饮品。
4. 点击“删除咖啡因数据”以清除 HealthKit 中的所有咖啡因样本。
5. 导航回表盘。

Coffee Tracker 会在 15 分钟内更新复杂功能；但是，根据系统的当前状态，更新可能会延迟。

### 将完成处理程序转换为使用异步方法

`HealthKitController` 类型包含对 HealthKit SDK 的多次调用。在支持 Swift 并发的 SDK 中，框架为大多数之前需要完成处理程序的函数添加了 `async`-`await` 版本。你可以通过更新这些调用以使用 `async`-`await` 版本，从而移除完成处理程序。你通过添加 `await` 关键字来挂起（suspend） `store.save()` 操作。执行在 `await` 完成后恢复。`async` 函数也可以是 throwing 函数，你通过将 `try await` 前置到函数调用来调用它。使用 `do-catch` 语句包裹调用，而不是使用 `Error?` 类型作为完成处理程序的参数。

```swift
// 将样本保存到 HealthKit 存储中。
do {
    try await store.save(caffeineSample)
    self.logger.debug("\(mgCaffeine) mg Drink saved to HealthKit")
} catch {
    self.logger.error("Unable to save \(caffeineSample) to the HealthKit store: \(error.localizedDescription)")
}
```

在某些情况下，SDK 调用需要使用完成处理程序。例如，调用 [init(type:predicate:anchor:limit:resultsHandler:)](<../healthkit/hkanchoredobjectquery/init(type_predicate_anchor_limit_resultshandler_).md>) 需要完成处理程序，但需要 `await` 的调用是 [execute(_:)](<../healthkit/hkhealthstore/execute(__).md>)。

要在此类情况下 `await` 完成处理程序的结果，添加一个 `continuation`：

```swift
private func queryHealthKit() async throws -> ([HKSample]?, [HKDeletedObject]?, HKQueryAnchor?) {
    return try await withCheckedThrowingContinuation { continuation in
        // 创建一个谓词，仅返回在过去 24 小时内创建的样本。
        let endDate = Date()
        let startDate = endDate.addingTimeInterval(-24.0 * 60.0 * 60.0)
        let datePredicate = HKQuery.predicateForSamples(withStart: startDate, end: endDate, options: [.strictStartDate, .strictEndDate])
        
        // 创建查询。
        let query = HKAnchoredObjectQuery(
            type: caffeineType,
            predicate: datePredicate,
            anchor: anchor,
            limit: HKObjectQueryNoLimit) { (_, samples, deletedSamples, newAnchor, error) in
            
            // 查询结束时检查错误。
            if let error = error {
                continuation.resume(throwing: error)
            } else {
                continuation.resume(returning: (samples, deletedSamples, newAnchor))
            }
            
        }
        store.execute(query)
    }
}
```

为了在异步访问时保护控制器的存储属性，将 `HealthKitController` 从 `class` 类型改为 `actor`：

```swift
actor HealthKitController {
```

对同步函数中 `async` 函数的调用是通过创建新的异步任务（asynchronous task）来进行的，这些任务可以使用 `await` 等待完成：

```swift
// 处理后台刷新任务。
case let backgroundTask as WKApplicationRefreshBackgroundTask:
    
    Task {
        // 检查来自 HealthKit 的更新。
        let model = CoffeeData.shared
        
        let success = await model.healthKitController.loadNewDataFromHealthKit()
            
        if success {
            // 安排下一次后台更新。
            scheduleBackgroundRefreshTasks()
            self.logger.debug("Background Task Completed Successfully!")
        }
        
        // 将任务标记为已结束，并在必要时请求更新的快照。
        backgroundTask.setTaskCompletedWithSnapshot(success)
    }
```

### 将咖啡数据类放在主要 Actor 上

`CoffeeData` 类实现了 `ObservableObject` 并拥有一个 `@Published` 属性来为 SwiftUI 视图提供数据。为确保对该属性的所有更新都在主线程（main thread）上执行，请将该类型放在主要 Actor（main actor）上：

```swift
@MainActor
class CoffeeData: ObservableObject {
```

执行同步 IO 的两个方法——`load` 和 `save` 方法——被提取到一个单独的 `CoffeeDataStore` actor 中，该 actor 在主线程之外执行这些活动。位于主要 Actor 上的模型类型必须使用 `await` 来调用 `CoffeeDataStore` actor 上的方法，这允许在同步 IO 操作期间在主线程上执行其他工作。

这两个类型通过传递一个 `Drink` 值数组进行通信，由于 `Drink` 是一个结构体，因此它是一个值类型。加载方法返回一个饮品数组，而保存方法则将饮品数组作为参数。

为了异步执行所有方法，将 `currentDrinks` 属性的 `didSet` 操作替换为 `private(set)`，并添加一个名为 `drinksUpdated` 的新 `async` 方法。将设置器中的代码移动到新方法中。在任何设置 `currentDrinks` 属性的代码之后，使用 `await` 调用 `drinksUpdated`。

更新 `drinksUpdated()` 方法，以使用 `await` 调用 `CoffeeDataStore` actor。`CoffeeDataStore` actor 在后台线程上保存数据。

从 SwiftUI 视图中对 `CoffeeData` 对象的调用不需要使用 `await`，因为这些视图由于使用了 `@EnvironmentObject`，也位于主要 Actor 上。

### 用异步方法替换委托和完成处理程序

[CLKComplicationDataSource](../clockkit/clkcomplicationdatasource.md) 协议中用于配置 App 时间线的几个方法需要完成处理程序，你可以用它们的 `async` 等效方法来替换：

```swift
// 定义手表解锁时复杂功能是否可见。
func privacyBehavior(for complication: CLKComplication) async -> CLKComplicationPrivacyBehavior {
    // 这是潜在敏感数据。在锁屏上隐藏它。
    .hideOnLockScreen
}
```

## 另请参阅

### 标准库

- [Int](int.md) — 一个有符号整数值类型。
- [Double](double.md) — 一个双精度浮点值类型。
- [String](string.md) — 一个 Unicode 字符串值，是字符的集合。
- [Array](array.md) — 一个有序的随机访问集合。
- [Dictionary](dictionary.md) — 一个元素为键值对的集合。
- [Swift 标准库](swift-standard-library.md) — 解决复杂问题并编写高性能、可读性强的代码。
- [TicTacFish：使用分布式 Actor 实现游戏](tictacfish_implementing_a_game_using_distributed_actors.md) — 使用分布式 Actor 将你的 Swift 并发和基于 Actor 的 App 扩展到单个进程之外。

## 下载

- [UpdatingAnAppToUseSwiftConcurrency.zip](https://docs-assets.developer.apple.com/published/0196478241/UpdatingAnAppToUseSwiftConcurrency.zip)
