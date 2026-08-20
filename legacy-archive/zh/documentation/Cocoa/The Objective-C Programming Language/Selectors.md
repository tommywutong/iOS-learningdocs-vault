---
title: Objective-C 编程语言
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocSelectors.html
archived_at: '2026-07-15T07:17:31.911439Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 编程语言](Introduction.md)


[下一页](Exception%20Handling.md)[上一页](Enabling%20Static%20Behavior.md)

# 选择器

在 Objective-C 中，_选择器（selector）_有两层含义。它既可以用来指代方法在源代码中向对象发送消息时所使用的名称，也可以指代源代码编译后用来替代该名称的那个唯一标识符。编译后的选择器属于 `SEL` 类型。所有同名的方法都拥有相同的选择器。你可以使用选择器在对象上调用某个方法——这为 Cocoa 中目标-动作（target-action）设计模式的实现提供了基础。

出于效率考虑，编译后的代码不会使用完整的 ASCII 名称作为方法选择器。相反，编译器会把每个方法名写入一张表中，然后把该名称与一个在运行时代表该方法的唯一标识符配对。运行时系统会确保每个标识符都是唯一的：任意两个选择器都不相同，且所有同名的方法都拥有相同的选择器。

编译后的选择器被赋予一种特殊的类型 `SEL`，以便与其他数据区分开来。有效的选择器永远不会是 `0`。你必须让系统来为方法分配 `SEL` 标识符；自行随意分配是徒劳的。

`@selector()` 指令让你可以引用编译后的选择器，而不是完整的方法名。这里，`setWidth:height:` 的选择器被赋给了 `setWidthHeight` 变量：

```objc
SEL setWidthHeight;
setWidthHeight = @selector(setWidth:height:);
```

在编译期用 `@selector()` 指令给 `SEL` 变量赋值是最高效的做法。但是，在某些情况下，你可能需要在运行时把一个字符串转换为选择器。你可以使用 [NSSelectorFromString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSSelectorFromString) 函数来做到这一点：

```objc
setWidthHeight = NSSelectorFromString(aBuffer);
```

反方向的转换同样是可行的。[NSStringFromSelector](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSStringFromSelector) 函数会返回某个选择器对应的方法名：

```objc
NSString *method;
method = NSStringFromSelector(setWidthHeight);
```


编译后的选择器标识的是方法名，而不是方法实现。例如，某个类的 `display` 方法与其他类中定义的 `display` 方法拥有相同的选择器。这对于多态和动态绑定而言至关重要；它让你可以把同一条消息发送给属于不同类的接收者。如果每个方法实现都对应一个独立的选择器，那么消息发送就和函数调用没有区别了。

同名的类方法和实例方法会被赋予相同的选择器。不过，由于它们各自处于不同的作用域，两者之间并不会产生混淆。一个类可以在定义 `display` 实例方法的同时，再定义一个 `display` 类方法。

消息传递机制只能通过选择器来访问方法实现，因此它会一视同仁地对待所有具有相同选择器的方法。它是从选择器中得知某个方法的返回类型及其参数的数据类型的。因此，除了发送给静态类型化接收者的消息之外，动态绑定要求所有同名方法的实现都具有相同的返回类型和相同的参数类型。（静态类型化的接收者是这条规则的例外，因为编译器可以从类的类型中得知方法实现的信息。）

尽管同名的类方法和实例方法由同一个选择器表示，但它们可以拥有不同的参数类型和返回类型。

`NSObject` 协议中定义的 `performSelector:`、`performSelector:withObject:` 和 `performSelector:withObject:withObject:` 方法，都把 `SEL` 标识符作为其第一个参数。这三个方法都会直接映射到消息传递函数。例如，

```objc
[friend performSelector:@selector(gossipAbout:)
    withObject:aNeighbor];
```

等价于：

```objc
[friend gossipAbout:aNeighbor];
```

这些方法使得在运行时改变一条消息成为可能，就像改变接收消息的对象一样。变量名可以出现在消息表达式的两个部分中：

```objc
id   helper = getTheReceiver();
SEL  request = getTheSelector();
[helper performSelector:request];
```

