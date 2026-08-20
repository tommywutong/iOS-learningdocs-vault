---
title: 用 Objective-C 编程
apple_id: TP40011210
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/EncapsulatingData/EncapsulatingData.html
archived_at: '2026-07-15T07:17:52.399572Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [用 Objective-C 编程](About%20Objective-C.md)


[下一页](Customizing%20Existing%20Classes.md)[上一页](Working%20with%20Objects.md)

# 封装数据

除了上一章介绍的消息传递行为之外，对象还通过其属性（property）封装数据。

本章介绍用于为对象声明属性的 Objective-C 语法，并说明这些属性在默认情况下是如何通过合成存取方法和实例变量来实现的。如果一个属性由实例变量支撑，那么该变量必须在任何初始化方法中被正确设置。

如果一个对象需要通过属性维持与另一个对象的链接，那么考虑这两个对象之间关系的性质就很重要。虽然 Objective-C 对象的内存管理大部分是通过自动引用计数（ARC）替你处理的，但了解如何避免诸如强引用循环这样会导致内存泄漏的问题仍然很重要。本章解释了对象的生命周期，并描述了如何通过关系来思考对对象图的管理。

大多数对象都需要跟踪信息以完成它们的任务。有些对象被设计用来对一个或多个值建模，比如 Cocoa 的 `NSNumber` 类用来保存一个数值，或者自定义的 `XYZPerson` 类用来对一个有名和姓的人建模。有些对象的作用范围更宽泛，可能是处理用户界面与其所显示信息之间的交互，但即便是这些对象，也需要跟踪用户界面元素或相关的模型对象。

Objective-C 属性提供了一种方式来定义一个类打算封装的信息。正如你在[属性控制对对象值的访问](Defining%20Classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqmznknlto)中所看到的，属性声明包含在类的接口中，就像这样：

```objc
@interface XYZPerson : NSObject
@property NSString *firstName;
@property NSString *lastName;
@end
```

在这个例子中，`XYZPerson` 类声明了两个字符串属性来保存一个人的名和姓。

考虑到面向对象编程的一个主要原则是对象应该把内部工作细节隐藏在其公共接口之后，因此通过对象暴露的行为来访问对象的属性、而不是试图直接访问内部值，这一点非常重要。

你通过存取方法（accessor）来访问或设置一个对象的属性：

```objc
    NSString *firstName = [somePerson firstName];
    [somePerson setFirstName:@"Johnny"];
```

默认情况下，这些存取方法会由编译器自动合成，所以除了在类接口中用 `@property` 声明属性之外，你不需要做任何其他事情。

合成的方法遵循特定的命名约定：

- 用于访问值的方法（_取值方法（getter）_）与属性同名。

  名为 `firstName` 的属性的取值方法也会被叫做 `firstName`。
- 用于设置值的方法（_赋值方法（setter）_）以单词"set"开头，后面跟上首字母大写的属性名。

  名为 `firstName` 的属性的赋值方法会被叫做 `setFirstName:`。

如果你不希望允许通过赋值方法来更改某个属性，可以给属性声明添加一个特性（attribute），指定它应为 `readonly`：

```objc
@property (readonly) NSString *fullName;
```

除了向其他对象展示它们应该如何与该属性交互之外，特性还告诉编译器该如何合成相应的存取方法。

在这种情况下，编译器会合成一个 `fullName` 取值方法，但不会合成 `setFullName:` 方法。

如果你想为存取方法使用不同的名字，可以通过给属性添加特性来指定一个自定义名称。对于布尔属性（值为 `YES` 或 `NO` 的属性），惯例是让取值方法以"is"开头。例如，名为 `finished` 的属性的取值方法应该叫做 `isFinished`。

同样，可以在属性上添加一个特性：

```objc
@property (getter=isFinished) BOOL finished;
```

如果你需要指定多个特性，只需将它们以逗号分隔列出即可，像这样：

```objc
@property (readonly, getter=isFinished) BOOL finished;
```

