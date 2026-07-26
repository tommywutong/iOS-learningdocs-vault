---
title: Objective-C 运行时
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objective-c-runtime
source_url: 'https://developer.apple.com/documentation/objectivec/objective-c-runtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objective-c-runtime.json'
content_hash: 'sha256:61df2a7e2cf3522c'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# Objective-C 运行时

<sub>API 集合</sub>

描述 macOS Objective-C runtime 库的支持函数和数据结构。

## Overview

Objective-C runtime 是一个运行时库，为 Objective-C 语言的动态特性提供支持，因此所有 Objective-C App 都会链接它。Objective-C runtime 库的支持函数实现在位于 `/usr/lib/libobjc.A.dylib` 的共享库中。

在使用 Objective-C 编程时，你通常不需要直接使用 Objective-C runtime 库。这个 API 主要用于在 Objective-C 与其他语言之间开发桥接层，或用于底层调试。

macOS 上 Objective-C runtime 库的实现是 Mac 平台独有的。对于其他平台，GNU Compiler Collection 提供了另一种具有类似 API 的实现。本文档只涵盖 macOS 的实现。

底层 Objective-C runtime API 在 OS X 10.5 版本中有重大更新。许多函数以及所有现有的数据结构都被替换为新的函数。旧的函数和结构体在 32 位模式下已废弃，在 64 位模式下不存在。这个 API 即使在 64 位模式下，也将若干值限制为 32 位整数——类的数量、协议的数量、每个类的方法数、每个类的实例变量数、每个方法的参数数、每个方法的所有参数大小（sizeof），以及类的版本号。此外，新的 Objective-C ABI（本文不做描述）进一步将 `sizeof(anInstance)` 限制为 32 位，并将另外三个值限制为 24 位——每个类的方法数、每个类的实例变量数，以及单个实例变量的大小（sizeof）。最后，已过时的 `NXHashTable` 和 `NXMapTable` 被限制为最多 40 亿个条目。

> [!note] String encoding
> runtime API 中所有的 `char *` 都应视为采用 UTF-8 编码。

下文中的「已废弃」指「在 OS X 10.5 版本中针对 32 位代码已废弃，且在 64 位代码中不允许使用」。

### Who Should Read This Document

本文档面向可能有兴趣了解 Objective-C runtime 的读者。

由于本文档不是一篇讲 C 语言的文档，它假定读者对该语言已有一定的了解。不过，不需要非常深入的了解。

## Topics

### Working with Classes

