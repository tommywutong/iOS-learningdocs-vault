---
title: Core Data 实用工具教程
apple_id: TP40001800
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreData
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataUtilityTutorial/Articles/03_createModel.html
archived_at: '2026-07-15T07:14:28.911050Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 实用工具教程](Introduction%20to%20Core%20Data%20Utility%20Tutorial.md)


[下一页](The%20Application%20Log%20Directory.md)[上一页](Creating%20the%20Project.md)

# 创建托管对象模型

本章说明 Run 实体的具体内容，并展示如何创建托管对象模型。虽然通常在 Xcode 中创建模型最为简便，但在本教程中你将完全用代码创建模型。

Xcode 提供了一个数据建模工具，通常用它来定义应用程序的数据模式（完整信息参见 _[Xcode Tools for Core Data](../../Developer%20Tools/Xcode%20Tools%20for%20Core%20Data/Xcode%20Entity%20Modeling%20Tools%20for%20Core%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dqnbw)_）。 Xcode 的数据建模工具与 Interface Builder 类似，它能让你以图形化的方式创建一个复杂的[对象图](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectGraph.html#//apple_ref/doc/uid/TP40008195-CH54)，该对象图会被[归档](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Archiving.html#//apple_ref/doc/uid/TP40008195-CH1)，并在运行时解档。不使用 Interface Builder 也可以创建用户界面，但可能需要付出大量精力。同样，即便是相当简单的模型，也需要大量代码，因此本教程只使用了一个包含两个简单属性的实体。

Run 实体有两个属性：进程 ID 和该进程运行的日期。这两个属性都不是可选的——也就是说，如果实例要被视为有效，每个属性都必须有值（如果你试图保存一个没有值的实例，将会得到一个验证错误）。进程 ID 的默认值为 `-1`。结合验证规则，这确保了该值在运行时能被正确设置。你还必须指定用于表示该实体的类——在本示例中，你将使用一个名为“Run”的自定义类。

__表 2-1__  Attributes for the Run entity

| Name | Type | Optional | Default Value | Minimum Value |
| date | date | NO |  |  |
| processID | int | NO | -1 | 0 |

你原本可以在 Xcode 中创建模型，将其放入应用程序支持目录，并在运行时使用 NSManagedObjectModel 的 `initWithContentsOfURL:` 方法加载它。但本示例展示的是如何完全用代码创建模型。`managedObjectModel` 函数会创建 Run 实体及其相关属性，然后创建一个托管对象模型实例，并将 Run 实体添加进去。为了让示例更加完善，它还为模型添加了一个本地化字典——使用本地化字典意味着任何与该模型相关的日志消息通常都更易于理解。

`managedObjectModel` 函数在 main 函数中被使用，但其实现代码却放在 main 函数之后；因此你需要为 `managedObjectModel` 函数提供一个前向声明。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)声明 managedObjectModel 函数

- 在主源文件的顶部、`main` 函数之前，添加该函数的声明。

```objc
NSManagedObjectModel *managedObjectModel();
```

下一步是声明并创建 `managedObjectModel()` 函数的一个初步实现。该函数应判断托管对象上下文实例是否已经存在。如果已存在，直接返回它；如果不存在，则创建它，然后配置技术栈的其余部分。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)开始实现 managedObjectModel 函数

- 在主源文件中，开始实现 `managedObjectModel` 函数。

  该函数为模型本身声明了一个 static 变量（`mom`），如果它不为 `nil`，立即返回该变量。该函数最终应返回 `mom`——接下来的步骤将创建该模型及其所包含的实体。

  添加以下代码：

```objc
NSManagedObjectModel *managedObjectModel() {

    static NSManagedObjectModel *mom = nil;

    if (mom != nil) {
        return mom;
    }

    // 实现继续……
    return mom;
}
```

