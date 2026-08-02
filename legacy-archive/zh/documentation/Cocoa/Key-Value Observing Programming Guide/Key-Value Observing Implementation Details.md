---
title: 键值观察编程指南
apple_id: 10000177i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/Articles/KVOImplementation.html
archived_at: '2026-07-15T07:16:19.095971Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [键值观察编程指南](Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md)


[下一页](Document%20Revision%20History.md)[上一页](Registering%20Dependent%20Keys.md)

# 键值观察实现细节

自动键值观察是使用一种称为 _isa-swizzling_ 的技术实现的。

顾名思义，`isa` 指针指向对象的类，而类维护着一个分发表。这个分发表本质上包含了指向该类所实现方法的指针，以及其他数据。

当为对象的某个属性注册观察者时，被观察对象的 isa 指针会被修改，指向一个中间类而非真正的类。因此，isa 指针的值并不一定反映实例的实际类。

你永远不应依赖 `isa` 指针来判断类的归属，而应使用 [class](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/class) 方法来确定对象实例的类。

[下一页](Document%20Revision%20History.md)[上一页](Registering%20Dependent%20Keys.md)
