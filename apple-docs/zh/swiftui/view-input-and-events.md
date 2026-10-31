---
title: 输入与事件修饰符
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-input-and-events
source_url: 'https://developer.apple.com/documentation/swiftui/view-input-and-events'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-input-and-events.json'
content_hash: 'sha256:185b040d871588d6'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [视图基础](view-fundamentals.md) · [View](view.md)

# 输入与事件修饰符

<sub>API 集合</sub>

提供供视图执行的操作，以响应用户输入和系统事件。

## 概述

使用输入与事件修饰符来为各种各样的用户输入或系统事件进行配置并提供处理程序。例如，你可以检测并控制焦点、响应视图出现和消失等生命周期事件、管理键盘快捷键等等。

## 主题

### 交互性

- [disabled(_:)](<view/disabled(__).md>) — 添加一个条件，控制用户能否与此视图交互。
- [interactionActivityTrackingTag(_:)](<view/interactionactivitytrackingtag(__).md>) — 设置一个用于跟踪交互性的标签。

### 列表控制

- [swipeActions(edge:allowsFullSwipe:content:)](<view/swipeactions(edge_allowsfullswipe_content_).md>) — 向列表中的行添加自定义轻扫操作。
- [refreshable(action:)](<view/refreshable(action_).md>) — 添加一个异步处理程序，当用户发起请求（例如下拉刷新）时，可更新视图显示的数据。
- [selectionDisabled(_:)](<view/selectiondisabled(__).md>) — 添加一个条件，控制用户能否选择此视图。

### 容器控制

- [swipeActions(edge:allowsFullSwipe:content:onPresentationChanged:)](<view/swipeactions(edge_allowsfullswipe_content_onpresentationchanged_).md>) — 向列表或容器中的行添加自定义轻扫操作，并在这些操作显示或收起时通知你。_(beta)_
- [swipeActionsContainer()](<view/swipeactionscontainer().md>) — 协调容器中各行的轻扫操作收起与互斥。_(beta)_

### 滚动控制

- [scrollPosition(_:anchor:)](<view/scrollposition(__anchor_).md>) — 将一个滚动位置的绑定 (binding) 与此视图内的滚动视图关联起来。
- [scrollPosition(id:anchor:)](<view/scrollposition(id_anchor_).md>) — 关联一个绑定，当此视图内的滚动视图滚动时更新该绑定。
- [defaultScrollAnchor(_:)](<view/defaultscrollanchor(__).md>) — 关联一个锚点，以控制默认情况下应渲染滚动视图内容的哪个部分。
- [defaultScrollAnchor(_:for:)](<view/defaultscrollanchor(__for_).md>) — 关联一个锚点，以控制在特定情境下滚动视图的位置。
- [scrollTargetBehavior(_:)](<view/scrolltargetbehavior(__).md>) — 设置在提供的轴向上可滚动视图的滚动行为。
- [scrollTargetLayout(isEnabled:)](<view/scrolltargetlayout(isenabled_).md>) — 将最外层的布局配置为滚动目标布局。
- [scrollInputBehavior(_:for:)](<view/scrollinputbehavior(__for_).md>) — 当使用特定输入时，在可滚动视图中启用或禁用滚动。
- [scrollTransition(_:axis:transition:)](<view/scrolltransition(__axis_transition_).md>) — 应用给定的过渡 (transition)，当此视图在包含它的滚动视图的可见区域内出现和消失时，在过渡的各阶段之间进行动画化。
- [scrollTransition(topLeading:bottomTrailing:axis:transition:)](<view/scrolltransition(topleading_bottomtrailing_axis_transition_).md>) — 应用给定的过渡，当此视图在包含它的滚动视图的可见区域内出现和消失时，在过渡的各阶段之间进行动画化。
- [onScrollGeometryChange(for:of:action:)](<view/onscrollgeometrychange(for_of_action_).md>) — 添加一个动作，当从滚动几何 (scroll geometry) 创建的值发生变化时执行。
- [onScrollTargetVisibilityChange(idType:threshold:_:)](<view/onscrolltargetvisibilitychange(idtype_threshold___).md>) — 添加一个动作，该动作被调用时会携带关于哪些视图被视为可见的信息。
- [onScrollVisibilityChange(threshold:_:)](<view/onscrollvisibilitychange(threshold___).md>) — 添加一个动作，当视图跨越被视为屏幕上或屏幕外的阈值时被调用。
- [onScrollPhaseChange(_:)](<view/onscrollphasechange(__).md>) — 添加一个动作，当层级结构中的第一个滚动视图的滚动阶段发生变化时执行。

