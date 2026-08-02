---
title: 谓词编程指南
apple_id: TP40001789
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/Articles/pUsing.html
archived_at: '2026-07-15T07:17:41.568911Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [谓词编程指南](Introduction.md)


[下一页](Comparison%20of%20NSPredicate%20and%20Spotlight%20Query%20Strings.md)[上一页](Creating%20Predicates.md)

# 使用谓词

本文档从总体上介绍如何使用谓词，以及使用谓词可能会如何影响你组织应用程序数据的方式。

要对谓词求值，你使用 `NSPredicate` 的 `evaluateWithObject:` 方法，并传入待求值的对象。该方法返回一个布尔值——在下面的例子中，结果是 `YES`。

```objc
NSPredicate *predicate = [NSPredicate predicateWithFormat:@"SELF IN %@", @[@"Stig", @"Shaffiq", @"Chris"]];
BOOL result = [predicate evaluateWithObject:@"Shaffiq"];
```

你可以对任意类的对象使用谓词，但对于你想在谓词中使用的那些键，该类必须支持[键值编码](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25)。

`NSArray` 和 `NSMutableArray` 提供了筛选数组内容的方法。`NSArray` 提供了 `filteredArrayUsingPredicate:`，它返回一个新数组，其中包含接收者中匹配指定谓词的对象。`NSMutableArray` 提供了 `filterUsingPredicate:`，它用指定谓词对接收者的内容求值，只保留匹配的对象。

```objc
NSMutableArray *names = [@[@"Nick", @"Ben", @"Adam", @"Melissa"] mutableCopy];

NSPredicate *bPredicate = [NSPredicate predicateWithFormat:@"SELF beginswith[c] 'b'"];
NSArray *beginWithB = [names filteredArrayUsingPredicate:bPredicate];
// beginWithB 中包含 { @"Ben" }。

NSPredicate *ePredicate = [NSPredicate predicateWithFormat:@"SELF contains[c] 'e'"];
[names filterUsingPredicate:ePredicate];
// 数组现在包含 { @"Ben", @"Melissa" }
```

如果你使用 Core Data 框架，这些数组方法提供了一种高效的手段来筛选已有的对象数组，而不像执行一次获取（fetch）那样需要往返访问持久化存储。

回想一下，你可以在谓词中用键路径来沿关系导航。下面的例子演示了如何创建谓词来查找隶属于某个指定名称部门的员工（但也请参阅[性能](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoojufvjvomq)）。

```objc
NSString *departmentName = ... ;
NSPredicate *predicate = [NSPredicate predicateWithFormat:
        @"department.name like %@", departmentName];
```

如果涉及对多关系，谓词的构造方式会略有不同。比方说，如果你想获取那些至少有一名员工名字为 "Matthew" 的部门，就要使用 `ANY` 运算符，如下例所示：

```objc
NSPredicate *predicate = [NSPredicate predicateWithFormat:
    @"ANY employees.firstName like 'Matthew'"];
```

如果你想查找那些至少有一名员工的薪水超过某个数额的部门，同样使用 `ANY` 运算符，如下例所示：

```objc
float salary = ... ;
NSPredicate *predicate = [NSPredicate predicateWithFormat:@"ANY employees.salary > %f", salary];
```


比较谓词不会让任何值与 null 匹配，除非该值本身就是 null（`nil`）或 `NSNull` 空值（也就是说，若 `$value` 为 `nil`，则（`$value == nil`）返回 `YES`）。看看下面这个例子。

```objc
NSString *firstName = @"Ben";

NSArray *array = @[ @{ @"lastName" : "Turner" }];
                    @{ @"firstName" : @"Ben", @"lastName" : @"Ballard",
                       @"birthday", [NSDate dateWithString:@"1972-03-24 10:45:32 +0600"] } ];

NSPredicate *predicate =
    [NSPredicate predicateWithFormat:@"firstName like %@", firstName];
NSArray *filteredArray = [array filteredArrayUsingPredicate:predicate];

NSLog(@"filteredArray: %@", filteredArray);
// 输出：
// filteredArray ({birthday = 1972-03-24 10:45:32 +0600; \\
                      firstName = Ben; lastName = Ballard;})
```

