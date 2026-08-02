---
title: 用 Objective-C 编程
apple_id: TP40011210
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/DefiningClasses/DefiningClasses.html
archived_at: '2026-07-15T07:17:51.067660Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [用 Objective-C 编程](About%20Objective-C.md)


[下一页](Working%20with%20Objects.md)[上一页](About%20Objective-C.md)

# 定义类

在为 OS X 或 iOS 编写软件时，你的大部分时间都花在处理对象上。Objective-C 中的对象和其他面向对象编程语言中的对象一样：它们把数据和相关行为打包在一起。

一个 app 由大量相互连接的对象组成一个庞大的生态系统，这些对象通过彼此通信来解决特定的问题，比如显示可视化界面、响应用户输入或存储信息。对于 OS X 或 iOS 开发而言，你不需要从零开始创建对象来解决所能想到的每一个问题；相反，你有大量现成的对象库可供使用，它们分别由 Cocoa（面向 OS X）和 Cocoa Touch（面向 iOS）提供。

其中一些对象可以立即使用，比如字符串和数字这样的基本数据类型，或者按钮和表视图这样的用户界面元素。还有一些则是设计成让你用自己的代码去定制，使其表现出你所需要的行为。app 开发过程就在于决定如何最好地定制和组合底层框架提供的对象与你自己的对象，从而赋予你的 app 独特的功能特性。

用面向对象编程的术语来说，对象是类的一个实例。本章将演示如何在 Objective-C 中通过声明接口来定义类，接口描述了你打算让该类及其实例被如何使用。这个接口包括该类能够接收的消息列表，因此你还需要提供类的实现，其中包含响应每条消息所要执行的代码。

类描述了某一特定类型对象所共有的行为和属性。对于一个字符串对象（在 Objective-C 中，它是类 `NSString` 的一个实例）来说，这个类提供了多种方式来检查和转换它所表示的内部字符。类似地，用来描述数字对象的类（`NSNumber`）围绕一个内部数值提供了相应功能，比如把这个值转换成另一种数值类型。

就像用同一张蓝图建造的多栋建筑在结构上完全相同一样，一个类的每个实例都与该类的其他所有实例共享相同的属性和行为。每个 `NSString` 实例的行为方式都相同，无论它内部保存的字符串是什么。

任何一个特定对象都是设计成以特定方式被使用的。你可能知道一个字符串对象代表某串字符，但你不需要知道用来存储这些字符的具体内部机制。你对该对象自身用来直接处理其字符的内部行为一无所知，但你确实需要知道该如何与这个对象交互，比如向它索取特定字符，或者请求一个把所有原始字符都转换成大写的新对象。

在 Objective-C 中，_类接口_ 精确规定了某种类型的对象应当如何被其他对象使用。换句话说，它定义了该类实例与外部世界之间的公开接口。

有些类定义的对象是_不可变（immutable）_的。这意味着对象的内部内容必须在创建时就设置好，之后不能再被其他对象更改。在 Objective-C 中，所有基本的 `NSString` 和 `NSNumber` 对象都是不可变的。如果你需要表示另一个数字，就必须使用一个新的 `NSNumber` 实例。

有些不可变类还提供了一个_可变（mutable）_版本。如果你确实需要在运行时更改字符串的内容——比如在通过网络连接接收字符时不断追加——就可以使用 `NSMutableString` 类的实例。这个类的实例行为和 `NSString` 对象完全一样，只是它们还额外提供了更改对象所表示字符的功能。

虽然 `NSString` 和 `NSMutableString` 是不同的类，但它们有许多相似之处。与其从零开始编写两个完全独立、却恰好有一些相似行为的类，不如充分利用继承。

在自然界中，分类学用「种」「属」「科」这样的术语把动物划分成不同的群组。这些群组是层级化的，多个种可能属于同一个属，多个属又可能属于同一个科。

举例来说，大猩猩、人类和红毛猩猩之间有不少明显的相似之处。虽然它们分属不同的种，甚至不同的属、族和亚科，但由于它们都同属一个科（称为「人科」），因此在分类学上有亲缘关系，如 [图 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqmznknltcnq) 所示。

