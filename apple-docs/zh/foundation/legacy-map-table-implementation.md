---
title: 旧版映射表实现
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/legacy-map-table-implementation
source_url: 'https://developer.apple.com/documentation/foundation/legacy-map-table-implementation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/legacy-map-table-implementation.json'
content_hash: 'sha256:cb7daee4a7520aeb'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [集合](collections.md) · [NSMapTable](nsmaptable.md)

# 旧版映射表实现

<sub>API 集合</sub>

## 主题

### 函数

- [NSAllMapTableKeys](<nsallmaptablekeys(__).md>) — 返回指定映射表中的所有键。
- [NSAllMapTableValues](<nsallmaptablevalues(__).md>) — 返回指定表中的所有值。
- [NSCompareMapTables](<nscomparemaptables(____).md>) — 比较两个映射表中的元素是否相等。
- [NSCopyMapTableWithZone](<nscopymaptablewithzone(____).md>) — 对指定映射表执行浅拷贝。
- [NSCountMapTable](<nscountmaptable(__).md>) — 返回映射表中的元素数量。
- [NSCreateMapTable](<nscreatemaptable(______).md>) — 在默认区域中创建新的映射表。
- [NSCreateMapTableWithZone](<nscreatemaptablewithzone(________).md>) — 在指定区域中创建新的映射表。
- [NSEndMapTableEnumeration](<nsendmaptableenumeration(__).md>) — 在完成枚举器的使用时调用。
- [NSEnumerateMapTable](<nsenumeratemaptable(__).md>) — 为指定映射表创建枚举器。
- [NSFreeMapTable](<nsfreemaptable(__).md>) — 删除指定映射表。
- [NSMapGet](<nsmapget(____).md>) — 返回指定键对应的映射表值。
- [NSMapInsert](<nsmapinsert(______).md>) — 将键值对插入指定表中。
- [NSMapInsertIfAbsent](<nsmapinsertifabsent(______).md>) — 将键值对插入指定表中。
- [NSMapInsertKnownAbsent](<nsmapinsertknownabsent(______).md>) — 如果此前未添加过该键值对，则将其插入指定表中。
- [NSMapMember](<nsmapmember(________).md>) — 指示给定表是否包含给定键。
- [NSMapRemove](<nsmapremove(____).md>) — 从指定表中移除键及其对应的值。
- [NSNextMapEnumeratorPair](<nsnextmapenumeratorpair(______).md>) — 返回一个布尔值，指示枚举中的下一个映射表键值对是否已设置。
- [NSResetMapTable](<nsresetmaptable(__).md>) — 删除指定映射表中的元素。
- [NSStringFromMapTable](<nsstringfrommaptable(__).md>) — 返回描述映射表内容的字符串。

### 数据类型

- [NSMapEnumerator](nsmapenumerator.md) — 每次将此结构体传递给 [NSNextMapEnumeratorPair](<nsnextmapenumeratorpair(______).md>) 时，允许返回映射表中的后续元素。
- [NSMapTable](legacy-nsmaptable.md) — “管理映射表”中所述函数使用的不透明数据类型。
- [NSMapTableKeyCallBacks](nsmaptablekeycallbacks.md) — 用于配置 `NSMapTable` 如何处理映射表内键元素的函数指针。
- [NSMapTableOptions](nsmaptableoptions.md) — 用作位域组成部分的常量，用于指定 `NSMapTable` 对象中元素（键和值）的行为。
- [NSMapTableValueCallBacks](nsmaptablevaluecallbacks.md) — 用于配置 `NSMapTable` 如何处理映射表内值元素的函数指针。

### 常量

- [NSIntegerMapKeyCallBacks](nsintegermapkeycallbacks.md) — 用于大小不超过指针的键（例如 `int`、`long` 或 `unichar`）。
- [NSIntMapKeyCallBacks](nsintmapkeycallbacks.md) — 用于大小不超过指针的键（例如 `int`、`long` 或 `unichar`）。_(已废弃)_
- [NSNonOwnedPointerMapKeyCallBacks](nsnonownedpointermapkeycallbacks.md) — 用于不会被释放的指针键。
- [NSNonOwnedPointerOrNullMapKeyCallBacks](nsnonownedpointerornullmapkeycallbacks.md) — 用于不会被释放的指针键，或 `NULL`。
- [NSNonRetainedObjectMapKeyCallBacks](nsnonretainedobjectmapkeycallbacks.md) — 用于对象集合，但不进行保留/释放。
- [NSObjectMapKeyCallBacks](nsobjectmapkeycallbacks.md) — 用于对象键。
- [NSOwnedPointerMapKeyCallBacks](nsownedpointermapkeycallbacks.md) — 用于指针键，并在插入时转移所有权（ownership）。

### 常量

- [NSIntegerMapValueCallBacks](nsintegermapvaluecallbacks.md) — 用于大小不超过指针的值（例如 `int`、`long` 或 `unichar`）。
- [NSIntMapValueCallBacks](nsintmapvaluecallbacks.md) — 用于大小不超过指针的值（例如 `int`、`long` 或 `unichar`）。_(已废弃)_
- [NSNonOwnedPointerMapValueCallBacks](nsnonownedpointermapvaluecallbacks.md) — 用于非自有指针值。
- [NSOwnedPointerMapValueCallBacks](nsownedpointermapvaluecallbacks.md) — 用于自有指针值。
- [NSNonRetainedObjectMapValueCallBacks](nsnonretainedobjectmapvaluecallbacks.md) — 用于对象集合，但不进行保留/释放。
- [NSObjectMapValueCallBacks](nsobjectmapvaluecallbacks.md) — 用于对象值。

## 另请参阅

### 已废弃
