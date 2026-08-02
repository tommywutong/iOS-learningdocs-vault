---
title: Objective-C 编程语言
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocProperties.html
archived_at: '2026-07-15T07:17:31.884592Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 编程语言](Introduction.md)


[下一页](Categories%20and%20Extensions.md)[上一页](Protocols.md)

# 声明属性

Objective-C 声明属性（declared property）特性提供了一种简单的方式，用来声明和实现对象的存取（accessor）方法。

你通常会通过一对存取（取值/赋值，getter/setter）方法来访问对象的属性（指其特性和关系）。使用存取方法可以让你遵循_封装（encapsulation）_原则（参见 _[Objective-C 面向对象编程](../Object-Oriented%20Programming%20with%20Objective-C/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbz)_ 中的[抽象的机制](../Object-Oriented%20Programming%20with%20Objective-C/The%20Object%20Model.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbzfvbuqnjnha3dgmjw)）。你可以严格控制取值/赋值方法对的行为以及底层的状态管理，同时让 API 的使用者不受实现变化的影响。

尽管使用存取方法因此具有明显的优势，但编写存取方法却是一件繁琐的工作。而且，属性中一些对 API 使用者而言可能很重要的方面会被隐藏起来——比如存取方法是否线程安全，或者赋值时是否会拷贝新值。

声明属性通过提供以下特性解决了这些问题：

- 属性声明为存取方法的行为提供了清晰、明确的说明。
- 编译器可以根据你在声明中提供的说明，为你合成（synthesize）存取方法。
- 属性在语法上表示为标识符，并且具有作用域，因此编译器可以检测出对未声明属性的使用。

声明属性包含两个部分：声明和实现。

