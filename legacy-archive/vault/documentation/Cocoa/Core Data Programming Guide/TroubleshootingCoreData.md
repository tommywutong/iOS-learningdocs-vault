---
title: Core Data 编程指南
apple_id: TP40001075
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/TroubleshootingCoreData.html
archived_at: '2026-07-15T07:14:28.453998Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 编程指南](index.md)



## Core Data 故障排查

Core Data 建立在 Cocoa 其他部分所提供的功能之上。在诊断使用 Core Data 的应用程序出现的问题时，要注意区分：哪些问题是 Core Data 特有的，哪些问题源自其他框架的错误，或者与架构相关。例如，性能不佳未必是 Core Data 的问题，而可能是由于没有遵循标准的 Cocoa 内存管理或资源节约技巧所致。如果用户界面没有正确更新，这可能是由于 Cocoa Bindings 配置有误。

### 对象生命周期问题

### 合并错误

_问题：_ 你看到错误消息："`Could not merge changes`"（无法合并变更）。

_原因：_ 两个不同的托管对象上下文尝试更改同一份数据。这也称为乐观锁定失败。

_解决方法：_ 要么为该上下文设置一个合并策略，要么手动（以编程方式）解决这个冲突。你可以使用 [committedValuesForKeys:](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506771-committedvaluesforkeys) 获取某个对象当前已提交的值，也可以使用 `refreshObject:mergeChanges:` 将该对象重新故障化，这样下次访问它时，它的数据值会从持久化存储中重新获取。

### 将托管对象分配给不同的存储

_问题：_ 你看到一个类似下面这样的异常。

1. `<NSInvalidArgumentException> [<MyMO 0x3036b0>_assignObject:toPersistentStore:]:`
2. `Can't reassign an object to a different store once it has been saved.`

_原因：_ 你想要分配给某个存储的对象，已经被分配并保存到了另一个不同的存储中。

_解决方法：_ 要将一个对象从一个存储移动到另一个存储，你必须创建一个新实例，把旧对象的信息拷贝过去，将其保存到合适的存储中，然后删除旧的实例。

### 无法满足的故障

_问题：_ 你看到错误消息 `NSObjectInaccessibleException`；"Core Data could not fulfill a fault."（Core Data 无法满足某个故障。）

_原因：_ Core Data 试图实现（realize）的那个对象，已经从持久化存储中被删除。

_解决方法：_ 移除对该对象的所有引用，将其丢弃。

_详情：_ 这个问题至少可能在以下两种情况下发生：

第一种情况：

- 你的应用程序中，另一个对象最初对某个托管对象持有一个强引用。
- 你通过托管对象上下文删除了该托管对象。
- 你保存了该对象上下文的更改。

  此时，被删除的对象已经变成了一个故障。它并没有被销毁，因为那样做会违反内存管理的规则。

Core Data 会尝试实现这个已故障化的托管对象，但会失败，因为该对象已经从存储中被删除——也就是说，存储中已不再存在具有相同全局 ID 的对象。

第二种情况：

- 你从某个托管对象上下文中删除了一个对象。
- 该删除操作未能打破其他对象指向被删除对象的所有关系。
- 你保存了更改。

此时，如果你尝试触发另一个对象指向该被删除对象的关系所对应的故障，根据该关系的配置方式（这会影响该关系的存储方式），触发可能会失败。

关系的删除规则只影响从源对象指向其他对象的关系（包括反向关系）。如果不去获取大量对象（可能还毫无必要），Core Data 就没有办法高效地清理指向该对象的各个关系。

请记住，Core Data 的对象图是有方向的。也就是说，一个关系有一个源和一个目标。从源到目标的这条路径，并不必然意味着存在一个反向关系。因此，从这个意义上说，你需要确保自己在删除操作中正确地维护了对象图。

Core Data 使用反向关系来维护数据模型内部的引用完整性。如果不存在反向关系、且某个对象被删除了，你就需要手动清理该关系。