### 几何

- [onGeometryChange(for:of:action:)](<view/ongeometrychange(for_of_action_).md>) — 添加一个操作，在由几何代理创建的值变化时执行。
- [onGeometryChange3D(for:of:action:)](<view/ongeometrychange3d(for_of_action_).md>) — 返回一个新视图，每当 `transform(proxy)` 计算出的值变化时都会调用 `action(value)`，其中 `proxy` 提供对该视图 3D 几何属性的访问。
- [onInteractiveResizeChange(_:)](<view/oninteractiveresizechange(__).md>) — 添加一个操作，在所属窗口正在被交互式调整大小时执行。

### 轻点与手势

- [onTapGesture(count:perform:)](<view/ontapgesture(count_perform_).md>) — 添加一个操作，在此视图识别出轻点手势时执行。
- [onTapGesture(count:coordinateSpace:perform:)](<view/ontapgesture(count_coordinatespace_perform_).md>) — 添加一个操作，在此视图识别出轻点手势时执行，并向该操作提供交互的位置。
- [onTapGesture(count:coordinateSpace:inputKinds:perform:)](<view/ontapgesture(count_coordinatespace_inputkinds_perform_).md>) — 添加一个操作，在此视图识别出轻点手势时执行，并向该操作提供交互的位置。_(beta)_
- [onLongPressGesture(minimumDuration:maximumDistance:perform:onPressingChanged:)](<view/onlongpressgesture(minimumduration_maximumdistance_perform_onpressingchanged_).md>) — 添加一个操作，在此视图识别出长按手势时执行。
- [onLongPressGesture(minimumDuration:maximumDistance:inputKinds:perform:onPressingChanged:)](<view/onlongpressgesture(minimumduration_maximumdistance_inputkinds_perform_onpressingchanged_).md>) — 添加一个操作，在此视图识别出长按手势时执行。_(beta)_
- [onLongPressGesture(minimumDuration:perform:onPressingChanged:)](<view/onlongpressgesture(minimumduration_perform_onpressingchanged_).md>) — 添加一个操作，在此视图识别出长按手势时执行。
- [onLongTouchGesture(minimumDuration:perform:onTouchingChanged:)](<view/onlongtouchgesture(minimumduration_perform_ontouchingchanged_).md>) — 添加一个操作，在此视图识别出遥控器长触手势时执行。长触手势是指手指放在遥控器触控表面上但并未实际按压。
- [gesture(_:)](<view/gesture(__).md>) — 将 [NSGestureRecognizerRepresentable](nsgesturerecognizerrepresentable.md) 附加到视图。
- [gesture(_:isEnabled:)](<view/gesture(__isenabled_).md>) — 将手势附加到视图，其优先级低于视图定义的手势。
- [gesture(_:name:isEnabled:)](<view/gesture(__name_isenabled_).md>) — 将手势附加到视图，其优先级低于视图定义的手势。
- [gesture(_:including:)](<view/gesture(__including_).md>) — 将手势附加到视图，其优先级低于视图定义的手势。
- [highPriorityGesture(_:including:)](<view/highprioritygesture(__including_).md>) — 将手势附加到视图，其优先级高于视图定义的手势。
- [highPriorityGesture(_:isEnabled:)](<view/highprioritygesture(__isenabled_).md>) — 将手势附加到视图，其优先级高于视图定义的手势。
- [highPriorityGesture(_:name:isEnabled:)](<view/highprioritygesture(__name_isenabled_).md>) — 将手势附加到视图，其优先级高于视图定义的手势。
- [simultaneousGesture(_:including:)](<view/simultaneousgesture(__including_).md>) — 将手势附加到视图，与视图定义的手势同时处理。
- [simultaneousGesture(_:isEnabled:)](<view/simultaneousgesture(__isenabled_).md>) — 将手势附加到视图，与视图定义的手势同时处理。
- [simultaneousGesture(_:name:isEnabled:)](<view/simultaneousgesture(__name_isenabled_).md>) — 将手势附加到视图，与视图定义的手势同时处理。
- [defersSystemGestures(on:)](<view/deferssystemgestures(on_).md>) — 设置屏幕边缘，使你的手势在该边缘优先于系统手势。
- [onPencilDoubleTap(perform:)](<view/onpencildoubletap(perform_).md>) — 添加一项操作，在用户双击 Apple Pencil 后执行。
- [onPencilSqueeze(perform:)](<view/onpencilsqueeze(perform_).md>) — 添加一项操作，在用户挤压 Apple Pencil 时执行。
- [allowsWindowActivationEvents()](<view/allowswindowactivationevents().md>) — 配置此视图层级结构中的手势来处理激活所属窗口的事件。
- [allowsWindowActivationEvents(_:)](<view/allowswindowactivationevents(__).md>) — 配置此视图层级结构中的手势能否处理激活所属窗口的事件。