- [class_getName](<class_getname(__).md>) — 返回一个类的名称。
- [class_getSuperclass](<class_getsuperclass(__).md>) — 返回一个类的超类。
- [class_setSuperclass](<class_setsuperclass(____).md>) — 设置给定类的超类。_(已废弃)_
- [class_isMetaClass](<class_ismetaclass(__).md>) — 返回一个布尔值，指示某个类对象是否为元类。
- [class_getInstanceSize](<class_getinstancesize(__).md>) — 返回一个类的实例的大小。
- [class_getInstanceVariable](<class_getinstancevariable(____).md>) — 返回给定类中指定实例变量的 `Ivar`。
- [class_getClassVariable](<class_getclassvariable(____).md>) — 返回给定类中指定类变量的 `Ivar`。
- [class_addIvar](<class_addivar(__________).md>) — 向一个类添加一个新的实例变量。
- [class_copyIvarList](<class_copyivarlist(____).md>) — 描述某个类声明的实例变量。
- [class_getIvarLayout](<class_getivarlayout(__).md>) — 返回给定类的 `Ivar` 布局的描述。
- [class_setIvarLayout](<class_setivarlayout(____).md>) — 设置给定类的 `Ivar` 布局。
- [class_getWeakIvarLayout](<class_getweakivarlayout(__).md>) — 返回给定类中弱 `Ivar` 布局的描述。
- [class_setWeakIvarLayout](<class_setweakivarlayout(____).md>) — 设置给定类中弱 `Ivar` 的布局。
- [class_getProperty](<class_getproperty(____).md>) — 返回给定类中具有给定名称的属性。
- [class_copyPropertyList](<class_copypropertylist(____).md>) — 描述某个类声明的属性。
- [class_addMethod](<class_addmethod(________).md>) — 以给定的名称和实现向一个类添加一个新方法。
- [class_getInstanceMethod](<class_getinstancemethod(____).md>) — 返回给定类中指定的实例方法。
- [class_getClassMethod](<class_getclassmethod(____).md>) — 返回一个指针，指向描述给定类中指定类方法的数据结构。
- [class_copyMethodList](<class_copymethodlist(____).md>) — 描述某个类实现的实例方法。
- [class_replaceMethod](<class_replacemethod(________).md>) — 替换给定类中某个方法的实现。
- [class_getMethodImplementation](<class_getmethodimplementation(____).md>) — 返回向某个类的实例发送特定消息时会被调用的函数指针。
- [class_getMethodImplementation_stret](<class_getmethodimplementation_stret(____).md>) — 返回向某个类的实例发送特定消息时会被调用的函数指针。
- [class_respondsToSelector](<class_respondstoselector(____).md>) — 返回一个布尔值，指示某个类的实例是否响应特定的选择器（selector）。
- [class_addProtocol](<class_addprotocol(____).md>) — 向一个类添加一个协议。
- [class_addProperty](<class_addproperty(________).md>) — 向一个类添加一个属性。
- [class_replaceProperty](<class_replaceproperty(________).md>) — 替换一个类的某个属性。
- [class_conformsToProtocol](<class_conformstoprotocol(____).md>) — 返回一个布尔值，指示某个类是否符合给定的协议。
- [class_copyProtocolList](<class_copyprotocollist(____).md>) — 描述某个类采用的协议。
- [class_getVersion](<class_getversion(__).md>) — 返回一个类定义的版本号。
- [class_setVersion](<class_setversion(____).md>) — 设置一个类定义的版本号。
- [objc_setFutureClass](1808430-objc_setfutureclass.md) — 由 CoreFoundation 的免费桥接（toll-free bridging）使用。

### Adding Classes

- [objc_allocateClassPair](<objc_allocateclasspair(______).md>) — 创建一个新的类及其元类。
- [objc_disposeClassPair](<objc_disposeclasspair(__).md>) — 销毁一个类及其关联的元类。
- [objc_registerClassPair](<objc_registerclasspair(__).md>) — 注册一个使用 [objc_allocateClassPair](<objc_allocateclasspair(______).md>) 分配的类。
- [objc_duplicateClass](<objc_duplicateclass(______).md>) — 由 Foundation 的键值观察使用。

### Instantiating Classes

- [class_createInstance](<class_createinstance(____).md>) — 创建一个类的实例，在默认的 malloc 内存区中为该类分配内存。

### Working with Instances

- [object_getIndexedIvars](<object_getindexedivars(__).md>) — 返回一个指针，指向随给定实例对象分配的任何额外字节。
- [object_getIvar](<object_getivar(____).md>) — 读取对象中某个实例变量的值。
- [object_setIvar](<object_setivar(______).md>) — 设置对象中某个实例变量的值。
- [object_getClassName](<object_getclassname(__).md>) — 返回给定对象的类名。
- [object_getClass](<object_getclass(__).md>) — 返回一个对象的类。
- [object_setClass](<object_setclass(____).md>) — 设置一个对象的类。

### Obtaining Class Definitions

- [objc_getClassList](<objc_getclasslist(____).md>) — 获取已注册的类定义列表。
- [objc_copyClassList](<objc_copyclasslist(__).md>) — 创建并返回一个指向所有已注册类定义的指针列表。
- [objc_lookUpClass](<objc_lookupclass(__).md>) — 返回指定类的类定义。
- [objc_getClass](<objc_getclass(__).md>) — 返回指定类的类定义。
- [objc_getRequiredClass](<objc_getrequiredclass(__).md>) — 返回指定类的类定义。
- [objc_getMetaClass](<objc_getmetaclass(__).md>) — 返回指定类的元类定义。

