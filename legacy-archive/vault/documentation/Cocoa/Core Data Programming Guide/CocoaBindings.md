---
title: Core Data 编程指南
apple_id: TP40001075
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/CocoaBindings.html
archived_at: '2026-07-15T07:14:12.020433Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 编程指南](index.md)



## 将 Core Data 与 Cocoa Bindings 配合使用

> [!NOTE]
> 

Core Data 框架关注的是对象模型，而 Cocoa Bindings 关注的是用户界面。Cocoa Bindings 使你能够轻松保持用户界面与模型同步，并在模型、控制器与用户界面（MVC 中的视图）之间提供集成。Core Data 框架的设计目标之一，就是能够与 Cocoa Bindings 无缝协作，并增强其实用性。更多信息请参阅 _[Cocoa Bindings Reference](../Cocoa%20Bindings%20Reference/Introduction%20to%20Cocoa%20Bindings%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4ds2i)_。

一般来说，Cocoa Bindings 处理 Core Data 托管对象的方式，与处理其他 Cocoa 模型对象完全相同。Core Data 使用的谓词对象和排序描述符，与你处理非 Core Data 管理的数据时（例如在表格视图中展示数据）所使用的完全一致。Core Data 与 Cocoa Bindings 之间的这些相似之处，为你在整个应用中提供了一套一致的 API。

Core Data 与 Cocoa Bindings 在配置和操作上存在一些差异，本章将对此进行讨论。另请参阅 [Troubleshooting Core Data](TroubleshootingCoreData.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrwfvjvomi)，了解可能导致 Cocoa Bindings 与 Core Data 之间出现交互问题的相关细节：

- [Cannot access contents of an object controller after a nib is loaded](TroubleshootingCoreData.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrwfvjvomjr)
- [Table view or outline view contents not kept up-to-date when bound to an NSArrayController or NSTreeController object](TroubleshootingCoreData.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrwfvjvomju)

除上述例外情况之外，_[Cocoa Bindings Programming Topics](../Cocoa%20Bindings%20Programming%20Topics/Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3do2i)_ 中讨论和描述的一切内容，同样适用于基于 Core Data 的应用。无论是否使用 Core Data，配置和调试绑定所用的技巧都是相同的。

### Core Data 为控制器带来的增强

