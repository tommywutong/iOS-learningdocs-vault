---
title: 用 Objective-C 编程
apple_id: TP40011210
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/FoundationTypesandCollections/FoundationTypesandCollections.html
archived_at: '2026-07-15T07:17:57.926006Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [用 Objective-C 编程](About%20Objective-C.md)


[下一页](Working%20with%20Blocks.md)[上一页](Working%20with%20Protocols.md)

# 值与集合

虽然 Objective-C 是一门面向对象的编程语言，但它是 C 的一个超集，这意味着你可以在 Objective-C 代码中使用任何标准 C 的 _标量（scalar）_（非对象）类型，比如 `int`、`float` 和 `char`。在 Cocoa 和 Cocoa Touch 应用程序中还可以使用一些额外的标量类型，比如 `NSInteger`、`NSUInteger` 和 `CGFloat`，它们的具体定义会因目标架构而异。

在你并不需要使用对象来表示一个值所带来的好处（或者说相应开销）的场合，就会用到标量类型。字符串通常用 `NSString` 类的实例来表示，而数值则常常保存在标量的局部变量或属性中。

在 Objective-C 中可以声明 C 风格的数组，但你会发现，Cocoa 和 Cocoa Touch 应用程序中的集合通常是用 `NSArray` 或 `NSDictionary` 这样的类的实例来表示的。这些类只能用来收集 Objective-C 对象，这意味着在把一个值添加到集合之前，你需要先创建一个 `NSValue`、`NSNumber` 或 `NSString` 之类的实例来表示这个值。

本指南前面几章频繁用到了 `NSString` 类及其初始化方法和类工厂方法，以及提供了简洁语法来创建 `NSString` 实例的 Objective-C `@"string"` 字面量。本章将说明如何通过方法调用或 Objective-C 值字面量语法来创建 `NSValue` 和 `NSNumber` 对象。

每一种标准 C 标量变量类型在 Objective-C 中都可以使用：

```c
    int someInteger = 42;
    float someFloatingPointNumber = 3.1415;
    double someDoublePrecisionFloatingPointNumber = 6.02214199e23;
```

以及标准的 C 运算符：

```c
    int someInteger = 42;
    someInteger++;            // someInteger == 43

    int anotherInteger = 64;
    anotherInteger--;         // anotherInteger == 63

    anotherInteger *= 2;      // anotherInteger == 126
```

如果你为一个 Objective-C 属性使用了标量类型，就像这样：

```objc
@interface XYZCalculator : NSObject
@property double currentValue;
@end
```

那么在通过点语法访问这个值时，也可以对该属性使用 C 运算符，像这样：

```objc
@implementation XYZCalculator
- (void)increment {
    self.currentValue++;
}
- (void)decrement {
    self.currentValue--;
}
- (void)multiplyBy:(double)factor {
    self.currentValue *= factor;
}
@end
```

点语法纯粹是对存取方法调用的一种语法包装，所以这个例子中的每个操作都等同于先用取值方法取得值，再执行相应运算，然后用赋值方法把运算结果设置回去。

`BOOL` 标量类型在 Objective-C 中被定义用来保存一个布尔值，即 `YES` 或 `NO`。正如你可能预期的那样，`YES` 在逻辑上等同于 `true` 和 `1`，而 `NO` 等同于 `false` 和 `0`。

Cocoa 和 Cocoa Touch 对象上的许多方法参数也使用特殊的标量数值类型，比如 `NSInteger` 或 `CGFloat`。

例如，`NSTableViewDataSource` 和 `UITableViewDataSource` 协议（在上一章中有介绍）都有请求要显示的行数的方法：

```objc
@protocol NSTableViewDataSource <NSObject>
- (NSInteger)numberOfRowsInTableView:(NSTableView *)tableView;
...
@end
```

像 `NSInteger` 和 `NSUInteger` 这样的类型，其具体定义会因目标架构而异。当为 32 位环境构建时（比如 iOS），它们分别是 32 位有符号和无符号整数；当为 64 位环境构建时（比如现代 OS X 运行时），它们分别是 64 位有符号和无符号整数。

