---
title: Core Data 实用工具教程
apple_id: TP40001800
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreData
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataUtilityTutorial/Articles/06_runClass.html
archived_at: '2026-07-15T07:14:28.949685Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 实用工具教程](Introduction%20to%20Core%20Data%20Utility%20Tutorial.md)


[下一页](Listing%20Previous%20Runs.md)[上一页](Creating%20the%20Core%20Data%20Stack.md)

# 自定义托管对象类

本教程中的托管对象模型指定 Run 实体由一个自定义类 Run 来表示。本章将展示如何实现该类，以及如何定义一个只在新实例首次创建时才会被调用的初始化方法。

有多种不同的场景，你可能想在其中对托管对象进行初始化。你可能想在每次创建某个给定类的实例时都执行初始化，这种情况下你可以直接重写指定初始化方法（designated initializer）。但你也可能想在对象从持久化存储中被获取时执行不同的初始化——或者更常见的情况是，只在对象首次被创建时执行。Core Data 提供了专门的方法来应对这两种情况——分别是 `awakeFromFetch` 和 `awakeFromInsert`。本示例演示的是后一种情况：你想在新记录被创建时记录日期和时间，此后不再更新该值。

出于演示目的，在本示例中你将为进程 ID 属性使用一个标量（scalar）值。使用标量类型的实例变量有一个缺点，就是没有明确的方式来表示 `nil` 值。`NSKeyValueCoding` 协议定义了一个特殊方法——`setNilValueForKey:`——让你可以指定，当有代码尝试将某个标量值设为 `nil` 时应该发生什么。

第一步是为这个新类创建文件。如果你的托管对象模型是作为项目资源存在的，你本可以使用 New File 助手，从模型中的某个实体创建一个托管对象类。但在本例中并非如此，因此像创建任何其他 Objective-C 类一样创建这些文件即可。

你需要为托管对象的各个属性声明 property。Core Data 会在运行时自动为托管对象的 property 实现存取方法（accessor），因此通常你不需要自己实现它们。为了告诉编译器，这些存取方法将通过另一种机制提供，需要将这些 property 声明为 dynamic。

在 `awakeFromInsert` 方法中（参见[实现初始化方法](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbqfvbuqmrtgqwvgvzv)），你会在 Run 对象首次创建时为其 date 属性设置一个值。为了避免为这个新的日期记录一次撤销操作，你需要使用_原始存取方法（primitive accessor）_，而不是常规的 property 存取方法。设置原始存取方法不会发出[键值观察](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16)（KVO）变更通知，因而不会导致该变更被记录为一次独立的撤销事件。你可以通过声明一个名为 `primitive<PropertyName>` 的 property 来声明原始存取方法，因此对于 `date` 属性，其原始 property 就是 `primitiveDate`。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)创建 Run 类的基础实现

1. 在 Xcode 中，为 Run 类添加一个新的 Objective-C 类文件（.h 和 .m 文件）。
2. 完成 Run 类的接口。

   在 `Run.h` 文件中，将该类的父类设为 `NSManagedObject`，并声明 `date` 和 `processID` 这两个 property。导入 Core Data 框架的头文件。接口看起来应该是这样：

```objc
#import <CoreData/CoreData.h>

@interface Run : NSManagedObject

@property (strong) NSDate *date;
@property (assign) NSInteger processID;

@end
```
3. 原始 property 应该只被实现它们的类使用，因此不应公开声明。你可以在 `Run.m` 文件的一个类扩展（class extension）中"隐藏" `primitiveDate` 的声明。

   在 `Run.m` 文件的 `@implementation` 代码块之前，添加以下内容：

```objc
@interface Run ()
@property (strong) NSDate *primitiveDate;
@end
```
4. 指明这些 property 是 dynamic 的。

   在 `Run.m` 文件的 `@implementation` 代码块中，添加以下内容：

```objc
@dynamic date, primitiveDate, processID;
```


如果你使用标量值来表示某个属性，就应该使用键值编码来指定：当该值被设为 `nil` 时应该发生什么。你可以通过实现 `setNilValueForKey:` 方法来做到这一点。在本例中，只需将进程 ID 设为 `0`。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)处理 nil 值

- 实现一个合适的 `setNilValueForKey:` 方法。

  如果 key 是"processID"，就将 `processID` 设为 `0`。

```objc
- (void)setNilValueForKey:(NSString *)key {

    if ([key isEqualToString:@"processID"]) {
        self.processID = 0;
    }
    else {
        [super setNilValueForKey:key];
    }
}
```


`NSManagedObject` 提供了一个特殊的方法——[awakeFromInsert](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506548-awakefrominsert)——它只会在一个新的托管对象首次被创建时（严格来说，是在它被插入托管对象上下文时）被调用，而_不会_在它之后从持久化存储中被获取时调用。你可以在这里用它来记录新记录被创建的日期和时间（这样，当对象被获取时，该值就不会再被更新）。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)实现初始化方法

