---
title: 在 iCloud 环境中同步文稿
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, Xcode 12.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/synchronizing-documents-in-the-icloud-environment
source_url: 'https://developer.apple.com/documentation/uikit/synchronizing-documents-in-the-icloud-environment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/synchronizing-documents-in-the-icloud-environment.json'
content_hash: 'sha256:e67634bd90607052'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Documents, data, and pasteboard](documents-data-and-pasteboard.md)

# 在 iCloud 环境中同步文稿

<sub>示例代码</sub>

跨多台设备管理文稿，打造无缝的编辑与协作体验。

## 概述

随着技术的发展，越来越多的人从不同设备生成自己的数字资产，并期望这些资产能够无缝同步。为了支持这类使用场景，App 需要从所有设备发现这些资产及其变化，并向用户呈现一致的视图。

本示例演示了如何在 iCloud 环境中发现并同步文稿，以及如何管理这些文稿以实现高性能和低内存占用。这些_文稿_可以是数字资产，也可以是任何用户数据。

本示例还演示了如何将某个 iCloud 容器发布到 iCloud Drive，以便用户可以从其他 App 访问该容器的 `Documents` 文件夹。此外，它还展示了如何支持原位打开（Open-in-Place）特性，该特性允许用户通过在“文件”App 中点按某个文稿来启动一个 App，然后直接编辑该文稿。

### 配置示例代码项目

在构建本示例之前，请在 Xcode 中执行以下步骤：

