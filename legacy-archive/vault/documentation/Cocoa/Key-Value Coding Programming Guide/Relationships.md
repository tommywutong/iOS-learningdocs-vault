---
title: 键值编码编程指南
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/Relationships.html
archived_at: '2026-07-15T07:16:15.084456Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [键值编码编程指南](index.md)



## 描述属性关系

类描述提供了一种描述类中对一和对多属性的方法。定义类属性之间的这些关系，可以通过键值编码更智能、更灵活地操作这些属性。

### 类描述

`NSClassDescription` 是一个基类，提供用于获取类元数据的接口。类描述对象记录特定类对象可用的属性，以及该类对象与其他对象之间的关系（一对一、一对多和反向关系）。例如，`attributeKeys` 方法返回为某个类定义的所有属性列表；`toManyRelationshipKeys` 和 `toOneRelationshipKeys` 方法返回定义对多和对一关系的键数组；`inverseRelationshipKey:` 则返回关系目标指回接收者的关系名称。

`NSClassDescription` 并未定义用于建立这些关系的方法，具体子类必须定义它们。创建类描述后，使用 `NSClassDescription` 的 `registerClassDescription:forClass:` 类方法注册该描述。

`NSScriptClassDescription` 是 Cocoa 提供的唯一 `NSClassDescription` 具体子类，它封装了应用的脚本信息。

[添加验证](Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tglkdjjbeiqsiinba)

[针对性能进行设计](Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tklkdjjbeiqsiinba)