如果你可能需要跨 API 边界（无论是内部 API 还是对外发布的 API）传递值，比如在应用程序代码与某个框架之间进行方法或函数调用时用作参数或返回值，那么最佳实践是使用这些与平台相关的类型。

对于局部变量（比如循环中的计数器），如果你知道该值在标准限制范围之内，使用基本的 C 类型也没问题。

一些 Cocoa 和 Cocoa Touch API 使用 C 结构体来保存它们的值。举个例子，可以向一个字符串对象请求某个子字符串的范围，像这样：

```objc
    NSString *mainString = @"This is a long string";
    NSRange substringRange = [mainString rangeOfString:@"long"];
```

一个 `NSRange` 结构体保存一个位置（location）和一个长度（length）。在这个例子中，`substringRange` 保存的范围将是 `{10,4}`——`@"long"` 开头的"`l`"是 `mainString` 中从零开始计数的第 `10` 个字符，而 `@"long"` 的长度是 `4` 个字符。

类似地，如果你需要编写自定义绘图代码，就需要与 Quartz 打交道，这需要用到围绕 `CGFloat` 数据类型构建的结构体，比如 OS X 上的 `NSPoint` 和 `NSSize`，以及 iOS 上的 `CGPoint` 和 `CGSize`。同样，`CGFloat` 的具体定义也会因目标架构而异。

关于 Quartz 2D 绘图引擎的更多信息，请参阅 _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_。

如果你需要把一个标量值表示为一个对象，比如在使用下一节所介绍的集合类时，可以使用 Cocoa 和 Cocoa Touch 提供的基础值类之一。

正如你在前面几章中所看到的，`NSString` 用来表示一串字符，比如 `Hello World`。有多种方式可以创建 `NSString` 对象，包括标准的分配和初始化、类工厂方法或字面量语法：

```objc
    NSString *firstString = [[NSString alloc] initWithCString:"Hello World!"
                                                     encoding:NSUTF8StringEncoding];
    NSString *secondString = [NSString stringWithCString:"Hello World!"
                                                encoding:NSUTF8StringEncoding];
    NSString *thirdString = @"Hello World!";
```

这几个例子实际上都完成了同样的事情——创建一个表示所提供字符的字符串对象。

基本的 `NSString` 类是不可变的，这意味着它的内容在创建时就已确定，之后无法更改。如果你需要表示一个不同的字符串，就必须创建一个新的字符串对象，像这样：

```objc
    NSString *name = @"John";
    name = [name stringByAppendingString:@"ny"];    // 返回一个新的字符串对象
```

`NSMutableString` 类是 `NSString` 的可变子类，它允许你在运行时使用 `appendString:` 或 `appendFormat:` 之类的方法来更改其字符内容，像这样：

```objc
    NSMutableString *name = [NSMutableString stringWithString:@"John"];
    [name appendString:@"ny"];   // 仍是同一个对象，但现在表示 "Johnny"
```


如果你需要构建一个包含可变值的字符串，就需要用到__格式字符串（format string）__。这可以让你使用格式说明符来指明这些值该如何插入：

```objc
    int magicNumber = ...
    NSString *magicString = [NSString stringWithFormat:@"The magic number is %i", magicNumber];
```

可用的格式说明符在[字符串格式说明符](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265)中有说明。关于字符串的更多总体信息，请参阅 _[String Programming Guide](../String%20Programming%20Guide/Introduction%20to%20String%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaztk2i)_。

`NSNumber` 类用来表示任何基本的 C 标量类型，包括 `char`、`double`、`float`、`int`、`long`、`short`，以及它们各自的 `unsigned` 变体，还有 Objective-C 的布尔类型 `BOOL`。

与 `NSString` 一样，你有多种方式可以创建 `NSNumber` 实例，包括分配和初始化，或者类工厂方法：

