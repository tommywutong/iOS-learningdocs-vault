---
title: 'storedValue(forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/storedvalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/storedvalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/storedvalue%28forkey%3A%29.json'
content_hash: 'sha256:1d571a124daa534a'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# storedValue(forKey:)

<sub>实例方法</sub>

返回由给定键标识的属性。

> [!warning] 已废弃
> 若你使用的是 `NSManagedObject` 类，请改用 [primitiveValue(forKey:)](<../../coredata/nsmanagedobject/primitivevalue(forkey_).md>)。

<sub>tvOS, visionOS, watchOS</sub>

```swift
func storedValue(forKey key: String) -> Any?
```

## 讨论

当为存储在对象存储中（通常最终存储在数据库中）或包含在快照中而检索值时，会使用此方法。默认实现类似于 [- valueForKey:](<value(forkey_).md>) 的实现，但它以不同的方法/实例变量搜索顺序解析 `key`：

1. 基于 `key` 搜索私有访问器方法（前面带下划线的方法）。例如，对于 `key` “lastName”，[- storedValueForKey:](<storedvalue(forkey_).md>) 会查找名为 `_getLastName` 或 `_lastName` 的方法。
2. 若未找到私有访问器，则基于 `key` 搜索实例变量并直接返回其值。例如，对于 `key` “lastName”，[- storedValueForKey:](<storedvalue(forkey_).md>) 会查找名为 `_lastName` 或 `lastName` 的实例变量。
3. 若既未找到私有访问器也未找到实例变量，[- storedValueForKey:](<storedvalue(forkey_).md>) 会基于 `key` 搜索公共访问器方法。对于 `key` “lastName”，这将是 `getLastName` 或 `lastName`。
4. 若 `key` 未知，[- storedValueForKey:](<storedvalue(forkey_).md>) 会调用 [- handleTakeValue:forUnboundKey:](<handletakevalue(__forunboundkey_).md>)。

这种不同的搜索顺序允许对象绕过通过公共 API 返回值之前执行的处理。不过，若你始终希望使用 [- valueForKey:](<value(forkey_).md>) 中的搜索顺序，可以实现类方法 [+ useStoredAccessor](<usestoredaccessor().md>) 以返回 [NO](../no.md)。并且与 [- valueForKey:](<value(forkey_).md>) 一样，你可以使用类方法 [accessInstanceVariablesDirectly](accessinstancevariablesdirectly.md) 阻止直接访问实例变量。

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