属性声明以关键字 `@property` 开头。`@property` 可以出现在类的 `@interface` 块中方法声明列表的任意位置，也可以出现在[协议](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45)或[分类](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Category.html#//apple_ref/doc/uid/TP40008195-CH5)的声明中。

```objc
@property (attributes) type name;
```

`@property` 指令用于声明一个属性。可选的、以圆括号括起的一组特性（attribute）为该属性的存储语义和其他行为提供了额外的说明——可能的取值参见[属性声明特性](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomq)。和其他 Objective-C 类型一样，每个属性都有类型说明和名称。

清单 4-1 展示了一个简单属性的声明。

__清单 4-1__  声明一个简单的属性

```objc
@interface MyClass : NSObject
@property float value;
@end
```

你可以把属性声明看作等价于声明两个存取方法。因此

```objc
@property float value;
```

等价于：

```objc
- (float)value;
- (void)setValue:(float)newValue;
```

不过，属性声明还提供了关于存取方法如何实现的额外信息（如[属性声明特性](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomq)中所述）。

你也可以把属性声明放在类扩展中（参见[扩展](Categories%20and%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmrqfvjvomq)）。例如，你可以像下面这样声明前面展示的 `value` 属性：

```objc
@interface MyClass : NSObject
@end

@interface MyClass ()
@property float value;
@end
```

如果你想隐藏私有属性的声明，这种做法会很有用。

你可以使用 `@property(attribute [, attribute2, ...])` 这种形式为属性添加特性。和方法一样，属性的作用域限定在其所在的接口声明中。对于使用逗号分隔的变量名列表的属性声明，这些特性会应用于所有列出的属性。

如果你使用 `@synthesize` 指令告诉编译器创建存取方法（参见[属性实现指令](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvooi)），编译器生成的代码会与关键字给出的说明相匹配。如果你自己实现存取方法，就应该确保实现与说明相符（例如，如果你指定了 `copy`，就必须确保赋值方法中确实拷贝了输入的值）。

与某个属性关联的取值方法和赋值方法默认名称分别是 _propertyName_ 和 `set`_PropertyName_`:`——例如，给定一个名为“foo”的属性，其存取方法就会是 `foo` 和 `setFoo:`。下面这些特性允许你指定自定义名称。它们都是可选的，可以和其他任何特性一起出现（`setter=` 的情况下不能和 `readonly` 一起出现）。

**`getter=getterName`**
: 指定该属性取值方法的名称。取值方法必须返回与属性类型匹配的类型，且不带参数。

**`setter=setterName`**
: 指定该属性赋值方法的名称。赋值方法必须接受一个与属性类型匹配的单一参数，并且必须返回 `void`。

如果你把某个属性指定为 `readonly`，同时又用 `setter=` 指定了赋值方法，编译器会发出警告。

通常你应该指定符合键值编码（key-value coding）规范的存取方法名称（参见 _[键值编码编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)_）——使用 `getter` 修饰符的一个常见原因，就是要遵循布尔值 `is`_PropertyName_ 的命名约定。

以下特性用于指定某个属性是否具有关联的赋值方法。它们互斥。

**`readwrite`**
: 表示该属性应被当作可读写处理。此特性是默认值。

`@implementation` 块中需要同时提供取值方法和赋值方法。如果你在实现块中使用 `@synthesize` 指令，取值方法和赋值方法都会被合成。

**`readonly`**
: 表示该属性是只读的。

如果你指定了 `readonly`，`@implementation` 块中只需要提供取值方法。如果你在实现块中使用 `@synthesize` 指令，也只会合成取值方法。此外，如果你尝试使用点语法赋值，会产生编译错误。

以下特性用于指定赋值方法的语义。它们互斥。

**`strong`**
: 表示与目标对象之间是强（拥有）关系。

**`weak`**
: 表示与目标对象之间是弱（非拥有）关系。

如果目标对象被释放，该属性的值会自动被设为 `nil`。

（OS X v10.6 和 iOS 4 不支持 weak 属性；请改用 `assign`。）

**`copy`**
: 表示赋值时应使用对象的一份拷贝。

之前的值会被发送一条 [release](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/release) 消息。

拷贝是通过调用 [copy](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/copy) 方法完成的。此特性仅对对象类型有效，且该对象类型必须实现 `NSCopying`  [协议](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45)。

**`assign`**
: 表示赋值方法使用简单赋值。此特性是默认值。

你可以为 `NSInteger`、`CGRect` 这类标量类型使用此特性。

**`retain`**
: 表示赋值时应对该对象调用 [retain](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/retain)。

之前的值会被发送一条 [release](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/release) 消息。

在 OS X v10.6 及更高版本中，你可以使用 `__attribute__` 关键字来指定：在内存管理方面，某个 Core Foundation 属性应被当作 Objective-C 对象处理：

```objc
@property(retain) __attribute__((NSObject)) CFDictionaryRef myDictionary;
```


你可以使用此特性来指定存取方法不是原子（atomic）的。

**`nonatomic`**
: 表示存取方法是非原子（nonatomic）的。_默认情况下，存取方法是原子（atomic）的。_

属性默认是 `atomic` 的，这样合成的存取方法就能在多线程环境中提供对属性的可靠访问——也就是说，无论其他线程正在并发执行什么操作，取值方法返回的值或通过赋值方法设置的值总是完整获取或设置的。

如果你指定了 `strong`、`copy` 或 `retain`，但没有指定 `nonatomic`，那么在引用计数环境中，为对象属性合成的取值方法会使用一个锁，并对返回值执行 retain 和 autorelease——其实现方式类似下面这样：

```objc
[_internal lock]; // 使用对象级锁进行加锁
id result = [[value retain] autorelease];
[_internal unlock];
return result;
```

如果你指定了 `nonatomic`，为对象属性合成的存取方法只会直接返回该值。

属性支持全部的 C 风格修饰符。属性可以被标记为已废弃，并支持 `__attribute__` 风格的标注：

```objc
@property CGFloat x
AVAILABLE_MAC_OS_X_VERSION_10_1_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_4;
@property CGFloat y __attribute__((...));
```

如果你想指定某个属性是一个出口（outlet）（参见 iOS 中的[出口](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Outlet.html#//apple_ref/doc/uid/TP40009071-CH4)和 OS X 中的[出口](https://developer.apple.com/library/archive/documentation/General/Devpedia-CocoaApp-MOSX/Outlet.html#//apple_ref/doc/uid/TP40009448-CH4)），可以使用 `IBOutlet` 标识符：

```objc
@property (nonatomic, weak) IBOutlet NSButton *myButton;
```

不过，`IBOutlet` 并不正式属于特性列表的一部分。关于声明出口属性的更多内容，参见[Nib 文件](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/CocoaNibs/CocoaNibs.html#//apple_ref/doc/uid/10000051i-CH4)。

你可以在 `@implementation` 块中使用 `@synthesize` 和 `@dynamic` 指令来触发特定的编译器行为。请注意，对于任何给定的 `@property` 声明，这两者都不是_必需_的。

**`@synthesize`**
: 如果你没有在 `@implementation` 块中提供某个属性的赋值方法和/或取值方法，就可以使用 `@synthesize` 指令告诉编译器应该为该属性合成这些方法。如果没有另行声明相应的实例变量，`@synthesize` 指令还会合成一个合适的实例变量。

__清单 4-2__  使用 @synthesize

```objc
@interface MyClass : NSObject
@property(copy, readwrite) NSString *value;
@end

@implementation MyClass
@synthesize value;
@end
```

你可以使用 `property=ivar` 这种形式来指明某个属性应使用特定的实例变量，例如：

```objc
@synthesize firstName, lastName, age=yearsOld;
```

这表示应该为 `firstName`、`lastName` 和 `age` 合成存取方法，并且属性 `age` 由实例变量 `yearsOld` 表示。合成方法的其他方面则由可选特性决定（参见[属性声明特性](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomq)）。

无论你是否指定实例变量的名称，`@synthesize` 指令都只能使用当前类中的实例变量，不能使用超类中的实例变量。

存取方法合成的行为会因运行时而异（另见[运行时差异](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomy)）：

- 对于旧版运行时，实例变量必须已经在当前类的 `@interface` 块中声明。如果存在与属性同名的实例变量，且其类型与属性类型兼容，就会使用该实例变量——否则会产生编译错误。
- 对于现代运行时（参见 _[Objective-C 运行时编程指南](../Objective-C%20Runtime%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danby)_ 中的[运行时版本与平台](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtVersionsPlatforms.html#//apple_ref/doc/uid/TP40008048-CH106)），实例变量会按需合成。如果已经存在同名的实例变量，就会使用它。

**`@dynamic`**
: 你可以使用 `@dynamic` 关键字告诉编译器，你将通过直接提供方法实现，或者在运行时使用诸如动态代码加载、动态方法解析之类的其他机制，来履行某个属性所隐含的 API 约定。它会抑制编译器在找不到合适实现时原本会产生的警告。只有在你确定这些方法在运行时会可用的情况下，才应该使用它。

清单 4-3 中的示例展示了如何在 [NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject) 的子类中使用 `@dynamic`。

__清单 4-3__  在 NSManagedObject 中使用 @dynamic

```objc
@interface MyClass : NSManagedObject
@property(nonatomic, retain) NSString *value;
@end

@implementation MyClass
@dynamic value;
@end
```

`NSManagedObject` 由 Core Data 框架提供。一个托管对象（managed object）类有一个对应的模式（schema），用来定义该类的属性和关系；在运行时，Core Data 框架会按需为这些属性和关系生成存取方法。因此，你通常只需要为这些属性和关系声明 `@property`，而不必自己实现存取方法，也不应该要求编译器去实现它们。但是，如果你只是声明了属性而没有提供任何实现，编译器就会产生警告。使用 `@dynamic` 可以抑制这个警告。

你可以为任意 Objective-C 类、Core Foundation 数据类型，或“纯旧数据”（plain old data，POD）类型声明属性（参见 [C++ Language Note: POD Types](http://www.fnal.gov/docs/working-groups/fpcltf/Pkg/ISOcxx/doc/POD.html)）。不过，关于使用 Core Foundation 类型的限制，参见 [Core Foundation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomjq)。

你可以在子类中重新声明某个属性，但（除了 `readonly` 与 `readwrite` 之间的切换之外）必须在子类中完整重复其特性。在[分类](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Category.html#//apple_ref/doc/uid/TP40008195-CH5)或[协议](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45)中声明的属性也是如此——虽然属性可以在分类或协议中重新声明，但其特性必须完整重复。

如果你在某个类中把某个属性声明为 `readonly`，可以在类扩展（参见[扩展](Categories%20and%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmrqfvjvomq)）、协议或子类（参见[使用属性做子类化](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvona)）中把它重新声明为 `readwrite`。在类扩展重新声明的情况下，由于属性是在任何 `@synthesize` 语句之前被重新声明的，这会导致赋值方法被合成。将只读属性重新声明为可读写的能力，支持了两种常见的实现模式：不可变类的可变子类（`NSString`、`NSArray` 和 `NSDictionary` 都是这样的例子），以及公开 API 为 `readonly`、但类内部私有实现为 `readwrite` 的属性。下面的示例展示了如何使用类扩展来提供一个在公共头文件中声明为只读、但在私有部分重新声明为可读写的属性。

```objc
// public header file
@interface MyObject : NSObject
@property (readonly, copy) NSString *language;
@end

// private implementation file
@interface MyObject ()
@property (readwrite, copy) NSString *language;
@end

@implementation MyObject
@synthesize language;
@end
```


正如[属性声明特性](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomq)中所述，在 OS X v10.6 之前，你不能为非对象类型指定 `retain` 特性。因此，如果你声明了一个类型为 CFType 的属性，并像下面的示例那样合成其存取方法：

```objc
@interface MyClass : NSObject
@property(readwrite) CGImageRef myImage;
@end

@implementation MyClass
@synthesize myImage;
@end
```

那么在引用计数环境中，合成的赋值方法只会把新值简单地赋给实例变量（新值不会被 retain，旧值也不会被 release）。对于 Core Foundation 对象来说，简单赋值通常是不正确的；你不应该合成这些方法，而应该自己实现它们。

你可以覆写一个 `readonly` 属性使其变为可写。例如，你可以定义一个类 `MyInteger`，它带有一个 `readonly` 属性 `value`：

```objc
@interface MyInteger : NSObject
@property(readonly) NSInteger value;
@end

@implementation MyInteger
@synthesize value;
@end
```

接下来你可以实现一个子类 `MyMutableInteger`，重新定义该属性使其变为可写：

```objc
@interface MyMutableInteger : MyInteger
@property(readwrite) NSInteger value;
@end

@implementation MyMutableInteger
@dynamic value;

- (void)setValue:(NSInteger)newX {
    value = newX;
}
@end
```


总的来说，属性的行为在现代运行时和旧版运行时上是相同的（参见 _[Objective-C 运行时编程指南](../Objective-C%20Runtime%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danby)_ 中的[运行时版本与平台](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtVersionsPlatforms.html#//apple_ref/doc/uid/TP40008048-CH106)）。但有一个关键区别：现代运行时支持实例变量合成，而旧版运行时不支持。

要让 `@synthesize` 在旧版运行时中生效，你必须提供一个与属性同名且类型兼容的实例变量，或者在 `@synthesize` 语句中指定另一个已存在的实例变量。而在现代运行时中，如果你没有提供实例变量，编译器会为你添加一个。例如，给定下面的类声明和实现：

```objc
@interface MyClass : NSObject
@property float noDeclaredIvar;
@end

@implementation MyClass
@synthesize noDeclaredIvar;
@end
```

旧版运行时的编译器会在 `@synthesize noDeclaredIvar;` 处产生一个错误，而现代运行时的编译器则会添加一个实例变量来表示 `noDeclaredIvar`。

[下一页](Categories%20and%20Extensions.md)[上一页](Protocols.md)

