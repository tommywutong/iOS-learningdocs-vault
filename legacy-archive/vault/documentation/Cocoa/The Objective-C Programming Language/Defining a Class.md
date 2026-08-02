---
title: Objective-C 编程语言
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocDefiningClasses.html
archived_at: '2026-07-15T07:17:29.443418Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 编程语言](Introduction.md)


[下一页](Protocols.md)[上一页](Objects%2C%20Classes%2C%20and%20Messaging.md)

# 定义类

大部分面向对象编程工作都是编写新对象的代码——也就是定义新的类。在 Objective-C 中，类分为两部分定义：

- 一个_接口_，用于声明类的方法和属性，并指明其超类
- 一个_实现_，用于真正定义这个类（包含实现其方法的代码）

这两部分通常各自位于独立的文件中。不过，有时借助一种叫做_分类_的特性，类的定义也会分散在多个文件里。分类可以把类的定义拆分成若干部分，也可以扩展一个已有的类。分类在[分类与扩展](Categories%20and%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmrqfvjvomi)中有详细说明。

虽然编译器并不强制要求，但类的接口和实现通常放在两个不同的文件中。接口文件必须让所有使用该类的人都能获取到。

单个文件可以声明或实现多个类。不过按照惯例，即使不为每个类都单独建立实现文件，通常也会为每个类单独建立一个接口文件。让类的接口彼此独立，能更好地体现它们作为独立实体的地位。

接口文件和实现文件通常以类名命名。实现文件使用 `.m` 扩展名，表示其中包含 Objective-C 源代码。接口文件可以使用其他任何扩展名。由于接口文件会被包含到其他源文件中，它通常使用头文件惯用的 `.h` 扩展名。例如，`Rectangle` 类会在 `Rectangle.h` 中声明，在 `Rectangle.m` 中定义。

把对象的接口与实现分开，与面向对象程序的设计理念十分契合。对象是一个自成一体的实体，从外部看几乎可以被视为一个黑盒。一旦确定了某个对象如何与程序中的其他元素交互——也就是声明好了它的接口——你就可以自由地修改它的实现，而不会影响应用程序的其他部分。

类接口的声明以编译器指令 `@interface` 开始，以指令 `@end` 结束。（所有 Objective-C 编译器指令都以“@”开头。）

```objc
@interface ClassName : ItsSuperclass
// 方法和属性声明。
@end
```

声明的第一行给出新类的名称，并将它与超类关联起来。超类决定了新类在继承层次结构中的位置，这一点在[继承](Objects%2C%20Classes%2C%20and%20Messaging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjrfu4dmmzxga)中有讨论。

接下来，在类声明结束之前，会声明该类的方法和属性。可供类对象使用的方法——即_类方法_——名称前面加一个加号：

```
+ alloc;
```

类的实例可以使用的方法——即_实例方法_——则用减号标记：

```objc
- (void)display;
```

虽然这不是常见的做法，但你可以定义一个同名的类方法和实例方法。方法也可以与实例变量同名，这种情况更常见，尤其是当该方法返回的正是该变量的值时。例如，`Circle` 有一个 `radius` 方法，它可能与一个 `radius` 实例变量同名。

方法的返回类型使用标准的 C 类型转换语法来声明：

```objc
- (float)radius;
```

参数类型也以同样的方式声明：

```objc
- (void)setRadius:(float)aRadius;
```

如果没有显式声明返回类型或参数类型，则默认其为方法和消息的默认类型——`id`。前面举例的 `alloc` 方法返回的就是 `id`。

当有多个参数时，参数会声明在方法名中冒号之后的位置。参数会像消息中那样，把方法名拆分成若干部分。例如：

```objc
- (void)setWidth:(float)width height:(float)height;
```

接受可变数量参数的方法，会像声明函数一样，用逗号和省略号来声明这些参数：

```
- makeGroup:group, ...;
```

属性声明的形式为：

```objc
@property (attributes) Type propertyName;
```

属性的详细内容将在[声明的属性](Declared%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomi)中讨论。

任何依赖该类接口的源模块都必须包含接口文件——这包括任何创建该类实例、发送消息以调用该类所声明方法，或者提到该类所声明实例变量的模块。接口通常使用 `#import` 指令来包含：

```objc
#import "Rectangle.h"
```

这个指令与 `#include` 相同，只是它能确保同一个文件不会被包含超过一次。因此它是首选做法，在 Objective-C 相关文档的代码示例中，都用它来代替 `#include`。