__图 1-1__  物种间的分类关系

!!

在面向对象编程的世界里，对象同样被划分成层级化的群组。这里不使用属或种这样的不同术语来区分不同的层级，对象只是被简单地组织成类。就像人类作为人科成员会继承某些特征一样，一个类也可以被设置为从父类继承功能。

当一个类从另一个类继承时，子类会继承父类定义的全部行为和属性。它也有机会去定义自己额外的行为和属性，或者_覆写（override）_父类的行为。

以 Objective-C 的字符串类为例，`NSMutableString` 的类描述指明该类继承自 `NSString`，如 [图 1-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqmznknltema) 所示。`NSString` 提供的所有功能在 `NSMutableString` 中都可以使用，比如查询特定字符或请求生成新的大写字符串，而 `NSMutableString` 还额外添加了一些方法，让你可以追加、插入、替换或删除子字符串和单个字符。

__图 1-2__  NSMutableString 类的继承关系

!

就像所有生物都共享一些基本的「生命」特征一样，某些功能在 Objective-C 的所有对象中也是通用的。

当一个 Objective-C 对象需要与另一个类的实例协同工作时，它期望对方的类提供某些基本特性和行为。因此，Objective-C 定义了一个_根类（root class）_，绝大多数其他类都从它继承而来，这个根类就是 `NSObject`。当一个对象遇到另一个对象时，它至少期望能够使用 `NSObject` 类描述所定义的基本行为来与之交互。

当你定义自己的类时，至少应该从 `NSObject` 继承。一般来说，你应该找一个提供与你所需功能最接近的 Cocoa 或 Cocoa Touch 对象，并从它继承。

举例来说，如果你想为 iOS app 定义一个自定义按钮，而系统提供的 `UIButton` 类没有提供足够的可定制属性来满足你的需求，那么创建一个继承自 `UIButton` 的新类会比继承自 `NSObject` 更合理。如果你只是继承自 `NSObject`，你就得把 `UIButton` 类定义的所有复杂视觉交互和通信逻辑都重新实现一遍，才能让你的按钮表现出用户期望的行为。此外，通过继承自 `UIButton`，你的子类还能自动获得未来对 `UIButton` 内部行为所做的任何增强或错误修复。

`UIButton` 类本身被定义为继承自 `UIControl`，后者描述了 iOS 上所有用户界面控件共有的基本行为。`UIControl` 类又继承自 `UIView`，从而获得了显示在屏幕上的对象所共有的功能。`UIView` 继承自 `UIResponder`，使其能够响应用户输入，比如轻触、手势或摇动。最后，在这棵继承树的根部，`UIResponder` 继承自 `NSObject`，如 [图 1-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqmznknltemi) 所示。

__图 1-3__  UIButton 类的继承关系

!!

这条继承链意味着 `UIButton` 的任何自定义子类不仅会继承 `UIButton` 自身声明的功能，还会依次继承每个超类所拥有的功能。最终你得到的这个类所描述的对象，其行为就像一个按钮，能够在屏幕上显示自己、响应用户输入，并能与任何其他基本的 Cocoa Touch 对象通信。

对于你需要用到的任何类，牢记它的继承链非常重要，这样才能准确弄清楚它到底能做什么。举例来说，Cocoa 和 Cocoa Touch 提供的类参考文档，可以让你轻松地从任何一个类导航到它的各个超类。如果你在某个类的接口或参考文档中没有找到你要找的内容，它很可能就定义或记录在继承链上更靠上的某个超类中。

面向对象编程的众多好处之一，就是前面提到的这个理念——要使用一个类，你只需要知道如何与它的实例交互即可。更具体地说，一个对象应当被设计成隐藏其内部实现的细节。

举例来说，如果你在 iOS app 中使用标准的 `UIButton`，你不需要关心像素是如何被操作从而让按钮显示在屏幕上的。你只需要知道可以更改某些属性，比如按钮的标题和颜色，并相信当你把它添加到你的可视化界面中时，它会被正确显示，并表现出你所期望的行为。

