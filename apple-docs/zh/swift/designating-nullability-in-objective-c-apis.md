---
title: 在 Objective-C API 中标注 Nullability
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/designating-nullability-in-objective-c-apis
source_url: 'https://developer.apple.com/documentation/swift/designating-nullability-in-objective-c-apis'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/designating-nullability-in-objective-c-apis.json'
content_hash: 'sha256:5c2fed44a81cd968'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Objective-C 与 C 代码自定义](objective-c-and-c-code-customization.md)

# 在 Objective-C API 中标注 Nullability

<sub>文章</sub>

使用 nullability 标注或将区域标记为已标注，以控制 Objective-C 声明如何被导入到 Swift。

## 概述

在 Objective-C 中，你使用可能为 null 的指针（在 Objective-C 中称为 `nil`）来引用对象。在 Swift 中，所有值（包括对象实例）都保证是非 null 的。相反，你将可能缺失的值表示为包装在可选类型（optional type）中。当你需要指示某个值缺失时，你使用 `nil` 值。

你可以在 Objective-C 代码中标注声明，以指示一个实例是否可以具有 null 或 `nil` 值。这些标注会改变 Swift 导入声明的方式。关于 Swift 如何导入未标注声明的示例，请考虑以下代码：

```occ
@interface MyList : NSObject
- (MyListItem *)itemWithName:(NSString *)name;
- (NSString *)nameForItem:(MyListItem *)item;
@property (copy) NSArray<MyListItem *> *allItems;
@end
```

Swift 会将每个对象实例参数、返回值以及属性导入为隐式封装的可选值（implicitly wrapped optional）：

```swift
class MyList: NSObject {
    func item(withName name: String!) -> MyListItem!
    func name(for item: MyListItem!) -> String!
    var allItems: [MyListItem]!
}
```

### 标注单个声明的 Nullability

你可以使用 Objective-C 代码中的 nullability 标注，来指定参数类型、属性类型或返回类型是否可为 null。对于简单对象或 block 指针的属性声明、参数类型和返回类型，可以使用 `nullable`、`nonnull` 和 `null_resettable` 属性标注。如果没有为某个类型提供 nullability 信息，Swift 将不会区分可选引用和非可选引用，并将该类型导入为隐式解包的可选值（implicitly unwrapped optional）。

以下列表描述了 Swift 如何导入具有不同 nullability 标注的类型：

- 非 null（Nonnullable）——导入为非可选值，无论是直接标注还是因为包含在已标注区域中
- 可为 null（Nullable）——导入为可选值
- 没有 nullability 标注或带有 `null_resettable` 标注——导入为隐式解包的可选值

以下代码展示了标注后的 `MyList` 类型。两个方法的返回类型被标注为 `nullable`，因为如果列表不包含给定的列表项或名称，这些方法会返回 `nil`。所有其他对象实例都被标注为 `nonnull`。

```occ
@interface MyList : NSObject
- (nullable MyListItem *)itemWithName:(nonnull NSString *)name;
- (nullable NSString *)nameForItem:(nonnull MyListItem *)item;
@property (copy, nonnull) NSArray<MyListItem *> *allItems;
@end
```

有了这些标注，Swift 在导入 `MyList` 类型时就不再使用任何隐式封装的可选值：

```swift
class MyList: NSObject {
    func item(withName name: String) -> MyListItem?
    func name(for item: MyListItem) -> String?
    var allItems: [MyListItem]
}
```

`nullable` 和 `nonnull` 标注是 `_Nullable` 和 `_Nonnull` 标注的简化形式，在几乎所有你会在指针类型上使用 `const` 关键字的上下文中都可以使用 `_Nullable` 和 `_Nonnull`。复杂的指针类型（例如 `id *`）必须显式使用这些标注进行标注。例如，要指定一个指向可为 null 对象引用的非 null 指针，请使用 `_Nullable id * _Nonnull`。

### 将区域标注为非 null

你可以通过将整个区域标记为已进行 nullability 审查，来简化标注 Objective-C 代码的过程。在由 `NS_ASSUME_NONNULL_BEGIN` 和 `NS_ASSUME_NONNULL_END` 宏界定的代码段内，你只需标注可为 null 的类型声明。已审查区域中未标注的声明将被视为非 null。

将 `MyList` 声明标记为已进行 nullability 审查，可以减少所需的标注数量。Swift 导入该类型的方式与上一节相同。

```occ
NS_ASSUME_NONNULL_BEGIN

@interface MyList : NSObject
- (nullable MyListItem *)itemWithName:(NSString *)name;
- (nullable NSString *)nameForItem:(MyListItem *)item;
@property (copy) NSArray<MyListItem *> *allItems;
@end

NS_ASSUME_NONNULL_END
```

请注意，`typedef` 类型即使在已审查区域内也不会被假定为非 null，因为它们本身并不是可为 null 的。

## 另请参阅

### 自定义 Objective-C API

- [为 Swift 重命名 Objective-C API](renaming-objective-c-apis-for-swift.md) —— 使用 `NS_SWIFT_NAME` 宏为 Swift 自定义 API 名称。
- [改进用于 Swift 的 Objective-C API 声明](improving-objective-c-api-declarations-for-swift.md) —— 使用 `NS_REFINED_FOR_SWIFT` 宏更改 API 导入 Swift 的方式。
- [对相关的 Objective-C 常量进行分组](grouping-related-objective-c-constants.md) —— 为 Objective-C 类型添加宏，以便在 Swift 中对其值进行分组。
- [在 Objective-C 中标注 API 可用性](marking-api-availability-in-objective-c.md) —— 使用宏来指示 Objective-C API 的可用性。
- [使 Objective-C API 在 Swift 中不可用](making-objective-c-apis-unavailable-in-swift.md) —— 使用 `NS_SWIFT_UNAVAILABLE` 宏防止 API 在 Swift 中使用。
