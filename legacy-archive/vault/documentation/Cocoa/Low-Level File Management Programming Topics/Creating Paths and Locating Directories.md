---
title: 底层文件管理编程主题
apple_id: 10000055i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LowLevelFileMgmt/Articles/StandardDirectories.html
archived_at: '2026-07-15T07:16:37.177060Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [底层文件管理编程主题](Introduction%20to%20Low-Level%20File%20Management%20Programming%20Topics.md)


[下一页](File%20Management.md)[上一页](File%20Management%20Classes.md)

# 创建路径与定位目录

本文介绍如何创建表示路径的 URL 和字符串，以及如何在文件系统中定位标准目录。

`NSString` 提供了许多路径工具方法，你可以用它们来完成诸如以下任务：提取路径的各个组成部分（目录、文件名和扩展名）、由这些组成部分构建路径、“转换”路径分隔符、清理包含符号链接和多余斜杠的路径，以及执行类似的操作。

在 Mac OS X v10.6 及更高版本中，`NSURL` 提供了一组与 `NSString` 类似的路径工具方法。在可能的情况下，你通常应使用基于 URL 的方法而不是基于字符串的方法，因为基于 URL 的操作通常比等效的字符串操作高效得多。因此，在可能的情况下，你应该直接使用 `NSURL` 对象，而不是把路径当作字符串来操作。

无论你使用 `NSString` 还是 `NSURL`，每当你需要对路径执行任何操作时，都应该使用这些方法，而不是任何其他途径。

在 Mac OS X v10.6 及更高版本中，你通常应使用基于 `NSURL` 的 API 来执行与文件相关的操作。下面的代码片段展示了：给定一个包含文件路径的 URL，如何确定文件名和路径扩展名，如何移除文件名以确定包含该文件的目录，以及如何创建一个新的文件 URL，其中原始文件名前面加上了“Copy of”。（例如，如果原始路径是 `/Users/me/MyFile.txt`，新路径将是 `/Users/me/Copy of MyFile.txt`。）

```objc
NSURL *url = <#URL containing a file path#>;

NSString *extension = [url pathExtension];
NSString *fileName = [[url lastPathComponent] stringByDeletingPathExtension];
NSString *copyFileName = [@"Copy of " stringByAppendingString:fileName];

NSURL *copyURL = [url URLByDeletingLastPathComponent];
copyURL = [copyURL URLByAppendingPathComponent:copyFileName];
copyURL = [copyURL URLByAppendingPathExtension:extension];
```

（要以与 Finder 相同的方式创建文件副本，请参阅[将文件移到废纸篓](File%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg44dalktk42a)。）

下面的代码片段展示了：给定一个包含文件路径的字符串，如何确定文件名和路径扩展名，如何移除文件名以确定包含该文件的目录，以及如何创建一个新路径，其中原始文件名前面加上了“Copy of”。（例如，如果原始路径是 `/Users/me/MyFile.txt`，新路径将是 `/Users/me/Copy of MyFile.txt`。）

```objc
NSString *path = <#String containing a file path#>;

NSString *extension = [path pathExtension];
NSString *fileName = [[path lastPathComponent] stringByDeletingPathExtension];
NSString *copyFileName = [@"Copy of " stringByAppendingString:fileName];

NSString *copyPath = [path stringByDeletingLastPathComponent];
copyPath = [copyPath stringByAppendingPathComponent:copyFileName];
copyPath = [copyPath stringByAppendingPathExtension:extension];
```

（要以与 Finder 相同的方式创建文件副本，请参阅[复制文件](File%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg44dalktk43a)。）

Mac OS X 和 iOS 定义了许多标准目录——例如用于存放用户文稿或系统框架的目录。显然，其中一些目录的位置——比如用户的文稿目录——并不是固定的（它取决于当前用户）；不过，一般来说你也不应该依赖其他目录（例如系统框架目录）在不同版本的操作系统中保持相同的位置。因此，不要硬编码目录路径，而应该使用可以帮助你在文件系统中定位标准目录的函数或方法。

Cocoa 提供了以下函数，可以直接返回少数几个标准目录的路径字符串：

|  |  |
| --- | --- |
| [NSHomeDirectory](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSHomeDirectory) |  |
| [NSHomeDirectoryForUser](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSHomeDirectoryForUser) |  |
| [NSTemporaryDirectory](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSTemporaryDirectory) |  |

你可以将返回值与 `NSString` 的路径工具方法结合使用来创建其他路径，例如：

```objc
NSString *path = [NSHomeDirectory() stringByAppendingPathComponent:@"MyFile.txt"];
```