为了体现类定义建立在所继承的类的定义之上这一事实，接口文件一开始会导入其超类的接口：

```objc
#import "ItsSuperclass.h"

@interface ClassName : ItsSuperclass
// 方法和属性声明。
@end
```

按照这一约定，每个接口文件都间接地包含了所有被继承的类的接口文件。当一个源模块导入某个类的接口时，它就获得了该类所建立的整个继承层次结构的接口。

请注意，如果存在支持该超类的_预编译头_（precomp），你可能更倾向于导入这个预编译头。

一个接口文件声明了一个类，并且通过导入其超类，隐式地包含了从 `NSObject` 直到其超类的所有被继承类的声明。如果接口中提到了不在这个继承层次中的类，就必须显式导入这些类，或者用 `@class` 指令来声明它们：

```
@class Rectangle, Circle;
```

这个指令只是告诉编译器“Rectangle”和“Circle”是类名，它并不会导入它们的接口文件。

接口文件在对实例变量、返回值和参数进行静态类型声明时，会提到类名。例如，下面这个声明

```objc
- (void)setPrimaryColor:(NSColor *)aColor;
```

就提到了 `NSColor` 类。

因为像这样的声明只是把类名当作类型使用，并不依赖该类接口的任何细节（它的方法和实例变量），所以 `@class` 指令就足以给编译器提供必要的预先提示。不过，当一个类的接口被真正使用时（创建实例、发送消息），就必须导入该类的接口。通常，接口文件用 `@class` 来声明类，而对应的实现文件则导入这些类的接口（因为它需要创建这些类的实例或向它们发送消息）。

`@class` 指令能最大限度地减少编译器和链接器所要处理的代码量，因此是对类名进行前向声明最简单的方式。正因为简单，它避免了导入文件可能带来的问题——那些被导入的文件可能又会导入其他文件。例如，如果一个类声明了另一个类的静态类型实例变量，而这两个类的接口文件又互相导入，那么这两个类都可能无法正确编译。

接口文件的目的是向其他源模块（以及其他程序员）声明这个新类。它包含了他们使用该类所需的信息（程序员们可能还会欣赏一点文档说明）。

- 接口文件告诉使用者该类是如何被纳入继承层次结构的，以及还需要哪些其他类——无论是被继承的，还是仅仅在该类定义中某处被提及的。
- 通过其方法声明列表，接口文件让其他模块知道可以向该类对象及其实例发送哪些消息。每一个可以在类定义之外使用的方法都会在接口文件中声明；仅供类实现内部使用的方法则可以省略。

类的定义在结构上与其声明非常相似。它以 `@implementation` 指令开始，以 `@end` 指令结束。此外，类还可以在 `@implementation` 指令后的花括号中声明实例变量：

```objc
@implementation ClassName
{
    // 实例变量声明。
}
// 方法定义。
@end
```

实例变量常常通过声明的属性来指定（参见[声明的属性](Declared%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomi)）。如果你不声明额外的实例变量，可以省略花括号：

```objc
@implementation ClassName
// 方法定义。
@end
```

类的方法和 C 函数一样，定义在一对花括号内。在花括号之前，它们的声明方式与接口文件中相同，只是不带分号。例如：

```objc
+ (id)alloc {
    ...
}

- (BOOL)isFilled {
    ...
}

- (void)setFilled:(BOOL)flag {
    ...
}
```

接受可变数量参数的方法，处理方式与函数完全一样：

```objc
#import <stdarg.h>

 ...

- getGroup:group, ... {

    va_list ap;
    va_start(ap, group);
    ...
}
```


默认情况下，实例方法的定义可以访问该对象的所有实例变量，它们都在其作用域之内。方法可以直接通过名称引用这些变量。虽然编译器会创建等价于 C 结构体的东西来存储实例变量，但这个结构体的具体形式是隐藏的。你不需要用到任何一个结构体运算符（`.` 或 `->`）来引用对象的数据。例如，下面这个方法定义引用了接收者的 `filled` 实例变量：

```objc
- (void)setFilled:(BOOL)flag
{
    filled = flag;
    ...
}
```

无论是接收对象本身，还是它的 `filled` 实例变量，都没有被声明为这个方法的参数，但这个实例变量仍然落在其作用域之内。这种方法语法上的简化，是编写 Objective-C 代码时一种重要的简写方式。

