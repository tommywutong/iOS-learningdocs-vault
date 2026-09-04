---
title: '把 [super init] 赋给 self 意味着什么？| Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/04/what-does-it-mean-when-you-assign-super.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:60f2313a4c234b76'
translated: true
---

> 原文：[What does it mean when you assign [super init] to self? | Cocoa with Love](https://www.cocoawithlove.com/2009/04/what-does-it-mean-when-you-assign-super.html)　·　Cocoa with Love (Matt Gallagher)

Objective-C 常见语法里最古怪的语句之一，就是 `self = [super init];` 这一行。如果没有任何解释，这种写法会引出几个问题：这一行是在给实例设置 `self` 的值吗？`self` 只是和其他变量一样的普通变量吗？如果是，那当初为什么要有它？我会逐一回答这些问题，并展示编译器如何转换 `self` 的使用和方法调用。

## 转换方法调用

理解 `self` 参数的第一步，是看看编译器如何转换一次标准的方法调用。

当你写下下面的代码时：

```objc
MyClass *myObject = [[MyClass alloc] initWithString:@"someString"];
```

编译器会把它转换成类似这样的函数调用：

```objc
class myClass = objc_getClass("MyClass");
SEL allocSelector = @selector(alloc);
MyClass *myObject1 = objc_msgSend(myClass, allocSelector);

SEL initSelector = @selector(initWithString:);
MyClass *myObject2 = objc_msgSend(myObject1, initSelector, @"someString");
```

编译器获取 `class` 和 `SEL` 值的手段其实比这稍微高效一些，但如果你去看汇编代码，就会看到每一次方法调用都对应着 `objc_msgSend` 调用。

## 那么「self」究竟是什么？

你声明的每一个方法都有两个隐藏参数：`self` 和 `_cmd`。

下面的方法：

```objc
- (id)initWithString:(NSString *)aString;
```

会被编译器转换成下面这个函数调用：

```objc
id initWithString(id self, SEL _cmd, NSString *aString);
```

实际情况是：`self` 只是每个方法上的一个隐藏参数。和任何其他参数一样，它的值来自函数调用。

是的，`_cmd` 也是每个方法上的隐藏参数，只要你想，就可以访问它。实际上，除了[一些冷门场景](https://www.cocoawithlove.com/2008/03/supersequent-implementation.html)之外，`_cmd` 参数几乎没有用武之地。

你可以做个实验：抛开 `objc_msgSend`，直接调用方法对应的函数。你可以不这样调用：

```objc
[myObject someMethodWithParameter:someValue];
```

而是通过重现 `objc_msgSend` 所做的工作，直接调到你的方法实现：

```objc
SEL methodSelector = @selector(someMethodWithParameter:);
IMP someMethodFunction = class_getMethodImplementation([myObject class], methodSelector);
someMethodFunction(myObject, methodSelector, someValue);
```

在 `someMethodWithParameter:` 的实现内部，`self` 之所以有值，唯一的原因是：指针 `myObject` 被当作第一个参数传进了 `someMethodFunction`。如果你给这第一个参数传一个别的值，那么方法内部的 `self` 就会是另一个值。

如果你传入的是一个属于其他类的值，程序很有可能会崩溃。下一节解释为什么。

## 为什么非要有一个「self」参数？

方法需要知道要去操作什么数据。`self` 参数把要操作的数据告诉类，因此它对面向对象编程至关重要。

这话听起来可能有点奇怪，因为你完全可以实现一个不按名字使用 `self` 参数的方法。实际情况是：编译器用 `self` 参数来解析方法内部对实例变量（instance variable）的一切引用。

假如你有一个这样定义的类：

```objc
@interface MyClass : NSObject
{
    NSInteger value;
}
- (void)setValueToZero;
@end
```

那么方法：

```objc
- (void)setValueToZero
{
    value = 0;
}
```

会被编译器转换成：

```objc
void setValueToZero(id self, SEL _cmd)
{
    self->value = 0;
}
```

所以，即使你从来没有亲手敲下「`self`」这个词，`self` 对访问任何实例变量来说都是必不可少的。

## 那么，调用 init 时 self 已经有值了吗？

如果你还记得开头的内容：我说过，典型的 `[[MyClass alloc] initWithString:@"someString"]` 调用里，`initWithString:` 这一部分会被转换成一次 `objc_msgSend` 调用：

```objc
MyClass *myObject2 = objc_msgSend(myObject1, initSelector, @"someString");
```

所以，等执行到方法内部时，`self` 已经有值了；它的值就是 `myObject1`（也就是分配出来的对象，即 `[MyClass alloc]` 调用返回的那个对象）。这一点至关重要：没有它，对 `super` 的调用就无从谈起——编译器正是用 `self` 的值来发送这次调用的：

```objc
[super init];
```

变成：

```objc
objc_msgSendSuper(self, @selector(init));
```

是的，你的初始化方法开始执行时，`self` 已经有值了。事实上，几乎可以保证它就是那个正确的最终值。

## 那么，为什么要把 [super init] 返回的值赋给 self？

看一个典型的初始化方法：

```objc
- (id)initWithString:(NSString *)aString
{
    self = [super init];
    if (self)
    {
        instanceString = [aString retain];
    }
    return self;
}
```

为什么这里要把 `[super init]` 赋给 self 呢？

教科书式的理由是：`[super init]` 允许做下面三件事之一：

1. 返回它自己的接收者（receiver）（`self` 指针不变），继承下来的实例值已完成初始化。
2. 返回一个不同的对象，继承下来的实例值已完成初始化。
3. 返回 `nil`，表示失败。

第一种情况下，赋值对 `self` 没有任何影响，`instanceString` 还是设置在原来的对象上（`instanceString = [aString retain];` 这一行就算写在方法的第一行，结果也一样）。

第三种情况下，初始化失败了。`self` 被设为 `nil`，不再执行任何后续操作，最后返回 `nil`。

把值赋给 `self` 的理由与第二种情况有关：如果返回的是另一个不同的对象，我们希望下面这行代码：

```objc
        instanceString = [aString retain];
```

会被转换成：

```objc
        self->instanceString = [aString retain];
```

之后能作用到正确的值上，所以我们不得不改变 `self` 的值，让它指向这个新对象。

## 几乎从不需要给 self 赋值

于是，给 `self` 赋值的理由就是：`[super init]` 可能返回一个不同的对象，而接下来的初始化应该作用在那个不同的对象上，而不是作用在旧的（很可能已经失效的）对象上。

那么要考虑的问题就来了：`[super init]` 什么时候会返回不同的对象？

答案是：在下面这几种情况之一里，它会返回不同的对象：

- 单例（singleton）对象（总是返回那个单例，而不是任何后续分配的对象）
- 其他唯一对象（`[NSNumber numberWithInteger:0]` 总是返回全局的「零」对象）
- 类簇（class cluster）会在你初始化超类的实例时，替换成私有的子类。
- 有的类会根据传入初始化方法的参数，选择重新分配同一个（或兼容的）类。

除最后一种情况外，如果返回的对象变了，还继续对它做初始化就是个错误——返回的对象已经完全初始化好了，而且很可能已经和你的类没有任何关系了。

于是，把「返回一个不同的对象」这一条拆成两条，`[super init]` 允许返回的东西就从三种扩展成了四种：

1. 返回它自己的接收者（`self` 指针不变），继承下来的实例值已完成初始化。
2. 返回一个同类的对象，还需要进一步初始化。
3. 返回一个已经完全初始化好的不同对象。
4. 返回 `nil`，表示失败。

在这个列表里，出现了两种互不兼容的情况（2 和 3）。典型的「把 `[super init]` 赋给 `self`」式初始化方法处理的是情况 1、2 和 4。

真正能处理情况 1、3 和 4 的 `init` 写法其实应该是：

```objc
- (id)initWithString:(NSString *)aString
{
    id result = [super init];
    if (self == result)
    {
        instanceString = [aString retain];
    }
    return result;
}
```

类簇、单例和唯一对象全都走的是情况 3，属于这一类的 Cocoa 类有几十个。而据我所知，用情况 2 的只有 `NSManagedObject`。奇怪的地方就在这里：尽管情况 3 占了压倒性的多数，成为标准的却是那些支持情况 1、2、4、但与情况 3 不兼容的初始化方法。

## 结论

> _更新_：我重写了这段结论，以表明我其实并不是在建议你停用「把 `[super init]` 赋给 `self`」式的初始化方法。感谢所有用各种有创意的方式告诉我「我在这层引申上理解错了」的人。

对大多数类来说，你_并不_需要把 `[super init]` 赋给 `self` 才能让它们正常工作。在某些冷门场景下，这么做实际上反而是错的。

那我们为什么还在继续给 `self` 赋值？因为它是初始化方法的传统模板；虽然它在一些情况下是错的，但在另一些情况下却是对的——那些代码本来就是按这种写法来编写的。

除此之外还要考虑一点：类簇以及其他一些类，它们的 init 方法本就可能返回无关的、不同的、已完全初始化好的对象，这些类本来就不该用常规方式去派生子类——这让偏向这类类的代码意义有限。

`super` 返回无关对象的情况非常少，完全可以逐个处理——一个类通常会把「它的初始化方法可能返回接收者或 `nil` 以外的东西」这件事说得非常清楚。
