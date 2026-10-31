---
title: accessibilityAttributeNames()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.1+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilityattributenames()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityattributenames()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityattributenames%28%29.json'
content_hash: 'sha256:8349bcb796e0a4ee'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityAttributeNames()

<sub>实例方法</sub>

返回接收者支持的属性名称数组。

> [!warning] Deprecated
> Use [NSAccessibilityProtocol](../../appkit/nsaccessibilityprotocol.md) instead.

<sub>macOS</sub>

```swift
func accessibilityAttributeNames() -> [NSAccessibility.Attribute]
```

## 返回值

包含接收者支持的属性的数组。

## 讨论

用户界面类必须实现此方法。子类应在超类实现存在时调用它，并追加额外属性或移除不支持的属性。属性名称列表参见 [NSAccessibility](../../appkit/nsaccessibility.md) 常量。

## 另请参阅

### 已废弃方法

- [- accessibilityAttributeValue:](<accessibilityattributevalue(__).md>) — Returns the value of the specified attribute in the receiver. _(已废弃)_
- [- accessibilityAttributeValue:forParameter:](<accessibilityattributevalue(__forparameter_).md>) — Returns the value of the receiver’s parameterized attribute corresponding to the specified attribute name and parameter. _(已废弃)_
- [- accessibilityActionDescription:](<accessibilityactiondescription(__).md>) — Returns a localized description of the specified action. _(已废弃)_
- [- accessibilityActionNames](<accessibilityactionnames().md>) — Returns an array of action names supported by the accessibility element. _(已废弃)_
- [- accessibilityArrayAttributeCount:](<accessibilityarrayattributecount(__).md>) — Returns the count of the specified accessibility array attribute. _(已废弃)_
- [- accessibilityArrayAttributeValues:index:maxCount:](<accessibilityarrayattributevalues(__index_maxcount_).md>) — Returns a subarray of values of an accessibility array attribute. _(已废弃)_
- [- accessibilityIndexOfChild:](<accessibilityindex(ofchild_).md>) — Returns the index of the specified accessibility child in the parent. _(已废弃)_
- [- accessibilityIsAttributeSettable:](<accessibilityisattributesettable(__).md>) — Returns a Boolean value that indicates whether the value for the specified attribute in the receiver can be set. _(已废弃)_
- [- accessibilityIsIgnored](<accessibilityisignored().md>) — Returns a Boolean value indicating whether the receiver should be ignored in the parent-child accessibility hierarchy. _(已废弃)_
- [- accessibilityParameterizedAttributeNames](<accessibilityparameterizedattributenames().md>) — Returns a list of parameterized attribute names supported by the receiver. _(已废弃)_
- [- accessibilityPerformAction:](<accessibilityperformaction(__).md>) — Performs the action associated with the specified action. _(已废弃)_
- [- accessibilitySetOverrideValue:forAttribute:](<accessibilitysetoverridevalue(__forattribute_).md>) — Overrides the specified attribute in the receiver or adds it if it does not exist, and sets its value to the specified value. _(已废弃)_
- [- accessibilitySetValue:forAttribute:](<accessibilitysetvalue(__forattribute_).md>) — Sets the value of the specified attribute in the receiver to the specified value. _(已废弃)_
- [- fileManager:shouldProceedAfterError:](<filemanager(__shouldproceedaftererror_).md>) — An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories. _(已废弃)_
- [- fileManager:willProcessPath:](<filemanager(__willprocesspath_).md>) — An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path. _(已废弃)_
