---
title: '在 App 启动时打开上一个文稿 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/05/open-previous-document-on-application.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:3decac9ef719a434'
translated: true
---

> 原文：[Open the previous document on application startup | Cocoa with Love](https://www.cocoawithlove.com/2008/05/open-previous-document-on-application.html)　·　Cocoa with Love (Matt Gallagher)

配置你的 App，使其在启动时打开最近使用的文稿，比你想象的要简单。以下是一个快速解决方案，附带一些可以直接插入到你的 App 中的代码。

## 用最近文稿替代“无标题”文稿

如果用户可能在多次 App 会话中编辑同一份文稿，那么在 App 启动时自动打开上次编辑的文稿是一个有用的选项。

为了方便我们实现这一点，Mac OS X 会自动记住最近打开的十份文稿。

我们只需三个步骤即可实现这一功能：

- 阻止默认的“无标题”文稿打开
- 根据共享的 `NSDocumentController` 的报告，打开最近使用的文稿
- 允许在启动后打开“无标题”文稿

## 全部在 App 委托中完成

App 的委托（delegate）是执行此工作的合适位置，大部分工作将在委托方法 `applicationShouldOpenUntitledFile:` 中完成。

通常，此方法返回 `YES`。即使我们希望在启动时打开最近使用的文稿，我们也会希望此方法在启动后返回 `YES`。

但我们不能直接询问 `NSApplication` 是否正在启动，因此我们必须保持一个标志 `applicationHasStarted`，它应在委托的构造方法中初始化为 `NO`，并在 `applicationDidFinishLaunching:` 中设置为 `YES`。在下面的代码示例中，我假设你已经设置了此行为，因此没有显式展示它。

因此，在 `applicationShouldOpenUntitledFile:` 的方法体内，如果 `applicationHasStarted` 是 `NO`，我们向共享的 `NSDocumentController` 请求最近使用的文稿，获取该文稿的 URL 并打开它，然后从 `applicationShouldOpenUntitledFile:` 返回 `NO`，以防止出现无标题文稿。

## 解决方案

```objc
- (BOOL)applicationShouldOpenUntitledFile:(NSApplication *)sender
{
    // 在启动时，当被要求打开无标题文件，则改为打开上次
    // 打开的文稿。
    if (!applicationHasStarted)
    {
        // 获取最近的文稿
        NSDocumentController *controller =
            [NSDocumentController sharedDocumentController];
        NSArray *documents = [controller recentDocumentURLs];
        
        // 如果有最近的文稿，则尝试打开它。
        if ([documents count] > 0)
        {
            NSError *error = nil;
            [controller
                openDocumentWithContentsOfURL:[documents objectAtIndex:0]
                display:YES error:&error];
            
            // 如果没有错误，则阻止无标题文稿出现。
            if (error == nil)
            {
                return NO;
            }
        }
    }
    
    return YES;
}
```
