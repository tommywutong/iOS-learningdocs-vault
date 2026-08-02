---
title: 用 Objective-C 编程
apple_id: TP40011210
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/CustomizingExistingClasses/CustomizingExistingClasses.html
archived_at: '2026-07-15T07:17:51.056742Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [用 Objective-C 编程](About%20Objective-C.md)


[下一页](Working%20with%20Protocols.md)[上一页](Encapsulating%20Data.md)

# 定制现有类

对象应该有明确定义的任务，比如为特定信息建模、显示可视内容，或者控制信息的流转。正如你已经了解到的，类接口定义了其他对象应该如何与某个对象交互，以帮助它完成这些任务。

有时候，你可能会发现自己想要扩展一个现有的类，给它添加一些只在特定情况下才有用的行为。举例来说，你可能会发现你的应用经常需要在可视界面中显示一串字符。与其每次要显示字符串时都创建某个专门用来绘制字符串的对象，不如直接让 `NSString` 类自己具备在屏幕上绘制其字符的能力，这样会更合理。

在这种情况下，把这种实用行为添加到原来的主类接口中并不总是合理的。举例来说，一个字符串对象在应用中被使用的大多数场合都不太可能需要绘制能力，而且对于 `NSString` 而言，因为它是一个框架类，你根本无法修改它原来的接口或实现。

而且，为现有类派生子类也可能并不合理，因为你可能希望绘制行为不仅对原来的 `NSString` 类可用，也对该类的所有子类（比如 `NSMutableString`）可用。此外，虽然 `NSString` 在 OS X 和 iOS 上都可用，但绘制代码在每个平台上都需要有所不同，这意味着你需要在每个平台上使用不同的子类。

作为替代方案，Objective-C 允许你通过分类和类扩展，把自己的方法添加到现有类中。

如果你需要给现有类添加一个方法——也许是为了增加某些功能，让你的应用更容易完成某件事——最简单的办法就是使用分类。

声明一个_分类（category）_的语法和标准 Objective-C 类描述一样，使用 `@interface` 关键字，但不表示任何子类继承关系。取而代之的是，它在圆括号里指定分类的名称，就像这样：

```objc
@interface ClassName (CategoryName)

@end
```

分类可以为任何类声明，即使你没有原始实现的源代码也是如此（比如标准的 Cocoa 或 Cocoa Touch 类）。你在分类中声明的任何方法，都会对原始类的所有实例、以及原始类的所有子类可用。在运行时，通过分类添加的方法和原始类自身实现的方法之间没有任何区别。

回想一下前面几章中的 `XYZPerson` 类，它有表示一个人的名和姓的属性。如果你正在编写一个记录管理应用，你可能会发现自己经常需要按姓氏显示一个人员列表，就像这样：

```
Appleseed, John
Doe, Jane
Smith, Bob
Warwick, Kate
```

与其每次要显示时都编写代码来生成合适的 `lastName, firstName` 字符串，你可以给 `XYZPerson` 类添加一个分类，就像这样：

```objc
#import "XYZPerson.h"

@interface XYZPerson (XYZPersonNameDisplayAdditions)
- (NSString *)lastNameFirstNameString;
@end
```

在这个例子中，`XYZPersonNameDisplayAdditions` 分类声明了一个额外的方法，用来返回所需的字符串。

分类通常在单独的头文件中声明，并在单独的源代码文件中实现。对于 `XYZPerson` 来说，你可能会在一个名为 `XYZPerson+XYZPersonNameDisplayAdditions.h` 的头文件中声明这个分类。

尽管分类添加的方法对该类及其子类的所有实例都可用，但在任何想要使用这些额外方法的源代码文件中，你都需要导入分类的头文件，否则就会遇到编译器警告和错误。

分类的实现可能是这样的：

```objc
#import "XYZPerson+XYZPersonNameDisplayAdditions.h"

@implementation XYZPerson (XYZPersonNameDisplayAdditions)
- (NSString *)lastNameFirstNameString {
    return [NSString stringWithFormat:@"%@, %@", self.lastName, self.firstName];
}
@end
```

一旦你声明了一个分类并实现了其中的方法，你就可以在该类的任何实例上使用这些方法，就好像它们本来就是原始类接口的一部分：

```objc
#import "XYZPerson+XYZPersonNameDisplayAdditions.h"
@implementation SomeObject
- (void)someMethod {
    XYZPerson *person = [[XYZPerson alloc] initWithFirstName:@"John"
                                                    lastName:@"Doe"];
    XYZShoutingPerson *shoutingPerson =
                        [[XYZShoutingPerson alloc] initWithFirstName:@"Monica"
                                                            lastName:@"Robinson"];

    NSLog(@"The two people are %@ and %@",
         [person lastNameFirstNameString], [shoutingPerson lastNameFirstNameString]);
}
@end
```

