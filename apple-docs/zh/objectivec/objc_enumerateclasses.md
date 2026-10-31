---
title: objc_enumerateClasses
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_enumerateclasses
source_url: 'https://developer.apple.com/documentation/objectivec/objc_enumerateclasses'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_enumerateclasses.json'
content_hash: 'sha256:bee71f40ca7a0688'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_enumerateClasses

<sub>函数</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void objc_enumerateClasses(const void *image, const char *namePrefix, Protocol *conformingTo, Class subclassing, void (^)(Class, _Bool *)block);
```

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
