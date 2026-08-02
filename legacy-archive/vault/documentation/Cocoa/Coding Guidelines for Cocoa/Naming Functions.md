---
title: Cocoa 编码规范
apple_id: 10000146i
resource_type: Guide
platform: watchOS|iOS|macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CodingGuidelines/Articles/NamingFunctions.html
archived_at: '2026-07-15T07:13:27.278486Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Cocoa 编码规范](Introduction%20to%20Coding%20Guidelines%20for%20Cocoa.md)


[下一页](Naming%20Properties%20and%20Data%20Types.md)[上一页](Naming%20Methods.md)

# 函数命名

[Objective-C](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectiveC.html#//apple_ref/doc/uid/TP40008195-CH43) 允许你既用方法也用函数来表达行为。当底层对象始终是[单例](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Singleton.html#//apple_ref/doc/uid/TP40008195-CH49)时，或者当你面对的是明显偏函数式的子系统时，就应该使用函数，而不是（比如说）[类方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassMethod.html#//apple_ref/doc/uid/TP40008195-CH8)。

函数命名有一些应当遵循的通用规则：

- 函数名的构成方式与方法名相同，但有两点例外：

  - 函数名以你用于类和常量的同一个前缀（prefix）开头。
  - 前缀后面那个词的首字母要大写。
- 大多数函数名以动词开头，描述该函数所产生的效果：

```c
NSHighlightRect
NSDeallocateObject
```

用于查询属性的函数还有另外一套命名规则：

- 如果函数返回的是其第一个参数的属性，就省略动词。

```c
unsigned int NSEventMaskFromType(NSEventType type)
float NSHeight(NSRect aRect)
```
- 如果值是通过引用返回的，就使用“Get”。

```c
const char *NSGetSizeAndAlignment(const char *typePtr, unsigned int *sizep, unsigned int *alignp)
```
- 如果返回的值是布尔值，函数名应当以一个变位后的动词开头。

```c
BOOL NSDecimalIsNotANumber(const NSDecimal *decimal)
```

[下一页](Naming%20Properties%20and%20Data%20Types.md)[上一页](Naming%20Methods.md)