在实践中，一个设计良好的对象图并不需要太多手动的删除后清理工作。大多数对象图都有若干个入口点，实际上充当了遍历该对象图的根节点，大多数插入和删除事件都以这些节点为根，就像获取操作一样。这意味着删除规则已经为你完成了大部分工作。类似地，由于智能分组（smart group）和其他松耦合的关系，通常最好使用获取属性（fetched property）来实现，因此各种用于进入对象图的辅助集合，通常不需要在删除操作中被维护，因为通过获取关系找到的对象，本身就不具有"永久存在"这个概念。

### 托管对象已失效

_问题：_ 你看到一个类似下面这样的异常：

1. `<NSObjectInaccessibleException> [<MyMO 0x3036b0>_assignObject:toPersistentStore:]:`
2. `The NSManagedObject with ID:#### has been invalidated.`

_原因：_ 要么你移除了你正试图触发的故障所在的存储，要么该托管对象所属的上下文收到了一次 [reset](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506807-reset)。

_解决方法：_ 移除对该对象的所有引用，将其丢弃。如果你重新添加该存储，可以再次尝试获取该对象。

### 类不符合键值编码

_问题：_ 你看到一个类似下面这样的异常。

1. `<NSUnknownKeyException> [<MyMO 0x3036b0> valueForUndefinedKey:]:`
2. `this class is not key value coding-compliant for the key randomKey.`

_原因：_ 要么你使用了错误的键，要么你使用 `init` 而不是 [initWithEntity:insertIntoManagedObjectContext:](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506357-init) 初始化了你的托管对象。

_解决方法：_ 使用一个有效的键（仔细检查拼写和大小写——同时复习一下 _[Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)_ 中关于键值编码兼容性的规则）。确保你为 `NSManagedObject` 使用了指定初始化方法（参见 [initWithEntity:insertIntoManagedObjectContext:](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506357-init)）。

### 实体类不响应自定义方法的调用

_问题：_ 你定义了一个使用 `NSManagedObject` 自定义子类的实体，然后在代码中创建了该实体的一个实例，并调用了一个自定义方法，如以下代码片段所示：

Objective-C

1. `NSManagedObject *entityInstance = [NSEntityDescription insertNewObjectForEntityForName:@"MyEntity" inManagedObjectContext:moc];`
2. `[entityInstance setAttribute: newValue];`

Swift

1. `let entityInstance = NSEntityDescription.insertNewObjectForEntityForName("MyEntity", inManagedObjectContext: moc)`
2. `entityInstance.attribute = newValue`

你会得到类似这样的运行时错误：

1. `"2005-05-05 15:44:51.233 MyApp[1234] ***`
2. `-[NSManagedObject setNameOfEntity:]: selector not recognized [self = 0x30e340]`

_原因：_ 在模型中，你把该实体自定义类的名称拼错了。

_解决方法：_ 确保模型中自定义类名的拼写，与你所实现的自定义类的拼写一致。

### 自定义存取方法未被调用，键依赖关系未生效

_问题：_ 你为某个特定实体定义了一个 [NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject) 的自定义子类，并实现了自定义的存取方法（也许还有依赖键）。在运行时，这些存取方法没有被调用，依赖键也没有被更新。

_原因：_ 在模型中，你没有为该实体指定自定义类。

_解决方法：_ 确保模型中为该实体指定的是自定义类名，而不是 [NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject)。

### 获取相关的问题

### SQLite 存储无法配合排序使用

