---
title: 用 Objective-C 编程
apple_id: TP40011210
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Conventions/Conventions.html
archived_at: '2026-07-15T07:17:51.046801Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [用 Objective-C 编程](About%20Objective-C.md)


[下一页](Document%20Revision%20History.md)[上一页](Dealing%20with%20Errors.md)

# 约定

当你使用框架类时，会注意到 Objective-C 代码非常易读。类名和方法名比一般 C 语言代码中的函数名，或者 C 标准库中的函数名要更具描述性，多单词组成的名称使用驼峰式（camel case）写法。当你编写自己的类时，应该遵循 Cocoa 和 Cocoa Touch 所使用的相同约定，这样可以让你的代码更易读——无论是对你自己，还是对可能需要处理你项目的其他 Objective-C 开发者来说都是如此，同时也能保持代码库的一致性。

此外，许多 Objective-C 和框架特性都要求你遵循严格的命名规范，各种机制才能正常工作。例如，存取方法的名称必须遵循相应约定，才能配合诸如[键值编码](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25)（KVC）或[键值观察](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16)（KVO）之类的技术使用。

本章介绍 Cocoa 和 Cocoa Touch 代码中一些最常见的约定，并说明在哪些情况下，名称需要在整个应用项目（包括其链接的框架）范围内保持唯一。

每次你创建一个新的类型、符号或标识符时，都应该首先考虑这个名称需要在多大范围内保持唯一。有时这个范围可能是整个应用程序（包括其链接的框架）；有时范围仅限于一个外层类，甚至只是一段代码块。

Objective-C 类不仅需要在你自己项目所编写的代码中保持名称唯一，在你所包含的任何框架或 bundle 中也是如此。举例来说，你应该避免使用像 `ViewController` 或 `TextParser` 这样通用的类名，因为你的应用中所包含的某个框架有可能没有遵循约定，创建了同名的类。

为了保持类名的唯一性，约定是在所有类上使用前缀。你会注意到，Cocoa 和 Cocoa Touch 的类名通常以 `NS` 或 `UI` 开头。像这样的两字母前缀是 Apple 保留用于框架类的。随着你对 Cocoa 和 Cocoa Touch 的深入了解，你会遇到与特定框架相关的各种其他前缀：

| 前缀 | 框架 |
| --- | --- |
| `NS` | Foundation（OS X 和 iOS）和 Application Kit（OS X） |
| `UI` | UIKit（iOS） |
| `AB` | Address Book |
| `CA` | Core Animation |
| `CI` | Core Image |

你自己的类应该使用三字母前缀。这些前缀可能与你的公司名称和应用名称的组合有关，甚至与应用中某个特定组件有关。举例来说，如果你的公司叫 Whispering Oak，你正在开发一款叫 Zebra Surprise 的游戏，你可能会选择 `WZS` 或 `WOZ` 作为类前缀。

你还应该使用能清楚表明该类所代表内容的名词来命名类，就像下面这些 Cocoa 和 Cocoa Touch 中的例子：

|  |  |  |  |
| --- | --- | --- | --- |
| `NSWindow` | `CAAnimation` | `NSWindowController` | `NSManagedObjectContext` |

如果类名需要多个单词，你应该使用 _驼峰式（camel case）_ 写法，将每个后续单词的首字母大写。

一旦你为类选定了唯一的名称，你在该类中声明的方法就只需要在这个类内部保持唯一即可。使用与另一个类中相同的方法名是很常见的做法，例如为了重写超类方法，或者利用多态性。在多个类中执行相同任务的方法，应该具有相同的名称、返回类型和参数类型。

方法名没有前缀，并且应该以小写字母开头；多单词的情况同样使用驼峰式写法，就像下面这些来自 `NSString` 类的例子：

|  |  |  |
| --- | --- | --- |
| `length` | `characterAtIndex:` | `lengthOfBytesUsingEncoding:` |

如果一个方法接受一个或多个参数，方法名应该指明每一个参数：

|  |  |  |
| --- | --- | --- |
| `substringFromIndex:` | `writeToURL:atomically:encoding:error:` | `enumerateSubstringsInRange:options:usingBlock:` |

方法名的第一部分应该指明调用该方法的主要意图或结果。如果一个方法返回一个值，第一个单词通常表明将要返回的内容，就像上面所示的 `length`、`character...` 和 `substring...` 方法那样。如果需要说明返回值的某个重要信息，则会使用多个单词，就像 `NSString` 类中的 `mutableCopy`、`capitalizedString` 或 `lastPathComponent` 方法那样。如果一个方法执行某个动作，比如写入磁盘或枚举内容，第一个单词应该表明这个动作，就像 `write...` 和 `enumerate...` 方法所示。

如果一个方法包含一个 _error_ 指针参数，用于在发生错误时被设置，这个参数应该是方法的最后一个参数。如果一个方法接受一个 _block_，block 参数应该是方法的最后一个参数，这样在以内联方式指定 block 时，方法调用才能尽可能保持可读性。出于同样的原因，最好尽量避免使用带有多个 block 参数的方法。

