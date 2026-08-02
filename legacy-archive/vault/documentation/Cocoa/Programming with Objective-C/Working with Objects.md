---
title: 用 Objective-C 编程
apple_id: TP40011210
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/WorkingwithObjects/WorkingwithObjects.html
archived_at: '2026-07-15T07:17:59.449707Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [用 Objective-C 编程](About%20Objective-C.md)


[下一页](Encapsulating%20Data.md)[上一页](Defining%20Classes.md)

# 使用对象

在一个 Objective-C 应用程序中，大部分工作都是通过消息在一个对象生态系统里来回发送而完成的。这些对象中，有些是 Cocoa 或 Cocoa Touch 提供的类的实例，有些则是你自己定义的类的实例。

上一章介绍了定义类的接口和实现的语法，包括实现方法（其中包含响应消息所要执行的代码）的语法。本章将说明如何向一个对象发送这样的消息，并涵盖 Objective-C 的一些动态特性，包括动态类型，以及在运行时确定应该调用哪个方法的能力。

在使用一个对象之前，必须通过为其属性分配内存，并对其内部值进行任何必要的初始化，来正确地创建它。本章将介绍如何嵌套调用_分配（allocate）_和初始化对象的方法，以确保它被正确配置。

虽然在 Objective-C 中有好几种不同的方式可以在对象之间发送消息，但迄今为止最常见的是使用方括号的基本语法，就像这样：

```objc
    [someObject doSomething];
```

左边的引用（在这个例子中是 `someObject`）是消息的_接收者（receiver）_。右边的消息 `doSomething` 是要在该接收者上调用的方法名。换句话说，当上面这行代码被执行时，`someObject` 将会收到 `doSomething` 消息。

上一章介绍了如何为一个类创建接口，就像这样：

```objc
@interface XYZPerson : NSObject
- (void)sayHello;
@end
```

以及如何为该类创建实现，就像这样：

```objc
@implementation XYZPerson
- (void)sayHello {
    NSLog(@"Hello, world!");
}
@end
```

假设你已经拿到了一个 `XYZPerson` 对象，你可以像这样向它发送 `sayHello` 消息：

```objc
    [somePerson sayHello];
```

发送一条 Objective-C 消息在概念上和调用一个 C 函数非常相似。[图 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnbnknlti) 展示了 `sayHello` 消息的实际程序流程。

__图 2-1__  基本的消息传递程序流程

!

为了指定消息的接收者，理解 Objective-C 中如何使用指针来引用对象非常重要。

和大多数其他编程语言一样，C 和 Objective-C 使用变量来追踪值。

标准 C 中定义了一些基本的_标量（scalar）_变量类型，包括整数、浮点数和字符，它们的声明和赋值方式是这样的：

```c
    int someInteger = 42;
    float someFloatingPointNumber = 3.14f;
```

_局部变量（local variable）_是在方法或函数内部声明的变量，就像这样：

```objc
- (void)myMethod {
    int someInteger = 42;
}
```

它们的作用域仅限于其所定义的方法内部。

在这个示例中，`someInteger` 被声明为 `myMethod` 内部的一个局部变量；一旦执行到达该方法的结束花括号，`someInteger` 就不再可访问了。当一个局部标量变量（比如 `int` 或 `float`）消失时，它的值也随之消失。

相比之下，Objective-C 对象的分配方式略有不同。对象通常比一次简单的方法调用作用域存活得更久。特别是，一个对象往往需要比最初用来追踪它的那个变量存活更长时间，因此对象的内存是_动态（dynamically）_分配和释放的。

这就要求你使用保存内存地址的 C 指针来追踪它们在内存中的位置，就像这样：

```objc
- (void)myMethod {
    NSString *myString = // 从某处获取一个字符串……
    [...]
}
```

虽然指针变量 `myString`（星号表明它是一个指针）的作用域被限制在 `myMethod` 内部，但它在内存中所指向的实际字符串对象，其生命周期可能会超出这个作用域。举例来说，它可能早已存在，或者你可能需要在其他方法调用中传递这个对象。

如果你在发送消息时需要传递一个对象，就要为某个方法参数提供一个对象指针。上一章介绍了声明带有单个参数的方法的语法：

```objc
- (void)someMethodWithValue:(SomeType)value;
```

因此，声明一个接受字符串对象的方法的语法是这样的：

```objc
- (void)saySomething:(NSString *)greeting;
```

