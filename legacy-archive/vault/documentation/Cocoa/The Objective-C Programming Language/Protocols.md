---
title: Objective-C 编程语言
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocProtocols.html
archived_at: '2026-07-15T07:17:31.898783Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 编程语言](Introduction.md)


[下一页](Declared%20Properties.md)[上一页](Defining%20a%20Class.md)

# 协议

协议声明的方法可以由任何类实现。协议至少在以下三种情况下很有用：

- 声明希望由其他人实现的方法
- 在隐藏对象所属类的同时，声明该对象的_接口_
- 捕捉那些在继承层次上没有关系的类之间的相似性

类和分类的接口所声明的方法都与某个特定的类相关联——主要是该类所实现的方法。而非正式和正式的_协议_，则声明那些不依赖于任何特定类、但可能由任何类（甚至许多个类）实现的方法。

协议其实就是一份方法声明的列表，不依附于任何类的定义。例如，下面这些报告用户鼠标操作的方法就可以归入一个协议：

```objc
- (void)mouseDown:(NSEvent *)theEvent;
- (void)mouseDragged:(NSEvent *)theEvent;
- (void)mouseUp:(NSEvent *)theEvent;
```

任何想要响应鼠标_事件_的类，都可以采纳该协议并实现其方法。

协议让方法声明摆脱了对类继承层次结构的依赖，因此协议可以用在类和分类都无法胜任的场合。协议所列出的方法是（或者可能是）在某处实现的，但具体是哪个类实现了它们并不重要。真正重要的是某个特定的类是否_遵循_该协议——也就是它是否实现了协议所声明的方法。这样一来，对象就不仅可以根据继承自同一个类所产生的相似性来分类，也可以根据它们同样遵循某个协议这一相似性来分类。位于继承层次结构中互不相关分支上的类，也可能因为遵循同一个协议而被归为同一种类型。

协议在面向对象设计中可以发挥重要作用，尤其是当一个项目由多位实现者共同完成，或者其中包含了在其他项目中开发的对象时。Cocoa 软件大量使用协议，以支持通过 Objective-C 消息进行的进程间通信。

不过，Objective-C 程序并不一定要使用协议。与类定义和消息表达式不同，协议是可选的。有些 Cocoa 框架会用到协议，有些则不会，这完全取决于具体的任务。

如果你知道一个对象所属的类，就可以查看它的接口声明（以及它所继承的各个类的接口声明），来了解它能响应哪些消息。这些声明公布了它可以接收的消息。而协议则提供了一种方式，让它也能公布自己所发送的消息。

通信是双向的；对象既会发送消息，也会接收消息。例如，一个对象可能把某项操作的职责委托给另一个对象，或者有时只是需要向另一个对象询问信息。在某些情况下，一个对象可能愿意把自己的行为通知给其他对象，以便它们采取可能需要的相应措施。

如果发送者所属的类和接收者所属的类都是同一个项目的一部分（或者别人已经把接收者及其接口文件提供给了你），那么这种通信就很容易协调。发送者只需导入接收者的接口文件即可。被导入的文件声明了发送者在其发送的消息中所用到的方法选择器。

然而，如果你开发的对象要向尚未定义的对象——也就是留给其他人去实现的对象——发送消息，你就不会有接收者的接口文件。这时你需要另一种方式，来声明那些你在消息中用到、但自己并不实现的方法。协议正是为此而生。它既告知编译器该类用到了哪些方法，也告知其他实现者，为了让他们的对象能与你的对象协同工作，需要定义哪些方法。

举例来说，假设你开发的一个对象，会通过发送 `helpOut:` 等消息，向另一个对象请求帮助。你提供了一个 `assistant` 实例变量，用来记录这些消息的出口（outlet），并定义了一个配套方法来设置这个实例变量。这个方法让其他对象可以把自己注册为你的对象所发消息的潜在接收者：

```objc
- setAssistant:anObject
{
    assistant = anObject;
}
```

然后，每当要向 `assistant` 发送消息时，都会先检查一下，确保接收者实现了可以响应的方法：

```objc
- (BOOL)doWork
{
    ...
    if ( [assistant respondsToSelector:@selector(helpOut:)] ) {
        [assistant helpOut:self];
        return YES;
    }
    return NO;
}
```

因为在编写这段代码的时候，你无法知道会有什么样的对象把自己注册为 `assistant`，所以你只能为 `helpOut:` 方法声明一个协议；你没办法导入实现该方法的那个类的接口文件。

协议可以用来声明一个_匿名对象_（即类未知的对象）的方法。匿名对象可能代表某种服务，或者处理一组有限的功能，尤其是在只需要这一类对象中的某一个实例时。（在定义应用程序架构中起基础性作用的对象，以及那些在使用前必须先初始化的对象，都不太适合做成匿名对象。）