```objc
    NSNumber *magicNumber = [[NSNumber alloc] initWithInt:42];
    NSNumber *unsignedNumber = [[NSNumber alloc] initWithUnsignedInt:42u];
    NSNumber *longNumber = [[NSNumber alloc] initWithLong:42l];

    NSNumber *boolNumber = [[NSNumber alloc] initWithBOOL:YES];

    NSNumber *simpleFloat = [NSNumber numberWithFloat:3.14f];
    NSNumber *betterDouble = [NSNumber numberWithDouble:3.1415926535];

    NSNumber *someChar = [NSNumber numberWithChar:'T'];
```

也可以用 Objective-C 字面量语法来创建 `NSNumber` 实例：

```objc
    NSNumber *magicNumber = @42;
    NSNumber *unsignedNumber = @42u;
    NSNumber *longNumber = @42l;

    NSNumber *boolNumber = @YES;

    NSNumber *simpleFloat = @3.14f;
    NSNumber *betterDouble = @3.1415926535;

    NSNumber *someChar = @'T';
```

这些例子等同于使用 `NSNumber` 的类工厂方法。

创建了一个 `NSNumber` 实例之后，就可以使用其中一个存取方法来请求其标量值：

```objc
    int scalarMagic = [magicNumber intValue];
    unsigned int scalarUnsigned = [unsignedNumber unsignedIntValue];
    long scalarLong = [longNumber longValue];

    BOOL scalarBool = [boolNumber boolValue];

    float scalarSimpleFloat = [simpleFloat floatValue];
    double scalarBetterDouble = [betterDouble doubleValue];

    char scalarChar = [someChar charValue];
```

`NSNumber` 类还提供了用于处理额外的 Objective-C 原始类型的方法。例如，如果你需要为标量的 `NSInteger` 和 `NSUInteger` 类型创建对象表示形式，请务必使用正确的方法：

```objc
    NSInteger anInteger = 64;
    NSUInteger anUnsignedInteger = 100;

    NSNumber *firstInteger = [[NSNumber alloc] initWithInteger:anInteger];
    NSNumber *secondInteger = [NSNumber numberWithUnsignedInteger:anUnsignedInteger];

    NSInteger integerCheck = [firstInteger integerValue];
    NSUInteger unsignedCheck = [secondInteger unsignedIntegerValue];
```

所有 `NSNumber` 实例都是不可变的，也没有可变子类；如果你需要一个不同的数字，只需使用另一个 `NSNumber` 实例即可。

`NSNumber` 类本身是基础 `NSValue` 类的子类，`NSValue` 类为单个值或数据项提供了一个对象包装。除了基本的 C 标量类型之外，`NSValue` 还可以用来表示指针和结构体。

`NSValue` 类提供了多种工厂方法，可以为给定的标准结构体创建一个值，这使得创建一个实例来表示（比如说）一个 `NSRange` 变得很容易，就像本章前面的那个例子：

```objc
    NSString *mainString = @"This is a long string";
    NSRange substringRange = [mainString rangeOfString:@"long"];
    NSValue *rangeValue = [NSValue valueWithRange:substringRange];
```

也可以创建 `NSValue` 对象来表示自定义的结构体。如果你有特殊需要，想用一个 C 结构体（而不是 Objective-C 对象）来存储信息，像这样：

```c
typedef struct {
    int i;
    float f;
} MyIntegerFloatStruct;
```

你可以通过提供一个指向该结构体的指针，以及一个编码后的 Objective-C 类型，来创建一个 `NSValue` 实例。`@encode()` 编译器指令用来创建正确的 Objective-C 类型，像这样：

```objc
    struct MyIntegerFloatStruct aStruct;
    aStruct.i = 42;
    aStruct.f = 3.14;

    NSValue *structValue = [NSValue value:&aStruct
                             withObjCType:@encode(MyIntegerFloatStruct)];
```

标准的 C 引用运算符（`&`）用来为 `value` 参数提供 `aStruct` 的地址。

虽然可以用一个 C 数组来保存一组标量值、甚至是对象指针，但 Objective-C 代码中的大多数集合都是 Cocoa 和 Cocoa Touch 集合类之一的实例，比如 `NSArray`、`NSSet` 和 `NSDictionary`。