### 键盘输入

- [onKeyPress(_:action:)](<view/onkeypress(__action_).md>) — 在此视图获得焦点时，如果用户按下硬件键盘上的某个键，则执行一个操作。
- [onKeyPress(phases:action:)](<view/onkeypress(phases_action_).md>) — 在此视图获得焦点时，如果用户按下硬件键盘上的任意键，则执行一个操作。
- [onKeyPress(_:phases:action:)](<view/onkeypress(__phases_action_).md>) — 在此视图获得焦点时，如果用户按下硬件键盘上的某个键，则执行一个操作。
- [onKeyPress(characters:phases:action:)](<view/onkeypress(characters_phases_action_).md>) — 在此视图获得焦点时，如果用户按下硬件键盘上的一个或多个键，则执行一个操作。
- [onKeyPress(keys:phases:action:)](<view/onkeypress(keys_phases_action_).md>) — 在此视图获得焦点时，如果用户按下硬件键盘上的一个或多个键，则执行一个操作。
- [onModifierKeysChanged(mask:initial:_:)](<view/onmodifierkeyschanged(mask_initial___).md>) — 每当用户按下或松开硬件修饰键时执行一个操作。

### 键盘快捷键

- [keyboardShortcut(_:)](<view/keyboardshortcut(__).md>) — 为被修饰的控制指定一个键盘快捷键。
- [keyboardShortcut(_:modifiers:)](<view/keyboardshortcut(__modifiers_).md>) — 定义一个键盘快捷键，并将其指定给被修饰的控制。
- [keyboardShortcut(_:modifiers:localization:)](<view/keyboardshortcut(__modifiers_localization_).md>) — 定义一个键盘快捷键，并将其指定给被修饰的控制。
- [modifierKeyAlternate(_:_:)](<view/modifierkeyalternate(____).md>) — 构建一个视图，当用户按下给定集合所指示的修饰键时，用它来替代被修饰的视图。

### 手部交互

- [handGestureShortcut(_:isEnabled:)](<view/handgestureshortcut(__isenabled_).md>) — 为被修饰的控制指定一个手部手势快捷键。
- [handPointerBehavior(_:)](<view/handpointerbehavior(__).md>) — 设置用户与此视图交互时手部指针的行为。
- [manipulable(coordinateSpace:operations:inertia:isEnabled:onChanged:)](<view/manipulable(coordinatespace_operations_inertia_isenabled_onchanged_).md>) — 允许使用常见的手部手势操控此视图。
- [manipulable(transform:coordinateSpace:operations:inertia:isEnabled:onChanged:)](<view/manipulable(transform_coordinatespace_operations_inertia_isenabled_onchanged_).md>) — 将给定的 3D 仿射变换应用到视图，并允许使用常见的手部手势操控它。
- [manipulable(using:)](<view/manipulable(using_).md>) — 允许使用附加到其他视图的操控手势来操控此视图。
- [manipulationGesture(updating:coordinateSpace:operations:inertia:isEnabled:onChanged:)](<view/manipulationgesture(updating_coordinatespace_operations_inertia_isenabled_onchanged_).md>) — 向此视图添加一个操控手势，但不允许此视图自身被操控。

### 悬停

