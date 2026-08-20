---
title: Objective-C 编程语言
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocCategories.html
archived_at: '2026-07-15T07:17:29.435424Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 编程语言](Introduction.md)


[下一页](Associative%20References.md)[上一页](Declared%20Properties.md)

# 分类与扩展

_分类（category）_让你可以为一个既有的类添加方法——即便你并没有该类的源代码，也同样可以做到。分类是一项强大的特性，让你无需派生子类就能扩展既有类的功能。使用分类，你还可以把自己所写的类的实现分散到多个文件中。_类扩展（class extension）_与之类似，但它允许你在类的主 `@interface` 块之外的位置，为该类声明额外的_必需（required）_ API。

你可以通过在接口文件中以某个分类名声明方法、并在实现文件中以同一个分类名定义这些方法，来为一个类添加方法。分类名表明这些方法是对某个在别处声明的类的补充，而不是一个新的类。不过，你不能使用分类为一个类添加额外的实例变量。

分类添加的方法会成为该类类型的一部分。例如，在某个分类中为 `NSArray` 类添加的方法，会被编译器视为 `NSArray` 实例本应具备的方法之一。而在子类中为 `NSArray` 类添加的方法，则不会被纳入 `NSArray` 类型中。（这一点只对静态类型化的对象才有意义，因为静态类型化是编译器能够得知一个对象所属类的唯一方式。）

分类方法能做到的事情，和类本身定义的方法完全一样。在运行时，两者没有任何区别。分类添加到某个类上的方法，会像其他方法一样被该类的所有子类继承。

分类接口的声明看起来和类接口的声明非常相似——只不过分类名会列在类名后面的圆括号中，而且不会提及超类。除非分类中的方法不访问该类的任何实例变量，否则分类必须导入它所扩展的那个类的接口文件：

```objc
#import "ClassName.h"

@interface ClassName ( CategoryName )
// 方法声明
@end
```

请注意，分类不能为该类声明额外的实例变量，它只能包含方法。不过，该类作用域内的所有实例变量，同样也在分类的作用域内，包括该类声明的所有实例变量，即使是声明为 `@private` 的实例变量也不例外。

你可以为一个类添加的分类数量没有限制，但每个分类名必须各不相同，并且每个分类应该声明和定义一组不同的方法。

类扩展就像是匿名的分类，不同之处在于，它们所声明的方法必须在对应类的主 `@implementation` 块中实现。使用 Clang/LLVM 2.0 编译器，你还可以在类扩展中声明属性和实例变量。

类扩展的一个常见用途，是把一个公开声明为只读的属性，私下重新声明为可读写：

```objc
@interface MyClass : NSObject
@property (retain, readonly) float value;
@end

// 私有扩展，通常隐藏在主实现文件中。
@interface MyClass ()
@property (retain, readwrite) float value;
@end
```

请注意（与分类相反），第二个 `@interface` 块的圆括号中没有给出名称。

通常，一个类会拥有一个公开声明的 API，然后再私下声明一些额外的方法，仅供该类或该类所在的框架内部使用。类扩展允许你在类的主 `@interface` 块之外的位置，为该类声明额外的_必需_方法，如下例所示：

```objc
@interface MyClass : NSObject
- (float)value;
@end


@interface MyClass () {
    float value;
}
- (void)setValue:(float)newValue;
@end

@implementation MyClass

- (float)value {
    return value;
}

- (void)setValue:(float)newValue {
    value = newValue;
}

@end
```

`setValue:` 方法的实现_必须_出现在该类的主 `@implementation` 块中（你不能在分类中实现它）。如果不是这样，编译器就会发出警告，说它找不到 `setValue:` 的方法定义。

[下一页](Associative%20References.md)[上一页](Declared%20Properties.md)

