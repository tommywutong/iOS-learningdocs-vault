---
title: 已废弃的修饰符
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-deprecated
source_url: 'https://developer.apple.com/documentation/swiftui/view-deprecated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-deprecated.json'
content_hash: 'sha256:53eeba13f5eef550'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [视图基础](view-fundamentals.md) · [View](view.md)

# 已废弃的修饰符

<sub>API 集合</sub>

查看不再受支持的修饰符及其替代方案。

## 概述

避免在你的 App 中使用已废弃的修饰符。选择一个修饰符来查看你应当改用的替代方案。

## 主题

### 辅助功能修饰符

- [accessibility(label:)](<view/accessibility(label_).md>) — 向视图添加一个描述其内容的标签。 _(已废弃)_
- [accessibility(value:)](<view/accessibility(value_).md>) — 添加视图所包含值的文本描述。 _(已废弃)_
- [accessibility(hidden:)](<view/accessibility(hidden_).md>) — 指定是否对系统辅助功能隐藏此视图。 _(已废弃)_
- [accessibility(identifier:)](<view/accessibility(identifier_).md>) — 使用指定的字符串来标识视图。 _(已废弃)_
- [accessibility(selectionIdentifier:)](<view/accessibility(selectionidentifier_).md>) — 为此视图的辅助功能元素设置选择标识符。 _(已废弃)_
- [accessibility(hint:)](<view/accessibility(hint_).md>) — 告知用户执行视图的操作后会发生什么。 _(已废弃)_
- [accessibility(activationPoint:)](<view/accessibility(activationpoint_).md>) — 指定视图中发生激活的点。 _(已废弃)_
- [accessibility(inputLabels:)](<view/accessibility(inputlabels_).md>) — 设置用户用来识别视图的备用输入标签。 _(已废弃)_
- [accessibility(addTraits:)](<view/accessibility(addtraits_).md>) — 向视图添加给定的特性。 _(已废弃)_
- [accessibility(removeTraits:)](<view/accessibility(removetraits_).md>) — 从此视图移除给定的特性。 _(已废弃)_
- [accessibility(sortPriority:)](<view/accessibility(sortpriority_).md>) — 相对于同一层级的其他元素，为此视图的辅助功能元素设置排序优先级。 _(已废弃)_

### 外观修饰符

- [colorScheme(_:)](<view/colorscheme(__).md>) — 设置此视图的颜色方案。 _(已废弃)_
- [listRowPlatterColor(_:)](<view/listrowplattercolor(__).md>) — 设置当此视图被放置在列表中时系统应用到行背景的颜色。 _(已废弃)_
- [background(_:alignment:)](<view/background(__alignment_).md>) — 将给定视图层叠在此视图后面。 _(已废弃)_
- [overlay(_:alignment:)](<view/overlay(__alignment_).md>) — 将一个次要视图层叠在此视图前面。 _(已废弃)_
- [foregroundColor(_:)](<view/foregroundcolor(__).md>) — 设置此视图显示的前景元素的颜色。 _(已废弃)_
- [complicationForeground()](<view/complicationforeground().md>) — 在复杂功能中将此视图提升到前景。 _(已废弃)_

### 文本修饰符

- [autocapitalization(_:)](<view/autocapitalization(__).md>) — 设置是否对此视图应用自动大写。 _(已废弃)_
- [disableAutocorrection(_:)](<view/disableautocorrection(__).md>) — 设置是否对此视图停用自动更正。 _(已废弃)_

### 辅助视图修饰符

- [navigationBarTitle(_:)](<view/navigationbartitle(__).md>) — 在导航栏中为此视图设置标题。 _(已废弃)_
- [navigationBarTitle(_:displayMode:)](<view/navigationbartitle(__displaymode_).md>) — 在导航栏中为此视图设置标题和显示模式。 _(已废弃)_
- [navigationBarItems(leading:)](<view/navigationbaritems(leading_).md>) — 为此视图设置导航栏条目。 _(已废弃)_
- [navigationBarItems(leading:trailing:)](<view/navigationbaritems(leading_trailing_).md>) — 为此视图设置导航栏条目。 _(已废弃)_
- [navigationBarItems(trailing:)](<view/navigationbaritems(trailing_).md>) — 为此视图配置导航栏条目。 _(已废弃)_
- [navigationBarHidden(_:)](<view/navigationbarhidden(__).md>) — 隐藏此视图的导航栏。 _(已废弃)_
- [statusBar(hidden:)](<view/statusbar(hidden_).md>) — 设置状态栏的可见性。 _(已废弃)_
- [contextMenu(_:)](<view/contextmenu(__).md>) — 向视图添加上下文菜单。 _(已废弃)_

### 样式修饰符

- [menuButtonStyle(_:)](<view/menubuttonstyle(__).md>) — 设置此视图内菜单按钮的样式。 _(已废弃)_
- [navigationViewStyle(_:)](<view/navigationviewstyle(__).md>) — 设置此视图内导览视图的样式。 _(已废弃)_

### 布局修饰符

- [frame()](<view/frame().md>) — 将此视图放置在一个不可见的 frame 内。 _(已废弃)_
- [edgesIgnoringSafeArea(_:)](<view/edgesignoringsafearea(__).md>) — 更改视图的拟议区域，使其延伸到屏幕安全区之外。 _(已废弃)_
- [coordinateSpace(name:)](<view/coordinatespace(name_).md>) — 为视图的坐标空间指定一个名称，以便其他代码可以相对于该命名空间操作点、大小等维度。 _(已废弃)_

