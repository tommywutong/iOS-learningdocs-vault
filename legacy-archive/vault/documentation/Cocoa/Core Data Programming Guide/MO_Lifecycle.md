---
title: Core Data 编程指南
apple_id: TP40001075
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/MO_Lifecycle.html
archived_at: '2026-07-15T07:14:25.307154Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 编程指南](index.md)



## 托管对象与引用

引用决定了托管对象何时会从内存中释放，也影响了是什么导致它们被保留下来。

### 托管对象与上下文之间的弱引用

托管对象知道自己关联的是哪个托管对象上下文，托管对象上下文也知道自己包含哪些托管对象。不过，_默认情况下_，托管对象与其上下文之间的引用是弱引用。这意味着一般来说，你不能依赖上下文来确保某个托管对象实例长期存在，也不能依赖某个托管对象的存在来确保上下文长期存在。换句话说，仅仅因为你获取了某个对象，并不意味着它会一直存在。

这条规则的例外情况是：托管对象上下文会对任何发生变更的对象（插入、删除、更新）持有强引用，直到该待处理事务通过 `save:` 提交，或通过 [reset](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506807-reset) 或 [rollback](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506942-rollback) 被丢弃为止。请注意，撤销管理器也可能对已变更的对象持有强引用——参见 [Change Management](ChangeManagement.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrsfvjvomi)。

### 在托管对象与上下文之间建立强引用

你可以更改上下文的默认行为，将 [retainsRegisteredObjects](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506290-retainsregisteredobjects) 属性设为 `true`，使其确实对自己的托管对象持有强引用。这样做会让托管对象的生命周期依赖于该上下文的生命周期。如果你在内存中缓存较小的数据集，这种依赖关系会很方便。例如，假设该上下文控制着一组可能会持续存在、超出单次事件周期的临时对象，比如 macOS 应用中的一个 sheet，或 iOS 应用中的一个模态视图。如果你使用多个线程并在它们之间传递数据，让托管对象依赖于上下文同样很有用——例如，如果你正在执行后台获取，并将对象 ID 传递给主线程。后台线程需要对它为主线程预取的对象持有强引用，直到它知道主线程确实已经使用这些对象 ID，在主线程中将对应的本地实例故障化（fault in）为止。否则，这些对象可能会从内存中被释放，需要重新从磁盘获取。

