---
title: 键值编码编程指南
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/AccessingCollectionProperties.html
archived_at: '2026-07-15T07:16:10.051889Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [键值编码编程指南](index.md)



## 访问集合属性

符合键值编码规范的对象以与其他属性相同的方式公开其对多属性。你可以像处理其他对象一样，使用 `valueForKey:` 和 `setValue:forKey:`（或相应的键路径方法）获取或设置集合对象。不过，要操作这些集合的内容时，使用协议定义的可变代理方法通常效率最高。

该协议为集合对象访问定义了三组不同的代理方法，每组都包含键和键路径两个版本：

- [mutableArrayValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1416339-mutablearrayvalueforkey) 和 [mutableArrayValueForKeyPath:](https://developer.apple.com/documentation/objectivec/nsobject/1414937-mutablearrayvalueforkeypath)

  这些方法返回一个行为类似 `NSMutableArray` 对象的代理对象。
- [mutableSetValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415105-mutablesetvalueforkey) 和 [mutableSetValueForKeyPath:](https://developer.apple.com/documentation/objectivec/nsobject/1408115-mutablesetvalue)

  这些方法返回一个行为类似 `NSMutableSet` 对象的代理对象。
- [mutableOrderedSetValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415479-mutableorderedsetvalue) 和 [mutableOrderedSetValueForKeyPath:](https://developer.apple.com/documentation/objectivec/nsobject/1407188-mutableorderedsetvalue)

  这些方法返回一个行为类似 `NSMutableOrderedSet` 对象的代理对象。

当你操作代理对象，在其中添加、移除或替换对象时，协议的默认实现会相应地修改底层属性。相比先用 `valueForKey:` 获取不可变集合对象、创建内容经过修改的新集合，再用 `setValue:forKey:` 消息将其存回对象，这种方式效率更高。在许多情况下，它也比直接操作可变属性更高效。这些方法还有一项额外优势：能让集合中保存的对象继续符合键值观察规范（详情请参阅《[键值观察编程指南](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)》）。

[访问对象属性](BasicPrinciples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3talkciffekqkjivcq)

[使用集合运算符](CollectionOperators.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tmlkciffekqkjivcq)
