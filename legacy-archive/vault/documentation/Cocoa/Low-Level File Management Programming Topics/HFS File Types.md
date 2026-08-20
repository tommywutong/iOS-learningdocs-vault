---
title: 底层文件管理编程主题
apple_id: 10000055i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LowLevelFileMgmt/Articles/HFSFileTypes.html
archived_at: '2026-07-15T07:16:36.109554Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [底层文件管理编程主题](Introduction%20to%20Low-Level%20File%20Management%20Programming%20Topics.md)


[下一页](Document%20Revision%20History.md)[上一页](File%20Handle.md)

# HFS 文件类型

HFS 类型代码已被文件 UTI 取代（参阅 _[Uniform Type Identifiers Overview](../../File%20Management/Uniform%20Type%20Identifiers%20Overview/Introduction%20to%20Uniform%20Type%20Identifiers%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmjz)_）。本文是为仍需使用 HFS 类型代码的读者提供的。

HFS 文件类型代码和创建者代码由一个 32 位无符号整数（`OSType`）指定，通常表示为四个字符，例如 `GIFf` 或 `MooV`。当 Mac OS X 的编译器在单引号内遇到四个字符（例如 `'GIFf'`）时，会自动将四字符表示转换为整数表示。

```objc
OSType aFileType = 'GIFf';
```

你可以使用 `NSFileManager` 操作 HFS 类型代码和创建者代码，方法如下：

- 要获取 HFS 类型代码和创建者代码，使用 [attributesOfItemAtPath:error:](https://developer.apple.com/documentation/foundation/nsfilemanager/1410452-attributesofitematpath) 获取包含文件属性的字典，然后分别使用 `NSDictionary` 的 [fileHFSTypeCode](https://developer.apple.com/documentation/foundation/nsdictionary/1417215-filehfstypecode) 和 [fileHFSCreatorCode](https://developer.apple.com/documentation/foundation/nsdictionary/1415065-filehfscreatorcode) 方法。
- 要设置类型代码和创建者代码，使用 `NSFileManager` 的 [setAttributes:ofItemAtPath:error:](https://developer.apple.com/documentation/foundation/nsfilemanager/1413667-setattributes) 方法，传入一个包含 `NSFileHFSCreatorCode` 和 `NSFileHFSTypeCode` 键的字典。这些键的值应该是保存 `OSType` 值的 `NSNumber` 对象，例如：

```objc
NSNumber *aFileType = [NSNumber numberWithUnsignedLong:'GIFf'];
```

Cocoa 的其他部分（例如 `NSOpenPanel`）传统上只能通过文件名扩展名（如 `"gif"` 或 `"mov"`）来指定文件类型。由于数据类型存在冲突——字符串与整数——这些基于文件名扩展名的 API 不能直接使用 HFS 文件类型。不过这些方法可以接受已正确编码为 `NSString` 的 HFS 文件类型。

Foundation Kit 定义了以下函数，用于在经典 HFS 文件类型和编码后的字符串之间进行转换：

|  |  |
| --- | --- |
| [NSFileTypeForHFSTypeCode](https://developer.apple.com/documentation/foundation/1412112-nsfiletypeforhfstypecode) |  |
| [NSHFSTypeCodeFromFileType](https://developer.apple.com/documentation/foundation/1415466-nshfstypecodefromfiletype) |  |
| [NSHFSTypeOfFile](https://developer.apple.com/documentation/foundation/1414326-nshfstypeoffile) |  |

前两个函数在 HFS 文件类型和编码后的 HFS 字符串之间进行转换。最后一个函数返回特定文件的编码 HFS 字符串。

举例来说，在指定 `NSOpenPanel` 对象可以打开的文件类型时，你可以按如下方式创建文件类型数组，以包含任何具有相应 HFS 类型代码的文本文档：

```objc
NSArray *fileTypes = [NSArray arrayWithObjects: @"txt", @"text",
                        NSFileTypeForHFSTypeCode('TEXT'), nil];
```

当你需要判断某个特定文件的 HFS 文件类型或扩展名是否属于一组 HFS 文件类型和扩展名时，可以使用类似下面这样的函数：

```objc
BOOL FileIsValid(NSString *fullFilePath)
{
    // Create an array of strings specifying valid extensions and HFS file types.
    NSArray *fileTypes = [NSArray arrayWithObjects:
                                           @"txt",
                                           @"text",
                                           NSFileTypeForHFSTypeCode('TEXT'),
                                           nil];

    // Try to get the HFS file type as a string.
    NSString *fileType = NSHFSTypeOfFile(fullFilePath);

    if ([fileType isEqualToString:@"''"])
    {
        // No HFS type; get the extension instead.
        fileType = [fullFilePath pathExtension];
    }

    return [fileTypes containsObject:fileType];
}
```

[下一页](Document%20Revision%20History.md)[上一页](File%20Handle.md)