- [onHover(perform:)](<view/onhover(perform_).md>) — 添加一个操作，在用户将指针移到视图框架上方或移离视图框架时执行。
- [onContinuousHover(coordinateSpace:perform:)](<view/oncontinuoushover(coordinatespace_perform_).md>) — 添加一个操作，在指针进入、在视图边界内移动以及离开视图边界时执行。
- [hoverEffect(_:)](<view/hovereffect(__).md>) — 将悬停效果应用到此视图。
- [hoverEffect(_:isEnabled:)](<view/hovereffect(__isenabled_).md>) — 将悬停效果应用到此视图。
- [hoverEffect(_:in:isEnabled:)](<view/hovereffect(__in_isenabled_).md>) — 将悬停效果应用到此视图，并可选地将其添加到 [HoverEffectGroup](hovereffectgroup.md)。
- [hoverEffect(in:isEnabled:body:)](<view/hovereffect(in_isenabled_body_).md>) — 将给定闭包描述的悬停效果应用到此视图。
- [hoverEffectGroup()](<view/hovereffectgroup().md>) — 向子视图中定义的所有效果添加一个隐式 [HoverEffectGroup](hovereffectgroup.md)，这样只要此视图或任何子视图被悬停，添加到子视图的所有效果就会作为一组激活。
- [hoverEffectGroup(_:)](<view/hovereffectgroup(__).md>) — 向子视图中定义的所有效果添加一个 [HoverEffectGroup](hovereffectgroup.md)，并且只要此视图或任何子视图被悬停，就会激活该组。
- [hoverEffectGroup(id:in:behavior:)](<view/hovereffectgroup(id_in_behavior_).md>) — 向子视图中定义的所有效果添加一个 [HoverEffectGroup](hovereffectgroup.md)，并且只要此视图或任何子视图被悬停，就会激活该组。
- [hoverEffectDisabled(_:)](<view/hovereffectdisabled(__).md>) — 添加一个条件，控制此视图是否可以显示悬停效果。
- [defaultHoverEffect(_:)](<view/defaulthovereffect(__).md>) — 设置此视图内各视图使用的默认悬停效果。
- [listRowHoverEffect(_:)](<view/listrowhovereffect(__).md>) — 请求所属列表行使用提供的悬停效果。
- [listRowHoverEffectDisabled(_:)](<view/listrowhovereffectdisabled(__).md>) — 请求禁用所属列表行的悬停效果。

### 指针

- [pointerVisibility(_:)](<view/pointervisibility(__).md>) — 设置指针位于视图上方时指针的可见性。
- [pointerStyle(_:)](<view/pointerstyle(__).md>) — 设置指针位于视图上方时要显示的指针样式。

### 焦点

- [focused(_:equals:)](<view/focused(__equals_).md>) — 通过将此视图的焦点状态绑定到给定的状态值来修改此视图。
- [focused(_:)](<view/focused(__).md>) — 通过将此视图的焦点状态绑定到给定的布尔状态值来修改此视图。
- [focusedValue(_:)](<view/focusedvalue(__).md>) — 为给定的对象类型设置焦点值。
- [focusedValue(_:_:)](<view/focusedvalue(____).md>) — 通过注入你提供的值来修改此视图，供状态依赖于焦点视图层级结构的其他视图使用。
- [focusedSceneValue(_:)](<view/focusedscenevalue(__).md>) — 在场景级作用域为给定的对象类型设置焦点值。
- [focusedSceneValue(_:_:)](<view/focusedscenevalue(____).md>) — 通过注入你提供的值来修改此视图，供状态依赖于焦点场景的其他视图使用。
- [focusedObject(_:)](<view/focusedobject(__).md>) — 创建一个新视图，将提供的对象暴露给状态依赖于焦点视图层级结构的其他视图。
- [focusedSceneObject(_:)](<view/focusedsceneobject(__).md>) — 创建一个新视图，将提供的对象暴露给状态依赖于活跃场景的其他视图。
- [prefersDefaultFocus(_:in:)](<view/prefersdefaultfocus(__in_).md>) — 指示对于给定的命名空间，该视图应默认获得焦点。
- [focusScope(_:)](<view/focusscope(__).md>) — 创建一个焦点作用域，SwiftUI 用它来限制默认焦点偏好。
- [focusSection()](<view/focussection().md>) — 指示应使用视图的框架及其可聚焦子视图群组来引导焦点移动。
- [focusable(_:)](<view/focusable(__).md>) — 指定视图是否可聚焦。
- [focusable(_:interactions:)](<view/focusable(__interactions_).md>) — 指定视图是否可聚焦，如果可以，它支持哪些焦点驱动的交互。
- [focusEffectDisabled(_:)](<view/focuseffectdisabled(__).md>) — 添加一个条件，控制此视图是否可以显示焦点效果，例如默认的焦点环或悬停效果。
- [defaultFocus(_:_:priority:)](<view/defaultfocus(____priority_).md>) — 通过为给定的焦点状态绑定赋值，定义窗口中评估默认焦点的区域。
- [searchFocused(_:)](<view/searchfocused(__).md>) — 通过将与最近的 searchable 修饰符关联的搜索栏的焦点状态绑定到给定的布尔值来修改此视图。
- [searchFocused(_:equals:)](<view/searchfocused(__equals_).md>) — 通过将与最近的 searchable 修饰符关联的搜索栏的焦点状态绑定到给定的值来修改此视图。

### 拷贝与粘贴