1. 在 `SimpleiCloudDocument` target 的 General 面板中，将 Bundle Identifier 字段更新为一个新的标识符。
2. 在 Signing & Capabilities 面板中，从 Team 下拉菜单中选择适用的团队，让 Xcode 自动管理预配描述文件。详情请参阅 [Assign a project to a team](https://help.apple.com/xcode/mac/current/#/dev23aab79b4)。
3. 确保 iCloud 能力已存在，且 iCloud Documents 复选框处于选中状态，然后从 Containers 列表中选择带有你在第 1 步中设置的 Bundle Identifier 的 iCloud 容器。如果该容器不存在，请点击“添加”按钮（+），输入容器名称（iCloud.\<bundle identifier\>），然后点击“好”，让 Xcode 创建该容器并将其与该 App 关联。
4. 如果你想使用其他容器，请从 Containers 列表中选择它，并在 `MainViewController` 类的 `viewDidLoad` 方法中创建 `MetadataProvider` 实例时指定该容器标识符。iCloud 容器标识符区分大小写，且必须以“`iCloud.`”开头。
5. 在 `Info.plist` 文件中找到 `NSUbiquitousContainers` 条目，并同样修改其中的 iCloud 容器标识符。

在设备上运行本示例之前，请按以下方式配置设备：

1. 使用 Apple ID 登录。要让文稿能够跨设备同步，所有设备上必须使用相同的 Apple ID。
2. 依次选择“设置” > Apple ID > iCloud，如果 iCloud Drive 处于关闭状态，请将其打开。
3. 在“照片”图库中准备一些图片，以便在本示例中使用。

### 将 iCloud 容器发布到 iCloud Drive

将某个 iCloud 容器发布到 iCloud Drive，会使该容器的 `Documents` 文件夹出现在 iCloud Drive 中，从而让用户可以从其他 App 访问该文件夹。请按以下步骤发布一个容器：

1. 按照下方示例代码所示，在 `Info.plist` 文件中添加一个 `NSUbiquitousContainers` 条目，以提供该容器的元数据。
2. 通过修改 Xcode target 的 General 面板中的 Build 字段，或修改 `Info.plist` 文件中的 [`CFBundleVersion`](../bundleresources/information-property-list/cfbundleversion.md) 条目，来提高 Bundle 版本号。使用 [numeric](../foundation/nsstring/compareoptions/numeric.md) 选项调用 [compare(_:options:range:)](<../foundation/nsstring/compare(__options_range_).md>) 方法进行比较时，新值必须大于之前的值，并且只能包含数字（0–9）和句点（.）字符。系统只有在检测到新版本时才会更新 App 的 iCloud 容器元数据，因此每次元数据发生变化时都要执行这一步骤。
3. 确保 `Documents` 文件夹已存在于该 iCloud 容器中，且至少包含一个文稿。

本示例的 `NSUbiquitousContainers` 条目如下：

```xml
    <key>NSUbiquitousContainers</key>
    <dict>
        <key>iCloud.com.example.apple-samplecode.SimpleiCloudDocument</key>
        <dict>
            <key>NSUbiquitousContainerIsDocumentScopePublic</key>
            <true/>
            <key>NSUbiquitousContainerName</key>
            <string>SimpleiCloudDocument</string>
            <key>NSUbiquitousContainerSupportedFolderLevels</key>
            <string>ANY</string>
        </dict>
    </dict>
```

### 支持原位打开

原位打开（Open-in-Place）特性允许用户通过点按该 App 拥有类型的文稿来启动该 App。打开后，App 可以直接修改该文稿，而无需将其复制到 App 的沙盒容器中。请按以下步骤实现该特性：

1. 通过添加 [`CFBundleDocumentTypes`](../bundleresources/information-property-list/cfbundledocumenttypes.md) 和 [`UTExportedTypeDeclarations`](../bundleresources/information-property-list/utexportedtypedeclarations.md) 这两个 `Info.plist` 条目，为该 App 声明并导出一种文稿类型。确保该类型在 [`UTTypeConformsTo`](../bundleresources/information-property-list/utexportedtypedeclarations/uttypeconformsto.md) 条目中至少符合 `public.content` 和 `public.data`，以便其他系统组件（例如 `UIActivityViewController`）能够识别它。
2. 在 `Info.plist` 文件中添加 `LSSupportsOpeningDocumentsInPlace` 键，并将其值设为 `YES`。
3. 实现 `UISceneDelegate` 协议的 [- scene:openURLContexts:](<uiscenedelegate/scene(__openurlcontexts_).md>) 方法来接收该文稿。

如果传入的 URL 位于 App 沙盒之外，App 需要用 [`startAccessingSecurityScopedResource`](<../foundation/nsurl/startaccessingsecurityscopedresource().md>) 和 [`stopAccessingSecurityScopedResource`](<../foundation/nsurl/stopaccessingsecurityscopedresource().md>) 方法包裹访问该 URL 的代码。本示例并未显式这样做，因为它是通过 [UIDocument](uidocument.md) 来访问该 URL 的，而 [UIDocument](uidocument.md) 会自动处理[安全范围书签](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AppSandboxInDepth/AppSandboxInDepth.html#//apple_ref/doc/uid/TP40011183-CH3-SW16)。

### 在 iCloud 容器中发现文稿

iOS App 使用 [`NSMetadataQuery`](../foundation/nsmetadataquery.md) 而不是文件系统 API 来发现 iCloud 容器中的文稿。当某个 App 在一台设备上创建一个 iCloud 文稿时，iCloud 首先会将该文稿的元数据同步到其他设备，告知它们该文稿的存在。然后，根据设备类型的不同，iCloud 可能会继续同步该文稿的数据，也可能不会。对于 iOS 设备，iCloud 在 App 请求（无论是显式还是隐式请求）之前不会同步文稿数据。当某个 iOS App 收到通知得知存在一个新文稿时，该文稿的数据可能尚未实际存在于本地文件系统中，因此文件系统 API 无法发现它。

为了监视 iCloud 容器中的元数据变化，本示例创建了一个 `NSMetadataQuery` 对象。它使用以下代码来配置并启动查询，以收集 iCloud 容器中扩展名为 `.sicd` 的文稿的变化。

```swift
metadataQuery.notificationBatchingInterval = 1
metadataQuery.searchScopes = [NSMetadataQueryUbiquitousDataScope, NSMetadataQueryUbiquitousDocumentsScope]
metadataQuery.predicate = NSPredicate(format: "%K LIKE %@", NSMetadataItemFSNameKey, "*." + Document.extensionName)
metadataQuery.sortDescriptors = [NSSortDescriptor(key: NSMetadataItemFSNameKey, ascending: true)]
metadataQuery.start()
```

一个查询在收集元数据时分两个阶段：第一阶段收集所有当前匹配的结果，第二阶段收集实时更新。查询完成第一阶段时会发出一条 [`NSMetadataQueryDidFinishGathering`](../foundation/nsnotification/name-swift.struct/nsmetadataquerydidfinishgathering.md) 通知，此后每次发生更新时都会发出一条 [`NSMetadataQueryDidUpdate`](../foundation/nsnotification/name-swift.struct/nsmetadataquerydidupdate.md) 通知。为了避免与系统发生潜在冲突，在访问结果时应禁用查询更新，并在访问结束后重新启用它，如下例所示：

```swift
func metadataItemList() -> [MetadataItem] {
    var result = [MetadataItem]()
    metadataQuery.disableUpdates()
    if let metadataItems = metadataQuery.results as? [NSMetadataItem] {
        result = metadataItemList(from: metadataItems)
    }
    metadataQuery.enableUpdates()
    return result
}
```

### 管理大型数据集

本示例中的文稿可能包含许多图像，而且这些图像可能很大。为了只在必要时才加载图像数据，并在使用后立即释放该数据，`Document` 类提供了一些公共方法，用于直接访问文稿包中的图像。例如，以下方法异步获取一张完整图像：

```swift
func retrieveImageAsynchronously(with imageName: String, completionHandler: @escaping (UIImage?) -> Void) {
    performAsynchronousFileAccess {
        let imageFileURL = self.fileURL.appendingPathComponent(imageName)
        let fileCoordinator = NSFileCoordinator(filePresenter: self)
        fileCoordinator.coordinate(readingItemAt: imageFileURL, options: .withoutChanges, error: nil) { newURL in
            if let imageData = try? Data(contentsOf: newURL), let image = UIImage(data: imageData) {
                completionHandler(image)
            } else {
                completionHandler(nil)
            }
        }
    }
}
```

在直接操作文稿包中的文件时，本示例调用 [- performAsynchronousFileAccessUsingBlock:](<uidocument/performasynchronousfileaccess(__).md>) 方法，将文件访问串行化到后台队列中执行，并使用 [`NSFileCoordinator`](../foundation/nsfilecoordinator.md) 来协调读取或写入操作。

同样，为了避免默认实现将图像数据加载到 [`FileWrapper`](../foundation/filewrapper.md) 对象中并将其保留在内存里，本示例重写了 [- saveToURL:forSaveOperation:completionHandler:](<uidocument/save(to_for_completionhandler_).md>) 方法，在更新文稿时直接移除或添加图像文件。

```swift
override func save(to url: URL, for saveOperation: UIDocument.SaveOperation, completionHandler: ((Bool) -> Void)? = nil) {
    if saveOperation != .forCreating {
        print("\(#function)")
        return performAsynchronousFileAccess {
            let fileCoordinator = NSFileCoordinator(filePresenter: self)
            fileCoordinator.coordinate(writingItemAt: self.fileURL, options: .forMerging, error: nil) { newURL in
                let success = self.fulfillUnsavedChanges()
                self.fileModificationDate = Date()
                if let completionHandler = completionHandler {
                    DispatchQueue.main.async {
                        completionHandler(success)
                    }
                }
            }
        }
    }
    super.save(to: url, for: saveOperation, completionHandler: completionHandler)
}
```

### 解决版本冲突

在 iCloud 环境中，用户可以从不同设备编辑同一个文稿。根据网络状况和同步时机的不同，这可能会触发版本冲突。为 iCloud 文稿提供支持的 App，需要解决这些冲突，并移除过时的版本，以免占用用户的 iCloud 存储空间。

要用本示例制造一次文稿冲突：

1. 在两台已使用同一个 Apple ID 登录 iCloud、且都联网的 iOS 设备上运行本示例。
2. 在其中一台设备上创建一个包含若干图像的文稿，并观察该文稿与另一台设备同步。
3. 在两台设备上都打开飞行模式，使其断开互联网连接。
4. 在两台设备上分别修改该文稿：在一台设备上添加一些图像，在另一台设备上移除一些图像，然后保存更改。
5. 同时关闭两台设备上的飞行模式，使其重新连接到互联网。
6. 如果没有发生冲突，重复步骤 3–5。检测到冲突后，本示例会启用工具栏上的 `Conflicts` 项目，并将其颜色变为红色，以便用户解决该冲突。

在基于文稿的 App 中处理版本冲突相当直接，因为大部分繁重的工作都由 `UIDocument` 完成。发生冲突时，`UIDocument` 会检测到它，并发出一条 [UIDocumentStateChangedNotification](uidocument/statechangednotification.md) 通知，App 可以观察这条通知，然后实现自己的冲突解决策略。

本示例通过选择 [`modificationDate`](../foundation/nsfileversion/modificationdate.md) 最新的版本、并移除其余所有版本来解决冲突。它使用文件协调来评估某个 iCloud 文稿的版本信息，以避免与系统发生潜在冲突。

```swift
private func resolveConflictsAsynchronously(document: Document, completionHandler: ((Bool) -> Void)?) {
    DispatchQueue.global().async {
        NSFileCoordinator().coordinate(writingItemAt: document.fileURL,
                                       options: .contentIndependentMetadataOnly, error: nil) { newURL in
            let shouldRevert = self.pickLatestVersion(for: newURL)
            completionHandler?(shouldRevert)
        }
    }
}
```

## 另请参阅

### Documents

- [UIDocument](uidocument.md) — 一个用于管理你 App 数据中离散部分的抽象基类。
- [UIManagedDocument](uimanageddocument.md) — 一个与 Core Data 集成的托管文稿对象。

## 下载

- [SynchronizingDocumentsInTheICloudEnvironment.zip](https://docs-assets.developer.apple.com/published/74e04f5e0a75/SynchronizingDocumentsInTheICloudEnvironment.zip)
