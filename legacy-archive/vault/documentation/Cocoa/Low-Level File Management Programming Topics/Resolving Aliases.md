---
title: 底层文件管理编程主题
apple_id: 10000055i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LowLevelFileMgmt/Articles/ResolvingAliases.html
archived_at: '2026-07-15T07:16:36.922324Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [底层文件管理编程主题](Introduction%20to%20Low-Level%20File%20Management%20Programming%20Topics.md)


[下一页](File%20Handle.md)[上一页](Working%20with%20the%20Contents%20of%20a%20Directory.md)

# 解析替身

与符号链接不同，Mac OS X 的替身（alias）不会由 Cocoa 自动处理。本文说明如何解析路径中的替身。

由 `NSOpenPanel` 等 Cocoa 类返回的路径可能包含替身引用，使用前必须先解析。要解析 `NSString` 中路径里的替身，你需要先将字符串转换为 URL，再将 URL 转换为 FSRef，解析替身，然后反向执行这一系列转换，得到另一个 `NSString`。要执行这些必要的转换，你需要使用 `<CoreServices/CoreServices.h>` 中提供的 URL 和替身服务。下面的代码片段使用 [FSResolveAliasFile](https://developer.apple.com/documentation/coreservices/1444372-fsresolvealiasfile) 来解析 `path` 中的所有替身，并将解析后的路径存入 `resolvedPath`：

```objc
NSString *path = <#Get a suitable path#>;
NSString *resolvedPath = nil;

CFURLRef url = CFURLCreateWithFileSystemPath
                   (kCFAllocatorDefault, (CFStringRef)path, kCFURLPOSIXPathStyle, NO);
if (url != NULL)
{
    FSRef fsRef;
    if (CFURLGetFSRef(url, &fsRef))
    {
        Boolean targetIsFolder, wasAliased;
        OSErr err = FSResolveAliasFile (&fsRef, true, &targetIsFolder, &wasAliased);
        if ((err == noErr) && wasAliased)
        {
            CFURLRef resolvedUrl = CFURLCreateFromFSRef(kCFAllocatorDefault, &fsRef);
            if (resolvedUrl != NULL)
            {
                resolvedPath = (NSString*)
                        CFURLCopyFileSystemPath(resolvedUrl, kCFURLPOSIXPathStyle);
                CFRelease(resolvedUrl);
            }
        }
    }
    CFRelease(url);
}

if (resolvedPath == nil)
{
    resolvedPath = [[NSString alloc] initWithString:path];
}
```

`FSResolveAliasFile` 的第二个参数指定你是否希望该函数解析替身链中的所有替身（例如，一个替身文件指向另一个替身文件，依此类推），直到到达目标文件为止。

[下一页](File%20Handle.md)[上一页](Working%20with%20the%20Contents%20of%20a%20Directory.md)
