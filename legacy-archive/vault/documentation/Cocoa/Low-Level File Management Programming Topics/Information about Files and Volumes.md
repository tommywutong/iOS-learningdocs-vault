---
title: 底层文件管理编程主题
apple_id: 10000055i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LowLevelFileMgmt/Articles/FileInfo.html
archived_at: '2026-07-15T07:16:34.859830Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [底层文件管理编程主题](Introduction%20to%20Low-Level%20File%20Management%20Programming%20Topics.md)


[下一页](Using%20URLs.md)[上一页](File%20Management.md)

# 关于文件和卷宗的信息

本文介绍如何获取和设置有关文件和卷宗的信息。

在 Mac OS X v10.6 及更高版本中，你可以使用 `NSURL` 获取和设置 URL 所指向项目的属性。获取属性值有两个方法，设置属性值也有两个方法，分别用于获取或设置单个值，或同时获取或设置多个值：

|  |  |
| --- | --- |
| [getResourceValue:forKey:error:](https://developer.apple.com/documentation/foundation/nsurl/1408874-getresourcevalue) |  |
| [setResourceValue:forKey:error:](https://developer.apple.com/documentation/foundation/nsurl/1413819-setresourcevalue) |  |
| [resourceValuesForKeys:error:](https://developer.apple.com/documentation/foundation/nsurl/1417657-resourcevalues) |  |
| [setResourceValues:error:](https://developer.apple.com/documentation/foundation/nsurl/1408208-setresourcevalues) |  |

`NSURL` 还为指定属性的键定义了常量，例如 `NSURLNameKey`、`NSURLLocalizedNameKey`、`NSURLIsPackageKey`、`NSURLCreationDateKey`、`NSURLFileSizeKey` 和 `NSURLCustomIconKey`。

以下示例展示了如何获取和设置单个及多个属性：

```objc
NSURL *url = <#Get a URL#>;
NSError *error = nil;
BOOL ok;

// Get the item's label color
NSColor *labelColor;
ok = [url getResourceValue:&labelColor forKey:NSURLLabelColorKey error:&error];
if (!ok) {
    // Handle the error.
}

// Make the item hidden
ok = [url setResourceValue:[NSNumber numberWithBool:YES] forKey:NSURLIsHiddenKey error:&error];
if (!ok) {
    // Handle the error.
}

// Get numerous properties
NSArray *keys = [NSArray arrayWithObjects:NSURLNameKey, NSURLLocalizedNameKey,
                                          NSURLIsRegularFileKey, NSURLIsDirectoryKey,
                                          NSURLIsSymbolicLinkKey, NSURLIsPackageKey, nil];
NSDictionary *properties = [url resourceValuesForKeys:keys error:&error];
if (properties == nil) {
    // Handle the error.
}
```


在 Mac OS X v10.6 及更高版本中，你可以使用 [mountedVolumeURLsIncludingResourceValuesForKeys:options:](https://developer.apple.com/documentation/foundation/nsfilemanager/1409626-mountedvolumeurlsincludingresour) 来查明系统上挂载了哪些卷宗。该方法返回一个 `NSURL` 对象数组，其中包含与你指定的键相对应的资源值（如果你只想知道存在哪些卷宗，可以为 keys 参数传入 `nil`）。options 参数允许你指定是否要忽略隐藏的卷宗，以及该方法是否应返回文件引用 URL（参阅[创建文件引用 URL](Using%20URLs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tanjzfvjvomy)）。

以下示例展示了如何获取所有可用卷宗的 URL，其中包含本地化名称和默认图标：

```objc
NSArray *resourceKeys = [NSArray arrayWithObjects:
                          NSURLLocalizedNameKey, NSURLEffectiveIconKey, nil];
NSArray *volumeURLs = [[NSFileManager defaultManager]
                         mountedVolumeURLsIncludingResourceValuesForKeys:resourceKeys
                         options:0];
```

[下一页](Using%20URLs.md)[上一页](File%20Management.md)
