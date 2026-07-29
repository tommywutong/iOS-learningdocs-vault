---
title: 检查 Core Data 特性
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/05/inspecting-core-data-attributes/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:18b00c7306a7e349'
translated: true
---

> 原文：[检查 Core Data 特性](https://oleb.net/blog/2011/05/inspecting-core-data-attributes/)　·　Ole Begemann

# 检查 Core Data 特性

在设计 Core Data 数据模型时，你可以为特性（attribute）选择多种数据类型。在你的托管对象模型（managed object model）中，许多这些数据类型（即 Integer 16、Integer 32、Integer 64、Double、Float 和 Bool）都是用 `NSNumber *` 类型的属性（property）建模的。

如果出于某种原因，你需要在代码中确定 Core Data 特性的底层数据类型，该怎么办？事实证明，使用 Core Data 的内省（introspection）API 很容易做到这一点。

# NSEntityDescription

你可能已经知道，Core Data 模型中的每个实体都由 `NSEntityDescription` 的一个实例（instance）表示。假设你有一个名为 "Person" 的实体（entity）：

```
NSEntityDescription *personEntity = [NSEntityDescription entityForName:@"Person" inManagedObjectContext:self.managedObjectContext];
```

# NSPropertyDescription 和 NSAttributeDescription

按照这个模式，实体的每个属性都由 `NSPropertyDescription` 子类（subclass）的一个实例表示，具体取决于我们处理的属性的类型：特性（attribute，由 `NSAttributeDescription` 表示）、关系（relationship，由 `NSRelationshipDescription` 表示）或获取属性（fetched property，由 `NSFetchedPropertyDescription` 表示）。

要遍历实体的所有属性，请执行以下操作：

```
for (NSPropertyDescription *property in eventEntity) {
    ...
}
```

如果你只对实体的特性感兴趣，`-attributesByName` 方法会返回一个字典，你可以遍历它，或者请求一个特定的特性。然后，`NSPropertyDescription` 和 `NSAttributeDescription` 类提供了检查特性属性的方法，例如 `-attributeType`：

```
NSDictionary *attributes = [eventEntity attributesByName];
NSAttributeDescription *ageAttribute = [attributes objectForKey:@"age"];
if ([ageAttribute attributeType == NSInteger32AttributeType]) {
    // 我们有一个 32 位 Integer
    ...
}
```

# NSAttributeType

`NSAttributeType` 的有效值列在 `NSAttributeDescription.h` 头文件中：

```
// 这些类型显式区分位宽，以确保
// 底层操作系统的数据存储独立性
enum {
    NSUndefinedAttributeType = 0,
    NSInteger16AttributeType = 100,
    NSInteger32AttributeType = 200,
    NSInteger64AttributeType = 300,
    NSDecimalAttributeType = 400,
    NSDoubleAttributeType = 500,
    NSFloatAttributeType = 600,
    NSStringAttributeType = 700,
    NSBooleanAttributeType = 800,
    NSDateAttributeType = 900,
    NSBinaryDataAttributeType = 1000
    // 如果你的特性是 NSTransformableAttributeType，则必须设置
    // attributeValueClassName 或特性值类必须实现 NSCopying。
    , NSTransformableAttributeType = 1800
    , NSObjectIDAttributeType = 2000
};

typedef NSUInteger NSAttributeType;
```