- [copyable(_:)](<view/copyable(__).md>) — 指定要拷贝的项目列表，以响应系统的「拷贝」命令。
- [cuttable(for:action:)](<view/cuttable(for_action_).md>) — 指定一个操作，响应系统的「剪切」命令将项目移动到剪贴板。
- [pasteDestination(for:action:validator:)](<view/pastedestination(for_action_validator_).md>) — 指定一个操作，响应系统的「粘贴」命令将验证过的项目添加到视图中。
- [onCopyCommand(perform:)](<view/oncopycommand(perform_).md>) — 添加一个操作，响应系统的「拷贝」命令而执行。
- [onCutCommand(perform:)](<view/oncutcommand(perform_).md>) — 添加一个操作，响应系统的「剪切」命令而执行。
- [onPasteCommand(of:perform:)](<view/onpastecommand(of_perform_).md>) — 添加一个操作，响应系统的「粘贴」命令而执行。
- [onPasteCommand(of:validator:perform:)](<view/onpastecommand(of_validator_perform_).md>) — 添加一个操作，响应系统的「粘贴」命令并使用你验证过的项目而执行。

### 拖放

- [dragConfiguration(_:)](<view/dragconfiguration(__).md>) — 配置一个拖放会话。
- [dragContainer(for:in:_:)](<view/dragcontainer(for_in___).md>) — 一个包含可拖动视图的容器，其拖放负载基于被拖动项的多个标识符。
- [dragContainer(for:itemID:in:_:)](<view/dragcontainer(for_itemid_in___).md>) — 一个包含可拖动视图的容器。
- [dragContainerSelection(_:containerNamespace:)](<view/dragcontainerselection(__containernamespace_).md>) — 为拖放容器提供多项目选择支持。
- [dragPreviewsFormation(_:)](<view/dragpreviewsformation(__).md>) — 描述被拖动预览在视觉上的组合方式。
- [draggable(_:)](<view/draggable(__).md>) — 将此视图激活为拖放操作的源。
- [draggable(_:preview:)](<view/draggable(__preview_).md>) — 将此视图激活为拖放操作的源。
- [draggable(_:containerNamespace:_:)](<view/draggable(__containernamespace___).md>) — 将此视图激活为拖放操作的源，允许提供可选的可标识负载，并指定此视图所属拖放容器的命名空间。
- [draggable(_:id:containerNamespace:_:)](<view/draggable(__id_containernamespace___).md>) — 将此视图激活为拖放操作的源，允许提供可选负载，并指定此视图所属拖放容器的命名空间。
- [draggable(_:id:item:containerNamespace:)](<view/draggable(__id_item_containernamespace_).md>) — 将此视图激活为拖放操作的源，允许提供可选负载，并指定此视图所属拖放容器的命名空间。
- [draggable(_:item:containerNamespace:)](<view/draggable(__item_containernamespace_).md>) — 将此视图激活为拖放操作的源，允许提供可选的可标识负载，并指定此视图所属拖放容器的命名空间。
- [draggable(containerItemID:containerNamespace:)](<view/draggable(containeritemid_containernamespace_).md>) — 在拖放容器内，将此视图激活为拖放操作的源。支持惰性拖放容器。
- [dropConfiguration(_:)](<view/dropconfiguration(__).md>) — 配置一个放置会话。
- [dropDestination(for:isEnabled:action:)](<view/dropdestination(for_isenabled_action_).md>) — 定义拖放操作的目的地，提供放置操作建议，并用你指定的闭包处理放入的内容。
- [dropPreviewsFormation(_:)](<view/droppreviewsformation(__).md>) — 描述放置预览的组合方式。
- [itemProvider(_:)](<view/itemprovider(__).md>) — 提供一个闭包，为特定数据元素提供要使用的拖放表示。
- [onDrag(_:preview:)](<view/ondrag(__preview_).md>) — 将此视图激活为拖放操作的源。
- [onDrag(_:)](<view/ondrag(__).md>) — 将此视图激活为拖放操作的源。
- [onDragSessionUpdated(_:)](<view/ondragsessionupdated(__).md>) — 指定一个操作，在由 `draggable(_:)` 或其他拖放修饰符激活的进行中拖放操作的每次更新时执行。
- [onDrop(of:isTargeted:perform:)](<view/ondrop(of_istargeted_perform_).md>) — 定义拖放操作的目的地，用你指定的闭包处理放入的内容。
- [onDrop(of:delegate:)](<view/ondrop(of_delegate_).md>) — 使用由你提供的委托控制的行为来定义拖放操作的目的地。
- [onDropSessionUpdated(_:)](<view/ondropsessionupdated(__).md>) — 指定一个操作，在由 `dropDestination(_:)` 或其他放置修饰符激活的进行中放置操作的每次更新时执行。
- [springLoadingBehavior(_:)](<view/springloadingbehavior(__).md>) — 设置此视图的弹簧加载（spring loading）行为。

