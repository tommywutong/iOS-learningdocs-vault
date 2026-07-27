---
title: Objective-C 函数
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objective-c-functions
source_url: 'https://developer.apple.com/documentation/objectivec/objective-c-functions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objective-c-functions.json'
content_hash: 'sha256:92b51981409b08b3'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# Objective-C 函数

<sub>API 集合</sub>

## 主题

### 函数

- [autoreleasepool(invoking:)](<autoreleasepool(invoking_).md>)
- [class_lookupMethod](<class_lookupmethod(____).md>) _(已废弃)_
- [class_respondsToMethod](<class_respondstomethod(____).md>) _(已废弃)_
- [objc_addExceptionHandler](<objc_addexceptionhandler(____).md>)
- [objc_addLoadImageFunc](<objc_addloadimagefunc(__).md>)
- [objc_assertRegisteredThreadWithCollector](<objc_assertregisteredthreadwithcollector().md>) _(已废弃)_
- [objc_begin_catch](<objc_begin_catch(__).md>)
- [objc_clear_stack](<objc_clear_stack(__).md>) _(已废弃)_
- [objc_collect](<objc_collect(__).md>) _(已废弃)_
- [objc_collectableZone](<objc_collectablezone().md>) _(已废弃)_
- [objc_collecting_enabled](<objc_collecting_enabled().md>) _(已废弃)_
- [objc_collectingEnabled](<objc_collectingenabled().md>) _(已废弃)_
- [objc_end_catch](<objc_end_catch().md>)
- [objc_enumerateClasses(fromImage:matchingNamePrefix:conformingTo:subclassing:)](<objc_enumerateclasses(fromimage_matchingnameprefix_conformingto_subclassing_).md>)
- [objc_exception_rethrow](<objc_exception_rethrow().md>)
- [objc_exception_throw](<objc_exception_throw(__).md>) — 抛出一个 runtime 异常。这个函数由编译器插入到本来应该是 \\c @throw 的位置。
- [objc_finalizeOnMainThread](<objc_finalizeonmainthread(__).md>) _(已废弃)_
- [objc_is_finalized](<objc_is_finalized(__).md>) _(已废弃)_
- [objc_memmove_collectable](<objc_memmove_collectable(______).md>) _(已废弃)_
- [objc_registerThreadWithCollector](<objc_registerthreadwithcollector().md>) _(已废弃)_
- [objc_removeExceptionHandler](<objc_removeexceptionhandler(__).md>)
- [objc_set_collection_ratio](<objc_set_collection_ratio(__).md>) _(已废弃)_
- [objc_set_collection_threshold](<objc_set_collection_threshold(__).md>) _(已废弃)_
- [objc_setCollectionRatio](<objc_setcollectionratio(__).md>) _(已废弃)_
- [objc_setCollectionThreshold](<objc_setcollectionthreshold(__).md>) _(已废弃)_
- [objc_setExceptionMatcher](<objc_setexceptionmatcher(__).md>)
- [objc_setExceptionPreprocessor](<objc_setexceptionpreprocessor(__).md>)
- [objc_setForwardHandler](<objc_setforwardhandler(____).md>) — 设置由 objc_msgForward 调用的函数。
- [objc_setHook_getClass](<objc_sethook_getclass(____).md>)
- [objc_setHook_getImageName](<objc_sethook_getimagename(____).md>)
- [objc_setHook_lazyClassNamer](<objc_sethook_lazyclassnamer(____).md>)
- [objc_setUncaughtExceptionHandler](<objc_setuncaughtexceptionhandler(__).md>)
- [objc_start_collector_thread](<objc_start_collector_thread().md>) _(已废弃)_
- [objc_startCollectorThread](<objc_startcollectorthread().md>) _(已废弃)_
- [objc_terminate](<objc_terminate().md>)
- [objc_unregisterThreadWithCollector](<objc_unregisterthreadwithcollector().md>) _(已废弃)_
- [object_isClass](<object_isclass(__).md>)
- [object_setIvarWithStrongDefault](<object_setivarwithstrongdefault(______).md>)
- [protocol_copyPropertyList2](<protocol_copypropertylist2(________).md>)
- [sel_isMapped](<sel_ismapped(__).md>) — 标识某个选择器是否有效。

## 另请参阅

### 参考

- [Objective-C Runtime](objective-c-runtime.md) — 描述 macOS Objective-C runtime 库的支持函数和数据结构。
- [Objective-C Structures](objective-c-structures.md)
- [Objective-C Constants](objective-c-constants.md)
- [Objective-C Data Types](objective-c-data-types.md)
- [Objective-C Macros](objective-c-macros.md)
- [Objective-C Enumerations](objective-c-enums.md)