在这种情况下，编译器只会合成一个 `isFinished` 方法，而不会合成 `setFinished:` 方法。

除了显式调用存取方法之外，Objective-C 还提供了一种替代的点语法（dot syntax）来访问对象的属性。

点语法允许你像这样访问属性：

```objc
    NSString *firstName = somePerson.firstName;
    somePerson.firstName = @"Johnny";
```

点语法纯粹是对存取方法调用的一种便捷包装。当你使用点语法时，属性仍然是通过上面提到的取值方法和赋值方法来访问或更改的：

- 使用 `somePerson.firstName` 取值等同于使用 `[somePerson firstName]`
- 使用 `somePerson.firstName = @"Johnny"` 赋值等同于使用 `[somePerson setFirstName:@"Johnny"]`

这意味着通过点语法访问属性同样受属性特性的控制。如果一个属性被标记为 `readonly`，那么当你试图通过点语法设置它时，会得到一个编译器错误。

默认情况下，一个 `readwrite` 属性会由一个实例变量支撑，而这个实例变量同样会由编译器自动合成。

实例变量是一种在对象的整个生命周期内存在并持有其值的变量。实例变量所使用的内存在对象首次创建时（通过 `alloc`）分配，并在对象被释放时回收。

除非你另行指定，否则合成的实例变量与属性同名，但会带有一个下划线前缀。例如，对于名为 `firstName` 的属性，合成的实例变量会被叫做 `_firstName`。

虽然让一个对象通过存取方法或点语法访问自己的属性是最佳实践，但也可以从类实现中的任何实例方法内直接访问实例变量。下划线前缀可以清楚地表明你访问的是一个实例变量，而不是（比如说）一个局部变量：

```objc
- (void)someMethod {
    NSString *myString = @"An interesting string";

    _someString = myString;
}
```

在这个例子中，`myString` 显然是一个局部变量，而 `_someString` 是一个实例变量。

一般来说，即使你是在对象自己的实现内部访问其属性，也应该使用存取方法或点语法来进行属性访问，此时你应该使用 `self`：

```objc
- (void)someMethod {
    NSString *myString = @"An interesting string";

    self.someString = myString;
  // or
    [self setSomeString:myString];
}
```

这条规则的例外情况是在编写初始化、释放或自定义存取方法时，本节稍后会介绍。

如前所述，可写属性的默认行为是使用一个名为 `_propertyName` 的实例变量。

如果你希望为实例变量使用一个不同的名字，需要在实现中用以下语法指示编译器合成该变量：

```objc
@implementation YourClass
@synthesize propertyName = instanceVariableName;
...
@end
```

例如：

```objc
@synthesize firstName = ivar_firstName;
```

在这种情况下，该属性仍然叫做 `firstName`，并且仍可以通过 `firstName` 和 `setFirstName:` 存取方法或点语法来访问，但它将由一个名为 `ivar_firstName` 的实例变量支撑。

最佳实践是：只要你需要跟踪一个值或另一个对象，就在对象上使用一个属性。

如果你确实需要在不声明属性的情况下定义自己的实例变量，可以把它们添加在类接口或实现顶部的大括号内，像这样：

```objc
@interface SomeClass : NSObject {
    NSString *_myNonPropertyInstanceVariable;
}
...
@end

@implementation SomeClass {
    NSString *_anotherCustomInstanceVariable;
}
...
@end
```


赋值方法可能带有额外的副作用。它们可能触发 KVC 通知，或者如果你自己编写了自定义方法，还可能执行进一步的任务。

你应该始终在初始化方法内部直接访问实例变量，因为在设置属性的那一刻，对象的其余部分可能还没有完全初始化完毕。即使你没有提供自定义的存取方法，或者不了解自己类中有任何副作用，将来的某个子类也很可能会重写这个行为。

一个典型的 `init` 方法看起来像这样：

```objc
- (id)init {
    self = [super init];

    if (self) {
        // initialize instance variables here
    }

    return self;
}
```

