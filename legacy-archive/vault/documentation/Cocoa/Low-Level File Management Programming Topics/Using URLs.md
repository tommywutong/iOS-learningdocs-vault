---
title: 底层文件管理编程主题
apple_id: 10000055i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LowLevelFileMgmt/Articles/FileManagementNSURL.html
archived_at: '2026-07-15T07:16:35.603985Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [底层文件管理编程主题](Introduction%20to%20Low-Level%20File%20Management%20Programming%20Topics.md)


[下一页](Working%20with%20the%20Contents%20of%20a%20Directory.md)[上一页](Information%20about%20Files%20and%20Volumes.md)

# 使用 URL

本文介绍在 Mac OS X v10.6 及更高版本中使用 `NSURL` 可以执行的各种操作。

有时你需要引用一个用户可能在应用程序运行期间移动的文件。在这种情况下，基于路径的 URL 就没有用了，因为用户移动文件后路径会改变，而 URL 仍会指向原始位置。文件引用 URL（file reference URL）提供了一种通过文件 ID 跟踪文件的方式。这意味着即使文件名或其在文件系统中的位置发生变化，该引用仍然有效。

你可以使用 [fileReferenceURL](https://developer.apple.com/documentation/foundation/nsurl/1408631-filereferenceurl) 方法从现有 URL 创建文件引用 URL：

```objc
NSURL *existingURL = <#A URL for an existing file or directory#>;
NSURL *fileReferenceURL = [existingURL fileReferenceURL];
```

示例中两个 URL 的表示形式是不同的：

```objc
existingURL = file://localhost/Users/me/MyFile.txt
fileReferenceURL = file:///.file/id=6238375.726492
```

不过，标准 URL 和文件引用 URL 都是有效的 URL。

关于文件引用 URL，有两点注意事项：

- `NSDocument` 内部已经使用了文件引用 URL，因此在基于文稿的应用程序中，通常不需要你自己管理它们。
- 你不应该存储或归档文件引用 URL。在操作系统的不同次启动之间，文件的 ID 可能不同。如果你需要存储 URL，请参阅[使用书签和替身](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tanjzfvjvomi)。

你可以使用 [bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:](https://developer.apple.com/documentation/foundation/nsurl/1417795-bookmarkdatawithoptions) 创建 URL 的持久表示。options 参数允许你指定被收藏 URL 的若干方面，包括文件替身信息。（这使你可以在 Mac OS X 10.6 之前的版本上把书签当作替身来读取。）

```objc
NSURL *url = <#Create a URL#>;
NSError *error = nil;
NSData *bookmarkData = [url bookmarkDataWithOptions:NSURLBookmarkCreationSuitableForBookmarkFile
                            includingResourceValuesForKeys:nil
                            relativeToURL:nil
                            error:&error];
if (bookmarkData == nil) {
    // Handle the error...
}
```

如果你使用 [NSURLBookmarkCreationSuitableForBookmarkFile](https://developer.apple.com/documentation/foundation/nsurlbookmarkcreationoptions/nsurlbookmarkcreationsuitableforbookmarkfile) 选项创建书签，随后可以使用类方法 [writeBookmarkData:toURL:options:error:](https://developer.apple.com/documentation/foundation/nsurl/1408532-writebookmarkdata) 从书签创建一个替身文件。

```objc
NSURL *bookmarkURL = <#Create a URL for the bookmark#>;
BOOL ok = [NSURL writeBookmarkData:bookmarkData toURL:bookmarkURL options:0 error:&error];
if (!ok) {
    // Handle the error...
}
```

如果书签 URL 指向一个目录，替身文件将在该目录中创建，其名称来自书签数据中的信息。如果 URL 指向一个文件，替身文件将按照书签 URL 指定的位置和名称创建，并且如果扩展名还不是 `.alias`，则会被改为 `.alias`。

你可以使用 [URLByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:](https://developer.apple.com/documentation/foundation/nsurl/1572035-urlbyresolvingbookmarkdata) 从书签数据重新创建 URL。

[下一页](Working%20with%20the%20Contents%20of%20a%20Directory.md)[上一页](Information%20about%20Files%20and%20Volumes.md)
