---
title: 'class_respondsToMethod(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/class_respondstomethod(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_respondstomethod(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_respondstomethod%28_%3A_%3A%29.json'
content_hash: 'sha256:86cd45017adee0f3'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_respondsToMethod(_:_:)

<sub>函数</sub>

> [!warning] 已废弃
> use class_respondsToSelector instead

<sub>tvOS, visionOS, watchOS</sub>

```swift
func class_respondsToMethod(_ cls: AnyClass?, _ sel: Selector) -> Bool
```

## 另请参阅

### 函数

- [autoreleasepool(invoking:)](<autoreleasepool(invoking_).md>)
- [class_lookupMethod](<class_lookupmethod(____).md>) _(已废弃)_
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