Core Data 主要在诸如 [NSObjectController](https://developer.apple.com/documentation/appkit/nsobjectcontroller) 和 [NSArrayController](https://developer.apple.com/documentation/appkit/nsarraycontroller) 这类控制器对象的配置方面，为 Cocoa Bindings 增加了新特性。Core Data 为这些类增加了以下功能：

- 一个用于所有获取、插入和删除操作的托管对象上下文引用。如果控制器的内容是一个托管对象或托管对象集合，你必须为该控制器绑定或设置托管对象上下文。
- 一个用于创建新对象的实体名称，用来代替内容对象类。
- 一个获取谓词的引用，在内容未被直接设置时，用于约束获取的内容以确定要设置的内容。
- Interface Builder 中的一个内容绑定选项（Deletes Objects On Remove）——如果内容绑定到某个关系上，该选项用于指定从控制器中移除的对象，是否除了从关系中移除之外，还要一并被删除。

### "自动准备内容"标志

如果某个控制器设置了 [automaticallyPreparesContent](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1534767-automaticallypreparescontent) 标志（例如通过 `setAutomaticallyPreparesContent:` 设置，或在 Interface Builder 中设置），控制器的初始内容会使用其当前的获取谓词，从其托管对象上下文中获取。如果未设置该标志，则数据不会从托管对象上下文中检索，直到 [prepareContent](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1534218-preparecontent) 被调用为止。无论是否使用 Core Data，`AutomaticallyPreparesContent` 标志在 [NSObjectController](https://developer.apple.com/documentation/appkit/nsobjectcontroller) 和 [NSArrayController](https://developer.apple.com/documentation/appkit/nsarraycontroller) 上都是可用的。

需要注意的重要一点是：控制器的获取操作是作为一个延迟操作执行的，它发生在控制器的托管对象上下文被设置之后（即 nib 加载之后）。因此，获取操作发生在 [awakeFromNib](https://developer.apple.com/documentation/objectivec/nsobject/1402907-awakefromnib) 和 [windowControllerDidLoadNib:](https://developer.apple.com/documentation/appkit/nsdocument/1515221-windowcontrollerdidloadnib) 被调用之后。如果你想在这两个方法中的任意一个里，对某个对象控制器的内容执行操作，这种执行顺序就可能带来问题，因为此时控制器的内容还是 `nil`。你可以通过使用 [fetchWithRequest:merge:error:](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1531782-fetch) 手动执行获取操作来解决这个问题。将 `nil` 作为获取请求参数传入即可使用默认请求，如以下代码片段所示：

Objective-C

1. `- (void)windowControllerDidLoadNib:(NSWindowController *)windowController`
2. `{`
3. `[super windowControllerDidLoadNib:windowController];`
5. `NSArrayController *arrayController = [self arrayController];`
6. `NSError *error = nil;`
7. `BOOL ok = [arrayController fetchWithRequest:nil merge:NO error:&error];`
8. `if (ok == NO) {`
9. `NSLog(@"Failed to perform fetch: %@", error);`
10. `abort();`
11. `}`
12. `}`

Swift

1. `override func windowControllerDidLoadNib(windowController: NSWindowController) {`
2. `super.windowControllerDidLoadNib(windowController)`
4. `do {`
5. `try arrayController.fetch(with: nil, merge: false)`
6. `} catch {`
7. `fatalError("Failed to perform fetch: \(error)")`
8. `}`
9. `}`

### 实体继承

如果你在 Core Data 获取请求中，将某个父实体指定为要获取的实体，获取操作会返回该实体及其子实体的所有匹配实例（参见 [Fetching Objects](FetchingObjects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqnrnknltc)）。作为一个推论，如果你为一个由 Core Data 支持的控制器指定了某个父实体，该控制器会获取该实体及其任何子实体的匹配实例。如果你指定的是一个抽象父实体，那么这个由 Core Data 支持的控制器就会获取具体子实体的匹配实例。

### 一对多关系的过滤谓词

有时你可能想为搜索字段设置一个过滤谓词，让用户能够基于某个一对多关系的目标对数组控制器的内容进行过滤。如果要在一对多关系中进行搜索，你需要在谓词中使用 `ANY` 或 `ALL` 操作符。例如，如果你想获取至少有一名员工名字为 Matthew 的部门，可以像下面这样使用 `ANY` 操作符：

Objective-C

1. `NSPredicate *predicate = [NSPredicate predicateWithFormat:`
2. `@"ANY employees.firstName like 'Matthew'"];`

Swift

1. `let predicate = NSPredicate(format: "ANY employees.firstName like 'Matthew'", argumentArray: nil)`

在搜索字段的谓词绑定中，你也使用同样的语法：

1. `ANY employees.firstName like $value`

不过，如果你想匹配前缀、后缀，或者两者都要匹配，情况就会更复杂一些——例如，你想查找至少有一名员工名字为 Matt、Matthew、Mattie，或任何以 Matt 开头的名字的部门。归根结底，你只需要添加通配符匹配即可：

Objective-C

1. `NSPredicate *predicate = [NSPredicate predicateWithFormat:`
2. `@"ANY employees.firstName like 'Matt*'"];`

Swift

1. `let predicate = NSPredicate(format: "ANY employees.firstName like 'Matt*'", argumentArray: nil)`

但是，你_不能_在搜索字段的谓词绑定中使用同样的语法：

1. `// does not work`
2. `ANY employees.firstName like '$value*'`

原因在 _[Predicate Programming Guide](../Predicate%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoobz)_ 中有所描述——在谓词格式字符串中加上引号，会阻止变量替换的发生。因此，在搜索字段的谓词绑定中，你必须先对任何通配符进行替换，如下例所示：

Objective-C

1. `NSString *value = @"Matt";`
2. `NSString *wildcardedString = [NSString stringWithFormat:@"%@*", value];`
3. `[[NSPredicate predicateWithFormat:@"ANY employees.firstName like %@", wildcardedString];`

Swift

1. `let value = "Matt"`
2. `let wildcardedString = "\(value)*"`
3. `let predicate = NSPredicate(format: "ANY employees.firstName like %@", wildcardedString)`

因此，由于 Interface Builder 与 [NSPredicate](https://developer.apple.com/documentation/foundation/nspredicate) 中通配符替换变量组合使用时存在的这一局限，你必须编写一些代码来支持通配符的替换。

> [!NOTE]
> 

[Integrating Core Data and Storyboards](CoreDataandStoryboards.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmjqfvjvomi)

[Managed Objects and References](MO_Lifecycle.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmzrfvjvomi)