该谓词匹配了键 `firstName` 的值为 `Ben` 的那个字典，但没有匹配键 `firstName` 没有值的那个字典。下面这段代码用日期和大于比较符说明了同样的道理。

```objc
NSDate *referenceDate = [NSDate dateWithTimeIntervalSince1970:0];

predicate = [NSPredicate predicateWithFormat:@"birthday > %@", referenceDate];
filteredArray = [array filteredArrayUsingPredicate:predicate];

NSLog(@"filteredArray: %@", filteredArray);
// 输出：
// filteredArray: ({birthday = 1972-03-24 10:45:32 +0600; \\
                       firstName = Ben; lastName = Ballard;})
```


如果你想匹配空值，就必须在其他比较之外再加上一个专门的判断，如下面这段代码所示。

```objc
predicate = [NSPredicate predicateWithFormat:@"(firstName == %@) || (firstName = nil)", firstName];
filteredArray = [array filteredArrayUsingPredicate:predicate];
NSLog(@"filteredArray: %@", filteredArray);

// 输出：
// filteredArray: ( { lastName = Turner; }, { birthday = 1972-03-23 20:45:32 -0800; firstName = Ben; lastName = Ballard; }
```

由此可以推出，对空值做空值判断会返回真。在下面这段代码中，两次谓词求值都会把 `ok` 置为 `YES`。

```objc
predicate = [NSPredicate predicateWithFormat:@"firstName = nil"];
BOOL ok = [predicate evaluateWithObject:[NSDictionary dictionary]];

ok = [predicate evaluateWithObject:
    [NSDictionary dictionaryWithObject:[NSNull null] forKey:@"firstName"]];
```


如果你在使用 Core Data 框架，你可以像不使用 Core Data 时那样使用谓词（例如筛选数组，或配合数组控制器使用）。此外，你还可以用谓词来约束获取请求，并把获取请求模板存放在托管对象模型里（参阅 Managed Object Models）。

你创建一个谓词来匹配目标实体的属性（注意你可以用键路径沿关系导航），并把该谓词关联到一个获取请求上。请求执行时会返回一个数组，其中包含符合谓词所指定条件的对象（如果有的话）。下面的例子演示了如何用谓词查找薪水高于指定数额的员工。

```objc
NSFetchRequest *request = [[NSFetchRequest alloc] init];
NSEntityDescription *entity = [NSEntityDescription entityForName:@"Employee"
        inManagedObjectContext:managedObjectContext];
[request setEntity:entity];

NSNumber *salaryLimit = <#A number representing the limit#>;
NSPredicate *predicate = [NSPredicate predicateWithFormat:@"salary > %@", salaryLimit];
[request setPredicate:predicate];
NSError *error;
NSArray *array = [managedObjectContext executeFetchRequest:request error:&error];
```


如果你在使用 Cocoa 绑定，可以为对象控制器（例如 `NSObjectController` 或 `NSArrayController` 的实例）指定一个获取谓词。你可以在 Xcode 的属性检查器中直接把谓词输入到谓词编辑器文本框里，也可以用 `setFetchPredicate:` 以编程方式设置。该谓词用于约束控制器执行获取时返回的结果。如果你用的是 `NSObjectController` 对象，你要指定一个能唯一标识出你希望作为控制器内容的那个对象的获取——例如，如果控制器的实体是 Department，谓词可能是 `name like "Engineering"`。

