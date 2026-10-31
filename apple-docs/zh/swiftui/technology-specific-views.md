---
title: 技术专属视图
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/technology-specific-views
source_url: 'https://developer.apple.com/documentation/swiftui/technology-specific-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/technology-specific-views.json'
content_hash: 'sha256:28c4240d788521ef'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 技术专属视图

<sub>API 集合</sub>

使用其他 Apple 框架提供的 SwiftUI 视图。

## 概述

要访问其他框架定义的 SwiftUI 视图，请在使用该视图的文件中同时导入 SwiftUI 和该框架。你可以查看视图文档页面上的可用性信息，找到需要导入的框架。

![](../../../attachments/dd13486d673485bcc02e34a3f2e756dd/technology-specific-views-hero@2x.png)

例如，要在你的 App 中使用 [Map](../mapkit/map.md) 视图，请同时导入 SwiftUI 和 MapKit。

```swift
import SwiftUI
import MapKit

struct MyMapView: View {
    // 将地图中心定于约书亚树国家公园。
    var region = MKCoordinateRegion(
            center: CLLocationCoordinate2D(latitude: 34.011_286, longitude: -116.166_868),
            span: MKCoordinateSpan(latitudeDelta: 0.2, longitudeDelta: 0.2)
        )

    var body: some View {
        Map(initialPosition: .region(region))
    }
}
```

有关设计指引，请参阅《人机界面指南》中的 [Technologies](../design/human-interface-guidelines/technologies.md)。

## 主题

### 显示网页内容

- [WebView](../webkit/webview-swift.struct.md) — 一个显示网页内容的视图。
- [WebPage](../webkit/webpage.md) — 一个控制和管理交互式网页内容行为的对象。
- [onWebViewImmersiveEnvironmentRequest(shouldAllow:present:dismiss:)](<view/onwebviewimmersiveenvironmentrequest(shouldallow_present_dismiss_).md>) — 管理网站请求的沉浸式环境的生命周期。_(beta)_
- [webViewBackForwardNavigationGestures(_:)](<view/webviewbackforwardnavigationgestures(__).md>) — 确定水平轻扫手势是否触发网页的后退和前进导航。
- [webViewContentBackground(_:)](<view/webviewcontentbackground(__).md>) — 指定网页自然背景色在此视图中的可见性。
- [webViewContextMenu(menu:)](<view/webviewcontextmenu(menu_).md>) — 向 WebView 添加基于项目的上下文菜单，替换默认的上下文菜单项集合。
- [webViewElementFullscreenBehavior(_:)](<view/webviewelementfullscreenbehavior(__).md>) — 确定网页视图能否全屏显示内容。
- [webViewLinkPreviews(_:)](<view/webviewlinkpreviews(__).md>) — 确定按下链接时是否显示该链接目的地的预览。
- [webViewMagnificationGestures(_:)](<view/webviewmagnificationgestures(__).md>) — 确定捏合缩放手势是否改变视图的放大率。
- [webViewOnScrollGeometryChange(for:of:action:)](<view/webviewonscrollgeometrychange(for_of_action_).md>) — 添加一个动作，当从滚动几何 (scroll geometry) 创建的值发生变化时执行。
- [webViewScrollInputBehavior(_:for:)](<view/webviewscrollinputbehavior(__for_).md>) — 在使用特定输入时启用或禁用网页视图的滚动。
- [webViewScrollPosition(_:)](<view/webviewscrollposition(__).md>) — 将滚动位置的绑定与网页视图关联。
- [webViewTextSelection(_:)](<view/webviewtextselection(__).md>) — 确定是否允许用户选择文本或以其他方式与文本交互。

### 访问 Apple Pay 与钱包

