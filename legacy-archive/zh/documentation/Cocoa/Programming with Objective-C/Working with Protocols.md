---
title: 用 Objective-C 编程
apple_id: TP40011210
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/WorkingwithProtocols/WorkingwithProtocols.html
archived_at: '2026-07-15T07:18:02.108341Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [用 Objective-C 编程](About%20Objective-C.md)


[下一页](Values%20and%20Collections.md)[上一页](Customizing%20Existing%20Classes.md)

# 使用协议

在现实生活中，处理公务的人员在应对某些情况时，常常被要求遵循严格的程序。例如，执法人员在进行询问或收集证据时，必须"遵循协议（follow protocol）"。

在面向对象编程的世界中，能够为对象在给定情形下定义一组预期行为非常重要。举例来说，table view 期望能够与一个数据源对象通信，以了解需要显示哪些内容。这意味着数据源必须能响应 table view 可能发送的一组特定消息。

数据源可以是任意类的实例，比如一个视图控制器（在 OS X 上是 `NSViewController` 的子类，在 iOS 上是 `UIViewController` 的子类），或者一个专门的数据源类，它可能只是继承自 `NSObject`。为了让 table view 知道某个对象是否适合作为数据源，能够声明该对象实现了必要的方法就很重要。

Objective-C 允许你定义 _协议（protocol）_，用来声明某个特定情形下预期会用到的方法。本章介绍定义正式协议的语法，并说明如何将类接口标记为 _遵循（conforming）_ 某个协议，这意味着该类必须实现其中的必需方法。

类接口用来声明与该类关联的方法和属性。相比之下，协议则用来声明独立于任何特定类的方法和属性。

定义协议的基本语法如下所示：

```objc
@protocol ProtocolName
// 方法和属性列表
@end
```

协议可以包含实例方法和类方法的声明，也可以包含属性声明。

举例来说，设想一个用于显示饼图的自定义视图类，如[图 5-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqmjrfvjvona)所示。

__图 5-1__  一个自定义饼图视图

!

为了让这个视图尽可能可复用，所有关于信息的决策都应该交给另一个对象——数据源——来处理。这意味着同一个视图类的多个实例，只需与不同的数据源通信，就可以显示不同的信息。

饼图视图所需的最少信息包括分段的数量、每个分段的相对大小，以及每个分段的标题。因此，饼图的数据源协议可能如下所示：

```objc
@protocol XYZPieChartViewDataSource
- (NSUInteger)numberOfSegments;
- (CGFloat)sizeOfSegmentAtIndex:(NSUInteger)segmentIndex;
- (NSString *)titleForSegmentAtIndex:(NSUInteger)segmentIndex;
@end
```

饼图视图类的接口需要一个属性来跟踪数据源对象。这个对象可以是任意类，因此基本的属性类型会是 `id`。关于该对象唯一已知的信息是它遵循相关协议。

视图声明数据源属性的语法如下所示：

```objc
@interface XYZPieChartView : UIView
@property (weak) id <XYZPieChartViewDataSource> dataSource;
...
@end
```

Objective-C 使用尖括号来表示对协议的遵循。这个示例声明了一个弱属性，用于一个遵循 `XYZPieChartViewDataSource` 协议的通用对象指针。

通过在属性上指定所需遵循的协议，即便属性的基本类型是通用类型，如果你试图将该属性设置为一个不遵循该协议的对象，也会得到编译器警告。该对象究竟是 `UIViewController` 的实例还是 `NSObject` 的实例都无关紧要，重要的只是它遵循该协议，这意味着饼图视图知道自己可以向它请求所需的信息。

默认情况下，协议中声明的所有方法都是必需方法。这意味着任何遵循该协议的类都必须实现这些方法。

也可以在协议中指定 _可选（optional）_ 方法。这些方法只有在类需要时才需要实现。

举例来说，你可能决定饼图上的标题应该是可选的。如果数据源对象没有实现 `titleForSegmentAtIndex:` 方法，视图中就不应该显示任何标题。

