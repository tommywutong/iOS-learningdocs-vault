---
title: Core Data 实用工具教程
apple_id: TP40001800
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreData
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataUtilityTutorial/Articles/04_appSupport.html
archived_at: '2026-07-15T07:14:28.927905Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 实用工具教程](Introduction%20to%20Core%20Data%20Utility%20Tutorial.md)


[下一页](Creating%20the%20Core%20Data%20Stack.md)[上一页](Creating%20the%20Managed%20Object%20Model.md)

# 应用程序日志目录

该实用工具需要一个地方来保存持久化存储的文件。本节演示了一种识别、并在必要时创建合适目录的方法。虽然这对该工具来说是一个有用的抽象，但它与 Core Data 本身并无直接关系，因此不再做额外说明。关于定位系统目录的详细信息，请参阅 _[Low-Level File Management Programming Topics](../Low-Level%20File%20Management%20Programming%20Topics/Introduction%20to%20Low-Level%20File%20Management%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tk2i)_。

实现一个函数，用于识别、并在必要时创建一个目录（位于 `~/Library/Logs`——即你主目录下的 Logs 目录），用于保存持久化存储的文件。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)实现并使用 applicationLogDirectory 函数

1. 声明 `applicationLogDirectory()` 函数。

   在主源文件中，`main()` 之前，声明一个返回 `NSURL` 对象的函数 `applicationLogDirectory()`：

```objc
NSURL *applicationLogDirectory();
```
2. 在 `main()` 之后，实现 `applicationLogDirectory()` 函数。

   按如下方式实现 `applicationLogDirectory()` 函数：

```objc
NSURL *applicationLogDirectory() {

    NSString *LOG_DIRECTORY = @"CDCLI";
    static NSURL *ald = nil;

    if (ald == nil) {

        NSFileManager *fileManager = [[NSFileManager alloc] init];
        NSError *error;
        NSURL *libraryURL = [fileManager URLForDirectory:NSLibraryDirectory inDomain:NSUserDomainMask appropriateForURL:nil create:YES error:&error];
        if (libraryURL == nil) {
            NSLog(@"Could not access Library directory\n%@", [error localizedDescription]);
        }
        else {
            ald = [libraryURL URLByAppendingPathComponent:@"Logs"];
            ald = [ald URLByAppendingPathComponent:LOG_DIRECTORY];
            NSDictionary *properties = [ald resourceValuesForKeys:@[NSURLIsDirectoryKey]
                                                            error:&error];
            if (properties == nil) {
                if (![fileManager createDirectoryAtURL:ald withIntermediateDirectories:YES attributes:nil error:&error]) {
                    NSLog(@"Could not create directory %@\n%@", [ald path], [error localizedDescription]);
                    ald = nil;
                }
            }
        }
    }
    return ald;
}
```
3. 

   更新 main 函数，调用 `applicationLogDirectory()` 函数。

   在 `main` 函数中，在调用 `managedObjectModel` 函数之后，调用 `applicationLogDirectory()`；如果返回 `nil`，则退出。

```objc
if (applicationLogDirectory() == nil) {
    exit(1);
}
```


构建并运行该工具。它应该能够无警告地编译通过。应用程序日志目录应该被正确创建，且不应记录任何错误。

[下一页](Creating%20the%20Core%20Data%20Stack.md)[上一页](Creating%20the%20Managed%20Object%20Model.md)
