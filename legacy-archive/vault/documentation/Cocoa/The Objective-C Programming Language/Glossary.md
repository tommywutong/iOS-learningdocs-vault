---
title: Objective-C 编程语言
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocGlossary.html
archived_at: '2026-07-15T07:17:30.401070Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 编程语言](Introduction.md)


[上一页](Document%20Revision%20History.md)

# 术语表

- __abstract class__

  仅仅是为了让其他类可以从中继承而定义的类。程序不会使用抽象类的实例，只使用其子类的实例。

- __abstract superclass__

  与 [abstract class](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqnjnijauur2iivcee) 相同。

- __adopt__

  在 Objective-C 语言中，如果一个类声明自己实现了某个协议中的全部方法，就称该类采用（adopt）了这个协议。协议的采用方式是在类或分类声明中，把协议名称列在尖括号之间。

- __anonymous object__

  类未知的对象。匿名对象的接口通过协议声明来公开。

- __AppKit__

  有时也称为 _Application Kit_。一个实现应用程序用户界面的 Cocoa 框架。AppKit 为在屏幕上绘制内容并响应事件的应用程序提供了基本的程序结构。

- __asynchronous message__

  一种远程消息，它会立即返回，而不等待接收该消息的应用程序做出响应。发送方应用程序和接收方应用程序各自独立运作，因此不同步。与 [synchronous message](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqnjnijauurcki5feo) 相对。

- __category__

  在 Objective-C 语言中，一组与类定义其余部分分离开的方法定义。分类可用于把一个类定义拆分成多个部分，或者为一个已有的类添加方法。

- __class__

  在 Objective-C 语言中，某一类对象的原型。类定义声明了实例变量，并为该类的所有成员定义了方法。具有相同类型实例变量、并可以访问相同方法的对象属于同一个类。另请参见 [class object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqnjnijauurceinbeo)。

- __class method__

  在 Objective-C 语言中，一种可以对类对象（而非该类的实例）进行操作的方法。

- __class object__

  在 Objective-C 语言中，代表一个类、并且知道如何创建该类新实例的对象。类对象由编译器创建，没有实例变量，也不能被静态类型化，但在其他方面的行为与所有其他对象相同。在消息表达式中作为接收者时，类对象由类名来表示。

- __Cocoa__

  OS X 中的一个先进的面向对象开发平台。Cocoa 是一组框架的集合，其主要编程接口都是用 Objective-C 编写的。

- __compile time__

  源代码被编译的时刻。编译时所做的决定，受限于源文件中所编码信息的数量和种类。

- __conform__

  在 Objective-C 语言中，如果一个类（或其超类）实现了某协议中声明的方法，就称该类遵循（conform to）这个协议。如果一个实例所属的类遵循某协议，那么该实例也遵循这个协议。因此，遵循某协议的实例可以执行该协议中声明的任何实例方法。

- __delegate__

  代表另一个对象行事的对象。

- __designated initializer__

  对初始化某个类的新实例负有主要责任的 `init...` 方法。每个类都会定义或继承自己的指定初始化方法。同一个类中的其他 `init...` 方法通过向 `self` 发消息，直接或间接调用该指定初始化方法；而指定初始化方法本身则通过向 `super` 发消息，调用其超类的指定初始化方法。

- __dispatch table__

  Objective-C 运行时中的一张表，其中的条目把方法选择器与它们所标识方法的、特定于类的地址关联起来。

- __distributed objects__

  一种便于不同地址空间中的对象之间进行通信的体系结构。

- __dynamic allocation__

  一种基于 C 的语言所使用的技术：由操作系统在运行中的应用程序需要内存时提供内存，而不是在应用程序启动时一次性分配。

- __dynamic binding__

  在运行时（而不是编译时）把方法绑定到消息上——也就是说，在响应消息时才去查找应当调用的方法实现。

- __dynamic typing__

  在运行时（而不是编译时）才确定一个对象所属的类。

- __encapsulation__

  一种编程技术，它把某个操作的实现细节隐藏在一个抽象接口背后，不让使用者看到。它使得实现可以被更新或更改，而不会影响接口的使用者。

- __event__

  外部活动（尤其是用户在键盘和鼠标上的操作）的直接或间接报告。

- __factory__

  与 [class object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqnjnijauurceinbeo) 相同。

- __factory object__

  与 [class object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqnjnijauurceinbeo) 相同。

- __formal protocol__

  在 Objective-C 语言中，用 `@protocol` 指令声明的协议。类可以采用正式协议，对象在运行时可以响应"是否遵循某个正式协议"的询问，实例也可以按其所遵循的正式协议来指定类型。

- __framework__

  一种打包方式，把一组逻辑上相关的类、协议和函数，连同本地化字符串、在线文档以及其他相关文件打包在一起。Cocoa 提供了 Foundation 框架和 AppKit 框架等。

- __id__

  在 Objective-C 语言中，不区分具体类的、任意一种对象的通用类型。`id` 被定义为指向对象数据结构的指针。它既可以用于类对象，也可以用于类的实例。