你可能会像这样实现 `saySomething:` 方法：

```objc
- (void)saySomething:(NSString *)greeting {
    NSLog(@"%@", greeting);
}
```

`greeting` 指针的行为和局部变量一样，其作用域仅限于 `saySomething:` 方法内部，即使它所指向的实际字符串对象在该方法被调用之前就已经存在，并且在方法执行完毕之后仍会继续存在。

除了通过方法参数传递值之外，方法也可以返回一个值。本章到目前为止展示的每个方法的返回类型都是 `void`。C 语言的 `void` 关键字表示该方法不返回任何东西。

指定返回类型为 `int` 表示该方法返回一个标量整数值：

```objc
- (int)magicNumber;
```

该方法的实现使用 C 语言的 `return` 语句来表示方法执行完毕后应该返回的值，就像这样：

```objc
- (int)magicNumber {
    return 42;
}
```

完全可以忽略一个方法会返回值这一事实。在这个例子中，`magicNumber` 方法除了返回一个值之外没有做任何有用的事情，但像这样调用该方法也完全没有问题：

```objc
    [someObject magicNumber];
```

如果你确实需要记录返回值，可以声明一个变量，并把方法调用的结果赋给它，就像这样：

```objc
    int interestingNumber = [someObject magicNumber];
```

你也可以用完全相同的方式从方法中返回对象。举例来说，`NSString` 类提供了一个 `uppercaseString` 方法：

```objc
- (NSString *)uppercaseString;
```

它的用法和返回标量值的方法一样，不过你需要使用一个指针来记录结果：

```objc
    NSString *testString = @"Hello, world!";
    NSString *revisedString = [testString uppercaseString];
```

当这个方法调用返回时，`revisedString` 将指向一个表示字符 `HELLO WORLD!` 的 `NSString` 对象。

请记住，当实现一个返回对象的方法时，就像这样：

```objc
- (NSString *)magicString {
    NSString *stringToReturn = // 创建一个有意思的字符串……

    return stringToReturn;
}
```

即使 `stringToReturn` 指针的作用域已经结束，当这个字符串对象作为返回值被传递时，它依然会继续存在。

这种情况下涉及一些内存管理方面的考量：一个返回的对象（在堆上创建）需要存活足够长的时间，以便让最初调用该方法的对象能够使用它，但又不能永久存在，否则会造成内存泄漏。在大多数情况下，Objective-C 编译器的_自动引用计数（Automatic Reference Counting，ARC）_特性会替你处理好这些考量。

每当你编写方法实现时，你都可以使用一个重要的隐藏值 `self`。从概念上讲，`self` 是一种指代「接收到这条消息的对象」的方式。它是一个指针，就像上面的 `greeting` 值一样，可以用来在当前的接收对象上调用方法。

你可能会决定重构 `XYZPerson` 的实现，修改 `sayHello` 方法使其使用上面展示的 `saySomething:` 方法，从而把 `NSLog()` 调用移到一个单独的方法中。这意味着你可以添加更多方法，比如 `sayGoodbye`，它们各自都调用 `saySomething:` 方法来处理实际的问候过程。如果你以后想把每条问候语显示在用户界面的一个文本框中，你只需要修改 `saySomething:` 方法，而不必逐一去调整每个问候方法。

使用 `self` 在当前对象上调用消息的新实现是这样的：

```objc
@implementation XYZPerson
- (void)sayHello {
    [self saySomething:@"Hello, world!"];
}
- (void)saySomething:(NSString *)greeting {
    NSLog(@"%@", greeting);
}
@end
```

如果针对这个更新后的实现，向一个 `XYZPerson` 对象发送 `sayHello` 消息，实际的程序流程如 [图 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnbnknltq) 所示。

__图 2-2__  向 self 发送消息时的程序流程

!

Objective-C 中还有另一个可供你使用的重要关键字，叫做 `super`。向 `super` 发送消息是一种调用继承链中更上层超类所定义的方法实现的方式。`super` 最常见的用法是在_覆写（override）_一个方法的时候。

假设你想创建一种新的 person 类，一个「喊叫的人」类，让每条问候语都以大写字母显示。你可以复制整个 `XYZPerson` 类，把每个方法中的每个字符串都改成大写，但最简单的方式是创建一个继承自 `XYZPerson` 的新类，只覆写 `saySomething:` 方法，让它以大写形式显示问候语，就像这样：

```objc
@interface XYZShoutingPerson : XYZPerson
@end
```

