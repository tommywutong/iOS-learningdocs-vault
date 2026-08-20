---
title: Cocoa 编码规范
apple_id: 10000146i
resource_type: Guide
platform: watchOS|iOS|macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CodingGuidelines/Articles/NamingIvarsAndTypes.html
archived_at: '2026-07-15T07:13:27.784598Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Cocoa 编码规范](Introduction%20to%20Coding%20Guidelines%20for%20Cocoa.md)


[下一页](Acceptable%20Abbreviations%20and%20Acronyms.md)[上一页](Naming%20Functions.md)

# 属性与数据类型命名

本节介绍声明属性、实例变量、常量、[通知](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35)和[异常](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ExceptionHandling.html#//apple_ref/doc/uid/TP40008195-CH18)的命名[规范](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/CodingConventions.html#//apple_ref/doc/uid/TP40008195-CH53)。

[声明属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)（declared property）实际上就是为某个属性声明了存取方法（accessor），因此声明属性的命名规范大体上与存取方法的命名规范相同（参见[存取方法](Naming%20Methods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4deljrgaydimrqgi)）。如果属性用名词或动词表达，形式为：

`@property (…)` _type_ _nounOrVerb_;

例如：

```objc
@property (strong) NSString *title;
@property (assign) BOOL showsAlpha;
```

不过，如果声明属性的名称是用形容词表达的，那么属性名要去掉“is”前缀，但要另行指定取值方法（getter）的惯用名称，例如：

```objc
@property (assign, getter=isEditable) BOOL editable;
```

很多情况下，在使用声明属性的同时你也会合成一个与之对应的实例变量。

要确保实例变量的名称能简洁地描述它所存储的属性。通常你不应该直接访问实例变量，而应该使用[存取方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AccessorMethod.html#//apple_ref/doc/uid/TP40008195-CH2)（在 `init` 和 `dealloc` 方法中确实要直接访问实例变量）。为了体现这一点，实例变量名要加下划线（`_`）前缀，例如：

```objc
@implementation MyClass {
    BOOL _showsTitle;
}
```

如果你是通过声明属性来合成实例变量的，就在 `@synthesize` 语句中指定实例变量的名称。

```objc
@implementation MyClass
@synthesize showsTitle=_showsTitle;
```

给类添加实例变量时，有几点需要留意：

- 避免显式声明公开的实例变量。

  开发者应当关心对象的接口，而不是它如何存储数据的细节。你可以用声明属性并合成对应的实例变量的方式，来避免显式声明实例变量。
- 如果确实需要声明实例变量，就用 `@private` 或 `@protected` 显式地声明它。

  如果你预计自己的类会被派生子类，而且这些子类需要直接访问数据，那就使用 `@protected` 指令。
- 如果某个实例变量要作为该类实例的一个可访问属性，就要确保为它编写[存取方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AccessorMethod.html#//apple_ref/doc/uid/TP40008195-CH2)（条件允许时使用声明属性）。

常量的命名规则视常量的创建方式而定。

- 对于一组取整数值的相关常量，使用枚举。
- 枚举常量_以及_归拢它们的 typedef 都遵循函数的命名规范（参见[函数命名](Naming%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dglkciffeor2difca)）。下面的例子出自 `NSMatrix.h`：

```c
typedef enum _NSMatrixMode {
    NSRadioModeMatrix           = 0,
    NSHighlightModeMatrix       = 1,
    NSListModeMatrix            = 2,
    NSTrackModeMatrix           = 3
} NSMatrixMode;
```

  注意，其中的 `typedef` 标签（上例中的 `_NSMatrixMode`）并非必需。
- 对于位掩码之类的东西，你可以创建匿名枚举，例如：

```c
enum {
    NSBorderlessWindowMask      = 0,
    NSTitledWindowMask          = 1 << 0,
    NSClosableWindowMask        = 1 << 1,
    NSMiniaturizableWindowMask  = 1 << 2,
    NSResizableWindowMask       = 1 << 3

};
```


- 用 `const` 为浮点值创建常量。如果某个整数常量与其他常量无关，也可以用 `const` 来创建它；否则请使用枚举。
- `const` 常量的格式可参考下面这个声明：

```c
const float NSLightGray;
```

  和枚举常量一样，其命名规范与函数相同（参见[函数命名](Naming%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dglkciffeor2difca)）。

- 一般来说，不要用 `#define` 预处理命令来创建常量。整数常量请用枚举，浮点常量请用上面说的 `const` 限定符。
- 对于那些由预处理器求值、用于判断某段代码是否参与编译的符号，请使用大写字母。例如：

```c
#ifdef DEBUG
```
- 注意，由编译器定义的宏，其名称前后都带有双下划线。例如：

```c
__MACH__
```
- 对于用作通知名称、字典键之类用途的字符串，要为它们定义常量。使用字符串常量可以确保编译器验证所指定的值是否正确（也就是说，它会帮你查拼写错误）。[Cocoa](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9)  [框架](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)提供了大量字符串常量的例子，比如：

```objc
APPKIT_EXTERN NSString *NSPrintCopies;
```

  实际的 NSString 值是在实现文件中赋给这个常量的。（注意，对 [Objective-C](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectiveC.html#//apple_ref/doc/uid/TP40008195-CH43) 而言，`APPKIT_EXTERN` 宏会展开为 `extern`。）

[通知](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35)和[异常](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ExceptionHandling.html#//apple_ref/doc/uid/TP40008195-CH18)的命名规则类似。但两者各有自己推荐的用法模式。

如果一个类有[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)（delegate），它的大部分通知很可能是委托通过某个已定义的委托方法接收到的。这些通知的名称应当与对应的委托方法相呼应。例如，全局 `NSApplication` 对象的委托会自动注册，以便在应用程序发布 `NSApplicationDidBecomeActiveNotification` 时收到 `applicationDidBecomeActive:` 消息。

通知由全局的 `NSString` 对象来标识，其名称按如下方式组成：

```
[Name of associated class] + [Did | Will] + [UniquePartOfName] + Notification
```

例如：

```
NSApplicationDidBecomeActiveNotification
NSWindowDidMiniaturizeNotification
NSTextViewDidChangeSelectionNotification
NSColorPanelColorDidChangeNotification
```


尽管你可以出于任何目的使用异常（也就是 `NSException` 类及相关函数提供的机制），但 Cocoa 把异常保留给编程错误使用，比如数组下标越界。Cocoa _不_ 用异常来处理常规的、可预期的错误情况。对于这类情况，请使用 `nil`、`NULL`、`NO` 之类的返回值或错误码。更多细节参见 _[错误处理编程指南](../Error%20Handling%20Programming%20Guide/Introduction%20to%20Error%20Handling%20Programming%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbw)_。

异常由全局的 `NSString` 对象来标识，其名称按如下方式组成：

```
[Prefix] + [UniquePartOfName] + Exception
```

名称中独特的那部分应当把各个单词连写在一起，并把每个单词的首字母大写。以下是一些例子：

```
NSColorListIOException
NSColorListNotEditableException
NSDraggingException
NSFontUnavailableException
NSIllegalSelectorException
```

[下一页](Acceptable%20Abbreviations%20and%20Acronyms.md)[上一页](Naming%20Functions.md)

