---
title: 键值编码编程指南
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/Performance.html
archived_at: '2026-07-15T07:16:14.845281Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [键值编码编程指南](index.md)



## 针对性能进行设计

键值编码效率很高，尤其是在大部分工作都交给默认实现时；但它确实增加了一层间接访问，因此比直接调用方法略慢。只有在能够受益于键值编码所提供的灵活性，或需要让对象参与依赖键值编码的 Cocoa 技术时，才应使用它。

### 重写键值编码方法

通常，你会让对象继承自 `NSObject`，然后按本指南各处所述提供特定于属性的访问器及相关方法，使对象符合键值编码规范。很少需要重写 `valueForKey:`、`setValue:forKey:` 等键值编码访问器，或 `validateValue:forKey:` 等基于键的验证方法的默认实现。由于这些实现会缓存运行时环境信息以提高效率，如果确实要重写它们来引入自定义逻辑，请确保在返回前调用超类中的默认实现。

### 优化对多关系

实现对多关系时，索引式访问器在许多情况下都能显著提升性能，对可变集合尤其如此。更多信息请参阅[访问集合属性](AccessingCollectionProperties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedilktk4yq)和[定义集合方法](DefiningCollectionMethods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedcnznknltc)。

[描述属性关系](Relationships.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2tmlkcijbuirchinbq)

[规范符合性检查清单](Compliant.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3telkciffekqkjivcq)
