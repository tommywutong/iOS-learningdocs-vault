---
title: Objective-C 编程语言
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocStaticBehavior.html
archived_at: '2026-07-15T07:17:31.919742Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 编程语言](Introduction.md)


[下一页](Selectors.md)[上一页](Fast%20Enumeration.md)

# 启用静态行为

本章说明静态类型（static typing）是如何工作的，并讨论了 Objective-C 的其他一些特性，包括暂时克服其固有动态性的方法。

按照设计，Objective-C 对象是动态实体。关于它们的决策会被尽可能地从编译期推迟到运行时：

- 对象的内存是由创建新实例的类方法在运行时_动态分配_的。
- 对象是_动态类型_的。在源代码中（也就是在编译期），任何对象变量都可以被声明为 `id` 类型，而不管该对象实际所属的类是什么。`id` 变量的确切类（因而也就是它特有的方法和数据结构）要等到程序运行时才能确定。
- 消息和方法是_动态绑定_的，正如[动态绑定](Objects%2C%20Classes%2C%20and%20Messaging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjrfu4dmmrwga)中所述。一个运行时过程会把消息中的方法选择器与“属于”接收者的某个方法实现进行匹配。

这些特性赋予了面向对象程序极大的灵活性和能力，但也是要付出代价的。具体来说，编译器无法检查 `id` 变量的确切类型（类）。为了实现更好的编译期类型检查，并让代码更具自说明性，Objective-C 允许把对象静态类型化为某个类名，而不是笼统地类型化为 `id`。Objective-C 还允许你关闭它的一些面向对象特性，从而把某些操作从运行时转移回编译期。

如果像下面这样，用指向某个类名的指针代替 `id` 出现在对象声明中

```objc
Rectangle *thisObject;
```

编译器会限制该声明变量的值，使其只能是声明中指定的那个类的实例，或者是继承自该类的某个类的实例。在上面的例子中，`thisObject` 只能是某种 `Rectangle` 对象。

静态类型化的对象与被声明为 `id` 类型的对象拥有相同的内部数据结构。类型并不影响对象本身；它影响的只是提供给编译器的关于该对象的信息量，以及阅读源代码的人所能获得的信息量。

静态类型化同样不会影响对象在运行时的处理方式。静态类型化的对象是由创建 `id` 类型实例的同一批类方法动态分配的。如果 `Square` 是 `Rectangle` 的子类，下面的代码仍然会产生一个拥有 `Square` 对象全部实例变量的对象，而不仅仅是 `Rectangle` 对象的实例变量：

```objc
Rectangle *thisObject = [[Square alloc] init];
```

发送给静态类型化对象的消息，和发送给 `id` 类型对象的消息一样，都是动态绑定的。静态类型化接收者的确切类型仍然是在运行时、作为消息传递过程的一部分被确定的。发送给 `thisObject` 对象的 `display` 消息：

```objc
[thisObject display];
```

执行的是 `Square` 类中定义的方法版本，而不是其超类 `Rectangle` 中的版本。

通过给编译器提供关于对象的更多信息，静态类型化开启了一些对于类型为 `id` 的对象而言不存在的可能性：

- 在某些情况下，它允许进行编译期类型检查。
- 它可以让对象摆脱“同名方法必须具有相同的返回类型和参数类型”这一限制。
- 它允许你使用结构体指针运算符直接访问对象的实例变量。

前两种可能性将在接下来的小节中讨论。第三种则在[定义一个类](Defining%20a%20Class.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjsfvjvomi)中介绍。

借助静态类型化所提供的额外信息，编译器可以在两种情况下提供更好的类型检查服务：

- 当消息被发送给一个静态类型化的接收者时，编译器可以确保该接收者能够响应这条消息。如果接收者无法访问消息中指定的方法，就会发出警告。
- 当一个静态类型化的对象被赋值给一个静态类型化的变量时，编译器会确保二者的类型是兼容的。如果类型不兼容，就会发出警告。

只要被赋值对象的类与接收赋值的变量的类相同，或者是它的子类，赋值就可以在没有警告的情况下进行。下面的例子说明了这一点：