除了单纯给现有类添加方法之外，你还可以用分类把一个复杂类的实现拆分到多个源代码文件中。举例来说，如果一个自定义用户界面元素的几何计算、颜色、渐变等特别复杂，你可以把它的绘制代码放在与其余实现代码分开的文件里。另外，你也可以根据是在为 OS X 还是 iOS 编写应用，为分类方法提供不同的实现。

分类既可以用来声明实例方法，也可以用来声明类方法，但通常不适合用来声明额外的属性。在分类接口里包含属性声明是合法的语法，但没办法在分类中声明额外的实例变量。这意味着编译器不会为其合成任何实例变量，也不会合成任何属性存取方法。你可以在分类的实现中自己编写存取方法，但除非该值已经由原始类存储，否则你无法保存这个属性的值。

要给现有类添加一个由新实例变量支撑的传统属性，唯一的办法是使用类扩展，具体说明见[类扩展扩充内部实现](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnrnknltg)。

因为分类中声明的方法会被添加到现有类中，所以你需要非常小心地对待方法名。

如果一个在分类中声明的方法，其名称与原始类中的某个方法相同，或者与同一个类的另一个分类（甚至超类）中的某个方法相同，那么运行时到底会使用哪个方法实现，其行为是未定义的。如果你是在自己的类上使用分类，这不太可能成为问题，但如果用分类给标准 Cocoa 或 Cocoa Touch 类添加方法，就可能引发问题。

举例来说，一个与远程 Web 服务打交道的应用，可能需要一种简便的方式对一串字符进行 Base64 编码。给 `NSString` 定义一个分类，添加一个实例方法来返回字符串的 Base64 编码版本，这样做是合理的，于是你可能会添加一个名为 `base64EncodedString` 的便利方法。

但如果你链接的另一个框架碰巧也在 `NSString` 上定义了自己的分类，其中也包含一个叫 `base64EncodedString` 的方法，问题就出现了。在运行时，只有一个方法实现会“胜出”并被添加到 `NSString` 上，但具体是哪一个是未定义的。

如果你给 Cocoa 或 Cocoa Touch 类添加了便利方法，而这些方法在后来的版本中又被加入到了原始类里，也可能引发另一个问题。举例来说，用来描述一组对象应如何排序的 `NSSortDescriptor` 类，一直都有一个 `initWithKey:ascending:` 初始化方法，但在早期的 OS X 和 iOS 版本中并没有提供相应的类工厂方法。

按照惯例，这个类工厂方法应该叫 `sortDescriptorWithKey:ascending:`，所以你可能会选择在 `NSSortDescriptor` 上添加一个分类，来提供这个便利方法。在较旧版本的 OS X 和 iOS 下，这样做本应像你预期的那样运作，但随着 Mac OS X 10.6 和 iOS 4.0 的发布，`sortDescriptorWithKey:ascending:` 方法被加入到了原始的 `NSSortDescriptor` 类中，这意味着当你的应用在这些或更新的平台上运行时，就会出现命名冲突。

为了避免出现未定义行为，最佳实践是给框架类上分类中的方法名加上前缀，就像你应该给自己_类_的名字加前缀一样。你可以选择使用与类前缀相同的三个字母，但按照方法名的通常惯例改为小写，再加一个下划线，然后才是方法名的其余部分。对于 `NSSortDescriptor` 这个例子，你自己的分类可能是这样的：

```objc
@interface NSSortDescriptor (XYZAdditions)
+ (id)xyz_sortDescriptorWithKey:(NSString *)key ascending:(BOOL)ascending;
@end
```

这意味着你可以确定自己的方法在运行时一定会被使用。歧义被消除了，因为你的代码现在是这样的：

```
    NSSortDescriptor *descriptor =
               [NSSortDescriptor xyz_sortDescriptorWithKey:@"name" ascending:YES];
```


类扩展与分类有几分相似，但它只能添加到你在编译期拥有其源代码的类上（该类会与类扩展一起编译）。类扩展所声明的方法要在原始类的 `@implementation` 代码块中实现，所以举例来说，你不能在框架类（比如 `NSString` 这样的 Cocoa 或 Cocoa Touch 类）上声明类扩展。

声明类扩展的语法与分类的语法类似，就像这样：

```objc
@interface ClassName ()

@end
```

因为圆括号里没有给出名称，类扩展常常被称为_匿名分类（anonymous category）_。

与普通分类不同，类扩展可以给一个类添加自己的属性和实例变量。如果你在类扩展中声明一个属性，就像这样：

```objc
@interface XYZPerson ()
@property NSObject *extraProperty;
@end
```

编译器就会在主类实现内部自动合成相应的存取方法，以及一个实例变量。

如果你在类扩展中添加了任何_方法_，这些方法就必须在该类的主实现中实现。

你也可以用类扩展来添加自定义实例变量。这些变量在类扩展接口中的花括号内声明：

```objc
@interface XYZPerson () {
    id _someCustomInstanceVariable;
}
...
@end
```


