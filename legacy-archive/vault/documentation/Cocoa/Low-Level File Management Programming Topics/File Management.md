---
title: 底层文件管理编程主题
apple_id: 10000055i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LowLevelFileMgmt/Articles/FileManagement.html
archived_at: '2026-07-15T07:16:35.105407Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [底层文件管理编程主题](Introduction%20to%20Low-Level%20File%20Management%20Programming%20Topics.md)


[下一页](Information%20about%20Files%20and%20Volumes.md)[上一页](Creating%20Paths%20and%20Locating%20Directories.md)

# 文件管理

本文介绍如何执行多种文件及与文件相关的操作。

以下示例展示了如何使用 [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager) 在 Mac OS X v10.6 及更高版本中提供的基于 URL 的方法进行文件操作。

要移动或重命名文件或目录，使用 [moveItemAtURL:toURL:error:](https://developer.apple.com/documentation/foundation/nsfilemanager/1414750-moveitematurl)，如下面的代码片段所示：

```objc
NSFileManager *fileManager = [NSFileManager defaultManager];
NSURL *srcURL = <#Get the source URL#>;
NSURL *destinationURL = <#Create the destination URL#>;

NSError *error = nil;
if (![fileManager moveItemAtURL:srcURL toURL:destinationURL error:&error]) {
    // Handle the error.
}
```

要复制文件或目录，使用 [copyItemAtURL:toURL:error:](https://developer.apple.com/documentation/foundation/filemanager/1412957-copyitem)，如下面的代码片段所示：

```objc
NSFileManager *fileManager = [NSFileManager defaultManager];
NSURL *srcURL = <#Get the source URL#>;
NSURL *destinationURL = <#Create the destination URL#>;

NSError *error = nil;
if (![fileManager copyItemAtURL:srcURL toURL:destinationURL error:&error]) {
    // Handle the error.
}
```

要删除文件或目录，使用 [removeItemAtURL:error:](https://developer.apple.com/documentation/foundation/nsfilemanager/1413590-removeitematurl)，如下面的代码片段所示：

```objc
NSFileManager *fileManager = [NSFileManager defaultManager];
NSURL *url = <#Get the URL of the item to delete#>;

NSError *error = nil;
if (![fileManager removeItemAtURL error:&error]) {
    // Handle the error.
}
```

你还可以用另一个文件或目录替换某个文件或目录，并使用 [replaceItemAtURL:withItemAtURL:backupItemName:options:resultingItemURL:error:](https://developer.apple.com/documentation/foundation/nsfilemanager/1412432-replaceitematurl) 将原始项目重命名为一个表示它是备份的名称（对于 Carbon 开发者来说，这是 [FSExchangeObjects](https://developer.apple.com/documentation/coreservices/1565474-fsexchangeobjects) 函数的替代方法）。你通常在保存文稿时需要此功能；由于 `NSDocument` 在保存文稿时自己就会执行此操作，因此一般来说你自己使用它的理由很少。

在 Mac OS X v10.6 及更高版本中，`NSWorkspace` 提供了两个方法，可用于以与 Finder 相同的方式复制文件或将文件移到废纸篓。

使用 [recycleURLs:completionHandler:](https://developer.apple.com/documentation/appkit/nsworkspace/1530465-recycleurls) 以与 Finder 相同的方式将指定 URL 处的文件移到废纸篓。completion handler 参数是一个 [block 对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3)，在操作完成时被调用。

```objc
NSWorkspace *workspace = [NSWorkspace sharedWorkspace];
NSArray *URLs = <#An array of file URLs#>;
[workspace recycleURLs:URLs completionHandler:^(NSDictionary *newURLs, NSError *error) {
    if (error != nil) {
        // Deal with any errors here.
    }
}];
```


使用 [duplicateURLs:completionHandler:](https://developer.apple.com/documentation/appkit/nsworkspace/1524490-duplicateurls) 以与 Finder 相同的方式复制指定 URL 处的文件。completion handler 参数是一个 [block 对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3)，在操作完成时被调用。

```objc
NSWorkspace *workspace = [NSWorkspace sharedWorkspace];
NSArray *URLs = <#An array of file URLs#>;
[workspace duplicateURLs:URLs completionHandler:^(NSDictionary *newURLs, NSError *error) {
    if (error != nil) {
        // Deal with any errors here.
    }
}];
```

[下一页](Information%20about%20Files%20and%20Volumes.md)[上一页](Creating%20Paths%20and%20Locating%20Directories.md)
