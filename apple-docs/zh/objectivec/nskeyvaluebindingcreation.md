---
title: NSKeyValueBindingCreation
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nskeyvaluebindingcreation
source_url: 'https://developer.apple.com/documentation/objectivec/nskeyvaluebindingcreation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nskeyvaluebindingcreation.json'
content_hash: 'sha256:a353c1304b60fd90'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# NSKeyValueBindingCreation

<sub>API 集合</sub>

一组方法，可用来在视图对象和控制器之间、或控制器和模型对象之间创建和移除绑定。

## 概述

[NSKeyValueBindingCreation](nskeyvaluebindingcreation.md) 这个非正式协议还为视图子类提供了一种方式，用来公布它所暴露的绑定。该协议由 [NSObject](nsobject-swift.class.md) 实现，其方法可以被视图和控制器子类重写。

创建新绑定时，会将接收者的绑定（例如视图对象的某个属性）与由键路径指定的可观察对象的某个属性关联起来。当可观察对象的指定属性的值发生变化时，接收者会通过键值观察机制收到通知。绑定还可以指定绑定选项，进一步自定观察对象与被观察对象之间的交互方式。

绑定被视为被绑定对象的一个属性，与绑定相关的所有信息都应由该对象所有。AppKit 对象（视图、单元格、表格列、控制器）上所有标准绑定在被释放时都会自动解除绑定，但如果你为其他类型的对象创建键值绑定，就需要确保在释放之前移除这些绑定（被观察对象对其观察者持有弱引用，因此控制器/模型对象可能会继续引用并向那些曾经绑定到它们的对象发送消息）。

对象之间的绑定通常在 Interface Builder 中使用 Bindings 检查器建立。但有时也必须以编程方式完成，例如在不同 nib 文件中的对象之间建立绑定时。

`NSView` 的子类可以通过为每个属性调用类方法 [+ exposeBinding:](<nsobject-swift.class/exposebinding(__).md>) 来将额外的符合键值编码/键值观察规范的属性暴露为绑定。这通常在类的 `initialize` 方法中完成。通过暴露对象所支持的绑定并创建一个 Interface Builder 面板，你可以让自己类的实例在 Interface Builder 中变得可绑定。

## 主题

### Exposing bindings

- [+ exposeBinding:](<nsobject-swift.class/exposebinding(__).md>) — 暴露指定的 `binding`，公布其可用性。
- [exposedBindings](nsobject-swift.class/exposedbindings.md) — 返回一个数组，包含接收者暴露的绑定。

### Managing bindings

- [- valueClassForBinding:](<nsobject-swift.class/valueclassforbinding(__).md>) — 返回指定绑定将要返回的值的类。
- [- bind:toObject:withKeyPath:options:](<nsobject-swift.class/bind(__to_withkeypath_options_).md>) — 在接收者的给定属性与给定对象由给定键路径指定的属性之间建立绑定。
- [- optionDescriptionsForBinding:](<nsobject-swift.class/optiondescriptionsforbinding(__).md>) — 返回一个数组，描述指定绑定的选项。
- [- infoForBinding:](<nsobject-swift.class/infoforbinding(__).md>) — 返回一个字典，描述接收者的 `binding`。
- [NSBindingInfoKey](../appkit/nsbindinginfokey.md)
- [- unbind:](<nsobject-swift.class/unbind(__).md>) — 移除接收者与控制器之间给定的绑定。
- [NSIsControllerMarker(_:)](<../appkit/nsiscontrollermarker(__).md>) — 测试给定对象是否为用于表示某个键相关的选择状态的特殊标记对象。

### 常量

- [NSBindingName](../appkit/nsbindingname.md) — 为某些方法指定绑定的值。
- [NSBindingOption](../appkit/nsbindingoption.md)
- [Binding Dictionary Keys](binding-dictionary-keys.md) — 以下值用作 [- infoForBinding:](<nsobject-swift.class/infoforbinding(__).md>) 返回的字典中的键

## 另请参阅

### 相关文档

- [Cocoa Bindings Reference](https://developer.apple.com/library/archive/documentation/Cocoa/Reference/CocoaBindingsRef/CocoaBindingsRef.html#//apple_ref/doc/uid/10000189i)
- [Cocoa Bindings Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html#//apple_ref/doc/uid/10000167i)

### Key-Value Coding

- [NSKeyValueCoding](nskeyvaluecoding.md) — 一种机制，可让你通过名称或键间接访问对象的属性。
- [NSScriptKeyValueCoding](nsscriptkeyvaluecoding.md) — 一组方法，为使用键值编码提供额外的能力。
- [NSScriptKeyValueCoding Exception Names](nsscriptkeyvaluecoding-exception-names.md) — 键值编码方法引发的异常。