当你定义自己的类时，首先要弄清楚这些公开的属性和行为。你希望哪些属性可以被公开访问？是否应该允许更改这些属性？其他对象要如何与你的类的实例通信？

这些信息都要写进你这个类的接口——它定义了你打算让其他对象如何与该类的实例交互。公开接口的描述与类的_内部（internal）_行为是分开的，后者构成了类的实现。在 Objective-C 中，接口和实现通常放在不同的文件里，这样你只需要公开接口即可。

用来声明类接口的 Objective-C 语法如下所示：

```objc
@interface SimpleClass : NSObject

@end
```

这个示例声明了一个名为 `SimpleClass` 的类，它继承自 `NSObject`。

公开的属性和行为都定义在 `@interface` 声明内部。在这个示例中，除了超类之外没有指定任何其他内容，所以 `SimpleClass` 实例上预期可用的功能就只有从 `NSObject` 继承来的功能。

对象通常拥有一些打算供公开访问的属性。举例来说，如果你在一个记录管理 app 中定义一个表示人的类，你可能会决定需要一些字符串属性来表示一个人的名字和姓氏。

这些属性的声明应该添加在接口内部，就像这样：

```objc
@interface Person : NSObject

@property NSString *firstName;
@property NSString *lastName;

@end
```

在这个示例中，`Person` 类声明了两个公开属性，它们都是 `NSString` 类的实例。

这两个属性都是针对 Objective-C 对象的，所以它们使用_星号（asterisk）_来表示自己是 C 指针。它们也和 C 语言中其他变量声明一样是语句，因此结尾需要一个分号。

你可能决定添加一个属性来表示一个人的出生年份，以便按年份分组排序，而不只是按姓名排序。你可以使用一个数字_对象_属性：

```objc
@property NSNumber *yearOfBirth;
```

但这么做只是为了存储一个简单的数值，可能显得有点大材小用。另一种选择是使用 C 提供的_基本类型（primitive type）_之一，它们保存标量值，比如一个整数：

```objc
@property int yearOfBirth;
```


到目前为止展示的示例都声明了打算完全公开访问的属性。这意味着其他对象既可以读取这些属性的值，也可以更改它们。

在某些情况下，你可能会决定声明某个属性不打算被更改。在现实世界中，一个人要更改自己登记在案的名字或姓氏，必须填写大量文件。如果你在编写一个官方记录管理 app，你可能会选择把表示一个人姓名的公开属性指定为_只读（read-only）_，要求任何更改都必须通过一个中间对象来请求，由该对象负责验证请求并批准或拒绝它。

Objective-C 的属性声明可以包含_属性特性（property attribute）_，除其他用途外，它们还可以用来表示某个属性是否打算设为只读。在一个官方记录管理 app 中，`Person` 类的接口可能是这样的：

```objc
@interface Person : NSObject
@property (readonly) NSString *firstName;
@property (readonly) NSString *lastName;
@end
```

属性特性是在 `@property` 关键字之后的括号内指定的，详见 [为暴露的数据声明公开属性](Encapsulating%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnjnknlti)。

