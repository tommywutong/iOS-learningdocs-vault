---
title: Cocoa 编码规范
apple_id: 10000146i
resource_type: Guide
platform: watchOS|iOS|macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CodingGuidelines/Articles/FrameworkImpl.html
archived_at: '2026-07-15T07:13:26.285971Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Cocoa 编码规范](Introduction%20to%20Coding%20Guidelines%20for%20Cocoa.md)


[下一页](Document%20Revision%20History.md)[上一页](Acceptable%20Abbreviations%20and%20Acronyms.md)

# 框架开发者的提示与技巧

[框架](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)的开发者在写代码时必须比其他开发者更加小心。可能有许多客户端应用程序链接了他们的框架，正因为影响面这么广，框架中的任何缺陷都可能在整个系统中被放大。下面几节讨论一些编程技巧，你可以采用它们来保证框架的效率和完整性。

以下建议与推荐做法涵盖框架的初始化。

`initialize` [类方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassMethod.html#//apple_ref/doc/uid/TP40008195-CH8)给了你一个位置，让某段代码在该类的任何其他方法被调用之前，以延迟的方式执行一次。它通常用来设置类的版本号（参见[版本管理与兼容性](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dmljrgaydcnzxg4)）。

运行时会向继承链上的每一个类发送 `initialize`，即使某个类并没有实现它也一样；因此一个类的 `initialize` 方法可能被调用不止一次（例如，当某个子类没有实现它时）。通常你希望初始化代码只执行一次。确保这一点的一种办法是使用 `dispatch_once()`：

```objc
+ (void)initialize {
    static dispatch_once_t onceToken = 0;
    dispatch_once(&onceToken, ^{
        // 初始化代码
    }
}
```

你绝不应该显式地调用 `initialize` 方法。如果需要触发初始化，可以调用某个无副作用的方法，例如：

```objc
[NSImage self];
```


指定初始化方法（designated initializer）是类中调用了超类某个 `init` 方法的那个 `init` 方法。（其他初始化方法调用的是本类定义的 `init` 方法。）每个公开的类都应当有一个或多个指定初始化方法。指定初始化方法的例子有 `NSView` 的 `initWithFrame:` 和 `NSResponder` 的 `init` 方法。如果 `init` 方法本来就不打算被[覆写](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57)，就像 `NSString` 以及其他作为[类簇](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassCluster.html#//apple_ref/doc/uid/TP40008195-CH7)门面的抽象类那样，那么子类就应当自己实现一个。

指定初始化方法应当被清楚地标识出来，因为这个信息对那些想为你的类派生子类的人很重要。子类只需覆写指定初始化方法，其他所有初始化方法就都能按设计正常工作。

当你实现框架中的某个类时，往往还得实现它的[归档](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Archiving.html#//apple_ref/doc/uid/TP40008195-CH1)方法：`initWithCoder:` 和 `encodeWithCoder:`。注意不要在初始化的代码路径中做那些对象在解归档时不会做的事情。要做到这一点，一个好办法是：如果你的类实现了归档，就从指定初始化方法和 `initWithCoder:`（它本身也是一个指定初始化方法）中调用同一个公共例程。

一个设计良好的初始化方法应当完成以下步骤，以确保错误被正确地检测和传播：

1. 通过调用 `super` 的[指定初始化方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)来给 self 重新赋值。
2. 检查返回值是否为 `nil`，`nil` 表示超类初始化过程中出了某种错误。
3. 如果在初始化当前类时发生错误，就释放该对象并返回 `nil`。

[清单 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dmljrgaydimbshawueqkkijfegskb) 演示了具体做法。

__清单 1__  初始化过程中的错误检测

```objc
- (id)init {
    self = [super init];  // 在这里调用一个指定初始化方法。
    if (self != nil) {
        // 初始化对象  ...
        if (someError) {
            [self release];
            self = nil;
        }
    }
    return self;
}
```


当你向[框架](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)中添加新的类或方法时，通常不必为每一组新功能指定新的版本号。开发者一般会（也应该）执行 [Objective-C](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectiveC.html#//apple_ref/doc/uid/TP40008195-CH43) 运行时检查，比如 `respondsToSelector:`，来判断某个特性在给定系统上是否可用。这类运行时检测是检查新特性的首选方式，也是最具动态性的方式。

不过，你可以采用若干技巧，确保框架的每个新版本都被恰当地标记，并尽可能与早期版本保持兼容。

当某个新特性或缺陷修复无法通过运行时检测轻易察觉时，你应当为开发者提供某种手段来检查这一变更。做到这一点的一种办法是存储框架的确切版本号，并让开发者能够访问到它：

- 把该变更（例如在发行说明中）记录在某个版本号之下。
- 设置框架的当前版本号，并提供某种全局可访问的方式。你可以把版本号存放在框架的信息[属性列表](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44)（`Info.plist`）中，然后从那里读取它。

如果你框架中的对象需要被写入 [nib 文件](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34)，它们就必须能够归档自身。对于任何使用归档机制来存储文档数据的文档，你同样需要把它们归档。

关于归档，你应当考虑以下问题：

- 如果归档中缺少某个键，那么请求它的值时会返回 `nil`、`NULL`、`NO`、0 或 0.0，具体取决于所请求的类型。可以检测这个返回值，从而减少需要写出的数据量。此外，你还可以查明某个键是否被写入了归档。
- 编码方法和解码方法都可以做一些事情来保证向后兼容。举例来说，某个类的新版本的编码方法可以用键写出新的值，但同时仍然写出旧的字段，好让该类的旧版本依然能够理解这个对象。此外，解码方法可能希望以某种合理的方式处理缺失的值，从而为将来的版本保留一定的灵活性。
- 对于框架类的归档键，推荐的命名[规范](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/CodingConventions.html#//apple_ref/doc/uid/TP40008195-CH53)是：以框架其他 API 元素所用的前缀开头，后面接实例变量的名称。只要确保这些名称不会与任何超类或子类中的名称冲突即可。
- 如果你有一个写出基本数据类型（换句话说，值不是对象）的工具函数，一定要使用唯一的键。例如，一个归档矩形的“archiveRect”例程应当接受一个键参数，然后要么直接使用给定的键，要么——如果它要写出多个值（比如四个 float）——就在给定的键后面追加它自己独有的一小段内容。
- 由于存在编译器依赖和字节序依赖，原样归档位域是危险的。只有当出于性能考虑，确实需要多次写出大量位时，才应该归档它们。相关建议参见[位域](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dmljrgaydkojvga)。

大多数 [Cocoa](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9) 框架方法并不强制开发者去捕获和处理[异常](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ExceptionHandling.html#//apple_ref/doc/uid/TP40008195-CH18)。这是因为异常并不是正常执行流程的一部分，也通常不用来传达可预期的运行时错误或用户错误。这类错误的例子包括：

- 文件未找到
- 没有这个用户
- 试图在应用程序中打开类型不正确的文档
- 把字符串转换为指定编码时出错

不过，Cocoa 确实会抛出异常来表示编程错误或逻辑错误，例如：

- 数组下标越界
- 试图修改不可变对象
- 参数类型错误

这里的预期是：开发者会在测试期间发现这类错误，并在应用程序发布之前解决它们；因此应用程序在运行时不需要处理这些异常。如果某个异常被抛出而应用程序的任何部分都没有捕获它，顶层的默认处理器通常会捕获并报告这个异常，然后程序继续执行。开发者可以选择用自己的处理器替换这个默认的异常捕获器，让它给出关于出错原因的更多细节，并提供保存数据并退出应用程序的选项。

错误是 Cocoa 框架与某些其他软件库不同的另一个方面。Cocoa 方法一般不返回错误码。当出错的合理原因或可能原因只有一个时，这些方法依赖于对返回的布尔值或对象（`nil`／非 `nil`）做一次简单的判断；返回 `NO` 或 `nil` 的原因会写在文档里。你不应该用错误码来表示那些需要在运行时处理的编程错误，而应该抛出异常，或者在某些情况下只是把错误记录下来而不抛出异常。

举例来说，`NSDictionary` 的 `objectForKey:` 方法要么返回找到的对象，要么在找不到时返回 `nil`。`NSArray` 的 `objectAtIndex:` 方法则永远不会返回 `nil`（除非按照更高优先级的通用语言约定，任何发送给 `nil` 的消息都返回 `nil`），因为 `NSArray` 对象不能存储 `nil` 值，而且按定义任何越界访问都是编程错误，应当导致抛出异常。许多 `init` 方法在无法用给定参数完成初始化时会返回 `nil`。

在少数确实需要多个不同错误码的情况下，方法应当通过一个引用型参数来给出它们，该参数返回一个错误码、一个本地化的错误字符串，或其他描述该错误的信息。比如说，你可能想把错误作为 `NSError` 对象返回；细节请查看 Foundation 中的 `NSError.h` 头文件。这个参数可以作为直接返回的、更简单的 `BOOL` 或 `nil` 之外的补充。该方法还应当遵守这样一条约定：所有引用型参数都是可选的，因此如果调用方不关心错误，就允许它为错误码参数传入 `NULL`。

你如何处理框架数据，会影响性能、跨平台兼容性等诸多方面。本节讨论与框架数据有关的技巧。

出于性能考虑，尽可能把框架数据标记为常量是有好处的，因为这样可以减小 Mach-O 二进制文件中 `__DATA` 段的大小。非 `const` 的全局数据和静态数据最终会落在 `__DATA` 段的 `__DATA` 节中。这类数据在每个用到该框架的运行中的应用程序实例里都要占用内存。虽然多出（比方说）500 字节看起来不算什么，但它可能导致所需页数增加——也就是每个应用程序多出四千字节。

任何常量数据你都应当标记为 `const`。如果这块数据中没有 `char *` 指针，这样做会让数据落到 `__TEXT` 段（这才是真正意义上的常量）；否则它仍会留在 `__DATA` 段，但不会被写入（除非没有做预绑定，或者因为加载时必须滑动二进制文件而破坏了预绑定）。

你应当初始化静态变量，以确保它们被并入 `__DATA` 段的 `__data` 节，而不是 `__bss` 节。如果没有明显合适的初始值，就用 0、`NULL`、0.0 或任何恰当的值。

给位域使用有符号类型（尤其是一位的位域）时，如果代码假定其值是布尔值，就可能导致未定义行为。一位的位域应当始终是无符号的。由于这样的位域中只能存放 0 和 -1（取决于编译器的实现），把它与 1 比较的结果为假。例如，如果你在代码里遇到这样的写法：

```objc
BOOL isAttachment:1;
int startTracking:1;
```

你应当把类型改为 `unsigned int`。

位域的另一个问题是归档。一般来说，你不应该把位域原样写入磁盘或归档，因为在另一种架构上、或者用另一个编译器读回时，格式可能不同。

在框架代码中，最好的做法是尽量完全避免分配内存。如果你出于某种原因需要一个临时缓冲区，通常用栈比分配缓冲区更好。不过栈的大小有限（通常总共 512 千字节），所以要不要用栈取决于具体的函数和你所需缓冲区的大小。一般来说，如果缓冲区大小在 1000 字节（或 `MAXPATHLEN`）以内，用栈是可以接受的。

一种改进做法是：先用栈，一旦大小需求超过栈缓冲区的容量就改用 `malloc` 分配的缓冲区。[清单 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dmljrgaydqnzvgqwueqkkjbcumq2f) 给出了一段正是这样做的代码：

__清单 2__  同时使用栈和 malloc 缓冲区进行分配

```c
#define STACKBUFSIZE (1000 / sizeof(YourElementType))
 YourElementType stackBuffer[STACKBUFSIZE];
 YourElementType *buf = stackBuffer;
 int capacity = STACKBUFSIZE;  // 以 YourElementType 为单位
 int numElements = 0;  // 以 YourElementType 为单位

while (1) {
    if (numElements > capacity) {  // 需要更多空间
        int newCapacity = capacity * 2;  // 或者换成你自己的增长算法
        if (buf == stackBuffer) {  // 之前用的是栈；切换到分配的内存
            buf = malloc(newCapacity * sizeof(YourElementType));
            memmove(buf, stackBuffer, capacity * sizeof(YourElementType));
        } else {  // 已经在用 malloc 了；直接 realloc
            buf = realloc(buf, newCapacity * sizeof(YourElementType));
        }
        capacity = newCapacity;
    }
    // ... 使用 buf；递增 numElements ...
  }
  // ...
  if (buf != stackBuffer) free(buf);
```


你应当注意通用[对象比较](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectComparison.html#//apple_ref/doc/uid/TP40008195-CH37)方法 `isEqual:` 与那些与具体对象类型关联的比较方法（比如 `isEqualToString:`）之间的一个重要区别。`isEqual:` 方法允许你传入任意对象作为参数，如果两个对象不是同一个类就返回 `NO`。而 `isEqualToString:`、`isEqualToArray:` 这类方法通常假定参数就是指定的类型（也就是接收者的类型）。因此它们不做类型检查，于是速度更快，但没那么安全。对于从外部来源取得的值，比如应用程序的信息[属性列表](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44)（`Info.plist`）或偏好设置，更推荐使用 `isEqual:`，因为它更安全；当类型已知时，则改用 `isEqualToString:`。

关于 `isEqual:` 还有一点，就是它与 `hash` 方法的关联。对于放入基于哈希的 Cocoa [集合](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10)（如 `NSDictionary` 或 `NSSet`）中的对象，有一条基本的不变式：如果 `[A isEqual:B] == YES`，那么 `[A hash] == [B hash]`。所以如果你在自己的类中覆写了 `isEqual:`，就也应当覆写 `hash` 以维持这条不变式。默认情况下，`isEqual:` 比较的是各个对象地址的指针相等性，而 `hash` 返回的哈希值也基于各个对象的地址，因此这条不变式是成立的。

[下一页](Document%20Revision%20History.md)[上一页](Acceptable%20Abbreviations%20and%20Acronyms.md)