- [PayWithApplePayButton](../passkit/paywithapplepaybutton.md) — 一种类型，提供一个通过 Apple Pay 支付的按钮。
- [AddPassToWalletButton](../passkit/addpasstowalletbutton.md) — 一种类型，提供一个让用户能够将新的或现有凭证添加到 Apple 钱包的按钮。
- [VerifyIdentityWithWalletButton](../passkit/verifyidentitywithwalletbutton.md) — 一种类型，显示一个用于呈现身份验证流程的按钮。
- [addOrderToWalletButtonStyle(_:)](<view/addordertowalletbuttonstyle(__).md>) — 设置按钮的样式。
- [addPassToWalletButtonStyle(_:)](<view/addpasstowalletbuttonstyle(__).md>) — 设置按钮使用的样式。（参见 `PKAddPassButtonStyle`。）
- [onApplePayCouponCodeChange(perform:)](<view/onapplepaycouponcodechange(perform_).md>) — 在用户输入或更新优惠券代码时调用。如果会要求用户提供优惠券代码，则此修饰符是必需的。
- [onApplePayPaymentMethodChange(perform:)](<view/onapplepaypaymentmethodchange(perform_).md>) — 在支付方式变化并要求更新支付请求时调用。如果未提供此修饰符，钱包将默认支付方式有效。
- [onApplePayShippingContactChange(perform:)](<view/onapplepayshippingcontactchange(perform_).md>) — 在用户选择收货地址时调用。如果会要求用户提供收货联系人，则此修饰符是必需的。
- [onApplePayShippingMethodChange(perform:)](<view/onapplepayshippingmethodchange(perform_).md>) — 在用户选择配送方式时调用。如果会要求用户提供配送方式，则此修饰符是必需的。
- [payLaterViewAction(_:)](<view/paylaterviewaction(__).md>) — 设置 PayLaterView 上的操作。参见 `PKPayLaterAction`。
- [payLaterViewDisplayStyle(_:)](<view/paylaterviewdisplaystyle(__).md>) — 设置 PayLaterView 的显示样式。参见 `PKPayLaterDisplayStyle`。
- [payWithApplePayButtonDisableCardArt()](<view/paywithapplepaybuttondisablecardart().md>) — 设置应允许在支付按钮上显示的特性。
- [payWithApplePayButtonStyle(_:)](<view/paywithapplepaybuttonstyle(__).md>) — 设置按钮使用的样式。（参见 `PayWithApplePayButtonStyle`。）
- [verifyIdentityWithWalletButtonStyle(_:)](<view/verifyidentitywithwalletbuttonstyle(__).md>) — 设置按钮使用的样式。（参见 `PKIdentityButtonStyle`。）
- [AsyncShareablePassConfiguration](../passkit/asyncshareablepassconfiguration.md)
- [transactionTask(_:action:)](<view/transactiontask(__action_).md>) — 提供一个任务，在此视图出现之前执行

### 授权与认证

- [LocalAuthenticationView](../localauthentication/localauthenticationview.md) — 一个显示认证界面的 SwiftUI 视图。
- [SignInWithAppleButton](../authenticationservices/signinwithapplebutton.md) — 一个 SwiftUI 视图，用于创建供显示的「通过 Apple 登录」按钮。
- [signInWithAppleButtonStyle(_:)](<view/signinwithapplebuttonstyle(__).md>) — 设置显示该控制时使用的样式（参见 `SignInWithAppleButton.Style`）。
- [authorizationController](environmentvalues/authorizationcontroller.md) — SwiftUI 环境中提供的一个值，视图可用它执行授权请求。
- [webAuthenticationSession](environmentvalues/webauthenticationsession.md) — SwiftUI 环境中提供的一个值，视图可用它通过网络服务认证用户。

### 配置家人共享

- [FamilyActivityPicker](../familycontrols/familyactivitypicker.md) — 一种视图，用户可在其中指定 App、网站域和类别，而不会向 App 透露他们的选择。
- [familyActivityPicker(isPresented:selection:)](<view/familyactivitypicker(ispresented_selection_).md>) — 以表单形式呈现一个活动选择器视图。
- [familyActivityPicker(headerText:footerText:isPresented:selection:)](<view/familyactivitypicker(headertext_footertext_ispresented_selection_).md>) — 以表单形式呈现一个活动选择器视图。
- [familyActivityPicker(title:headerText:footerText:isPresented:selection:)](<view/familyactivitypicker(title_headertext_footertext_ispresented_selection_).md>) — 呈现一个活动选择器表单，用于选择要管理的 App 和网站。

### 报告设备活动

- [DeviceActivityReport](../deviceactivity/deviceactivityreport.md) — 一个以保护隐私的方式报告用户的 App、类别和网站域活动的视图。

### 使用受管理的设备

