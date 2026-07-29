---
title: 持久化历史记录
framework: Core Data
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/persistent-history
source_url: 'https://developer.apple.com/documentation/coredata/persistent-history'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/persistent-history.json'
content_hash: 'sha256:84453809abb69386'
translated: true
---

> 导航：[技术](../technologies.md) · [Core Data](../coredata.md)

# 持久化历史记录

<sub>API 集合</sub>

使用持久化历史记录跟踪（persistent history tracking）功能，来确定在启用该功能后存储中发生了哪些更改。

## 主题

### 跟踪历史记录

- [NSPersistentHistoryToken](nspersistenthistorytoken.md) — 一个书签，用于追踪你已处理的最新历史记录。

### 请求历史记录

- [NSPersistentHistoryChangeRequest](nspersistenthistorychangerequest.md) — 用于获取或清除持久化历史记录的请求。
- [NSPersistentHistoryResult](nspersistenthistoryresult.md) — 获取持久化历史记录请求的结果。

### 读取历史记录

- [NSPersistentHistoryTransaction](nspersistenthistorytransaction.md) — 持久化历史记录中，基于某次上下文保存或批量操作的一组更改。
- [NSPersistentHistoryChange](nspersistenthistorychange.md) — 代表持久化存储中托管对象（managed object）的插入、更新或删除的更改。

## 另请参阅

### 处理更改

- [在存储发生变化时访问数据](accessing-data-when-the-store-changes.md) — 保证在你告诉上下文去查看之前，它不会看到存储的更改。
- [处理相关的存储更改](consuming-relevant-store-changes.md) — 筛选存储事务，以获取与当前视图相关的更改。