在执行自己的初始化之前，`init` 方法应该把 `self` 赋值为调用超类初始化方法的结果。超类可能无法正确初始化对象而返回 `nil`，所以在执行自己的初始化之前，你应该始终检查确认 `self` 不是 `nil`。

通过在方法的第一行调用 `[super init]`，一个对象会从它的根类开始，依次向下经过每个子类的 `init` 实现来完成初始化。[图 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnjnknltcmq) 展示了初始化一个 `XYZShoutingPerson` 对象的过程。

__图 3-1__  初始化过程

!!

正如你在上一章所看到的，一个对象要么通过调用 `init` 来初始化，要么通过调用一个用特定值来初始化对象的方法来初始化。

对于 `XYZPerson` 类而言，提供一个用来设置该人初始名和姓的初始化方法是合理的：

```objc
- (id)initWithFirstName:(NSString *)aFirstName lastName:(NSString *)aLastName;
```

你可以像这样实现该方法：

```objc
- (id)initWithFirstName:(NSString *)aFirstName lastName:(NSString *)aLastName {
    self = [super init];

    if (self) {
        _firstName = aFirstName;
        _lastName = aLastName;
    }

    return self;
}
```


如果一个对象声明了一个或多个初始化方法，你应该确定哪个方法是 _指定初始化方法（designated initializer）_。这通常是提供最多初始化选项的方法（比如参数最多的方法），并且会被你为方便起见编写的其他方法所调用。你通常还应该重写 `init`，使其用合适的默认值调用你的指定初始化方法。

如果 `XYZPerson` 还拥有一个用于出生日期的属性，那么指定初始化方法可能是这样的：

```objc
- (id)initWithFirstName:(NSString *)aFirstName lastName:(NSString *)aLastName
                                            dateOfBirth:(NSDate *)aDOB;
```

这个方法会像前面展示的那样设置相关的实例变量。如果你仍然希望提供一个只需要名和姓的便捷初始化方法，可以像这样实现该方法，让它调用指定初始化方法：

```objc
- (id)initWithFirstName:(NSString *)aFirstName lastName:(NSString *)aLastName {
    return [self initWithFirstName:aFirstName lastName:aLastName dateOfBirth:nil];
}
```

你也可以实现一个标准的 `init` 方法来提供合适的默认值：

```objc
- (id)init {
    return [self initWithFirstName:@"John" lastName:@"Doe" dateOfBirth:nil];
}
```

如果你需要在派生子类时为一个使用了多个 `init` 方法的类编写初始化方法，你应该要么重写超类的指定初始化方法来执行自己的初始化，要么添加自己额外的初始化方法。无论哪种方式，你都应该在执行任何自己的初始化之前，调用超类的指定初始化方法（取代 `[super init];`）。

属性不一定总是要由自己的实例变量支撑。

举个例子，`XYZPerson` 类可能会为一个人的全名定义一个只读属性：

```objc
@property (readonly) NSString *fullName;
```

与其在每次名或姓变化时都去更新 `fullName` 属性，不如直接编写一个自定义存取方法，在被请求时按需构建全名字符串，这样会更简单：

```objc
- (NSString *)fullName {
    return [NSString stringWithFormat:@"%@ %@", self.firstName, self.lastName];
}
```

这个简单的例子使用了格式字符串和格式说明符（在上一章中有介绍）来构建一个包含一个人的名和姓、并以空格分隔的字符串。

如果你需要为一个确实使用实例变量的属性编写自定义存取方法，那么你必须在方法内部直接访问该实例变量。例如，一种常见做法是使用"惰性存取方法（lazy accessor）"，把属性的初始化推迟到它第一次被请求的时候，就像这样：

```objc
- (XYZObject *)someImportantObject {
    if (!_someImportantObject) {
        _someImportantObject = [[XYZObject alloc] init];
    }

    return _someImportantObject;
}
```

在返回值之前，这个方法先检查 `_someImportantObject` 实例变量是否为 `nil`；如果是，就分配一个对象。