当然，对象对它们的开发者来说并不是匿名的，但当开发者把它们提供给别人时，它们就是匿名的了。举例来说，考虑下面这些情形：

- 提供框架或一整套对象供他人使用的开发者，可以在其中包含一些没有类名或接口文件标识的对象。由于缺少类名和类接口，使用者无法自行创建该类的实例。因此，供应方必须提供一个现成的实例。通常，另一个类中的某个方法会返回一个可用的对象：

```objc
id formatter = [receiver formattingService];
```

  这个方法返回的对象没有类身份——至少供应方不愿意透露它的类身份。为了让这个对象还能有些用处，供应方必须愿意说明它能响应的至少一部分消息。这些消息是通过把该对象与协议中声明的一系列方法关联起来来说明的。
- 你可以向_远程对象_——也就是其他应用程序中的对象——发送 Objective-C 消息。

  每个应用程序都有自己的结构、类和内部逻辑。但要和另一个应用程序通信，你并不需要知道它是如何运作的，也不需要知道它由哪些组件构成。作为一个局外者，你只需要知道可以发送哪些消息（协议）以及把它们发送到哪里（接收者）。

  如果一个应用程序把自己的某个对象公开为可能接收_远程消息_的对象，那它也必须公开一个协议，声明该对象用来响应这些消息的方法。除此之外，它不必透露关于这个对象的任何其他信息。发送消息的应用程序不需要知道这个对象的类，也不需要在自己的设计中使用这个类，它所需要的只是这个协议。

协议让匿名对象成为可能。如果没有协议，就没有办法在不指明对象所属类的情况下，为它声明一个接口。

如果有不止一个类实现了同一组方法，这些类通常会被归到一个抽象类之下，由该抽象类声明它们共有的方法。每个子类都可以按自己的方式重新实现这些方法，但继承层次结构以及抽象类中的公共声明，捕捉到了这些子类之间本质上的相似性。

然而，有时无法把公共方法归入一个抽象类中。那些在大多数方面都毫不相干的类，可能仍然需要实现一些相似的方法。这种有限的相似性，可能还不足以构成一种继承层次上的关系。例如，你可能想为应用程序中的对象添加创建 XML 表示形式的支持，以及从 XML 表示形式初始化对象的支持：

```objc
- (NSXMLElement *)XMLRepresentation;
- initFromXMLRepresentation:(NSXMLElement *)xmlString;
```

这些方法可以归入一个协议中，而实现这些方法的各个类之间的相似性，则可以通过说明它们都遵循同一个协议来体现。

对象可以根据这种相似性（也就是它们所遵循的协议）来划分类型，而不是根据它们所属的类。例如，一个 `NSMatrix` 实例必须与代表其单元格的对象进行通信。这个矩阵可以要求每一个这样的对象都是某种 `NSCell`（一种基于类的类型），并依赖这样一个事实：所有继承自 `NSCell` 类的对象都拥有响应 `NSMatrix` 消息所需的方法。另一种做法是，`NSMatrix` 对象可以要求代表单元格的对象拥有能够响应某组特定消息的方法（一种基于协议的类型）。在这种情况下，`NSMatrix` 对象并不关心某个单元格对象属于哪个类，只关心它是否实现了这些方法。

Objective-C 语言提供了一种方式，可以把一份方法列表（包括[声明的属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)）正式声明为一个协议。_正式协议_由语言本身和运行时系统提供支持。例如，编译器可以检查基于协议的类型，对象也可以在运行时进行自省，来报告自己是否遵循某个协议。

你使用 `@protocol` 指令来声明正式协议：

```objc
@protocol ProtocolName
method declarations
@end
```

例如，你可以像这样声明一个 XML 表示协议：

```objc
@protocol MyXMLSupport
- initFromXMLRepresentation:(NSXMLElement *)XMLElement;
- (NSXMLElement *)XMLRepresentation;
@end
```

与类名不同，协议名并不具有全局可见性。它们生活在自己的命名空间里。

协议方法可以用 `@optional` 关键字标记为可选。与 `@optional` 这个模态关键字相对应的是 `@required` 关键字，用于正式表明默认行为的语义。你可以用 `@optional` 和 `@required` 按自己的需要，把协议划分成若干部分。如果你不指定任何关键字，默认就是 `@required`。

```objc
@protocol MyProtocol

- (void)requiredMethod;

@optional
- (void)anOptionalMethod;
- (void)anotherOptionalMethod;

@required
- (void)anotherRequiredMethod;

@end
```


除了正式协议之外，你还可以通过在一个分类声明中对方法进行分组，来定义一个_非正式协议_：

```objc
@interface NSObject ( MyXMLSupport )
- initFromXMLRepresentation:(NSXMLElement *)XMLElement;
- (NSXMLElement *)XMLRepresentation;
@end
```

