---
title: Objective-C 编程语言
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocAssociativeReferences.html
archived_at: '2026-07-15T07:17:29.426764Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 编程语言](Introduction.md)


[下一页](Fast%20Enumeration.md)[上一页](Categories%20and%20Extensions.md)

# 关联引用

关联引用（associative reference）从 OS X v10.6 起可用，用于模拟向一个已有类添加对象实例变量。使用关联引用，你可以在不修改类声明的情况下为对象添加存储。如果你无法访问该类的源代码，或者出于二进制兼容性的原因无法更改对象的内存布局，这项特性会很有用。

关联（association）以键（key）为基础。对任何对象，你都可以添加任意数量的关联，每个关联使用不同的键。一个关联还可以确保被关联的对象至少在源对象的生命周期内保持有效。

你可以使用 Objective-C 运行时函数 [objc_setAssociatedObject](https://developer.apple.com/documentation/objectivec/1418509-objc_setassociatedobject) 在两个对象之间建立关联。该函数接受四个参数：源对象、键、值，以及一个关联策略常量。其中键和关联策略值得进一步讨论。

- 键是一个 `void` 指针。每个关联的键都必须是唯一的。典型的做法是使用一个 `static` 变量。
- 策略指定了被关联对象是被赋值（assign）、保留（retain）还是拷贝（copy），以及该关联是原子的还是非原子的。这种模式与声明属性的特性类似（参见[属性声明特性](Declared%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomq)）。你使用一个常量来指定该关系的策略（参见 [objc_AssociationPolicy](https://developer.apple.com/documentation/objectivec/objc_associationpolicy) 和 `Associative Object Behaviors`）。

清单 6-1 展示了如何在一个数组和一个字符串之间建立关联。

__清单 6-1__  在数组和字符串之间建立关联

```objc
static char overviewKey;

NSArray *array =
    [[NSArray alloc] initWithObjects:@"One", @"Two", @"Three", nil];
// 出于说明目的，使用 initWithFormat: 来确保
// 该字符串可以被释放
NSString *overview =
    [[NSString alloc] initWithFormat:@"%@", @"First three numbers"];

objc_setAssociatedObject (
    array,
    &overviewKey,
    overview,
    OBJC_ASSOCIATION_RETAIN
);

[overview release];
// (1) overview 仍然有效
[array release];
// (2) overview 已失效
```

在第 1 点，字符串 `overview` 仍然有效，因为 [OBJC_ASSOCIATION_RETAIN](https://developer.apple.com/documentation/objectivec/objc_associationpolicy/objc_association_retain) 策略指定数组会保留（retain）被关联的对象。然而，当数组被释放后（第 2 点），`overview` 也被释放，在这种情况下也随之被释放（deallocated）。如果你此时尝试记录 `overview` 的值，就会产生一个运行时异常。

你可以使用 Objective-C 运行时函数 [objc_getAssociatedObject](https://developer.apple.com/documentation/objectivec/1418865-objc_getassociatedobject) 来获取一个关联对象。沿用[清单 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmrufvjvona)中的示例，你可以用下面这行代码从数组中取回 overview：

```objc
NSString *associatedObject =
    (NSString *)objc_getAssociatedObject(array, &overviewKey);
```


要解除一个关联，通常调用 `objc_setAssociatedObject`，并把 `nil` 作为值传入。

沿用[清单 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmrufvjvona)中的示例，你可以用下面这行代码解除数组与字符串 `overview` 之间的关联：

```objc
objc_setAssociatedObject(array, &overviewKey, nil, OBJC_ASSOCIATION_ASSIGN);
```

由于被关联对象被设为 `nil`，策略在这里实际上并不重要。

要解除某个对象的_全部_关联，可以调用 [objc_removeAssociatedObjects](https://developer.apple.com/documentation/objectivec/1418683-objc_removeassociatedobjects)。不过一般不建议使用这个函数，因为它会解除该对象对所有客户端的全部关联。只有在你需要把对象恢复到"最初状态"时，才应使用这个函数。

下面这个程序综合了前几节的代码。

```objc
#import <Foundation/Foundation.h>
#import <objc/runtime.h>

int main (int argc, const char * argv[]) {

    @autoreleasepool {
        static char overviewKey;

        NSArray *array = [[NSArray alloc]
            initWithObjects:@ "One", @"Two", @"Three", nil];
        // 出于说明目的，使用 initWithFormat: 来确保
        // 得到一个可释放的字符串
        NSString *overview = [[NSString alloc]
            initWithFormat:@"%@", @"First three numbers"];

        objc_setAssociatedObject (
            array,
            &overviewKey,
            overview,
            OBJC_ASSOCIATION_RETAIN
        );
        [overview release];

        NSString *associatedObject =
            (NSString *) objc_getAssociatedObject (array, &overviewKey);
        NSLog(@"associatedObject: %@", associatedObject);

        objc_setAssociatedObject (
            array,
            &overviewKey,
            nil,
            OBJC_ASSOCIATION_ASSIGN
        );
        [array release];

    }
    return 0;
}
```

[下一页](Fast%20Enumeration.md)[上一页](Categories%20and%20Extensions.md)

