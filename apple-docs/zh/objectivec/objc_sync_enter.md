---
title: objc_sync_enter
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_sync_enter
source_url: 'https://developer.apple.com/documentation/objectivec/objc_sync_enter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_sync_enter.json'
content_hash: 'sha256:8a443419cb9c9e60'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_sync_enter

<sub>函数</sub>

Begin synchronizing on ‘obj’.
Allocates recursive pthread_mutex associated with ‘obj’ if needed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int objc_sync_enter(id obj);
```

## 参数

- `obj` — The object to begin synchronizing on.

## 返回值

OBJC_SYNC_SUCCESS once lock is acquired.

## 另请参阅

### 函数

- [class_createInstanceFromZone](class_createinstancefromzone.md) _(已废弃)_
- [class_lookupMethod](<class_lookupmethod(____).md>) _(已废弃)_
- [class_respondsToMethod](<class_respondstomethod(____).md>) _(已废弃)_
- [NXCompareHashTables](nxcomparehashtables.md) _(已废弃)_
- [NXCopyHashTable](nxcopyhashtable.md) _(已废弃)_
- [NXCountHashTable](nxcounthashtable.md) _(已废弃)_
- [NXCreateHashTable](nxcreatehashtable.md) _(已废弃)_
- [NXCreateHashTableFromZone](nxcreatehashtablefromzone.md) _(已废弃)_
- [NXEmptyHashTable](nxemptyhashtable.md) _(已废弃)_
- [NXFreeHashTable](nxfreehashtable.md) _(已废弃)_
- [NXHashGet](nxhashget.md) _(已废弃)_
- [NXHashInsert](nxhashinsert.md) _(已废弃)_
- [NXHashInsertIfAbsent](nxhashinsertifabsent.md) _(已废弃)_
- [NXHashMember](nxhashmember.md) _(已废弃)_
- [NXHashRemove](nxhashremove.md) _(已废弃)_