非正式协议通常被声明为 `NSObject` 类的分类，因为这样可以把这些方法名广泛地与所有继承自 `NSObject` 的类关联起来。由于所有的类都继承自根类，这些方法就不会被限制在_继承层次结构_的某一部分。（也可以把非正式协议声明为另一个类的分类，从而把它限制在继承层次结构的某个分支上，但这样做的理由不多。）

当用于声明协议时，分类接口并没有对应的实现。相反，实现该协议的各个类会在自己的接口文件中再次声明这些方法，并在各自的_实现_文件中把它们和其他方法一起定义出来。

非正式协议变通地利用了分类声明的规则，列出了一组方法，却不把它们与任何特定的类或实现关联起来。

由于是非正式的，声明在分类中的协议得不到太多语言层面的支持。既没有编译期的类型检查，也没有运行时检查一个对象是否遵循该协议。要获得这些好处，你必须使用正式协议。当所有方法都是可选的时候，非正式协议可能会很有用，比如用于_委托_，但（在 OS X v10.5 及之后的版本中）通常更适合使用带有可选方法的正式协议。

正如类在运行时由类对象表示、方法由选择器代码表示一样，正式协议也由一种特殊的数据类型表示——即 `Protocol` 类的实例。凡是要处理协议本身（而不只是在类型说明中使用它）的源代码，都必须引用相应的协议对象。

在许多方面，协议都与类的定义很相似。它们都声明方法，在运行时也都由对象表示——类由 `Class` 的实例表示，协议由 `Protocol` 的实例表示。和类对象一样，协议对象也是根据源代码中的定义和声明自动创建的，并由运行时系统使用。它们不会在程序源代码中被分配和初始化。

源代码可以使用 `@protocol()` 指令来引用一个协议对象——这与声明协议所用的指令相同，只是这里多了一对结尾的圆括号。圆括号中包含协议名：

```
Protocol *myXMLSupportProtocol = @protocol(MyXMLSupport);
```

这是源代码能够凭空生成一个协议对象的唯一方式。与类名不同，协议名本身并不指代该对象——除非是在 `@protocol()` 内部。

编译器只会为它遇到的每一个协议声明创建一个协议对象，但前提是这个协议还必须：

- 被某个类采纳，或者
- 在源代码中的某处被引用（使用 `@protocol()`）

那些已声明但未被使用的协议（除了用于类型检查，如下文所述），在运行时不会由协议对象来表示。

采纳一个协议，在某些方面类似于声明一个超类。两者都会为类赋予方法。超类声明为类赋予继承来的方法；协议则为类赋予协议列表中声明的方法。如果一个类在其声明中，把某个协议列在超类名之后的尖括号里，就说这个类_采纳_了这个正式协议：

```objc
@interface ClassName : ItsSuperclass < protocol list >
```

分类采纳协议的方式与此大致相同：

```objc
@interface ClassName ( CategoryName ) < protocol list >
```

一个类可以采纳不止一个协议；协议列表中的各个名称用逗号分隔。

```objc
@interface Formatter : NSObject < Formatting, Prettifying >
```

采纳某个协议的类或分类，必须实现该协议所声明的全部必需方法，否则编译器会发出警告。上面的 Formatter 类会定义它所采纳的两个协议中声明的全部必需方法，此外还可能定义它自己声明的其他方法。

采纳某个协议的类或分类，必须导入声明该协议的头文件。协议中所声明的方法，不会在类或分类接口的其他地方重复声明。

一个类完全可以只采纳协议，而不声明任何其他方法。例如，下面这个类声明采纳了 `Formatting` 和 `Prettifying` 协议，但没有声明它自己的任何实例变量或方法：

```objc
@interface Formatter : NSObject < Formatting, Prettifying >
@end
```


如果一个类采纳了某个正式协议，或者继承自另一个采纳了该协议的类，就说这个类_遵循_这个协议。一个类的实例，被认为遵循其所属类所遵循的那一整套协议。

因为一个类必须实现它所采纳的协议中声明的全部必需方法，所以说一个类或一个实例遵循某个协议，等同于说它的方法库里具备了该协议所声明的全部方法。

可以通过向一个对象发送 [conformsToProtocol:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/conformsToProtocol:) 消息，来检查它是否遵循某个协议。

```
if ( ! [receiver conformsToProtocol:@protocol(MyXMLSupport)]  ) {
    // 对象不遵循 MyXMLSupport 协议
    // 如果你原本期望 receiver 实现 MyXMLSupport 协议中声明的方法，
    //  那这里很可能就是一个错误
}
```

（请注意，还存在一个同名的类方法——[conformsToProtocol:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/conformsToProtocol:)。）

