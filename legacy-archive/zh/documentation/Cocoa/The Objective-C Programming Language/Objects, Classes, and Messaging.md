---
title: Objective-C 编程语言
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocObjectsClasses.html
archived_at: '2026-07-15T07:17:30.409991Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 编程语言](Introduction.md)


[下一页](Defining%20a%20Class.md)[上一页](Introduction.md)

# 对象、类与消息传递

本章描述 Objective-C 语言所使用和实现的对象、类与消息传递的基本原理，同时介绍 Objective-C 运行时（runtime）。

Objective-C 语言尽可能把决策从 _编译期_ 和 _链接期_ 推迟到 _运行期_。只要有可能，它就会动态地执行诸如创建对象、决定要调用哪个方法之类的操作。因此，这门语言不仅需要一个编译器，还需要一套运行时系统来执行编译后的代码。运行时系统就像 Objective-C 语言的一种操作系统，正是它让这门语言得以运作。不过通常你并不需要直接与运行时打交道。若想进一步了解运行时提供的功能，请参阅 _[Objective-C 运行时编程指南](../Objective-C%20Runtime%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danby)_。

正如其名称所示，面向对象的程序是围绕 _对象（object）_ 构建的。对象把数据和能够使用或影响该数据的特定操作关联在一起。Objective-C 提供了一种数据类型，用来标识对象变量，而不必指定该对象所属的具体类。

对象把数据和能够使用或影响该数据的特定操作关联在一起。在 Objective-C 中，这些操作被称为对象的 _方法（method）_；它们所作用的数据则是对象的 _实例变量（instance variable）_（在其他环境中可能称为 _ivar_ 或 _成员变量_）。从本质上说，对象把一个数据结构（实例变量）和一组过程（方法）捆绑成一个自成一体的编程单元。

在 Objective-C 中，对象的实例变量属于对象内部；一般来说，你只能通过对象的方法来访问其状态（你可以使用作用域指令来指定子类或其他对象是否可以直接访问实例变量，参见 [实例变量的作用域](Defining%20a%20Class.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjsfu4dqnbwha)）。要让别人了解某个对象的某些情况，就必须有一个方法来提供这些信息。例如，一个矩形会有一些方法来揭示它的尺寸和位置。

此外，一个对象只能看到为它设计的方法；它不可能误执行为其他类型对象所设计的方法。正如 C 函数会保护自己的局部变量、使程序的其余部分无法访问一样，对象也会把自己的实例变量和方法实现都隐藏起来。

在 Objective-C 中，对象标识符属于一种独特的数据类型：`id`。这种类型是任何一种对象（无论其所属类别）的通用类型，既可以用于类的实例，也可以用于类对象本身。

```objc
id anObject;
```

对于 Objective-C 面向对象的构造（例如方法返回值），`id` 取代 `int` 成为默认的数据类型。（对于纯 C 的构造，例如函数返回值，`int` 仍然是默认类型。）

关键字 `nil` 被定义为一个空对象，即值为 `0` 的 `id`。`id`、`nil` 以及 Objective-C 的其他基本类型都定义在头文件 `objc/objc.h` 中。

`id` 被定义为指向对象数据结构的指针：

```c
typedef struct objc_object {
    Class isa;
} *id;
```

因此，每个对象都有一个 `isa` 变量，用来告诉自己它是哪个类的实例。由于 `Class` 类型本身被定义为一个指针：

```c
typedef struct objc_class *Class;
```

因此 `isa` 变量常被称为“`isa` 指针”。

`id` 类型完全不带任何限制。就其本身而言，除了表明这是一个对象之外，它不会提供任何关于该对象的信息。而在某个时刻，程序通常需要找出所包含对象的更具体的信息。由于 `id` 这个类型标识符无法向编译器提供这种具体信息，因此每个对象都必须能够在运行时自行提供这些信息。

`isa` 这个实例变量标识了对象的 _类（class）_——即它是哪种对象。具有相同行为（方法）和相同种类数据（实例变量）的对象属于同一个类的成员。

因此，对象在运行时是 _动态类型（dynamically typed）_ 的。运行时系统只需在需要时向对象询问，就能找出该对象所属的确切类。（想进一步了解运行时，请参阅 _[Objective-C 运行时编程指南](../Objective-C%20Runtime%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danby)_。）Objective-C 中的动态类型是动态绑定的基础，后文将讨论动态绑定。