到目前为止的示例涉及的都是描述典型[模型](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ModelObject.html#//apple_ref/doc/uid/TP40008195-CH31)对象的类，即主要用于封装数据的对象。以 `Person` 类为例，除了能够访问这两个已声明的属性之外，很可能不需要任何其他功能。然而，大多数类除了已声明的属性之外，确实还包含相应的行为。

既然 Objective-C 软件是由一个庞大的对象网络构建而成的，那么需要注意的是，这些对象可以通过发送_消息（message）_彼此交互。用 Objective-C 的术语来说，一个对象通过在另一个对象上调用方法来向它发送消息。

Objective-C 方法在概念上和 C 语言及其他编程语言中的标准函数类似，只是语法相当不同。一个 C 函数声明是这样的：

```c
void SomeFunction();
```

等价的 Objective-C 方法声明是这样的：

```objc
- (void)someMethod;
```

在这个例子中，该方法没有参数。C 语言的 `void` 关键字被用在声明开头的括号内，表示该方法执行完毕后不返回任何值。

方法名前面的减号（`-`）表示这是一个_实例方法（instance method）_，可以在该类的任何实例上调用。这将它与_类方法（class method）_区分开来，类方法是在类本身上调用的，详见 [Objective-C 的类也是对象](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqmznknltcoa)。

和 C 函数原型一样，Objective-C 类接口中的方法声明也和其他 C 语句一样，需要以分号结尾。

如果你需要声明一个带有一个或多个参数的方法，其语法和典型的 C 函数截然不同。

对于 C 函数，参数是在括号内指定的，就像这样：

```c
void SomeFunction(SomeType value);
```

Objective-C 方法声明则是用冒号把参数作为方法名的一部分包含进来，就像这样：

```objc
- (void)someMethodWithValue:(SomeType)value;
```

和返回类型一样，参数类型也是写在括号中指定的，就像标准的 C 类型转换一样。

如果你需要提供多个参数，其语法和 C 语言又有很大不同。C 函数的多个参数是在括号内用逗号分隔指定的；而在 Objective-C 中，一个带有两个参数的方法声明是这样的：

```objc
- (void)someMethodWithFirstValue:(SomeType)value1 secondValue:(AnotherType)value2;
```

在这个示例中，`value1` 和 `value2` 是在实现中用来访问方法调用时所提供的值的名称，就像它们是变量一样。

有些编程语言允许在函数定义中使用所谓的_命名参数（named argument）_；需要注意的是，Objective-C 并非如此。方法调用中参数的顺序必须与方法声明相匹配，事实上方法声明中 `secondValue:` 这部分本身就是方法名的一部分：

```
someMethodWithFirstValue:secondValue:
```

这也是让 Objective-C 成为一门可读性很强的语言的特性之一，因为方法调用时传入的值是_内联（inline）_指定的，紧挨着方法名中相应的部分，详见 [你可以为方法参数传入对象](Working%20with%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnbnknltcmy)。

需要注意的是，每个类的名字在一个 app 内必须是唯一的，即便跨越所引入的库或框架也是如此。如果你在一个项目中尝试创建一个与现有类同名的新类，就会收到一个编译器错误。

因此，建议为你定义的所有类名加上一个由三个或更多字母组成的_前缀（prefix）_。这些字母可能与你当前编写的 app 有关，或者与某个可复用代码框架的名字有关，也可能只是你名字的缩写。

本文档接下来给出的所有示例都会使用类名前缀，就像这样：

```objc
@interface XYZPerson : NSObject
@property (readonly) NSString *firstName;
@property (readonly) NSString *lastName;
@end
```

相比之下，方法名和属性名只需要在其所定义的类内部保持唯一即可。虽然一个 app 中的每个 C 函数都必须有唯一的名字，但多个 Objective-C 类定义同名方法是完全可以接受的（而且往往是可取的）。不过，你不能在同一个类声明中多次定义同一个方法；但如果你想_覆写（override）_从父类继承来的方法，就必须使用与原始声明完全相同的名字。

和方法一样，对象的属性与_实例变量（instance variable）_（详见 [大多数属性都由实例变量支撑](Encapsulating%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnjnknltm)）也只需要在其所定义的类内部保持唯一。不过，如果你使用全局变量，这些变量的名字就必须在整个 app 或项目内保持唯一。

更多命名规范和建议参见 [约定](Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqmjqfvjvomi)。

一旦你为一个类定义好了接口，包括打算公开访问的属性和方法，接下来就需要编写代码来实现这个类的行为。

如前所述，一个类的接口通常放在一个专门的文件里，这个文件常被称为_头文件（header file）_，其文件扩展名一般为 `.h`。Objective-C 类的实现则写在扩展名为 `.m` 的源代码文件中。

每当接口定义在头文件中时，你都需要在编译源代码文件中的实现之前，告诉编译器先读取这个头文件。为此，Objective-C 提供了一个预处理指令 `#import`。它类似于 C 语言的 `#include` 指令，但能确保一个文件在编译过程中只被包含一次。

请注意，预处理指令不同于传统的 C 语句，结尾不使用分号。

为一个类提供实现的基本语法如下所示：

```objc
#import "XYZPerson.h"

@implementation XYZPerson

@end
```

如果你在类接口中声明了任何方法，就需要在这个文件中实现它们。

对于一个只有一个方法的简单类接口，就像这样：

```objc
@interface XYZPerson : NSObject
- (void)sayHello;
@end
```

其实现可能是这样的：

```objc
#import "XYZPerson.h"

@implementation XYZPerson
- (void)sayHello {
    NSLog(@"Hello, World!");
}
@end
```

这个示例使用 `NSLog()` 函数把一条消息记录到控制台。它类似于标准 C 库中的 `printf()` 函数，接受数量可变的参数，其中第一个参数必须是一个 Objective-C 字符串。

方法的实现和 C 函数定义类似，都使用花括号来包含相应的代码。此外，方法的名字必须与其原型完全一致，参数和返回类型也必须精确匹配。

Objective-C 从 C 语言继承了大小写敏感的特性，所以下面这个方法：

```objc
- (void)sayhello {
}
```

会被编译器视为与前面展示的 `sayHello` 方法完全不同的方法。

一般来说，方法名应该以小写字母开头。Objective-C 的惯例是给方法起比典型 C 函数更具描述性的名字。如果方法名涉及多个单词，使用_驼峰式命名（camel case）_（每个新单词的首字母大写）让它们更易读。

另外要注意，Objective-C 对空白符的使用比较灵活。惯例是用制表符或空格缩进代码块内的每一行，你也经常会看到左花括号单独占一行，就像这样：

```objc
- (void)sayHello
{
    NSLog(@"Hello, World!");
}
```

Xcode 是苹果用于创建 OS X 和 iOS 软件的集成开发环境（IDE），它会根据一组可自定义的用户偏好设置自动为你的代码缩进。更多信息参见 _[Xcode Workspace Guide](../../Developer%20Tools/Xcode%20Workspace%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmrq)_ 中的 [更改缩进和制表符宽度](../../Developer%20Tools/Xcode%20Workspace%20Guide/The%20Text%20Editor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnzzfvjvonbr)。

在下一章[使用对象](Working%20with%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnbnknltc)中，你将看到更多方法实现的示例。

在 Objective-C 中，类本身就是一个对象，其类型是一个名为 `Class` 的_不透明类型（opaque type）_。类不能像前面为实例展示的那样用声明语法来定义属性，但类可以接收消息。

类方法的典型用途是作为_工厂方法（factory method）_，它是 [对象是动态创建的](Working%20with%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjqfvbuqnbnknlto) 中所描述的对象分配与初始化流程的另一种选择。举例来说，`NSString` 类提供了多种工厂方法，可以用来创建一个空字符串对象，或者一个用特定字符初始化的字符串对象，包括：

```objc
+ (id)string;
+ (id)stringWithString:(NSString *)aString;
+ (id)stringWithFormat:(NSString *)format, …;
+ (id)stringWithContentsOfFile:(NSString *)path encoding:(NSStringEncoding)enc error:(NSError **)error;
+ (id)stringWithCString:(const char *)cString encoding:(NSStringEncoding)enc;
```

如这些示例所示，类方法用 `+` 号表示，这将它们与使用 `-` 号的实例方法区分开来。

类方法的原型可以和实例方法原型一样包含在类接口中。类方法的实现方式也和实例方法相同，都写在该类的 `@implementation` 块内。

1. 使用 Xcode 的 New File 模板窗口，为一个名为 `XYZPerson`、继承自 `NSObject` 的 Objective-C 类创建接口文件和实现文件。
2. 为 `XYZPerson` 类接口添加表示一个人名字、姓氏和出生日期的属性（日期用 `NSDate` 类表示）。
3. 声明 `sayHello` 方法，并按照本章前面展示的方式实现它。
4. 添加一个名为「`person`」的类工厂方法的声明。在读完下一章之前，先不用管这个方法的实现。

[下一页](Working%20with%20Objects.md)[上一页](About%20Objective-C.md)