一个类的主接口用来定义其他类应该如何与它交互。换句话说，它是该类的_公共（public）_接口。

类扩展常常被用来扩充公共接口，加入额外的_私有（private）_方法或属性，供类自身的实现内部使用。举例来说，常见的做法是在接口中把一个属性定义为 `readonly`，而在实现之上声明的类扩展中把它定义为 `readwrite`，这样类的内部方法就可以直接修改该属性的值。

举个例子，`XYZPerson` 类可能会添加一个名为 `uniqueIdentifier` 的属性，用来保存类似美国社会安全号码这样的信息。

在现实世界中，给个人分配一个唯一标识符通常需要办理大量手续，所以 `XYZPerson` 类接口可能会把这个属性声明为 `readonly`，并提供某个方法来请求分配一个标识符，就像这样：

```objc
@interface XYZPerson : NSObject
...
@property (readonly) NSString *uniqueIdentifier;
- (void)assignUniqueIdentifier;
@end
```

这意味着 `uniqueIdentifier` 不可能被另一个对象直接设置。如果某个人还没有标识符，就必须调用 `assignUniqueIdentifier` 方法来请求分配一个。

为了让 `XYZPerson` 类能够在内部修改这个属性，合理的做法是在该类实现文件顶部定义的类扩展中重新声明这个属性：

```objc
@interface XYZPerson ()
@property (readwrite) NSString *uniqueIdentifier;
@end

@implementation XYZPerson
...
@end
```

这意味着编译器现在也会合成一个 setter 方法，所以 `XYZPerson` 实现内部的任何方法都可以用 setter 或点语法直接设置这个属性。

通过在 `XYZPerson` 实现的源代码文件内部声明这个类扩展，这些信息就只对 `XYZPerson` 类保持私有。如果另一种类型的对象试图设置这个属性，编译器就会产生一个错误。

分类和类扩展让你可以很方便地直接给现有类添加行为，但有时候这并不是最好的选择。

面向对象编程的主要目标之一，是编写可复用的代码，这意味着类应该尽可能在各种情况下都能被复用。举例来说，如果你正在创建一个视图类来描述一个在屏幕上显示信息的对象，最好想一想这个类是否能在多种场合下使用。

与其把关于布局或内容的决策硬编码进去，一种做法是利用继承，把这些决策留给专门设计成供子类覆写的方法。虽然这确实能让这个类相对容易复用，但每次想使用这个原始类时，你仍然需要创建一个新的子类。

另一种做法是让类使用一个_委托（delegate）_对象。任何可能限制复用性的决策，都可以委托给另一个对象，由它在运行时来做出这些决策。一个常见的例子是标准的 table view 类（OS X 上的 `NSTableView` 和 iOS 上的 `UITableView`）。为了让一个通用的 table view（一个用一列或多列、一行或多行来显示信息的对象）能够发挥作用，它把关于内容的决策留给另一个对象在运行时决定。委托将在下一章[使用协议](Working%20with%20Protocols.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqmjrfvjvomi)中详细介绍。

Objective-C 通过 Objective-C 运行时系统提供其动态行为。

许多决策，比如发送消息时到底调用哪个方法，并不是在编译期做出的，而是在应用运行时才被决定。Objective-C 不仅仅是一门被编译成机器代码的语言，它还需要有一个运行时系统就位，才能执行这些代码。

你可以直接与这个运行时系统交互，比如给一个对象添加_关联引用（associative reference）_。与类扩展不同，关联引用不会影响原始类的声明和实现，这意味着即便你没有原始源代码的访问权限，也可以在框架类上使用它们。

关联引用以类似于属性或实例变量的方式，把一个对象和另一个对象关联起来。要了解更多信息，请参阅[关联引用](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocAssociativeReferences.html#//apple_ref/doc/uid/TP30001163-CH24)。要进一步了解 Objective-C 运行时的整体情况，请参阅 _[Objective-C 运行时编程指南](../Objective-C%20Runtime%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danby)_。

1. 给 `XYZPerson` 类添加一个分类，声明并实现额外的行为，比如以不同方式显示一个人的姓名。
2. 给 `NSString` 添加一个分类，添加一个方法，在给定的点上绘制字符串的大写版本，调用现有 `NSStringDrawing` 分类方法之一来执行实际的绘制。这些方法记录在 iOS 的 _NSString UIKit Additions Reference_ 和 OS X 的 _NSString Application Kit Additions Reference_ 中。
3. 给原始的 `XYZPerson` 类实现添加两个 `readonly` 属性，分别表示一个人的身高和体重，并添加 `measureWeight` 和 `measureHeight` 方法。

   使用类扩展把这些属性重新声明为 `readwrite`，并实现这些方法，把属性设置为合适的值。

[下一页](Working%20with%20Protocols.md)[上一页](Encapsulating%20Data.md)

