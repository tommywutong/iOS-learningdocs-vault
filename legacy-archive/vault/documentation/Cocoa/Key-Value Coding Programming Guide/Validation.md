---
title: 键值编码编程指南
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/Validation.html
archived_at: '2026-07-15T07:16:17.103945Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [键值编码编程指南](index.md)



## 添加验证

键值编码协议定义了按键或键路径验证属性的方法。这些方法的默认实现又依赖你定义遵循特定命名模式的方法，该模式与访问器方法所用模式类似。具体来说，需要为每个想要验证且名称为 `key` 的属性提供 `validate<Key>:error:` 方法。默认实现在响应基于键的 [validateValue:forKey:error:](https://developer.apple.com/documentation/objectivec/nsobject/1416754-validatevalue) 消息时，会搜索该方法。

如果没有为某个属性提供验证方法，无论其值如何，协议的默认实现都会假定该属性验证成功。这意味着验证是按属性逐个选择启用的。

### 实现验证方法

为属性提供验证方法时，该方法会通过引用接收两个参数：待验证的值对象，以及用于返回错误信息的 `NSError`。因此，验证方法可以采取以下三种操作之一：

- 如果值对象有效，则在不修改值对象或错误的情况下返回 `YES`（`true`）。
- 如果值对象无效，并且无法或不想提供有效替代值，请将错误参数设为说明失败原因的 `NSError` 对象，并返回 `NO`（`false`）。

- 如果值对象无效，但存在有效替代值，请创建有效对象，将值引用指向新对象，并在不修改错误引用的情况下返回 `YES`（`true`）。如果提供其他值，应始终返回新对象，而不是修改正在验证的对象，即使原对象可变也是如此。

清单 11-1 展示了用于 `name` 字符串属性的验证方法，它确保值对象不为 `nil`，且姓名达到最小长度。如果验证失败，该方法不会替换为其他值。

__清单 11-1__　`name` 属性的验证方法

1. `- (BOOL)validateName:(id *)ioValue error:(NSError * __autoreleasing *)outError{`
2. `if ((*ioValue == nil) || ([(NSString *)*ioValue length] < 2)) {`
3. `if (outError != NULL) {`
4. `*outError = [NSError errorWithDomain:PersonErrorDomain`
5. `code:PersonInvalidNameCode`
6. `userInfo:@{ NSLocalizedDescriptionKey`
7. `: @"Name too short" }];`
8. `}`
9. `return NO;`
10. `}`
11. `return YES;`
12. `}`

### 验证标量值

验证方法要求值参数是对象，因此非对象属性的值会装箱为 `NSValue` 或 `NSNumber` 对象，如[表示非对象值](DataTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tclkciffekqkjivcq)所述。清单 11-2 展示了标量属性 `age` 的验证方法。在本例中，一种潜在的无效情况是 `age` 值为 `nil`；该方法会创建值为零的有效值，并返回 `YES`（`true`）。你也可以在重写的 `setNilValueForKey:` 中处理这种特殊情况，因为类的使用者可能不会调用验证方法。

__清单 11-2__　标量属性的验证方法

1. `- (BOOL)validateAge:(id *)ioValue error:(NSError * __autoreleasing *)outError {`
2. `if (*ioValue == nil) {`
3. `// 值为 nil：也可以在 setNilValueForKey 中处理`
4. `*ioValue = @(0);`
5. `} else if ([*ioValue floatValue] < 0.0) {`
6. `if (outError != NULL) {`
7. `*outError = [NSError errorWithDomain:PersonErrorDomain`
8. `code:PersonInvalidAgeCode`
9. `userInfo:@{ NSLocalizedDescriptionKey`
10. `: @"Age cannot be negative" }];`
11. `}`
12. `return NO;`
13. `}`
14. `return YES;`
15. `}`

[处理非对象值](HandlingNon-ObjectValues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedklktk4yq)

[描述属性关系](Relationships.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2tmlkcijbuirchinbq)