默认情况下，一个 Objective-C 属性是 _原子（atomic）_ 的：

```objc
@interface XYZObject : NSObject
@property NSObject *implicitAtomicObject;          // 默认就是 atomic
@property (atomic) NSObject *explicitAtomicObject; // 显式标记为 atomic
@end
```

这意味着即使存取方法是从不同线程同时被调用的，合成的存取方法也能保证一个值总是通过取值方法被完整取出、或者通过赋值方法被完整设置。

由于原子（atomic）存取方法的内部实现和同步机制是私有的，因此无法将一个合成的存取方法与你自己实现的存取方法结合使用。举例来说，如果你试图为一个 `atomic`、`readwrite` 的属性提供自定义赋值方法，却把取值方法留给编译器合成，你会得到一个编译器警告。

你可以使用 `nonatomic` 属性特性来指定，合成的存取方法只是直接设置或返回一个值，对于该值被不同线程同时访问时会发生什么不做任何保证。因此，访问一个 `nonatomic` 属性比访问一个 `atomic` 属性更快，而且可以放心地将一个合成的赋值方法与你自己实现的取值方法结合使用，例如：

```objc
@interface XYZObject : NSObject
@property (nonatomic) NSObject *nonatomicObject;
@end
```

```objc
@implementation XYZObject
- (NSObject *)nonatomicObject {
    return _nonatomicObject;
}
// 赋值方法会被自动合成
@end
```


正如你已经看到的，Objective-C 对象的内存是动态分配的（在堆上），这意味着你需要使用指针来跟踪一个对象的地址。与标量值不同，对象的生命周期并不总能通过某一个指针变量的作用域来确定。相反，只要一个对象仍被其他对象所需要，它就必须在内存中保持活跃。

与其试图操心手动管理每个对象的生命周期，你应该转而思考对象之间的关系。

以 `XYZPerson` 对象为例，`firstName` 和 `lastName` 这两个字符串属性实际上是被 `XYZPerson` 实例所"拥有"的。这意味着只要 `XYZPerson` 对象还留在内存中，它们就应该留在内存中。

当一个对象以这种方式依赖于其他对象、实际上取得了对那些对象的所有权时，我们说第一个对象拥有指向其他对象的 _强引用（strong reference）_。在 Objective-C 中，只要一个对象至少有一个来自另一个对象的强引用，它就会被保持存活。[图 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnjnknltcna) 展示了 `XYZPerson` 实例与两个 `NSString` 对象之间的关系。

__图 3-2__  强引用关系

!

当一个 `XYZPerson` 对象从内存中被释放时，假设没有其他强引用留在这两个字符串对象上，那么这两个字符串对象也会被释放。

为了给这个例子增加一点复杂度，考虑一下如 [图 3-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnjnknltcoa) 所示的某个应用程序的对象图。

__图 3-3__  Name Badge Maker 应用程序

!

当用户点击 Update 按钮时，姓名牌预览会用相关的姓名信息进行更新。

第一次输入某个人的详细信息并点击 update 按钮时，简化后的对象图可能看起来像 [图 3-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnjnknltcoi)。

__图 3-4__  初次创建 XYZPerson 时的简化对象图

!!

当用户修改这个人的名（first name）时，对象图会变成 [图 3-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnjnknltema) 所示的样子。

__图 3-5__  修改这个人的 first name 时的简化对象图

!!

即使 `XYZPerson` 对象现在有了一个不同的 `firstName`，姓名牌显示视图仍然保持着对原始 `@"John"` 字符串对象的强引用关系。这意味着 `@"John"` 对象仍留在内存中，供姓名牌视图用来打印名字。

一旦用户第二次点击 Update 按钮，姓名牌视图就会被告知去更新其内部属性以匹配这个 person 对象，于是对象图看起来就像 [图 3-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnjnknltemi) 那样。

__图 3-6__  更新姓名牌视图后的对象图

!!

