---
title: 属性列表编程指南
apple_id: 10000048i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/SerializePlist/SerializePlist.html
archived_at: '2026-07-15T07:18:03.508425Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [属性列表编程指南](Introduction%20to%20Property%20Lists.md)


[下一页](Reading%20and%20Writing%20Property-List%20Data.md)[上一页](Understanding%20XML%20Property%20Lists.md)

# 序列化属性列表

使用 [NSPropertyListSerialization](https://developer.apple.com/documentation/foundation/nspropertylistserialization) 类或 Property List Services（Core Foundation），你可以把运行时（对象）形式的属性列表序列化成可存储在文件系统中的静态表示；之后你还可以把这个静态表示反序列化回原来的属性列表对象。属性列表序列化会自动处理不同处理器架构上的字节序问题——例如，你可以在基于 Intel 的 Macintosh 上正确读取在基于 PowerPC 的 Macintosh 上创建的二进制属性列表。

属性列表序列化 API 既可以把属性列表对象图保存为二进制数据，也可以保存为 XML 属性列表。关于 XML 属性列表和二进制属性列表各自的优缺点，请参阅[属性列表的表示形式](About%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgaytaljugy3tcoi)。

[NSPropertyListSerialization](https://developer.apple.com/documentation/foundation/nspropertylistserialization) 类（从 OS X v10.2 起可用）提供了以两种主要支持格式（XML 和二进制）保存与恢复属性列表的方法。要以 XML 格式保存属性列表，调用 [dataFromPropertyList:format:errorDescription:](https://developer.apple.com/documentation/foundation/nspropertylistserialization/1416061-datafrompropertylist) 方法，并把第二个参数指定为 [NSPropertyListXMLFormat_v1_0](https://developer.apple.com/documentation/foundation/propertylistserialization/propertylistformat/xml)；要以二进制格式保存，则改为指定 [NSPropertyListBinaryFormat_v1_0](https://developer.apple.com/documentation/foundation/propertylistserialization/propertylistformat/binary)。

清单 5-1 把一个属性列表对象图保存为应用程序 bundle 中的 XML 属性列表。

__清单 5-1__  把属性列表保存为 XML 属性列表（Objective-C）

```objc
id plist;       // 假设这个属性列表已经存在。
NSString *path = [[NSBundle mainBundle] pathForResource:@"Data" ofType:@"plist"];
NSData *xmlData;
NSString *error;

xmlData = [NSPropertyListSerialization dataFromPropertyList:plist
                                       format:NSPropertyListXMLFormat_v1_0
                                       errorDescription:&error];
if(xmlData) {
    NSLog(@"No error creating XML data.");
    [xmlData writeToFile:path atomically:YES];
}
else {
    NSLog(error);
    [error release];
}
```

由于你无法把属性列表保存为旧式（OpenStep）格式，这个方法的 format 参数只有两个有效取值：[NSPropertyListXMLFormat_v1_0](https://developer.apple.com/documentation/foundation/propertylistserialization/propertylistformat/xml) 和 [NSPropertyListBinaryFormat_v1_0](https://developer.apple.com/documentation/foundation/propertylistserialization/propertylistformat/binary)。`dataFromPropertyList:format:errorDescription:` 返回的 [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) 对象封装了 XML 或二进制数据。随后你可以调用 [writeToFile:atomically:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/instm/NSData/writeToFile:atomically:) 或 [writeToURL:atomically:](https://developer.apple.com/documentation/foundation/nsdata/1415134-writetourl) 方法把这些数据存到文件系统中。

要通过反序列化从一个数据对象恢复属性列表，调用 `NSPropertyListSerialization` 类的类方法 [propertyListFromData:mutabilityOption:format:errorDescription:](https://developer.apple.com/documentation/foundation/propertylistserialization/1411993-propertylistfromdata)，把数据对象传进去。清单 5-2 从位于 `path` 的文件创建了一个不可变的属性列表：

__清单 5-2__  恢复属性列表（Objective-C）

```objc
NSString *path = [[NSBundle mainBundle] pathForResource:@"Data" ofType:@"plist"];
NSData *plistData = [NSData dataWithContentsOfFile:path];
NSString *error;
NSPropertyListFormat format;
id plist;

plist = [NSPropertyListSerialization propertyListFromData:plistData
                                mutabilityOption:NSPropertyListImmutable
                                format:&format
                                errorDescription:&error];
if(!plist){
    NSLog(error);
    [error release];
}
```

反序列化方法的[可变性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectMutability.html#//apple_ref/doc/uid/TP40008195-CH42)选项参数决定反序列化出来的属性列表对象是可变的还是不可变的。你可以指定所有对象都不可变、只有容器对象可变，或者所有对象都可变。除非你有明确的理由要修改反序列化后属性列表中的集合和其他对象，否则请使用不可变选项。它更快，占用的内存也更少。

`propertyListFromData:mutabilityOption:format:errorDescription:` 的最后两个参数是按引用传递的。调用返回时，format 参数中保存的常量表示该属性列表在磁盘上的格式：[NSPropertyListXMLFormat_v1_0](https://developer.apple.com/documentation/foundation/propertylistserialization/propertylistformat/xml)、[NSPropertyListBinaryFormat_v1_0](https://developer.apple.com/documentation/foundation/propertylistserialization/propertylistformat/binary) 或 [NSPropertyListOpenStepFormat](https://developer.apple.com/documentation/foundation/propertylistserialization/propertylistformat/openstep)。如果你不关心格式，可以传入 `NULL`。

如果方法调用返回 `nil`，最后一个参数——错误描述字符串——会说明反序列化失败的原因。

Core Foundation 的 Property List Services 提供了一些序列化函数，它们与“在 Objective-C 中保存和恢复属性列表”一节介绍的 [NSPropertyListSerialization](https://developer.apple.com/documentation/foundation/nspropertylistserialization) 类方法相对应。要从属性列表对象创建 XML 属性列表，调用 [CFPropertyListCreateXMLData](https://developer.apple.com/documentation/corefoundation/1429991-cfpropertylistcreatexmldata) 函数。要从 XML 数据恢复属性列表对象，调用 [CFPropertyListCreateFromXMLData](https://developer.apple.com/documentation/corefoundation/1429995-cfpropertylistcreatefromxmldata) 函数。

清单 5-3 展示了如何创建一个复杂的属性列表、把它转换成 XML、写入磁盘，然后再用保存下来的 XML 重建原来的数据结构。关于使用 CFDictionary 对象的更多信息，请参阅 _[Core Foundation 集合编程主题](../../Core%20Foundation/Collections%20Programming%20Topics%20for%20Core%20Foundation/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdi2i)_。

__清单 5-3__  保存和恢复属性列表数据（Core Foundation）

```c
#include <CoreFoundation/CoreFoundation.h>

#define kNumKids 2
#define kNumBytesInPic 10

CFDictionaryRef CreateMyDictionary( void );
CFPropertyListRef CreateMyPropertyListFromFile( CFURLRef fileURL );
void WriteMyPropertyListToFile( CFPropertyListRef propertyList,
            CFURLRef fileURL );

int main () {
   CFPropertyListRef propertyList;
   CFURLRef fileURL;

   // 构造一个复杂的字典对象；
   propertyList = CreateMyDictionary();

   // 创建一个 URL，指定我们将要创建的、
   // 用于保存 XML 数据的文件。
   fileURL = CFURLCreateWithFileSystemPath( kCFAllocatorDefault,
               CFSTR("test.txt"),       // 文件路径名
               kCFURLPOSIXPathStyle,    // 按 POSIX 路径解释
               false );                 // 它是目录吗？

   // 把属性列表写入文件。
   WriteMyPropertyListToFile( propertyList, fileURL );
   CFRelease(propertyList);

   // 从文件重新创建属性列表。
   propertyList = CreateMyPropertyListFromFile( fileURL );

   // 释放我们持有引用的所有对象。
   CFRelease(propertyList);
   CFRelease(fileURL);
   return 0;
}

CFDictionaryRef CreateMyDictionary( void ) {
   CFMutableDictionaryRef dict;
   CFNumberRef            num;
   CFArrayRef             array;
   CFDataRef              data;

   int                    yearOfBirth;
   CFStringRef            kidsNames[kNumKids];

   // 用假数据代替 John Doe 的照片。
   const unsigned char pic[kNumBytesInPic] = {0x3c, 0x42, 0x81,
            0xa5, 0x81, 0xa5, 0x99, 0x81, 0x42, 0x3c};

   // 定义一些数据。
   kidsNames[0] = CFSTR("John");
   kidsNames[1] = CFSTR("Kyra");

   yearOfBirth = 1965;

   // 创建一个用于保存这些数据的字典。
   dict = CFDictionaryCreateMutable( kCFAllocatorDefault,
            0,
            &kCFTypeDictionaryKeyCallBacks,
            &kCFTypeDictionaryValueCallBacks );

   // 把各个数据项放进字典。
   // 由于这些值在放入字典时会被保留，
   //  我们可以在这里释放所有已分配的对象。

   CFDictionarySetValue( dict, CFSTR("Name"), CFSTR("John Doe") );

   CFDictionarySetValue( dict,
            CFSTR("City of Birth"),
            CFSTR("Springfield") );

   num = CFNumberCreate( kCFAllocatorDefault,
            kCFNumberIntType,
            &yearOfBirth );
   CFDictionarySetValue( dict, CFSTR("Year Of Birth"), num );
   CFRelease( num );

   array = CFArrayCreate( kCFAllocatorDefault,
               (const void **)kidsNames,
               kNumKids,
               &kCFTypeArrayCallBacks );
   CFDictionarySetValue( dict, CFSTR("Kids Names"), array );
   CFRelease( array );

   array = CFArrayCreate( kCFAllocatorDefault,
               NULL,
               0,
               &kCFTypeArrayCallBacks );
   CFDictionarySetValue( dict, CFSTR("Pets Names"), array );
   CFRelease( array );

   data = CFDataCreate( kCFAllocatorDefault, pic, kNumBytesInPic );
   CFDictionarySetValue( dict, CFSTR("Picture"), data );
   CFRelease( data );

   return dict;
}

void WriteMyPropertyListToFile( CFPropertyListRef propertyList,
            CFURLRef fileURL ) {
   CFDataRef xmlData;
   Boolean status;
   SInt32 errorCode;

   // 把属性列表转换成 XML 数据。
   xmlData = CFPropertyListCreateXMLData( kCFAllocatorDefault, propertyList );

   // 把 XML 数据写入文件。
   status = CFURLWriteDataAndPropertiesToResource (
               fileURL,                  // 要使用的 URL
               xmlData,                  // 要写入的数据
               NULL,
               &errorCode);

   CFRelease(xmlData);
}

CFPropertyListRef CreateMyPropertyListFromFile( CFURLRef fileURL ) {
   CFPropertyListRef propertyList;
   CFStringRef       errorString;
   CFDataRef         resourceData;
   Boolean           status;
   SInt32            errorCode;

   // 读取 XML 文件。
   status = CFURLCreateDataAndPropertiesFromResource(
               kCFAllocatorDefault,
               fileURL,
               &resourceData,            // 用于存放文件数据的位置
               NULL,
               NULL,
               &errorCode);

   // 用这些 XML 数据重建字典。
   propertyList = CFPropertyListCreateFromXMLData( kCFAllocatorDefault,
               resourceData,
               kCFPropertyListImmutable,
               &errorString);

   if (resourceData) {
        CFRelease( resourceData );
    } else {
        CFRelease( errorString );
    }
   return propertyList;
}
```

关于 `CFPropertyListCreateFromXMLData` 的可变性选项参数的讨论，请参阅[在 Objective-C 中保存和恢复属性列表](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2jninedolktk42a)中对 [propertyListFromData:mutabilityOption:format:errorDescription:](https://developer.apple.com/documentation/foundation/propertylistserialization/1411993-propertylistfromdata) 方法相应参数的说明。

清单 5-4 展示了[清单 5-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2jninedolktk4zq) 中创建的 `xmlData` 如果打印到屏幕上会是什么样子。

__清单 5-4__  示例程序生成的 XML 文件内容

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
        "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Year Of Birth</key>
    <integer>1965</integer>
    <key>Pets Names</key>
    <array/>
    <key>Picture</key>
    <data>
        PEKBpYGlmYFCPA==
    </data>
    <key>City of Birth</key>
    <string>Springfield</string>
    <key>Name</key>
    <string>John Doe</string>
    <key>Kids Names</key>
    <array>
        <string>John</string>
        <string>Kyra</string>
    </array>
</dict>
</plist>
```


Cocoa 内部使用 Core Foundation 的属性列表 API 来读写 XML 属性列表。在某些情况下，你可能希望在 Objective-C 的 Cocoa 应用程序中直接使用这套 API。例如，如果你想把 `NSArray` 或 `NSDictionary` 之外的某个类的实例作为 XML plist 的根对象保存下来，目前最简单的办法就是通过 Property List Services。这个过程之所以简单，是因为 Cocoa 对象可以与对应的 Core Foundation 类型相互转换。Cocoa 与 Core Foundation 对象类型之间的这种转换称为_免费桥接_（toll-free bridging）。

要从属性列表对象创建 XML 属性列表，调用 [CFPropertyListCreateXMLData](https://developer.apple.com/documentation/corefoundation/1429991-cfpropertylistcreatexmldata) 函数。下面这段代码片段把属性列表 `plist` 保存到位于 `path` 的文件中：

```objc
NSString *path = [NSString stringWithFormat:@"%@/MyData.plist", NSTemporaryDirectory()];
id plist;       // 假设这是一个有效的属性列表。
NSData *xmlData;

xmlData = (NSData *)CFPropertyListCreateXMLData(kCFAllocatorDefault,
                                               (CFPropertyListRef)plist);
[xmlData writeToFile:path atomically:YES];
[xmlData release];
```

要从 XML 数据恢复属性列表对象，调用 [CFPropertyListCreateFromXMLData](https://developer.apple.com/documentation/corefoundation/1429995-cfpropertylistcreatefromxmldata) 函数。下面这段代码片段从位于 `path` 的 XML plist 文件恢复属性列表，其容器可变而叶子节点不可变：

```objc
NSString *path = [NSString stringWithFormat:@"%@/MyData.plist", NSTemporaryDirectory()];
NSString *errorString;
NSData *xmlData;
id plist;

xmlData = [NSData dataWithContentsOfFile:path];
plist = (id)CFPropertyListCreateFromXMLData(kCFAllocatorDefault,
                 (CFDataRef)xmlData, kCFPropertyListMutableContainers,
                 (CFStringRef *)&errorString);
```

[下一页](Reading%20and%20Writing%20Property-List%20Data.md)[上一页](Understanding%20XML%20Property%20Lists.md)