- [managedContentStyle(_:)](<view/managedcontentstyle(__).md>) — 将受管理内容样式应用到视图。
- [automatedDeviceEnrollmentAddition(isPresented:)](<view/automateddeviceenrollmentaddition(ispresented_).md>) — 呈现一个模态视图，让用户能够将设备添加到其组织。

### 创建图形

- [Chart](../charts/chart.md) — 一个显示图表的 SwiftUI 视图。
- [SceneView](../scenekit/sceneview.md) — 一个用于显示 3D SceneKit 内容的 SwiftUI 视图。_(已废弃)_
- [SpriteView](../spritekit/spriteview.md) — 一个渲染 SpriteKit 场景的 SwiftUI 视图。

### 获取位置信息

- [LocationButton](../corelocationui/locationbutton.md) — 一个授予一次性位置授权的 SwiftUI 按钮。
- [Map](../mapkit/map.md) — 一个显示嵌入式地图界面的视图。
- [mapStyle(_:)](<view/mapstyle(__).md>) — 指定要使用的地图样式。
- [mapScope(_:)](<view/mapscope(__).md>) — 创建一个 mapScope，SwiftUI 用它将地图控制连接到关联的地图。
- [mapFeatureSelectionDisabled(_:)](<view/mapfeatureselectiondisabled(__).md>) — 指定哪些地图要素应禁用选择。
- [mapFeatureSelectionAccessory(_:)](<view/mapfeatureselectionaccessory(__).md>) — 指定为 `MapFeature` 显示的选择附件
- [mapFeatureSelectionContent(content:)](<view/mapfeatureselectioncontent(content_).md>) — 为当前选定的地图要素指定自定呈现方式。
- [mapControls(_:)](<view/mapcontrols(__).md>) — 将关联环境中的所有 `Map` 视图配置为具有标准尺寸和位置控制
- [mapControlVisibility(_:)](<view/mapcontrolvisibility(__).md>) — 将环境中的所有地图控制配置为具有指定的可见性
- [mapCameraKeyframeAnimator(trigger:keyframes:)](<view/mapcamerakeyframeanimator(trigger_keyframes_).md>) — 当给定的触发值变化时，使用给定的关键帧为 `Map` 的相机制作动画。
- [lookAroundViewer(isPresented:scene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)](<view/lookaroundviewer(ispresented_scene_allowsnavigation_showsroadlabels_pointsofinterest_ondismiss_).md>)
- [lookAroundViewer(isPresented:initialScene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)](<view/lookaroundviewer(ispresented_initialscene_allowsnavigation_showsroadlabels_pointsofinterest_ondismiss_).md>)
- [onMapCameraChange(frequency:_:)](<view/onmapcamerachange(frequency___).md>) — 当地图相机取景变化时执行一个操作
- [mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:)](<view/mapitemdetailpopover(ispresented_item_displaysmap_attachmentanchor_).md>) — 呈现地图项详情弹出窗口。
- [mapItemDetailPopover(isPresented:item:displaysMap:attachmentAnchor:arrowEdge:)](<view/mapitemdetailpopover(ispresented_item_displaysmap_attachmentanchor_arrowedge_).md>) — 呈现地图项详情弹出窗口。
- [mapItemDetailPopover(item:displaysMap:attachmentAnchor:)](<view/mapitemdetailpopover(item_displaysmap_attachmentanchor_).md>) — 呈现地图项详情弹出窗口。
- [mapItemDetailPopover(item:displaysMap:attachmentAnchor:arrowEdge:)](<view/mapitemdetailpopover(item_displaysmap_attachmentanchor_arrowedge_).md>) — 呈现地图项详情弹出窗口。
- [mapItemDetailSheet(isPresented:item:displaysMap:)](<view/mapitemdetailsheet(ispresented_item_displaysmap_).md>) — 呈现地图项详情表单。
- [mapItemDetailSheet(item:displaysMap:)](<view/mapitemdetailsheet(item_displaysmap_).md>) — 呈现地图项详情表单。

### 显示媒体