此时，原来的 `@"John"` 对象已经没有任何强引用指向它了，所以它会从内存中被移除。

默认情况下，Objective-C 的属性和变量都保持着对其对象的强引用。这在很多情况下都没问题，但确实会带来强引用循环这一潜在问题。

虽然强引用对于对象之间的单向关系效果很好，但在处理一组相互连接的对象时，你需要格外小心。如果一组对象由一个由强引用关系构成的环连接在一起，即使组外没有任何强引用指向它们，它们也会彼此保持存活。

一个明显的潜在引用循环的例子，存在于一个表格视图对象（iOS 上的 `UITableView`、OS X 上的 `NSTableView`）与其委托之间。为了让一个通用的表格视图类能在多种场景下都有用，它把一些决策[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)给了外部对象。这意味着它要依赖另一个对象来决定它显示什么内容，或者当用户与表格视图中某个特定条目交互时该做什么。

一种常见的场景是，表格视图持有一个指向其委托的引用，而委托又持有一个指回表格视图的引用，如 [图 3-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnjnknlteni) 所示。

__图 3-7__  表格视图与其委托之间的强引用

!

如果其他对象放弃了它们对表格视图和委托的强引用关系，就会出现问题，如 [图 3-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnjnknltenq) 所示。

__图 3-8__  强引用循环

!

尽管这些对象并不需要被保留在内存中——除了这两个对象之间的关系之外，没有任何强引用关系指向表格视图或委托——但剩下的这两个强引用关系仍然让这两个对象保持存活。这就是所谓的 _强引用循环（strong reference cycle）_。

解决这个问题的办法，是把其中一个强引用替换成一个 _弱引用（weak reference）_。弱引用并不意味着两个对象之间存在所有权或责任关系，也不会让一个对象保持存活。

如果把表格视图修改为对其委托使用弱引用关系（`UITableView` 和 `NSTableView` 正是这样解决这个问题的），那么最初的对象图现在看起来就像 [图 3-9](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnjnknlteny)。

__图 3-9__  表格视图与其委托之间正确的关系

!

这一次，当对象图中的其他对象放弃了它们对表格视图和委托的强引用关系时，就不再有任何强引用留在委托对象上了，如 [图 3-10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnjnknlteoa) 所示。

__图 3-10__  避免强引用循环

!

这意味着委托对象会被释放，从而解除它对表格视图的强引用，如 [图 3-11](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnjnknlteoi) 所示。

__图 3-11__  释放委托

!

一旦委托被释放，就不再有任何强引用指向表格视图了，所以它也会被释放。

默认情况下，像这样声明的对象属性：

```objc
@property id delegate;
```

会对其合成的实例变量使用强引用。要声明一个弱引用，可以给属性添加一个特性，像这样：

```objc
@property (weak) id delegate;
```

局部变量（以及非属性的实例变量）默认也保持着对对象的强引用。这意味着下面的代码会完全按你期望的方式运行：

```objc
    NSDate *originalDate = self.lastModificationDate;
    self.lastModificationDate = [NSDate date];
    NSLog(@"Last modification date changed from %@ to %@",
                        originalDate, self.lastModificationDate);
```

在这个例子中，局部变量 `originalDate` 对最初的 `lastModificationDate` 对象保持着强引用。当 `lastModificationDate` 属性被更改后，这个属性不再对原来的日期保持强引用，但那个日期对象仍然由 `originalDate` 这个强变量保持存活。

如果你不希望一个变量保持强引用，可以把它声明为 `__weak`，像这样：

```objc
    NSObject * __weak weakVariable;
```

因为弱引用不会让一个对象保持存活，所以引用所指向的对象有可能在该引用仍在使用时就被释放。为了避免留下一个指向已释放对象原先所占内存的危险悬空指针，当一个对象被释放时，指向它的弱引用会被自动设为 `nil`。

这意味着，如果你在前面的日期示例中使用一个弱变量：

```objc
    NSDate * __weak originalDate = self.lastModificationDate;
    self.lastModificationDate = [NSDate date];
```