这些类用于管理一组对象，这意味着任何你想添加到集合中的项都必须是一个 Objective-C 类的实例。如果你需要添加一个标量值，就必须先创建一个合适的 `NSNumber` 或 `NSValue` 实例来表示它。

集合类不会以某种方式为每个被收集的对象单独维护一份拷贝，而是使用强引用来跟踪其内容。这意味着任何你添加到集合中的对象，至少会在集合本身存活期间保持存活，正如[通过所有权和责任管理对象图](Encapsulating%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnjnknltg)中所描述的那样。

除了跟踪其内容之外，Cocoa 和 Cocoa Touch 的每个集合类都让执行某些任务变得很容易，比如枚举、访问特定项，或者判断某个特定对象是否是集合的一部分。

基本的 `NSArray`、`NSSet` 和 `NSDictionary` 类都是不可变的，这意味着它们的内容在创建时就已确定。每个类也都有一个可变子类，让你可以随意添加或移除对象。

关于 Cocoa 和 Cocoa Touch 中可用的各种集合类的更多信息，请参阅 _[Collections Programming Topics](../Collections%20Programming%20Topics/About%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazti2i)_。

`NSArray` 用来表示一个对象的 _有序集合（ordered collection）_。唯一的要求是每一项都必须是一个 Objective-C 对象——并不要求每个对象都是同一个类的实例。

为了在数组中保持顺序，每个元素都存储在一个从零开始计数的索引位置上，如 [图 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnznknltcmq) 所示。

__图 6-1__  Objective-C 对象数组

!

与本章前面介绍的值类一样，你可以通过分配和初始化、类工厂方法或字面量语法来创建一个数组。

根据对象数量的不同，有多种不同的初始化和工厂方法可供使用：

```objc
+ (id)arrayWithObject:(id)anObject;
+ (id)arrayWithObjects:(id)firstObject, ...;
- (id)initWithObjects:(id)firstObject, ...;
```

`arrayWithObjects:` 和 `initWithObjects:` 方法都接受一个以 `nil` 结尾的、数量可变的参数列表，这意味着你必须把 `nil` 作为最后一个值包含进去，像这样：

```objc
    NSArray *someArray =
  [NSArray arrayWithObjects:someObject, someString, someNumber, someValue, nil];
```

这个例子创建的数组与前面 [图 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnznknltcmq) 中展示的那个类似。第一个对象 `someObject` 的数组索引为 `0`；最后一个对象 `someValue` 的索引为 `3`。

如果所提供的值中有一个是 `nil`，就有可能无意中截断这份条目列表，像这样：

```objc
    id firstObject = @"someString";
    id secondObject = nil;
    id thirdObject = @"anotherString";
    NSArray *someArray =
  [NSArray arrayWithObjects:firstObject, secondObject, thirdObject, nil];
```

在这种情况下，`someArray` 将只包含 `firstObject`，因为 `nil` 的 `secondObject` 会被解释为条目列表的结尾。

也可以使用 Objective-C 字面量来创建数组，像这样：

```objc
    NSArray *someArray = @[firstObject, secondObject, thirdObject];
```

当使用这种字面量语法时，你不应该用 `nil` 来终止对象列表，事实上 `nil` 在这里是一个无效值。举例来说，如果你试图执行下面的代码，会在运行时得到一个异常：

```objc
    id firstObject = @"someString";
    id secondObject = nil;
    NSArray *someArray = @[firstObject, secondObject];
    // 异常："attempt to insert nil object"
```

如果你确实需要在某个集合类中表示一个 `nil` 值，应该使用 `NSNull` 单例类，具体做法参见[用 NSNull 表示 nil](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnznknltgna)。

创建了一个数组之后，你可以查询它的一些信息，比如对象的数量，或者它是否包含某个给定的项：

```objc
    NSUInteger numberOfItems = [someArray count];

    if ([someArray containsObject:someString]) {
        ...
    }
```

