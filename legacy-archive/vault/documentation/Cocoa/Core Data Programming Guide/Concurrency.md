---
title: Core Data 编程指南
apple_id: TP40001075
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/Concurrency.html
archived_at: '2026-07-15T07:14:12.516285Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 编程指南](index.md)



## 并发

并发（concurrency）是指同时在多个队列上处理数据的能力。如果你选择在 Core Data 中使用并发，还需要考虑应用所处的环境。在多数情况下，AppKit 和 UIKit 并非线程安全的。在 macOS 上尤其如此，Cocoa Bindings 和控制器都不是线程安全的——如果你正在使用这些技术，多线程处理可能会变得相当复杂。

### Core Data、多线程与主线程

在 Core Data 中，托管对象上下文可以配合两种并发模式使用，分别由 [NSMainQueueConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/nsmainqueueconcurrencytype) 和 [NSPrivateQueueConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/nsprivatequeueconcurrencytype) 定义。

[NSMainQueueConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/nsmainqueueconcurrencytype) 专门用于你的应用界面，只能在应用的主队列上使用。

[NSPrivateQueueConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/nsprivatequeueconcurrencytype) 这种配置会在初始化时创建属于自己的队列，并且只能在该队列上使用。由于这个队列是 [NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext) 实例私有且内部的，因此只能通过 [performBlock:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506578-performblock) 和 [performBlockAndWait:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506364-performblockandwait) 方法来访问。

无论采用哪种情况，`NSManagedObjectContext` 实例的初始化方式都是相同的：

Objective-C

1. `NSManagedObjectContext *moc = [[NSManagedObjectContext alloc] initWithConcurrencyType:<#type#>];`

Swift

1. `let moc = NSManagedObjectContext(concurrencyType:<#type#>)`

初始化时传入的参数决定了返回的 `NSManagedObjectContext` 是哪种类型。

当你使用 [NSPersistentContainer](https://developer.apple.com/documentation/coredata/nspersistentcontainer) 时，viewContext 属性会被配置为 [NSMainQueueConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/nsmainqueueconcurrencytype) 类型的上下文，而与 [performBackgroundTask:](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640564-performbackgroundtask) 和 [newBackgroundContext](https://developer.apple.com/documentation/coredata/nspersistentcontainer/1640581-newbackgroundcontext) 相关联的上下文，则会被配置为 [NSPrivateQueueConcurrencyType](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextconcurrencytype/nsprivatequeueconcurrencytype) 类型。

### 使用私有队列支持并发

一般来说，应避免在主队列上执行与用户操作无关的数据处理工作。数据处理可能是 CPU 密集型的，如果在主队列上执行，会导致用户界面失去响应。如果你的应用需要处理数据，例如从 JSON 向 Core Data 导入数据，应创建一个私有队列上下文，并在该私有上下文中执行导入操作。下面的示例展示了具体做法：

Objective-C

1. `NSArray *jsonArray = …; //JSON data to be imported into Core Data`
2. `NSManagedObjectContext *moc = …; //Our primary context on the main queue`
4. `NSManagedObjectContext *private = [[NSManagedObjectContext alloc] initWithConcurrencyType:NSPrivateQueueConcurrencyType];`
5. `[private setParentContext:moc];`
7. `[private performBlock:^{`
8. `for (NSDictionary *jsonObject in jsonArray) {`
9. `NSManagedObject *mo = …; //Managed object that matches the incoming JSON structure`
10. `//update MO with data from the dictionary`
11. `}`
12. `NSError *error = nil;`
13. `if (![private save:&error]) {`
14. `NSLog(@"Error saving context: %@\n%@", [error localizedDescription], [error userInfo]);`
15. `abort();`
16. `}`
17. `[moc performBlockAndWait:^{`
18. `NSError *error = nil;`
19. `if (![moc save:&error]) {`
20. `NSLog(@"Error saving context: %@\n%@", [error localizedDescription], [error userInfo]);`
21. `abort();`
22. `}`
23. `}];`
24. `}];`

Swift

1. `let jsonArray = … //JSON data to be imported into Core Data`
2. `let moc = … //Our primary context on the main queue`
4. `let privateMOC = NSManagedObjectContext(concurrencyType: .PrivateQueueConcurrencyType)`
5. `privateMOC.parentContext = moc`
7. `privateMOC.performBlock {`
8. `for jsonObject in jsonArray {`
9. `let mo = … //Managed object that matches the incoming JSON structure`
10. `//update MO with data from the dictionary`
11. `}`
12. `do {`
13. `try privateMOC.save()`
14. `moc.performBlockAndWait {`
15. `do {`
16. `try moc.save()`
17. `} catch {`
18. `fatalError("Failure to save context: \(error)")`
19. `}`
20. `}`
21. `} catch {`
22. `fatalError("Failure to save context: \(error)")`
23. `}`
24. `}`

在这个示例中，一批数据最初是以 JSON 负载的形式接收到的。接着你创建了一个新的 [NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext)，并将其定义为私有队列。这个新上下文被设置为运行应用的主队列上下文的子上下文。之后你调用 [performBlock:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506578-performblock)，并在传给它的代码块内部，实际执行 [NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject) 的创建工作。当所有数据都被处理完毕并转换成 [NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject) 实例后，你在私有上下文上调用 save，这会把所有变更移动到主队列上下文中，而不会阻塞主队列。

如果使用 [NSPersistentContainer](https://developer.apple.com/documentation/coredata/nspersistentcontainer)，上面的示例还可以进一步简化：

Objective-C

1. `NSArray *jsonArray = …;`
2. `NSPersistentContainer *container = self.persistentContainer;`
3. `[container performBackgroundTask:^(NSManagedObjectContext *context) {`
4. `for (NSDictionary *jsonObject in jsonArray) {`
5. `AAAEmployeeMO *mo = [[AAAEmployeeMO alloc] initWithContext:context];`
6. `[mo populateFromJSON:jsonObject];`
7. `}`
8. `NSError *error = nil;`
9. `if (![context save:&error]) {`
10. `NSLog(@"Failure to save context: %@\n%@", [error localizedDescription], [error userInfo]);`
11. `abort();`
12. `}`
13. `}];`

Swift

1. `let jsonArray = …`
2. `let container = self.persistentContainer`
3. `container.performBackgroundTask() { (context) in`
4. `for jsonObject in jsonArray {`
5. `let mo = EmployeeMO(context: context)`
6. `mo.populateFromJSON(jsonObject)`
7. `}`
8. `do {`
9. `try context.save()`
10. `} catch {`
11. `fatalError("Failure to save context: \(error)")`
12. `}`
13. `}`

### 在队列之间传递引用

[NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject) 实例并不适合在不同队列之间传递。这样做可能会导致数据损坏，并使应用终止运行。当确实需要把一个托管对象引用从一个队列交接给另一个队列时，必须通过 [NSManagedObjectID](https://developer.apple.com/documentation/coredata/nsmanagedobjectid) 实例来完成。

你可以通过在 [NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject) 实例上调用 [objectID](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506848-objectid) 方法，来获取某个托管对象的托管对象 ID。

[Persistent Store Types and Behaviors](PersistentStoreFeatures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrtfvjvomi)

[Performance](Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrvfvjvomi)