`originalDate` 变量就有可能被设为 `nil`。当 `self.lastModificationDate` 被重新赋值时，该属性不再对原来的日期保持强引用。如果没有其他强引用指向它，原来的日期就会被释放，`originalDate` 也随之被设为 `nil`。

弱变量可能会造成困惑，尤其是在像这样的代码中：

```objc
    NSObject * __weak someObject = [[NSObject alloc] init];
```

在这个例子中，新分配的对象没有任何强引用指向它，所以它会立即被释放，`someObject` 被设为 `nil`。

同样重要的是，要考虑一个需要多次访问某个弱属性的方法会带来的影响，像这样：

```objc
- (void)someMethod {
    [self.weakProperty doSomething];
    ...
    [self.weakProperty doSomethingElse];
}
```

在这种情况下，你可能想把这个弱属性缓存到一个强变量中，以确保只要你还需要用到它，它就会一直留在内存里：

```objc
- (void)someMethod {
    NSObject *cachedObject = self.weakProperty;
    [cachedObject doSomething];
    ...
    [cachedObject doSomethingElse];
}
```

在这个例子中，`cachedObject` 变量对最初的弱属性值保持着强引用，因此只要 `cachedObject` 仍在作用域内（并且没有被重新赋成另一个值），该对象就不会被释放。

如果你需要在使用一个弱属性之前确认它不是 `nil`，那么牢记这一点尤为重要。仅仅像这样测试是不够的：

```objc
    if (self.someWeakProperty) {
        [someObject doSomethingImportantWith:self.someWeakProperty];
    }
```

因为在一个多线程应用程序中，该属性可能会在测试和方法调用之间被释放，使得这次测试失去意义。你需要转而声明一个强局部变量来缓存这个值，像这样：

```objc
    NSObject *cachedObject = self.someWeakProperty;           // 1
    if (cachedObject) {                                       // 2
        [someObject doSomethingImportantWith:cachedObject];   // 3
    }                                                         // 4
    cachedObject = nil;                                       // 5
```

在这个例子中，强引用是在第 1 行建立的，这意味着在测试和方法调用期间，该对象保证是存活的。在第 5 行，`cachedObject` 被设为 `nil`，从而放弃了这个强引用。如果此时原始对象没有其他强引用指向它，它就会被释放，`someWeakProperty` 也会被设为 `nil`。

Cocoa 和 Cocoa Touch 中有少数几个类目前还不支持弱引用，这意味着你无法声明弱属性或弱局部变量来跟踪它们。这些类包括 `NSTextView`、`NSFont` 和 `NSColorSpace`；完整列表请参阅 _[Transitioning to ARC Release Notes](../../../releasenotes/Objective%20C/Transitioning%20to%20ARC%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrw)_。

如果你需要对这些类之一使用弱引用，就必须使用非安全（unsafe）引用。对于属性来说，这意味着使用 `unsafe_unretained` 特性：

```objc
@property (unsafe_unretained) NSObject *unsafeProperty;
```

对于变量，你需要使用 `__unsafe_unretained`：

```objc
    NSObject * __unsafe_unretained unsafeReference;
```

非安全引用与弱引用类似，都不会让与之关联的对象保持存活，但如果目标对象被释放，它不会被设为 `nil`。这意味着你会留下一个指向已释放对象原先所占内存的悬空指针，"unsafe"（非安全）一词由此而来。向一个悬空指针发送消息会导致崩溃。

在某些情况下，一个对象可能希望为设置给它的属性的对象保留自己的一份拷贝。

举个例子，前面 [图 3-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnjnknltcoi) 中展示的 `XYZBadgeView` 类的类接口可能是这样的：

```objc
@interface XYZBadgeView : NSView
@property NSString *firstName;
@property NSString *lastName;
@end
```

这里声明了两个 `NSString` 属性，它们都隐式地对其对象保持着强引用。

考虑一下，如果另一个对象创建了一个字符串，并将其设置为姓名牌视图的某个属性，会发生什么，像这样：