在这个例子中，接收者（`helper`）是在运行时（由虚构的 `getTheReceiver` 函数）选定的，而接收者被要求执行的方法（`request`）同样是在运行时（由同样是虚构的 `getTheSelector` 函数）确定的。

在处理用户界面控件方面，AppKit 很好地利用了在运行时改变接收者和消息这两者的能力。

`NSControl` 对象是可用于向应用程序发出指令的图形化设备。它们大多类似于现实世界中的控制设备，比如按钮、开关、旋钮、文本框、拨盘、菜单项等等。在软件中，这些设备位于应用程序和用户之间。它们负责解释来自键盘、鼠标等硬件设备的事件，并把它们转换成特定于应用程序的指令。例如，一个标有“查找”的按钮，会把一次鼠标点击转换成一条让应用程序开始搜索某样东西的指令。

AppKit 定义了一套用于创建控制设备的模板，并自带了若干现成的设备。例如，`NSButtonCell` 类定义了一个对象，你可以把它赋给某个 `NSMatrix` 实例，并用尺寸、标签、图片、字体和键盘快捷键来初始化它。当用户点击按钮（或使用键盘快捷键）时，`NSButtonCell` 对象会发送一条消息，指示应用程序执行某个操作。为此，`NSButtonCell` 对象在初始化时，不仅需要图像、尺寸和标签，还需要有关“该发送什么消息、发送给谁”的指示。因此，`NSButtonCell` 实例可以被初始化一个动作消息（也就是它在发送消息时应使用的方法选择器）和一个目标（应该接收该消息的对象）。

```objc
[myButtonCell setAction:@selector(reapTheWind:)];
[myButtonCell setTarget:anObject];
```

当用户点击相应的按钮时，按钮单元格会使用 `NSObject` 协议中的 `performSelector:withObject:` 方法来发送这条消息。所有动作消息都只带一个参数，也就是发送该消息的控制设备的 `id`。

如果 Objective-C 不允许改变消息，那么所有 `NSButtonCell` 对象就都得发送同一条消息；方法的名称就会被固定在 `NSButtonCell` 的源代码中。这样一来，按钮单元格和其他控件就不能只是简单地实现一套把用户操作转换为动作消息的机制，而必须限定消息的内容。受限的消息传递会使得任何对象都难以响应一个以上的按钮单元格。要么每个按钮都得对应一个目标，要么目标对象就得自行判断消息来自哪个按钮，再据此采取行动。每当你重新排布用户界面时，都得重新实现响应该动作消息的方法。缺少动态消息传递会带来不必要的复杂性，而这正是 Objective-C 欣然避免的。

如果一个对象收到一条要求它执行某个不在其方法列表中的方法的消息，就会产生错误。这与调用一个不存在的函数属于同一类错误。但是，由于消息传递发生在运行时，这个错误往往要等到程序执行时才会显现出来。

当消息的选择器是固定的、且接收对象的类是已知的时，避免这种错误相对容易。在编写程序时，你可以确保接收者能够作出响应。如果接收者是静态类型化的，编译器会替你完成这项检查。

不过，如果消息的选择器或接收者的类是可变的，就可能需要把这项检查推迟到运行时。`NSObject` 类中定义的 `respondsToSelector:` 方法，用于测试某个接收者能否响应一条消息。它接受方法选择器作为参数，并返回接收者是否能访问与该选择器匹配的方法：

```objc
if ( [anObject respondsToSelector:@selector(setOrigin::)] )
    [anObject setOrigin:0.0 :0.0];
else
    fprintf(stderr, "%s can’t be placed\n",
        [NSStringFromClass([anObject class]) UTF8String]);
```

当你向那些在编译期无法控制的对象发送消息时，`respondsToSelector:` 这项运行时测试就显得尤为重要。例如，如果你编写的代码要向一个可以由他人设置的变量所代表的对象发送消息，就应该确保接收者实现了能够响应该消息的方法。

[下一页](Exception%20Handling.md)[上一页](Enabling%20Static%20Behavior.md)