你还可以查询数组中某个给定索引位置上的项。如果你试图请求一个无效的索引，会在运行时得到一个越界异常，所以你应该总是先检查一下项的数量：

```objc
    if ([someArray count] > 0) {
        NSLog(@"First item is: %@", [someArray objectAtIndex:0]);
    }
```

这个例子检查项的数量是否大于零。如果是，就记录索引为零的第一项的描述信息。

除了使用 `objectAtIndex:`，还有一种下标语法（subscripting）可以替代使用，这就跟访问标准 C 数组中的一个值一样。前面的例子可以像这样重写：

```objc
    if ([someArray count] > 0) {
        NSLog(@"First item is: %@", someArray[0]);
    }
```


`NSArray` 类还提供了多种方法来对其收集的对象进行排序。因为 `NSArray` 是不可变的，所以这些方法中的每一个都会返回一个包含按排序顺序排列的项的新数组。

举个例子，你可以根据对每个字符串调用 `compare:` 的结果，对一个字符串数组进行排序，像这样：

```objc
    NSArray *unsortedStrings = @[@"gammaString", @"alphaString", @"betaString"];
    NSArray *sortedStrings =
                 [unsortedStrings sortedArrayUsingSelector:@selector(compare:)];
```


虽然 `NSArray` 类本身是不可变的，但这对其中收集的任何对象都没有影响。例如，如果你把一个可变字符串添加到一个不可变数组中，像这样：

```objc
NSMutableString *mutableString = [NSMutableString stringWithString:@"Hello"];
NSArray *immutableArray = @[mutableString];
```

没有什么能阻止你去改变这个字符串：

```objc
    if ([immutableArray count] > 0) {
        id string = immutableArray[0];
        if ([string isKindOfClass:[NSMutableString class]]) {
            [string appendString:@" World!"];
        }
    }
```

如果你需要能够在数组创建之后添加或移除对象，就需要使用 `NSMutableArray`，它增加了多种方法来添加、移除或替换一个或多个对象：

```objc
    NSMutableArray *mutableArray = [NSMutableArray array];
    [mutableArray addObject:@"gamma"];
    [mutableArray addObject:@"alpha"];
    [mutableArray addObject:@"beta"];

    [mutableArray replaceObjectAtIndex:0 withObject:@"epsilon"];
```

这个例子创建的数组最终会包含 `@"epsilon"`、`@"alpha"`、`@"beta"` 这些对象。

也可以就地对一个可变数组进行排序，而不需要创建第二个数组：

```objc
    [mutableArray sortUsingSelector:@selector(caseInsensitiveCompare:)];
```

在这种情况下，数组中包含的项会按 `@"alpha"`、`@"beta"`、`@"epsilon"` 这样不区分大小写的升序排列。

`NSSet` 与数组类似，但它维护的是一组无序的__不重复（distinct）__对象，如 [图 6-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnznknltcna) 所示。

__图 6-2__  对象集合

!

因为集合不维护顺序，所以在测试成员关系时，它们比数组带来更好的性能。

基本的 `NSSet` 类同样是不可变的，所以它的内容必须在创建时指定，可以使用分配和初始化，也可以使用一个类工厂方法，像这样：

```objc
    NSSet *simpleSet =
      [NSSet setWithObjects:@"Hello, World!", @42, aValue, anObject, nil];
```

与 `NSArray` 一样，`initWithObjects:` 和 `setWithObjects:` 方法都接受一个以 `nil` 结尾的、数量可变的参数列表。`NSSet` 的可变子类是 `NSMutableSet`。

即使你试图多次添加同一个对象，集合也只会为单个对象存储一个引用：

```objc
    NSNumber *number = @42;
    NSSet *numberSet =
      [NSSet setWithObjects:number, number, number, number, nil];
    // numberSet 只包含一个对象
```

