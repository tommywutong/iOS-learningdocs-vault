---
title: Core Data 编程指南
apple_id: TP40001075
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/FrequentlyAskedQuestions.html
archived_at: '2026-07-15T07:14:16.538830Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 编程指南](index.md)



## 常见问题

### 托管对象上下文是在哪里创建的？

托管对象上下文从何而来，完全取决于具体应用程序。在使用 `NSPersistentDocument` 的基于文档的 Cocoa 应用程序中，持久化文档通常会创建该上下文，并通过 [managedObjectContext](https://developer.apple.com/documentation/appkit/nspersistentdocument/1396162-managedobjectcontext) 方法让你访问它。

在单窗口应用程序中，如果你使用标准的项目助手创建项目，应用程序委托（[NSApplicationDelegate](https://developer.apple.com/documentation/appkit/nsapplicationdelegate) 类的实例）同样会创建该上下文，并通过 `managedObjectContext` 方法让你访问它。不过在这种情况下，创建上下文（以及 Core Data 栈其余部分）的代码是显式的，会作为模板的一部分自动为你写好。

不要直接使用 [NSController](https://developer.apple.com/documentation/appkit/nscontroller) 子类的实例来执行获取操作。例如，不要专门为了执行一次获取操作而创建一个 [NSArrayController](https://developer.apple.com/documentation/appkit/nsarraycontroller) 实例。控制器（Controller）的职责是管理模型对象与应用程序界面之间的交互。在模型对象这一层，应直接使用托管对象上下文来执行获取操作。

### 如何用默认数据初始化一个存储？

这里需要考虑两个方面：创建数据，以及确保数据只被导入一次。

创建数据有几种方式：

- 创建一个包含默认数据的独立持久化存储，并将其作为应用程序资源包含进去。需要使用时，可以将整个存储复制到合适的位置，或者将默认存储中的对象复制到已有存储中。
- 对于小数据集，可以直接在代码中创建托管对象。
- 创建一个属性列表（property list）或其他基于文件的数据表示形式，并将其作为应用程序资源保存。需要使用时，打开该文件并解析其中的表示形式来创建托管对象。

  > [!NOTE]
  > 

确保默认数据只被导入一次，也有几种方式：

- 如果你使用的是 iOS，或者是为 OS X 创建一个非基于文档的应用程序，可以在应用程序启动时添加一项检查，判断你为应用程序存储指定的位置是否存在文件。如果不存在，就需要导入数据。
- 如果你正在创建一个基于文档的应用程序并使用 [NSPersistentDocument](https://developer.apple.com/documentation/appkit/nspersistentdocument)，可以在 [initWithType:error:](https://developer.apple.com/documentation/appkit/nsdocument/1515159-initwithtype) 中初始化默认数据。

如果存在这样一种可能性，即存储（因而文件）已经被创建，但数据尚未导入，你可以为存储添加一个元数据标志。检查元数据（使用 [metadataForPersistentStoreWithURL:error:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468915-metadataforpersistentstorewithur)）比执行一次获取操作更高效（而且不需要你硬编码任何默认数据值）。

### 如何将现有的 SQLite 数据库与 Core Data 一起使用？

不能直接这样做，除非你将现有的 SQLite 数据库导入到一个 Core Data 存储中。尽管 Core Data 支持 SQLite 作为其持久化存储类型之一，但该数据库格式是私有的。你不能使用原生 SQLite API 创建一个 SQLite 数据库，然后直接在 Core Data 中使用它。如果你有一个现有的 SQLite 数据库，需要将它导入到一个 Core Data 存储中。此外，不要使用原生 SQLite API 操作由 Core Data 创建的现有 SQLite 存储。

### 我有一个从实体 A 到实体 B 的一对多关系。如何获取与实体 A 的某个实例相关联的实体 B 的实例？

你不需要这样做。更准确地说，没有必要显式地 _获取_ 目标实例，你只需在实体 A 的实例上调用相应的键值编码方法或存取方法即可。如果该关系名为 widgets，并且你实现了一个具有相应命名存取方法的自定义类，那么只需这样写：

Objective-C

1. `NSSet *asWidgets = [instanceA widgets];`

Swift

1. `let asWidets = instanceA.widgets`

否则，使用键值编码：

Objective-C

1. `NSMutableSet *asWidgets = [instanceA mutableSetValueForKey:@"widgets"];`

Swift

1. `let asWidgets = instanceA.mutableSetValueForKey("widgets")`

### 如何按创建对象时的顺序获取对象？

持久化存储中的对象是无序的。通常你应该在控制器层或视图层施加顺序，依据的可以是创建日期之类的属性。如果你的数据中固有某种顺序，则需要显式地对其建模。

### 如何将一个托管对象从一个上下文复制到另一个上下文？

首先要注意，严格来说，你并不是在复制该对象，而是在概念上为持久化存储中同一份底层数据创建了一个额外的引用。

要将一个托管对象从一个上下文复制到另一个上下文，可以使用该对象的对象 ID，如下例所示。

Objective-C

1. `NSManagedObjectID *objectID = [managedObject objectID];`
2. `NSManagedObject *copy = [context2 objectWithID:objectID];`

Swift

1. `let objectID = managedObject.objectID`
2. `let copy = context2.objectWithID(objectID)`

### 我有一个键，其值依赖于相关实体中属性的值——如何确保当该属性值发生变化、或该关系被操作时，此键始终保持最新？

有许多情况下，一个属性的值依赖于另一个实体中一个或多个其他属性的值。如果某个属性的值发生变化，派生属性的值也应该被标记为已变化。如何确保为这些依赖属性发布键值观察通知，取决于你所使用的 OS X 版本以及关系的基数。

### macOS v10.5 及更高版本中的一对一关系

如果与相关实体存在一对一关系，要自动触发通知，可以重写 [keyPathsForValuesAffectingValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1414299-keypathsforvaluesaffectingvalue)，或者实现一个遵循 [keyPathsForValuesAffectingValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1414299-keypathsforvaluesaffectingvalue) 所定义的、用于注册依赖键的命名模式的方法。

例如，你可以像下面这样重写 [keyPathsForValuesAffectingValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1414299-keypathsforvaluesaffectingvalue)：

Objective-C

1. `+ (NSSet *)keyPathsForValuesAffectingValueForKey:(NSString *)key {`
2. `NSSet *keyPaths = [super keyPathsForValuesAffectingValueForKey:key];`
3. `if ([key isEqualToString:@"fullNameAndDepartment"]) {`
4. `NSSet *affectingKeys = [NSSet setWithObjects:@"lastName", @"firstName", @"department.deptName", nil];`
5. `keyPaths = [keyPaths setByAddingObjectsFromSet:affectingKeys];`
6. `}`
7. `return keyPaths;`
8. `}`

Swift

1. `class override public func keyPathsForValuesAffectingValueForKey(key: String) -> Set<String> {`
2. `var keyPaths = super.keyPathsForValuesAffectingValueForKey(key)`
3. `if key == "fullNameAndDepartment" {`
4. `let affectingKeys: Set = ["lastName", "firstName", "department.deptName"]`
5. `keyPaths = keyPaths.union(affectingKeys)`
6. `}`
7. `return keyPaths`
8. `}`

或者，为了达到同样的效果，你也可以直接实现 `keyPathsForValuesAffectingFullNameAndDepartment`，如下例所示：

Objective-C

1. `+ (NSSet *)keyPathsForValuesAffectingFullNameAndDepartment {`
3. `return [NSSet setWithObjects:@"lastName", @"firstName", @"department.deptName", nil];`
4. `}`

Swift

1. `class public func keyPathsForValuesAffectingFullNameAndDepartment() -> Set<String> {`
2. `return ["lastName", "firstName", "department.deptName"]`
3. `}`

### 一对多关系

[keyPathsForValuesAffectingValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1414299-keypathsforvaluesaffectingvalue) 方法不允许键路径中包含一对多关系。例如，假设你有一个 Department 实体，与 Employee 存在一对多关系（`employees`），而 Employee 有一个 `salary` 属性。你可能希望 Department 实体有一个 `totalSalary` 属性，它依赖于该关系中所有 Employee 的薪资总和。你 _不能_ 通过例如 `keyPathsForValuesAffectingTotalSalary` 并返回 `employees.salary` 作为键来实现这一点。

有两种可能的解决方案：

- 使用键值观察，将父对象（在本例中为 Department）注册为所有子对象（本例中为 Employee）相关属性的观察者。你必须在子对象被添加到该关系或从该关系中移除时，相应地添加或移除该父对象作为观察者（参见 [注册键值观察](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/Articles/KVOBasics.html#//apple_ref/doc/uid/20002252)）。在 [observeValueForKeyPath:ofObject:change:context:](https://developer.apple.com/documentation/objectivec/nsobject/1416553-observevalueforkeypath) 方法中，你需要在变化发生时更新依赖值，如下面的代码片段所示：

  Objective-C

  1. `- (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context {`
  3. `if (context != totalSalaryContext) {`
  4. `return [super observeValueForKeyPath:keyPath ofObject:object change:change context:context];`
  5. `}`
  6. `if ([keyPath isEqualToString:@"totalSalary"]) {`
  7. `[self setTotalSalary:[self valueForKeyPath:@"employees.@sum.salary"]];`
  8. `}`
  9. `// Deal with other observations and/or invoke super...`
  10. `}`

  Swift

  1. `override public func observeValue(forKeyPath keyPath: String?, of object: Any?, change: [NSKeyValueChangeKey : Any]?, context: UnsafeMutableRawPointer?) {`
  2. `switch (keyPath, context) {`
  3. `case ("totalSalary"?, totalSalaryContext?):`
  4. `self.totalSalary = self.value(forKeyPath: "employees.@sum.salary") as! NSNumber?`
  5. `default:`
  6. `return super.observeValue(forKeyPath: keyPath, of: object, change: change, context: context)`
  7. `}`
  8. `}`
- 你也可以将父对象注册为应用程序通知中心的观察者，观察其托管对象上下文。父对象应以类似于键值观察的方式，响应由子对象发布的相关变更通知。

### 在 Xcode 谓词生成器中，为什么获取属性谓词看不到任何属性？

如果你想在 Xcode 的谓词生成器中为一个获取属性创建谓词，却看不到任何属性，很可能是因为你还没有为该获取属性设置目标实体。

### Core Data 的效率如何？

在 Core Data 的整个开发过程中，工程团队将一个使用 Core Data 的通用应用程序的运行时性能，与一个未使用 Core Data 开发的类似应用程序进行了比较。总体而言，Core Data 的实现表现更好。不过仍然可能存在进一步优化的空间，团队也在持续积极地追求性能提升。关于如何尽可能高效地使用 Core Data 的讨论，参见 [性能](Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrvfvjvomi)。

### macOS

以下问题仅与在 OS X 中使用 Core Data 相关。

### 如何让 GUI 校验用户输入的数据？

当托管对象上下文收到 `save:` 调用时，Core Data 会校验所有托管对象。在基于文档的 Core Data 应用程序中，用户保存文档时会触发这一调用。要让 GUI 在数据输入过程中就进行校验，可以在 Interface Builder 的 Bindings 检查器中，为某个值绑定选择 Validates Immediately 选项。如果你通过编程方式建立绑定，则需要在绑定选项字典中，为键 [NSValidatesImmediatelyBindingOption](https://developer.apple.com/documentation/appkit/nsbindingoption/1458045-validatesimmediately) 提供一个值 `YES``true`（以 `NSNumber` 对象的形式）。参见 [绑定选项](https://developer.apple.com/library/archive/documentation/Cocoa/Reference/CocoaBindingsRef/Concepts/BindingsOptions.html#//apple_ref/doc/uid/20002304)。

关于如何编写自定义校验方法的详情，参见 [NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject) 的子类化说明。

### 当我从由数组控制器管理的详情表格视图中移除对象时，为什么它们没有从对象图中被移除？

如果数组控制器管理着某个关系目标处的对象集合，默认情况下，移除方法只是把当前选中项从该关系中移除。如果你希望被移除的对象也从对象图中删除，需要为 `contentSet` 绑定启用 Deletes Objects On Remove 选项。

### 在非文档应用程序中，如何免费获得撤销/重做功能？

在基于文档的 Core Data 应用程序中，标准的 `NSDocument` 撤销管理器会被文档托管对象上下文的撤销管理器取代。在 OS X 的非文档应用程序中，你的窗口的委托可以通过 [windowWillReturnUndoManager:](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419745-windowwillreturnundomanager) 委托方法提供托管对象上下文的撤销管理器。如果你的窗口委托有一个托管对象上下文的存取方法（如果你使用 Core Data Application 模板就是这种情况），那么你的 [windowWillReturnUndoManager:](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419745-windowwillreturnundomanager) 实现可能如下所示：

Objective-C

1. `- (NSUndoManager *)windowWillReturnUndoManager:(NSWindow *)sender {`
2. `return [[self managedObjectContext] undoManager];`
3. `}`

Swift

1. `func windowWillReturnUndoManager(window: NSWindow) -> NSUndoManager? {`
2. `return managedObjectContext!.undoManager`
3. `}`

[排查 Core Data 问题](TroubleshootingCoreData.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrwfvjvomi)
