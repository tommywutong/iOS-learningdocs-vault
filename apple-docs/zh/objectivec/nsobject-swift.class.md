---
title: NSObject
framework: Objective-C Runtime
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class.json'
content_hash: 'sha256:2e0ea9a8f58cef55'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# NSObject

<sub>类</sub>

大多数 Objective-C 类层次结构的根类，子类从中继承与运行时系统交互的基本接口，以及作为 Objective-C 对象运行的能力。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSObject
```

## 关系

- **符合**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](nsobjectprotocol.md)

## 主题

### 初始化类

- [+ initialize](<nsobject-swift.class/initialize().md>) — 在类收到第一条消息之前对其进行初始化。
- [+ load](<nsobject-swift.class/load().md>) — 每当类或类别添加到 Objective-C 运行时都会调用；实现此方法以在加载时执行特定于类的行为。

### 创建、拷贝与释放对象

- [- init](<nsobject-swift.class/init().md>) — 由子类实现，以在为新对象（接收者）分配内存后立即对其进行初始化。
- [- copy](<nsobject-swift.class/copy().md>) — 返回 `copy(with:)` 返回的对象。
- [- mutableCopy](<nsobject-swift.class/mutablecopy().md>) — 返回 `mutableCopy(with:)`（其中 zone 为 `nil`）返回的对象。

### 识别类

- [+ superclass](<nsobject-swift.class/superclass().md>) — 返回接收者超类的类对象。
- [+ isSubclassOfClass:](<nsobject-swift.class/issubclass(of_).md>) — 返回一个布尔值，指示接收类是否为给定类的子类，或与给定类相同。

### 测试类功能

- [+ instancesRespondToSelector:](<nsobject-swift.class/instancesrespond(to_).md>) — 返回一个布尔值，指示接收者的实例是否能够响应给定选择器。

### 测试协议一致性

- [+ conformsToProtocol:](<nsobject-swift.class/conforms(to_).md>) — 返回一个布尔值，指示目标是否符合给定协议。

### 获取方法信息

- [- methodForSelector:](<nsobject-swift.class/method(for_).md>) — 定位并返回接收者某个方法实现的地址，以便可将其作为函数调用。
- [+ instanceMethodForSelector:](<nsobject-swift.class/instancemethod(for_).md>) — 定位并返回由给定选择器标识的实例方法实现的地址。

### 描述对象

- [+ description](<nsobject-swift.class/description().md>) — 返回表示接收类内容的字符串。

### 支持可丢弃内容

- [autoContentAccessingProxy](nsobject-swift.class/autocontentaccessingproxy.md) — 接收对象的代理

### 发送消息

- [- performSelector:withObject:afterDelay:](<nsobject-swift.class/perform(__with_afterdelay_).md>) — 在延迟后使用默认模式在当前线程上调用接收者的方法。
- [- performSelector:withObject:afterDelay:inModes:](<nsobject-swift.class/perform(__with_afterdelay_inmodes_).md>) — 在延迟后使用指定模式在当前线程上调用接收者的方法。
- [- performSelectorOnMainThread:withObject:waitUntilDone:](<nsobject-swift.class/performselector(onmainthread_with_waituntildone_).md>) — 使用默认模式在主线程上调用接收者的方法。
- [- performSelectorOnMainThread:withObject:waitUntilDone:modes:](<nsobject-swift.class/performselector(onmainthread_with_waituntildone_modes_).md>) — 使用指定模式在主线程上调用接收者的方法。
- [- performSelector:onThread:withObject:waitUntilDone:](<nsobject-swift.class/perform(__on_with_waituntildone_).md>) — 使用默认模式在指定线程上调用接收者的方法。
- [- performSelector:onThread:withObject:waitUntilDone:modes:](<nsobject-swift.class/perform(__on_with_waituntildone_modes_).md>) — 使用指定模式在指定线程上调用接收者的方法。
- [- performSelectorInBackground:withObject:](<nsobject-swift.class/performselector(inbackground_with_).md>) — 在新的后台线程上调用接收者的方法。
- [+ cancelPreviousPerformRequestsWithTarget:](<nsobject-swift.class/cancelpreviousperformrequests(withtarget_).md>) — 取消先前使用 [- performSelector:withObject:afterDelay:](<nsobject-swift.class/perform(__with_afterdelay_).md>) 实例方法注册的执行请求。
- [+ cancelPreviousPerformRequestsWithTarget:selector:object:](<nsobject-swift.class/cancelpreviousperformrequests(withtarget_selector_object_).md>) — 取消先前使用 [- performSelector:withObject:afterDelay:](<nsobject-swift.class/perform(__with_afterdelay_).md>) 注册的执行请求。

### 转发消息

- [- forwardingTargetForSelector:](<nsobject-swift.class/forwardingtarget(for_).md>) — 返回应首先将无法识别的消息定向到的对象。

### 动态解析方法

- [+ resolveClassMethod:](<nsobject-swift.class/resolveclassmethod(__).md>) — 为类方法的给定选择器动态提供实现。
- [+ resolveInstanceMethod:](<nsobject-swift.class/resolveinstancemethod(__).md>) — 为实例方法的给定选择器动态提供实现。

### 处理错误

- [- doesNotRecognizeSelector:](<nsobject-swift.class/doesnotrecognizeselector(__).md>) — 处理接收者不识别的消息。

### 归档

- [- awakeAfterUsingCoder:](<nsobject-swift.class/awakeafter(using_).md>) — 由子类重写，以便用另一个对象替换已解码并随后收到此消息的对象。
- [classForArchiver](nsobject-swift.class/classforarchiver.md) — 在归档期间用于替代接收者自身类的类。
- [classForCoder](nsobject-swift.class/classforcoder.md) — 由子类重写，以便在编码期间用其他类替代自身类。
- [classForKeyedArchiver](nsobject-swift.class/classforkeyedarchiver.md) — 子类在键控归档期间用新类替代实例。
- [+ classFallbacksForKeyedArchiver](<nsobject-swift.class/classfallbacksforkeyedarchiver().md>) — 重写以返回在对象的类不可用时可用于解码对象的类名。
- [+ classForKeyedUnarchiver](<nsobject-swift.class/classforkeyedunarchiver().md>) — 由子类重写，以便在键控解档期间替换为新类。
- [- replacementObjectForArchiver:](<nsobject-swift.class/replacementobject(for_)-8ih2x.md>) — 由子类重写，以便在归档期间用另一个对象替换自身。 _(已废弃)_
- [- replacementObjectForCoder:](<nsobject-swift.class/replacementobject(for_)-2l8ox.md>) — 由子类重写，以便在键控归档期间用另一对象替代自身。
- [- replacementObjectForKeyedArchiver:](<nsobject-swift.class/replacementobject(for_)-60vwc.md>) — 由子类重写，以便在键控归档期间用另一对象替代自身。
- [+ setVersion:](<nsobject-swift.class/setversion(__).md>) — 设置接收者的版本号。
- [+ version](<nsobject-swift.class/version().md>) — 返回分配给该类的版本号。

### 使用类描述

- [attributeKeys](nsobject-swift.class/attributekeys.md) — 包含接收者类的实例所包含的不可变值名称的 `NSString` 对象数组。
- [classDescription](nsobject-swift.class/classdescription.md) — 包含接收者类的属性和关系信息的对象。
- [- inverseForRelationshipKey:](<nsobject-swift.class/inverse(forrelationshipkey_).md>) — 对于定义从接收者类到另一类的关系名称的给定键，返回从另一类到接收者类的关系名称。
- [toManyRelationshipKeys](nsobject-swift.class/tomanyrelationshipkeys.md) — 包含接收者一对多关系属性键的数组。
- [toOneRelationshipKeys](nsobject-swift.class/toonerelationshipkeys.md) — 接收者一对一关系属性的键（如果有）。

### 改进辅助功能

- [UIAccessibility](../uikit/uiaccessibility-protocol.md) — 一组方法，提供有关 App 用户界面中视图和控制的辅助功能信息。
- [UIAccessibilityContainer](../uikit/uiaccessibilitycontainer.md) — 提供一组方法，供视图子类使用，以使子组件能作为独立元素被辅助功能访问。
- [UIAccessibilityAction](uiaccessibilityaction.md) — 一组方法，辅助功能元素可用它来支持特定操作。
- [UIAccessibilityFocus](uiaccessibilityfocus.md) — 一个非正式协议，提供一种方法来判断辅助 App（如旁白）是否将焦点置于某个辅助功能元素上。
- [UIAccessibilityDragging](uiaccessibilitydragging.md) — 一对属性，可让你微调拖放操作如何暴露给辅助技术。

### 改进浏览器辅助功能

- [- browserAccessibilityAttributedValueInRange:](<nsobject-swift.class/browseraccessibilityattributedvalue(in_).md>) — 以归因字符串形式返回此元素在给定范围内的值。
- [- browserAccessibilityDeleteTextAtCursor:](<nsobject-swift.class/browseraccessibilitydeletetextatcursor(numberofcharacters_).md>) — 从元素的当前光标位置删除文本。
- [- browserAccessibilityInsertTextAtCursor:](<nsobject-swift.class/browseraccessibilityinserttextatcursor(text_).md>) — 在元素的当前光标位置插入文本。
- [- browserAccessibilitySelectedTextRange](<nsobject-swift.class/browseraccessibilityselectedtextrange().md>) — 返回元素中选中文本的范围。
- [- browserAccessibilitySetSelectedTextRange:](<nsobject-swift.class/browseraccessibilitysetselectedtextrange(__).md>) — 更新元素的选中文本。
- [- browserAccessibilityValueInRange:](<nsobject-swift.class/browseraccessibilityvalue(in_).md>) — 返回此元素在给定范围内的值。
- [browserAccessibilityContainerType](nsobject-swift.class/browseraccessibilitycontainertype.md) — 包含此元素的容器种类。
- [browserAccessibilityCurrentStatus](nsobject-swift.class/browseraccessibilitycurrentstatus.md) — 作为元素 aria-current 值的字符串。
- [browserAccessibilityHasDOMFocus](nsobject-swift.class/browseraccessibilityhasdomfocus.md) — 一个布尔值，指示元素在浏览器文档对象模型中是否具有原生焦点。
- [browserAccessibilityIsRequired](nsobject-swift.class/browseraccessibilityisrequired.md) — 作为元素 aria-required 值的布尔值。
- [browserAccessibilityPressedState](nsobject-swift.class/browseraccessibilitypressedstate.md) — 元素的 aria-pressed 值。
- [browserAccessibilityRoleDescription](nsobject-swift.class/browseraccessibilityroledescription.md) — 描述元素对辅助技术角色的字符串。
- [browserAccessibilitySortDirection](nsobject-swift.class/browseraccessibilitysortdirection.md) — 作为元素 aria-sort 值的字符串。

### 脚本

- [classCode](nsobject-swift.class/classcode.md) — 接收者的 Apple 事件类型代码，存储在该对象类的 `NSScriptClassDescription` 对象中。
- [className](nsobject-swift.class/classname.md) — 包含类名的字符串。
- [- copyScriptingValue:forKey:withProperties:](<nsobject-swift.class/copyscriptingvalue(__forkey_withproperties_).md>) — 通过拷贝传入的值并设置拷贝对象中的属性，创建并返回一个或多个要插入到指定关系中的脚本对象。
- [- newScriptingObjectOfClass:forValueForKey:withContentsValue:properties:](<nsobject-swift.class/newscriptingobject(of_forvalueforkey_withcontentsvalue_properties_).md>) — 创建并返回可脚本化类的实例，设置其内容和属性，以便插入到由键标识的关系中。
- [scriptingProperties](nsobject-swift.class/scriptingproperties.md) — 以 `NSString` 为键的接收者可脚本化属性字典。
- [- scriptingValueForSpecifier:](<nsobject-swift.class/scriptingvalue(for_).md>) — 给定对象说明符，返回接收容器中指定的一个或多个对象。

### 与 Combine 集成

- [KeyValueObservingPublisher](nsobject-swift.class/keyvalueobservingpublisher.md) — 每当观察值更改时生成新元素的 Combine 发布者。

### 键值观察

- [NSKeyValueObserving](nskeyvalueobserving.md) — 对象为接收其他对象指定属性发生更改的通知而采纳的非正式协议。

### 键值编码

- [NSKeyValueBindingCreation](nskeyvaluebindingcreation.md) — 一组方法，可用来在视图对象和控制器之间、或控制器和模型对象之间创建和移除绑定。
- [NSKeyValueCoding](nskeyvaluecoding.md) — 一种通过名称或键间接访问对象属性的机制。
- [NSScriptKeyValueCoding](nsscriptkeyvaluecoding.md) — 一组为使用键值编码提供额外功能的方法。
- [NSScriptKeyValueCoding Exception Names](nsscriptkeyvaluecoding-exception-names.md) — 键值编码方法引发的异常。

### 与 Web 插件交互

- [WebPlugInContainer](webplugincontainer.md) — `WebPlugInContainer` 是一个非正式协议，使插件能够向应用程序发送消息。
- [WebPlugIn](webplugin.md) — `WebPlugIn` 这个非正式协议定义了一些方法，使得使用 WebKit 框架的应用程序与其可能使用的任何基于 WebKit 的插件之间能够进行交互。

### 实现 Web 脚本

- [WebScripting](webscripting.md) — `WebScripting` 是一个非正式协议，定义了一些方法，类可以实现这些方法将其接口导出到诸如 JavaScript 之类的 WebScript 环境。

### 支持 Cocoa 脚本

- [NSScriptingComparisonMethods](nsscriptingcomparisonmethods.md) — 一组用于比较脚本对象的方法。

### 自定义辅助功能

- [accessibilityElements](nsobject-swift.class/accessibilityelements.md) — 一个数组，包含辅助技术可以访问的对象的各项特性。

### 已废弃

- [Deprecated Symbols](deprecated-symbols.md) — 查看不再受支持的符号，找到应改用的替代方案。

### 实例属性

- [accessibilityActivateBlock](nsobject-swift.class/accessibilityactivateblock.md)
- [accessibilityActivationPoint](nsobject-swift.class/accessibilityactivationpoint.md)
- [accessibilityActivationPointBlock](nsobject-swift.class/accessibilityactivationpointblock.md)
- [accessibilityAttributedHint](nsobject-swift.class/accessibilityattributedhint.md)
- [accessibilityAttributedHintBlock](nsobject-swift.class/accessibilityattributedhintblock.md)
- [accessibilityAttributedLabel](nsobject-swift.class/accessibilityattributedlabel.md)
- [accessibilityAttributedLabelBlock](nsobject-swift.class/accessibilityattributedlabelblock.md)
- [accessibilityAttributedUserInputLabels](nsobject-swift.class/accessibilityattributeduserinputlabels.md)
- [accessibilityAttributedUserInputLabelsBlock](nsobject-swift.class/accessibilityattributeduserinputlabelsblock.md)
- [accessibilityAttributedValue](nsobject-swift.class/accessibilityattributedvalue.md)
- [accessibilityAttributedValueBlock](nsobject-swift.class/accessibilityattributedvalueblock.md)
- [accessibilityContainerType](nsobject-swift.class/accessibilitycontainertype.md)
- [accessibilityContainerTypeBlock](nsobject-swift.class/accessibilitycontainertypeblock.md)
- [accessibilityCustomActionsBlock](nsobject-swift.class/accessibilitycustomactionsblock.md)
- [accessibilityCustomRotors](nsobject-swift.class/accessibilitycustomrotors.md)
- [accessibilityCustomRotorsBlock](nsobject-swift.class/accessibilitycustomrotorsblock.md)
- [accessibilityDecrementBlock](nsobject-swift.class/accessibilitydecrementblock.md)
- [accessibilityDirectTouchOptions](nsobject-swift.class/accessibilitydirecttouchoptions.md)
- [accessibilityElementsBlock](nsobject-swift.class/accessibilityelementsblock.md)
- [accessibilityElementsHidden](nsobject-swift.class/accessibilityelementshidden.md)
- [accessibilityElementsHiddenBlock](nsobject-swift.class/accessibilityelementshiddenblock.md)
- [accessibilityExpandedStatus](nsobject-swift.class/accessibilityexpandedstatus.md)
- [accessibilityExpandedStatusBlock](nsobject-swift.class/accessibilityexpandedstatusblock.md)
- [accessibilityFocusedUIElement](nsobject-swift.class/accessibilityfocuseduielement.md)
- [accessibilityFrame](nsobject-swift.class/accessibilityframe.md)
- [accessibilityFrameBlock](nsobject-swift.class/accessibilityframeblock.md)
- [accessibilityHeaderElements](nsobject-swift.class/accessibilityheaderelements.md)
- [accessibilityHeaderElementsBlock](nsobject-swift.class/accessibilityheaderelementsblock.md)
- [accessibilityHint](nsobject-swift.class/accessibilityhint.md)
- [accessibilityHintBlock](nsobject-swift.class/accessibilityhintblock.md)
- [accessibilityIdentifierBlock](nsobject-swift.class/accessibilityidentifierblock.md)
- [accessibilityIncrementBlock](nsobject-swift.class/accessibilityincrementblock.md)
- [accessibilityLabel](nsobject-swift.class/accessibilitylabel.md)
- [accessibilityLabelBlock](nsobject-swift.class/accessibilitylabelblock.md)
- [accessibilityLanguage](nsobject-swift.class/accessibilitylanguage.md)
- [accessibilityLanguageBlock](nsobject-swift.class/accessibilitylanguageblock.md)
- [accessibilityMagicTapBlock](nsobject-swift.class/accessibilitymagictapblock.md)
- [accessibilityNavigationStyle](nsobject-swift.class/accessibilitynavigationstyle.md)
- [accessibilityNavigationStyleBlock](nsobject-swift.class/accessibilitynavigationstyleblock.md)
- [accessibilityNextTextNavigationElement](nsobject-swift.class/accessibilitynexttextnavigationelement.md) — 包含在语义上紧随此元素文本之后的文本的辅助功能元素。
- [accessibilityNextTextNavigationElementBlock](nsobject-swift.class/accessibilitynexttextnavigationelementblock.md)
- [accessibilityNotifiesWhenDestroyed](nsobject-swift.class/accessibilitynotifieswhendestroyed.md) — 一个布尔值，指示自定义辅助功能对象在其对应 UI 元素被销毁时是否发送通知。
- [accessibilityPath](nsobject-swift.class/accessibilitypath.md)
- [accessibilityPathBlock](nsobject-swift.class/accessibilitypathblock.md)
- [accessibilityPerformEscapeBlock](nsobject-swift.class/accessibilityperformescapeblock.md)
- [accessibilityPreviousTextNavigationElement](nsobject-swift.class/accessibilityprevioustextnavigationelement.md) — 包含在语义上位于此元素文本之前的文本的辅助功能元素。
- [accessibilityPreviousTextNavigationElementBlock](nsobject-swift.class/accessibilityprevioustextnavigationelementblock.md)
- [accessibilityRespondsToUserInteraction](nsobject-swift.class/accessibilityrespondstouserinteraction.md)
- [accessibilityRespondsToUserInteractionBlock](nsobject-swift.class/accessibilityrespondstouserinteractionblock.md)
- [accessibilityShouldGroupAccessibilityChildrenBlock](nsobject-swift.class/accessibilityshouldgroupaccessibilitychildrenblock.md)
- [accessibilityTextInputResponder](nsobject-swift.class/accessibilitytextinputresponder.md) — 处理此辅助功能元素文本输入调用的对象。
- [accessibilityTextInputResponderBlock](nsobject-swift.class/accessibilitytextinputresponderblock.md) — 用于处理对后备视图的文本输入调用的 block。
- [accessibilityTextualContext](nsobject-swift.class/accessibilitytextualcontext.md)
- [accessibilityTextualContextBlock](nsobject-swift.class/accessibilitytextualcontextblock.md)
- [accessibilityTraits](nsobject-swift.class/accessibilitytraits.md)
- [accessibilityTraitsBlock](nsobject-swift.class/accessibilitytraitsblock.md)
- [accessibilityUserInputLabels](nsobject-swift.class/accessibilityuserinputlabels.md)
- [accessibilityUserInputLabelsBlock](nsobject-swift.class/accessibilityuserinputlabelsblock.md)
- [accessibilityValue](nsobject-swift.class/accessibilityvalue.md)
- [accessibilityValueBlock](nsobject-swift.class/accessibilityvalueblock.md)
- [accessibilityViewIsModal](nsobject-swift.class/accessibilityviewismodal.md)
- [accessibilityViewIsModalBlock](nsobject-swift.class/accessibilityviewismodalblock.md)
- [automationElements](nsobject-swift.class/automationelements.md)
- [automationElementsBlock](nsobject-swift.class/automationelementsblock.md)
- [browserAccessibilityDetailsElements](nsobject-swift.class/browseraccessibilitydetailselements.md)
- [browserAccessibilityImageDataSize](nsobject-swift.class/browseraccessibilityimagedatasize-swift.property.md) — 返回此元素所表示图像的原生像素尺寸；若此元素不表示图像，则返回 `CGSize.zero`。 _(beta)_
- [browserAccessibilityKeyboardShortcuts](nsobject-swift.class/browseraccessibilitykeyboardshortcuts.md)
- [browserAccessibilityOrientation](nsobject-swift.class/browseraccessibilityorientation.md)
- [isAccessibilityElement](nsobject-swift.class/isaccessibilityelement.md)
- [isAccessibilityElementBlock](nsobject-swift.class/isaccessibilityelementblock.md)
- [selectable](nsobject-swift.class/isselectable.md)
- [objectSpecifier](nsobject-swift.class/objectspecifier.md) — 返回接收者的对象说明符。
- [shouldGroupAccessibilityChildren](nsobject-swift.class/shouldgroupaccessibilitychildren.md)

### 实例方法

- [- acceptsPreviewPanelControl:](<nsobject-swift.class/acceptspreviewpanelcontrol(__).md>)
- [- accessibilityElementAtIndex:](<nsobject-swift.class/accessibilityelement(at_).md>)
- [- accessibilityElementCount](<nsobject-swift.class/accessibilityelementcount().md>)
- [- accessibilityHitTest:](<nsobject-swift.class/accessibilityhittest(__).md>)
- [- accessibilityHitTest:withEvent:](<nsobject-swift.class/accessibilityhittest(__event_).md>)
- [- accessibilityLineEndPositionFromCurrentSelection](<nsobject-swift.class/accessibilitylineendpositionfromcurrentselection().md>)
- [- accessibilityLineRangeForPosition:](<nsobject-swift.class/accessibilitylinerange(forposition_).md>)
- [- accessibilityLineStartPositionFromCurrentSelection](<nsobject-swift.class/accessibilitylinestartpositionfromcurrentselection().md>)
- [- accessibilityZoomInAtPoint:](<nsobject-swift.class/accessibilityzoomin(at_).md>) — 放大指定点处的内容。
- [- accessibilityZoomOutAtPoint:](<nsobject-swift.class/accessibilityzoomout(at_).md>) — 缩小指定点处的内容。
- [- actionProperty](<nsobject-swift.class/actionproperty().md>) — 发送给委托，以请求该操作所应用的属性。
- [- attemptRecoveryFromError:optionIndex:](<nsobject-swift.class/attemptrecovery(fromerror_optionindex_).md>) — 实现此方法，以尝试从 App 模态对话框中显示的错误恢复。
- [- attemptRecoveryFromError:optionIndex:delegate:didRecoverSelector:contextInfo:](<nsobject-swift.class/attemptrecovery(fromerror_optionindex_delegate_didrecoverselector_contextinfo_).md>) — 实现此方法，以尝试从文稿模态表单中显示的错误恢复。
- [- authorizationViewCreatedAuthorization:](<nsobject-swift.class/authorizationviewcreatedauthorization(__).md>) — 发送给委托，以指示授权对象已创建或更改。
- [- authorizationViewDidAuthorize:](<nsobject-swift.class/authorizationviewdidauthorize(__).md>) — 发送给委托，以指示用户已获授权，且授权视图已更改为解锁状态。
- [- authorizationViewDidDeauthorize:](<nsobject-swift.class/authorizationviewdiddeauthorize(__).md>) — 发送给委托，以指示用户已被取消授权，且授权视图已更改为锁定状态。
- [- authorizationViewDidHide:](<nsobject-swift.class/authorizationviewdidhide(__).md>) — 发送给委托，以指示视图的可见性已更改。
- [- authorizationViewReleasedAuthorization:](<nsobject-swift.class/authorizationviewreleasedauthorization(__).md>) — 发送给委托，以指示即将取消授权。
- [- authorizationViewShouldDeauthorize:](<nsobject-swift.class/authorizationviewshoulddeauthorize(__).md>) — 当用户点击打开的锁图标时发送给委托。
- [- awakeFromNib](<nsobject-swift.class/awakefromnib().md>) — 在从 Interface Builder 归档或 nib 文件加载后，使接收者准备好提供服务。
- [- beginPreviewPanelControl:](<nsobject-swift.class/beginpreviewpanelcontrol(__).md>)
- [- browserAccessibilityImageData:](<nsobject-swift.class/browseraccessibilityimagedata(__).md>)
- [- burnProgressPanel:burnDidFinish:](<nsobject-swift.class/burnprogresspanel(__burndidfinish_).md>) — 允许委托处理刻录结束反馈。
- [- burnProgressPanelDidFinish:](<nsobject-swift.class/burnprogresspaneldidfinish(__).md>) — 面板在 order out 之后发送的通知。
- [- burnProgressPanelWillBegin:](<nsobject-swift.class/burnprogresspanelwillbegin(__).md>) — 面板在显示前发送的通知。
- [- candidates:](<nsobject-swift.class/candidates(__).md>) — 返回候选数组。
- [- certificatePanelShowHelp:](<nsobject-swift.class/certificatepanelshowhelp(__).md>) — 为实现该模态面板实现自定义帮助行为。
- [- chooseIdentityPanelShowHelp:](<nsobject-swift.class/chooseidentitypanelshowhelp(__).md>) — 为实现该模态面板实现自定义帮助行为。
- [- commitComposition:](<nsobject-swift.class/commitcomposition(__).md>) — 通知控制器应提交组合。
- [- composedString:](<nsobject-swift.class/composedstring(__).md>) — 返回当前的组合字符串。
- [- compositionParameterView:didChangeParameterWithKey:](<nsobject-swift.class/compositionparameterview(__didchangeparameterwithkey_).md>) — 在合成参数视图中的输入参数被编辑后调用。 _(已废弃)_
- [- compositionParameterView:shouldDisplayParameterWithKey:attributes:](<nsobject-swift.class/compositionparameterview(__shoulddisplayparameterwithkey_attributes_).md>) — 允许你定义在合成参数视图刷新时，哪些合成参数在用户界面中可见。 _(已废弃)_
- [- compositionPickerView:didSelectComposition:](<nsobject-swift.class/compositionpickerview(__didselect_).md>) — 当合成选择器视图中的所选合成更改时执行自定义任务。 _(已废弃)_
- [- compositionPickerViewDidStartAnimating:](<nsobject-swift.class/compositionpickerviewdidstartanimating(__).md>) — 当合成选择器视图开始为合成设置动画时执行自定义任务。 _(已废弃)_
- [- compositionPickerViewWillStopAnimating:](<nsobject-swift.class/compositionpickerviewwillstopanimating(__).md>) — 当合成选择器视图停止为合成设置动画时执行自定义任务。 _(已废弃)_
- [- didCommandBySelector:client:](<nsobject-swift.class/didcommand(by_client_).md>) — 处理由用户操作（例如键入某些键或按下鼠标按钮）生成的命令。
- [- doesContain:](<nsobject-swift.class/doescontain(__).md>) — 返回一个布尔值，指示接收者是否包含给定对象。
- [- endPreviewPanelControl:](<nsobject-swift.class/endpreviewpanelcontrol(__).md>)
- [- eraseProgressPanel:eraseDidFinish:](<nsobject-swift.class/eraseprogresspanel(__erasedidfinish_).md>) — 面板在显示前发送的通知。
- [- eraseProgressPanelDidFinish:](<nsobject-swift.class/eraseprogresspaneldidfinish(__).md>) — 面板在 order out 之后发送的通知。
- [- eraseProgressPanelWillBegin:](<nsobject-swift.class/eraseprogresspanelwillbegin(__).md>) — 面板在显示前发送的通知。
- [- exceptionHandler:shouldHandleException:mask:](<nsobject-swift.class/exceptionhandler(__shouldhandle_mask_).md>) — 由委托实现，用于评估委托方异常处理程序是否应处理给定异常。
- [- exceptionHandler:shouldLogException:mask:](<nsobject-swift.class/exceptionhandler(__shouldlogexception_mask_).md>) — 由委托实现，用于评估委托方异常处理程序是否应记录给定异常。
- [- fileTransferServicesAbortComplete:error:](<nsobject-swift.class/filetransferservicesabortcomplete(__error_).md>)
- [- fileTransferServicesConnectionComplete:error:](<nsobject-swift.class/filetransferservicesconnectioncomplete(__error_).md>)
- [- fileTransferServicesCopyRemoteFileComplete:error:](<nsobject-swift.class/filetransferservicescopyremotefilecomplete(__error_).md>)
- [- fileTransferServicesCopyRemoteFileProgress:transferProgress:](<nsobject-swift.class/filetransferservicescopyremotefileprogress(__transferprogress_).md>)
- [- fileTransferServicesCreateFolderComplete:error:folder:](<nsobject-swift.class/filetransferservicescreatefoldercomplete(__error_folder_).md>)
- [- fileTransferServicesDisconnectionComplete:error:](<nsobject-swift.class/filetransferservicesdisconnectioncomplete(__error_).md>)
- [- fileTransferServicesFilePreparationComplete:error:](<nsobject-swift.class/filetransferservicesfilepreparationcomplete(__error_).md>)
- [- fileTransferServicesPathChangeComplete:error:finalPath:](<nsobject-swift.class/filetransferservicespathchangecomplete(__error_finalpath_).md>)
- [- fileTransferServicesRemoveItemComplete:error:removedItem:](<nsobject-swift.class/filetransferservicesremoveitemcomplete(__error_removeditem_).md>)
- [- fileTransferServicesRetrieveFolderListingComplete:error:listing:](<nsobject-swift.class/filetransferservicesretrievefolderlistingcomplete(__error_listing_).md>)
- [- fileTransferServicesSendFileComplete:error:](<nsobject-swift.class/filetransferservicessendfilecomplete(__error_).md>)
- [- fileTransferServicesSendFileProgress:transferProgress:](<nsobject-swift.class/filetransferservicessendfileprogress(__transferprogress_).md>)
- [- handleEvent:client:](<nsobject-swift.class/handle(__client_).md>) — 处理按键按下和鼠标事件。
- [- imageBrowser:backgroundWasRightClickedWithEvent:](<nsobject-swift.class/imagebrowser(__backgroundwasrightclickedwith_).md>) — 当用户右键点按图像浏览器视图背景时执行自定义任务。
- [- imageBrowser:cellWasDoubleClickedAtIndex:](<nsobject-swift.class/imagebrowser(__cellwasdoubleclickedat_).md>) — 当用户在图像浏览器视图中双击某个项目时执行自定义任务。
- [- imageBrowser:cellWasRightClickedAtIndex:withEvent:](<nsobject-swift.class/imagebrowser(__cellwasrightclickedat_with_).md>) — 当用户在图像浏览器视图中右键点按某个项目时执行自定义任务。
- [- imageBrowser:groupAtIndex:](<nsobject-swift.class/imagebrowser(__groupat_).md>) — 返回指定索引处的组。
- [- imageBrowser:itemAtIndex:](<nsobject-swift.class/imagebrowser(__itemat_).md>) — 返回图像浏览器视图中对应于指定索引的项目对象。
- [- imageBrowser:moveItemsAtIndexes:toIndex:](<nsobject-swift.class/imagebrowser(__moveitemsat_to_).md>) — 发出信号，指示应将指定项目移动到指定目标位置。
- [- imageBrowser:removeItemsAtIndexes:](<nsobject-swift.class/imagebrowser(__removeitemsat_).md>) — 表示应对指定项目应用移除操作。
- [- imageBrowser:writeItemsAtIndexes:toPasteboard:](<nsobject-swift.class/imagebrowser(__writeitemsat_to_).md>) — 表示应开始拖放。
- [- imageBrowserSelectionDidChange:](<nsobject-swift.class/imagebrowserselectiondidchange(__).md>) — 在选中项更改时执行自定义任务。
- [- imageRepresentation](<nsobject-swift.class/imagerepresentation().md>) — 返回要显示的图像。
- [- imageRepresentationType](<nsobject-swift.class/imagerepresentationtype().md>) — 返回要显示图像的表示类型。
- [- imageSubtitle](<nsobject-swift.class/imagesubtitle().md>) — 返回图像的显示副标题。
- [- imageTitle](<nsobject-swift.class/imagetitle().md>) — 返回图像的显示标题。
- [- imageUID](<nsobject-swift.class/imageuid().md>) — 返回标识数据源项的唯一字符串。
- [- imageVersion](<nsobject-swift.class/imageversion().md>) — 返回项的版本。
- [- indexOfAccessibilityElement:](<nsobject-swift.class/index(ofaccessibilityelement_).md>)
- [- indicesOfObjectsByEvaluatingObjectSpecifier:](<nsobject-swift.class/indicesofobjects(byevaluatingobjectspecifier_).md>) — 返回指定容器对象的索引。
- [- inputText:client:](<nsobject-swift.class/inputtext(__client_).md>) — 处理未映射到操作方法的按键按下事件。
- [- inputText:key:modifiers:client:](<nsobject-swift.class/inputtext(__key_modifiers_client_).md>) — 接收 Unicode、生成它的键码以及任何修饰键标志。
- [- isCaseInsensitiveLike:](<nsobject-swift.class/iscaseinsensitivelike(__).md>) — 返回一个布尔值，指示在忽略接收者中字符大小写时，是否认为接收者“像”给定字符串。
- [- isEqualTo:](<nsobject-swift.class/isequal(to_).md>) — 返回一个布尔值，指示接收者是否等于另一个给定对象。
- [- isGreaterThan:](<nsobject-swift.class/isgreaterthan(__).md>) — 返回一个布尔值，指示接收者是否大于另一个给定对象。
- [- isGreaterThanOrEqualTo:](<nsobject-swift.class/isgreaterthanorequal(to_).md>) — 返回一个布尔值，指示接收者是否大于或等于另一个给定对象。
- [- isLessThan:](<nsobject-swift.class/islessthan(__).md>) — 返回一个布尔值，指示接收者是否小于另一个给定对象。
- [- isLessThanOrEqualTo:](<nsobject-swift.class/islessthanorequal(to_).md>) — 返回一个布尔值，指示接收者是否小于或等于另一个给定对象。
- [- isLike:](<nsobject-swift.class/islike(__).md>) — 返回一个布尔值，指示接收者是否“像”另一个给定对象。
- [- isNotEqualTo:](<nsobject-swift.class/isnotequal(to_).md>) — 返回一个布尔值，指示接收者是否不等于另一个给定对象。
- [- numberOfGroupsInImageBrowser:](<nsobject-swift.class/numberofgroups(inimagebrowser_).md>) — 返回图像浏览器视图中的组数。
- [- numberOfItemsInImageBrowser:](<nsobject-swift.class/numberofitems(inimagebrowser_).md>) — 返回数据源对象管理的记录数。
- [- originalString:](<nsobject-swift.class/originalstring(__).md>) — 返回由预组合 Unicode 字符组成的字符串。
- [- performActionForPerson:identifier:](<nsobject-swift.class/performaction(for_identifier_).md>) — 发送给委托以执行该操作。
- [- prepareForInterfaceBuilder](<nsobject-swift.class/prepareforinterfacebuilder().md>) — 在 Interface Builder 中创建可设计对象时调用。
- [- provideImageToMTLTexture:commandBuffer:originx:originy:width:height:userInfo:](<nsobject-swift.class/provideimage(to_commandbuffer_originx_originy_width_height_userinfo_).md>) — 图像提供程序对象可以实现的可选方法。
使用此方法，提供程序对象可以使用 Metal API 提供像素
数据到 MTLTexture 中，以便在渲染图像对象时使用。
- [- provideImageData:bytesPerRow:origin::size::userInfo:](<nsobject-swift.class/provideimagedata(__bytesperrow_origin___size___userinfo_).md>) — 向 `CIImage` 对象提供数据。
- [- quartzFilterManager:didAddFilter:](<nsobject-swift.class/quartzfiltermanager(__didadd_).md>)
- [- quartzFilterManager:didModifyFilter:](<nsobject-swift.class/quartzfiltermanager(__didmodifyfilter_).md>)
- [- quartzFilterManager:didRemoveFilter:](<nsobject-swift.class/quartzfiltermanager(__didremove_).md>)
- [- quartzFilterManager:didSelectFilter:](<nsobject-swift.class/quartzfiltermanager(__didselect_).md>)
- [- readLinkQualityForDeviceComplete:device:info:error:](<nsobject-swift.class/readlinkquality(fordevicecomplete_device_info_error_).md>)
- [- readRSSIForDeviceComplete:device:info:error:](<nsobject-swift.class/readrssi(fordevicecomplete_device_info_error_).md>)
- [- saveOptions:shouldShowUTType:](<nsobject-swift.class/saveoptions(__shouldshowuttype_).md>) — 调用以确定是否应在存储面板中显示指定的统一类型标识符。
- [- setSharedObservers:](<nsobject-swift.class/setsharedobservers(__).md>)
- [- setupPanel:determineBestDeviceOfA:orB:](<nsobject-swift.class/setuppanel(__determinebestdeviceofa_orb_).md>) — 允许委托指定其首选设备。
- [- setupPanel:deviceContainsSuitableMedia:promptString:](<nsobject-swift.class/setuppanel(__devicecontainssuitablemedia_promptstring_).md>) — 此委托方法允许委托确定设备中插入的介质是否适合要执行的操作。
- [- setupPanel:deviceCouldBeTarget:](<nsobject-swift.class/setuppanel(__devicecouldbetarget_).md>) — 允许委托确定设备是否可用作目标。
- [- setupPanelDeviceSelectionChanged:](<nsobject-swift.class/setuppaneldeviceselectionchanged(__).md>) — 当面板中的设备选中项更改时，由默认通知中心发送。
- [- setupPanelShouldHandleMediaReservations:](<nsobject-swift.class/setuppanelshouldhandlemediareservations(__).md>) — 此委托方法允许委托控制如何处理媒体预留。
- [- shouldEnableActionForPerson:identifier:](<nsobject-swift.class/shouldenableaction(for_identifier_).md>) — 发送给委托以确定是否应启用该操作。
- [- titleForPerson:identifier:](<nsobject-swift.class/title(for_identifier_).md>) — 发送给委托以请求该操作的菜单项标题。
- [- workflowController:didError:](<nsobject-swift.class/workflowcontroller(__diderror_).md>) _(已废弃)_
- [- workflowController:didRunAction:](<nsobject-swift.class/workflowcontroller(__didrun_).md>) _(已废弃)_
- [- workflowController:willRunAction:](<nsobject-swift.class/workflowcontroller(__willrun_).md>) _(已废弃)_
- [- workflowControllerDidRun:](<nsobject-swift.class/workflowcontrollerdidrun(__).md>) _(已废弃)_
- [- workflowControllerDidStop:](<nsobject-swift.class/workflowcontrollerdidstop(__).md>) _(已废弃)_
- [- workflowControllerWillRun:](<nsobject-swift.class/workflowcontrollerwillrun(__).md>) _(已废弃)_
- [- workflowControllerWillStop:](<nsobject-swift.class/workflowcontrollerwillstop(__).md>) _(已废弃)_

### 类型方法

- [+ debugDescription](<nsobject-swift.class/debugdescription().md>)
- [+ hash](<nsobject-swift.class/hash().md>)

### 默认实现

- [Equatable 实现](nsobject-swift.class/equatable-implementations.md)
- [Hashable 实现](nsobject-swift.class/hashable-implementations.md)

## 另请参阅

### 类

- [Protocol](protocol.md)
