---
title: 底层文件管理编程主题
apple_id: 10000055i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LowLevelFileMgmt/Articles/EnumADir.html
archived_at: '2026-07-15T07:16:33.804698Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [底层文件管理编程主题](Introduction%20to%20Low-Level%20File%20Management%20Programming%20Topics.md)


[下一页](Resolving%20Aliases.md)[上一页](Using%20URLs.md)

# 处理目录的内容

本文介绍处理目录内容的两种方法。`NSFileManager` 提供了多个方法，可以返回目录中项目的路径数组或 URL 数组。要遍历目录的内容，可以使用 `NSDirectoryEnumerator` 对象。

`NSFileManager` 提供了多个方法，以路径数组或（在 Mac OS X v10.6 及更高版本中）URL 数组的形式返回目录的内容。

在 Mac OS X v10.6 及更高版本中，你可以使用 [contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:](https://developer.apple.com/documentation/foundation/nsfilemanager/1413768-contentsofdirectoryaturl) 获取目录中每个顶层项目的 `NSURL` 对象数组。（这是 [contentsOfDirectoryAtPath:error:](https://developer.apple.com/documentation/foundation/filemanager/1414584-contentsofdirectory) 基于 URL 的等效方法。如果你需要递归进入子目录，请使用 `enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:`，如[使用目录枚举器](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg44dglktk4yq)所示。）如果你只对 URL 感兴趣而不需要其他属性，可以为 keys 传入一个空数组、为 options 传入 `0`，如下例所示：

```objc
NSURL *url = <#A URL for a directory#>;
NSError *error = nil;
NSArray *array = [[NSFileManager defaultManager]
                   contentsOfDirectoryAtURL:url
                   includingPropertiesForKeys:[NSArray array]
                   options:0
                   error:&error];
if (array == nil) {
    // Handle the error
}
```

不过，使用 URL 的好处之一是你还可以高效地获取每个项目的附加信息。如果你希望返回的 URL 的属性缓存预先填充一组默认属性，可以为 keys 传入 `nil`、为 options 传入 `0`。你也可以指定要获取哪些属性，并通过选项忽略子目录、文件包的内容以及隐藏文件，如下例所示：

```objc
NSURL *url = <#A URL for a directory#>;
NSError *error = nil;
NSArray *properties = [NSArray arrayWithObjects: NSURLLocalizedNameKey,
                          NSURLCreationDateKey, NSURLLocalizedTypeDescriptionKey, nil];

NSArray *array = [[NSFileManager defaultManager]
                   contentsOfDirectoryAtURL:url
                   includingPropertiesForKeys:properties
                   options:(NSDirectoryEnumerationSkipsPackageDescendants |
                            NSDirectoryEnumerationSkipsHiddenFiles)
                   error:&error];
if (array == nil) {
    // Handle the error
}
```


如果你只想要一个目录的内容列表，排除任何子目录（并且不跟随符号链接），可以使用 [contentsOfDirectoryAtPath:error:](https://developer.apple.com/documentation/foundation/filemanager/1414584-contentsofdirectory)，如下例所示：

```objc
NSString *path = <#A path to a directory#>;
NSError *error = nil;
NSArray *array = [[NSFileManager defaultManager]
                   contentsOfDirectoryAtPath:path error:&error];
if (array == nil) {
    // Handle the error
}
```

如果你需要递归列表——即包含给定目录及其所有子目录中各个项目文件名的列表——可以使用 [subpathsOfDirectoryAtPath:error:](https://developer.apple.com/documentation/foundation/nsfilemanager/1417353-subpathsofdirectoryatpath)，如下例所示：

```objc
NSString *path = <#A path to a directory#>;
NSError *error = nil;
NSArray *array = [[NSFileManager defaultManager]
                   subpathsOfDirectoryAtPath:path error:&error];
if (array == nil) {
    // Handle the error
}
```


你可以使用 [NSDirectoryEnumerator](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDirectoryEnumerator/Description.html#//apple_ref/occ/cl/NSDirectoryEnumerator) 对象来[枚举](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Enumeration.html#//apple_ref/doc/uid/TP40008195-CH17)目录及其包含的所有子目录的内容。`NSDirectoryEnumerator` 是一个抽象类，是针对文件系统目录结构定制的私有具体子类的外壳。你不能直接创建 `NSDirectoryEnumerator` 对象——要通过 `NSFileManager` 获取合适的实例。

你可以使用 `NSFileManager` 的 [enumeratorAtPath:](https://developer.apple.com/documentation/foundation/filemanager/1408726-enumerator) 方法获取一个以文件路径字符串形式返回项目的目录枚举器。在 Mac OS X v10.6 及更高版本中，你可以使用以 URL 形式返回项目的目录枚举器。（如果你打算对返回的项目执行任何操作，使用 URL 通常更高效。）你可以通过文件管理器对象使用 [enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:](https://developer.apple.com/documentation/foundation/nsfilemanager/1409571-enumeratoraturl) 获取这样的实例。

两种枚举器都会返回该目录内包含的所有文件和目录的路径。这些路径是相对于该目录的。枚举是递归的，包括所有子目录中的文件，并跨越设备边界。它不解析符号链接，也不会尝试跟随指向目录的符号链接。通常你只需枚举 `NSDirectoryEnumerator` 对象中的各个项目即可。不过，你也可以使用 [skipDescendents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDirectoryEnumerator/Description.html#//apple_ref/occ/instm/NSDirectoryEnumerator/skipDescendents) 方法来避免列出你不感兴趣的目录的内容。

下面的基于 URL 的示例（适用于 Mac OS X v10.6 及更高版本）说明了如何使用 `enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:` 列出给定目录的所有用户可见子目录，并注明它们是目录还是文件包。keys 数组参数指定：对于本次枚举产生的每个 URL，预先获取并缓存指定的属性值——这使后续访问更高效。options 参数指定枚举不应列出文件包和隐藏文件的内容。错误处理器是一个返回布尔值的 [block 对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3)；如果它返回 `YES`，枚举在出错后继续；如果返回 `NO`，枚举停止。

```objc
NSURL *directoryURL = <#An NSURL object that contains a reference to a directory#>;

NSArray *keys = [NSArray arrayWithObjects:
    NSURLIsDirectoryKey, NSURLIsPackageKey, NSURLLocalizedNameKey, nil];

NSDirectoryEnumerator *enumerator = [[NSFileManager defaultManager]
                                     enumeratorAtURL:directoryURL
                                     includingPropertiesForKeys:keys
                                     options:(NSDirectoryEnumerationSkipsPackageDescendants |
                                              NSDirectoryEnumerationSkipsHiddenFiles)
                                     errorHandler:^(NSURL *url, NSError *error) {
                                         // Handle the error.
                                         // Return YES if the enumeration should continue after the error.
                                         return <#YES or NO#>;
                                     }];

for (NSURL *url in enumerator) {

    // Error-checking is omitted for clarity.

    NSNumber *isDirectory = nil;
    [url getResourceValue:&isDirectory forKey:NSURLIsDirectoryKey error:NULL];

    if ([isDirectory boolValue]) {

        NSString *localizedName = nil;
        [url getResourceValue:&localizedName forKey:NSURLLocalizedNameKey error:NULL];

        NSNumber *isPackage = nil;
        [url getResourceValue:&isPackage forKey:NSURLIsPackageKey error:NULL];

        if ([isPackage boolValue]) {
            NSLog(@"Package at %@", localizedName);
        }
        else {
            NSLog(@"Directory at %@", localizedName);
        }
    }
}
```

你还可以使用 `NSDirectoryEnumerator` 声明的其他方法，在枚举过程中确定文件的属性——包括父目录和当前文件或目录的属性——以及控制是否递归进入子目录。下面的基于字符串的示例枚举一个目录的内容，并列出最近 24 小时内被修改过的文件；不过，如果遇到 RTFD 文件包，它会跳过对它们的递归：

```objc
NSString *directoryPath = <#Get a path to a directory#>;
NSDirectoryEnumerator *directoryEnumerator = [[NSFileManager defaultManager] enumeratorAtPath:directoryPath];

NSDate *yesterday = [NSDate dateWithTimeIntervalSinceNow:(-60*60*24)];

for (NSString *path in directoryEnumerator) {

    if ([[path pathExtension] isEqualToString:@"rtfd"]) {
        // Don't enumerate this directory.
        [directoryEnumerator skipDescendents];
    }
    else {

        NSDictionary *attributes = [directoryEnumerator fileAttributes];
        NSDate *lastModificationDate = [attributes objectForKey:NSFileModificationDate];

        if ([yesterday earlierDate:lastModificationDate] == yesterday) {
            NSLog(@"%@ was modified within the last 24 hours", path);
        }
    }
}
```

[下一页](Resolving%20Aliases.md)[上一页](Using%20URLs.md)
