---
title: NSKeyValueObserving
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nskeyvalueobserving
source_url: 'https://developer.apple.com/documentation/objectivec/nskeyvalueobserving'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nskeyvalueobserving.json'
content_hash: 'sha256:e01f4840b044f834'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# NSKeyValueObserving

<sub>API 集合</sub>

一个非正式协议，对象采用它来接收其他对象指定属性变化的通知。

## 概述

你可以观察任何对象属性，包括简单特性、一对一关系和一对多关系。一对多关系的观察者会被告知所做变化的类型——以及变化中涉及哪些对象。

[NSObject](nsobject-swift.class.md) 提供了 [NSKeyValueObserving](nskeyvalueobserving.md) 协议的一个实现，为所有对象提供自动观察能力。你可以通过禁用自动观察者通知、并使用该协议中的方法实现手动通知，来进一步细化通知行为。

## 主题

### Change Notification

- [- observeValueForKeyPath:ofObject:change:context:](<nsobject-swift.class/observevalue(forkeypath_of_change_context_).md>) — 当被观察对象相对指定键路径处的值发生变化时通知观察对象。

### Registering for Observation

- [- addObserver:forKeyPath:options:context:](<nsobject-swift.class/addobserver(__forkeypath_options_context_).md>) — 注册观察者对象，以接收相对于接收此消息的对象的指定键路径的 KVO 通知。
- [- removeObserver:forKeyPath:](<nsobject-swift.class/removeobserver(__forkeypath_).md>) — 停止观察者对象接收相对于接收此消息的对象、由键路径指定的属性的变化通知。
- [- removeObserver:forKeyPath:context:](<nsobject-swift.class/removeobserver(__forkeypath_context_).md>) — 在给定上下文的情况下，停止观察者对象接收相对于接收此消息的对象、由键路径指定的属性的变化通知。

### Notifying Observers of Changes

- [- willChangeValueForKey:](<nsobject-swift.class/willchangevalue(forkey_).md>) — 告知被观察对象，某给定属性的值即将变化。
- [- didChangeValueForKey:](<nsobject-swift.class/didchangevalue(forkey_).md>) — 告知被观察对象，某给定属性的值已经变化。
- [- willChange:valuesAtIndexes:forKey:](<nsobject-swift.class/willchange(__valuesat_forkey_).md>) — 告知被观察对象，对于指定的有序一对多关系，某个指定变化即将在给定索引处执行。
- [- didChange:valuesAtIndexes:forKey:](<nsobject-swift.class/didchange(__valuesat_forkey_).md>) — 告知被观察对象，对于指定的有序一对多关系，某个指定变化已在给定索引处发生。
- [- willChangeValueForKey:withSetMutation:usingObjects:](<nsobject-swift.class/willchangevalue(forkey_withsetmutation_using_).md>) — 告知被观察对象，即将对指定的无序一对多关系做出指定变化。
- [- didChangeValueForKey:withSetMutation:usingObjects:](<nsobject-swift.class/didchangevalue(forkey_withsetmutation_using_).md>) — 告知被观察对象，已对指定的无序一对多关系做出指定变化。

### Observing Customization

- [+ automaticallyNotifiesObserversForKey:](<nsobject-swift.class/automaticallynotifiesobservers(forkey_).md>) — 返回一个布尔值，指示被观察对象是否支持对给定键的自动键值观察。
- [+ keyPathsForValuesAffectingValueForKey:](<nsobject-swift.class/keypathsforvaluesaffectingvalue(forkey_).md>) — 返回一组键路径，这些键路径对应的属性的值会影响指定键的值。
- [NSKeyValueObservingCustomization](../foundation/nskeyvalueobservingcustomization.md) — 使用键值观察并不要求遵循 NSKeyValueObservingCustomization。如果你需要针对某个键禁用自动通知，或添加依赖键，就提供这些函数的实现
- [observationInfo](nsobject-swift.class/observationinfo.md) — 返回一个指针，标识与被观察对象上已注册的所有观察者相关的信息。

### 常量

- [NSKeyValueObservation](../foundation/nskeyvalueobservation.md)
- [NSKeyValueObservedChange](../foundation/nskeyvalueobservedchange.md)
- [NSKeyValueChange](../foundation/nskeyvaluechange.md) — 可以被观察到的变化种类。
- [NSKeyValueObservingOptions](../foundation/nskeyvalueobservingoptions.md) — 可以在变化字典中返回的值。
- [NSKeyValueChangeKey](../foundation/nskeyvaluechangekey.md) — 可以出现在变化字典中的键。
- [NSKeyValueSetMutationKind](../foundation/nskeyvaluesetmutationkind.md)

## 另请参阅

### 相关文档

- [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i)
