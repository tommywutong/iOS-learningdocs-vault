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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_sync_enter

<sub>Function</sub>

Begin synchronizing on ‘obj’.
Allocates recursive pthread_mutex associated with ‘obj’ if needed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int objc_sync_enter(id obj);
```

## Parameters

- `obj` — The object to begin synchronizing on.

## Return Value

OBJC_SYNC_SUCCESS once lock is acquired.

## See Also

### Functions

- [class_createInstanceFromZone](class_createinstancefromzone.md) _(deprecated)_
- [class_lookupMethod](<class_lookupmethod(____).md>) _(deprecated)_
- [class_respondsToMethod](<class_respondstomethod(____).md>) _(deprecated)_
- [NXCompareHashTables](nxcomparehashtables.md) _(deprecated)_
- [NXCopyHashTable](nxcopyhashtable.md) _(deprecated)_
- [NXCountHashTable](nxcounthashtable.md) _(deprecated)_
- [NXCreateHashTable](nxcreatehashtable.md) _(deprecated)_
- [NXCreateHashTableFromZone](nxcreatehashtablefromzone.md) _(deprecated)_
- [NXEmptyHashTable](nxemptyhashtable.md) _(deprecated)_
- [NXFreeHashTable](nxfreehashtable.md) _(deprecated)_
- [NXHashGet](nxhashget.md) _(deprecated)_
- [NXHashInsert](nxhashinsert.md) _(deprecated)_
- [NXHashInsertIfAbsent](nxhashinsertifabsent.md) _(deprecated)_
- [NXHashMember](nxhashmember.md) _(deprecated)_
- [NXHashRemove](nxhashremove.md) _(deprecated)_
