---
title: UIViewController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller.json'
content_hash: 'sha256:6ef2a84d279b1fa0'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md)

# UIViewController

<sub>类</sub>

管理 UIKit App 中视图层级结构（view hierarchy）的对象。

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIViewController
```

## 概述

[UIViewController](uiviewcontroller.md) 类定义了所有视图控制器（view controller）共有的行为。你很少直接创建 [UIViewController](uiviewcontroller.md) 类的实例。相反，你会派生出 [UIViewController](uiviewcontroller.md) 的子类，并添加管理视图控制器视图层级结构所需的方法和属性。

视图控制器的主要职责包括：

- 更新视图的内容，通常是对底层数据的变更做出响应
- 响应用户与视图的交互
- 调整视图大小并管理整体界面的布局
- 与 App 中的其他对象（包括其他视图控制器）进行协调

视图控制器与其管理的视图紧密绑定，并参与处理其视图层级结构中的事件。具体来说，视图控制器是 [UIResponder](uiresponder.md) 对象，被插入到其根视图与该视图的父视图（通常属于另一个视图控制器）之间的响应者链（responder chain）中。如果视图控制器的任何视图都未处理某个事件，视图控制器可以选择处理该事件，或将其传递给父视图。

视图控制器很少孤立使用。相反，你通常会使用多个视图控制器，每个视图控制器拥有 App 用户界面的一部分。例如，一个视图控制器可能显示项目表格，而另一个视图控制器显示该表格中的选中项目。通常，一次只显示一个视图控制器的视图。一个视图控制器可以呈现另一个视图控制器以显示一组新视图，或者充当其他视图控制器内容的容器，并按需对视图进行动画处理。

### 子类化说明

每个 App 都至少包含一个 [UIViewController](uiviewcontroller.md) 的自定义子类。更常见的是，App 包含许多自定义视图控制器。自定义视图控制器定义了 App 的整体行为，包括 App 的外观及其对用户交互的响应方式。以下部分简要概述了你的自定义子类需要执行的某些任务。有关使用和实现视图控制器的详细信息，请参阅《[iOS 视图控制器编程指南](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457)》。

#### 管理视图

每个视图控制器管理一个视图层级结构，其根视图存储在此类的 [view](uiviewcontroller/view.md) 属性中。根视图主要充当视图层级结构其余部分的容器。根视图的大小和位置由其拥有者（父视图控制器或 App 的窗口）确定。由窗口拥有的视图控制器是 App 的根视图控制器，其视图大小将填满窗口。

视图控制器会延迟加载其视图。首次访问 [view](uiviewcontroller/view.md) 属性会加载或创建视图控制器的视图。有多种方式可以为视图控制器指定视图：

- 在 App 的 Storyboard 中指定视图控制器及其视图。Storyboard 是首选方式。使用 Storyboard，你可以指定视图及其与视图控制器的连接。你还可以指定视图控制器之间的关系和 Segue，从而更容易查看和修改 App 的行为。

要从 Storyboard 加载视图控制器，请调用相应 [UIStoryboard](uistoryboard.md) 对象的 [instantiateViewControllerWithIdentifier:](<uistoryboard/instantiateviewcontroller(withidentifier_).md>) 方法。Storyboard 对象会创建视图控制器并将其返回给你的代码。

- 使用 nib 文件为视图控制器指定视图。nib 文件允许你指定单个视图控制器的视图，但无法定义视图控制器之间的 Segue 或关系。nib 文件也只存储关于视图控制器本身的最少信息。

要使用 nib 文件初始化视图控制器对象，请以编程方式创建你的视图控制器类，并使用 [initWithNibName:bundle:](<uiviewcontroller/init(nibname_bundle_).md>) 方法进行初始化。当请求其视图时，视图控制器会从 nib 文件加载它们。

- 使用 [loadView](<uiviewcontroller/loadview().md>) 方法为视图控制器指定视图。在该方法中，以编程方式创建你的视图层级结构，并将该层级结构的根视图分配给视图控制器的 [view](uiviewcontroller/view.md) 属性。

所有这些技术都会产生相同的最终结果，即创建适当的视图集并通过 [view](uiviewcontroller/view.md) 属性公开它们。

> [!important] 重要
> 视图控制器是其视图及其创建的任何子视图的唯一拥有者。它负责创建这些视图，并在适当的时候（例如视图控制器本身被释放时）放弃对这些视图的所有权。如果你使用 Storyboard 或 nib 文件来存储视图对象，则每个视图控制器对象在请求这些视图时会自动获得其自己的副本。但是，如果你手动创建视图，则每个视图控制器必须拥有自己独特的视图集。你不能在视图控制器之间共享视图。

视图控制器的根视图的大小始终会调整为适合其分配的空间。对于视图层级结构中的其他视图，请使用 Interface Builder 指定控制每个视图在其父视图边界内定位和大小的 Auto Layout 约束。你也可以以编程方式创建约束并在适当的时候将其添加到视图中。有关如何创建约束的更多信息，请参阅《[Auto Layout 指南](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html#//apple_ref/doc/uid/TP40010853)》。

##### 处理与视图相关的通知

当其视图的可见性发生变化时，视图控制器会自动调用其自身的方法，以便子类可以响应此变化。使用诸如 [viewIsAppearing:](<uiviewcontroller/viewisappearing(__).md>) 之类的方法来准备视图以在屏幕上显示，并使用 [viewWillDisappear:](<uiviewcontroller/viewwilldisappear(__).md>) 来保存更改或其他状态信息。使用其他方法进行适当的更改。

下图显示了视图控制器视图的可能可见状态以及可能发生的状态转换。并非每个 `will` 回调方法都只对应一个 `did` 回调方法。你需要确保，如果你在 `will` 回调方法中启动了某个过程，则需要同时在相应的 `did` 和相反的 `will` 回调方法中结束该过程。

![](../../../attachments/a941e6911051bdb9476e5c7b33a7eea2/media-1965800@2x.png)

<sub>一个由四个球体排列成圆形的示意图。右侧的球体标记为“正在出现”，并有一个顺时针箭头指向底部的球体，该球体标记为“已出现”。箭头上的一个小点标记为 viewDidAppear。一个顺时针箭头从底部球体指向左侧球体，该球体标记为“正在消失”。箭头上的一个小点标记为 viewWillDisappear。一个顺时针箭头从左侧球体指向顶部球体，该球体标记为“已消失”。箭头上的两个小点标记为 viewDidDisappear 和 View removed。一个顺时针箭头从顶部球体指向右侧球体。箭头上的三个小点标记为 viewWillAppear、View added 和 viewIsAppearing。</sub>

##### 处理视图旋转

从 iOS 8 开始，所有与旋转相关的方法均已废弃。相反，旋转被视为视图控制器视图大小的变化，因此通过 [viewWillTransitionToSize:withTransitionCoordinator:](<uicontentcontainer/viewwilltransition(to_with_).md>) 方法进行报告。当界面方向改变时，UIKit 会在窗口的根视图控制器上调用此方法。然后该视图控制器通知其子视图控制器，在整个视图控制器层级结构中传播该消息。

在 iOS 6 和 iOS 7 中，你的 App 支持在 App 的 `Info.plist` 文件中定义的界面方向。视图控制器可以重写 [supportedInterfaceOrientations](uiviewcontroller/supportedinterfaceorientations.md) 方法来限制支持的方向列表。通常，系统仅对窗口的根视图控制器或呈现以填充整个屏幕的视图控制器调用此方法；子视图控制器使用其父视图控制器为它们提供的窗口部分，不再直接参与决定支持哪些旋转。App 的方向掩码与视图控制器的方向掩码的交集用于确定视图控制器可以旋转到哪些方向。

对于打算以特定方向全屏呈现的视图控制器，你可以重写 [preferredInterfaceOrientationForPresentation](uiviewcontroller/preferredinterfaceorientationforpresentation.md) 方法。

当可见视图控制器发生旋转时，在旋转期间会调用 [willRotateToInterfaceOrientation:duration:](<uiviewcontroller/willrotate(to_duration_).md>)、[willAnimateRotationToInterfaceOrientation:duration:](<uiviewcontroller/willanimaterotation(to_duration_).md>) 和 [didRotateFromInterfaceOrientation:](<uiviewcontroller/didrotate(from_).md>) 方法。在视图由其父视图调整大小和定位后，也会调用 [viewWillLayoutSubviews](<uiviewcontroller/viewwilllayoutsubviews().md>) 方法。如果在方向更改时视图控制器不可见，则永远不会调用旋转方法。但是，当视图变为可见时，会调用 [viewWillLayoutSubviews](<uiviewcontroller/viewwilllayoutsubviews().md>) 方法。

> [!note] 注意
> 在启动时，App 应始终以竖屏方向设置其界面。在 [application:didFinishLaunchingWithOptions:](<uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>) 方法返回后，App 会使用上述视图控制器旋转机制，在显示窗口之前将视图旋转到适当的方向。

#### 实现容器视图控制器

自定义的 [UIViewController](uiviewcontroller.md) 子类也可以充当容器视图控制器（container view controller）。容器视图控制器管理其拥有的其他视图控制器（也称为其子视图控制器）内容的呈现。子视图的视图可以原样呈现，或与容器视图控制器拥有的视图一起呈现。

你的容器视图控制器子类应声明一个公共接口来关联其子视图控制器。这些方法的性质取决于你，并取决于你正在创建的容器的语义。你需要决定你的视图控制器一次可以显示多少个子视图控制器、何时显示这些子视图控制器，以及它们在视图控制器的视图层级结构中的位置。你的视图控制器类定义了子视图控制器之间共享哪些关系（如果有）。通过为容器建立清晰的公共接口，你可以确保子视图控制器逻辑地使用其功能，而无需访问容器实现行为方式的太多私有细节。

你的容器视图控制器必须在将子视图控制器的根视图添加到视图层级结构之前将其与自身关联。这允许 iOS 正确地将事件路由到子视图控制器及其管理的视图。同样，在从其视图层级结构中移除子视图控制器的根视图后，它应该将该子视图控制器与自身断开连接。要建立或断开这些关联，容器会调用基类定义的特定方法。这些方法不打算由容器类的客户端调用；它们仅用于容器的实现以提供预期的包含行为。

以下是可能需要调用的基本方法：

- [addChildViewController:](<uiviewcontroller/addchild(__).md>)
- [removeFromParentViewController](<uiviewcontroller/removefromparent().md>)
- [willMoveToParentViewController:](<uiviewcontroller/willmove(toparent_).md>)
- [didMoveToParentViewController:](<uiviewcontroller/didmove(toparent_).md>)

> [!note] 注意
> 创建容器视图控制器时，不需要重写任何方法。
>
> 默认情况下，旋转和外观回调会自动转发给子视图控制器。你也可以选择重写 [shouldAutomaticallyForwardRotationMethods](<uiviewcontroller/shouldautomaticallyforwardrotationmethods().md>) 和 [shouldAutomaticallyForwardAppearanceMethods](uiviewcontroller/shouldautomaticallyforwardappearancemethods.md) 方法来自己控制此行为。

#### 管理内存

内存是 iOS 中的关键资源，视图控制器提供了内置支持来在关键时刻减少其内存占用空间。[UIViewController](uiviewcontroller.md) 类通过其 [didReceiveMemoryWarning](<uiviewcontroller/didreceivememorywarning().md>) 方法提供了对低内存状况的一些自动处理，该方法会释放不需要的内存。

#### 支持状态保存与恢复

如果你为视图控制器的 [restorationIdentifier](uiviewcontroller/restorationidentifier.md) 属性分配了一个值，则当 App 转换到后台时，系统可能会要求视图控制器对自身进行编码。当被保存时，视图控制器会保存其视图层级结构中任何也具有恢复标识符的视图的状态。视图控制器不会自动保存任何其他状态。如果你正在实现自定义容器视图控制器，则必须自行对任何子视图控制器进行编码。你编码的每个子视图控制器都必须具有唯一的恢复标识符。

有关系统如何确定要保存和恢复哪些视图控制器的更多信息，请参阅《[iOS App 编程指南](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)》。要查看状态保存与恢复的示例，请参阅[恢复 App 的状态](restoring-your-app-s-state.md)。

## 关系

- **继承自**：[UIResponder](uiresponder.md)

- **被继承于**：[UIActivityViewController](uiactivityviewcontroller.md)、[UIAlertController](uialertcontroller.md)、[UICloudSharingController](uicloudsharingcontroller.md)、[UICollectionViewController](uicollectionviewcontroller.md)、[UIColorPickerViewController](uicolorpickerviewcontroller.md)、[UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md)、[UIDocumentMenuViewController](uidocumentmenuviewcontroller.md)、[UIDocumentPickerExtensionViewController](uidocumentpickerextensionviewcontroller.md)、[UIDocumentPickerViewController](uidocumentpickerviewcontroller.md)、[UIDocumentViewController](uidocumentviewcontroller.md)、[UIFontPickerViewController](uifontpickerviewcontroller.md)、[UIInputViewController](uiinputviewcontroller.md)、[UINavigationController](uinavigationcontroller.md)、[UIPageViewController](uipageviewcontroller.md)、[UIReferenceLibraryViewController](uireferencelibraryviewcontroller.md)、[UISearchContainerViewController](uisearchcontainerviewcontroller.md)、[UISearchController](uisearchcontroller.md)、[UISplitViewController](uisplitviewcontroller.md)、[UITabBarController](uitabbarcontroller.md)、[UITableViewController](uitableviewcontroller.md)、[UITextFormattingViewController](uitextformattingviewcontroller.md)

- **遵循**：[CVarArg](../swift/cvararg.md)、[Copyable](../swift/copyable.md)、[CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)、[CustomStringConvertible](../swift/customstringconvertible.md)、[Equatable](../swift/equatable.md)、[Escapable](../swift/escapable.md)、[Hashable](../swift/hashable.md)、[NSCoding](../foundation/nscoding.md)、[NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)、[NSObjectProtocol](../objectivec/nsobjectprotocol.md)、[NSTouchBarProvider](../appkit/nstouchbarprovider.md)、[Sendable](../swift/sendable.md)、[SendableMetatype](../swift/sendablemetatype.md)、[UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)、[UIAppearanceContainer](uiappearancecontainer.md)、[UIContentContainer](uicontentcontainer.md)、[UIFocusEnvironment](uifocusenvironment.md)、[UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)、[UIResponderStandardEditActions](uiresponderstandardeditactions.md)、[UIStateRestoring](uistaterestoring.md)、[UITraitChangeObservable](uitraitchangeobservable-67e94.md)、[UITraitEnvironment](uitraitenvironment.md)、[UIUserActivityRestoring](uiuseractivityrestoring.md)

## 主题

### 创建视图控制器

- [initWithNibName:bundle:](<uiviewcontroller/init(nibname_bundle_).md>) — 使用指定 bundle 中的 nib 文件创建视图控制器。
- [initWithCoder:](<uiviewcontroller/init(coder_).md>) — 使用解归档器中的数据创建视图控制器。

### 获取 Storyboard 和 nib 信息

- [storyboard](uiviewcontroller/storyboard.md) — 视图控制器来源的 Storyboard。
- [nibName](uiviewcontroller/nibname.md) — 视图控制器 nib 文件的名称（如果已指定）。
- [nibBundle](uiviewcontroller/nibbundle.md) — 视图控制器的 nib bundle（如果存在）。

### 管理视图

- [view](uiviewcontroller/view.md) — 控制器管理的视图。
- [viewIfLoaded](uiviewcontroller/viewifloaded.md) — 视图控制器的视图，如果视图尚未加载则为 `nil`。
- [viewLoaded](uiviewcontroller/isviewloaded.md) — 一个布尔值，指示视图当前是否已加载到内存中。
- [loadView](<uiviewcontroller/loadview().md>) — 创建控制器管理的视图。
- [viewDidLoad](<uiviewcontroller/viewdidload().md>) — 在控制器的视图加载到内存后调用。
- [loadViewIfNeeded](<uiviewcontroller/loadviewifneeded().md>) — 如果尚未加载视图控制器的视图，则加载它。
- [title](uiviewcontroller/title.md) — 代表此控制器管理的视图的本地化字符串。
- [preferredContentSize](uiviewcontroller/preferredcontentsize.md) — 视图控制器视图的首选大小。
- [ornaments](uiviewcontroller/ornaments.md) — 显示在视图控制器旁边的 SwiftUI 挂饰。

### 响应与视图相关的事件

- [viewWillAppear:](<uiviewcontroller/viewwillappear(__).md>) — 通知视图控制器其视图即将添加到视图层级结构。
- [viewIsAppearing:](<uiviewcontroller/viewisappearing(__).md>) — 通知视图控制器系统正在将其视图添加到视图层级结构。
- [viewDidAppear:](<uiviewcontroller/viewdidappear(__).md>) — 通知视图控制器其视图已添加到视图层级结构。
- [viewWillDisappear:](<uiviewcontroller/viewwilldisappear(__).md>) — 通知视图控制器其视图即将从视图层级结构中移除。
- [viewDidDisappear:](<uiviewcontroller/viewdiddisappear(__).md>) — 通知视图控制器其视图已从视图层级结构中移除。
- [beingDismissed](uiviewcontroller/isbeingdismissed.md) — 一个布尔值，指示视图控制器是否正被其某个祖先视图控制器解除。
- [beingPresented](uiviewcontroller/isbeingpresented.md) — 一个布尔值，指示视图控制器是否正被其某个祖先视图控制器呈现。
- [movingFromParentViewController](uiviewcontroller/ismovingfromparent.md) — 一个布尔值，指示视图控制器是否正在从父视图控制器移出。
- [movingToParentViewController](uiviewcontroller/ismovingtoparent.md) — 一个布尔值，指示视图控制器是否正在移入父视图控制器。

### 管理视图的属性

- [ViewLoading](uiviewcontroller/viewloading.md) — 一个属性包装器，在访问属性之前加载视图控制器的视图。
- [updateProperties](<uiviewcontroller/updateproperties().md>) — 配置视图控制器的内容和样式属性。
- [updatePropertiesIfNeeded](<uiviewcontroller/updatepropertiesifneeded().md>) — 强制对此视图控制器及其视图（包括此子树中的任何视图控制器和视图）立即进行属性更新。
- [setNeedsUpdateProperties](<uiviewcontroller/setneedsupdateproperties().md>) — 调用以手动请求视图控制器的属性更新。多个请求可能会合并为单次更新，与下一次布局传递同时进行。

### 扩展视图的安全区

- [将内容相对于安全区（safe area）定位](positioning-content-relative-to-the-safe-area.md) — 定位视图使其不被其他内容遮挡。
- [additionalSafeAreaInsets](uiviewcontroller/additionalsafeareainsets.md) — 你指定的自定义内边距，用于修改视图控制器的安全区。
- [viewSafeAreaInsetsDidChange](<uiviewcontroller/viewsafeareainsetsdidchange().md>) — 当根视图的安全区内边距发生变化时调用，以通知视图控制器。

### 管理视图的边距

- [在布局边距内定位内容](positioning-content-within-layout-margins.md) — 定位视图使其不被其他内容挤压。
- [viewRespectsSystemMinimumLayoutMargins](uiviewcontroller/viewrespectssystemminimumlayoutmargins.md) — 一个布尔值，指示视图控制器的视图是否使用系统定义的最小布局边距。
- [systemMinimumLayoutMargins](uiviewcontroller/systemminimumlayoutmargins.md) — 视图控制器根视图的最小布局边距。
- [viewLayoutMarginsDidChange](<uiviewcontroller/viewlayoutmarginsdidchange().md>) — 当根视图的布局边距发生变化时调用，以通知视图控制器。

### 配置视图的布局行为

- [edgesForExtendedLayout](uiviewcontroller/edgesforextendedlayout.md) — 你为视图控制器扩展的边缘。
- [UIRectEdge](uirectedge.md) — 指定矩形边缘的常量。
- [extendedLayoutIncludesOpaqueBars](uiviewcontroller/extendedlayoutincludesopaquebars.md) — 一个布尔值，指示扩展布局是否包含不透明栏。
- [viewWillLayoutSubviews](<uiviewcontroller/viewwilllayoutsubviews().md>) — 通知视图控制器其视图即将布局其子视图。
- [viewDidLayoutSubviews](<uiviewcontroller/viewdidlayoutsubviews().md>) — 当视图完成其子视图的布局时通知视图控制器。
- [updateViewConstraints](<uiviewcontroller/updateviewconstraints().md>) — 当视图需要更新其约束时通知视图控制器。

### 配置视图旋转设置

- [supportedInterfaceOrientations](uiviewcontroller/supportedinterfaceorientations.md) — 视图控制器支持的界面方向。
- [preferredInterfaceOrientationForPresentation](uiviewcontroller/preferredinterfaceorientationforpresentation.md) — 呈现视图控制器时使用的首选界面方向。
- [setNeedsUpdateOfSupportedInterfaceOrientations](<uiviewcontroller/setneedsupdateofsupportedinterfaceorientations().md>) — 通知视图控制器支持的界面方向或呈现的首选界面方向发生了变化。
- [prefersInterfaceOrientationLocked](uiviewcontroller/prefersinterfaceorientationlocked.md) — 一个布尔值，指示当场景可见时，视图控制器是否倾向于锁定场景的界面方向。
- [setNeedsUpdateOfPrefersInterfaceOrientationLocked](<uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked().md>) — 指示视图控制器更改了界面方向锁定偏好。
- [childViewControllerForInterfaceOrientationLock](uiviewcontroller/childforinterfaceorientationlock.md) — 用于查询界面方向锁定偏好的子视图控制器。

### 执行 Segue

- [shouldPerformSegueWithIdentifier:sender:](<uiviewcontroller/shouldperformsegue(withidentifier_sender_).md>) — 确定是否应执行具有指定标识符的 Segue。
- [prepareForSegue:sender:](<uiviewcontroller/prepare(for_sender_).md>) — 通知视图控制器即将执行 Segue。
- [performSegueWithIdentifier:sender:](<uiviewcontroller/performsegue(withidentifier_sender_).md>) — 从当前视图控制器的 Storyboard 文件中启动具有指定标识符的 Segue。
- [allowedChildViewControllersForUnwindingFromSource:](<uiviewcontroller/allowedchildrenforunwinding(from_).md>) — 返回要搜索 unwind Segue 目标的子视图控制器数组。
- [childViewControllerContainingSegueSource:](<uiviewcontroller/childcontaining(__).md>) — 返回包含 unwind Segue 来源的子视图控制器。
- [canPerformUnwindSegueAction:fromViewController:sender:](<uiviewcontroller/canperformunwindsegueaction(__from_sender_).md>) — 在视图控制器上调用，以确定它是否响应 unwind 操作。
- [unwindForSegue:towardsViewController:](<uiviewcontroller/unwind(for_towards_).md>) — 当 unwind Segue 过渡到新视图控制器时调用。

### 呈现视图控制器

- [showViewController:sender:](<uiviewcontroller/show(__sender_).md>) — 在主上下文中呈现视图控制器。
- [showDetailViewController:sender:](<uiviewcontroller/showdetailviewcontroller(__sender_).md>) — 在次要（或详细）上下文中呈现视图控制器。
- [ShowDetailTargetDidChangeMessage](uiviewcontroller/showdetailtargetdidchangemessage.md)
- [presentViewController:animated:completion:](<uiviewcontroller/present(__animated_completion_).md>) — 以模态方式呈现视图控制器。
- [dismissViewControllerAnimated:completion:](<uiviewcontroller/dismiss(animated_completion_).md>) — 解除由当前视图控制器以模态方式呈现的视图控制器。
- [modalPresentationStyle](uiviewcontroller/modalpresentationstyle.md) — 模态视图控制器的呈现样式。
- [UIModalPresentationStyle](uimodalpresentationstyle.md) — 呈现视图控制器时可用的模态呈现样式。
- [modalTransitionStyle](uiviewcontroller/modaltransitionstyle.md) — 呈现视图控制器时使用的过渡样式。
- [UIModalTransitionStyle](uimodaltransitionstyle.md) — 呈现视图控制器时可用的过渡样式。
- [modalInPresentation](uiviewcontroller/ismodalinpresentation.md) — 一个布尔值，指示视图控制器是否强制执行模态行为。
- [definesPresentationContext](uiviewcontroller/definespresentationcontext.md) — 一个布尔值，指示当此视图控制器或其某个子代呈现视图控制器时，此视图控制器的视图是否被覆盖。
- [providesPresentationContextTransitionStyle](uiviewcontroller/providespresentationcontexttransitionstyle.md) — 一个布尔值，指示视图控制器是否为其呈现的视图控制器指定过渡样式。
- [disablesAutomaticKeyboardDismissal](uiviewcontroller/disablesautomatickeyboarddismissal.md) — 返回一个布尔值，指示在更改控制时是否自动关闭当前输入视图。
- [UIViewControllerShowDetailTargetDidChangeNotification](uiviewcontroller/showdetailtargetdidchangenotification.md) — 当拆分视图控制器展开或折叠时发布。

### 添加自定义过渡或呈现

- [transitioningDelegate](uiviewcontroller/transitioningdelegate.md) — 提供过渡动画器、交互控制器和自定义呈现控制器对象的委托对象。
- [transitionCoordinator](uiviewcontroller/transitioncoordinator.md) — 返回活动的过渡协调器对象。
- [targetViewControllerForAction:sender:](<uiviewcontroller/targetviewcontroller(foraction_sender_).md>) — 返回响应该操作的视图控制器。
- [presentationController](uiviewcontroller/presentationcontroller.md) — 正在管理当前视图控制器的呈现控制器。
- [popoverPresentationController](uiviewcontroller/popoverpresentationcontroller.md) — 正在管理当前视图控制器的最近弹窗呈现控制器。
- [sheetPresentationController](uiviewcontroller/sheetpresentationcontroller.md) — 视图控制器的表单（sheet）呈现控制器。
- [activePresentationController](uiviewcontroller/activepresentationcontroller.md) — 正在管理视图控制器的呈现控制器。
- [restoresFocusAfterTransition](uiviewcontroller/restoresfocusaftertransition.md) — 一个布尔值，指示当项目的视图控制器变为可见且可聚焦时，先前聚焦的项目是否应再次获得焦点。
- [在 UIKit 中自定义和调整表单大小](customizing-and-resizing-sheets-in-uikit.md) — 了解如何在 UIKit 中创建分层和自定义的表单体验。

### 适应环境变化

- [collapseSecondaryViewController:forSplitViewController:](<uiviewcontroller/collapsesecondaryviewcontroller(__for_).md>) — 当拆分视图控制器过渡到紧凑宽度尺寸类别时调用。
- [separateSecondaryViewControllerForSplitViewController:](<uiviewcontroller/separatesecondaryviewcontroller(for_).md>) — 当拆分视图控制器过渡到常规宽度尺寸类别时调用。

### 调整界面样式

- [overrideUserInterfaceStyle](uiviewcontroller/overrideuserinterfacestyle.md) — 视图控制器及其所有子视图控制器采用的用户界面样式。
- [preferredUserInterfaceStyle](uiviewcontroller/preferreduserinterfacestyle.md) — 此视图控制器的首选界面样式。
- [childViewControllerForUserInterfaceStyle](uiviewcontroller/childviewcontrollerforuserinterfacestyle.md) — 支持首选用户界面样式的子视图控制器。
- [setNeedsUserInterfaceAppearanceUpdate](<uiviewcontroller/setneedsuserinterfaceappearanceupdate().md>) — 通知视图控制器发生了可能影响首选界面样式的更改。
- [UIUserInterfaceStyle](uiuserinterfacestyle.md) — 指示 App 界面样式的常量。

### 调整容器背景样式

- [preferredContainerBackgroundStyle](uiviewcontroller/preferredcontainerbackgroundstyle.md)
- [childViewControllerForPreferredContainerBackgroundStyle](uiviewcontroller/childviewcontrollerforpreferredcontainerbackgroundstyle.md)
- [setNeedsUpdateOfPreferredContainerBackgroundStyle](<uiviewcontroller/setneedsupdateofpreferredcontainerbackgroundstyle().md>)
- [UIContainerBackgroundStyle](uicontainerbackgroundstyle.md)

### 观察特征变化

- [UITraitChangeObservable](uitraitchangeobservable-67e94.md) — 一种类型，当特征环境发生变化时会调用你的代码。

### 重写特征值

- [traitOverrides](uiviewcontroller/traitoverrides-1z1cc.md) — 用于为此视图控制器及其视图设置特征更改的可变特征容器。
- [UITraitOverrides](uitraitoverrides-swift.struct.md) — 用于为对象及其子代设置特征更改的可变特征容器。
- [updateTraitsIfNeeded](<uiviewcontroller/updatetraitsifneeded().md>) — 立即为此视图控制器及其视图（包括此子树中的任何视图控制器和视图）更新特征。

### 在自定义容器中管理子视图控制器

- [childViewControllers](uiviewcontroller/children.md) — 当前视图控制器的子视图控制器数组。
- [addChildViewController:](<uiviewcontroller/addchild(__).md>) — 将指定的视图控制器添加为当前视图控制器的子视图控制器。
- [removeFromParentViewController](<uiviewcontroller/removefromparent().md>) — 将视图控制器从其父视图控制器中移除。
- [transitionFromViewController:toViewController:duration:options:animations:completion:](<uiviewcontroller/transition(from_to_duration_options_animations_completion_).md>) — 在视图控制器的两个子视图控制器之间进行过渡。
- [shouldAutomaticallyForwardAppearanceMethods](uiviewcontroller/shouldautomaticallyforwardappearancemethods.md) — 返回一个布尔值，指示外观方法是否转发给子视图控制器。
- [beginAppearanceTransition:animated:](<uiviewcontroller/beginappearancetransition(__animated_).md>) — 告知子控制器其外观即将改变。
- [endAppearanceTransition](<uiviewcontroller/endappearancetransition().md>) — 告知子控制器其外观已改变。
- [UIViewControllerHierarchyInconsistencyException](uiviewcontroller/hierarchyinconsistencyexception.md) — 如果视图控制器层级结构与视图层级结构不一致，则引发。

### 响应包含事件

- [willMoveToParentViewController:](<uiviewcontroller/willmove(toparent_).md>) — 在视图控制器被添加或移除出容器视图控制器之前调用。
- [didMoveToParentViewController:](<uiviewcontroller/didmove(toparent_).md>) — 在视图控制器被添加或移除出容器视图控制器之后调用。

### 获取其他相关视图控制器

- [presentingViewController](uiviewcontroller/presentingviewcontroller.md) — 呈现此视图控制器的视图控制器。
- [presentedViewController](uiviewcontroller/presentedviewcontroller.md) — 由此视图控制器或其视图控制器层级结构中的某个祖先呈现的视图控制器。
- [parentViewController](uiviewcontroller/parent.md) — 接收者的父视图控制器。
- [splitViewController](uiviewcontroller/splitviewcontroller.md) — 视图控制器层级结构中最近的拆分视图控制器祖先。
- [navigationController](uiviewcontroller/navigationcontroller.md) — 视图控制器层级结构中最近的导览控制器（navigation controller）祖先。
- [tabBarController](uiviewcontroller/tabbarcontroller.md) — 视图控制器层级结构中最近的标签页栏控制器祖先。

### 配置导览界面

- [navigationItem](uiviewcontroller/navigationitem.md) — 用于在父视图控制器的导航栏中表示视图控制器的导览项。
- [hidesBottomBarWhenPushed](uiviewcontroller/hidesbottombarwhenpushed.md) — 一个布尔值，指示当视图控制器被推入导览控制器时，屏幕底部的工具栏是否被隐藏。
- [setToolbarItems:animated:](<uiviewcontroller/settoolbaritems(__animated_).md>) — 设置与视图控制器一起显示的工具栏项目。
- [toolbarItems](uiviewcontroller/toolbaritems.md) — 与视图控制器关联的工具栏项目。

### 配置标签页栏内容

- [tab](uiviewcontroller/tab.md) — 用于创建接收者的 `UITab` 实例，并代表该视图控制器。默认为 nil。
- [tabBarItem](uiviewcontroller/tabbaritem.md) — 当视图控制器添加到标签页栏控制器时，代表该视图控制器的标签页栏项目。
- [tabBarObservedScrollView](uiviewcontroller/tabbarobservedscrollview.md) — 要与滚动的标签页栏同步的全屏滚动视图。 _(已废弃)_

### 使用滚动内容

- [setContentScrollView:forEdge:](<uiviewcontroller/setcontentscrollview(__for_).md>) — 为指定边缘设置栏所观察的滚动视图。
- [setContentScrollView(_:)](<uiviewcontroller/setcontentscrollview(__).md>) — 为视图的所有边缘设置栏所观察的滚动视图。
- [contentScrollViewForEdge:](<uiviewcontroller/contentscrollview(for_).md>) — 返回视图控制器为指定边缘观察的滚动视图。

### 指示内容不可用

- [contentUnavailableConfiguration](uiviewcontroller/contentunavailableconfiguration-4b95e.md) — 视图控制器的当前内容不可用配置。
- [contentUnavailableConfigurationState](uiviewcontroller/contentunavailableconfigurationstate-7sczw.md) — 内容不可用视图的当前配置状态。
- [setNeedsUpdateContentUnavailableConfiguration](<uiviewcontroller/setneedsupdatecontentunavailableconfiguration().md>) — 请求系统为最新状态更新内容不可用配置。
- [updateContentUnavailableConfiguration(using:)](<uiviewcontroller/updatecontentunavailableconfiguration(using_).md>) — 为提供的状态更新内容不可用配置。
- [UIContentUnavailableConfiguration](uicontentunavailableconfiguration-swift.struct.md) — 内容不可用视图的内容配置。

### 支持 App 扩展

- [extensionContext](uiviewcontroller/extensioncontext.md) — 返回视图控制器的扩展上下文。

### 协调系统手势

- [preferredScreenEdgesDeferringSystemGestures](uiviewcontroller/preferredscreenedgesdeferringsystemgestures.md) — 你希望自己的手势优先于系统手势的屏幕边缘。
- [childViewControllerForScreenEdgesDeferringSystemGestures](uiviewcontroller/childforscreenedgesdeferringsystemgestures.md) — 返回应被查询以确定其手势是否应优先的子视图控制器。
- [setNeedsUpdateOfScreenEdgesDeferringSystemGestures](<uiviewcontroller/setneedsupdateofscreenedgesdeferringsystemgestures().md>) — 通知系统推迟系统手势的屏幕边缘发生了变化。
- [prefersHomeIndicatorAutoHidden](uiviewcontroller/prefershomeindicatorautohidden.md) — 一个布尔值，指示是否允许系统隐藏用于返回主屏幕的视觉指示器。
- [childViewControllerForHomeIndicatorAutoHidden](uiviewcontroller/childforhomeindicatorautohidden.md) — 返回被咨询有关显示返回主屏幕视觉指示器偏好的子视图控制器。
- [setNeedsUpdateOfHomeIndicatorAutoHidden](<uiviewcontroller/setneedsupdateofhomeindicatorautohidden().md>) — 通知 UIKit 你的视图控制器已更新其关于返回主屏幕视觉指示器的偏好。

### 使用过渡

- [preferredTransition](uiviewcontroller/preferredtransition.md) — 定义切换到视图控制器时的过渡动画的对象。
- [Transition](uiviewcontroller/transition.md) — 定义切换到新视图控制器时的过渡动画的对象。

### 使用焦点

- [focusGroupIdentifier](uiviewcontroller/focusgroupidentifier.md) — 视图控制器所属焦点组的标识符。

### 管理指针锁定状态

- [prefersPointerLocked](uiviewcontroller/preferspointerlocked.md) — 一个布尔值，指示视图控制器是否倾向于将指针锁定到特定场景。
- [setNeedsUpdateOfPrefersPointerLocked](<uiviewcontroller/setneedsupdateofpreferspointerlocked().md>) — 指示视图控制器更改了指针锁定偏好。
- [childViewControllerForPointerLock](uiviewcontroller/childviewcontrollerforpointerlock.md) — 用于查询指针锁定偏好的子视图控制器。

### 管理状态栏

- [prefersStatusBarHidden](uiviewcontroller/prefersstatusbarhidden.md) — 指定视图控制器是倾向于隐藏还是显示状态栏。
- [childViewControllerForStatusBarHidden](uiviewcontroller/childforstatusbarhidden.md) — 用于确定状态栏隐藏状态的视图控制器。
- [childViewControllerForStatusBarStyle](uiviewcontroller/childforstatusbarstyle.md) — 当系统需要用于确定状态栏样式的视图控制器时调用。
- [preferredStatusBarStyle](uiviewcontroller/preferredstatusbarstyle.md) — 视图控制器的首选状态栏样式。
- [UIStatusBarStyle](uistatusbarstyle.md) — 描述设备状态栏样式的常量。
- [modalPresentationCapturesStatusBarAppearance](uiviewcontroller/modalpresentationcapturesstatusbarappearance.md) — 指定非全屏呈现的视图控制器是否接管呈现视图控制器的状态栏外观控制权。
- [preferredStatusBarUpdateAnimation](uiviewcontroller/preferredstatusbarupdateanimation.md) — 指定视图控制器用于隐藏和显示状态栏的动画样式。
- [setNeedsStatusBarAppearanceUpdate](<uiviewcontroller/setneedsstatusbarappearanceupdate().md>) — 向系统指示视图控制器的状态栏属性已更改。

### 管理 Touch Bar

- [childViewControllerForTouchBar](uiviewcontroller/childviewcontrollerfortouchbar.md) — 系统用于在 Touch Bar 中显示内容的子视图控制器。
- [setNeedsTouchBarUpdate](<uiviewcontroller/setneedstouchbarupdate().md>) — 告知系统更新 Touch Bar。

### 访问可用的快捷键命令

- [performsActionsWhilePresentingModally](uiviewcontroller/performsactionswhilepresentingmodally.md) — 一个布尔值，指示视图控制器是否执行与菜单相关的操作。
- [addKeyCommand:](<uiviewcontroller/addkeycommand(__).md>) — 将指定的键盘快捷键与视图控制器关联。
- [removeKeyCommand:](<uiviewcontroller/removekeycommand(__).md>) — 从视图控制器中移除快捷键命令。

### 向视图控制器添加编辑行为

- [editing](uiviewcontroller/isediting.md) — 一个布尔值，指示视图控制器当前是否允许用户编辑视图内容。
- [setEditing:animated:](<uiviewcontroller/setediting(__animated_).md>) — 设置视图控制器是否显示可编辑视图。
- [editButtonItem](uiviewcontroller/editbuttonitem.md) — 返回一个在“编辑”和“完成”之间切换其标题和关联状态的栏按钮项目。

### 处理内存警告

- [didReceiveMemoryWarning](<uiviewcontroller/didreceivememorywarning().md>) — 当 App 收到内存警告时发送给视图控制器。

### 管理状态恢复

- [恢复 App 的状态](restoring-your-app-s-state.md) — 通过保留当前活动为用户提供连续性。
- [restorationIdentifier](uiviewcontroller/restorationidentifier.md) — 确定视图控制器是否支持状态恢复的标识符。
- [restorationClass](uiviewcontroller/restorationclass.md) — 负责在恢复 App 状态时重新创建此视图控制器的类。
- [encodeRestorableStateWithCoder:](<uiviewcontroller/encoderestorablestate(with_).md>) — 为视图控制器编码与状态相关的信息。
- [decodeRestorableStateWithCoder:](<uiviewcontroller/decoderestorablestate(with_).md>) — 解码并恢复视图控制器与状态相关的信息。
- [applicationFinishedRestoringState](<uiviewcontroller/applicationfinishedrestoringstate().md>) — 在其他对象解码完成后，在已恢复的视图控制器上调用。

### 记录用户交互间隔

- [interactionActivityTrackingBaseName](uiviewcontroller/interactionactivitytrackingbasename.md) — 视图控制器用于记录注释用户交互的 Signpost 的基础名称。

### 注册场景配件

- [registerSceneAccessory:](<uiviewcontroller/registersceneaccessory(__).md>) — 注册与此视图控制器关联的新场景配件配置。 _(beta)_
- [unregisterSceneAccessory:](<uiviewcontroller/unregistersceneaccessory(__).md>) — 使用指定的注册标识符注销场景配件。 _(beta)_

### 已废弃

- [已废弃的符号](uiviewcontroller-deprecated-symbols.md) — 视图控制器不再支持的符号。

## 另请参阅

### 内容视图控制器

- [使用视图控制器显示和管理视图](displaying-and-managing-views-with-a-view-controller.md) — 在 Storyboard 中构建视图控制器，使用自定义视图配置它，并使用 App 的数据填充这些视图。
- [显示和隐藏视图控制器](showing-and-hiding-view-controllers.md) — 使用不同技术显示视图控制器，并在过渡期间在它们之间传递数据。
- [UITableViewController](uitableviewcontroller.md) — 专门管理表格视图的视图控制器。
- [UICollectionViewController](uicollectionviewcontroller.md) — 专门管理集合视图的视图控制器。
- [UIContentContainer](uicontentcontainer.md) — 一组用于使视图控制器的内容适应大小和特征变化的方法。