当实例变量属于某个不是接收者的对象时，就必须通过静态类型，向编译器明确该对象的类型。在引用一个静态类型对象的实例变量时，需要使用结构体指针运算符（`->`）。

举例来说，假设 `Sibling` 类声明了一个静态类型的对象 `twin` 作为实例变量：

```objc
@interface Sibling : NSObject
{
    Sibling *twin;
    int gender;
    struct features *appearance;
}
```

只要这个静态类型对象的实例变量在该类的作用域之内（在这里就是这样，因为 `twin` 的类型正是同一个类），`Sibling` 的方法就可以直接设置这些变量：

```swift
- makeIdenticalTwin
{
    if ( !twin ) {
        twin = [[Sibling alloc] init];
        twin->gender = gender;
        twin->appearance = appearance;
    }
    return twin;
}
```


为了让对象具备隐藏自身数据的能力，编译器会限制实例变量的作用域——也就是限制它们在程序中的可见性。但为了提供灵活性，编译器也允许你显式地将作用域设置为四个级别之一。每个级别都由一个编译器指令标记：

| 指令 | 含义 |
| --- | --- |
| `@private` | 该实例变量只能在声明它的类内部访问。 |
| `@protected` | 该实例变量可以在声明它的类内部访问，也可以在继承它的类内部访问。所有没有显式作用域指令的实例变量都具有 `@protected` 作用域。 |
| `@public` | 该实例变量在任何地方都可以访问。 |
| `@package` | 在现代运行时环境下，一个 `@package` 实例变量在实现该类的可执行映像内部具有 `@public` 作用域，但在该映像外部则表现得像 `@private` 一样。Objective-C 实例变量的 `@package` 作用域类似于 C 变量和函数中的 `private_extern`。任何在该类实现所在映像之外、试图使用该实例变量的代码，都会收到一个链接错误。这个作用域对框架类中的实例变量最为有用，在这类场景中，`@private` 可能过于严格，而 `@protected` 或 `@public` 又过于宽松。 |

图 2-1 展示了各个作用域级别。

__图 2-1__  实例变量的作用域（未展示 `@package` 作用域）

!

作用域指令适用于它之后列出的所有实例变量，直到下一个指令或列表末尾为止。在下面的例子中，`age` 和 `evaluation` 实例变量是私有的；`name`、`job` 和 `wage` 是受保护的；`boss` 是公开的。

```objc
@interface Worker : NSObject
{
    char *name;
@private
    int age;
    char *evaluation;
@protected
    id job;
    float wage;
@public
    id boss;
}
```

默认情况下，所有未标记的实例变量（比如上面的 `name`）都是 `@protected` 的。

无论以何种方式标记，一个类所声明的所有实例变量都在该类定义的作用域之内。例如，一个声明了 `job` 实例变量的类，比如上面展示的 `Worker` 类，可以在方法定义中引用它：

```
- promoteTo:newPosition
{
    id old = job;
    job = newPosition;
    return old;
}
```

显然，如果一个类连自己的实例变量都无法访问，那这些实例变量就毫无用处了。

通常，一个类也可以访问它所继承的实例变量。引用某个实例变量的能力，通常会随着该变量一起被继承。类拥有其整个数据结构的访问权限，这是合乎情理的——尤其是如果你把类的定义仅仅看作是对其所继承的类的一种细化。前面举例的 `promoteTo:` 方法，同样可以定义在任何继承了 `Worker` 类 `job` 实例变量的类中。

不过，出于以下原因，你可能会希望限制继承类直接访问某个实例变量：

- 一旦子类访问了某个继承来的实例变量，声明该变量的类就与实现的这一部分绑定在一起了。在后续版本中，它就不能再随意去掉这个变量或改变它的作用，否则可能会不小心破坏子类的功能。
- 此外，如果子类访问了某个继承来的实例变量并修改了它的值，可能会不小心给声明该变量的类引入 bug，尤其是当这个变量涉及类内部的某些依赖关系时。

要把一个实例变量的作用域限制在声明它的类内部，你必须把它标记为 `@private`。标记为 `@private` 的实例变量，子类只能通过调用公开的存取方法（如果存在的话）来使用它。

在另一个极端，把一个变量标记为 `@public`，会让它在任何地方都能被普遍访问，甚至在继承或声明该变量的类定义之外也是如此。通常，要获取存储在实例变量中的信息，其他对象必须发送消息来请求它。然而，公开的实例变量可以在任何地方被访问，就像访问 C 结构体中的字段一样。例如：