`conformsToProtocol:` 测试类似于针对单个方法的 [respondsToSelector:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/respondsToSelector:) 测试，区别在于它测试的是某个协议是否已被采纳（并且大概协议所声明的全部方法都已实现），而不仅仅是某一个特定方法是否已实现。因为它一次性检查协议中的所有方法，`conformsToProtocol:` 可能比 [respondsToSelector:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/respondsToSelector:) 更高效。

`conformsToProtocol:` 测试也类似于 `isKindOfClass:` 测试，区别在于它测试的是基于协议的类型，而不是基于继承层次结构的类型。

对象的类型声明可以扩展，加入正式协议。因此，协议提供了另一层由编译器执行的类型检查的可能性，这种检查更为抽象，因为它并不依赖于具体的实现。

在类型声明中，协议名会列在类型名之后的尖括号之间：

```objc
- (id <Formatting>)formattingService;
id <MyXMLSupport> anObject;
```

正如静态类型让编译器能够基于类的继承层次结构来检验类型一样，这种语法也让编译器能够基于是否遵循某个协议来检验类型。

例如，如果 `Formatter` 是一个抽象类，那么下面这个声明

```
Formatter *anObject;
```

把所有继承自 Formatter 的对象归为一种类型，并允许编译器据此检查赋值是否合法。

同样，下面这个声明

```
id <Formatting> anObject;
```

把所有遵循 Formatting 协议的对象都归为一种类型，无论它们在类继承层次结构中处于什么位置。编译器可以确保只有遵循该协议的对象才能被赋值给这个类型。

在这两种情况下，类型都把相似的对象归到了一起——要么是因为它们有共同的继承关系，要么是因为它们汇聚到了同一组方法上。

这两种类型可以合并在同一个声明里：

```
Formatter <Formatting> *anObject;
```

协议不能用来对类对象进行类型声明。只有实例才能被静态声明为某个协议的类型，就像只有实例才能被静态声明为某个类的类型一样。（不过，在运行时，类和实例都可以响应 `conformsToProtocol:` 消息。）

一个协议可以用类采纳协议时所用的相同语法，来纳入其他协议：

```objc
@protocol ProtocolName < protocol list >
```

列在尖括号之间的所有协议，都被视为 _ProtocolName_ 协议的一部分。例如，如果 `Paging` 协议纳入了 `Formatting` 协议

```objc
@protocol Paging < Formatting >
```

那么任何遵循 `Paging` 协议的对象，也就遵循 `Formatting` 协议。像下面这样的类型声明

```
id <Paging> someObject;
```

以及像下面这样的 `conformsToProtocol:` 消息

```
if ( [anotherObject conformsToProtocol:@protocol(Paging)] )
    ...
```

只需要提到 `Paging` 协议，就同时测试了是否遵循 `Formatting` 协议。

正如前面提到的，当一个类采纳某个协议时，它必须实现该协议所声明的必需方法。此外，它还必须遵循这个所采纳协议所纳入的其他任何协议。如果某个被纳入的协议又纳入了别的协议，这个类也必须遵循那些协议。一个类可以通过以下两种方式之一，来遵循一个被纳入的协议：

- 实现该协议所声明的方法
- 继承自一个采纳了该协议并实现了这些方法的类

举例来说，假设 `Pager` 类采纳了 `Paging` 协议。如果 `Pager` 是 `NSObject` 的子类，如下所示：

```objc
@interface Pager : NSObject < Paging >
```

它就必须实现全部的 `Paging` 方法，包括所纳入的 `Formatting` 协议中声明的方法。它随 `Paging` 一起采纳了 `Formatting` 协议。

另一方面，如果 `Pager` 是 `Formatter`（一个独立采纳了 `Formatting` 协议的类）的子类，如下所示：

```objc
@interface Pager : Formatter < Paging >
```

它就只需要实现 `Paging` 协议本身声明的方法，而不必实现 `Formatting` 中声明的方法。`Pager` 从 `Formatter` 那里继承了对 `Formatting` 协议的遵循。

请注意，一个类可以在不正式采纳某个协议的情况下遵循它，只需实现该协议所声明的方法即可。

在处理复杂的应用程序时，你偶尔会发现自己写出了这样的代码：

```objc
#import "B.h"

@protocol A
- foo:(id <B>)anObject;
@end
```

而协议 `B` 则是这样声明的：

```objc
#import "A.h"

@protocol B
- bar:(id <A>)anObject;
@end
```

在这种情况下，就会出现循环依赖，两个文件都无法正确编译。要打破这种循环，你必须使用 `@protocol` 指令，对所需的协议做一个前向引用，而不是导入定义该协议的接口文件：

```objc
@protocol B;

@protocol A
- foo:(id <B>)anObject;
@end
```

请注意，以这种方式使用 `@protocol` 指令，只是告诉编译器 `B` 是一个稍后会被定义的协议。它并不会导入定义协议 `B` 的接口文件。

[下一页](Declared%20Properties.md)[上一页](Defining%20a%20Class.md)