你应该把接下来几节（[创建 Run 实体](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbqfvbuqmrrhewugsscijcuerkk)、[添加属性](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbqfvbuqmrrhewugsscizbekssh)、[创建模型](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbqfvbuqmrrhewvgvzrgm)和[添加本地化字典](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbqfvbuqmrrhewvgvzr)）中描述的代码，添加到 return 语句之前（即注释"实现继续……"所在的位置）。

创建模型的第一步是创建 Run 实体，由 [NSEntityDescription](https://developer.apple.com/documentation/coredata/nsentitydescription) 的一个实例来表示。该实体描述同时指定了实体的名称，以及在运行时用于表示该实体实例的类名。在本例中，这两个名称都是"Run"。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)创建 Run 实体

- 创建实体描述对象，设置其名称和托管对象类名，并将其添加到模型中。

  添加以下代码：

```objc
NSEntityDescription *runEntity = [[NSEntityDescription alloc] init];
[runEntity setName:@"Run"];
[runEntity setManagedObjectClassName:@"Run"];
```


属性由 [NSAttributeDescription](https://developer.apple.com/documentation/coredata/nsattributedescription) 的实例来表示。你必须创建两个实例——一个用于 date，另一个用于进程 ID——并适当设置它们的特性。两者都需要一个名称和一个类型，且都不是可选的。进程 ID 的默认值为 `-1`。你还需要为进程 ID 的校验创建一个谓词。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)为 Run 实体添加属性

1. 创建 date 属性描述——其类型为 `NSDateAttributeType`，且不是可选的。

   添加以下代码：

```objc
NSAttributeDescription *dateAttribute = [[NSAttributeDescription alloc] init];

[dateAttribute setName:@"date"];
[dateAttribute setAttributeType:NSDateAttributeType];
[dateAttribute setOptional:NO];
```
2. 创建进程 ID 属性描述——其类型为 `NSInteger64AttributeType`，不是可选的，默认值为 `-1`。

   添加以下代码：

```objc
NSAttributeDescription *idAttribute = [[NSAttributeDescription alloc] init];

[idAttribute setName:@"processID"];
[idAttribute setAttributeType:NSInteger64AttributeType];
[idAttribute setOptional:NO];
[idAttribute setDefaultValue:@(-1)];
```
3. 为进程 ID 创建校验谓词；该属性本身的值必须大于零。

   以下代码等价于 `validationPredicate = [NSPredicate predicateWithFormat:@"SELF > 0"]`，但本示例延续了展示完整写法的一贯风格。

   添加以下代码：

```objc
NSExpression *lhs = [NSExpression expressionForEvaluatedObject];
NSExpression *rhs = [NSExpression expressionForConstantValue:@0];

NSPredicate *validationPredicate = [NSComparisonPredicate
                                        predicateWithLeftExpression:lhs
                                        rightExpression:rhs
                                        modifier:NSDirectPredicateModifier
                                        type:NSGreaterThanPredicateOperatorType
                                        options:0];
```
4. 为校验谓词添加错误字符串。

   每个校验谓词都需要一个对应的错误字符串。通常错误字符串应该经过适当的本地化。你既可以在此处直接提供一个本地化的表示（例如使用 [NSLocalizedString](https://developer.apple.com/documentation/foundation/nslocalizedstring)），也可以为该模型提供一个本地化字典。后一种方式将在下一节（[添加本地化字典](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbqfvbuqmrrhewvgvzr)）中展示。你需要为该属性描述提供一个谓词数组和一个错误字符串数组。在本例中，每个数组都只包含一个对象。

   添加以下代码：

```objc
NSString *validationWarning = @"Process ID < 1";
[idAttribute setValidationPredicates:@[validationPredicate]
        withValidationWarnings:@[validationWarning]];
```
5. 将这些属性添加到该实体。

   添加以下代码：

```objc
[runEntity setProperties:@[dateAttribute, idAttribute]];
```


接下来你要创建托管对象模型本身，并将 Run 实体添加进去。一个模型可以包含多个实体，因此设置实体的方法接受的是一个实体数组。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)创建模型

- 创建该模型，并将 Run 实体以数组形式添加到该模型中。

  添加以下代码：

```objc
mom = [[NSManagedObjectModel alloc] init];
[mom setEntities:@[runEntity]];
```


你可以设置一个本地化字典，为该模型相关的实体、属性和错误字符串提供本地化的字符串值。键和值的模式在 [setLocalizationDictionary:](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506846-localizationdictionary) 的 API 参考文档中有说明。你用作错误键的字符串，必须与你为对应校验谓词所指定的字符串相同。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)为模型添加本地化字典

- 创建本地化字典，并将其设置到该模型中：

  添加以下代码：

```objc
NSDictionary *localizationDictionary = @{
                        @"Property/date/Entity/Run":@"Date",
                        @"Property/processID/Entity/Run":@"Process ID",
                        @"ErrorString/Process ID < 1":@"Process ID must not be less than 1"};

[mom setLocalizationDictionary:localizationDictionary];
```


为了能够测试目前为止的实现，实例化该托管对象模型，并记录其模型描述。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)测试目前为止的实现