### Working with Instance Variables

- [ivar_getName](<ivar_getname(__).md>) — 返回一个实例变量的名称。
- [ivar_getTypeEncoding](<ivar_gettypeencoding(__).md>) — 返回一个实例变量的类型字符串。
- [ivar_getOffset](<ivar_getoffset(__).md>) — 返回一个实例变量的偏移量。

### Associative References

- [objc_setAssociatedObject](<objc_setassociatedobject(________).md>) — 使用给定的键和关联策略为给定对象设置一个关联值。
- [objc_getAssociatedObject](<objc_getassociatedobject(____).md>) — 返回给定对象在给定键下关联的值。
- [objc_removeAssociatedObjects](<objc_removeassociatedobjects(__).md>) — 移除给定对象的所有关联。

### Working with Methods

- [method_getName](<method_getname(__).md>) — 返回一个方法的名称。
- [method_getImplementation](<method_getimplementation(__).md>) — 返回一个方法的实现。
- [method_getTypeEncoding](<method_gettypeencoding(__).md>) — 返回一个描述方法参数和返回类型的字符串。
- [method_copyReturnType](<method_copyreturntype(__).md>) — 返回一个描述方法返回类型的字符串。
- [method_copyArgumentType](<method_copyargumenttype(____).md>) — 返回一个描述方法单个参数类型的字符串。
- [method_getReturnType](<method_getreturntype(______).md>) — 通过引用返回一个描述方法返回类型的字符串。
- [method_getNumberOfArguments](<method_getnumberofarguments(__).md>) — 返回一个方法所接受的参数数量。
- [method_getArgumentType](<method_getargumenttype(________).md>) — 通过引用返回一个描述方法单个参数类型的字符串。
- [method_getDescription](<method_getdescription(__).md>) — 返回指定方法的方法描述结构体。_(已废弃)_
- [method_setImplementation](<method_setimplementation(____).md>) — 设置一个方法的实现。
- [method_exchangeImplementations](<method_exchangeimplementations(____).md>) — 交换两个方法的实现。

### Working with Libraries

- [objc_copyImageNames](<objc_copyimagenames(__).md>) — 返回所有已加载的 Objective-C 框架和动态库的名称。
- [class_getImageName](<class_getimagename(__).md>) — 返回某个类所来源的动态库的名称。
- [objc_copyClassNamesForImage](<objc_copyclassnamesforimage(____).md>) — 返回指定库或框架内所有类的名称。

### Working with Selectors

- [sel_getName](<sel_getname(__).md>) — 返回给定选择器（selector）所指定方法的名称。
- [sel_registerName](<sel_registername(__).md>) — 向 Objective-C runtime 系统注册一个方法，将方法名称映射为一个选择器，并返回该选择器的值。
- [sel_getUid](<sel_getuid(__).md>) — 向 Objective-C runtime 系统注册一个方法名称。
- [sel_isEqual](<sel_isequal(____).md>) — 返回一个布尔值，指示两个选择器是否相等。

### Working with Protocols

