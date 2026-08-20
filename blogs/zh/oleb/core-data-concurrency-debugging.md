---
title: Core Data 并发调试
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/06/core-data-concurrency-debugging/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:27ae975a05a98c8d'
translated: true
---

> 原文：[Core Data Concurrency Debugging](https://oleb.net/blog/2014/06/core-data-concurrency-debugging/)　·　Ole Begemann

# Core Data 并发调试

在 iOS 8 和 OS X Yosemite 中，Core Data 具备了检测和报告违反其[并发模型](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSManagedObjectContext_Class/NSManagedObjectContext.html#//apple_ref/doc/uid/TP30001182-SW39)行为的能力。^[1](#fn:1) 我认为这是一项非常有价值的功能，因为从错误的队列访问托管对象上下文（managed object context）是一个容易犯的错误，而如果导致用户数据损坏，后果可能很严重。^[2](#fn:2)

在 Mac 上，Core Data [曾经提供过一个选项](https://developer.apple.com/library/mac/technotes/tn2124/_index.html#//apple_ref/doc/uid/DTS10003391-CH1-SECCOREDATA)来调试并发问题。然而，启用该功能需要开发者手动安装框架的特殊调试版本，而由于 Apple 没有保持其更新，该版本经常完全不可用。这根本算不上一个实用的解决方案。对于 iOS，Apple 一开始就根本没发布过调试库。

# 启用多线程断言

在 iOS 8 和 Yosemite 中，Core Data 框架原生支持并发调试。它的工作原理是：每当你的 App 从错误的派发队列访问托管对象上下文或托管对象（managed object）时，就会抛出一个异常。你可以通过在 Xcode 的方案编辑器中向 App 传递命令行参数 `-com.apple.CoreData.ConcurrencyDebug 1` 来启用这些断言。^[3](#fn:3)

[![在 Xcode 的方案编辑器中配置命令行参数](https://oleb.net/media/xcode-scheme-core-data-concurrency-debug.png)](https://oleb.net/media/xcode-scheme-core-data-concurrency-debug.png)

<sub>在 Xcode 中，将启动参数 `-com.apple.CoreData.ConcurrencyDebug 1` 添加到你的构建方案的 Run 操作中。</sub>

当你启动 App 时，你应当在控制台中看到一条消息，告知你断言已启用：

```
CoreData: annotation: Core Data multi-threading assertions enabled.
```

# 它是如何工作的？

让我们搭建一个非常简单的 Core Data 栈，来实际测试一下它的工作方式（而且是用 Swift！）。在这个示例里我使用的是内存存储，但它与 SQLite 的工作方式完全相同。另请注意，我省略了错误处理，这并不意味着你也应该这样做。

```
let objectModelURL = NSBundle.mainBundle().URLForResource("MyDataModel", withExtension: "momd")
let objectModel: NSManagedObjectModel? = NSManagedObjectModel(contentsOfURL: objectModelURL)
assert(objectModel)

let storeCoordinator: NSPersistentStoreCoordinator? = NSPersistentStoreCoordinator(managedObjectModel: objectModel)
assert(storeCoordinator)

let store: NSPersistentStore? = storeCoordinator!.addPersistentStoreWithType(NSInMemoryStoreType, configuration: nil, URL: nil, options: nil, error: nil)
assert(store)

// 设置一个使用私有队列并发的托管对象上下文
// backgroundContext 是 NSManagedObjectContext? 类型的属性
backgroundContext = NSManagedObjectContext(concurrencyType: .PrivateQueueConcurrencyType)
assert(backgroundContext)
backgroundContext!.persistentStoreCoordinator = storeCoordinator!
```

需要特别注意的一点是，我已将托管对象上下文设置为 `.PrivateQueueConcurrencyType` 类型的后台上下文。这意味着我不允许从主队列（或其他任何队列）访问此上下文。如果我非要这样做，会发生什么？（同样，在你的代码中不要省略 `save()` 方法的错误处理。）

```
// 在后台上下文中工作，而不使用 performBlock:
// 这应当会失败，因为我们违反了 Core Data 的并发契约。
let person = NSEntityDescription.insertNewObjectForEntityForName("Person", inManagedObjectContext: backgroundContext!) as NSManagedObject
person.setValue("John Appleseed", forKey: "name")
backgroundContext!.save(nil)
```

当我运行这段代码时，执行甚至未能到达 `save()` 调用。因为我从主线程调用 `.insertNewObjectForEntityForName()` 方法，并将私有队列上下文作为参数传入，这违反了 Core Data 的并发模型，所以框架在第一行就抛出了异常。

[![Xcode 6 显示 Core Data 多线程违规异常](https://oleb.net/media/xcode-core-data-multithreading-violation.png)](https://oleb.net/media/xcode-core-data-multithreading-violation.png)

<sub>当你违反 Core Data 的线程契约时，调试器会在 `+[NSManagedObjectContext __Multithreading_Violation_AllThatIsLeftToUsIsHonor__]:` 处停止。</sub>

## iOS 8 Beta 1 中的一个 Bug

我本应做的，是将所有对 `backgroundContext` 的访问都包装在一个 `block` 里，并传递给 [`performBlock:`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSManagedObjectContext_Class/NSManagedObjectContext.html#//apple_ref/doc/uid/TP30001182-SW45) 或 [`performBlockAndWait:`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSManagedObjectContext_Class/NSManagedObjectContext.html#//apple_ref/doc/uid/TP30001182-SW46)，这些方法会在上下文的私有派发队列上执行该 `block`：

```
// 使用 performBlockAndWait: 在后台上下文中工作。这应当能正常工作。
backgroundContext!.performBlockAndWait {
    let person = NSEntityDescription.insertNewObjectForEntityForName("Person", inManagedObjectContext: self.backgroundContext!) as NSManagedObject
    person.setValue("John Appleseed", forKey: "name")
    self.backgroundContext!.save(nil)
}
```

在我使用 iOS 8 beta 1 进行的测试中，这段代码通过了第一个断言，但在最后一行 `self.backgroundContext!.save(nil)` 处因多线程违规而失败。我认为这是当前 SDK beta 版本中的一个 bug，因为我并没有违反线程模型。其他开发者也看到了[相同的行为](https://devforums.apple.com/message/983107)。我已经向 Apple 报告了此问题，编号为 rdar://17266389，并希望尽快得到回复。

**2014 年 7 月 23 日更新：** 此 Bug 已在 Xcode 6 beta 4 中修复。

# GDCoreDataConcurrencyDebugging

我还应该提一下 Graham Dennis 的 [GDCoreDataConcurrencyDebugging 库](http://www.grahamdennis.me/blog/2013/09/09/debugging-concurrency-with-core-data/)，它运用了一些巧妙的方法交换（method swizzling）和动态派生子类（dynamic subclassing）来检测托管对象何时以无效的方式被访问。据我所知，该库只监视发送给 `NSManagedObject` 的消息，而不监视发送给 `NSManagedObjectContext` 的消息，但它看起来是一个很不错的选项，至少在我上面提到的那个 bug 被 Apple 修复之前是如此。

1. 来源：[WWDC 2014 讲座](https://developer.apple.com/videos/wwdc/2014/) 225，“What’s New in Core Data”。[↩︎](#fnref:1)
2. 事实上，[据 Core Data 专家 Marcus Zarra 称](https://forums.pragprog.com/forums/252/topics/12271)，iOS 6 和 OS X 10.8 曾经会对每一次线程违规抛出异常，但 Apple 不得不关闭该功能，因为它会导致生产中太多 App 崩溃。这应该能告诉你这类错误有多普遍。[↩︎](#fnref:2)
3. 确保勾选“Shared”选项，并将方案文件添加到版本控制中，如果你想与你的团队共享该方案的话。[↩︎](#fnref:3)