1. 创建一个托管对象模型的实例，并记录其描述。

   在 `main` 函数中，`@autoreleasepool` 代码块内，声明一个 `NSManagedObjectModel` 类型的变量，并将其值赋为调用 `managedObjectModel` 函数的结果。使用 `NSLog` 打印该模型的描述。

```objc
NSManagedObjectModel *mom = managedObjectModel();
NSLog(@"The managed object model is defined as follows:\n%@", mom);
```
2. 构建并运行该项目。

   该项目应该能够无警告地编译通过。记录下来的模型文件描述中，应包含你所定义的实体和属性。在这个阶段，该模型尚未被使用，因此其 `isEditable` 状态仍为 true。

`managedObjectModel` 函数的完整清单如清单 2-1 所示。

__清单 2-1__  `managedObjectModel` 函数的完整清单

```objc
NSManagedObjectModel *managedObjectModel() {

    static NSManagedObjectModel *mom = nil;

    if (mom != nil) {
        return mom;
    }

    NSEntityDescription *runEntity = [[NSEntityDescription alloc] init];
    [runEntity setName:@"Run"];
    [runEntity setManagedObjectClassName:@"Run"];

    NSAttributeDescription *dateAttribute = [[NSAttributeDescription alloc] init];

    [dateAttribute setName:@"date"];
    [dateAttribute setAttributeType:NSDateAttributeType];
    [dateAttribute setOptional:NO];


    NSAttributeDescription *idAttribute = [[NSAttributeDescription alloc] init];

    [idAttribute setName:@"processID"];
    [idAttribute setAttributeType:NSInteger64AttributeType];
    [idAttribute setOptional:NO];
    [idAttribute setDefaultValue:@(-1)];

    NSExpression *lhs = [NSExpression expressionForEvaluatedObject];
    NSExpression *rhs = [NSExpression expressionForConstantValue:@0];

    NSPredicate *validationPredicate = [NSComparisonPredicate
                                            predicateWithLeftExpression:lhs
                                            rightExpression:rhs
                                            modifier:NSDirectPredicateModifier
                                            type:NSGreaterThanPredicateOperatorType
                                            options:0];

    NSString *validationWarning = @"Process ID < 1";

    [idAttribute setValidationPredicates:@[validationPredicate]
                 withValidationWarnings:@[validationWarning]];

    [runEntity setProperties:@[dateAttribute, idAttribute]];

    mom = [[NSManagedObjectModel alloc] init];
    [mom setEntities:@[runEntity]];

    NSDictionary *localizationDictionary = @{
                            @"Property/date/Entity/Run":@"Date",
                            @"Property/processID/Entity/Run":@"Process ID",
                            @"ErrorString/Process ID < 1":@"Process ID must not be less than 1"};

    [mom setLocalizationDictionary:localizationDictionary];

    return mom;
}
```

[下一页](The%20Application%20Log%20Directory.md)[上一页](Creating%20the%20Project.md)

