---
title: UIAccessibility
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility-protocol
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility-protocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility-protocol.json'
content_hash: 'sha256:8c807bf35f225750'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Accessibility for UIKit](accessibility-for-uikit.md)

# UIAccessibility

<sub>API 集合</sub>

一组方法，提供有关 App 用户界面中视图和控制的辅助功能信息。

## 概述

`UIAccessibility` 非正式协议提供有关 App 用户界面元素的辅助功能信息。诸如旁白等辅助 App 会将这些信息传达给有障碍的用户，帮助他们使用该 App。

标准 UIKit 控制和视图实现了 `UIAccessibility` 方法，默认即可被辅助 App 访问。这意味着，如果你的 App 只使用标准控制和视图，例如 [UIButton](uibutton.md)、[UISegmentedControl](uisegmentedcontrol.md) 和 [UITableView](uitableview.md)，你只需要在默认值不完整时补充 App 特有的细节。你可以在 Interface Builder 中设置这些值，或通过设置该非正式协议中的属性来实现。

代表自定义用户界面对象的 [UIAccessibilityElement](uiaccessibilityelement.md) 类同样实现了 `UIAccessibility` 非正式协议。如果你创建了一个完全自定义的 [UIView](https://developer.apple.com/library/archive/releasenotes/iPhone/RN-iPhoneSDK/index.html#//apple_ref/doc/uid/TP40007428-CH1-SW18) 子类，你可能需要创建一个 [UIAccessibilityElement](uiaccessibilityelement.md) 实例来代表它。在这种情况下，你需要支持全部 `UIAccessibility` 属性，以正确设置并返回该辅助功能元素的属性。

## 主题

### 支持基本辅助功能

- [isAccessibilityElement](../objectivec/nsobject-swift.class/isaccessibilityelement.md)
- [accessibilityLabel](../objectivec/nsobject-swift.class/accessibilitylabel.md)
- [accessibilityValue](../objectivec/nsobject-swift.class/accessibilityvalue.md)
- [accessibilityHint](../objectivec/nsobject-swift.class/accessibilityhint.md)
- [accessibilityTraits](../objectivec/nsobject-swift.class/accessibilitytraits.md)
- [UIAccessibilityTraits](uiaccessibilitytraits.md) — 描述辅助功能元素行为方式的常量。

### 定义辅助功能文本与语言

- [Speech attributes for attributed strings](speech-attributes-for-attributed-strings.md) — 为属性字符串中的文本应用属性，以修改该文本的发音方式。
- [Text attributes for attributed strings](text-attributes-for-attributed-strings.md) — 为属性字符串中的文本应用属性，以传达关于该文本的额外信息。
- [accessibilityHeaderElements](../objectivec/nsobject-swift.class/accessibilityheaderelements.md)
- [accessibilityAttributedHint](../objectivec/nsobject-swift.class/accessibilityattributedhint.md)
- [accessibilityAttributedLabel](../objectivec/nsobject-swift.class/accessibilityattributedlabel.md)
- [accessibilityLanguage](../objectivec/nsobject-swift.class/accessibilitylanguage.md)
- [accessibilityTextualContext](../objectivec/nsobject-swift.class/accessibilitytextualcontext.md)
- [accessibilityUserInputLabels](../objectivec/nsobject-swift.class/accessibilityuserinputlabels.md)
- [accessibilityAttributedUserInputLabels](../objectivec/nsobject-swift.class/accessibilityattributeduserinputlabels.md)
- [accessibilityAttributedValue](../objectivec/nsobject-swift.class/accessibilityattributedvalue.md)

### 配置行为

- [accessibilityCustomRotors](../objectivec/nsobject-swift.class/accessibilitycustomrotors.md)
- [accessibilityElementsHidden](../objectivec/nsobject-swift.class/accessibilityelementshidden.md)
- [accessibilityRespondsToUserInteraction](../objectivec/nsobject-swift.class/accessibilityrespondstouserinteraction.md)
- [accessibilityViewIsModal](../objectivec/nsobject-swift.class/accessibilityviewismodal.md)
- [shouldGroupAccessibilityChildren](../objectivec/nsobject-swift.class/shouldgroupaccessibilitychildren.md)
- [accessibilityDirectTouchOptions](../objectivec/nsobject-swift.class/accessibilitydirecttouchoptions.md)
- [DirectTouchOptions](uiaccessibility/directtouchoptions.md) — 用于配置旁白如何为直接触摸区域生成音频的常量。

### 处理通知

- [Notification names](notification-names.md) — 辅助功能系统生成的各种通知的名称。
- [Notification dictionary keys](notification-dictionary-keys.md) — 使用用户信息字典中的键处理通知。
- [Notification](uiaccessibility/notification.md) — App 可以发送的一种辅助功能通知。
- [UIAccessibilityPostNotification](<uiaccessibility/post(notification_argument_).md>) — 向辅助 App 发布一条通知。

### 在元素间导览

- [UIAccessibilityContainer](uiaccessibilitycontainer.md) — 提供一组方法，供视图子类使用，以使子组件能作为独立元素被辅助功能访问。
- [accessibilityActivationPoint](../objectivec/nsobject-swift.class/accessibilityactivationpoint.md)
- [accessibilityFocusedUIElement](../objectivec/nsobject-swift.class/accessibilityfocuseduielement.md)
- [accessibilityFrame](../objectivec/nsobject-swift.class/accessibilityframe.md)
- [accessibilityHitTest(_:)](<../objectivec/nsobject-swift.class/accessibilityhittest(__).md>)
- [accessibilityNavigationStyle](../objectivec/nsobject-swift.class/accessibilitynavigationstyle.md)
- [UIAccessibilityNavigationStyle](uiaccessibilitynavigationstyle.md) — 描述如何用辅助 App 在某个对象的各元素间导览的常量。
- [accessibilityPath](../objectivec/nsobject-swift.class/accessibilitypath.md)
- [UIAccessibilityZoomFocusChanged](<uiaccessibility/zoomfocuschanged(zoomtype_toframe_in_).md>) — 当 App 的焦点变化到新位置时通知系统。
- [ZoomType](uiaccessibility/zoomtype.md) — 可生效的系统缩放类型。
- [UIGuidedAccessAccessibilityFeatureAssistiveTouch](uiguidedaccessaccessibilityfeature/assistivetouch.md) — 辅助触控辅助功能。

### 支持类型

- [AXArrayReturnBlock](axarrayreturnblock.md)
- [AXAttributedStringArrayReturnBlock](axattributedstringarrayreturnblock.md)
- [AXAttributedStringReturnBlock](axattributedstringreturnblock.md)
- [AXBoolReturnBlock](axboolreturnblock.md)
- [AXContainerTypeReturnBlock](axcontainertypereturnblock.md)
- [AXCustomActionsReturnBlock](axcustomactionsreturnblock.md)
- [AXCustomRotorsReturnBlock](axcustomrotorsreturnblock.md)
- [AXNavigationStyleReturnBlock](axnavigationstylereturnblock.md)
- [AXObjectReturnBlock](axobjectreturnblock.md)
- [AXPathReturnBlock](axpathreturnblock.md)
- [AXPointReturnBlock](axpointreturnblock.md)
- [AXRectReturnBlock](axrectreturnblock.md)
- [AXStringArrayReturnBlock](axstringarrayreturnblock.md)
- [AXStringReturnBlock](axstringreturnblock.md)
- [AXTextualContextReturnBlock](axtextualcontextreturnblock.md)
- [AXTraitsReturnBlock](axtraitsreturnblock.md)
- [AXUITextInputReturnBlock](axuitextinputreturnblock.md)
- [AXVoidReturnBlock](axvoidreturnblock.md)
- [UIAccessibility](uiaccessibility.md) — 一个用于 UIKit App 的辅助功能符号命名空间。

## 另请参阅

### 相关文档

- [Accessibility](../accessibility.md) — 让所有使用 Apple 设备的人都能使用你的 App。
- [Accessibility for UIKit](accessibility-for-uikit.md) — 让所有使用 iOS 和 tvOS 的人都能使用你的 UIKit App。

### 基础

- [UIAccessibilityContainer](uiaccessibilitycontainer.md) — 提供一组方法，供视图子类使用，以使子组件能作为独立元素被辅助功能访问。
- [Supporting VoiceOver in your app](supporting-voiceover-in-your-app.md) — 在你的 App 中添加旁白支持，让失明或视力低下的用户能更好地使用你的 iOS App。
