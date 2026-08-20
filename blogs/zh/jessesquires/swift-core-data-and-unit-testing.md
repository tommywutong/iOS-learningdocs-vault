---
title: Swift、Core Data 与单元测试
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2015/01/05/swift-coredata-and-testing/'
original_language: en
published: 2015-01-05
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:acfcad591275519f'
translated: true
---

> 原文：[Swift, Core Data, and unit testing](https://www.jessesquires.com/blog/2015/01/05/swift-coredata-and-testing/)　·　Jesse Squires

[Core Data](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/) 大概是 iOS 开发者既爱又恨的框架。它功能强大，却常常令人沮丧。不过，尽管存在诸多陷阱，它仍然是开发者中流行的工具——这很可能是因为 Apple 仍在继续[投入](https://developer.apple.com/videos/wwdc/2014/?id=225)并鼓励人们采用它，同时还有[众多](http://nshipster.com/core-data-libraries-and-utilities/)能让 Core Data 更易使用的开源[库](https://github.com/rosettastone/RSTCoreDataKit)。如果再加上单元测试，Core Data 用起来就更麻烦了。幸运的是，已有[成熟的技术](https://github.com/rosettastone/RSTCoreDataKit#unit-testing)可以方便你测试模型。要是再引入 [Swift](http://www.apple.com/swift/)，学习曲线又会变得更陡一些。

### 为托管对象（managed object）子类添加前缀

由于 Swift 类是有命名空间的，你必须用类被编译时所在模块的名称作为类名的前缀。你可以在 Xcode 中打开 `.xcdatamodeld` 文件，选择一个实体（entity），然后打开模型实体检查器（Model Entity Inspector）来完成此操作。

![Core Data namespace](https://www.jessesquires.com/img/blog/coredata_namespace.png)

<sub>在 Core Data 中使用 Swift 命名空间 / [来源](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/BuildingCocoaApps/WritingSwiftClassesWithObjective-CBehavior.html#//apple_ref/doc/uid/TP40014216-CH5-XID_56)</sub>

这当然很容易忘记，如果你忘了，就会看到这个错误：

```
CoreData: warning: Unable to load class named 'Person' for entity 'Person'.
Class not found, using default NSManagedObject instead.
```

没什么帮助，对吧？我第一次看到它时，迷惑了好几分钟才意识到自己忘了给类名加前缀。还有另一个陷阱。你必须在生成类**之后**添加模块名前缀，否则 Xcode 就无法正确创建这些类（或者根本创建不了）。这是一个 bug。

### 实现通用的托管对象扩展

你找到的大部分现有 Objective-C Core Data 库，即使不是逐字照搬，也多多少少会实现以下这些辅助方法。这些方法减轻了向 Core Data 插入新对象时的别扭感，并避免了[_字符串类型的_ Objective-C](http://corner.squareup.com/2014/02/objc-codegenutils.html) 写法。

```
@implementation NSManagedObject (Helpers)

+ (NSString *)entityName
{
    return NSStringFromClass([self class]);
}

+ (instancetype)insertNewObjectInContext:(NSManagedObjectContext *)context
{
    return [NSEntityDescription insertNewObjectForEntityForName:[self entityName]
                                         inManagedObjectContext:context];
}

@end
```

我决定在某个个人项目中使用 Swift，在设计 App 的模型层时，我的第一个想法就是用 Swift 重写这些方法。让我们看看会是什么样子。

```
extension NSManagedObject {

    class public func entityName() -> String {
        let fullClassName: String = NSStringFromClass(object_getClass(self))
        let classNameComponents: [String] = split(fullClassName) { $0 == "." }
        return last(classNameComponents)!
    }

    class public func insertNewObjectInContext(context: NSManagedObjectContext) -> AnyObject {
        return NSEntityDescription.insertNewObjectForEntityForName(entityName(), inManagedObjectContext: context)
    }

}
```

嗯。`entityName()` 函数变得不那么优雅了。记住，我们必须为 Core Data 的 Swift 类添加前缀，这意味着它们的完全限定名是 `<ModuleName>.<ClassName>` 的形式。所以我们必须解析出_实体名称_，也就是类名本身。这看起来很脆弱，可能不是个好主意。此外，我们还得使用来自 [Objective-C runtime 库](https://developer.apple.com/library/mac/documentation/Cocoa/Reference/ObjCRuntimeRef/index.html)的 `object_getClass()` 函数，这感觉有点脏——_即使在 Objective-C 中也是如此_。我一直尽可能避免使用这种 [runtime](http://nshipster.com/associated-objects/) [魔术](http://nshipster.com/method-swizzling/)，而是选择实际的设计模式。即使在 Swift 中，`NSStringFromClass()` 也感觉_不对劲_。一般来说，_仅仅重写我们**旧的** Objective-C 代码，我们能得到什么呢？_**并不多。**

尽管有这些问题，我决定暂时先放一放，这样我才能继续工作，并思考一种_更符合 Swift 风格_的设计。我继续构建模型类，搭建 Core Data 栈，并编写单元测试。令我非常惊讶的是，在运行单元测试时，使用上面的扩展函数竟然崩溃了。在 Application Target 中运行同样的代码，一切正常。经过更多调查后，我意识到自己刚刚发现了一个 Swift 编译器的 [bug](http://openradar.appspot.com/19368054)。你可以在 GitHub 上找到一个[示例项目](https://github.com/jessesquires/rdar-19368054)，它展示了这个 bug。问题在于，以下函数在项目的 Test Target 中会错误地返回 `nil`。

```
class func insertNewObjectForEntityForName(_ entityName: String,
                    inManagedObjectContext context: NSManagedObjectContext) -> AnyObject

//  示例
//  在 App Target 中返回有效的 Person 对象
//  在 Test Target 中返回 nil
let person = NSEntityDescription.insertNewObjectForEntityForName("Person", inManagedObjectContext: context) as? Person
```

看来以后也没必要再回头看这些函数了。我可以在 Application Target 中继续使用它们，但我仍然需要找到一种方法来解决在 Test Target 中初始化托管对象的问题。这并不理想。我更希望有一个能在两个 Target 中都起作用的单一解决方案。回到绘图板。

### 重新思考与重新设计

让我们重申一下我们要达到的目标。我们希望：

1.  找到一种便捷的方式来初始化托管对象，通过封装对 `NSEntityDescription` 的使用

    -   绕过 `NSEntityDescription.insertNewObjectForEntityForName(_, inManagedObjectContext:)` 中的 bug
    -   避免向初始化器传递字面实体名称，比如 `"Person"`
    -   避免上面提到的那些问题（使用 `object_getClass()` 和 `NSStringFromClass()`）
    -   符合 Swift 的范型并利用 Swift 的特性

满足上述所有条件的解决方案是一个便利初始化器（convenience initializer）：

```
class Person: NSManagedObject {

    convenience init(context: NSManagedObjectContext) {
        let entityDescription = NSEntityDescription.entityForName("Person", inManagedObjectContext: context)!
        self.init(entity: entityDescription, insertIntoManagedObjectContext: context)
    }

}
```

这与扩展中原有的类工厂函数非常相似。它接收一个 context 并返回一个托管对象。关于第 (2) 点，很明显这是如何解决有问题的 `NSEntityDescription` 类函数的。在 Swift 中，初始化器保证返回一个非空、类型化的实例，而 `insertNewObjectForEntityForName(_, inManagedObjectContext:)` 返回的是 `AnyObject`。我们完全避免了强制转换返回值。

你可能已经注意到了，实体名称（`"Person"`）是硬编码的。你得出这个方案无法通用化的结论是正确的。也就是说，**所有**你的托管对象子类都需要实现这个便利初始化器，并为实体名称提供自己的值。你可能会考虑调整一下，把这个便利初始化器移动到一个新的扩展中，并用一个类必须覆盖的 `entityName()` 函数来替换那个硬编码的字符串。不幸的是，由于 Swift 对[初始化器委派和两段式初始化](https://developer.apple.com/library/mac/documentation/Swift/Conceptual/Swift_Programming_Language/Initialization.html#//apple_ref/doc/uid/TP40014097-CH18-XID_324)的强制要求，这[行不通](https://github.com/jessesquires/rdar-19368054#swift-extensions-will-not-work)。

归根结底，我认为在你的每个托管对象子类中添加这 3 行代码，对于换取类型安全以及更纯粹、_更符合 Swift 风格_的设计来说是值得的。也许这最终可以通过 [mogenerator](https://github.com/rentzsch/mogenerator) 或类似工具实现自动化。Cocoa [也许正在消亡](http://nshipster.com/the-death-of-cocoa/)，但它肯定**还没死**。当我们用 Swift 面对这类挑战时，重要的是要记住：_Objective-C 的方式_并不总是 _Swift 的方式_。

---

**还有一件事。** 在试图寻找绕过 `NSEntityDescription` bug 的方法时，我找到了一种奇怪的方式让前面提到的扩展函数在 Test Target 中工作。我们知道，由于 Swift 的[访问控制（access control）](https://developer.apple.com/library/mac/documentation/Swift/Conceptual/Swift_Programming_Language/AccessControl.html#//apple_ref/doc/uid/TP40014097-CH41-XID_29)实现，Swift 中的单元测试是[棘手的](http://natashatherobot.com/swift-unit-testing-tips-and-tricks/)。Application Target 中的文件对 Test Target 不可用，因为它们是两个不同的模块。通常的策略是将你的文件添加到两个 Target 中。如果你不这样做，而是将你的托管对象子类设为 `public`，并在 Test Target 中导入它们（`import <AppTargetName>`），那么从 `NSEntityDescription.insertNewObjectForEntityForName(_, inManagedObjectContext:)` 进行类型转换就会成功。
