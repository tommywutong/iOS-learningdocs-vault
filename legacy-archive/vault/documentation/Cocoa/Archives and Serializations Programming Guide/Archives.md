---
title: 归档与序列化编程指南
apple_id: 10000047i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2012-07-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Articles/archives.html
archived_at: '2026-07-15T05:25:40.666321Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [归档与序列化编程指南](Introduction.md)


[下一页](Creating%20and%20Extracting%20Archives.md)[上一页](Object%20Graphs.md)

# 归档

归档提供了一种将对象和值转换为与体系结构无关的字节流的方式，同时保留对象和值的身份标识以及它们之间的关系。

Cocoa 归档可以保存 Objective-C 对象、标量、数组、结构体和字符串。它们无法保存那些在不同平台上实现方式各异的类型，例如 `union`、`void *`、函数指针以及长的指针链。

归档会将对象的类型信息与数据一起存储，因此从字节流中解码出的对象，通常与最初编码进字节流的对象属于同一个类。这条规则的例外情况在 [Making Substitutions During Coding](Encoding%20and%20Decoding%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2dqljzg4ydomq) 中有所描述。

对象通过编码器对象读写归档。编码器对象是抽象类 `NSCoder` 的具体子类的实例。`NSCoder` 声明了一套广泛的接口，用于将对象中存储的信息转换为适合写入文件、在进程间或跨网络传输，或执行其他类型数据交换的格式。`NSCoder` 还声明了用于反向操作的接口，即把字节流中存储的信息转换回对象。子类通过实现该接口的相应部分来支持特定的归档格式。

编码器对象通过向要编码或解码的对象发送两种[消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)之一来读写对象。创建归档时，编码器向对象发送 `encodeWithCoder:`；读取归档时，则发送 `initWithCoder:`。这两个消息由 `NSCoding` [协议](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45)定义。只有类符合 `NSCoding` 协议的对象才能被写入归档（每个 Cocoa 类的参考文档都会说明该类是否采纳了 `NSCoding` 协议）。当对象收到这两个消息之一时，该对象会向编码器发回消息，告知编码器接下来应读取或写入哪些对象或值（通常是实例变量）。在编码对象时，编码器会在归档中记录这些对象的类身份（或 Objective-C 值的类型）以及它们在层次结构中的位置。

对象图（例如 [Figure 1](Object%20Graphs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4tgljrgeytonbsfvbeeq2eijdegqi) 中展示的那样）会给编码器带来两个问题：冗余和约束。为了解决这些问题，`NSCoder` 引入了根对象和条件对象的概念，具体内容将在以下小节中描述。

对象图不一定是简单的树状结构。举例来说，两个对象可以彼此持有对方的引用，从而形成一个循环。如果编码器沿着每一条链接盲目地对遇到的每个对象进行编码，这种循环引用就会导致编码器陷入无限循环。此外，单个对象也可能被多个其他对象引用。编码器必须能够识别并处理多重引用和循环引用，以确保不会对同一个对象编码超过一次副本，同时在解码时仍能重新生成所有引用。

为了解决这个问题，`NSCoder` 引入了根对象的概念。根对象是对象图的起始点。要对一个对象图进行编码，你需要调用 `NSCoder` 的方法 `encodeRootObject:`，并传入要编码的第一个对象。在这次调用的上下文中，每一个被编码的对象都会被追踪。如果编码器被要求对同一个对象编码多次，编码器会编码一个指向首次编码的引用，而不是再次编码该对象。

`NSCoder` 本身并未实现对根对象的支持；`NSCoder` 对 `encodeRootObject:` 的实现只是简单地通过调用 `encodeObject:` 来编码对象。追踪对象的多重引用、从而保留对象图结构的责任，落在其具体子类身上。

对象图带来的另一个问题是，归档整个图并不总是合适的做法。例如，当你对一个 `NSView` 对象进行编码时，该视图可能拥有许多指向其他对象的链接：子视图、父视图、格式化器、目标、窗口、菜单等等。如果一个视图对它对这些对象的所有引用都进行编码，那么整个应用程序都会被牵连进去。不过有些对象比其他对象更重要：视图的子视图应始终被归档，但它的父视图未必需要如此。在这种情况下，父视图被视为对象图中多余的部分——一个视图可以在没有父视图的情况下存在，但不能没有子视图。然而，如果一个视图的父视图也在归档中被编码，那么该视图仍需要保留对其父视图的引用。

为了解决这个两难问题，`NSCoder` 引入了条件对象的概念。条件对象是指仅当它在对象图的其他地方被无条件编码时，才应被编码的对象。条件对象通过调用 `encodeConditionalObject:forKey:` 来编码。如果对某个对象的所有编码请求都是通过这些条件方法发出的，那么该对象将不会被编码，对它的引用在解码时会得到 `nil`。如果该对象在其他地方被编码了，那么所有的条件引用在解码时都会得到同一个已编码的对象。

通常，条件对象用于编码对对象的弱引用。

