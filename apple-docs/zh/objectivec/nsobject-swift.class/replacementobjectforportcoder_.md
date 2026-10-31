---
title: 'replacementObjectForPortCoder:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/replacementobjectforportcoder:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/replacementobjectforportcoder:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/replacementobjectforportcoder%3A.json'
content_hash: 'sha256:554e2fcece2d02fe'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# replacementObjectForPortCoder:

<sub>实例方法</sub>

由子类重写，以便在分发编码期间用另一个对象或副本替换自身。

<sub>Mac Catalyst, macOS</sub>

```objc
- (id) replacementObjectForPortCoder:(NSPortCoder *) coder;
```

## 参数

- `coder` — The port coder encoding the receiver.

## 返回值

代替接收者进行编码的对象（若不同）。

## 讨论

此方法由 `NSPortCoder` 调用。`NSObject` 的实现为 [- replacementObjectForCoder:](<replacementobject(for_)-2l8ox.md>) 返回的对象返回一个 `NSDistantObject` 对象，从而默认启用所有对象通过代理进行分发。不过，若 [- replacementObjectForCoder:](<replacementobject(for_)-2l8ox.md>) 返回 `nil`，则 `NSObject` 的实现也将返回 `nil`。

希望按副本而非按引用传递的子类必须重写此方法并返回 `self`。以下示例显示如何同时支持按副本和按引用的对象替换：

```objc
- (id)replacementObjectForPortCoder:(NSPortCoder *)encoder {
    return [encoder isByref] ? [super replacementObjectForPortCoder:encoder] : self;
}
```

## 另请参阅

### 相关文档

- [classForPortCoder](classforportcoder.md) — 在分布式编码中用于替代接收者的类。 _(已废弃)_

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
