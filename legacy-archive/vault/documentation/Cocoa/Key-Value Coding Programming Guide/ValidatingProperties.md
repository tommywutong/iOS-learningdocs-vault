---
title: 键值编码编程指南
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/ValidatingProperties.html
archived_at: '2026-07-15T07:16:16.598036Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [键值编码编程指南](index.md)



## 验证属性

键值编码协议定义了支持属性验证的方法。正如可以使用基于键的访问器读写符合键值编码规范的对象属性一样，也可以按键（或键路径）验证属性。调用 [validateValue:forKey:error:](https://developer.apple.com/documentation/objectivec/nsobject/1416754-validatevalue)（或 [validateValue:forKeyPath:error:](https://developer.apple.com/documentation/objectivec/nsobject/1416245-validatevalue)）方法时，协议的默认实现会在接收验证消息的对象（或键路径末端的对象）中搜索名称符合 `validate<Key>:error:` 模式的方法。如果对象没有这样的方法，验证默认成功，默认实现返回 `YES`（`true`）。如果存在特定于属性的验证方法，默认实现会改为返回调用该方法的结果。

由于特定于属性的验证方法通过引用接收值参数和错误参数，因此验证可能产生三种结果：

1. 验证方法认为值对象有效，在不修改值或错误的情况下返回 `YES`（`true`）。
2. 验证方法认为值对象无效，但选择不修改它。此时，该方法返回 `NO`（`false`），并将错误引用（如果调用者提供）设为说明失败原因的 `NSError` 对象。
3. 验证方法认为值对象无效，但创建一个新的有效对象作为替代。此时，该方法返回 `YES`（`true`），并保持错误对象不变。返回前，方法会修改值引用，使其指向新的值对象。进行修改时，方法始终创建新对象，而不修改旧对象，即使值对象本身可变也是如此。

清单 6-1 展示了如何对姓名字符串调用验证。

__清单 6-1__　验证 `name` 属性

1. `Person* person = [[Person alloc] init];`
2. `NSError* error;`
3. `NSString* name = @"John";`
4. `if (![person validateValue:&name forKey:@"name" error:&error]) {`
5. `NSLog(@"%@",error);`
6. `}`

### 自动验证

通常，键值编码协议及其默认实现都没有定义自动执行验证的机制。你应在适合应用的时机使用验证方法。

某些其他 Cocoa 技术会在特定情况下自动执行验证。例如，Core Data 会在保存托管对象上下文时自动执行验证（参阅《[Core Data 编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)》）。此外，在 macOS 中，Cocoa 绑定允许你指定自动执行验证（更多信息请参阅《[Cocoa 绑定编程主题](../Cocoa%20Bindings%20Programming%20Topics/Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3do2i)》）。

[表示非对象值](DataTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tclkciffekqkjivcq)

[访问器搜索模式](SearchImplementation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2tklkdjjbeeqsgizaq)