`NSCoder` 本身并未实现对条件对象的支持；`NSCoder` 对 `encodeConditionalObject:forKey:` 的实现只是简单地通过调用 `encodeObject:forKey:` 来编码对象。追踪条件对象、并且只在需要时才对对象进行编码的责任，落在其具体子类身上。

键控归档由 [NSKeyedArchiver](https://developer.apple.com/documentation/foundation/nskeyedarchiver) 对象创建，并由 [NSKeyedUnarchiver](https://developer.apple.com/documentation/foundation/nskeyedunarchiver) 对象解码。键控归档与顺序归档的不同之处在于：键控归档中编码的每个值都会被赋予一个名称，即键（key）。解码归档时，可以按名称请求这些值，从而可以按任意顺序请求，或者根本不请求某些值。这种自由度使你的类在实现向前和向后兼容性方面拥有更大的灵活性。

以下小节将描述如何使用键控归档。

对象编码到键控归档中的值，可以分别用任意字符串命名。归档是分层的，每个对象都为其编码的值定义了一个独立的命名空间，类似于该对象的实例变量。因此，键只需要在当前正在编码的对象范围内唯一即可。对象 A 用于编码其实例变量的键，不会与对象 B 所使用的键冲突，即使 A 和 B 是同一个类的实例。然而，在单个对象内部，子类使用的键可能会与其超类使用的键发生冲突。

公共类（例如某个[框架](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)中的类）如果可以被子类化，就应该在名称字符串前加上前缀，以避免与该类的子类现在或将来可能使用的键发生冲突。一个合理的前缀是类的完整名称。Cocoa 类在其键中使用前缀 “NS”，与 API 前缀相同，并且仔细确保在类层次结构中不会发生冲突。另一种可能的做法是使用框架的 bundle 标识符作为前缀字符串。

你应避免使用 “$” 作为键的前缀。键控归档器和解档器使用以 “$” 为前缀的键来存储内部值。虽然它们会检测并处理带有 “$” 前缀的用户自定义键，但这种额外开销会降低归档性能。

子类也需要在一定程度上留意超类所使用的前缀，以避免键名意外发生冲突。Cocoa 类的子类应避免让自己的键名无意中以 “NS” 开头。例如，不要将某个键命名为 “NSString search options”。

在解码时，如果你请求一个不存在的键值，解档器会根据你调用的解码方法的返回类型返回一个默认值。默认值相当于每种数据类型的零值：对象为 `nil`，布尔值为 `NO`，实数为 `0.0`，尺寸为 `NSZeroSize`，依此类推。如果你需要检测某个键值是否缺失，可以使用 `NSKeyedUnarchiver` 的实例方法 `containsValueForKey:`，如果提供的键不存在，该方法会返回 `NO`。出于性能考虑，如果默认值已经足够，应避免显式测试键是否存在。

`NSKeyedUnarchiver` 支持有限的类型强制转换。以任意整数类型编码的值（无论是标准的 `int`，还是显式的 32 位或 64 位整数）都可以使用任意整数解码方法进行解码。同样，以 `float` 或 `double` 编码的值也可以解码为 `float` 或 `double` 值。不过，将 `double` 值解码为 `float` 时，解码后的值会损失精度。如果编码的值太大，无法放入强制转换后的解码类型，解码方法会抛出 `NSRangeException`。此外，当尝试将某个值强制转换为不兼容的类型时（例如将 `int` 解码为 `float`），解码方法会抛出 `NSInvalidUnarchiveOperationException`。

在键控编码中，编码数据的版本控制不像顺序归档那样通过类版本控制来处理。事实上，对于一个类，系统不会自动进行任何版本控制；这样一来，类至少可以先查看编码的值，而不会被解档器自作主张地判定版本严重不匹配。如果一个类愿意，它可以自由决定将某种版本信息与其他值一起编码，这类信息可以是任意类型或数量。

`encodeObject:` 和 `encodeObject:forKey:` 方法能够在多个对象图中追踪对象的多重引用。可以在一个键控归档的顶层编码任意数量的对象图或值。

`NSKeyedArchiver` 实现了 `archiveRootObject:toFile:` 和 `archivedDataWithRootObject:`，用于生成只包含单个对象图的归档。不过，这类归档必须使用 `NSKeyedUnarchiver` 的 `unarchiveObjectWithFile:` 和 `unarchiveObjectWithData:` 方法进行解档。

`NSKeyedArchiver` 和 `NSKeyedUnarchiver` 对象可以拥有[委托对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)。每当一个对象被编码或解码时，委托都会收到通知。如果需要，你可以利用委托执行替换操作，用一个对象替换另一个对象。

键控归档器不必为归档中编码的每个值都提供名称。`NSKeyedArchiver` 和 `NSKeyedUnarchiver` 类实现了它们从 `NSCoder` 继承而来的非键控编码和解码方法。不建议在键控编码中使用非键控方法。

[下一页](Creating%20and%20Extracting%20Archives.md)[上一页](Object%20Graphs.md)