```swift
Worker *ceo = [[Worker alloc] init];
ceo->boss = nil;
```

请注意，该对象必须是静态类型的。

把实例变量标记为 `@public`，会破坏对象隐藏自身数据的能力。这有悖于面向对象编程的一项基本原则——把数据封装在对象内部，使其不受外界窥视和意外错误的影响。因此，除非在特殊情况下，否则应当避免使用公开的实例变量。

Objective-C 提供了两个可以在方法定义中使用的术语，用来指代执行该方法的对象——`self` 和 `super`。

举例来说，假设你定义了一个 `reposition` 方法，需要改变它所作用的对象的坐标。它可以调用 `setOrigin::` 方法来完成这一改变。它所要做的，就是向接收 `reposition` 消息的同一个对象发送 `setOrigin::` 消息。在编写 reposition 代码时，你可以用 `self` 或 `super` 来指代那个对象。`reposition` 方法可以写成这样：

```
- reposition
{
    ...
    [self setOrigin:someX :someY];
    ...
}
```

也可以写成这样：

```
- reposition
{
    ...
    [super setOrigin:someX :someY];
    ...
}
```

这里，`self` 和 `super` 都指代接收 `reposition` 消息的对象，无论那具体是什么对象。然而，这两个术语有很大的不同。`self` 是消息传递机制传给每个方法的隐藏参数之一；它是一个局部变量，可以在方法实现中自由使用，就像使用实例变量的名字一样。`super` 则是一个只有在消息表达式中作为接收者时才能替代 `self` 的术语。作为接收者，这两个术语的主要区别在于它们对消息传递过程的影响方式：

- `self` 会按通常的方式查找方法实现，从接收对象所属类的_分派表_开始查找。在上面的例子中，它会从接收 reposition 消息的对象所属的类开始查找。
- `super` 是一个标志，告诉编译器要在一个完全不同的地方查找方法实现。它会从定义了 `super` 所在方法的那个类的超类开始查找。在上面的例子中，它会从定义 reposition 方法的那个类的超类开始查找。

无论何时向 `super` 发送消息，编译器都会用另一个消息传递例程来替代 `objc_msgSend` 函数。这个替代例程会直接查找定义类的超类——也就是向 `super` 发送消息的那个类的超类——而不是接收消息的对象所属的类。

当涉及三个类组成的层次结构时，`self` 和 `super` 之间的区别就变得清晰了。举例来说，假设我们创建了一个属于 `Low` 类的对象。`Low` 的超类是 `Mid`；`Mid` 的超类是 `High`。这三个类都定义了一个叫做 `negotiate` 的方法，每个类都按自己的方式使用它。此外，`Mid` 还定义了一个雄心勃勃的方法，叫做 `makeLastingPeace`，它本身就会调用 `negotiate` 方法。这些类和方法如图 2-2 所示。

__图 2-2__  High、Mid 和 Low 的层次结构

!

假设 `makeLastingPeace`（在 `Mid` 类中）的实现使用 `self` 来指明要向哪个对象发送 `negotiate` 消息：

```
- makeLastingPeace
{
    [self negotiate];
    ...
}
```

当向一个 `Low` 对象发送消息以执行 `makeLastingPeace` 方法时，`makeLastingPeace` 会向同一个 `Low` 对象发送 `negotiate` 消息。消息传递机制会找到 `Low` 中定义的那个版本的 `negotiate`，因为 `Low` 是 `self` 所属的类。

然而，如果 `makeLastingPeace` 的实现改用 `super` 作为接收者，

```
- makeLastingPeace
{
    [super negotiate];
    ...
}
```

消息传递机制就会找到 `High` 中定义的那个版本的 `negotiate`。它会忽略接收 `makeLastingPeace` 消息的对象所属的类（`Low`），直接跳到 `Mid` 的超类，因为 `Mid` 正是定义 `makeLastingPeace` 的类。这两种实现都不会找到 `negotiate` 在 `Mid` 中的版本。

正如这个例子所展示的，`super` 提供了一种绕过某个覆盖了另一个方法的方法的方式。在这里，`super` 的使用使得 `makeLastingPeace` 得以绕过 `Mid` 版本的 `negotiate`——而这个版本原本重新定义了 `High` 版本的方法。

正如刚才所描述的那样，无法访问到 `Mid` 版本的 `negotiate`，看起来可能像是一个缺陷，但在这种情况下，这是故意为之的：