`isa` 变量还使对象能够进行[内省（introspection）](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Introspection.html#//apple_ref/doc/uid/TP40008195-CH24)——即了解自身（或其他对象）的情况。编译器会把类定义的相关信息记录在数据结构中，供运行时系统使用。运行时系统的函数会利用 `isa` 在运行时查找这些信息。借助运行时系统，你可以例如判断一个对象是否实现了某个特定方法，或者查出它的超类名称。

对象所属的类将在 [类](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjrfu4dmmzshe) 一节中有更详细的讨论。

此外，你还可以在源代码中用类名对对象进行静态类型标注，从而把该对象的类信息告知编译器。类本身也是一种特殊的对象，类名可以充当类型名。参见 [类类型](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjrfu4dmnrtgi) 和 [启用静态行为](Enabling%20Static%20Behavior.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjwfvjvomi)。

在任何程序中，确保对象在不再需要时被释放都很重要——否则应用程序的内存占用会变得比实际需要更大。同样重要的是，要确保不会在对象仍在使用时就将其释放。

Objective-C 提供了三种内存管理机制，帮助你实现这些目标：

- _自动引用计数_（ARC），由编译器负责推断对象的生命周期。
- _手动引用计数_（MRC，有时也称为 MRR，即“手动 retain/release”），由你自己最终负责确定对象的生命周期。

  手动引用计数在 _[高级内存管理编程指南](../Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytc2i)_ 中有详细描述。
- _垃圾回收_，把确定对象生命周期的责任交给一个自动的“回收器”。

  垃圾回收在 _[垃圾回收编程指南](../Garbage%20Collection%20Programming%20Guide/Introduction%20to%20Garbage%20Collection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimzr)_ 中有详细描述。（iOS 不支持该机制——你无法通过 iOS Dev Center 访问这份文档。）

本节说明发送消息的语法，包括如何嵌套消息表达式，还会讨论对象实例变量的作用域（即“可见性”），以及多态和动态绑定的概念。

要让一个对象去做某件事，你需要向它发送一条 _消息_，告诉它去执行某个方法。在 Objective-C 中，_消息表达式_ 用方括号括起来：

```objc
[receiver message]
```

_接收者（receiver）_ 是一个对象，消息则告诉它要做什么。在源代码中，消息就是一个方法的名称以及传给它的所有参数。发送消息时，运行时系统会从接收者的方法集合中挑选出合适的方法并加以调用。

例如，下面这条消息告诉 `myRectangle` 对象执行它的 `display` 方法，使这个矩形显示自身：

```objc
[myRectangle display];
```

和 C 语言中所有语句一样，消息后面要跟一个“`;`”。

由于消息中的方法名起到“选中”某个方法实现的作用，消息中的方法名常被称为 _选择器（selector）_。

方法还可以带参数，有时也称为 _实参（argument）_。带单个参数的消息会在方法名后加上一个冒号（`:`），并紧跟着放上参数：

```objc
[myRectangle setWidth:20.0];
```

对于带多个参数的方法，Objective-C 的方法名会与参数交错排列，使方法名能自然地描述该方法所期望的参数。下面这条虚构的消息告诉 `myRectangle` 对象把它的原点设置为坐标 (30.0, 50.0)：

```objc
[myRectangle setOriginX: 30.0 y: 50.0]; // 这是一个多参数的
                                        // 良好示例
```

选择器名称包括名称的所有部分，包括冒号，因此上面例子中的选择器名为 `setOriginX:y:`。它有两个冒号，因为它接受两个参数。不过，选择器名称不包含返回类型或参数类型之类的其他内容。

原则上，`Rectangle` 类也可以改为实现一个 `setOrigin::` 方法，不为第二个参数加标签，调用方式如下：

```objc
[myRectangle setOrigin:30.0 :50.0]; // 这是一个多参数的糟糕示例
```

虽然这在语法上是合法的，但 `setOrigin::` 并没有把方法名与参数交错排列。这样一来，第二个参数实际上就没有标签，代码的读者也很难判断该方法参数的种类或用途。

带可变数量参数的方法也是可行的，虽然这种情况比较少见。额外的参数在方法名结束后用逗号分隔。（与冒号不同，逗号不被视为名称的一部分。）在下面的例子中，这个虚构的 `makeGroup:` 方法接受一个必需参数（`group`）和三个可选参数：

```objc
[receiver makeGroup:group, memberOne, memberTwo, memberThree];
```

和标准 C 函数一样，方法也可以返回值。下面的例子中，如果 `myRectangle` 被绘制成实心矩形，就把变量 `isFilled` 设为 `YES`；如果只以轮廓形式绘制，则设为 `NO`。

```objc
BOOL isFilled;
isFilled = [myRectangle isFilled];
```

注意，变量和方法可以同名。

一个消息表达式可以嵌套在另一个消息表达式内部。下面这个例子把一个矩形的颜色设置为另一个矩形的颜色：

```objc
[myRectangle setPrimaryColor:[otherRect primaryColor]];
```

Objective-C 还提供了一个点（`.`）运算符，为调用对象的存取方法提供了一种简洁便利的语法。点运算符常与声明属性特性配合使用（参见 [声明属性](Declared%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomi)），并在 [点语法](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjrfvjvomjx) 一节中有详细描述。

在 Objective-C 中，向 `nil` 发送消息是合法的——它在运行时只是不产生任何效果。Cocoa 中有若干模式利用了这一特性。向 `nil` 发送消息所返回的值也可能是有效的：

- 如果方法返回一个对象，那么向 `nil` 发送消息会返回 `0`（`nil`）。例如：

```objc
Person *motherInLaw = [[aPerson spouse] mother];
```

  如果这里的 `spouse` 对象是 `nil`，那么 `mother` 就会被发送给 `nil`，方法返回 `nil`。
- 如果方法返回任意指针类型、任意大小不超过 `sizeof(void*)` 的整数标量、`float`、`double`、`long double` 或 `long long`，那么向 `nil` 发送消息会返回 `0`。
- 如果方法按照 _[OS X ABI 函数调用指南](../../Developer%20Tools/OS%20X%20ABI%20Function%20Call%20Guide/Introduction%20to%20OS%20X%20ABI%20Function%20Call%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkmrr)_ 中定义的方式，返回一个通过寄存器传递的 `struct`，那么向 `nil` 发送消息会让该 `struct` 中的每个字段都返回 `0.0`。其他 `struct` 数据类型不会被填充为零。
- 如果方法返回的既非上述值类型，那么向 `nil` 发送消息的返回值是未定义的。

下面这段代码演示了向 `nil` 发送消息的一种合法用法。

```objc
id anObjectMaybeNil = nil;

// 这是合法的
if ([anObjectMaybeNil methodThatReturnsADouble] == 0.0)
{
    // 实现继续...
}
```


方法可以自动访问接收对象的实例变量，你不需要把这些变量作为参数传给方法。例如，前面演示的 `primaryColor` 方法不接受任何参数，却能找到 `otherRect` 的主色并将其返回。每个方法都默认拥有接收者及其实例变量，无需把它们声明为参数。

这一约定简化了 Objective-C 源代码，也符合面向对象程序员看待对象和消息的方式。消息被发送给接收者，就像信件被投递到你家一样。消息参数把外部的信息带给接收者，而不需要把接收者本身带来带去。

方法只能自动访问接收者自己的实例变量。如果它需要了解存储在另一个对象中的某个变量的信息，就必须向该对象发送消息，请求它揭示该变量的内容。前面提到的 `primaryColor` 和 `isFilled` 方法正是用于这个目的。

关于引用实例变量的更多信息，参见 [定义类](Defining%20a%20Class.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjsfvjvomi)。

正如前面的例子所示，Objective-C 中的消息出现在与标准 C 中函数调用相同的语法位置上。但由于方法“属于”某个对象，消息的行为方式与函数调用并不相同。

具体来说，一个对象只能被为它定义的方法所操作。它不会把这些方法和为其他种类对象定义的方法相混淆，即便另一个对象有一个同名方法也是如此。因此，两个对象可以对同一条消息做出不同的响应。例如，每种收到 `display` 消息的对象都可以用自己独特的方式来显示自己。`Circle` 和 `Rectangle` 在收到相同的“跟踪光标”指令时会有不同的响应。

这一特性被称为 _多态（polymorphism）_，在面向对象程序的设计中扮演着重要角色。多态与动态绑定相结合，使你能够编写适用于任意数量不同种类对象的代码，而不必在编写代码时就确定这些对象具体是什么类型。它们甚至可能是日后由其他项目上的其他程序员开发出来的对象。如果你编写的代码向一个 `id` 变量发送 `display` 消息，那么任何拥有 `display` 方法的对象都可能成为接收者。

函数调用和消息之间一个关键的区别在于：函数及其参数在编译后的代码中是绑定在一起的，而消息和接收对象要等到程序运行、消息真正发送时才会结合在一起。因此，响应某条消息所调用的确切方法只能在运行时确定，而不是在代码编译时确定。

当消息被发送时，一个运行时消息传递例程会查看接收者以及消息中所指定的方法。它会定位接收者中与该名称匹配的方法实现，“调用”这个方法，并向它传递一个指向接收者实例变量的指针。（关于这一例程的更多信息，参见 _[Objective-C 运行时编程指南](../Objective-C%20Runtime%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danby)_ 中的 [消息传递](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtHowMessagingWorks.html#//apple_ref/doc/uid/TP40008048-CH104)。）

方法与消息之间的这种 _动态绑定（dynamic binding）_ 与多态相辅相成，赋予了面向对象编程极大的灵活性和能力。由于每个对象都可以拥有自己的方法版本，同一条 Objective-C 语句可以产生各种不同的结果——变化的不是消息本身，而是接收该消息的对象。接收者可以在程序运行过程中才决定；这种选择可以取决于诸如用户操作之类的因素。

例如，在执行基于 Application Kit（_AppKit_）的代码时，用户决定哪些对象接收来自剪切、拷贝、粘贴等菜单命令的消息。消息会发给当前控制着选区的那个对象。一个显示文本的对象对 `copy` 消息的反应，会与一个显示扫描图像的对象不同。一个表示一组形状的对象对 `copy` 消息的响应，也会与 `Rectangle` 不同。由于消息要到运行时才会选定方法（换个角度说，方法与消息的绑定要到运行时才会发生），这些行为上的差异被局限在方法本身之内。发送消息的代码不必关心这些差异，甚至不必一一列举各种可能性。一个应用程序中的各个对象都可以用自己的方式响应 `copy` 消息。

Objective-C 把动态绑定又向前推进了一步，甚至允许所发送的消息本身（即方法选择器）也是一个在运行时才确定的变量。这一机制在 _[Objective-C 运行时编程指南](../Objective-C%20Runtime%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danby)_ 的 [消息传递](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtHowMessagingWorks.html#//apple_ref/doc/uid/TP40008048-CH104) 一节中有讨论。

你可以使用动态方法解析，在运行时提供类方法和实例方法的实现。更多细节参见 _[Objective-C 运行时编程指南](../Objective-C%20Runtime%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danby)_ 中的 [动态方法解析](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtDynamicResolution.html#//apple_ref/doc/uid/TP40008048-CH102)。

Objective-C 提供了一个点（`.`）运算符，作为方括号表示法（`[]`）之外调用[存取方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AccessorMethod.html#//apple_ref/doc/uid/TP40008195-CH2)的另一种方式。点语法沿用了访问 C 结构体元素时的相同模式：

```objc
myInstance.value = 10;
printf("myInstance value: %d", myInstance.value);
```

然而，当用于对象时，点语法起到的是“语法糖”的作用——编译器会把它转换成对某个存取方法的调用。点语法 _并不_ 直接获取或设置实例变量。上面的代码示例与下面的代码完全等价：

```objc
[myInstance setValue:10];
printf("myInstance value: %d", [myInstance value]);
```

由此可以推出，如果你想通过存取方法访问对象自己的实例变量，就必须显式地调用 `self`，例如：

```objc
self.age = 10;
```

或者等价地写成：

```objc
[self setAge:10];
```

如果不使用 `self.`，你访问的就是实例变量本身。在下面的例子中，`age` 的 set 存取方法 _不会_ 被调用：

```objc
age = 10;
```

如果在属性遍历过程中遇到 `nil` 值，其结果和向 `nil` 发送等价消息是一样的。例如，下面这几对写法都是等价的：

```objc
// 路径中的每个成员都是一个对象。
x = person.address.street.name;
x = [[[person address] street] name];

// 该路径中包含一个 C 结构体。
// 如果 window 为 nil，或者 -contentView 返回 nil，这里会崩溃。
y = window.contentView.bounds.origin.y;
y = [[window contentView] bounds].origin.y;

// 使用 setter 的示例。
person.address.street.name = @"Oxford Road";
[[[person address] street] setName: @"Oxford Road"];
```


一个面向对象的程序通常由多种多样的对象构建而成。一个基于 Cocoa 框架的程序可能会用到 `NSMatrix` 对象、`NSWindow` 对象、`NSDictionary` 对象、`NSFont` 对象、`NSText` 对象等等。程序常常会用到多个同种或同一个类的对象——例如若干个 `NSArray` 对象或 `NSWindow` 对象。

在 Objective-C 中，你通过定义类来定义对象。类定义是一种对象的原型：它声明了成为该类每个成员一部分的实例变量，并定义了该类所有对象都能使用的一组方法。

编译器为每个类只创建一个可访问的对象，即一个知道如何构建属于该类的新对象的 _类对象（class object）_。（正因为如此，它在传统上也被称为 _工厂对象（factory object）_。）类对象是这个类经过编译后的版本；它所构建出来的对象则是该类的 _实例（instance）_。程序中真正完成主要工作的对象，就是由类对象在运行时创建出来的实例。

同一个类的所有实例都拥有同一套方法，也都拥有从同一个模子里刻出来的一套实例变量。每个对象都有自己的实例变量，但方法是共享的。

按照惯例，类名以大写字母开头（例如 `Rectangle`）；实例的名称通常以小写字母开头（例如 `myRectangle`）。

类定义是可累加的：你定义的每个新类都基于另一个类，并从中继承方法和实例变量。新类只是在继承来的基础上加以补充或修改，不需要重复被继承的代码。

_继承（inheritance）_ 把所有类连接成一棵有单一根类的层级树。在编写基于 Foundation 框架的代码时，这个根类通常是 `NSObject`。每个类（根类除外）都有一个离根更近一步的 _超类（superclass）_，而任何类（包括根类）都可以作为任意数量、离根更远一步的 _子类（subclass）_ 的超类。图 1-1 展示了一个绘图程序中部分类的层级关系。

__图 1-1__  一个绘图程序中的部分类

!

图 1-1 显示了 `Square` 类是 `Rectangle` 类的子类，`Rectangle` 类是 `Shape` 的子类，`Shape` 是 `Graphic` 的子类，而 `Graphic` 又是 `NSObject` 的子类。继承是累加的，所以一个 `Square` 对象既拥有为 `Rectangle`、`Shape`、`Graphic` 和 `NSObject` 定义的方法和实例变量，也拥有专门为 `Square` 定义的方法和实例变量。这只是说明，一个 `Square` 类型的对象不仅仅是一个正方形，它同时也是一个矩形、一个形状、一个图形，还是一个 `NSObject` 类型的对象。

因此，除 `NSObject` 之外的每个类都可以看作是另一个类的特化或改造。每一个后续的子类都会进一步修改所继承内容的累加总和。`Square` 类只定义了把矩形变成正方形所需的最少内容。

当你定义一个类时，你通过声明其超类把它连接到层级结构中；你创建的每个类都必须是另一个类的子类（除非你定义了一个新的根类）。可供选择的超类有很多。Cocoa 包含 `NSObject` 类，以及若干个框架，这些框架中定义了 250 多个额外的类。有些类你可以拿来就用，原样纳入你的程序；另一些你可能需要通过派生子类来按自己的需求进行改造。

有些框架类几乎定义了你所需要的一切，只把某些具体细节留给子类去实现。这样，你只需编写少量代码，重用框架程序员已经完成的工作，就能创建出非常精巧的对象。

`NSObject` 是一个根类，因此没有超类。它定义了 Objective-C 对象及对象间交互的基本框架，赋予继承自它的类及其实例作为对象行事、并与运行时系统协作的能力。

即使一个类不需要从另一个类继承任何特殊行为，也应该让它成为 `NSObject` 类的子类。该类的实例至少必须具备在运行时表现得像 Objective-C 对象的能力。从 `NSObject` 类继承这种能力，要比在新的类定义中重新发明它简单得多，也可靠得多。

当一个类对象创建一个新实例时，这个新对象不仅包含为其所属类定义的实例变量，还包含为其超类、以及超类的超类一路定义下来直到根类的所有实例变量。因此，定义在 `NSObject` 类中的 `isa` 实例变量会成为每个对象的一部分。`isa` 把每个对象和它所属的类连接起来。

图 1-2 展示了某个 `Rectangle` 类具体实现中可能定义的一些实例变量，以及它们各自的来源。请注意，使对象成为矩形的那些变量，是叠加在使它成为形状的那些变量之上的；而使它成为形状的那些变量，又是叠加在使它成为图形的那些变量之上的，依此类推。

__图 1-2__  Rectangle 的实例变量

!

一个类不一定非要声明实例变量。如果它根本不需要任何实例变量，它完全可以只定义新方法，并依赖于它继承来的实例变量。例如，`Square` 可能不会声明任何属于自己的新实例变量。

一个对象不仅能访问为其所属类定义的方法，还能访问为其超类、超类的超类，一路到层级根部所定义的方法。例如，一个 `Square` 对象既可以使用定义在 `Rectangle`、`Shape`、`Graphic` 和 `NSObject` 类中的方法，也可以使用定义在它自己类中的方法。

因此，你在程序中定义的任何新类，都可以利用层级结构中位于它之上的所有类所编写的代码。这种继承是面向对象编程的一大好处。当你使用 Cocoa 提供的某个面向对象框架时，你的程序可以利用编写在框架类中的基本功能，你只需添加针对你应用程序定制标准功能的代码。

类对象同样从层级结构中位于它们之上的类那里继承。但由于类对象没有实例变量（只有实例才有），它们只继承方法。

继承有一个很有用的例外：当你定义一个新类时，可以实现一个与层级结构中更上层某个类所定义的方法同名的新方法。这个新方法会覆盖原来的方法：新类的实例会执行新方法而不是原来的方法，新类的子类也会继承新方法而不是原来的方法。

例如，`Graphic` 定义了一个 `display` 方法，而 `Rectangle` 通过定义自己的 `display` 版本覆盖了它。`Graphic` 的这个方法对所有继承自 `Graphic` 类的对象都可用——但 `Rectangle` 对象除外，它们会执行 `Rectangle` 版本的 `display`。

虽然覆盖一个方法会阻止原始版本被继承，但新类中定义的其他方法仍可以绕过被重新定义的方法，找到原始版本（参见 [向 self 和 super 发送消息](Defining%20a%20Class.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjsfu4dsnrwga)了解具体做法）。

一个被重新定义的方法也可以把它所覆盖的那个方法本身纳入进来。这样一来，新方法只是对被覆盖的方法加以细化或修改，而不是彻底取代它。当层级结构中的若干个类都定义了同一个方法，而每个新版本都把它所覆盖的版本纳入其中时，这个方法的实现实际上就分布在所有这些类当中。

虽然子类可以覆盖继承来的方法，但不能覆盖继承来的实例变量。因为一个对象会为它继承的每个实例变量分配内存，所以你不能通过声明一个同名的新变量来覆盖一个继承来的变量。如果你这样做，编译器会报错。

有些类的设计目的只是、或主要是让其他类去继承。这些 _抽象类（abstract class）_ 把可供若干个子类使用的方法和实例变量归纳到一个公共定义中。抽象类本身通常是不完整的，但它包含了有用的代码，能减轻其子类的实现负担。（由于抽象类必须要有子类才有意义，它们有时也被称为 _抽象超类_。）

和其他一些语言不同，Objective-C 没有把类标记为抽象类的语法，也不会阻止你创建一个抽象类的实例。

`NSObject` 类是 Cocoa 中抽象类的典型例子。你永远不会在应用程序中直接使用 `NSObject` 类的实例——那样做没有任何意义；它只是一个什么特定的事都做不了的通用对象。

而 `NSView` 类则是另一个抽象类的例子，你偶尔可能会直接使用它的实例。

抽象类通常包含帮助定义应用程序结构的代码。当你为这些类创建子类时，你新类的实例能毫不费力地融入应用程序的结构，并自动与其他对象协同工作。

类定义是对一种对象的规格说明。类实际上定义了一种数据类型，这种类型不仅基于该类所定义的数据结构（实例变量），也基于其定义中所包含的行为（方法）。

类名可以出现在源代码中任何 C 语言允许类型说明符出现的地方——例如，作为 `sizeof` 运算符的参数：

```objc
int i = sizeof(Rectangle);
```


你可以用类名代替 `id` 来指定对象的类型：

```objc
Rectangle *myRectangle;
```

由于这种声明对象类型的方式向编译器提供了该对象所属种类的信息，因此被称为 _静态类型（static typing）_。正如 `id` 实际上是一个指针一样，静态类型的对象也是指向某个类的指针。对象始终是通过指针来确定类型的：静态类型让这个指针变得显式，而 `id` 则把它隐藏了起来。

静态类型让编译器能够做一些类型检查——例如，如果某个对象可能收到一个它似乎无法响应的消息，编译器会给出警告——并放宽某些适用于泛型 `id` 类型对象的限制。此外，它还能让你的意图对阅读源代码的其他人来说更清楚。不过，它并不会破坏动态绑定，也不会改变接收者的类在运行时被动态确定这一事实。

一个对象既可以被静态类型标注为它自己所属的类，也可以标注为它所继承的任何类。例如，由于继承关系使 `Rectangle` 对象也是一种 `Graphic` 对象（如 [图 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjrfu4dmnbqgu) 中所示的示例层级结构所示），一个 `Rectangle` 实例可以被静态类型标注为 `Graphic` 类：

```objc
Graphic *myRectangle;
```

之所以能够对超类做静态类型标注，是因为一个 `Rectangle` 对象本身就是一个 `Graphic` 对象。而且它不止于此，因为它还拥有 `Shape` 和 `Rectangle` 对象的实例变量和方法能力，但它终究还是一个 `Graphic` 对象。就类型检查而言，按照这里所描述的声明，编译器会认为 `myRectangle` 属于 `Graphic` 类型。然而在运行时，如果 `myRectangle` 对象是作为 `Rectangle` 的实例被分配和初始化的，它就会被当作 `Rectangle` 对象来对待。

关于静态类型及其好处的更多信息，参见 [启用静态行为](Enabling%20Static%20Behavior.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjwfvjvomi)。

实例可以在运行时揭示自己的类型。定义在 `NSObject` 类中的 `isMemberOfClass:` 方法可以检查接收者是否是某个特定类的实例：

```objc
if ( [anObject isMemberOfClass:someClass] )
    ...
```

同样定义在 `NSObject` 类中的 `isKindOfClass:` 方法则更笼统地检查接收者是否继承自某个特定类或是其成员（即该类是否在它的继承路径中）：

```objc
if ( [anObject isKindOfClass:someClass] )
    ...
```

`isKindOfClass:` 返回 `YES` 的那一组类，与接收者可以被静态类型标注为的那一组类是相同的。

内省不局限于类型信息。本章后面几节还会讨论一些方法，它们可以返回类对象、报告一个对象是否能响应某条消息，以及揭示其他信息。

关于 `isKindOfClass:`、`isMemberOfClass:` 及相关方法的更多信息，参见 _[NSObject 类参考](https://developer.apple.com/documentation/objectivec/nsobject)_。

一个类定义包含多种信息，其中大多数都是关于该类实例的：

- 类的名称及其超类的名称
- 描述一组实例变量的模板
- 方法名称及其返回类型和参数类型的声明
- 方法的实现

这些信息经过编译后记录在提供给运行时系统使用的数据结构中。编译器只会创建一个对象——一个 _类对象（class object）_——来代表这个类。类对象能够访问关于这个类的全部信息，而这主要就是关于该类实例是什么样子的信息。它能够按照类定义中提出的方案来产生新的实例。

虽然类对象保存着类实例的原型，但它本身并不是一个实例。它没有自己的实例变量，也不能执行专门供该类实例使用的方法。不过，类定义中可以包含专门供类对象使用的方法——即 _类方法（class method）_，与 _实例方法（instance method）_ 相对。类对象会像实例继承实例方法一样，从层级结构中位于它之上的类那里继承类方法。

在源代码中，类对象由类名来表示。在下面的例子中，`Rectangle` 类使用一个从 `NSObject` 类继承来的方法返回类的版本号：

```objc
int versionNumber = [Rectangle version];
```

不过，类名只有作为消息表达式中的接收者时，才能代表类对象。在其他场合，你需要请求某个实例或类返回类的 `id`。实例和类都能响应 `class` 消息：

```objc
id aClass = [anObject class];
id rectClass = [Rectangle class];
```

如这些例子所示，类对象和所有其他对象一样，可以被标注为 `id` 类型。但类对象也可以更具体地被标注为 `Class` 这种数据类型：

```objc
Class aClass = [anObject class];
Class rectClass = [Rectangle class];
```

所有类对象都属于 `Class` 类型。用这个类型名来标注一个类，等价于用类名来对一个实例做静态类型标注。

因此，类对象是货真价实的对象，可以被动态类型化、接收消息、并从其他类继承方法。它们唯一特殊之处在于：它们由编译器创建，除了根据类定义构建出来的部分之外没有自己的数据结构（实例变量），并且是在运行时产生实例的代理者。

类对象的一项主要职能就是创建新实例。下面这段代码告诉 `Rectangle` 类创建一个新的矩形实例，并把它赋值给 `myRectangle` 变量：

```objc
id  myRectangle;
myRectangle = [Rectangle alloc];
```

`alloc` 方法为新对象的实例变量动态分配内存，并把它们全部初始化为 `0`——除了把新实例和它所属类连接起来的 `isa` 变量之外都是如此。要让一个对象真正有用，通常还需要对它做更完整的初始化，这正是 `init` 方法的职能。初始化通常紧接在分配之后进行：

```objc
myRectangle = [[Rectangle alloc] init];
```

在 `myRectangle` 能够接收本章前面例子中所展示的任何消息之前，必须先执行这行代码（或类似的代码）。`alloc` 方法返回一个新实例，该实例再执行一个 `init` 方法来设置自己的初始状态。每个类对象至少有一个能让它产生新对象的方法（比如 `alloc`），每个实例也至少有一个为它使用做准备的方法（比如 `init`）。初始化方法常常带有参数，用来传入特定的值，并用关键字来标注这些参数（例如 `initWithPosition:size:` 就可能是用来初始化一个新 `Rectangle` 实例的方法），但每个初始化方法都以“`init`”开头。

把类当作对象来处理，并不只是 Objective-C 语言的一时兴起，而是一个在设计上带来了预期收益、有时甚至带来意外收益的选择。举例来说，你可以用一个类来定制一个对象，而这个类本身属于一个开放的集合。例如在 AppKit 中，一个 `NSMatrix` 对象可以用某种特定的 `NSCell` 对象来定制。

`NSMatrix` 对象可以负责创建代表其单元格的各个对象。它可以在矩阵首次初始化时这样做，也可以在之后需要新单元格时这样做。`NSMatrix` 对象在屏幕上绘制的这个可见矩阵，可以在运行时——也许是响应用户操作——变大或变小。当它变大时，矩阵需要能够产生新的对象来填充新增的槽位。

但这些对象应该是什么种类呢？每个矩阵只显示一种 `NSCell`，但 `NSCell` 有许多不同的种类。图 1-3 中的继承层级展示了 AppKit 提供的其中一部分，它们都继承自通用的 `NSCell` 类。

__图 1-3__  NSCell 的继承层级

!

当一个矩阵创建 `NSCell` 对象时，这些对象应该是用来显示一排按钮或开关的 `NSButtonCell` 对象、用来显示供用户输入和编辑文本字段的 `NSTextFieldCell` 对象，还是其他某种 `NSCell`？`NSMatrix` 对象必须能容纳任意种类的单元格，甚至是尚未被发明出来的类型。

解决这个问题的一种办法是把 `NSMatrix` 类定义为抽象类，要求每个使用它的人都声明一个子类，并实现产生新单元格的方法。由于这些方法由使用者自己实现，他们就能确保创建出来的对象类型是正确的。

但这种解决方案要求 `NSMatrix` 类的使用者去做本该由 `NSMatrix` 类自己完成的工作，而且还会不必要地增加类的数量。因为一个应用程序可能需要不止一种矩阵，每种矩阵又搭配不同种类的单元格，程序中可能会因此充斥着各种 `NSMatrix` 子类。每当你发明一种新的 `NSCell`，你也不得不定义一种新的 `NSMatrix`。而且，不同项目上的程序员们会为了完成同样的工作而编写几乎完全相同的代码，全都是为了弥补 `NSMatrix` 自身的不足。

一个更好的解决方案——也是 `NSMatrix` 类所采用的方案——是允许用某种 `NSCell`（即某个类对象）来初始化 `NSMatrix` 实例。`NSMatrix` 类还定义了一个 `setCellClass:` 方法，用来传入 `NSMatrix` 在填充空槽位时应该使用的那种 `NSCell` 对象所对应的类对象：

```objc
[myMatrix setCellClass:[NSButtonCell class]];
```

`NSMatrix` 对象在首次初始化时、以及每当调整大小以容纳更多单元格时，都会使用这个类对象来产生新的单元格。如果类不是可以在消息中传递、可以赋值给变量的对象，这种定制就很难实现。

当你定义一个新类时，可以指定实例变量。该类的每个实例都可以维护你所声明变量的自己的一份副本——每个对象都控制着自己的数据。然而，与实例变量对应的类变量并不存在。类所提供的只是根据类定义初始化的内部数据结构。而且，类对象无法访问任何实例的实例变量；它不能初始化、读取或修改这些变量。

要让一个类的所有实例共享数据，你必须定义某种外部变量。最简单的做法是在类的实现文件中声明一个变量：

```objc
int MCLSGlobalVariable;

@implementation MyClass
// 实现继续
```

在更复杂的实现中，你可以把一个变量声明为 `static`，并提供类方法来管理它。把一个变量声明为 `static` 会把它的作用域限制在该类之内——而且只限于在该文件中实现的那部分类。（因此，与实例变量不同，静态变量不能被子类继承，也不能被子类直接操作。）这种模式常用来定义一个类的共享实例（例如单例；参见 _[Cocoa 基础指南](../Cocoa%20Fundamentals%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzu)_ 中的 [创建单例实例](../Cocoa%20Fundamentals%20Guide/Cocoa%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzufvbuqnbnknltgmq)）。

```objc
static MyClass *MCLSSharedInstance;

@implementation MyClass

+ (MyClass *)sharedInstance
{
    // 检查共享实例是否存在
    // 如有需要就创建它
    return MCLSSharedInstance;
}
// 实现继续
```

静态变量能让类对象获得的功能不止于充当产生实例的 _工厂（factory）_，还可以让它本身接近于一个完整而多用途的对象。类对象可以用来协调它所创建的实例、从已创建对象的列表中分发实例，或者管理应用程序所需的其他一些流程。如果你只需要某个特定类的一个对象，就可以把该对象的全部状态都放进静态变量中，只使用类方法，从而省去分配和初始化一个实例的步骤。

如果你想把类对象用于分配实例以外的其他用途，你可能需要像初始化实例一样对它进行初始化。虽然程序不会去分配类对象，但 Objective-C 确实提供了一种让程序对类对象进行初始化的方式。

如果一个类用到了静态变量或全局变量，`initialize` 方法就是设置它们初始值的好地方。例如，如果一个类维护着一个实例数组，`initialize` 方法就可以用来建立这个数组，甚至预先分配一两个默认实例备用。

运行时系统会在一个类接收任何其他消息之前、且在其超类已经收到 `initialize` 消息之后，向该类对象发送一条 `initialize` 消息。这个顺序让类有机会在被使用之前搭建好自己的运行时环境。如果不需要做任何初始化，你就不必编写 `initialize` 方法来响应这条消息。

由于继承的关系，如果一个类没有实现 `initialize` 方法，那么发送给它的 `initialize` 消息会被转发给它的超类，即使这个超类已经收到过 `initialize` 消息。举例来说，假设类 A 实现了 `initialize` 方法，类 B 继承自类 A 但没有实现 `initialize` 方法。就在类 B 即将接收它的第一条消息之前，运行时系统会向它发送 `initialize`。但由于类 B 没有实现 `initialize`，实际执行的会是类 A 的 `initialize`。因此，类 A 应当确保它的初始化逻辑只针对合适的类执行一次。

为了避免初始化逻辑被执行多次，在实现 `initialize` 方法时请使用清单 1-1 中的模板。

__清单 1-1__  initialize 方法的实现

```objc
+ (void)initialize
{
  if (self == [ThisClass class]) {
        // 在此执行初始化。
        ...
    }
}
```


所有对象，无论是类还是实例，都需要一个通往运行时系统的接口。类对象和实例都应当能够对自己的能力进行内省，并报告自己在继承层级中的位置。提供这个接口正是 `NSObject` 类的职责所在。

为了让 `NSObject` 的方法不必被实现两次——一次为实例提供运行时接口，再重复实现一次给类对象——类对象被赋予了一种特殊待遇，可以执行定义在根类中的实例方法。当一个类对象收到一条它无法用类方法响应的消息时，运行时系统会判断是否存在一个可以响应的根类实例方法。类对象能够执行的实例方法，只限于定义在根类中的那些，而且仅在没有类方法能胜任这项工作时才会如此。

关于类对象这种执行根类实例方法的特殊能力的更多信息，参见 _[NSObject 类参考](https://developer.apple.com/documentation/objectivec/nsobject)_。

在源代码中，类名只能用于两种截然不同的语境。这两种语境反映了类作为数据类型和作为对象的双重角色：

- 类名可以用作某种对象的类型名。例如：

```objc
Rectangle *anObject;
```

  这里 `anObject` 被静态标注为指向一个 `Rectangle` 对象的指针。编译器期望它具有 `Rectangle` 实例的数据结构，以及 `Rectangle` 类所定义和继承的实例方法。静态类型让编译器能做更好的类型检查，也让源代码更能自我说明。详情参见 [启用静态行为](Enabling%20Static%20Behavior.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjwfvjvomi)。

  只有实例才能被静态标注类型；类对象不能，因为它们不是某个类的成员，而是属于 `Class` 这种数据类型。
- 作为消息表达式中的接收者时，类名指的是类对象。前面几个例子已经展示过这种用法。类名只有作为消息接收者时才能代表类对象。在其他任何语境下，你都必须请求类对象揭示它的 `id`（通过向它发送一条 `class` 消息）。下面这个例子把 `Rectangle` 类作为参数传给一条 `isKindOfClass:` 消息：

```objc
if ( [anObject isKindOfClass:[Rectangle class]] )
    ...
```

  如果直接把名称“Rectangle”当作参数使用，那是非法的。类名只能充当接收者。

  如果你在编译期不知道类名，但在运行时以字符串的形式拥有它，你可以使用 `NSClassFromString` 来返回相应的类对象：

```objc
NSString *className;
    ...
if ( [anObject isKindOfClass:NSClassFromString(className)] )
    ...
```

  如果传给它的字符串不是有效的类名，这个函数会返回 `nil`。

类名和全局变量、函数名共享同一个命名空间。类和全局变量不能同名。在 Objective-C 中，类名是唯一具有全局可见性的名称。

你可以通过直接比较指针来测试两个类对象是否相等。不过，拿到正确的类是很重要的一点。Cocoa 框架中有若干特性会动态地、透明地为现有类派生子类，以扩展其功能（例如键值观察和 Core Data 就是这样做的——分别参见 _[键值观察编程指南](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)_ 和 _[Core Data 编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_）。在动态创建的子类中，[class](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/class) 方法通常会被重写，使这个子类伪装成它所替代的那个类。因此，在测试类是否相等时，你应当比较 [class](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/class) 方法返回的值，而不是比较更底层函数返回的值。用 API 的方式来表达，对于动态子类会有如下不等关系：

```objc
[object class] != object_getClass(object) != *((Class*)object)
```

因此，你应当按如下方式测试两个类是否相等：

```objc
if ([objectA class] == [objectB class]) { //...
```

[下一页](Defining%20a%20Class.md)[上一页](Introduction.md)