`MATCHES` 运算符使用 [ICU 的正则表达式包](http://icu.sourceforge.net/userguide/regexp.html)，如下例所示：

```objc
NSArray *array = @[@"TATACCATGGGCCATCATCATCATCATCATCATCATCATCATCACAG",
                   @"CGGGATCCCTATCAAGGCACCTCTTCG", @"CATGCCATGGATACCAACGAGTCCGAAC",
                   @"CAT", @"CATCATCATGTCT", @"DOG"];

// 查找包含至少 3 次 'CAT' 序列重复、
// 且其后没有紧跟 'CA' 的字符串
NSPredicate *catPredicate =
    [NSPredicate predicateWithFormat:@"SELF MATCHES '.*(CAT){3,}(?!CA).*'"];

NSArray *filteredArray = [array filteredArrayUsingPredicate:catPredicate];
// filteredArray 中只包含 'CATCATCATGTCT'
```

按照 ICU 规范，正则表达式元字符在模式集合内部是无效的。例如，正则表达式 `\d{9}[\dxX]` _并不_匹配有效的 ISBN 号（任意十位数字，或九位数字加字母 'X'），因为模式集合（`[\dxX]`）中含有元字符（`\d`）。你可以改写成一个 `OR` 表达式，如下面的代码示例所示：

```objc
NSArray *isbnTestArray = @[@"123456789X", @"987654321x", @"1234567890", @"12345X", @"1234567890X"];
NSPredicate *isbnPredicate =
    [NSPredicate predicateWithFormat:@"SELF MATCHES '\\\\d{10}|\\\\d{9}[Xx]'"];

NSArray *isbnArray = [isbnTestArray filteredArrayUsingPredicate:isbnPredicate];
// isbnArray 中包含 (123456789X, 987654321x, 1234567890)
```


你应当把复合谓词组织成能把工作量降到最低的形式。正则表达式匹配尤其是一项开销很大的操作。因此在复合谓词中，你应该把简单的判断放在正则表达式之前；也就是说，不要写成下面这样：

```objc
NSPredicate *predicate = [NSPredicate predicateWithFormat:
    @"( title matches .*mar[1-10] ) OR ( type = 1 )"];
```

而应该写成

```objc
NSPredicate *predicate = [NSPredicate predicateWithFormat:
    @"( type = 1 ) OR ( title matches .*mar[1-10] )"];
```

在第二个例子中，只有当第一个子句为假时才会去求值正则表达式。

一般来说，连接（跨关系的查询）同样是开销很大的操作，能避免就应该避免。在测试对一关系时，如果你已经持有——或者能轻松取到——关系的源对象（或它的 object ID），那么测试对象相等性要比测试源对象的某个属性更高效。与其写成下面这样：

```objc
NSPredicate *predicate = [NSPredicate predicateWithFormat:
        @"department.name like %@", [department name]];
```

写成下面这样更高效：

```objc
NSPredicate *predicate = [NSPredicate predicateWithFormat:
        @"department == %@", department];
```

如果一个谓词包含多个表达式，通常把它组织成能避免连接的形式也会更高效。例如，`@"firstName beginswith[cd] 'Matt' AND (ANY directreports.paygrade <= 7)"` 很可能比 `@"(ANY directreports.paygrade <= 7) AND (firstName beginswith[cd] 'Matt')"` 更高效，因为前者只有在第一个判断成功时才会进行连接。

在某些场景下，你的数据表示方式与谓词的使用之间可能存在矛盾。如果你打算在应用程序中使用谓词，那么典型查询操作的模式可能会影响你组织数据的方式。在 Core Data 中，虽然实体以及实体到类的映射由你指定，但在持久化存储中创建底层结构的那些层次是不透明的。尽管如此，你仍然可以掌控自己的实体以及它们所拥有的属性。

除了开销通常较大之外，连接还可能限制灵活性。因此，把数据反规范化有时是合适的做法。总体而言——假定查询发生得相当频繁——用更大的对象换取更容易找到正确对象（从而在内存中保留更少的对象）往往是一笔划算的交易。

在 OS X 中，你可以为数组控制器设置一个谓词来筛选内容数组。你可以在代码中设置该谓词（使用 `setFilterPredicate:`）。你也可以把数组控制器的 `filterPredicate` 绑定绑到一个返回 `NSPredicate` 对象的方法上。实现该方法的对象可以是 File's Owner，也可以是另一个控制器对象。如果你要修改谓词，记得必须以符合键值观察规范的方式修改（参阅 _[键值观察编程指南](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)_），这样数组控制器才会相应地更新自身。

你还可以把 `NSSearchField` 对象的 `predicate` 绑定绑到数组控制器的 `filterPredicate` 上。搜索框的 `predicate` 绑定是一个多值绑定，相关说明见 [Binding Types](https://developer.apple.com/library/archive/documentation/Cocoa/Reference/CocoaBindingsRef/Concepts/BindingTypes.html#//apple_ref/doc/uid/20002305)。

[下一页](Comparison%20of%20NSPredicate%20and%20Spotlight%20Query%20Strings.md)[上一页](Creating%20Predicates.md)