你可以使用 `@optional` 指令将协议方法标记为可选，就像这样：

```objc
@protocol XYZPieChartViewDataSource
- (NSUInteger)numberOfSegments;
- (CGFloat)sizeOfSegmentAtIndex:(NSUInteger)segmentIndex;
@optional
- (NSString *)titleForSegmentAtIndex:(NSUInteger)segmentIndex;
@end
```

在这个例子中，只有 `titleForSegmentAtIndex:` 方法被标记为可选。之前的方法没有任何指令，因此被视为必需方法。

`@optional` 指令会应用于其后的所有方法，直到协议定义结束，或者遇到另一个指令（例如 `@required`）为止。你可以像这样为协议添加更多方法：

```objc
@protocol XYZPieChartViewDataSource
- (NSUInteger)numberOfSegments;
- (CGFloat)sizeOfSegmentAtIndex:(NSUInteger)segmentIndex;
@optional
- (NSString *)titleForSegmentAtIndex:(NSUInteger)segmentIndex;
- (BOOL)shouldExplodeSegmentAtIndex:(NSUInteger)segmentIndex;
@required
- (UIColor *)colorForSegmentAtIndex:(NSUInteger)segmentIndex;
@end
```

这个示例定义了一个包含三个必需方法和两个可选方法的协议。

如果协议中的某个方法被标记为可选，你必须在尝试调用它之前，先检查对象是否实现了该方法。

举例来说，饼图视图可能会像这样测试分段标题方法：

```objc
    NSString *thisSegmentTitle;
    if ([self.dataSource respondsToSelector:@selector(titleForSegmentAtIndex:)]) {
        thisSegmentTitle = [self.dataSource titleForSegmentAtIndex:index];
    }
```

`respondsToSelector:` 方法使用了一个[选择器](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)，它指的是方法在编译后对应的标识符。你可以使用 `@selector()` 指令并指定方法名称，来提供正确的标识符。

如果这个示例中的数据源实现了该方法，就会使用这个标题；否则，标题将保持为 `nil`。

如果你尝试在一个遵循上面所定义协议的 `id` 上调用 `respondsToSelector:` 方法，你会得到一个编译器错误，提示没有已知的实例方法。一旦你用协议限定了一个 `id`，所有的静态类型检查都会恢复；如果你尝试调用一个未在指定协议中定义的方法，就会得到错误。避免这个编译器错误的一种方法是让自定义协议采纳 `NSObject` 协议。

就像 Objective-C 类可以从超类继承一样，你也可以指定一个协议遵循另一个协议。

举例来说，最佳实践是让你的协议遵循 `NSObject` 协议（`NSObject` 的部分行为从其类接口中拆分到了一个单独的协议中；`NSObject` 类本身采纳了 `NSObject` 协议）。

通过表明你自己的协议遵循 `NSObject` 协议，你就是在表明任何采纳这个自定义协议的对象，也都会提供 `NSObject` 协议中每个方法的实现。因为你所使用的通常是 `NSObject` 的某个子类，所以你不需要担心自己提供这些 `NSObject` 方法的实现。不过，这种协议遵循方式在前面所描述的那种场景中很有用。

要指定一个协议遵循另一个协议，你需要用尖括号提供另一个协议的名称，就像这样：

```objc
@protocol MyProtocol <NSObject>
...
@end
```

在这个例子中，任何采纳 `MyProtocol` 的对象，实际上也就采纳了 `NSObject` 协议中声明的所有方法。

表明一个类采纳某个协议的语法同样使用尖括号，就像这样

```objc
@interface MyClass : NSObject <MyProtocol>
...
@end
```

这意味着 `MyClass` 的任何实例不仅会响应接口中专门声明的方法，`MyClass` 还会为 `MyProtocol` 中的必需方法提供实现。不需要在类接口中重新声明协议方法——采纳该协议就足够了。

如果你需要一个类采纳多个协议，可以用逗号分隔的列表来指定它们，就像这样：