_问题：_ 你创建了一个使用 [NSString](https://developer.apple.com/documentation/foundation/nsstring) 所定义的比较方法的排序描述符，例如以下这样：

Objective-C

1. `NSSortDescriptor *mySortDescriptor = [[NSSortDescriptor alloc] initWithKey:@"lastName" ascending:YES selector:@selector(localizedCaseInsensitiveCompare:)];`

Swift

1. `let mySortDescriptor = NSSortDescriptor(key: "lastName", ascending: true, selector: #(localizedCaseInsensitiveCompare:))`

然后你将该描述符用于某个获取请求，或作为某个数组控制器排序描述符之一。运行时，你会看到一条类似以下的错误消息：

1. `NSRunLoop ignoring exception 'unsupported NSSortDescriptor selector:`
2. `localizedCaseInsensitiveCompare:' that raised during posting of`
3. `delayed perform with target 3e2e42 and selector 'invokeWithTarget:'`

_原因：_ 一个获取请求具体是如何执行的，取决于所使用的存储——参见 [Fetching Objects](FetchingObjects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqnrnknltc)。

_解决方法：_ 如果你是直接执行该获取的，不要使用基于 Cocoa 的排序运算符——而应在内存中对返回的数组进行排序。如果你使用的是数组控制器，可能需要创建 [NSArrayController](https://developer.apple.com/documentation/appkit/nsarraycontroller) 的子类，使其不将排序描述符传给数据库，而是在数据获取完成之后再进行排序。

### 保存相关的问题

### 由于实体为空而无法保存文档

_问题：_ 你有一个基于文档的 Core Data 应用程序，无法保存。当你尝试保存文档时，会得到一个异常：

1. `Exception raised during posting of notification. Ignored. exception: Cannot perform operation since entity with name 'Wxyz' cannot be found`

_原因：_ 这个错误是由某个处于 Entity 模式、但无法在与 Interface Builder 中所指定实体名称相关联的托管对象模型中访问到对应实体描述的 `NSObjectController`（或其子类）实例发出的。简而言之，你有一个处于 entity 模式、但实体名称无效的控制器。

_解决方法：_ 在 Interface Builder 中依次选中每个控制器，按 Command-1 显示检查器（inspector）。对每个控制器，确保检查器顶部的 Entity name 字段中填写了一个有效的实体名称。

### retainedDataForObjectID:withContext 中产生的异常

_问题：_ 你向某个上下文添加了一个对象。当你尝试保存文档时，会得到一个类似这样的错误：

1. `[date] My App[2529:4b03] cannot find data for a temporary oid: 0x60797a0 <<x-coredata:///MyClass/t8BB18D3A-0495-4BBE-840F-AF0D92E549FA195>x-coredata:///MyClass/t8BB18D3A-0495-4BBE-840F-AF0D92E549FA195>`

这个异常出现在 `-[NSSQLCore retainedDataForObjectID:withContext:]` 中，回溯（backtrace）看起来是这样的：

1. `#1 0x9599a6ac in -[NSSQLCore retainedDataForObjectID:withContext:]`
2. `#2 0x95990238 in -[NSPersistentStoreCoordinator(_NSInternalMethods) _conflictsWithRowCacheForObject:andStore:]`
3. `#3 0x95990548 in -[NSPersistentStoreCoordinator(_NSInternalMethods) _checkRequestForStore:originalRequest:andOptimisticLocking:]`
4. `#4 0x9594e8f0 in -[NSPersistentStoreCoordinator(_NSInternalMethods) executeRequest:withContext:]`
5. `#5 0x959617ec in -[NSManagedObjectContext save:]`

对 `_conflictsWithRowCacheForObject:` 的调用，是在把你要保存的对象，与数据库中最后缓存的版本进行比较。基本上，它是在检查是否有其他代码（线程、进程，或只是另一个托管对象上下文）在你不知情的情况下更改了这个对象。

Core Data 不会对新插入的对象执行这项检查，因为它们不可能已经存在于任何其他作用域中——它们还没有被写入数据库。

_原因：_ 你可能强行让一个新插入的对象失去了"已插入"状态，然后又对其进行了更改或删除。如果你把一个临时对象 ID 传给了 [objectWithID:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506197-object)，就可能发生这种情况。你也可能把一个已插入的对象传给了另一个托管对象上下文。

_解决方法：_ 根据根本原因不同，有若干种可能的解决方法：

- 不要把一个已插入（但尚未保存）的对象传给另一个上下文。只有已经保存过的对象才能在不同上下文之间传递。
- 不要对一个刚插入的对象调用 `refreshObject:`。
- 不要与一个你从未插入到上下文中的对象建立关系。
- 确保你为 `NSManagedObject` 的实例使用了指定初始化方法。

在保存之前（调用栈中的第 5 帧），确保该上下文的 [updatedObjects](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506985-updatedobjects) 和 [deletedObjects](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506699-deletedobjects) 集合中，所有成员的对象 ID，其 [isTemporaryID](https://developer.apple.com/documentation/coredata/nsmanagedobjectid/1391691-temporaryid) 都应返回 `false`。

### 调试获取操作

使用用户默认值 `com.apple.CoreData.SQLDebug`，将发送给 SQLite 的实际 SQL 语句记录到 `stderr`。（请注意，用户默认值的名称是区分大小写的。）例如，你可以将以下内容作为参数传给应用程序：

1. `-com.apple.CoreData.SQLDebug 1`

调试级别数字越高，产生的信息就越多，不过使用更高的数字，其效用可能会逐渐递减。

输出所提供的信息在调试性能问题时可能会很有用——尤其是它可能会告诉你，Core Data 何时在执行大量的小规模获取（例如逐个触发故障时）。与文件 I/O 类似，相比执行一次大规模获取，执行许多次小规模获取的代价更高。关于如何纠正这种情况的示例，请参阅 [Preventing a Fault from Firing](Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrvfvjvonq)。

> [!IMPORTANT]
> 

### 托管对象模型

### 你的应用程序产生消息"+entityForName: could not locate an NSManagedObjectModel"

_问题：_ 错误信息已经说得很清楚了——实体描述找不到一个可供访问实体信息的托管对象模型。

_原因：_ 该模型可能没有被包含在你的应用程序资源中。你可能在模型加载完成之前就尝试访问它。对该上下文的引用可能是 `nil`。

_解决方法：_ 确保该模型已包含在你的应用程序资源中，并且在 Xcode 中对应的项目 target 选项已被选中。

你所调用的类方法需要一个实体名称和一个托管对象上下文，实体正是通过该上下文获取模型的。基本上，Core Data 技术栈是这样的：

托管对象上下文 ---> 持久化存储协调器 ---> 托管对象模型

如果找不到托管对象模型，请确认以下几点：

- 托管对象上下文不是 `nil`。

  如果你是在一个 `.nib` 文件中设置对该上下文的引用，请确保相应的 outlet 或绑定设置正确。
- 如果你在自行管理 Core Data 技术栈，请确保在分配（alloc）之后，该托管对象上下文有一个与之关联的协调器（[setPersistentStoreCoordinator:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506618-persistentstorecoordinator)）。
- 持久化存储协调器拥有一个有效的模型。

### Bindings 集成

许多与绑定相关的问题并非 Core Data 所特有，这些内容在 [Troubleshooting Cocoa Bindings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/Concepts/Troubleshooting.html#//apple_ref/doc/uid/TP40002148) 中有讨论。本节描述一些可能由 Core Data 与绑定交互所导致的额外问题。

### nib 加载完成后无法访问对象控制器的内容

_问题：_ 在 `.nib` 文件加载完成后，你想对某个对象控制器（[NSObjectController](https://developer.apple.com/documentation/appkit/nsobjectcontroller)、[NSArrayController](https://developer.apple.com/documentation/appkit/nsarraycontroller) 或 [NSTreeController](https://developer.apple.com/documentation/appkit/nstreecontroller) 的实例）的内容执行某个操作，但该控制器的内容是 `nil`。

_原因：_ 该控制器的获取操作是作为一个延迟操作执行的，它发生在其托管对象上下文被设置（通过 nib 加载）之后——因此该获取发生在 [awakeFromNib](https://developer.apple.com/documentation/objectivec/nsobject/1402907-awakefromnib) 和 [windowControllerDidLoadNib:](https://developer.apple.com/documentation/appkit/nsdocument/1515221-windowcontrollerdidloadnib) 之后。

_解决方法：_ 使用 [fetchWithRequest:merge:error:](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1531782-fetch) 手动执行获取操作。参见 [Using Core Data with Cocoa Bindings](CocoaBindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmjsfvjvomi)。

### 无法使用数组控制器创建新对象

_问题：_ 你无法使用 `NSArrayController` 创建新对象。例如，当你点击分配给 `add:` 动作的按钮时，会得到一个类似以下的错误：

1. `2005-05-05 12:00:)).000 MyApp[1234] *** NSRunLoop`
2. `ignoring exception 'Failed to create new object' that raised`
3. `during posting of delayed perform with target 123456`
4. `and selector 'invokeWithTarget:'`

_原因：_ 在你的托管对象模型中，你可能为该实体指定了一个自定义类，但没有实现这个类。

_解决方法：_ 实现这个自定义类，或者指定该实体由 `NSManagedObject` 表示。

### 绑定到数组控制器的表格视图无法显示关系的内容

_问题：_ 你想在一个绑定到数组控制器的表格视图中显示某个关系的内容，但什么都没有显示，并且你得到了一个类似以下的错误：

1. `2005-05-27 14:13:39.077 MyApp[1234] *** NSRunLoop ignoring exception`
2. `'Cannot create NSArray from object <_NSFaultingMutableSet: 0x3818f0> ()`
3. `of class _NSFaultingMutableSet - consider using contentSet`
4. `binding instead of contentArray binding' that raised during posting of`
5. `delayed perform with target 385350 and selector 'invokeWithTarget:'`

_原因：_ 你把该控制器的 `contentArray` 绑定绑到了一个关系上。关系是用集（set）来表示的。

_解决方法：_ 把该控制器的 `contentSet` 绑定绑到这个关系上。

### 新对象没有被添加到表格视图中当前所选对象的关系里

_问题：_ 你有一个表格视图，展示某个实体的一组实例。该实体与另一个实体存在一个关系，后者的实例展示在第二个表格视图中。每个表格视图都由一个数组控制器管理。当你添加第二个实体的新实例时，它们没有被添加到第一个实体当前所选实例的关系中。

_原因：_ 这两个数组控制器之间没有关联。没有任何机制告诉第二个数组控制器关于第一个的信息。

_解决方法：_ 把第二个数组控制器的 `contentSet` 绑定，绑到指定第一个数组控制器所选内容的那个关系的键路径上。例如，如果第一个数组控制器管理的是 Department 实体，第二个数组控制器管理的是 Employee 实体，那么第二个数组控制器的 `contentSet` 绑定应该是 `[Department Controller].selection.employees`。

### 绑定到 NSArrayController 或 NSTreeController 对象的表格视图或大纲视图内容未保持最新

_问题：_ 你有一个表格视图或大纲视图，展示某个实体的一组实例。随着该实体新实例的添加和移除，表格视图没有保持同步。

_原因：_ 如果该控制器的内容是一个由你自己管理的数组，那么你可能没有以符合 KVO 规范的方式修改这个数组。

如果该控制器的内容是自动获取的，那么你很可能没有把该控制器设置为"Automatically prepare content"。

或者，该控制器可能配置不正确。

_解决方法：_ 如果该控制器的内容是一个由你自己管理的集合，请确保你以符合 KVO 规范的方式修改该集合。参见 [Troubleshooting Cocoa Bindings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/Concepts/Troubleshooting.html#//apple_ref/doc/uid/TP40002148)。

如果该控制器的内容是自动获取的，请在 Interface Builder 的 Attributes inspector 中为该控制器打开"Automatically prepares content"开关（另请参阅 [automaticallyPreparesContent](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1534767-automaticallypreparescontent)）。这样做意味着该控制器会跟踪其托管对象上下文中，针对其实体所发生的插入和删除。

同时也要检查该控制器是否配置正确（例如，你是否正确设置了实体）。

[Performance](Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrvfvjvomi)

[Frequently Asked Questions](FrequentlyAskedQuestions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrzfvjvomi)