关于集合的更多信息，请参阅 [Sets: Unordered Collections of Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Articles/Sets.html#//apple_ref/doc/uid/20000136)。

`NSDictionary` 不是简单地维护一个有序或无序的对象集合，而是根据给定的键（key）来存储对象，之后可以用这些键来获取对象。

最佳实践是使用字符串对象作为字典的键，如 [图 6-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnznknltcni) 所示。

__图 6-3__  对象字典

!!

你可以通过分配和初始化，也可以通过类工厂方法来创建字典，像这样：

```objc
    NSDictionary *dictionary = [NSDictionary dictionaryWithObjectsAndKeys:
                   someObject, @"anObject",
             @"Hello, World!", @"helloString",
                          @42, @"magicNumber",
                    someValue, @"aValue",
                             nil];
```

请注意，对于 `dictionaryWithObjectsAndKeys:` 和 `initWithObjectsAndKeys:` 方法，每个对象都要写在它的键之前，并且同样地，这份对象和键的列表必须以 `nil` 结尾。

Objective-C 也为字典创建提供了字面量语法，像这样：

```objc
    NSDictionary *dictionary = @{
                  @"anObject" : someObject,
               @"helloString" : @"Hello, World!",
               @"magicNumber" : @42,
                    @"aValue" : someValue
    };
```

请注意，对于字典字面量，键要写在其对象之前，并且不需要以 `nil` 结尾。

创建了一个字典之后，你可以向它询问存储在某个给定键下的对象，像这样：

```objc
    NSNumber *storedNumber = [dictionary objectForKey:@"magicNumber"];
```

如果没有找到该对象，`objectForKey:` 方法将返回 `nil`。

除了使用 `objectForKey:`，还有一种下标语法可以替代使用，看起来是这样的：

```objc
    NSNumber *storedNumber = dictionary[@"magicNumber"];
```


如果你需要在字典创建之后添加或移除对象，就需要使用 `NSMutableDictionary` 子类，像这样：

```objc
    [dictionary setObject:@"another string" forKey:@"secondString"];
    [dictionary removeObjectForKey:@"anObject"];
```


本节所描述的这些集合类不能添加 `nil`，因为 `nil` 在 Objective-C 中表示"没有对象"。如果你需要在集合中表示"没有对象"，可以使用 `NSNull` 类：

```objc
    NSArray *array = @[ @"string", @42, [NSNull null] ];
```

`NSNull` 是一个单例类，这意味着 `null` 方法总是返回同一个实例。因此你可以检查数组中的某个对象是否等于共享的那个 `NSNull` 实例：

```objc
    for (id object in array) {
        if (object == [NSNull null]) {
            NSLog(@"Found a null object");
        }
    }
```


`NSArray` 和 `NSDictionary` 类让把它们的内容直接写入磁盘变得很容易，像这样：

```objc
    NSURL *fileURL = ...
    NSArray *array = @[@"first", @"second", @"third"];

    BOOL success = [array writeToURL:fileURL atomically:YES];
    if (!success) {
        // 发生了一个错误……
    }
```

如果其中包含的每个对象都属于 _属性列表（property list）_ 类型之一（`NSArray`、`NSDictionary`、`NSString`、`NSData`、`NSDate` 和 `NSNumber`），就可以从磁盘上重新创建整个层级结构，像这样：

```objc
    NSURL *fileURL = ...
    NSArray *array = [NSArray arrayWithContentsOfURL:fileURL];
    if (!array) {
        // 发生了一个错误……
    }
```

关于属性列表的更多信息，请参阅 _[Property List Programming Guide](../Property%20List%20Programming%20Guide/Introduction%20to%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2i)_。

如果你需要持久化除上面展示的那些标准属性列表类之外的其他类型的对象，可以使用一个归档器对象，比如 `NSKeyedArchiver`，来为所收集的对象创建一份归档。

创建归档的唯一要求是每个对象都必须支持 `NSCoding` 协议。这意味着每个对象都必须知道如何把自己 _编码（encode）_ 进一份归档中（通过实现 `encodeWithCoder:` 方法），以及在从现有归档中读取时如何 _解码（decode）_ 自己（`initWithCoder:` 方法）。

`NSArray`、`NSSet` 和 `NSDictionary` 类及其可变子类都支持 `NSCoding`，这意味着你可以使用归档器来持久化复杂的对象层级结构。举例来说，如果你使用 Interface Builder 来布局窗口和视图，那么生成的 nib 文件其实就是你以可视化方式创建的对象层级结构的一份归档。在运行时，nib 文件会使用相关的类被解档成一个对象层级结构。

关于归档的更多信息，请参阅 _[Archives and Serializations Programming Guide](../Archives%20and%20Serializations%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2do2i)_。

Objective-C 以及 Cocoa 或 Cocoa Touch 提供了多种方式来枚举一个集合的内容。虽然可以使用一个传统的 C `for` 循环来遍历其内容，像这样：

```objc
    int count = [array count];
    for (int index = 0; index < count; index++) {
        id eachObject = [array objectAtIndex:index];
        ...
    }
```

最佳实践是使用本节介绍的其他技术之一。

许多集合类都遵循 `NSFastEnumeration` 协议，包括 `NSArray`、`NSSet` 和 `NSDictionary`。这意味着你可以使用快速枚举（fast enumeration），这是 Objective-C 语言层面的一项特性。

用来枚举一个数组或集合内容的快速枚举语法看起来是这样的：

```
    for (<Type> <variable> in <collection>) {
        ...
    }
```

举个例子，你可以使用快速枚举来记录数组中每个对象的描述信息，像这样：

```objc
    for (id eachObject in array) {
        NSLog(@"Object: %@", eachObject);
    }
```

`eachObject` 变量在每一次循环中都会被自动设置为当前对象，所以每个对象都会有一条对应的日志语句。

如果你对一个字典使用快速枚举，你遍历的是字典的 _键（key）_，像这样：

```objc
    for (NSString *eachKey in dictionary) {
        id object = dictionary[eachKey];
        NSLog(@"Object: %@ for key: %@", object, eachKey);
    }
```

快速枚举的行为和标准 C 的 `for` 循环很相似，所以你可以使用 `break` 关键字来中断迭代，或者使用 `continue` 来前进到下一个元素。

如果你枚举的是一个有序集合，枚举会按该顺序进行。对于 `NSArray` 而言，这意味着第一次遍历对应索引 `0` 处的对象，第二次对应索引 `1` 处的对象，依此类推。如果你需要跟踪当前的索引，只需在迭代发生时对其计数即可：

```objc
    int index = 0;
    for (id eachObject in array) {
        NSLog(@"Object at index %i is: %@", index, eachObject);
        index++;
    }
```

在快速枚举期间不能改变一个集合，即使这个集合是可变的。如果你试图在循环内部添加或移除一个被收集的对象，就会产生一个运行时异常。

也可以通过使用一个 `NSEnumerator` 对象来枚举许多 Cocoa 和 Cocoa Touch 集合。

举例来说，你可以向一个 `NSArray` 请求一个 `objectEnumerator` 或者一个 `reverseObjectEnumerator`。这些对象可以配合快速枚举一起使用，像这样：

```objc
    for (id eachObject in [array reverseObjectEnumerator]) {
        ...
    }
```

在这个例子中，循环将以相反的顺序遍历所收集的对象，所以最后一个对象会排在最前面，以此类推。

也可以通过反复调用枚举器的 `nextObject` 方法来遍历其内容，像这样：

```objc
    id eachObject;
    while ( (eachObject = [enumerator nextObject]) ) {
        NSLog(@"Current object is: %@", eachObject);
    }
```

在这个例子中，用一个 `while` 循环在每次循环时把 `eachObject` 变量设置为下一个对象。当没有更多对象剩余时，`nextObject` 方法将返回 `nil`，它在逻辑上等同于 false，所以循环会停止。

和快速枚举一样，在枚举期间也不能改变一个集合。而且，正如你可能从名字上就能猜到的，使用快速枚举比手动使用一个枚举器对象要更快。

也可以使用 block 来枚举 `NSArray`、`NSSet` 和 `NSDictionary`。下一章会详细介绍 block。

[下一页](Working%20with%20Blocks.md)[上一页](Working%20with%20Protocols.md)