追求清晰而简洁的方法名同样重要。清晰并不一定意味着冗长，简洁也不一定就能带来清晰，所以最好在两者之间找到一个恰当的平衡：

|  |  |
| --- | --- |
| `stringAfterFindingAndReplacingAllOccurrencesOfThisString:withThisString:` | 太冗长 |
| `strReplacingStr:str:` | 太简略 |
| `stringByReplacingOccurrencesOfString:withString:` | 恰到好处 |

你应该避免在方法名中使用缩写，除非你确定这个缩写在多种语言和文化中都广为人知。[可接受的缩写和首字母缩略词](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CodingGuidelines/Articles/APIAbbreviations.html#//apple_ref/doc/uid/20001285)中给出了一份常见缩写列表。

当使用分类向现有框架类添加方法时，你应该在方法名上加一个前缀以避免冲突，具体描述见[避免分类方法名冲突](Customizing%20Existing%20Classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnrnknlti)。

由于 Objective-C 是 C 语言的超集，C 语言的变量作用域规则同样适用于 Objective-C。一个局部变量的名称不能与同一作用域内声明的任何其他变量冲突：

```objc
- (void)someMethod {
    int interestingNumber = 42;
    ...
    int interestingNumber = 44; // 不允许
}
```

虽然 C 语言确实允许你在 _外层_ 作用域中声明一个与已声明变量同名的新局部变量，就像这样：

```objc
- (void)someMethod {
    int interestingNumber = 42;
    ...
    for (NSNumber *eachNumber in array) {
        int interestingNumber = [eachNumber intValue]; // 不建议这样做
        ...
    }
}
```

但这会让代码变得令人困惑、可读性降低，因此最好的做法是尽量避免这样做。

除了考虑唯一性之外，对于一些重要的方法类型，遵循严格的约定也至关重要。这些约定被 Objective-C 编译器和运行时的一些底层机制所使用，此外 Cocoa 和 Cocoa Touch 中的类所要求的行为也依赖于这些约定。

当你使用 `@property` 语法在对象上声明属性时（具体描述见[封装数据](Encapsulating%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnjnknltc)），编译器会自动合成相应的取值方法和赋值方法（除非你另有指示）。如果出于某种原因你需要自己提供存取方法的实现，重要的是要确保为属性使用正确的方法名称，例如这样才能通过点语法调用你的方法。

除非另有说明，取值方法应该使用与属性相同的名称。对于名为 `firstName` 的属性，其取值方法也应该叫做 `firstName`。这一规则的例外是布尔属性，其取值方法应该以 `is` 开头。举例来说，对于名为 `paused` 的属性，其取值方法应该叫做 `isPaused`。

属性的赋值方法应该采用 `setPropertyName:` 的形式。对于名为 `firstName` 的属性，赋值方法应该叫做 `setFirstName:`；对于名为 `paused` 的布尔属性，赋值方法应该叫做 `setPaused:`。

虽然 `@property` 语法允许你指定不同的存取方法名称，但你应该只在诸如布尔属性这类情形下才这样做。遵循这里所描述的约定至关重要，否则像键值编码（使用 `valueForKey:` 和 `setValue:forKey:` 来获取或设置属性的能力）这样的技术将无法正常工作。有关 KVC 的更多信息，请参阅 _[键值编码编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)_。

正如你在前面的章节中所看到的，创建一个类的实例通常有多种方式。你可以结合使用分配和初始化，就像这样：

```objc
    NSMutableArray *array = [[NSMutableArray alloc] init];
```

或者使用 `new` 这个便捷方法，作为显式调用 `alloc` 和 `init` 的替代方式：

```objc
    NSMutableArray *array = [NSMutableArray new];
```

有些类还提供了类工厂方法：

```objc
    NSMutableArray *array = [NSMutableArray array];
```

类工厂方法应该始终以其所创建的类的名称（不含前缀）开头，但存在既有工厂方法的类的子类是个例外。以 `NSArray` 类为例，其工厂方法以 `array` 开头。`NSMutableArray` 类并没有定义任何自己专属的类工厂方法，因此可变数组的工厂方法仍然以 `array` 开头。

Objective-C 底层有各种各样的内存管理规则，编译器依靠这些规则来确保对象在必要的时间内保持存活。虽然你通常不需要太过担心这些规则，但编译器会根据创建方法的名称来判断应该遵循哪条规则。由于自动释放池（autorelease pool block）的使用，通过工厂方法创建的对象，与通过传统的分配和初始化或 `new` 创建的对象，在管理方式上略有不同。有关自动释放池和内存管理的更多信息，请参阅 _[高级内存管理编程指南](../Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytc2i)_。

[下一页](Document%20Revision%20History.md)[上一页](Dealing%20with%20Errors.md)