- 实现一个 `awakeFromInsert` 方法，将接收者的 date 设为当前日期和时间。

```objc
- (void) awakeFromInsert {
    [super awakeFromInsert];
    self.primitiveDate = [NSDate date];
}
```


要为某个给定实体创建一个新实例并将其插入托管对象上下文，你通常会使用 `NSEntityDescription` 的便捷方法 `insertNewObjectForEntityForName:inManagedObjectContext:`。使用这个便捷方法的好处就是——方便！不过在本例中，你将自己执行这些设置操作。有了这个新实例后，你可以将其进程 ID 设为当前进程的 ID，然后向托管对象上下文发送一条 save 消息，将该变更提交到持久化存储。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)创建并保存一个 Run 实体的实例

1. 在 `main` 源文件中，导入 Run 类的头文件。

```objc
#import "Run.h"
```
2. 在 main 函数中，在调用 `managedObjectContext()` 函数之后，创建一个 Run 类的新实例。

   你必须从托管对象模型中获取 Run 实体描述，这样才能告诉这个新的托管对象它是哪个实体的实例。

```objc
NSEntityDescription *runEntity = [[mom entitiesByName] objectForKey:@"Run"];
Run *run = [[Run alloc] initWithEntity:runEntity insertIntoManagedObjectContext:moc];
```
3. 获取当前进程的进程 ID，并设置 Run 对象的进程 ID。

```objc
NSProcessInfo *processInfo = [NSProcessInfo processInfo];
run.processID = [processInfo processIdentifier];
```
4. 通过保存托管对象上下文，将变更提交到持久化存储。

   检查是否有错误，如果发生错误则退出。

```objc
NSError *error;

if (![moc save: &error]) {
    NSLog(@"Error while saving\n%@",
        ([error localizedDescription] != nil) ? [error localizedDescription] : @"Unknown Error");
    exit(1);
}
```


构建并运行该工具。它应该能够无警告地编译通过。运行该工具时，不应记录任何错误。你应该会看到应用程序日志目录中创建了一个新文件。如果检查该文件，你应该能看到其中包含 run 对象的详细信息。

测试其他一些特性。将设置 Run 对象进程 ID 的那一行注释掉。构建并运行该工具。会发生什么（回忆一下，进程 ID 的默认值是 `-1`）？你是否看到了本地化的错误消息（在[添加本地化字典](Creating%20the%20Managed%20Object%20Model.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbqfvbuqmrrhewvgvzr)中定义）？使用键值编码将进程 ID 设为 `nil`。构建并运行该工具。同样，会发生什么？最后，把 `setNilValueForKey:` 方法也注释掉，再测试一次。

Run 类的声明和实现的完整清单如清单 5-2 所示。

__清单 5-1__  Run.h 文件的完整清单

```objc
#import <CoreData/CoreData.h>

@interface Run : NSManagedObject

@property (strong) NSDate *date;
@property (assign) NSInteger processID;

@end
```


__清单 5-2__  Run.m 文件的完整清单

```objc
#import "Run.h"


@interface Run ()
@property (strong) NSDate *primitiveDate;
@end


@implementation Run

@dynamic date, primitiveDate, processID;


- (void) awakeFromInsert
{
    [super awakeFromInsert];
    self.primitiveDate = [NSDate date];
}


- (void)setNilValueForKey:(NSString *)key
{
    if ([key isEqualToString:@"processID"]) {
        self.processID = 0;
    }
    else {
        [super setNilValueForKey:key];
    }
}

@end
```


main 函数如清单 5-3 所示。

__清单 5-3__  `main` 函数的代码清单

```objc
int main (int argc, const char * argv[]) {

    @autoreleasepool {
        NSManagedObjectModel *mom = managedObjectModel();
        NSLog(@"mom: %@", mom);

        if (applicationLogDirectory() == nil) {
            NSLog(@"Could not find application logs directory\nExiting...");
            exit(1);
        }

        NSManagedObjectContext *moc = managedObjectContext();

        NSEntityDescription *runEntity = [[mom entitiesByName] objectForKey:@"Run"];
        Run *run = [[Run alloc] initWithEntity:runEntity insertIntoManagedObjectContext:moc];

        NSProcessInfo *processInfo = [NSProcessInfo processInfo];
        run.processID = [processInfo processIdentifier];

        NSError *error;

        if (![moc save: &error]) {
            NSLog(@"Error while saving\n%@",
                ([error localizedDescription] != nil) ? [error localizedDescription] : @"Unknown Error");
            exit(1);
        }

        // 实现将继续……
    }
    return 0;
}
```

[下一页](Listing%20Previous%20Runs.md)[上一页](Creating%20the%20Core%20Data%20Stack.md)