使用一个单独的容器，只对你真正需要的那些托管对象持有强引用。你可以使用数组、字典，或者一个对这些托管对象持有强引用的对象控制器（例如 [NSArrayController](https://developer.apple.com/documentation/appkit/nsarraycontroller) 的实例）。你不再需要的托管对象随后会在可能的时候被释放，例如当相关关系被清除时（参见[打破对象之间的强引用](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmzrfvjvooi)）。

如果你已经使用完某个托管对象上下文，或者出于其他原因想要将某个上下文与其持久化存储协调器断开连接，_不要_将该上下文的协调器设为 `nil`。

正确做法是：直接放弃对该上下文的持有权，让它按正常方式被释放。

Objective-C

1. `[self setMyManagedObjectContext:nil];`

Swift

1. `myManagedObjectContext = nil`

### 打破对象之间的强引用

与托管对象和其托管对象上下文之间的默认行为不同，在托管对象之间的关系中，每个对象都会对与其相关联的一个或多个对象持有强引用。这种关系可能导致强引用循环，进而导致对象在内存中被保留的时间，远远超过它们实际有用的时间。为确保引用循环被打破，当你使用完某个对象后，可以使用托管对象上下文的 [refreshObject:mergeChanges:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506224-refreshobject) 方法，将该托管对象转变为一个故障（fault）。

你通常会使用 `refreshObject:mergeChanges:` 来刷新某个托管对象的属性值。如果 `mergeChanges` 标志为 `true`，该方法会将该对象的属性值，与持久化存储协调器中可获取到的对象属性值进行合并。但如果该标志为 `false`，该方法只会简单地把对象重新转变为一个故障，而不进行合并，这样会导致它与相关托管对象之间的强引用被打破。

在某个托管对象被释放之前，指向它的所有强引用都必须被移除，包括来自 Core Data 之外的强引用。另请参阅 [Change Management](ChangeManagement.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrsfvjvomi)。

### 变更与撤销管理中的强引用

在收到 `save:`、`reset`、`rollback` 或 `dealloc` 调用之前，或者在收到相应数量的撤销操作以撤销该变更之前，上下文会一直对存在待处理变更（插入、删除或更新）的托管对象持有强引用。如果一系列撤销调用导致某个对象上的所有变更都被撤销，该对象的强引用就会恢复为弱引用。

_与某个上下文关联的撤销管理器，会对任何已变更的托管对象持有强引用。_ 默认情况下，上下文的撤销管理器会维护一个不限长度的撤销/重做栈。为了限制你的应用程序的内存占用，请确保在合适的时机（使用 [removeAllActions](https://developer.apple.com/documentation/foundation/nsundomanager/1407442-removeallactions)）清空该上下文的撤销栈。

如果你不打算使用 Core Data 的撤销功能，可以通过将该上下文的撤销管理器设为 `nil`，来降低你的应用程序的资源需求。这对于后台工作线程，以及大型导入或批处理操作而言，可能尤其有益。

### 确保数据保持最新

如果两个应用程序在使用同一个数据存储，或者单个应用程序拥有多个持久化技术栈，那么某个托管对象上下文或持久化对象存储中的托管对象，就有可能与该数据仓库的内容失去同步。如果发生这种情况，你需要刷新托管对象中的数据，尤其是持久化对象存储（快照），以确保数据值是最新的。

### 刷新一个对象

那些属性值来自持久化存储的托管对象（已实现对象），以及待处理的更新、插入或删除对象，绝不会在没有开发者介入的情况下，因为一次获取操作而被更改。举个例子，假设你在一个编辑上下文中获取了一些对象并对其进行了修改；与此同时，在另一个编辑上下文中，你编辑了同一份数据并提交了变更。如果此后你在第一个编辑上下文中执行一次新的获取，返回同样的对象，你将看不到新提交的数据值——你看到的是这些既有对象当前在内存中的状态。

要刷新某个托管对象的属性值，可以使用托管对象上下文的 [refreshObject:mergeChanges:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506224-refreshobject) 方法。如果 `mergeChanges` 标志为 `true`，该方法会将该对象的属性值，与持久化存储协调器中可获取到的对象属性值进行合并。如果该标志设为 `false`，该方法只会简单地把对象重新转变为一个故障，而不进行合并，这同样会导致与其他相关托管对象之间的强引用被打破。因此，你可以使用这个方法，来精简你想保留在内存中的那部分对象图。

一个对象的"陈旧间隔"（staleness interval）是指必须经过多长时间，存储才会重新获取该快照。陈旧间隔只影响故障的触发；此外，它只与增量式（即 SQLite）存储相关。其他类型的存储永远不会重新获取，因为整个数据集都保存在内存中。

### 合并带有瞬态属性的变更

瞬态属性是指对象上一个不会被持久化到磁盘的属性。如果你在使用 [refreshObject:mergeChanges:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506224-refreshobject) 时将 `mergeChanges` 标志设为 `true`，那么在调用 [awakeFromFetch](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506424-awakefromfetch) 之后，所有瞬态属性都会恢复为刷新之前的值。这意味着，如果你有一个瞬态属性，其值依赖于某个会被刷新的属性，那么这个瞬态值就可能变得不同步。

设想这样一个应用：有一个 Person 实体，具有 `firstName` 和 `lastName` 两个属性，以及一个_缓存的_瞬态派生属性 `fullName`。（实际当中，缓存一个 `fullName` 属性的做法可能不太常见，但这个例子便于理解。）再假设 `fullName` 是在一个自定义的 [awakeFromFetch](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506424-awakefromfetch) 方法中计算并缓存的。

一位当前在持久化存储中名为"Sarit Smith"的员工，在两个托管对象上下文中被编辑：

- 在上下文一中，对应实例的 `firstName` 被改为"Fiona"，这导致缓存的 `fullName` 被更新为"Fiona Smith"，随后该上下文被保存。

  此时持久化存储中，该员工现在是"Fiona Smith"。
- 在上下文二中，对应实例的 `lastName` 被改为"Jones"，这导致缓存的 `fullName` 被更新为"Sarit Jones"。

  随后该对象以 `mergeChanges` 标志为 `true` 进行刷新。此次刷新从存储中获取到"Fiona Smith"。该刷新会按如下方式更新对象：

  - `firstName` 在刷新之前_没有_被修改；刷新会使它被更新为持久化存储中的新值，因此现在是"Fiona"。
  - `lastName` 在刷新之前_确实_被修改过；刷新之后，它会被设回其修改后的值——"Jones"。
  - _瞬态_值 `fullName` 在刷新之前也发生了变化。刷新之后，它的值被恢复为"Sarit Jones"。然而，正确的值本应是"Fiona Jones"。

这个例子说明，由于刷新前的值是在 [awakeFromFetch](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506424-awakefromfetch) 之_后_才被应用的，你不能依靠 [awakeFromFetch](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506424-awakefromfetch) 来确保某个瞬态值在刷新之后被正确更新（即便你这样做了，该值随后也会被覆盖）。在这种情况下，最好的解决方案是使用一个额外的实例变量，来记录刷新已经发生、且该瞬态值需要被重新计算。

[Using Core Data with Cocoa Bindings](CocoaBindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmjsfvjvomi)

[Creating Managed Object Relationships](HowManagedObjectsarerelated.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmjxfvjvomi)