- `Low` 类的作者故意重写了 `Mid` 版本的 `negotiate`，好让 `Low`（及其子类）的实例调用这个重新定义的方法版本。`Low` 的设计者不希望 `Low` 的对象执行继承来的方法。
- `Mid` 中 `makeLastingPeace` 方法的作者，在第二种实现中向 `super` 发送 `negotiate` 消息时，是故意跳过 `Mid` 版本的 `negotiate`（以及任何像 `Low` 这样继承自 `Mid` 的类中可能定义的版本），去执行 `High` 类中定义的版本。这第二个版本的 `makeLastingPeace` 的设计者，就是想使用 `High` 版本的 `negotiate`，而不是别的版本。

`Mid` 版本的 `negotiate` 仍然是可以使用的，只不过需要直接向 `Mid` 的实例发送消息才行。

向 `super` 发送消息，使得方法的实现可以分布在多个类中。你可以重写一个已有的方法来修改它或为它添加内容，同时仍然把原来的方法纳入这个修改后的版本中：

```
- negotiate
{
    ...
    return [super negotiate];
}
```

对于某些任务，继承层次结构中的每个类都可以实现一个方法，完成其中一部分工作，再把消息传给 `super` 去完成剩余部分。`init` 方法用于初始化一个新分配的实例，就是按这种方式设计的。每个 `init` 方法都负责初始化其所在类中定义的实例变量。但在此之前，它会先向 `super` 发送一条 `init` 消息，让它所继承的那些类初始化它们各自的实例变量。每个版本的 `init` 都遵循这一流程，因此各个类会按照继承顺序来初始化它们的实例变量：

```objc
- (id)init
{
    self = [super init];
    if (self) {
        ...
    }
}
```

还可以把核心功能集中定义在超类中的某一个方法里，然后让子类通过向 `super` 发送消息来纳入这个方法。例如，每一个创建实例的类方法都必须为新对象分配存储空间，并把它的 `isa` 变量初始化为该类的结构体。分配存储空间的工作通常交给 `NSObject` 类中定义的 `alloc` 和 `allocWithZone:` 方法。如果另一个类重写了这些方法（这种情况很少见），它仍然可以通过向 `super` 发送消息来获得这个基本功能。

`super` 只是给编译器的一个标志，告诉它从哪里开始查找要执行的方法；它只能用作消息的接收者。但 `self` 是一个变量名，可以以多种方式使用，甚至可以被赋予新的值。

在定义类方法时，有一种常见的倾向就是这样做。类方法通常关注的不是类对象本身，而是该类的实例。例如，许多类方法会同时完成实例的分配和初始化，往往还会同时设置实例变量的值。在这样的方法中，你可能会忍不住向新分配的实例发送消息，并像在实例方法中那样把这个实例叫做 `self`。但这样做是错误的。`self` 和 `super` 都指代接收对象——也就是接到消息、被告知去执行该方法的那个对象。在实例方法内部，`self` 指代该实例；但在类方法内部，`self` 指代的是类对象。下面是一个不应该这样做的例子：

```objc
+ (Rectangle *)rectangleOfColor:(NSColor *) color
{
    self = [[Rectangle alloc] init]; // 错误
    [self setColor:color];
    return self;
}
```

为了避免混淆，在类方法内部引用一个实例时，最好使用一个不是 `self` 的变量：

```objc
+ (id)rectangleOfColor:(NSColor *)color
{
    id newInstance = [[Rectangle alloc] init]; // 正确
    [newInstance setColor:color];
    return newInstance;
}
```

实际上，在类方法中，与其向类本身发送 `alloc` 消息，不如向 `self` 发送 `alloc` 消息，这样往往更好。这样一来，如果这个类被派生出子类，并且 `rectangleOfColor:` 消息是由某个子类接收的，那么返回的实例类型就会与这个子类一致（例如，`NSArray` 的 `array` 方法就被 `NSMutableArray` 继承了）。

```objc
+ (id)rectangleOfColor:(NSColor *)color
{
    id newInstance = [[self alloc] init]; // 更佳
    [newInstance setColor:color];
    return newInstance;
}
```

关于实现初始化方法及相关方法的更多信息，请参见[创建和初始化对象](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/EncapsulatingData/EncapsulatingData.html#//apple_ref/doc/uid/TP40011210-CH5)。

[下一页](Protocols.md)[上一页](Objects%2C%20Classes%2C%20and%20Messaging.md)