### 图形与渲染修饰符

- [accentColor(_:)](<view/accentcolor(__).md>) — 为此视图及其包含的视图设置强调色。 _(已废弃)_
- [mask(_:)](<view/mask(__).md>) — 使用给定视图的 alpha 通道遮罩此视图。 _(已废弃)_
- [animation(_:)](<view/animation(__)-1hc0p.md>) — 将给定的动画应用到该视图内的所有可动画值。 _(已废弃)_
- [cornerRadius(_:antialiased:)](<view/cornerradius(__antialiased_).md>) — 以指定的圆角半径将此视图裁剪到其边界 frame。 _(已废弃)_

### 输入与事件修饰符

- [dropDestination(for:action:isTargeted:)](<view/dropdestination(for_action_istargeted_).md>) — 定义拖放操作的目的地，使用你指定的闭包处理被拖放的内容。 _(已废弃)_
- [onChange(of:perform:)](<view/onchange(of_perform_).md>) — 添加一个在给定值发生变化时执行的操作。 _(已废弃)_
- [onTapGesture(count:coordinateSpace:perform:)](<view/ontapgesture(count_coordinatespace_perform_)-36x9h.md>) — 添加一个在此视图识别到点按手势时执行的操作，并向该操作提供交互发生的位置。 _(已废弃)_
- [onLongPressGesture(minimumDuration:maximumDistance:pressing:perform:)](<view/onlongpressgesture(minimumduration_maximumdistance_pressing_perform_).md>) — 添加一个在此视图识别到长按手势时执行的操作。 _(已废弃)_
- [onLongPressGesture(minimumDuration:pressing:perform:)](<view/onlongpressgesture(minimumduration_pressing_perform_).md>) — 添加一个在此视图识别到长按手势时执行的操作。 _(已废弃)_
- [onPasteCommand(of:perform:)](<view/onpastecommand(of_perform_)-4f78f.md>) — 添加一个为响应系统的粘贴命令而执行的操作。 _(已废弃)_
- [onPasteCommand(of:validator:perform:)](<view/onpastecommand(of_validator_perform_)-964k1.md>) — 添加一个为响应系统的粘贴命令而执行的操作，并由你校验其中的条目。 _(已废弃)_
- [onDrop(of:delegate:)](<view/ondrop(of_delegate_)-2vr9o.md>) — 为拖放操作定义一个与此视图大小和位置相同的目的地，其行为由给定的委托控制。 _(已废弃)_
- [onDrop(of:isTargeted:perform:)](<view/ondrop(of_istargeted_perform_).md>) — 定义拖放操作的目的地，使用你指定的闭包处理被拖放的内容。
- [focusable(_:onFocusChange:)](<view/focusable(__onfocuschange_).md>) — 指定视图是否可聚焦，如果可以，则添加一个在视图获得焦点时执行的操作。 _(已废弃)_
- [onContinuousHover(coordinateSpace:perform:)](<view/oncontinuoushover(coordinatespace_perform_)-8gyrl.md>) — 添加一个在指针进入、移动于和离开视图边界时执行的操作。 _(已废弃)_

### 视图呈现修饰符

- [actionSheet(isPresented:content:)](<view/actionsheet(ispresented_content_).md>) — 当给定条件为真时呈现一个操作表单。 _(已废弃)_
- [actionSheet(item:content:)](<view/actionsheet(item_content_).md>) — 呈现一个操作表单，使用给定条目作为表单内容的数据源。 _(已废弃)_
- [alert(isPresented:content:)](<view/alert(ispresented_content_).md>) — 向用户呈现一个提醒。 _(已废弃)_
- [alert(item:content:)](<view/alert(item_content_).md>) — 向用户呈现一个提醒。 _(已废弃)_

### 搜索修饰符

- [searchable(text:placement:prompt:suggestions:)](<view/searchable(text_placement_prompt_suggestions_).md>) — 将此视图标记为可搜索，这会配置一个搜索栏的显示。 _(已废弃)_

### 标签页修饰符

- [tabItem(_:)](<view/tabitem(__).md>) — 设置与此视图关联的标签页栏条目。 _(已废弃)_

### 生成图像修饰符

- [imagePlaygroundPersonalizationPolicy(_:)](<view/imageplaygroundpersonalizationpolicy(__).md>) — 决定是否支持在 playground 中使用人物的政策。 _(已废弃)_

### 特定技术修饰符

- [postToPhotosSharedAlbumSheet(isPresented:items:photoLibrary:defaultAlbumIdentifier:completion:)](<view/posttophotossharedalbumsheet(ispresented_items_photolibrary_defaultalbumidentifier_completion_).md>) — 呈现一个「添加到共享相簿」表单，允许用户将给定条目发布到共享相簿。 _(已废弃)_
- [offerCodeRedemption(isPresented:onCompletion:)](<view/offercoderedemption(ispresented_oncompletion_).md>) _(已废弃)_
- [subscriptionPromotionalOffer(offer:signature:)](<view/subscriptionpromotionaloffer(offer_signature_).md>) — 选择一个促销优惠，应用于顾客从订阅商店视图进行的购买。 _(已废弃)_
