---
title: 已废弃符号
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/deprecated-symbols
source_url: 'https://developer.apple.com/documentation/objectivec/deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/deprecated-symbols.json'
content_hash: 'sha256:c53fee4ba25eb543'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# 已废弃符号

<sub>API 集合</sub>

查看不再受支持的符号，找到应改用的替代方案。

## Topics

### Deprecated Class Methods

- [+ defaultPlaceholderForMarker:withBinding:](<nsobject-swift.class/defaultplaceholder(for_with_).md>) — 当接收类的实例上某个符合键值编码规范的属性返回 `marker` 指定的值、且没有指定其他占位符时，返回将被用作 `binding` 占位符的对象。_(已废弃)_
- [+ setDefaultPlaceholder:forMarker:withBinding:](<nsobject-swift.class/setdefaultplaceholder(__for_with_).md>) — 当接收类的实例上某个符合键值编码规范的属性返回 `marker` 指定的值、且没有指定其他占位符时，将 `placeholder` 设置为 `binding` 的默认占位符。_(已废弃)_
- [+ useStoredAccessor](<nsobject-swift.class/usestoredaccessor().md>) — 如果存储值方法 [- storedValueForKey:](<nsobject-swift.class/storedvalue(forkey_).md>) 和 [- takeStoredValue:forKey:](<nsobject-swift.class/takestoredvalue(__forkey_).md>) 应优先使用私有存取方法而非公共存取方法，则返回 `true`。_(已废弃)_

### Deprecated Methods

