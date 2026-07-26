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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_enumerateClasses

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void objc_enumerateClasses(const void *image, const char *namePrefix, Protocol *conformingTo, Class subclassing, void (^)(Class, _Bool *)block);
```

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
