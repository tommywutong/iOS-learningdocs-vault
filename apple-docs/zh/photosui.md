---
title: PhotosUI
framework: PhotosUI
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui
source_url: 'https://developer.apple.com/documentation/photosui'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui.json'
content_hash: 'sha256:7ed3fcc384607e60'
translated: true
---

> 导航：[Technologies](technologies.md)

# PhotosUI

<sub>框架</sub>

使用选择器界面呈现某人的照片图库、显示实况照片，或者用自定功能扩展「照片」App。

## 概述

PhotosUI 提供了一个照片选择器，让用户可以查看自己的照片库，并选择一张或多张照片供你的 App 显示或处理。选择器渲染在系统视图中，只将用户所选的照片提供给你的 App 访问，从而实现具有增强隐私性的用户体验。

该框架还提供了一个可用于显示实况照片的视图。

> [!note] 注意
> PhotosUI 是一个 [PhotoKit](photokit.md) 框架。

## 主题

### 共享照片库

- [Delivering an Enhanced Privacy Experience in Your Photos App](photokit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md) — 采用最新的隐私增强功能，提供高级用户隐私控制。
- [PHLivePhotoView](photosui/phlivephotoview.md) — 一个用于显示实况照片的视图——实况照片是包含拍摄前后瞬间动态与声音的照片。

### 面向 UIKit、AppKit 的照片选择器

- [Selecting Photos and Videos in iOS](photokit/selecting-photos-and-videos-in-ios.md) — 通过使用照片选择器，改善查找和选择资源的用户体验。
- [PHPickerViewController](photosui/phpickerviewcontroller.md) — 一个视图控制器，为从照片库中选择资源提供用户界面。
- [PHPickerViewControllerDelegate](photosui/phpickerviewcontrollerdelegate-5yntc.md) — 委托必须实现的一组方法，用于响应 `PHPickerViewController` 的用户事件。
- [PHPickerConfiguration](photosui/phpickerconfiguration-swift.struct.md) — 一个包含如何配置选择器视图控制器信息的对象。
- [PHPickerFilter](photosui/phpickerfilter-swift.struct.md) — 一种定义要应用于照片库的过滤器的类型。
- [PHPickerResult](photosui/phpickerresult-swift.struct.md) — 表示从用户照片库中选中的资源的类型。

### 面向 SwiftUI 的照片选择器

- [Bringing Photos picker to your SwiftUI app](photokit/bringing-photos-picker-to-your-swiftui-app.md) — 使用 SwiftUI 提供的照片选择器视图来选择媒体资源。
- [Implementing an inline Photos picker](photokit/implementing-an-inline-photos-picker.md) — 将系统提供的半高照片选择器嵌入你 App 的视图中。
- [PhotosPicker](photosui/photospicker.md) — 一个显示照片选择器的视图，用于从照片库中选择资源。
- [PhotosPickerItem](photosui/photospickeritem.md) — 与照片选择器一起使用的项目所对应的类型。
- [PhotosPickerSelectionBehavior](photosui/photospickerselectionbehavior.md) — 描述照片选择器如何处理用户选择的类型。
- [PhotosPickerStyle](photosui/photospickerstyle.md)

### 实况照片

- [Displaying Live Photos](photokit/displaying-live-photos.md) — 提供与 iOS「照片」App 中一致的实况照片交互式回放。

### 照片编辑扩展

- [Creating Photo Editing Extensions](photokit/creating-photo-editing-extensions.md) — 通过捆绑 App 扩展，在「照片」App 中提供自定功能。
- [PHContentEditingController](photosui/phcontenteditingcontroller.md) — 你自定的视图控制器类实现的协议，用于为你的照片扩展提供用户界面。

### macOS「照片」项目扩展

- [Creating a Slideshow Project Extension for Photos](photokit/creating-a-slideshow-project-extension-for-photos.md) — 通过支持项目创建的扩展来增强 macOS「照片」App。
- [PHProject](photos/phproject.md) — 「照片」App 项目扩展的表示。
- [PHProjectInfo](photosui/phprojectinfo.md) — 有关项目扩展的信息。
- [PHProjectExtensionContext](photosui/phprojectextensioncontext.md) — 一个对象，为「照片」项目扩展提供对底层项目的访问，以及供编辑的用户照片库的访问。
- [PHProjectElement](photosui/phprojectelement.md) — 所有元素对象的超类。
- [PHProjectSection](photosui/phprojectsection.md) — 表示精选资源和文本元素的集合。
- [PHProjectRegionOfInterest](photosui/phprojectregionofinterest.md) — 照片资源中感兴趣区域的表示。
- [PHProjectChangeRequest](photos/phprojectchangerequest.md) — 在「照片」项目扩展中更改资源数据的请求。
- [PHProjectExtensionController](photosui/phprojectextensioncontroller.md) — 定义项目扩展生命周期和支持类型的协议。
- [PHProjectCategory](photosui/phprojectcategory.md) — 「照片」项目扩展分类的表示。

### Classes

- [PHSharedAlbumCreationViewController](photosui/phsharedalbumcreationviewcontroller.md) _(beta)_
- [PHSharedAlbumCustomizationViewController](photosui/phsharedalbumcustomizationviewcontroller.md) _(beta)_
- [PHSharedAlbumPostingViewController](photosui/phsharedalbumpostingviewcontroller.md) _(beta)_

### Structures

- [PHPickerMetadataOptions](photosui/phpickermetadataoptions.md) — 为 \\c PHPickerViewController 指定元数据选项的常量。 _(beta)_
- [PHPickerSearchText](photosui/phpickersearchtext-swift.struct.md) — `PHPickerViewController` 的搜索文本。
- [PHSharedAlbumCreationConfiguration](photosui/phsharedalbumcreationconfiguration-swift.struct.md) — 用于配置 `PHSharedAlbumCreationViewController` 的对象。
- [PHSharedAlbumCreationResult](photosui/phsharedalbumcreationresult-swift.struct.md) — 用户创建共享相簿的结果。

### Enumerations

- [PHSharedAlbumCreationSharingPolicy](photosui/phsharedalbumcreationsharingpolicy.md) — 创建共享相簿的共享策略。 _(beta)_

## 另请参阅

### Frameworks

- [Photos](photos.md) — 处理「照片」App 管理的图像和视频资源，包括来自 iCloud 照片和实况照片的资源。
