---
title: Core Data 编程指南
apple_id: TP40001075
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/FetchingObjects.html
archived_at: '2026-07-15T07:14:16.027562Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 编程指南](index.md)



## 获取对象

既然数据已经保存在 Core Data 持久化存储中，接下来就要使用 [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest) 来访问这些已有数据。从 Core Data 中获取对象，是该框架最强大的特性之一。

### 获取 NSManagedObject 实例

在本示例中，首先要构造一个 `NSFetchRequest`，用于描述你希望返回的数据。除了指定要返回的实体类型之外，本示例没有对数据附加其他任何要求。然后，在 [NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext) 上调用 [executeFetchRequest:error:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506672-fetch)，将请求以及一个指向错误的指针一并传入。

Objective-C

1. `NSManagedObjectContext *moc = …;`
2. `NSFetchRequest *request = [NSFetchRequest fetchRequestWithEntityName:@"Employee"];`
4. `NSError *error = nil;`
5. `NSArray *results = [moc executeFetchRequest:request error:&error];`
6. `if (!results) {`
7. `NSLog(@"Error fetching Employee objects: %@\n%@", [error localizedDescription], [error userInfo]);`
8. `abort();`
9. `}`

Swift

1. `let moc = …`
2. `let employeesFetch = NSFetchRequest(entityName: "Employee")`
4. `do {`
5. `let fetchedEmployees = try moc.executeFetchRequest(employeesFetch) as! [EmployeeMO]`
6. `} catch {`
7. `fatalError("Failed to fetch employees: \(error)")`
8. `}`

[executeFetchRequest:error:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506672-fetch) 方法有两种可能的结果。它要么返回一个包含零个或多个对象的 [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray) 对象，要么返回 `nil`。如果返回 `nil`，说明你收到了来自 Core Data 的错误，需要对其进行处理。如果数组存在，即便这个 `NSArray` 可能是空的，你也得到了该请求可能的结果。空的 `NSArray` 表示没有找到任何记录。

### 过滤结果

获取对象的真正灵活性体现在获取请求的复杂程度上。首先，你可以为获取请求添加一个 [NSPredicate](https://developer.apple.com/documentation/foundation/nspredicate) 对象，以缩小返回对象的数量。例如，如果你只想要 firstName 为 Trevor 的 Employee 对象，可以直接将谓词添加到 `NSFetchRequest`：

Objective-C

1. `NSString *firstName = @"Trevor";`
2. `[fetchRequest setPredicate:[NSPredicate predicateWithFormat:@"firstName == %@", firstName]];`

Swift

1. `let firstName = "Trevor"`
2. `fetchRequest.predicate = NSPredicate(format: "firstName == %@", firstName)`

除了缩小返回对象的范围之外，你还可以配置这些对象的返回方式。例如，你可以指示 Core Data 返回 [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) 实例，而不是完整的 [NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject) 实例。此外，你还可以配置 `NSFetchRequest`，让这些 `NSDictionary` 实例只包含 Employee 实体所拥有属性中的一个子集。

有关 [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest) 的更多信息，请参阅该类的文档。

[Creating and Saving Managed Objects](CreatingObjects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqnjnknltc)

[Creating and Modifying Custom Managed Objects](LifeofaManagedObject.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmjwfvjvomi)
