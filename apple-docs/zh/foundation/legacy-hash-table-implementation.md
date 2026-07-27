---
title: 旧版哈希表实现
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/legacy-hash-table-implementation
source_url: 'https://developer.apple.com/documentation/foundation/legacy-hash-table-implementation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/legacy-hash-table-implementation.json'
content_hash: 'sha256:40dcf14cd80c0039'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [Collections](collections.md) · [NSHashTable](nshashtable.md)

# 旧版哈希表实现

<sub>API 集合</sub>

## 主题

### 函数

- [NSAllHashTableObjects](<nsallhashtableobjects(__).md>) — 返回指定哈希表中的所有元素。
- [NSCompareHashTables](<nscomparehashtables(____).md>) — 返回一个布尔值，指示两个哈希表的元素是否相等。
- [NSCopyHashTableWithZone](<nscopyhashtablewithzone(____).md>) — 对指定的哈希表执行浅拷贝。
- [NSCountHashTable](<nscounthashtable(__).md>) — 返回哈希表中元素的数量。
- [NSCreateHashTable](<nscreatehashtable(____).md>) — 创建并返回一个新的哈希表。
- [NSCreateHashTableWithZone](<nscreatehashtablewithzone(______).md>) — 在给定的区域中创建一个新的哈希表。
- [NSEndHashTableEnumeration](<nsendhashtableenumeration(__).md>) — 在使用完某个枚举器后调用。
- [NSEnumerateHashTable](<nsenumeratehashtable(__).md>) — 为指定的哈希表创建一个枚举器。
- [NSFreeHashTable](<nsfreehashtable(__).md>) — 删除指定的哈希表。
- [NSHashGet](<nshashget(____).md>) — 返回哈希表中的一个元素。
- [NSHashInsert](<nshashinsert(____).md>) — 向指定的哈希表添加一个元素。
- [NSHashInsertIfAbsent](<nshashinsertifabsent(____).md>) — 仅当哈希表中尚不包含该元素时，才向指定的哈希表添加该元素。
- [NSHashInsertKnownAbsent](<nshashinsertknownabsent(____).md>) — 向指定的哈希表添加一个元素。
- [NSHashRemove](<nshashremove(____).md>) — 从指定的哈希表中移除一个元素。
- [NSNextHashEnumeratorItem](<nsnexthashenumeratoritem(__).md>) — 返回枚举中的下一个哈希表元素。
- [NSResetHashTable](<nsresethashtable(__).md>) — 删除指定哈希表中的元素。
- [NSStringFromHashTable](<nsstringfromhashtable(__).md>) — 返回描述哈希表内容的字符串。

### 数据类型

- [NSHashEnumerator](nshashenumerator.md) — 每次将该结构体传递给 [NSNextHashEnumeratorItem](<nsnexthashenumeratoritem(__).md>) 时，都能依次返回哈希表中的元素。
- [NSHashTableCallBacks](nshashtablecallbacks.md) — 定义一个结构体，其中包含用于配置 `NSHashTable` 针对哈希表内元素行为的函数指针。
- [NSHashTableOptions](nshashtableoptions.md) — 位字段中的组成部分，用于指定 [NSHashTable](nshashtable.md) 对象中元素的行为。

### 常量

- [NSIntegerHashCallBacks](nsintegerhashcallbacks.md) — 用于 `NSInteger` 大小或更小的数量集合（例如 `int`、`long` 或 `unichar`）。
- [NSNonOwnedPointerHashCallBacks](nsnonownedpointerhashcallbacks.md) — 用于指针集合，按地址进行哈希。
- [NSNonRetainedObjectHashCallBacks](nsnonretainedobjecthashcallbacks.md) — 用于对象集合，但不进行保留/释放。
- [NSObjectHashCallBacks](nsobjecthashcallbacks.md) — 用于对象集合（类似于 `NSSet`）。
- [NSOwnedObjectIdentityHashCallBacks](nsownedobjectidentityhashcallbacks.md) — 用于对象集合，在插入时转移所有权，使用指针相等性判断。
- [NSOwnedPointerHashCallBacks](nsownedpointerhashcallbacks.md) — 用于指针集合，在插入时转移所有权。
- [NSPointerToStructHashCallBacks](nspointertostructhashcallbacks.md) — 用于指向结构体的指针集合，当该结构体的第一个字段为 `int` 大小时使用。

## 另请参阅

### 已废弃
</content>