- [objc_getProtocol](<objc_getprotocol(__).md>) — 返回指定的协议。
- [objc_copyProtocolList](<objc_copyprotocollist(__).md>) — 返回一个数组，包含 runtime 已知的所有协议。
- [objc_allocateProtocol](<objc_allocateprotocol(__).md>) — 创建一个新的协议实例。
- [objc_registerProtocol](<objc_registerprotocol(__).md>) — 向 Objective-C runtime 注册一个新创建的协议。
- [protocol_addMethodDescription](<protocol_addmethoddescription(__________).md>) — 向一个协议添加一个方法。
- [protocol_addProtocol](<protocol_addprotocol(____).md>) — 将一个已注册的协议添加到另一个正在构建中的协议。
- [protocol_addProperty](<protocol_addproperty(____________).md>) — 向一个正在构建中的协议添加一个属性。
- [protocol_getName](<protocol_getname(__).md>) — 返回一个协议的名称。
- [protocol_isEqual](<protocol_isequal(____).md>) — 返回一个布尔值，指示两个协议是否相等。
- [protocol_copyMethodDescriptionList](<protocol_copymethoddescriptionlist(________).md>) — 返回一个数组，包含给定协议中符合给定规范的方法的方法描述。
- [protocol_getMethodDescription](<protocol_getmethoddescription(________).md>) — 返回给定协议中指定方法的方法描述结构体。
- [protocol_copyPropertyList](<protocol_copypropertylist(____).md>) — 返回一个数组，包含某个协议声明的属性。
- [protocol_getProperty](<protocol_getproperty(________).md>) — 返回给定协议中指定的属性。
- [protocol_copyProtocolList](<protocol_copyprotocollist(____).md>) — 返回一个数组，包含某个协议采用的协议。
- [protocol_conformsToProtocol](<protocol_conformstoprotocol(____).md>) — 返回一个布尔值，指示一个协议是否符合另一个协议。

### Working with Properties

- [property_getName](<property_getname(__).md>) — 返回一个属性的名称。
- [property_getAttributes](<property_getattributes(__).md>) — 返回一个属性的特性字符串。
- [property_copyAttributeValue](<property_copyattributevalue(____).md>) — 根据给定的特性名称返回属性特性的值。
- [property_copyAttributeList](<property_copyattributelist(____).md>) — 返回给定属性的属性特性数组。

### Using Objective-C Language Features

- [objc_enumerationMutation](<objc_enumerationmutation(__).md>) — 在 foreach 迭代过程中检测到变更时由编译器插入。
- [objc_setEnumerationMutationHandler](<objc_setenumerationmutationhandler(__).md>) — 设置当前的变更处理程序。
- [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) — 创建一个函数指针，在该方法被调用时调用指定的 block。
- [imp_getBlock](<imp_getblock(__).md>) — 返回与某个使用 [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) 创建的 `IMP` 关联的 block。
- [imp_removeBlock](<imp_removeblock(__).md>) — 将一个 block 从使用 [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) 创建的 `IMP` 中解除关联，并释放所创建的该 block 的副本。
- [objc_loadWeak](<objc_loadweak(__).md>) — 加载弱指针所引用的对象并返回它。
- [objc_storeWeak](<objc_storeweak(____).md>) — 在一个 `__weak` 变量中存储一个新值。

### Class-Definition Data Structures

- [Method](method.md) — 一个不透明类型，表示类定义中的一个方法。
- [Ivar](ivar.md) — 一个不透明类型，表示一个实例变量。
- [Category](category.md) — 一个不透明类型，表示一个分类。
- [objc_property_t](objc_property_t.md) — 一个不透明类型，表示一个 Objective-C 声明的属性。
- [IMP](imp.md) — 一个指向方法实现起始位置的指针。
- [objc_method_description](objc_method_description.md) — 定义一个 Objective-C 方法。
- [objc_cache](objc_cache.md) — 针对方法调用的性能优化。包含指向最近使用过的方法的指针。
- [objc_property_attribute_t](objc_property_attribute_t.md) — 定义一个属性特性。

### Instance Data Types

- [objc_object](objc_object.md) — 表示一个类的实例。
- [objc_super](objc_super-swift.struct.md) — 指定一个实例的超类。

### Associative References

- [objc_AssociationPolicy](objc_associationpolicy.md) — 用于指定关联行为的类型。

## See Also

### Related Documentation

- [Objective-C Runtime Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008048)

### Reference

- [Objective-C Structures](objective-c-structures.md)
- [Objective-C Constants](objective-c-constants.md)
- [Objective-C Functions](objective-c-functions.md)
- [Objective-C Data Types](objective-c-data-types.md)
- [Objective-C Macros](objective-c-macros.md)
- [Objective-C Enumerations](objective-c-enums.md)
