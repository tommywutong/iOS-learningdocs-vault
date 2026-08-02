---
title: 字符串编程指南
apple_id: 10000035i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/ManipulatingPaths.html
archived_at: '2026-07-15T07:19:31.190425Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [字符串编程指南](Introduction%20to%20String%20Programming%20Guide.md)


[下一页](Drawing%20Strings.md)[上一页](Scanners.md)

# 文件路径的字符串表示

[NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) 提供了一套丰富的方法，可以把字符串当作文件系统路径来操作。你可以提取路径中的目录、文件名和扩展名，展开波浪号表达式（例如“`~me`”）或为用户的主目录创建一个波浪号表达式，还可以清理路径中的符号链接、冗余斜杠，以及对“.”（当前目录）和“..”（父目录）的引用。

`NSString` 以通用方式表示路径，用“/”作为路径分隔符、“.”作为扩展名分隔符。接受字符串作为路径参数的方法会在需要时把这种通用表示转换为相应系统的正确形式。在具有隐式根目录的系统上，绝对路径以路径分隔符开头，或者以波浪号表达式（“`~/...`”或“`~user/...`”）开头。在必须指定设备的场合，你可以自己指定设备（这会引入系统依赖），也可以让字符串对象添加默认设备。

你可以使用 [stringByStandardizingPath](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/stringByStandardizingPath) 创建路径的标准化表示。它会完成若干项工作，包括：

- 展开开头的波浪号表达式；
- 把空的路径组件以及对当前目录的引用（“//”和“/./”）归约为单个路径分隔符；
- 在绝对路径中，把对父目录（“..”）的引用解析为真正的父目录；

例如：

```objc
NSString *path = @"/usr/bin/./grep";
NSString *standardizedPath = [path stringByStandardizingPath];
// standardizedPath: /usr/bin/grep

path = @"~me";
standardizedPath = [path stringByStandardizingPath];
// standardizedPath（假设采用常规的命名方案）: /Users/Me

path = @"/usr/include/objc/..";
standardizedPath = [path stringByStandardizingPath];
// standardizedPath: /usr/include

path = @"/private/usr/include";
standardizedPath = [path stringByStandardizingPath];
// standardizedPath: /usr/include
```


下面的例子说明如何使用 `NSString` 的路径工具方法以及其他 Cocoa 函数来获取用户目录。

```objc
// 假设用户的主目录存放在 /Users 下

NSString *meHome = [@"~me" stringByExpandingTildeInPath];
// meHome = @"/Users/me"

NSString *mePublic = [@"~me/Public" stringByExpandingTildeInPath];
// mePublic = @"/Users/me/Public"
```

你可以分别用 [NSHomeDirectory](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSHomeDirectory) 和 [NSHomeDirectoryForUser](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSHomeDirectoryForUser) 获取当前用户和指定用户的主目录：

```objc
NSString *currentUserHomeDirectory = NSHomeDirectory();
NSString *meHomeDirectory = NSHomeDirectoryForUser(@"me");
```

注意，要定位当前用户的标准目录，通常应当使用 [NSSearchPathForDirectoriesInDomains](https://developer.apple.com/documentation/foundation/1414224-nssearchpathfordirectoriesindoma) 函数。例如，不要这样写：

```objc
NSString *documentsDirectory =
                [NSHomeDirectory() stringByAppendingPathComponent:@"Documents"];
```

而应当这样写：

```objc
NSString *documentsDirectory;
NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
if ([paths count] > 0) {
    documentsDirectory = [paths objectAtIndex:0];
}
```


`NSString` 提供了一套丰富的方法，可以把字符串当作文件系统路径来操作，例如：

- [pathExtension](https://developer.apple.com/documentation/foundation/nsstring/1407801-pathextension)
- [stringByDeletingPathExtension](https://developer.apple.com/documentation/foundation/nsstring/1418214-stringbydeletingpathextension)
- [stringByDeletingLastPathComponent](https://developer.apple.com/documentation/foundation/nsstring/1411141-stringbydeletinglastpathcomponen)

使用这些方法以及 _[NSString 类参考](https://developer.apple.com/documentation/foundation/nsstring)_ 中介绍的相关方法，你可以提取路径中的目录、文件名和扩展名，如下面的例子所示。

```objc
NSString *documentPath = @"~me/Public/Demo/readme.txt";

NSString *documentDirectory = [documentPath stringByDeletingLastPathComponent];
// documentDirectory = @"~me/Public/Demo"

NSString *documentFilename = [documentPath lastPathComponent];
// documentFilename = @"readme.txt"

NSString *documentExtension = [documentPath pathExtension];
// documentExtension = @"txt"
```


你可以使用 [completePathIntoString:caseSensitive:matchesIntoArray:filterTypes:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/completePathIntoString:caseSensitive:matchesIntoArray:filterTypes:) 查找文件名的可能补全形式。例如，假设目录 `~/Demo` 中包含以下文件：

`ReadMe.txt readme.html readme.rtf recondite.txt test.txt`

那么你可以按如下方式找出路径 `~/Demo/r` 的所有可能补全：

```objc
NSString *partialPath = @"~/Demo/r";
NSString *longestCompletion;
NSArray *outputArray;

unsigned allMatches = [partialPath completePathIntoString:&longestCompletion
    caseSensitive:NO
    matchesIntoArray:&outputArray
    filterTypes:nil];

// allMatches = 3
// longestCompletion = @"~/Demo/re"
// outputArray = (@"~/Demo/readme.html", "~/Demo/readme.rtf", "~/Demo/recondite.txt")
```

你可以按如下方式找出路径 `~/Demo/r` 中扩展名为“.txt”或“.rtf”的补全形式：

```objc
NSArray *filterTypes = @[@"txt", @"rtf"];

unsigned textMatches = [partialPath completePathIntoString:&outputName
    caseSensitive:NO
    matchesIntoArray:&outputArray
    filterTypes:filterTypes];
// allMatches = 2
// longestCompletion = @"~/Demo/re"
// outputArray = (@"~/Demo/readme.rtf", @"~/Demo/recondite.txt")
```

[下一页](Drawing%20Strings.md)[上一页](Scanners.md)