```objc
@implementation XYZShoutingPerson
- (void)saySomething:(NSString *)greeting {
    NSString *uppercaseGreeting = [greeting uppercaseString];
    NSLog(@"%@", uppercaseGreeting);
}
@end
```

这个示例声明了一个额外的字符串指针 `uppercaseGreeting`，并把向原始 `greeting` 对象发送 `uppercaseString` 消息所返回的值赋给它。正如你之前所看到的，这会是一个新的字符串对象，它是通过把原字符串中的每个字符都转换成大写而构建出来的。

因为 `sayHello` 是由 `XYZPerson` 实现的，而 `XYZShoutingPerson` 又被设置为继承自 `XYZPerson`，所以你同样可以在 `XYZShoutingPerson` 对象上调用 `sayHello`。当你在 `XYZShoutingPerson` 上调用 `sayHello` 时，`[self saySomething:...]` 这次调用将使用_被覆写（overridden）_的实现，以大写形式显示问候语，由此产生的实际程序流程如 [图 2-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnbnknlts) 所示。

__图 2-3__  被覆写方法的程序流程

!

然而，这个新实现并不理想，因为如果你以后决定修改 `XYZPerson` 中 `saySomething:` 的实现，让它把问候语显示在用户界面元素中而不是通过 `NSLog()` 输出，你还得同时修改 `XYZShoutingPerson` 的实现。

更好的做法是修改 `XYZShoutingPerson` 版本的 `saySomething:`，让它调用超类（`XYZPerson`）的实现来处理实际的问候：

```objc
@implementation XYZShoutingPerson
- (void)saySomething:(NSString *)greeting {
    NSString *uppercaseGreeting = [greeting uppercaseString];
    [super saySomething:uppercaseGreeting];
}
@end
```

现在，向一个 `XYZShoutingPerson` 对象发送 `sayHello` 消息所产生的实际程序流程如 [图 2-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnbnknltcmq) 所示。

__图 2-4__  向 super 发送消息时的程序流程

!

正如本章前面所述，Objective-C 对象的内存是动态分配的。创建一个对象的第一步，是确保为该对象所属类所定义的属性——以及其继承链上每个超类所定义的属性——都分配了足够的内存。

`NSObject` 根类提供了一个类方法 `alloc`，它会替你处理这个过程：

```objc
+ (id)alloc;
```

注意，这个方法的返回类型是 `id`。这是 Objective-C 中一个用来表示「某种对象」的特殊关键字。它是指向对象的指针，就像 `(NSObject *)` 一样，但特殊之处在于它不使用星号。本章后面的 [Objective-C 是一门动态语言](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnbnknltcoa) 中会更详细地介绍它。

`alloc` 方法还有另一项重要任务，那就是把为对象属性分配的内存清零。这样可以避免内存中残留着之前存储内容的垃圾数据这一常见问题，但这还不足以完整地初始化一个对象。

你需要把对 `alloc` 的调用与对 `init`（另一个 `NSObject` 方法）的调用结合起来：

```objc
- (id)init;
```

`init` 方法被类用来确保其属性在创建时具有合适的初始值，下一章会更详细地介绍它。

注意，`init` 同样返回一个 `id`。

如果一个方法返回一个对象指针，就可以把对该方法的调用嵌套起来，作为另一个方法调用的接收者，从而在一条语句中组合多个消息调用。分配并初始化一个对象的正确方式，是把 `alloc` 调用嵌套在 `init` 调用_内部_，就像这样：

```objc
    NSObject *newObject = [[NSObject alloc] init];
```

这个示例把 `newObject` 变量设置为指向一个新创建的 `NSObject` 实例。

最内层的调用会最先执行，因此 `NSObject` 类会先收到 `alloc` 方法，返回一个新分配的 `NSObject` 实例。接着，这个返回的对象被用作 `init` 消息的接收者，`init` 消息本身又会把该对象返回，赋给 `newObject` 指针，如 [图 2-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnbnknltcna) 所示。

__图 2-5__  嵌套 alloc 和 init 消息

!

有些对象需要用必需的值来初始化。举例来说，一个 `NSNumber` 对象在创建时必须提供它要表示的数值。

`NSNumber` 类定义了几个_初始化方法（initializer）_，包括：

```objc
- (id)initWithBool:(BOOL)value;
- (id)initWithFloat:(float)value;
- (id)initWithInt:(int)value;
- (id)initWithLong:(long)value;
```