- [CameraView](../homekit/cameraview.md) — 一个 SwiftUI 视图，视频流或图像快照会渲染到其中。
- [NowPlayingView](../watchkit/nowplayingview.md) — 一个显示系统「正在播放」界面的视图，供用户控制音频。
- [VideoPlayer](../avkit/videoplayer.md) — 一个显示播放器内容的视图，并提供用于控制播放的原生用户界面。
- [continuityDevicePicker(isPresented:onDidConnect:)](<view/continuitydevicepicker(ispresented_ondidconnect_).md>) — `continuityDevicePicker` 应用于通过按钮界面或其他形式的激活方式来发现并连接附近的连续互通设备。在 tvOS 上，选中后会呈现全屏的连续互通设备选择体验。当给定条件为真时，模态视图会尽可能覆盖 `self` 的屏幕。
- [cameraAnchor(isActive:)](<view/cameraanchor(isactive_).md>) — 指定应充当 Apple Vision Pro 2D Persona 流虚拟相机的视图。
- [foveatedStreamingPauseSheet(session:)](<view/foveatedstreamingpausesheet(session_).md>) — 告知系统在注视流式传输会话暂停时呈现一个带有恢复或结束该会话控制的表单。

### 支持群组活动

- [groupActivityAssociation(_:)](<view/groupactivityassociation(__).md>) — 指定某个视图应如何与当前的 SharePlay 群组活动相关联。

### 选取照片

- [PhotosPicker](../photosui/photospicker.md) — 一个显示照片选择器的视图，用于从照片库中选择资源。
- [photosPicker(isPresented:selection:matching:preferredItemEncoding:)](<view/photospicker(ispresented_selection_matching_preferreditemencoding_).md>) — 呈现一个可选择 `PhotosPickerItem` 的照片选择器。
- [photosPicker(isPresented:selection:matching:preferredItemEncoding:photoLibrary:)](<view/photospicker(ispresented_selection_matching_preferreditemencoding_photolibrary_).md>) — 呈现一个照片选择器，从给定的照片图库中选择 `PhotosPickerItem`。
- [photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)](<view/photospicker(ispresented_selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_).md>) — 呈现一个可选择一组 `PhotosPickerItem` 的照片选择器。
- [photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:)](<view/photospicker(ispresented_selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_photolibrary_).md>) — 呈现一个照片选择器，从给定的照片图库中选择一组 `PhotosPickerItem`。
- [photosPickerAccessoryVisibility(_:edges:)](<view/photospickeraccessoryvisibility(__edges_).md>) — 设置照片选择器的附件可见性。附件包括内容与边缘之间的任何内容，例如导航栏或边栏。
- [photosPickerDisabledCapabilities(_:)](<view/photospickerdisabledcapabilities(__).md>) — 停用照片选择器的某些功能。
- [photosPickerSearchText(_:)](<view/photospickersearchtext(__).md>) — 设置照片选择器的搜索文本。 _(beta)_
- [photosPickerStyle(_:)](<view/photospickerstyle(__).md>) — 设置照片选择器的模式。
- [photosPickerMetadataOptions(_:)](<view/photospickermetadataoptions(__).md>) — 设置照片选择器的元数据选项。_(beta)_
- [photosSharedAlbumCreationSheet(isPresented:defaultTitle:defaultSharingPolicy:photoLibrary:onCompletion:)](<view/photossharedalbumcreationsheet(ispresented_defaulttitle_defaultsharingpolicy_photolibrary_oncompletion_).md>) — 呈现一个视图，允许用户创建新的共享相簿。 _(beta)_
- [photosSharedAlbumCustomizationSheet(isPresented:albumIdentifier:photoLibrary:onCompletion:)](<view/photossharedalbumcustomizationsheet(ispresented_albumidentifier_photolibrary_oncompletion_).md>) — 呈现一个视图，允许用户自定指定的共享相簿。 _(beta)_
- [photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:)](<view/photossharedalbumpostingsheet(ispresented_items_defaultalbumidentifier_photolibrary_completion_).md>) — 呈现一个「添加到共享相簿」表单，允许用户将给定条目发布到共享相簿。 _(beta)_

### 生成图像

