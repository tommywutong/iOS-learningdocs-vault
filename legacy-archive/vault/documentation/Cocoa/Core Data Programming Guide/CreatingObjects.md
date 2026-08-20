---
title: Core Data 编程指南
apple_id: TP40001075
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/CreatingObjects.html
archived_at: '2026-07-15T07:14:13.512698Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 编程指南](index.md)



## 创建并保存托管对象

在你定义好托管对象模型并在应用中初始化 Core Data 技术栈之后，就可以开始创建用于数据存储的对象了。

### 创建托管对象

一个 [NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject) 实例实现了 Core Data 模型对象所需的基本行为。`NSManagedObject` 实例需要两个要素：一个实体描述（一个 [NSEntityDescription](https://developer.apple.com/documentation/coredata/nsentitydescription) 实例）和一个托管对象上下文（一个 [NSManagedObjectContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext) 实例）。实体描述包含该对象所代表的实体名称，以及该实体的属性和关系。托管对象上下文相当于一个用于创建托管对象的草稿板。上下文会跟踪对象所做的更改以及对象之间的关系。

正如下面的示例所示，`NSEntityDescription` 类有一个类方法，它接受一个表示实体名称的字符串，以及一个指向 `NSManagedObject` 实例将要关联的 `NSManagedObjectContext` 的引用。该示例将返回的对象定义为一个 `AAAEmployeeMO` 对象。

Objective-C

1. `AAAEmployeeMO *employee = [NSEntityDescription insertNewObjectForEntityForName:@"Employee" inManagedObjectContext:[self managedObjectContext];`

Swift

1. `let employee = NSEntityDescription.insertNewObjectForEntityForName("Employee", inManagedObjectContext: managedObjectContext) as! EmployeeMO`

### 创建 NSManagedObject 子类

默认情况下，Core Data 会向你的应用返回 `NSManagedObject` 实例。不过，为模型中的每个实体定义 `NSManagedObject` 子类往往很有用处。具体来说，当你为实体创建 `NSManagedObject` 子类时，你可以定义该实体可用的属性以供代码补全使用，还可以为这些子类添加便利方法。

要创建 `NSManagedObject` 的子类，请在 Xcode 的 Core Data 模型编辑器中选中该实体，然后在数据模型检查器的 Entity 面板中，在 Class 字段填入名称。接着在 Xcode 中创建该子类。

Objective-C

1. `#import <CoreData/CoreData.h>`
3. `@interface AAAEmployeeMO : NSManagedObject`
5. `@property (nonatomic, strong) NSString *name;`
7. `@end`
9. `@implementation AAAEmployeeMO`
11. `@dynamic name;`
13. `@end`

Swift

1. `import UIKit`
2. `import CoreData`
3. `import Foundation`
5. `class EmployeeMO: NSManagedObject {`
7. `@NSManaged var name: String?`
9. `}`

`@dynamic` 标记告诉编译器，该变量将在运行时被解析。

在数据模型中定义好子类并将其添加到项目之后，你就可以在应用中直接引用它，从而提升应用代码的可读性。

### 保存 NSManagedObject 实例

创建 `NSManagedObject` 实例并不能保证它们会被持久化。在托管对象上下文中创建一个 `NSManagedObject` 实例之后，需要显式保存该上下文，才能将这些更改持久化到持久化存储中。

Objective-C

1. `NSError *error = nil;`
2. `if ([[self managedObjectContext] save:&error] == NO) {`
3. `NSAssert(NO, @"Error saving context: %@\n%@", [error localizedDescription], [error userInfo]);`
4. `}`

Swift

1. `do {`
2. `try managedObjectContext.save()`
3. `} catch {`
4. `fatalError("Failure to save context: \(error)")`
5. `}`

对 `NSManagedObjectContext` 调用 save 时，会接受一个指向 [NSError](https://developer.apple.com/documentation/foundation/nserror) 变量的引用，并且总是返回成功或失败。如果保存失败，重要的是把错误情况展示出来，以便能够加以纠正。展示错误情况的方式可以很简单，比如把错误输出到控制台，也可以很复杂，比如把错误信息呈现给用户。如果 save 方法返回成功，则不需要再查看错误变量。

[Initializing the Core Data Stack](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/InitializingtheCoreDataStack.html#//apple_ref/doc/uid/TP40001075-CH4-SW1)

[Fetching Objects](FetchingObjects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqnrnknltc)