带参数的初始化方法的调用方式和普通的 `init` 方法完全相同——一个 `NSNumber` 对象是这样被分配和初始化的：

```objc
    NSNumber *magicNumber = [[NSNumber alloc] initWithInt:42];
```


正如上一章所提到的，一个类也可以定义_工厂方法（factory method）_。工厂方法为传统的 `alloc]init]` 流程提供了另一种选择，不需要嵌套两个方法。

`NSNumber` 类定义了几个与其初始化方法相对应的类工厂方法，包括：

```objc
+ (NSNumber *)numberWithBool:(BOOL)value;
+ (NSNumber *)numberWithFloat:(float)value;
+ (NSNumber *)numberWithInt:(int)value;
+ (NSNumber *)numberWithLong:(long)value;
```

工厂方法的用法是这样的：

```objc
    NSNumber *magicNumber = [NSNumber numberWithInt:42];
```

这实际上和前面使用 `alloc]initWithInt:]` 的示例是等效的。类工厂方法通常只是直接调用 `alloc` 和相应的 `init` 方法，提供它们只是为了方便使用。

你也可以使用 `new` 类方法来创建一个类的实例。这个方法由 `NSObject` 提供，你不需要在自己的子类中覆写它。

它实际上等同于不带参数地调用 `alloc` 和 `init`：

```objc
    XYZObject *object = [XYZObject new];
    // 实际上等同于：
    XYZObject *object = [[XYZObject alloc] init];
```


有些类允许你使用更简洁的_字面量（literal）_语法来创建实例。

举例来说，你可以使用一种特殊的字面量表示法来创建 `NSString` 实例，就像这样：

```objc
    NSString *someString = @"Hello, World!";
```

这实际上等同于分配并初始化一个 `NSString`，或者使用它的某个类工厂方法：

```objc
    NSString *someString = [NSString stringWithCString:"Hello, World!"
                                              encoding:NSUTF8StringEncoding];
```

`NSNumber` 类也支持多种字面量：

```objc
    NSNumber *myBOOL = @YES;
    NSNumber *myFloat = @3.14f;
    NSNumber *myInt = @42;
    NSNumber *myLong = @42L;
```

同样，这些示例中的每一个实际上都等同于使用相应的初始化方法或类工厂方法。

你还可以使用_装箱表达式（boxed expression）_来创建一个 `NSNumber`，就像这样：

```objc
    NSNumber *myInt = @(84 / 2);
```

在这种情况下，表达式会被求值，并用求值结果创建一个 `NSNumber` 实例。

Objective-C 还支持用字面量创建不可变的 `NSArray` 和 `NSDictionary` 对象；[值与集合](Values%20and%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnznknltc) 会进一步讨论这一点。

如前所述，你需要使用指针来追踪内存中的对象。由于 Objective-C 的动态特性，你为这个指针使用什么具体的类类型并不重要——当你向相应的对象发送消息时，总会调用正确的方法。

`id` 类型定义了一个通用的对象指针。你可以在声明变量时使用 `id`，但这样会丢失关于该对象的_编译期（compile-time）_信息。

考虑下面这段代码：

```objc
    id someObject = @"Hello, World!";
    [someObject removeAllObjects];
```

在这个例子中，`someObject` 会指向一个 `NSString` 实例，但编译器除了知道它是某种对象之外，对这个实例一无所知。`removeAllObjects` 消息是由某些 Cocoa 或 Cocoa Touch 对象（比如 `NSMutableArray`）定义的，所以编译器不会报错，尽管这段代码在运行时会产生一个异常，因为 `NSString` 对象无法响应 `removeAllObjects`。

把这段代码改写成使用_静态类型（static type）_：

```objc
    NSString *someObject = @"Hello, World!";
    [someObject removeAllObjects];
```

这样一来，编译器现在就会产生一个错误，因为 `removeAllObjects` 没有在它所知道的任何公开的 `NSString` 接口中声明。

由于一个对象的类是在_运行时（runtime）_确定的，因此在创建或使用一个实例时，你给变量指定什么类型都没有关系。要使用本章前面介绍的 `XYZPerson` 和 `XYZShoutingPerson` 类，你可能会使用下面这样的代码：

```objc
    XYZPerson *firstPerson = [[XYZPerson alloc] init];
    XYZPerson *secondPerson = [[XYZShoutingPerson alloc] init];
    [firstPerson sayHello];
    [secondPerson sayHello];
```