```objc
@interface MyClass : NSObject <MyProtocol, AnotherProtocol, YetAnotherProtocol>
...
@end
```

一旦你表明了对某个协议的遵循，这个类就必须至少为每个必需的协议方法提供实现，以及你选择实现的任何可选方法。如果你没有实现任何必需方法，编译器会发出警告。

协议在 Cocoa 和 Cocoa Touch 对象中被用于各种不同的场景。例如，table view 类（OS X 上是 `NSTableView`，iOS 上是 `UITableView`）都使用一个数据源对象来提供它们所需的信息。两者都定义了各自的数据源协议，其使用方式与上面的 `XYZPieChartViewDataSource` 协议示例大致相同。这两个 table view 类还都允许你设置一个委托对象，该对象同样必须遵循相应的 `NSTableViewDelegate` 或 `UITableViewDelegate` 协议。委托负责处理用户交互，或者自定义某些条目的显示方式。

有些协议用来表明类之间的 _非层级相似性（non-hierarchical similarities）_。这些协议并不与特定类的要求相关联，而是与更通用的 Cocoa 或 Cocoa Touch 通信机制相关，这些机制可能被多个互不相关的类所采纳。

举例来说，许多框架的模型对象（比如 `NSArray` 和 `NSDictionary` 这样的集合类）都支持 `NSCoding` 协议，这意味着它们可以对自身的属性进行编码和解码，以便归档或作为原始数据分发。只要对象关系图中的每个对象都采纳了该协议，`NSCoding` 就能让把整个对象关系图写入磁盘变得相对容易。

一些 Objective-C 语言层面的特性也依赖于协议。举例来说，要使用快速枚举，一个集合必须采纳 `NSFastEnumeration` 协议，具体描述见[快速枚举让枚举集合变得简单](Values%20and%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnznknltgma)。此外，有些对象是可以被拷贝的，比如使用带有 `copy` 特性的属性时，具体描述见[拷贝属性维护自己的副本](Encapsulating%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnjnknltgni)。任何你尝试拷贝的对象都必须采纳 `NSCopying` 协议，否则会得到运行时异常。

协议在无法知道对象所属类、或者类需要保持隐藏的场景中也很有用。

举例来说，框架的开发者可能选择不公开框架内某个类的接口。因为类名未知，框架的 _使用者_ 就无法直接创建该类的实例。取而代之，框架中通常会指定另一个对象来返回一个现成的实例，就像这样：

```objc
    id utility = [frameworkObject anonymousUtility];
```

为了让这个 `anonymousUtility` 对象变得有用，框架的开发者可以发布一个协议，公开它的部分方法。即便没有提供原始的类接口——也就是说这个类依然保持匿名——这个对象仍然可以在有限的范围内使用：

```objc
    id <XYZFrameworkUtility> utility = [frameworkObject anonymousUtility];
```

如果你在编写一个使用 Core Data 框架的 iOS 应用，你很可能会遇到 `NSFetchedResultsController` 类。这个类旨在帮助数据源对象向 iOS 的 `UITableView` 提供存储的数据，让获取诸如行数之类的信息变得容易。

如果你正在处理的 table view 内容被拆分成多个分区，你也可以向 fetched results controller 询问相关的分区信息。`NSFetchedResultsController` 类不会返回一个包含这些分区信息的特定类，而是返回一个匿名对象，该对象遵循 `NSFetchedResultsSectionInfo` 协议。这意味着你依然可以查询该对象以获取所需信息，比如某个分区中的行数：

```objc
    NSInteger sectionNumber = ...
    id <NSFetchedResultsSectionInfo> sectionInfo =
            [self.fetchedResultsController.sections objectAtIndex:sectionNumber];
    NSInteger numberOfRowsInSection = [sectionInfo numberOfObjects];
```

尽管你不知道 `sectionInfo` 对象的类，但 `NSFetchedResultsSectionInfo` 协议规定它可以响应 `numberOfObjects` 消息。

[下一页](Values%20and%20Collections.md)[上一页](Customizing%20Existing%20Classes.md)