```objc
    NSMutableString *nameString = [NSMutableString stringWithString:@"John"];
    self.badgeView.firstName = nameString;
```

这是完全合法的，因为 `NSMutableString` 是 `NSString` 的子类。虽然姓名牌视图认为自己处理的是一个 `NSString` 实例，但实际上它处理的是一个 `NSMutableString`。

这意味着这个字符串是可以改变的：

```objc
    [nameString appendString:@"ny"];
```

在这种情况下，虽然这个名字在最初被设置给姓名牌视图的 `firstName` 属性时是"John"，但由于这个可变字符串被更改了，它现在变成了"Johnny"。

你可能希望姓名牌视图为设置给其 `firstName` 和 `lastName` 属性的任何字符串都维护自己的一份拷贝，从而有效地捕获属性被设置那一刻的字符串内容。通过给这两个属性声明添加一个 `copy` 特性：

```objc
@interface XYZBadgeView : NSView
@property (copy) NSString *firstName;
@property (copy) NSString *lastName;
@end
```

现在这个视图为这两个字符串各维护了一份自己的拷贝。即使设置了一个可变字符串、并且随后又发生了改变，姓名牌视图捕获到的也是该字符串在被设置那一刻的值。例如：

```objc
    NSMutableString *nameString = [NSMutableString stringWithString:@"John"];
    self.badgeView.firstName = nameString;
    [nameString appendString:@"ny"];
```

这一次，姓名牌视图所持有的 `firstName` 将是原始"John"字符串一份不受影响的拷贝。

`copy` 特性意味着该属性会使用强引用，因为它必须持有自己创建出的这个新对象。

如果你需要直接设置一个带 `copy` 特性的属性的实例变量，例如在一个初始化方法中，不要忘记设置原始对象的一份拷贝：

```objc
- (id)initWithSomeOriginalString:(NSString *)aString {
    self = [super init];
    if (self) {
        _instanceVariableForCopyProperty = [aString copy];
    }
    return self;
}
```


1. 修改 `XYZPerson` 类中的 `sayHello` 方法，用这个人的 first name 和 last name 记录一句问候语。
2. 声明并实现一个新的指定初始化方法，用于通过指定的名、姓和出生日期创建一个 `XYZPerson`，同时提供一个合适的类工厂方法。

   别忘了重写 `init`，让它调用这个指定初始化方法。
3. 测试一下，如果你把一个可变字符串设置为这个人的 first name，然后在调用你修改后的 `sayHello` 方法之前改变这个字符串，会发生什么。给 `NSString` 属性声明添加 `copy` 特性，再测试一次。
4. 尝试在 `main()` 函数中使用各种各样的强变量和弱变量来创建 `XYZPerson` 对象。验证一下强变量是否至少在你所预期的时间内让 `XYZPerson` 对象保持存活。

   为了帮助验证一个 `XYZPerson` 对象何时被释放，你可能想通过在 `XYZPerson` 实现中提供一个 `dealloc` 方法来介入对象的生命周期。当一个 Objective-C 对象从内存中被释放时，这个方法会被自动调用，通常用来释放你手动分配的任何内存，比如通过 C 的 `malloc()` 函数分配的内存，具体请参阅 _[Advanced Memory Management Programming Guide](../Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytc2i)_。

   出于本练习的目的，在 `XYZPerson` 中重写 `dealloc` 方法来记录一条消息，像这样：

```objc
- (void)dealloc {
    NSLog(@"XYZPerson is being deallocated");
}
```

   尝试把每个 `XYZPerson` 指针变量都设为 `nil`，验证这些对象是否在你所预期的时候被释放。
5. 修改 `XYZPerson` 类的描述，使其能够跟踪一个配偶或伴侣。

   你需要决定如何最好地对这种关系建模，并仔细考虑对象图的管理方式。

[下一页](Customizing%20Existing%20Classes.md)[上一页](Working%20with%20Objects.md)