虽然 `firstPerson` 和 `secondPerson` 在静态类型上都是 `XYZPerson` 对象，但 `secondPerson` 在运行时会指向一个 `XYZShoutingPerson` 对象。当在每个对象上调用 `sayHello` 方法时，都会使用正确的实现；对 `secondPerson` 来说，这意味着使用的是 `XYZShoutingPerson` 版本。

如果你需要判断一个对象是否与另一个对象相同，重要的是要记住你处理的是指针。

标准 C 的_相等运算符（equality operator）_ `==` 用来检验两个变量的值是否相等，就像这样：

```c
    if (someInteger == 42) {
        // someInteger 的值为 42
    }
```

在处理对象时，`==` 运算符用来检验两个不同的指针是否指向同一个对象：

```objc
    if (firstPerson == secondPerson) {
        // firstPerson 与 secondPerson 是同一个对象
    }
```

如果你需要检验两个对象是否表示相同的数据，就需要调用一个类似 `isEqual:` 的方法，它由 `NSObject` 提供：

```objc
    if ([firstPerson isEqual:secondPerson]) {
        // firstPerson 与 secondPerson 内容相同
    }
```

如果你需要比较一个对象所表示的值是否大于或小于另一个对象，就不能使用标准 C 的比较运算符 `>` 和 `<`。相反，基本的 Foundation 类型，比如 `NSNumber`、`NSString` 和 `NSDate`，都提供了一个 `compare:` 方法：

```objc
    if ([someDate compare:anotherDate] == NSOrderedAscending) {
        // someDate 早于 anotherDate
    }
```


在声明标量变量的同时对其进行初始化，始终是一个好习惯，否则它们的初始值会包含之前栈内容残留的垃圾数据：

```objc
    BOOL success = NO;
    int magicNumber = 42;
```

对象指针则不需要这样做，因为如果你没有指定其他初始值，编译器会自动把该变量设为 `nil`：

```objc
    XYZPerson *somePerson;
    // somePerson 会自动被设为 nil
```

如果你没有其他值可用，`nil` 值是初始化对象指针最安全的方式，因为在 Objective-C 中向 `nil` 发送消息是完全可以接受的。如果你确实向 `nil` 发送了消息，显然什么都不会发生。

如果你需要检查确保一个对象不是 `nil`（即某个变量指向内存中的一个对象），你既可以使用标准 C 的_不等运算符（inequality operator）_：

```objc
    if (somePerson != nil) {
        // somePerson 指向一个对象
    }
```

也可以直接提供该变量：

```objc
    if (somePerson) {
        // somePerson 指向一个对象
    }
```

如果 `somePerson` 变量是 `nil`，它的逻辑值就是 `0`（假）。如果它有一个地址，那就不是零，因此求值为真。

类似地，如果你需要检查一个变量是否为 `nil`，你既可以使用相等运算符：

```objc
    if (somePerson == nil) {
        // somePerson 没有指向任何对象
    }
```

也可以直接使用 C 语言的_逻辑取反运算符（logical negation operator）_：

```objc
    if (!somePerson) {
        // somePerson 没有指向任何对象
    }
```


1. 打开你在上一章练习中创建的项目里的 `main.m` 文件，找到 `main()` 函数。和任何用 C 编写的可执行程序一样，这个函数代表你应用程序的起始点。

   使用 `alloc` 和 `init` 创建一个新的 `XYZPerson` 实例，然后调用 `sayHello` 方法。
2. 实现本章前面展示的 `saySomething:` 方法，并重写 `sayHello` 方法来使用它。添加几种其他问候语，并在上面创建的实例上分别调用它们。
3. 为 `XYZShoutingPerson` 类创建新的类文件，将其设置为继承自 `XYZPerson`。

   覆写 `saySomething:` 方法以显示大写的问候语，并在一个 `XYZShoutingPerson` 实例上测试这个行为。
4. 实现你在上一章中声明的 `XYZPerson` 类的 `person` 工厂方法，使其返回一个正确分配并初始化的 `XYZPerson` 类实例，然后在 `main()` 中使用这个方法，取代你之前嵌套的 `alloc` 和 `init`。
5. 创建一个新的局部 `XYZPerson` 指针，但不要包含任何赋值。

   使用一个分支（`if` 语句）来检查该变量是否被自动赋值为 `nil`。

[下一页](Encapsulating%20Data.md)[上一页](Defining%20Classes.md)