- [- accessibilityAttributeNames](<nsobject-swift.class/accessibilityattributenames().md>) — 返回接收者所支持的特性名称组成的数组。_(已废弃)_
- [- accessibilityAttributeValue:](<nsobject-swift.class/accessibilityattributevalue(__).md>) — 返回接收者中指定特性的值。_(已废弃)_
- [- accessibilityAttributeValue:forParameter:](<nsobject-swift.class/accessibilityattributevalue(__forparameter_).md>) — 返回接收者中与指定特性名称和参数对应的参数化特性的值。_(已废弃)_
- [- accessibilityActionDescription:](<nsobject-swift.class/accessibilityactiondescription(__).md>) — 返回指定动作的本地化描述。_(已废弃)_
- [- accessibilityActionNames](<nsobject-swift.class/accessibilityactionnames().md>) — 返回辅助功能元素所支持的动作名称组成的数组。_(已废弃)_
- [- accessibilityArrayAttributeCount:](<nsobject-swift.class/accessibilityarrayattributecount(__).md>) — 返回指定辅助功能数组特性的计数。_(已废弃)_
- [- accessibilityArrayAttributeValues:index:maxCount:](<nsobject-swift.class/accessibilityarrayattributevalues(__index_maxcount_).md>) — 返回辅助功能数组特性中值的一个子数组。_(已废弃)_
- [- accessibilityIndexOfChild:](<nsobject-swift.class/accessibilityindex(ofchild_).md>) — 返回指定辅助功能子项在父项中的索引。_(已废弃)_
- [- accessibilityIsAttributeSettable:](<nsobject-swift.class/accessibilityisattributesettable(__).md>) — 返回一个布尔值，指示接收者中指定特性的值是否可以设置。_(已废弃)_
- [- accessibilityIsIgnored](<nsobject-swift.class/accessibilityisignored().md>) — 返回一个布尔值，指示在父子辅助功能层级结构中是否应忽略接收者。_(已废弃)_
- [- accessibilityParameterizedAttributeNames](<nsobject-swift.class/accessibilityparameterizedattributenames().md>) — 返回接收者所支持的参数化特性名称列表。_(已废弃)_
- [- accessibilityPerformAction:](<nsobject-swift.class/accessibilityperformaction(__).md>) — 执行与指定动作关联的动作。_(已废弃)_
- [- accessibilitySetOverrideValue:forAttribute:](<nsobject-swift.class/accessibilitysetoverridevalue(__forattribute_).md>) — 覆盖接收者中指定的特性，如果不存在则添加该特性，并将其值设置为指定的值。_(已废弃)_
- [- accessibilitySetValue:forAttribute:](<nsobject-swift.class/accessibilitysetvalue(__forattribute_).md>) — 将接收者中指定特性的值设置为指定的值。_(已废弃)_
- [- fileManager:shouldProceedAfterError:](<nsobject-swift.class/filemanager(__shouldproceedaftererror_).md>) — `NSFileManager` 对象在复制、移动、删除或链接文件或目录时每遇到一个错误，就会向其处理程序发送这个消息。_(已废弃)_
- [- fileManager:willProcessPath:](<nsobject-swift.class/filemanager(__willprocesspath_).md>) — `NSFileManager` 对象在尝试移动、复制、重命名或删除给定路径，或者尝试链接到给定路径之前，会立即向处理程序发送这个消息。_(已废弃)_
- [- finalize](<nsobject-swift.class/finalize().md>) — 垃圾回收器在释放接收者所使用的内存之前，会在接收者上调用这个方法。_(已废弃)_
- [- fontManager:willIncludeFont:](<nsobject-swift.class/fontmanager(__willincludefont_).md>) — 向 Font 面板的委托请求权限，以在 Font 面板中显示给定的字体名称。_(已废弃)_
- [- namesOfPromisedFilesDroppedAtDestination:](<nsobject-swift.class/namesofpromisedfilesdropped(atdestination_).md>) — 返回接收者承诺在指定位置创建的文件的名称。_(已废弃)_
- [- storedValueForKey:](<nsobject-swift.class/storedvalue(forkey_).md>) — 返回由给定键标识的属性。_(已废弃)_
- [- textStorageDidProcessEditing:](<nsobject-swift.class/textstoragedidprocessediting(__).md>) _(已废弃)_
- [- textStorageWillProcessEditing:](<nsobject-swift.class/textstoragewillprocessediting(__).md>) _(已废弃)_
- [- takeStoredValue:forKey:](<nsobject-swift.class/takestoredvalue(__forkey_).md>) — 设置由给定键标识的属性的值。_(已废弃)_
- [- takeValue:forKey:](<nsobject-swift.class/takevalue(__forkey_).md>) — 将由 `key` 标识的属性的值设置为 `value`。_(已废弃)_
- [- takeValue:forKeyPath:](<nsobject-swift.class/takevalue(__forkeypath_).md>) — 将由 `keyPath` 标识的属性的值设置为 `value`。_(已废弃)_
- [- takeValuesFromDictionary:](<nsobject-swift.class/takevalues(from_).md>) — 使用给定字典中的值设置接收者的属性，用字典的键来标识属性。_(已废弃)_
- [- unableToSetNilForKey:](<nsobject-swift.class/unabletosetnil(forkey_).md>) — 当 `key` 由一个标量特性表示时被调用。_(已废弃)_
- [- valuesForKeys:](<nsobject-swift.class/values(forkeys_).md>) — 返回一个字典，其键为 `keys` 中的属性名称，对应的值为相应的属性值。_(已废弃)_
- [workflowController(_:didError:)](<../automator/amworkflowcontrollerdelegate/workflowcontroller(__diderror_).md>) — 当工作流遇到错误时通知委托。
- [workflowController(_:didRun:)](<../automator/amworkflowcontrollerdelegate/workflowcontroller(__didrun_).md>) — 当指定动作运行结束时通知委托。
- [workflowController(_:willRun:)](<../automator/amworkflowcontrollerdelegate/workflowcontroller(__willrun_).md>) — 当指定动作即将运行时通知委托。
- [workflowControllerDidRun(_:)](<../automator/amworkflowcontrollerdelegate/workflowcontrollerdidrun(__).md>) — 当工作流控制器对象运行结束时通知委托。
- [workflowControllerDidStop(_:)](<../automator/amworkflowcontrollerdelegate/workflowcontrollerdidstop(__).md>) — 告知委托工作流控制器对象已停止。
- [workflowControllerWillRun(_:)](<../automator/amworkflowcontrollerdelegate/workflowcontrollerwillrun(__).md>) — 当工作流控制器对象即将运行时通知委托。
- [workflowControllerWillStop(_:)](<../automator/amworkflowcontrollerdelegate/workflowcontrollerwillstop(__).md>) — 告知委托工作流控制器对象即将停止。