### 重新排序

- [reorderContainer(for:isEnabled:move:)](<view/reordercontainer(for_isenabled_move_).md>) — 定义一个由可重新排序视图组成的容器。_(beta)_
- [reorderContainer(for:in:isEnabled:move:)](<view/reordercontainer(for_in_isenabled_move_).md>) — 定义一个由可重新排序视图组成的容器，使用你指定的类型来标识分区。_(beta)_
- [reorderContainer(for:itemID:isEnabled:move:)](<view/reordercontainer(for_itemid_isenabled_move_).md>) — 定义一个由可重新排序视图组成的容器，使用你指定的类型和键路径来标识项目。_(beta)_
- [reorderContainer(for:itemID:in:isEnabled:move:)](<view/reordercontainer(for_itemid_in_isenabled_move_).md>) — 定义一个由可重新排序视图组成的容器，使用你指定的类型和键路径来标识项目，并使用一个类型来标识集合。_(beta)_

### 提交

- [onAssignedDocumentDidSubmit(_:)](<view/onassigneddocumentdidsubmit(__).md>) — 添加一个操作，在提交指定文稿之后执行。
- [onAssignedDocumentDidWithdraw(_:)](<view/onassigneddocumentdidwithdraw(__).md>) — 添加一个操作，在指定文稿的提交被撤回之后执行。
- [onAssignedDocumentWillSubmit(_:)](<view/onassigneddocumentwillsubmit(__).md>) — 添加一个操作，在提交指定文稿之前执行。
- [onAssignedDocumentWillWithdraw(_:)](<view/onassigneddocumentwillwithdraw(__).md>) — 添加一个操作，在撤回指定文稿的提交之前执行。
- [onSubmit(of:_:)](<view/onsubmit(of___).md>) — 添加一个操作，在用户向此视图提交值时执行。
- [submitScope(_:)](<view/submitscope(__).md>) — 阻止源自此视图的提交触发器去调用视图层级结构中更高处的提交修饰符所配置的提交操作。
- [submitLabel(_:)](<view/submitlabel(__).md>) — 设置此视图的提交标签。

### 移动

- [onMoveCommand(perform:)](<view/onmovecommand(perform_).md>) — 添加一个操作，响应移动命令而执行，例如用户在 Mac 键盘上按下箭头键，或者在控制 Apple TV 时轻点 Siri Remote 的边缘。
- [moveDisabled(_:)](<view/movedisabled(__).md>) — 添加一个条件，控制视图的视图层级结构是否可移动。

### 删除

- [onDeleteCommand(perform:)](<view/ondeletecommand(perform_).md>) — 添加一个操作，响应系统的「删除」命令而执行，或者在此视图获得焦点时按下 ⌫（删除）或 ⌦（向前删除）键时执行。
- [deleteDisabled(_:)](<view/deletedisabled(__).md>) — 添加一个条件，控制视图的视图层级结构是否可删除。

### 命令

- [pageCommand(value:in:step:)](<view/pagecommand(value_in_step_).md>) — 响应向上翻页或向下翻页命令，让值在一个范围内按步进移动。
- [onExitCommand(perform:)](<view/onexitcommand(perform_).md>) — 设置一个操作，在此视图获得焦点时响应收到退出命令而触发。
- [onPlayPauseCommand(perform:)](<view/onplaypausecommand(perform_).md>) — 添加一个操作，响应系统的「播放/暂停」命令而执行。
- [onCommand(_:perform:)](<view/oncommand(__perform_).md>) — 添加一个操作，响应给定的选择器而执行。

### 数码旋钮