对于其他标准目录，你可以使用 [NSSearchPathForDirectoriesInDomains](https://developer.apple.com/documentation/foundation/1414224-nssearchpathfordirectoriesindoma) 函数（它以 `NSString` 对象的形式返回路径），或者——在 Mac OS X v10.6 及更高版本中——使用 [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager) 的 [URLsForDirectory:inDomains:](https://developer.apple.com/documentation/foundation/nsfilemanager/1407726-urlsfordirectory) 和 [URLForDirectory:inDomain:appropriateForURL:create:error:](https://developer.apple.com/documentation/foundation/filemanager/1407693-url) 方法（它们返回 URL）。该函数和这些方法使用常量来标识你感兴趣的目录。常量有两种类型：

- [NSSearchPathDirectory](https://developer.apple.com/documentation/foundation/nssearchpathdirectory) 枚举中的常量，用于标识目录的名称或类型（例如 `Library`、`Documents` 或 `Applications`）；例如 [NSDocumentDirectory](https://developer.apple.com/documentation/foundation/nssearchpathdirectory/nsdocumentdirectory)、[NSDesktopDirectory](https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory/desktopdirectory) 和 [NSLibraryDirectory](https://developer.apple.com/documentation/foundation/nssearchpathdirectory/nslibrarydirectory)。
- [NSSearchPathDomainMask](https://developer.apple.com/documentation/foundation/nssearchpathdomainmask) 枚举中的位掩码常量，用于标识文件系统域（User、System、Local、Network）或所有域；例如 [NSUserDomainMask](https://developer.apple.com/documentation/foundation/nssearchpathdomainmask/nsuserdomainmask) 和 [NSLocalDomainMask](https://developer.apple.com/documentation/foundation/filemanager/searchpathdomainmask/1417507-localdomainmask)。

一般来说，如果参数隐含多个位置，`NSSearchPathForDirectoriesInDomains` 和 `URLsForDirectory:inDomains:` 可能会返回多个值。不过，你不应该对返回路径的数量做任何假设。某些域或位置可能随时间推移而被废弃，也可能新增其他域或位置（同时保留旧的）；无论哪种情况，返回数组中的路径数量都可能增加或减少。如果你想枚举所有文件，只需查看所有返回值；如果你只是想把一个文件复制或移动到某个位置，并且返回了多个路径，就使用数组中的第一个。

在 Mac OS X v10.6 及更高版本中，你可以使用 [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager) 对象来定位标准系统目录。它的方法返回的是 `NSURL` 对象，而不是基于字符串的路径。

[URLsForDirectory:inDomains:](https://developer.apple.com/documentation/foundation/nsfilemanager/1407726-urlsfordirectory) 与 `NSSearchPathForDirectoriesInDomains` 类似。你指定想要查找的目录类型和域，该方法返回一个 URL 数组。下面的示例说明了如何使用该方法获取当前用户 Documents 目录的 URL：

```objc
NSFileManager *fileManager = [NSFileManager defaultManager];
NSArray *urls = [fileManager URLsForDirectory:NSDocumentDirectory inDomains:NSUserDomainMask];
if ([paths count] > 0) {
    NURL *userDocumentsURL = [urls objectAtIndex:0];
    // Implementation continues...
```

`URLsForDirectory:inDomains:` 只是返回相应目录的 URL，并不保证该目录存在。如果你想执行诸如向目录写入数据之类的操作，可能需要先创建它。

[URLForDirectory:inDomain:appropriateForURL:create:error:](https://developer.apple.com/documentation/foundation/filemanager/1407693-url) 是 [FSFindFolder](https://developer.apple.com/documentation/coreservices/1389059-fsfindfolder) 基于 URL 的替代方法。你可以为特定用途指定并可选地创建一个目录（例如用于替换磁盘上的某个项目，或某个特定的 Library 目录）。你只能传入 [NSSearchPathDomainMask](https://developer.apple.com/documentation/foundation/nssearchpathdomainmask) 枚举中的一个值，且不能传入 [NSAllDomainsMask](https://developer.apple.com/documentation/foundation/nssearchpathdomainmask/nsalldomainsmask)。

下面的示例说明了如何使用 [NSSearchPathForDirectoriesInDomains](https://developer.apple.com/documentation/foundation/1414224-nssearchpathfordirectoriesindoma) 函数来查找当前用户的 Documents 目录：


```objc
NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
if ([paths count] > 0) {
    NSString *userDocumentsPath = [paths objectAtIndex:0];
    // Implementation continues...
```

`NSSearchPathForDirectoriesInDomains` 只是返回相应目录的路径，并不保证该目录存在。如果你想执行诸如向目录写入数据之类的操作，可能需要先创建它。

构造一个指向文件的路径名并不保证该路径上存在文件。指定一个路径会出现以下几种可能：

- 该路径上存在一个文件。
- 该路径上存在一个指向文件的链接。
- 该路径上存在一个失效的链接。
- 该路径上不存在任何文件。

如果路径名指定了一个有效的文件或链接，你可以使用 `NSFileManager` 的 [attributesOfItemAtPath:error:](https://developer.apple.com/documentation/foundation/nsfilemanager/1410452-attributesofitematpath) 方法获取该文件的信息（参阅[获取和设置文件属性](Information%20about%20Files%20and%20Volumes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tanryfvjvomq)）。不过这个方法不会跟随链接。你可以先调用 [destinationOfSymbolicLinkAtPath:error:](https://developer.apple.com/documentation/foundation/filemanager/1415161-destinationofsymboliclink)，然后再调用 [attributesOfItemAtPath:error:](https://developer.apple.com/documentation/foundation/nsfilemanager/1410452-attributesofitematpath)。在 Mac OS X v10.6 及更高版本中，你可以使用 `NSURL` 的 [URLByResolvingSymlinksInPath](https://developer.apple.com/documentation/foundation/nsurl/1415965-resolvingsymlinksinpath) 和 [resourceValuesForKeys:error:](https://developer.apple.com/documentation/foundation/nsurl/1417657-resourcevalues) 方法（参阅[获取和设置文件属性](Information%20about%20Files%20and%20Volumes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tanryfvjvomq)）。

[下一页](File%20Management.md)[上一页](File%20Management%20Classes.md)
