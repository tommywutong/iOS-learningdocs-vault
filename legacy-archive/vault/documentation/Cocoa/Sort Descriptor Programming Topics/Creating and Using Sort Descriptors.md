---
title: 排序描述符编程主题
apple_id: 10000174i
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2012-07-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SortDescriptors/Articles/Creating.html
archived_at: '2026-07-15T07:19:14.038749Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [排序描述符编程主题](Introduction%20to%20Sort%20Descriptors.md)


[下一页](Document%20Revision%20History.md)[上一页](Introduction%20to%20Sort%20Descriptors.md)

# 创建和使用排序描述符

排序描述符描述了用于对一组对象集合进行排序的比较方式。你可以创建一个 `NSSortDescriptor` 实例，指定要排序的属性键（property key），以及比较应该是升序还是降序。排序描述符还可以指定一个用于比较属性键值的方法，而不是使用默认的 `compare:`。

需要记住的重要一点是：`NSSortDescriptor` 本身并不执行排序，它只是提供了如何排序的描述。实际的排序工作是由其他类完成的，通常是 `NSArray` 或 `NSMutableArray`。

举个例子，假设我们有一个数组（`NSArray` 的实例），其中包含自定义类 `Employee` 的实例（该类满足 [Requirements of Collection Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha2dkljrg43tcobu) 中列出的要求）。`Employee` 类具有员工姓和名（`NSString` 实例）、入职日期（`NSDate` 实例）以及年龄（`NSNumber` 实例）等属性。

我们的第一个任务是返回一个按年龄排序的 `NSArray` 对象。清单 1 中的示例演示了如何创建一个 `NSSortDescriptor`，用于按 `age` 键以升序方式对数组内容进行排序。

__清单 1__  按 age 键对数组排序

```objc
NSSortDescriptor *ageDescriptor = [[NSSortDescriptor alloc] initWithKey:@"age" ascending:YES];
NSArray *sortDescriptors = @[ageDescriptor];
NSArray *sortedArray = [employeesArray sortedArrayUsingDescriptors:sortDescriptors];
```

你会注意到，在对数组排序时，需要提供一个由 `NSSortDescriptor` 实例组成的数组。这些排序描述符会按顺序依次应用，从而实现按多个属性键进行排序。

如果我们还想按入职日期排序，可以在提供给 `sortedArrayUsingDescriptors:` 的数组中再添加一个描述符。清单 2 中的示例演示了如何使用多个排序描述符，先按年龄排序，再对年龄相同的员工按入职日期排序。

__清单 2__  按 age 和入职日期键对数组排序

```objc
NSSortDescriptor *ageDescriptor = [[NSSortDescriptor alloc] initWithKey:@"age" ascending:YES];
NSSortDescriptor *hireDateDescriptor = [[NSSortDescriptor alloc] initWithKey:@"hireDate" ascending:YES];
NSArray *sortDescriptors = @[ageDescriptor, hireDateDescriptor];
NSArray *sortedArray = [employeesArray sortedArrayUsingDescriptors:sortDescriptors];
```

在上述两种情况中，都使用了默认的比较方法 `compare:`。按年龄排序时（年龄值是 `NSNumber` 实例），使用的是 `NSNumber` 实现的 `compare:` 方法；按入职日期排序时（入职日期值是 `NSDate` 实例），使用的是 `NSDate` 实现的 `compare:` 方法。

但如果我们想按姓名对员工排序，由于姓名是字符串，结果应该根据用户的语言环境按字母顺序排列，且可能不区分大小写。`NSString` 默认的 `compare:` 方法并不能做到这一点，因此我们需要指定一个自定义方法来执行比较。

前面的示例都依赖默认的 `compare:` 方法按年龄和入职日期排序。姓名是字符串，当你对要展示给用户的字符串进行排序时，应始终使用本地化比较（参见 _[String Programming Guide](../String%20Programming%20Guide/Introduction%20to%20String%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaztk2i)_ 中的 [Searching, Comparing, and Sorting Strings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/SearchingStrings.html#//apple_ref/doc/uid/20000149)）。通常你还希望进行不区分大小写的比较。清单 3 中的示例展示了如何指定合适的比较方法（[localizedStandardCompare:](https://developer.apple.com/documentation/foundation/nsstring/1409742-localizedstandardcompare)），按姓和名对数组排序。

__清单 3__  使用本地化标准比较对数组排序

```objc
NSSortDescriptor *lastNameDescriptor = [[NSSortDescriptor alloc]
              initWithKey:@"lastName" ascending:YES selector:@selector(localizedStandardCompare:)];
NSSortDescriptor * firstNameDescriptor = [[NSSortDescriptor alloc]
              initWithKey:@"firstName" ascending:YES selector:@selector(localizedStandardCompare:)];
NSArray *sortDescriptors = @[lastNameDescriptor, firstNameDescriptor];
NSArray *sortedArray = [peopleArray sortedArrayUsingDescriptors:sortDescriptors];
```

表 1 列出了那些拥有可与排序描述符配合使用的方法的 Foundation 类。

__表 1__  常见 Foundation 类及其比较方法

| 比较方法 | 支持的类 |
| --- | --- |
| `compare:` | `NSString`、`NSMutableString`、`NSDate`、`NSCalendarDate`、`NSValue`（仅限标量类型和 unsigned char）、`NSNumber` |
| `caseInsensitiveCompare:` | `NSString`、`NSMutableString` |
| `localizedCompare:` | `NSString`、`NSMutableString` |
| `localizedCaseInsensitiveCompare:` | `NSString`、`NSMutableString` |
| `localizedStandardCompare:` | `NSString`、`NSMutableString` |

你可以通过实现一个符合规范的比较方法，为自己的类添加比较支持，具体要求见 Requirements of Collection Objects。

要让一个集合能够使用 `NSSortDescriptor` 对其内容进行排序，其中的对象必须满足以下要求：

- 集合中的每个对象，对于用来创建排序描述符的属性键，都必须是键值编码（key-value coding）兼容的（关于键值编码的更多内容，请参阅 _[Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)_）。
- 集合中每个对象在指定属性键处的对象，必须实现用于创建排序描述符时所用的比较选择器（selector）。如果未指定自定义选择器，则对象必须实现 `compare:`。
- 用于比较的选择器接收一个参数，即与 `self` 进行比较的对象，并且必须返回相应的 `NSComparisonResult`。

尝试对包含不满足上述任一要求的对象的集合进行排序，将引发异常。

[下一页](Document%20Revision%20History.md)[上一页](Introduction%20to%20Sort%20Descriptors.md)

