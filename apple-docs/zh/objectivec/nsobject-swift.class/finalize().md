---
title: finalize()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/objectivec/nsobject-swift.class/finalize()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/finalize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/finalize%28%29.json'
content_hash: 'sha256:a5d2c84e59183b73'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# finalize()

<sub>实例方法</sub>

垃圾回收器在处置接收者使用的内存之前会对其调用此方法。

> [!warning] 已废弃
> 垃圾回收在 OS X v10.8 中已废弃；你应改用自动引用计数——请参阅 [Transitioning to ARC Release Notes](https://developer.apple.com/library/archive/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011226)。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func finalize()
```

## 讨论

垃圾回收器在处置接收者使用的内存之前会对其调用此方法。启用垃圾回收时，会调用此方法而不是 `dealloc`。

你可以重写此方法以放弃接收者已获取的资源，如下例所示：

```objc
- (void)finalize {
    if (log_file != NULL) {
        fclose(log_file);
        log_file = NULL;
    }
    [super finalize];
}
```

不过，通常鼓励你尽可能在最终化之前放弃资源。有关更多详细信息，请参阅 Implementing a finalize Method。

### 特殊注意事项

将 `self` 存储到新的或现有的活动对象中（俗称“复活”）是错误的，这意味着此方法只会调用一次。不过，接收者可能在最终化时被同时正在最终化的其他对象发消息，因此你的重写应防范已回收资源的未来使用，如示例中的 `log_file = NULL` 语句所示。对于给定对象，`finalize` 方法本身绝不会被调用多次。

> [!important] 重要
> `finalize` methods must be thread-safe.

## 另请参阅

### 已废弃的方法

- [- accessibilityAttributeNames](<accessibilityattributenames().md>) — 返回接收者支持的属性名称数组。 _(已废弃)_
- [- accessibilityAttributeValue:](<accessibilityattributevalue(__).md>) — 返回接收者中指定属性的值。 _(已废弃)_
- [- accessibilityAttributeValue:forParameter:](<accessibilityattributevalue(__forparameter_).md>) — 返回接收者中与指定属性名和参数对应的参数化属性值。 _(已废弃)_
- [- accessibilityActionDescription:](<accessibilityactiondescription(__).md>) — 返回指定操作的本地化描述。 _(已废弃)_
- [- accessibilityActionNames](<accessibilityactionnames().md>) — 返回辅助功能元素支持的操作名称数组。 _(已废弃)_
- [- accessibilityArrayAttributeCount:](<accessibilityarrayattributecount(__).md>) — 返回指定辅助功能数组属性的计数。 _(已废弃)_
- [- accessibilityArrayAttributeValues:index:maxCount:](<accessibilityarrayattributevalues(__index_maxcount_).md>) — 返回辅助功能数组属性的值的子数组。 _(已废弃)_
- [- accessibilityIndexOfChild:](<accessibilityindex(ofchild_).md>) — 返回指定辅助功能子项在父项中的索引。 _(已废弃)_
- [- accessibilityIsAttributeSettable:](<accessibilityisattributesettable(__).md>) — 返回一个布尔值，指示接收者中指定属性的值是否可设置。 _(已废弃)_
- [- accessibilityIsIgnored](<accessibilityisignored().md>) — 返回一个布尔值，指示在父子辅助功能层次结构中是否应忽略接收者。 _(已废弃)_
- [- accessibilityParameterizedAttributeNames](<accessibilityparameterizedattributenames().md>) — 返回接收者支持的参数化属性名称列表。 _(已废弃)_
- [- accessibilityPerformAction:](<accessibilityperformaction(__).md>) — 执行与指定操作关联的操作。 _(已废弃)_
- [- accessibilitySetOverrideValue:forAttribute:](<accessibilitysetoverridevalue(__forattribute_).md>) — 覆盖接收者中的指定属性（若不存在则添加），并将其值设置为指定值。 _(已废弃)_
- [- accessibilitySetValue:forAttribute:](<accessibilitysetvalue(__forattribute_).md>) — 将接收者中指定属性的值设置为指定值。 _(已废弃)_
- [- fileManager:shouldProceedAfterError:](<filemanager(__shouldproceedaftererror_).md>) — 当复制、移动、移除或链接文件或目录时，`NSFileManager` 对象每遇到一个错误就会向其处理程序发送此消息。 _(已废弃)_
