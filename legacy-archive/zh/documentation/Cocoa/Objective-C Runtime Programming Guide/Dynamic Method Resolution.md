---
title: Objective-C 运行时编程指南
apple_id: TP40008048
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtDynamicResolution.html
archived_at: '2026-07-15T07:17:28.420591Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 运行时编程指南](Introduction.md)


[下一页](Message%20Forwarding.md)[上一页](Messaging.md)

# 动态方法解析

本章介绍如何动态地为一个方法提供实现。

在某些场景下，你可能希望动态地为某个方法提供实现。例如，Objective-C 的声明属性特性（参见 _[Objective-C 编程语言](../The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_ 中的 [声明属性](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocProperties.html#//apple_ref/doc/uid/TP30001163-CH17)）就包含 `@dynamic` 指令：

```objc
@dynamic propertyName;
```

它告诉编译器：与该属性关联的方法将以动态方式提供。

你可以实现 [resolveInstanceMethod:](https://developer.apple.com/documentation/objectivec/nsobject/1418500-resolveinstancemethod) 和 [resolveClassMethod:](https://developer.apple.com/documentation/objectivec/nsobject/1418889-resolveclassmethod)，分别为给定选择器动态提供实例方法和类方法的实现。

一个 Objective-C 方法其实就是一个至少接受两个参数——`self` 和 `_cmd`——的 C 函数。你可以用 [class_addMethod](https://developer.apple.com/documentation/objectivec/1418901-class_addmethod) 函数把一个函数作为方法添加到类中。因此，给定下面这个函数：

```c
void dynamicMethodIMP(id self, SEL _cmd) {
    // 实现 ....
}
```

你可以像下面这样用 `resolveInstanceMethod:` 把它动态添加到类中，作为一个名为 `resolveThisMethodDynamically` 的方法：

```objc
@implementation MyClass
+ (BOOL)resolveInstanceMethod:(SEL)aSEL
{
    if (aSEL == @selector(resolveThisMethodDynamically)) {
          class_addMethod([self class], aSEL, (IMP) dynamicMethodIMP, "v@:");
          return YES;
    }
    return [super resolveInstanceMethod:aSEL];
}
@end
```

转发方法（如 [消息转发](Message%20Forwarding.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqguwvgvzr) 中所述）与动态方法解析在很大程度上是正交的。在转发机制启动之前，类有机会先动态解析某个方法。如果调用了 [respondsToSelector:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/respondsToSelector:) 或 [instancesRespondToSelector:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/clm/NSObject/instancesRespondToSelector:)，动态方法解析器会先得到为该选择器提供 `IMP` 的机会。如果你实现了 [resolveInstanceMethod:](https://developer.apple.com/documentation/objectivec/nsobject/1418500-resolveinstancemethod)，但希望某些特定的选择器实际走转发机制，就对这些选择器返回 `NO`。

Objective-C 程序可以在运行期间加载并链接新的类和分类。新代码会被并入程序，其待遇与程序启动时加载的类和分类完全相同。

动态加载可以用来做很多不同的事情。例如，“系统偏好设置”应用程序中的各个模块就是动态加载的。

在 Cocoa 环境中，动态加载常用于让应用程序可被定制。其他人可以编写模块，由你的程序在运行时加载——就像 Interface Builder 加载自定义面板、OS X 的“系统偏好设置”应用程序加载自定义偏好设置模块那样。可加载的模块扩展了你的应用程序的能力。它们以你所允许、却无法预料也无法自行定义的方式为程序添砖加瓦。你提供框架，别人提供代码。

虽然有一个运行时函数可以对 Mach-O 文件中的 Objective-C 模块执行动态加载（`objc_loadModules`，定义于 `objc/objc-load.h`），但 Cocoa 的 `NSBundle` 类为动态加载提供了方便得多的接口——它是面向对象的，并与相关服务集成在一起。关于 `NSBundle` 类及其用法的信息，参见 Foundation 框架参考中的 [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) 类说明。关于 Mach-O 文件的信息，参见 _OS X ABI Mach-O File Format Reference_。

[下一页](Message%20Forwarding.md)[上一页](Messaging.md)

