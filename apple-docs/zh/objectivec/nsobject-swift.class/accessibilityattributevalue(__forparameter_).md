---
title: 'accessibilityAttributeValue(_:forParameter:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.1+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/accessibilityattributevalue(_:forparameter:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityattributevalue(_:forparameter:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityattributevalue%28_%3Aforparameter%3A%29.json'
content_hash: 'sha256:bf298adf7e66ed0a'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityAttributeValue(_:forParameter:)

<sub>实例方法</sub>

返回接收者中与指定属性名和参数对应的参数化属性值。

> [!warning] Deprecated
> Use [NSAccessibilityProtocol](../../appkit/nsaccessibilityprotocol.md) instead.

<sub>macOS</sub>

```swift
func accessibilityAttributeValue(_ attribute: NSAccessibility.ParameterizedAttribute, forParameter parameter: Any?) -> Any?
```

## 参数

- `attribute` — 属性名称。属性名称列表参见 [NSAccessibility](../../appkit/nsaccessibility.md) 常量。

- `parameter` — The parameter.

## 讨论

如果实现此方法，还应实现 [- accessibilityParameterizedAttributeNames](<accessibilityparameterizedattributenames().md>)。

## 另请参阅

### 已废弃方法

- [- accessibilityAttributeNames](<accessibilityattributenames().md>) — Returns an array of attribute names supported by the receiver. _(已废弃)_
- [- accessibilityAttributeValue:](<accessibilityattributevalue(__).md>) — Returns the value of the specified attribute in the receiver. _(已废弃)_
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