- [imagePlaygroundGenerationStyle(_:in:)](<view/imageplaygroundgenerationstyle(__in_).md>) — 设置显示图像生成表单时要使用的已选样式和允许样式。
- [imagePlaygroundOptions(_:)](<view/imageplaygroundoptions(__).md>) — 设置生成图像时要使用的选项。
- [imagePlaygroundSheet(isPresented:concept:sourceImage:onCompletion:onCancellation:)](<view/imageplaygroundsheet(ispresented_concept_sourceimage_oncompletion_oncancellation_).md>) — 呈现系统表单，使用指定的字符串和可选的起始图像创建图像。
- [imagePlaygroundSheet(isPresented:concept:sourceImage:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<view/imageplaygroundsheet(ispresented_concept_sourceimage_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — 呈现系统表单，根据指定的输入创建图像。
- [imagePlaygroundSheet(isPresented:concept:sourceImageURL:onCompletion:onCancellation:)](<view/imageplaygroundsheet(ispresented_concept_sourceimageurl_oncompletion_oncancellation_).md>) — 呈现系统表单，使用指定的字符串和图像 URL 创建图像。
- [imagePlaygroundSheet(isPresented:concept:sourceImageURL:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<view/imageplaygroundsheet(ispresented_concept_sourceimageurl_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — 呈现系统表单，使用指定的字符串和图像 URL 创建图像或 Genmoji。
- [imagePlaygroundSheet(isPresented:concepts:sourceImage:onCompletion:onCancellation:)](<view/imageplaygroundsheet(ispresented_concepts_sourceimage_oncompletion_oncancellation_).md>) — 呈现系统表单，使用一个或多个概念和可选的起始图像创建图像。
- [imagePlaygroundSheet(isPresented:concepts:sourceImage:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<view/imageplaygroundsheet(ispresented_concepts_sourceimage_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — 呈现系统表单，使用一个或多个概念和可选的起始图像创建图像或 Genmoji。
- [imagePlaygroundSheet(isPresented:concepts:sourceImageURL:onCompletion:onCancellation:)](<view/imageplaygroundsheet(ispresented_concepts_sourceimageurl_oncompletion_oncancellation_).md>) — 呈现系统表单，使用一个或多个概念和图像 URL 创建图像。
- [imagePlaygroundSheet(isPresented:concepts:sourceImageURL:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<view/imageplaygroundsheet(ispresented_concepts_sourceimageurl_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — 呈现系统表单，使用一个或多个概念和图像 URL 创建图像或 Genmoji。

### 预览内容

- [quickLookPreview(_:)](<view/quicklookpreview(__).md>) — 呈现单个 URL 内容的快速查看预览。
- [quickLookPreview(_:in:)](<view/quicklookpreview(__in_).md>) — 呈现你提供的 URL 的快速查看预览。

### 与联网设备交互

- [DevicePicker](../devicediscoveryui/devicepicker.md) — 一个 SwiftUI 视图，显示网络上的其他设备，并创建到该设备上运行的你 App 副本的加密连接。
- [devicePickerSupports](environmentvalues/devicepickersupports.md) — 检查是否支持呈现 DevicePicker。

### 配置实时活动

- [activitySystemActionForegroundColor(_:)](<view/activitysystemactionforegroundcolor(__).md>) — 系统在锁定屏幕上的实时活动旁边显示的辅助操作按钮的文本颜色。
- [activityBackgroundTint(_:)](<view/activitybackgroundtint(__).md>) — 为出现在锁定屏幕上的实时活动的背景设置色调颜色。
- [isActivityFullscreen](environmentvalues/isactivityfullscreen.md) — 一个布尔值，指示实时活动是否以全屏呈现方式显示。
- [activityFamily](environmentvalues/activityfamily.md) — 当前实时活动的尺寸系列。

### 与 App Store 和 Apple Music 交互

- [appStoreOverlay(isPresented:configuration:)](<view/appstoreoverlay(ispresented_configuration_).md>) — 当给定条件为真时呈现一个 StoreKit 覆盖层。
- [manageSubscriptionsSheet(isPresented:)](<view/managesubscriptionssheet(ispresented_).md>)
- [refundRequestSheet(for:isPresented:onDismiss:)](<view/refundrequestsheet(for_ispresented_ondismiss_).md>) — 为给定的交易显示退款请求表单。
- [offerCodeRedemption(options:isPresented:onCompletion:)](<view/offercoderedemption(options_ispresented_oncompletion_).md>) — 呈现一个表单，让顾客可以兑换你在 App Store Connect 中配置的优惠代码。 _(beta)_
- [musicPicker(isPresented:title:selection:)](<view/musicpicker(ispresented_title_selection_).md>) — 呈现一个音乐选择器，用于从 Apple Music 目录和用户的音乐资料库中选取项目。_(beta)_
- [musicSubscriptionOffer(isPresented:options:onLoadCompletion:)](<view/musicsubscriptionoffer(ispresented_options_onloadcompletion_).md>) — 当 `isPresented` 绑定为 `true` 时，启动呈现一个包含 Apple Music 订阅优惠的表单的流程。
- [currentEntitlementTask(for:priority:action:)](<view/currententitlementtask(for_priority_action_).md>) — 将视图声明为依赖某个 App 内购买产品的 entitlement，并返回修改后的视图。
- [inAppPurchaseOptions(_:)](<view/inapppurchaseoptions(__).md>) — 添加一个在此视图内的 StoreKit 视图发起购买之前调用的函数，为购买提供一组选项。
- [manageSubscriptionsSheet(isPresented:subscriptionGroupID:)](<view/managesubscriptionssheet(ispresented_subscriptiongroupid_).md>)
- [onInAppPurchaseCompletion(perform:)](<view/oninapppurchasecompletion(perform_).md>) — 添加一个操作，在此视图内的 StoreKit 视图发起的购买完成时执行。
- [onInAppPurchaseStart(perform:)](<view/oninapppurchasestart(perform_).md>) — 添加一个操作，在用户触发此视图内 StoreKit 视图上的购买按钮时执行。
- [productIconBorder()](<view/producticonborder().md>) — 为 App 内购买产品的图标添加标准边框。
- [productViewStyle(_:)](<view/productviewstyle(__).md>) — 设置视图内 App 内购买产品视图的样式。
- [productDescription(_:)](<view/productdescription(__).md>) — 配置视图内显示 App 内购买产品描述的标签的可见性。
- [storeButton(_:for:)](<view/storebutton(__for_).md>) — 指定商店视图和订阅商店视图实例可能使用的辅助按钮的可见性。
- [storeProductTask(for:priority:action:)](<view/storeproducttask(for_priority_action_).md>) — 将视图声明为依赖某个 App 内购买产品，并返回修改后的视图。
- [storeProductsTask(for:priority:action:)](<view/storeproductstask(for_priority_action_).md>) — 将视图声明为依赖一组 App 内购买产品，并返回修改后的视图。
- [subscriptionStatusTask(for:priority:action:)](<view/subscriptionstatustask(for_priority_action_).md>) — 将视图声明为依赖某个自动续期订阅组的状态，并返回修改后的视图。
- [subscriptionStoreButtonLabel(_:)](<view/subscriptionstorebuttonlabel(__).md>) — 将视图内的订阅商店视图实例配置为使用提供的按钮标签。
- [subscriptionStoreControlIcon(icon:)](<view/subscriptionstorecontrolicon(icon_).md>) — 设置一个视图，用于装饰订阅商店视图中的各个订阅选项。
- [subscriptionStoreControlStyle(_:)](<view/subscriptionstorecontrolstyle(__).md>) — 设置视图内订阅商店视图的控制样式。
- [subscriptionStoreControlStyle(_:placement:)](<view/subscriptionstorecontrolstyle(__placement_).md>) — 设置视图内订阅商店视图的控制样式和控制放置位置。
- [subscriptionStoreOptionGroupStyle(_:)](<view/subscriptionstoreoptiongroupstyle(__).md>) — 设置此视图内的订阅商店视图显示订阅选项组时使用的样式。
- [subscriptionStorePickerItemBackground(_:)](<view/subscriptionstorepickeritembackground(__).md>) — 设置视图内订阅商店视图实例的选择器项目的背景样式。
- [subscriptionStorePickerItemBackground(_:in:)](<view/subscriptionstorepickeritembackground(__in_).md>) — 设置视图内订阅商店视图选择器项目的背景形状和样式。
- [subscriptionStorePolicyDestination(for:destination:)](<view/subscriptionstorepolicydestination(for_destination_).md>) — 将一个视图配置为订阅商店视图中政策按钮操作的目的地。
- [subscriptionStorePolicyDestination(url:for:)](<view/subscriptionstorepolicydestination(url_for_).md>) — 将一个 URL 配置为订阅商店视图中政策按钮操作的目的地。
- [subscriptionStorePolicyForegroundStyle(_:)](<view/subscriptionstorepolicyforegroundstyle(__).md>) — 设置订阅商店视图内服务条款和隐私政策按钮的样式。
- [subscriptionStorePolicyForegroundStyle(_:_:)](<view/subscriptionstorepolicyforegroundstyle(____).md>) — 设置订阅商店视图内服务条款和隐私政策按钮的主要和次要样式。
- [subscriptionStoreSignInAction(_:)](<view/subscriptionstoresigninaction(__).md>) — 添加一个操作，在用户使用视图内订阅商店视图上的登录按钮时执行。
- [subscriptionStoreControlBackground(_:)](<view/subscriptionstorecontrolbackground(__).md>) — 设置一个标准效果，用于视图内订阅商店视图控制的背景。
- [subscriptionPromotionalOffer(offer:compactJWS:)](<view/subscriptionpromotionaloffer(offer_compactjws_).md>) — 选择要应用于顾客从订阅商店视图进行购买的促销优惠。
- [subscriptionIntroductoryOffer(applyOffer:compactJWS:)](<view/subscriptionintroductoryoffer(applyoffer_compactjws_).md>) — 选择要应用于顾客从订阅商店视图进行购买的介绍性优惠资格偏好。
- [subscriptionOfferViewButtonVisibility(_:for:)](<view/subscriptionofferviewbuttonvisibility(__for_).md>)
- [subscriptionOfferViewDetailAction(_:)](<view/subscriptionofferviewdetailaction(__).md>)
- [subscriptionOfferViewStyle(_:)](<view/subscriptionofferviewstyle(__).md>)
- [preferredSubscriptionOffer(_:)](<view/preferredsubscriptionoffer(__).md>) — 选择要应用于顾客从订阅商店视图、商店视图或产品视图进行购买的订阅优惠。
- [preferredSubscriptionPricingTerms(_:)](<view/preferredsubscriptionpricingterms(__).md>)

### 访问健康数据

- [healthDataAccessRequest(store:objectType:predicate:trigger:completion:)](<view/healthdataaccessrequest(store_objecttype_predicate_trigger_completion_).md>) — 异步请求读取需要按对象授权的数据类型的权限（例如视力处方）。
- [healthDataAccessRequest(store:readTypes:trigger:completion:)](<view/healthdataaccessrequest(store_readtypes_trigger_completion_).md>) — 请求读取指定 HealthKit 数据类型的权限。
- [healthDataAccessRequest(store:shareTypes:readTypes:trigger:completion:)](<view/healthdataaccessrequest(store_sharetypes_readtypes_trigger_completion_).md>) — 请求保存和读取指定 HealthKit 数据类型的权限。
- [workoutPreview(_:isPresented:)](<view/workoutpreview(__ispresented_).md>) — 以模态表单的形式呈现体能训练内容的预览

### 提供提示

- [popoverTip(_:arrowEdge:action:)](<view/popovertip(__arrowedge_action_).md>) — 在被修饰的视图上呈现弹出窗口提示。
- [popoverTip(_:isPresented:attachmentAnchor:arrowEdge:action:)](<view/popovertip(__ispresented_attachmentanchor_arrowedge_action_).md>) — 在被修饰的视图上呈现弹出窗口提示。
- [popoverTip(_:isPresented:attachmentAnchor:arrowEdges:action:)](<view/popovertip(__ispresented_attachmentanchor_arrowedges_action_).md>) — 在被修饰的视图上呈现弹出窗口提示。
- [tipAnchor(_:)](<view/tipanchor(__).md>) — 为指定的提示锚点设置一个值，用于将提示视图锚定到视图的 `.bounds`。
- [tipBackground(_:)](<view/tipbackground(__).md>) — 将提示视图的背景设置为某种样式。
- [tipBackgroundInteraction(_:)](<view/tipbackgroundinteraction(__).md>) — 控制用户能否与所呈现提示背后的视图交互。
- [tipCornerRadius(_:antialiased:)](<view/tipcornerradius(__antialiased_).md>) — 设置内联提示视图的圆角半径。
- [tipImageSize(_:)](<view/tipimagesize(__).md>) — 设置提示图像的尺寸。
- [tipViewStyle(_:)](<view/tipviewstyle(__).md>) — 为视图层级结构中的 TipView 设置给定样式。
- [tipImageStyle(_:)](<view/tipimagestyle(__).md>) — 设置提示图像的样式。
- [tipImageStyle(_:_:)](<view/tipimagestyle(____).md>) — 设置提示图像的样式。
- [tipImageStyle(_:_:_:)](<view/tipimagestyle(______).md>) — 设置提示图像的样式。

### 显示翻译

- [translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)](<view/translationpresentation(ispresented_text_attachmentanchor_arrowedge_replacementaction_).md>) — 当给定条件为真时呈现一个翻译弹出窗口。
- [translationTask(_:action:)](<view/translationtask(__action_).md>) — 添加一个任务，在此视图出现之前或翻译配置更改时执行。
- [translationTask(source:target:action:)](<view/translationtask(source_target_action_).md>) — 添加一个任务，在此视图出现之前或指定的源语言或目标语言更改时执行。
- [translationTask(source:target:preferredStrategy:action:)](<view/translationtask(source_target_preferredstrategy_action_).md>) — 添加一个任务，在此视图出现之前或指定的源语言或目标语言更改时执行。

### 呈现手记建议

- [journalingSuggestionsPicker(isPresented:onCompletion:)](<view/journalingsuggestionspicker(ispresented_oncompletion_).md>) — 呈现一个可视化的选择器界面，其中包含用户可选择的活动和图像，以获取更多信息。
- [journalingSuggestionsPicker(isPresented:journalingSuggestionToken:onCompletion:)](<view/journalingsuggestionspicker(ispresented_journalingsuggestiontoken_oncompletion_).md>) — 呈现一个可视化的选择器界面，其中包含用户可选择的活动和图像，以获取更多信息。

### 管理通讯录访问

- [contactAccessButtonCaption(_:)](<view/contactaccessbuttoncaption(__).md>)
- [contactAccessButtonStyle(_:)](<view/contactaccessbuttonstyle(__).md>)
- [contactAccessPicker(isPresented:completionHandler:)](<view/contactaccesspicker(ispresented_completionhandler_).md>) — 以模态方式呈现一个界面，允许用户选择你的 App 可以访问哪些联系人。

### 同步游戏存档

- [gameSaveSyncingAlert(directory:finishedLoading:)](<view/gamesavesyncingalert(directory_finishedloading_).md>) — 在游戏同步目录加载期间呈现一个模态视图。

### 处理游戏控制器事件

- [handlesGameControllerEvents(matching:)](<view/handlesgamecontrollerevents(matching_).md>) — 指定当此视图或其某个子视图获得焦点时，应通过 GameController 框架递送的游戏控制器事件。

### 创建桌面游戏

- [tabletopGame(_:parent:automaticUpdate:)](<view/tabletopgame(__parent_automaticupdate_).md>) — 向视图添加桌面游戏。
- [tabletopGame(_:parent:automaticUpdate:interaction:)](<view/tabletopgame(__parent_automaticupdate_interaction_).md>) — 提供一个闭包，在需要时返回新的交互。

### 配置相机控制

- [realityViewCameraControls](environmentvalues/realityviewcameracontrols.md) — 现实视图的相机控制。
- [realityViewCameraControls(_:)](<view/realityviewcameracontrols(__).md>) — 添加控制虚拟相机位置和方向的手势。
- [realityViewLayoutBehavior(_:)](<view/realityviewlayoutbehavior(__).md>) — 一种视图修饰符，控制 `RealityView` 的边框尺寸和内容对齐行为

### 与交易交互

- [transactionPicker(isPresented:selection:)](<view/transactionpicker(ispresented_selection_).md>) — 呈现一个选择器，用于选择一组交易。

## 另请参阅

### 框架集成

- [AppKit integration](appkit-integration.md) — 向你的 SwiftUI App 添加 AppKit 视图，或在你的 AppKit App 中使用 SwiftUI 视图。
- [UIKit integration](uikit-integration.md) — 向你的 SwiftUI App 添加 UIKit 视图，或在你的 UIKit App 中使用 SwiftUI 视图。
- [WatchKit integration](watchkit-integration.md) — 向你的 SwiftUI App 添加 WatchKit 视图，或在你的 WatchKit App 中使用 SwiftUI 视图。