- [digitalCrownAccessory(_:)](<view/digitalcrownaccessory(__).md>) — 指定 Apple Watch 上数码旋钮附件视图的可见性。
- [digitalCrownAccessory(content:)](<view/digitalcrownaccessory(content_).md>) — 在 Apple Watch 上将一个附件视图放到数码旋钮旁边。
- [digitalCrownRotation(_:from:through:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](<view/digitalcrownrotation(__from_through_sensitivity_iscontinuous_ishapticfeedbackenabled_onchange_onidle_).md>) — 通过更新指定的绑定来跟踪数码旋钮的旋转。
- [digitalCrownRotation(_:onChange:onIdle:)](<view/digitalcrownrotation(__onchange_onidle_).md>) — 通过更新指定的绑定来跟踪数码旋钮的旋转。
- [digitalCrownRotation(detent:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:onChange:onIdle:)](<view/digitalcrownrotation(detent_from_through_by_sensitivity_iscontinuous_ishapticfeedbackenabled_onchange_onidle_).md>) — 通过更新指定的绑定来跟踪数码旋钮的旋转。
- [digitalCrownRotation(_:)](<view/digitalcrownrotation(__).md>) — 通过更新指定的绑定来跟踪数码旋钮的旋转。
- [digitalCrownRotation(_:from:through:by:sensitivity:isContinuous:isHapticFeedbackEnabled:)](<view/digitalcrownrotation(__from_through_by_sensitivity_iscontinuous_ishapticfeedbackenabled_).md>) — 通过更新指定的绑定来跟踪数码旋钮的旋转。

### 游戏控制器

- [handlesGameControllerEvents(matching:)](<view/handlesgamecontrollerevents(matching_).md>) — 指定当此视图或其某个子视图获得焦点时，应通过 GameController 框架递送的游戏控制器事件。
- [handlesGameControllerEvents(matching:withOptions:)](<view/handlesgamecontrollerevents(matching_withoptions_).md>) — 指定当此视图或其某个子视图获得焦点时，应通过 GameController 框架递送的游戏控制器事件。

### 沉浸式空间

- [onImmersionChange(initial:_:)](<view/onimmersionchange(initial___).md>) — 在你 App 的沉浸状态变化时执行一个操作。
- [onWorldRecenter(action:)](<view/onworldrecenter(action_).md>) — 添加一个操作，在使用数码旋钮重新居中视图时执行。
- [immersiveEnvironmentPicker(content:)](<view/immersiveenvironmentpicker(content_).md>) — 添加菜单项，以便从媒体播放器的环境选择器中打开沉浸式空间。

### Volumes

- [onVolumeViewpointChange(updateStrategy:initial:_:)](<view/onvolumeviewpointchange(updatestrategy_initial___).md>) — 添加一个操作，在 volume 的视点变化时执行。
- [supportedVolumeViewpoints(_:)](<view/supportedvolumeviewpoints(__).md>) — 指定 volume 中窗口栏和挂饰支持哪些视点。

### 用户活动

- [userActivity(_:element:_:)](<view/useractivity(__element___).md>) — 发布一种用户活动类型。
- [userActivity(_:isActive:_:)](<view/useractivity(__isactive___).md>) — 发布一种用户活动类型。
- [onContinueUserActivity(_:perform:)](<view/oncontinueuseractivity(__perform_).md>) — 注册一个处理程序，以响应你 App 收到的用户活动。
- [handlesExternalEvents(preferring:allowing:)](<view/handlesexternalevents(preferring_allowing_).md>) — 指定当场景已打开时该视图的场景要处理的外部事件。

### 视图生命周期

- [onAppear(perform:)](<view/onappear(perform_).md>) — 添加一个操作，在此视图出现之前执行。
- [onDisappear(perform:)](<view/ondisappear(perform_).md>) — 添加一个操作，在此视图消失之后执行。
- [onChange(of:initial:_:)](<view/onchange(of_initial___).md>) — 为此视图添加一个修饰符，在特定值变化时触发一个操作。
- [task(id:name:executorPreference:priority:file:line:_:)](<view/task(id_name_executorpreference_priority_file_line___).md>) — 添加一个任务，在此视图出现之前或指定值变化时执行。
- [task(id:name:priority:file:line:_:)](<view/task(id_name_priority_file_line___).md>) — 添加一个任务，在此视图出现之前或指定值变化时执行。
- [task(name:executorPreference:priority:file:line:action:)](<view/task(name_executorpreference_priority_file_line_action_).md>) — 添加一个异步任务，在此视图出现之前执行。
- [task(name:priority:file:line:_:)](<view/task(name_priority_file_line___).md>) — 添加一个异步任务，在此视图出现之前执行。

### 文件重命名

- [renameAction(_:)](<view/renameaction(__).md>) — 设置要为重命名操作运行的闭包。

### URLs

- [onOpenURL(perform:)](<view/onopenurl(perform_).md>) — 注册一个处理程序，以响应你 App 收到的 URL。
- [onOpenURL(prefersInApp:)](<view/onopenurl(prefersinapp_).md>) — 设置一个 `OpenURLAction`，偏好使用 App 内浏览器打开 URL。`handler` 闭包接受一个 URL 作为输入，并返回一个指示操作结果的 `OpenURLAction.Result`。
- [widgetURL(_:)](<view/widgeturl(__).md>) — 设置用户点击小组件时要在所属 App 中打开的 URL。

### 异步图像加载

- [asyncImageURLSession(_:)](<view/asyncimageurlsession(__).md>) — 一个修饰符，为视图中包含的异步图像添加一个 URL 会话，供其获取图像数据时使用。_(beta)_

### 发布者事件

- [onReceive(_:perform:)](<view/onreceive(__perform_).md>) — 添加一个操作，在此视图检测到给定发布者发出的数据时执行。

### 命中测试

- [allowsHitTesting(_:)](<view/allowshittesting(__).md>) — 配置此视图是否参与命中测试操作。

### 内容形状

- [contentShape(_:eoFill:)](<view/contentshape(__eofill_).md>) — 定义用于命中测试的内容形状。
- [contentShape(_:_:eoFill:)](<view/contentshape(____eofill_).md>) — 设置此视图的内容形状。

### 导入与导出

- [exportsItemProviders(_:onExport:)](<view/exportsitemproviders(__onexport_).md>) — 导出一个只读条目提供器，供快捷指令、快速操作和服务使用。
- [exportsItemProviders(_:onExport:onEdit:)](<view/exportsitemproviders(__onexport_onedit_).md>) — 导出一个可读写条目提供器，供快捷指令、快速操作和服务使用。
- [importsItemProviders(_:onImport:)](<view/importsitemproviders(__onimport_).md>) — 允许从服务导入条目提供器，例如 macOS 上的连续互通相机。
- [exportableToServices(_:)](<view/exportabletoservices(__).md>) — 导出项目，供快捷指令、快速操作和服务使用。
- [exportableToServices(_:onEdit:)](<view/exportabletoservices(__onedit_).md>) — 导出可读写项目，供快捷指令、快速操作和服务使用。
- [importableFromServices(for:action:)](<view/importablefromservices(for_action_).md>) — 允许从服务导入项目，例如 macOS 上的连续互通相机。

### App Intents

- [appEntityIdentifier(_:)](<view/appentityidentifier(__).md>) — 将 SwiftUI 视图与 App 实体关联，使其内容可被 Apple Intelligence 和 Siri 发现。
- [appEntityIdentifier(forSelectionType:identifier:)](<view/appentityidentifier(forselectiontype_identifier_).md>) — 将 SwiftUI 列表视图中的项目与 App 实体关联，使其可被 Apple Intelligence 和 Siri 发现。
- [appEntityUIElements(_:)](<view/appentityuielements(__).md>) — 向系统提供额外上下文，使自定视图的内容可被 Apple Intelligence 和 Siri 发现。
- [onAppIntentExecution(_:perform:)](<view/onappintentexecution(__perform_).md>) — 注册一个处理程序，以响应你 App 收到的指定 App 意图。
- [shortcutsLinkStyle(_:)](<view/shortcutslinkstyle(__).md>) — 为视图层级结构中的 ShortcutsLink 设置给定样式
- [siriTipViewStyle(_:)](<view/siritipviewstyle(__).md>) — 为视图层级结构中的 SiriTipView 设置给定样式

### 相机

- [onCameraCaptureEvent(isEnabled:action:)](<view/oncameracaptureevent(isenabled_action_).md>) — 用于注册由系统捕捉事件触发的操作。
- [onCameraCaptureEvent(isEnabled:defaultSoundDisabled:action:)](<view/oncameracaptureevent(isenabled_defaultsounddisabled_action_).md>) — 用于注册由系统捕捉事件触发的操作。
- [onCameraCaptureEvent(isEnabled:defaultSoundDisabled:primaryAction:secondaryAction:)](<view/oncameracaptureevent(isenabled_defaultsounddisabled_primaryaction_secondaryaction_).md>) — 用于注册由系统捕捉事件触发的操作。
- [onCameraCaptureEvent(isEnabled:primaryAction:secondaryAction:)](<view/oncameracaptureevent(isenabled_primaryaction_secondaryaction_).md>) — 用于注册由系统捕捉事件触发的操作。
- [cameraAnchor(isActive:)](<view/cameraanchor(isactive_).md>) — 指定应充当 Apple Vision Pro 2D Persona 流虚拟相机的视图。

## 另请参阅

### 提供交互性

- [Search modifiers](view-search.md) — 让人们能够在你的 App 中搜索内容。
- [Presentation modifiers](view-presentation.md) — 为视图定义额外要在指定条件下呈现的视图。
- [State modifiers](view-state.md) — 访问存储，并为子视图提供配置数据。