```objc
Shape     *aShape;
Rectangle *aRect;

aRect = [[Rectangle alloc] init];
aShape = aRect;
```

这里，`aRect` 可以被赋值给 `aShape`，因为矩形是一种形状——`Rectangle` 类继承自 `Shape`。但是，如果把这两个变量的角色互换，把 `aShape` 赋值给 `aRect`，编译器就会产生警告；并不是每种形状都是矩形。（作为参考，请参见[图 1-2](Objects%2C%20Classes%2C%20and%20Messaging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjrfu4dmnjqge)，其中展示了包含 `Shape` 和 `Rectangle` 的类层级结构。）

当赋值运算符两侧的表达式都是 `id` 类型时，不会进行任何检查。一个静态类型化的对象可以被自由地赋值给一个 `id` 类型的对象，反之亦然。因为像 `alloc` 和 `init` 这样的方法返回的都是 `id` 类型的对象，编译器无法确保返回给静态类型化变量的是一个兼容的对象。下面的代码虽然容易出错，但依然是允许的：

```objc
Rectangle *aRect;
aRect = [[Shape alloc] init];
```


一般来说，不同类中具有相同选择器（也就是相同名称）的方法，也必须具有相同的返回类型和参数类型。编译器施加这一约束，是为了支持动态绑定。因为消息接收者的类（因而与该类相关的、方法实现的具体细节）在编译期是无法得知的，所以编译器必须一视同仁地对待所有同名方法。当它为运行时系统准备方法返回类型和参数类型的信息时，会为每个方法选择器只生成一份方法描述。

不过，当消息被发送给一个静态类型化的对象时，编译器是知道接收者的类的。编译器可以访问关于该方法的、与类相关的具体信息。因此，这条消息就摆脱了对其返回类型和参数类型的限制。

一个实例可以被静态类型化为它自身所属的类，也可以被静态类型化为它所继承的任何类。例如，所有实例都可以被静态类型化为 `NSObject`。

不过，编译器只能通过类型声明中的类名来了解静态类型化对象的类，并据此进行类型检查。因此，把一个实例类型化为它所继承的某个类，可能会导致编译器认为在运行时会发生的情况，与实际发生的情况之间出现差异。

例如，如果你像下面这样把一个 `Rectangle` 实例静态类型化为 `Shape`：

```objc
Shape *myRectangle = [[Rectangle alloc] init];
```

编译器会把它当作 `Shape` 实例来处理。如果你给这个对象发送一条消息，要求它执行某个 `Rectangle` 方法，

```objc
BOOL solid = [myRectangle isFilled];
```

编译器就会报错。`isFilled` 方法是在 `Rectangle` 类中定义的，而不是在 `Shape` 类中。

但是，如果你给它发送一条消息，要求它执行一个 `Shape` 类知道的方法，比如

```objc
[myRectangle display];
```

编译器就不会报错，即便 `Rectangle` 覆写了这个方法。在运行时，执行的是 `display` 方法的 `Rectangle` 版本。

类似地，假设 `Upper` 类声明了一个返回 `double` 的 `worry` 方法，如下所示：

```objc
- (double)worry;
```

而 `Upper` 的子类 `Middle` 覆写了这个方法，并声明了一个新的返回类型：

```objc
- (int)worry;
```

如果一个实例被静态类型化为 `Upper` 类，编译器就会认为它的 `worry` 方法返回 `double`；如果一个实例被类型化为 `Middle` 类，编译器就会认为 `worry` 返回 `int`。如果一个 `Middle` 实例被类型化为 `Upper` 类，就会产生错误：编译器会告诉运行时系统，发送给该对象的 `worry` 消息返回的是 `double`，但在运行时它实际返回的却是 `int`，于是产生了一个错误。

静态类型化可以让同名方法摆脱“必须具有相同返回类型和参数类型”这一限制，但只有当这些方法分别声明在类层级结构的不同分支上时，这种做法才是可靠的。

[下一页](Selectors.md)[上一页](Fast%20Enumeration.md)