- __implementation__

  Objective-C 类规范中定义公开方法（在类接口中声明的方法）以及私有方法（未在类接口中声明的方法）的部分。

- __informal protocol__

  在 Objective-C 语言中，以分类形式声明的协议，通常是作为 `NSObject` 类的分类。该语言对正式协议提供了明确的支持，但对非正式协议没有。

- __inheritance__

  在面向对象编程中，超类把自身特性（方法和实例变量）传递给其子类的能力。

- __inheritance hierarchy__

  在面向对象编程中，由超类和子类的排列所定义的类层次结构。每个类（根类如 `NSObject` 除外）都有一个超类，任何类都可以拥有数量不限的子类。每个类都通过其超类，从层次结构中位于它上方的类继承而来。

- __instance__

  在 Objective-C 语言中，属于（是其成员的）某个特定类的对象。实例是在运行时根据类定义中的规范创建的。

- __instance method__

  在 Objective-C 语言中，可供类的实例（而非类对象）使用的方法。

- __instance variable__

  在 Objective-C 语言中，属于实例内部数据结构一部分的变量。实例变量在类定义中声明，并成为该类所有成员对象、以及继承自该类的对象的一部分。

- __interface__

  Objective-C 类规范中声明其公开接口的部分，其中包括超类名称、实例变量以及公开方法的原型。

- __Interface Builder__

  一个让你以图形化方式指定应用程序用户界面的工具。它会为你建立相应的对象，并让你在需要时轻松地在这些对象与你自己的代码之间建立连接。

- __link time__

  由不同源模块编译出的文件被链接成单一程序的时刻。链接器所做的决定，受限于已编译的代码，并最终受限于源代码中包含的信息。

- __message__

  在面向对象编程中，方法选择器（名称）及其附带的参数，它们告诉消息表达式中的接收对象应当做什么。

- __message expression__

  在面向对象编程中，向某个对象发送消息的表达式。在 Objective-C 语言中，消息表达式用方括号括起来，由一个接收者和随后的消息（方法选择器和参数）组成。

- __method__

  在面向对象编程中，可由某个对象执行的一段过程。

- __mutex__

  _mutual exclusion semaphore_（互斥信号量）的简称。用于同步线程执行的对象。

- __namespace__

  程序中的一个逻辑子区划，在其内部所有名称都必须唯一。一个命名空间中的符号不会与另一个命名空间中同名的符号冲突。例如，在 Objective-C 中，一个类的实例方法拥有该类专属的命名空间。类似地，一个类的类方法拥有自己的命名空间，一个类的实例变量也拥有自己的命名空间。

- __nil__

  在 Objective-C 语言中，值为 0 的对象 `id`。

- __object__

  一种编程单元，把数据结构（实例变量）与可以使用或影响该数据的操作（方法）组合在一起。对象是面向对象程序的主要构成模块。

- __outlet__

  指向另一个对象的实例变量。outlet 实例变量是一种方式，让对象记录它可能需要发送消息的其他对象。

- __polymorphism__

  在面向对象编程中，不同对象各自以自己的方式响应同一消息的能力。

- __procedural programming language__

  一种诸如 C 这样的语言，它把程序组织成一组有明确起止的过程。

- __protocol__

  在 Objective-C 语言中，一组不与任何特定类关联的方法声明。另请参见 [formal protocol](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqnjnijauurshinduq)、[informal protocol](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqnjnijauuqsjizeuq)。

- __receiver__

  在面向对象编程中，被发送消息的那个对象。

- __reference counting__

  一种内存管理技术：每个声明拥有某对象所有权的实体都会递增该对象的引用计数，之后再递减。当对象的引用计数归零时，该对象就会被释放。这项技术使得一个对象的实例可以安全地被多个其他对象共享。

- __remote message__

  从一个应用程序发送到另一个应用程序中某个对象的消息。

- __remote object__

  另一个应用程序中的对象，是远程消息的潜在接收者。

- __runtime__

  程序启动之后、运行期间的这段时间。运行时所做的决定，可能受到用户所做选择的影响。

- __selector__

  在 Objective-C 语言中，方法在源代码中向对象发送消息时所使用的名称，或者源代码编译后取代该名称的唯一标识符。已编译的选择器类型为 `SEL`。

- __static typing__

  在 Objective-C 语言中，通过把某个实例声明为指向某个类的指针，向编译器提供该实例属于哪种对象的信息。

- __subclass__

  在 Objective-C 语言中，在继承层次结构中恰好位于另一个类下方一级的任何类。有时也在更宽泛的意义上，泛指从另一个类继承而来的任何类。也用作动词，表示定义某个类的子类这一过程。

- __superclass__

  在 Objective-C 语言中，在继承层次结构中恰好位于另一个类上方一级的类；子类正是通过它继承方法和实例变量。

- __synchronous message__

  一种远程消息，接收方应用程序完成对该消息的响应之前不会返回。因为发送消息的应用程序会等待接收方应用程序的确认或返回信息，所以两个应用程序保持同步。与 [asynchronous message](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqnjnijauursjirceo) 相对。

[上一页](Document%20Revision%20History.md)

