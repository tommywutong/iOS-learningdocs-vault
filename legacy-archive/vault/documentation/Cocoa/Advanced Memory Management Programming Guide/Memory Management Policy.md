---
title: 高级内存管理编程指南
apple_id: 10000011i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Performance
technology: Foundation
published: '2012-07-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmRules.html
archived_at: '2026-07-15T07:16:41.041691Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [高级内存管理编程指南](About%20Memory%20Management.md)


[下一页](Practical%20Memory%20Management.md)[上一页](About%20Memory%20Management.md)

# 内存管理策略

在引用计数环境中，内存管理所使用的基本模型由 [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intf/NSObject)  [协议](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45)中定义的一组方法与一套标准的方法命名约定共同提供。`NSObject` 类还定义了一个方法 `dealloc`，它会在对象被释放时自动调用。本文介绍在 Cocoa 程序中正确管理内存所需了解的全部基本规则，并给出一些正确用法的示例。

内存管理模型建立在对象所有权的基础之上。任何对象都可以有一个或多个拥有者。只要一个对象至少还有一个拥有者，它就会继续存在。如果一个对象没有任何拥有者，运行时系统就会自动销毁它。为了明确区分你何时拥有一个对象、何时不拥有，Cocoa 制定了如下策略：

- __你拥有你创建的任何对象__

  你使用名称以 “alloc”、“new”、“copy” 或 “mutableCopy” 开头的方法来创建对象（例如 [alloc](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/alloc)、[newObject](https://developer.apple.com/documentation/appkit/nsobjectcontroller/1535921-newobject) 或 [mutableCopy](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/mutableCopy)）。
- __你可以使用 retain 取得一个对象的所有权__

  一般来说，接收到的对象在接收它的那个方法内部保证保持有效，并且该方法也可以安全地把这个对象返回给它的调用者。你会在两种情况下使用 `retain`：（1）在存取方法（accessor）或 `init` 方法的实现中，取得某个你想作为属性值存储起来的对象的所有权；（2）防止某个对象因为其他操作的副作用而失效（详见[避免让你正在使用的对象被释放](Practical%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga2dgljrgaydaojsgi)）。
- __当你不再需要某个你拥有的对象时，你必须放弃它的所有权__

  你通过向对象发送 [release](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/release) 消息或 [autorelease](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/autorelease) 消息来放弃它的所有权。因此在 Cocoa 的术语中，放弃一个对象的所有权通常被称为“释放”（releasing）该对象。
- __你不能放弃一个你并不拥有的对象的所有权__

  这只是前面几条策略规则的一个推论，在此明确写出来。

为了说明这套策略，来看下面这段代码：

```objc
{
    Person *aPerson = [[Person alloc] init];
    // ...
    NSString *name = aPerson.fullName;
    // ...
    [aPerson release];
}
```

这个 Person 对象是用 `alloc` 方法创建的，所以在不再需要它时，随后要向它发送 `release` 消息。而这个人的姓名并不是通过任何一个具有所有权的方法取得的，所以不需要向它发送 `release` 消息。不过请注意，这个例子用的是 `release` 而不是 `autorelease`。

当你需要发送一条延迟的 `release` 消息时（典型场景是从方法中返回一个对象时），就使用 `autorelease`。例如，你可以像下面这样实现 `fullName` 方法：

```objc
- (NSString *)fullName {
    NSString *string = [[[NSString alloc] initWithFormat:@"%@ %@",
                                          self.firstName, self.lastName] autorelease];
    return string;
}
```

你拥有 `alloc` 返回的这个字符串。为了遵守内存管理规则，你必须在失去对它的引用之前放弃它的所有权。但如果你使用 `release`，这个字符串会在返回之前就被释放（于是该方法返回的将是一个无效对象）。使用 `autorelease` 则表示你想放弃所有权，同时又让方法的调用者能够在该字符串被释放之前使用它。

你也可以像下面这样实现 `fullName` 方法：

```objc
- (NSString *)fullName {
    NSString *string = [NSString stringWithFormat:@"%@ %@",
                                 self.firstName, self.lastName];
    return string;
}
```

按照基本规则，你并不拥有 `stringWithFormat:` 返回的字符串，所以可以安全地把这个字符串从方法中返回。

作为对照，_下面这种实现是错误的_：

```objc
- (NSString *)fullName {
    NSString *string = [[NSString alloc] initWithFormat:@"%@ %@",
                                         self.firstName, self.lastName];
    return string;
}
```

按照命名约定，没有任何迹象表明 `fullName` 方法的调用者拥有返回的字符串。因此调用者没有理由去释放这个返回的字符串，于是它就会被泄漏。

Cocoa 中有些方法规定通过引用返回对象（也就是说，它们接受类型为 `ClassName **` 或 `id *` 的参数）。一种常见的模式是使用一个 `NSError` 对象，在发生错误时由它携带错误信息，[initWithContentsOfURL:options:error:](https://developer.apple.com/documentation/foundation/nsdata/1407864-initwithcontentsofurl)（`NSData`）和 [initWithContentsOfFile:encoding:error:](https://developer.apple.com/documentation/foundation/nsstring/1412610-init)（`NSString`）就是这样的例子。

在这些情况下，适用的仍然是前面已经描述过的规则。当你调用这些方法中的任何一个时，`NSError` 对象并不是由你创建的，所以你不拥有它。因此也就不需要释放它，如下例所示：

```objc
NSString *fileName = <#Get a file name#>;
NSError *error;
NSString *string = [[NSString alloc] initWithContentsOfFile:fileName
                        encoding:NSUTF8StringEncoding error:&error];
if (string == nil) {
    // 处理错误……
}
// ...
[string release];
```


`NSObject` 类定义了一个方法 [dealloc](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/dealloc)，当一个对象没有任何拥有者、其内存被回收时，该方法会被自动调用——在 Cocoa 的术语中，这称为对象被“释放”（freed 或 deallocated）。`dealloc` 方法的职责是释放对象自身的内存，并处置它所持有的所有资源，包括它对各个对象类型实例变量的所有权。

下面的例子演示了如何为 Person 类实现 `dealloc` 方法：

```objc
@interface Person : NSObject
@property (retain) NSString *firstName;
@property (retain) NSString *lastName;
@property (assign, readonly) NSString *fullName;
@end

@implementation Person
// ...
- (void)dealloc
    [_firstName release];
    [_lastName release];
    [super dealloc];
}
@end
```


Core Foundation 对象也有类似的内存管理规则（参见 _[Core Foundation 内存管理编程指南](../../Core%20Foundation/Memory%20Management%20Programming%20Guide%20for%20Core%20Foundation/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdo2i)_）。但 Cocoa 与 Core Foundation 的命名约定并不相同。特别是，Core Foundation 的 Create 规则（参见 [The Create Rule](../../Core%20Foundation/Memory%20Management%20Programming%20Guide%20for%20Core%20Foundation/Ownership%20Policy.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge2dqljrgaztamrz)）并不适用于返回 Objective-C 对象的方法。例如，在下面这段代码中，你_不_需要负责放弃 `myInstance` 的所有权：

```objc
MyClass *myInstance = [MyClass createInstance];
```

[下一页](Practical%20Memory%20Management.md)[上一页](About%20Memory%20Management.md)

