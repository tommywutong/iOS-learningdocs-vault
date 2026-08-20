---
title: 属性列表编程指南
apple_id: 10000048i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/CreatePropListProgram/CreatePropListProgram.html
archived_at: '2026-07-15T07:18:02.552653Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [属性列表编程指南](Introduction%20to%20Property%20Lists.md)


[下一页](Understanding%20XML%20Property%20Lists.md)[上一页](About%20Property%20Lists.md)

# 以编程方式创建属性列表

你可以把各种类型的属性列表对象嵌套到数组和字典中，从而构建出一个属性列表对象图。以下各节详细说明如何以编程方式做到这一点。

在 Objective-C 中，只要聚合体中的所有对象都派生自 [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary)、[NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray)、[NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString)、[NSDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/cl/NSDate)、[NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) 或 [NSNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/cl/NSNumber) 类，你就可以创建属性列表。清单 3-1 中的代码创建了一个属性列表，它由一个 `NSDictionary` 对象（根对象）构成，其中包含两个字典，每个字典又各自包含一个字符串、一个日期和一个数字数组。

__清单 3-1__  以编程方式创建属性列表（Objective-C）

```objc
        NSMutableDictionary *rootObj = [NSMutableDictionary dictionaryWithCapacity:2];
        NSDictionary *innerDict;
        NSString *name;
        NSDate *dob;
        NSArray *scores;

        scores = [NSArray arrayWithObjects:[NSNumber numberWithInt:6],
            [NSNumber numberWithFloat:4.6], [NSNumber numberWithLong:6.0000034], nil];
        name = @"George Washington";
        dob = [NSDate dateWithString:@"1732-02-17 04:32:00 +0300"];
        innerDict = [NSDictionary dictionaryWithObjects:
            [NSArray arrayWithObjects: name, dob, scores, nil]
            forKeys:[NSArray arrayWithObjects:@"Name", @"DOB", @"Scores"]];
        [rootObj setObject:innerDict forKey:@"Washington"];

        scores = [NSArray arrayWithObjects:[NSNumber numberWithInt:8],
            [NSNumber numberWithFloat:4.9],
            [NSNumber numberWithLong:9.003433], nil];
        name = @"Abraham Lincoln";
        dob = [NSDate dateWithString:@"1809-02-12 13:18:00 +0400"];
        innerDict = [NSDictionary dictionaryWithObjects:
            [NSArray arrayWithObjects: name, dob, scores, nil]
            forKeys:[NSArray arrayWithObjects:@"Name", @"DOB", @"Scores"]];
        [rootObj setObject:innerDict forKey:@"Lincoln"];

        id plist = [NSPropertyListSerialization dataFromPropertyList:(id)rootObj
            format:NSPropertyListXMLFormat_v1_0 errorDescription:&error];
```

清单 3-1 中代码的 XML 输出如清单 3-2 所示。

__清单 3-2__  作为输出生成的 XML 属性列表

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Lincoln</key>
    <dict>
        <key>DOB</key>
        <date>1809-02-12T09:18:00Z</date>
        <key>Name</key>
        <string>Abraham Lincoln</string>
        <key>Scores</key>
        <array>
            <integer>8</integer>
            <real>4.9000000953674316</real>
            <integer>9</integer>
        </array>
    </dict>
    <key>Washington</key>
    <dict>
        <key>DOB</key>
        <date>1732-02-17T01:32:00Z</date>
        <key>Name</key>
        <string>George Washington</string>
        <key>Scores</key>
        <array>
            <integer>6</integer>
            <real>4.5999999046325684</real>
            <integer>6</integer>
        </array>
    </dict>
</dict>
</plist>
```


本节的示例演示如何使用 Core Foundation 函数创建和操作属性列表。为了清晰起见，示例中省略了错误检查代码。在实际开发中，检查错误是_至关重要_的，因为向 Core Foundation 例程传入错误的参数会导致应用程序崩溃。

清单 3-3 展示了如何创建一个非常简单的属性列表——一个由 CFString 对象组成的数组。

__清单 3-3__  用数组创建一个简单的属性列表

```c
#include <CoreFoundation/CoreFoundation.h>
#define kNumFamilyMembers 5

void main () {
    CFStringRef names[kNumFamilyMembers];
    CFArrayRef  array;
    CFDataRef   xmlData;

    // 定义家庭成员。
    names[0] = CFSTR("Marge");
    names[1] = CFSTR("Homer");
    names[2] = CFSTR("Bart");
    names[3] = CFSTR("Lisa");
    names[4] = CFSTR("Maggie");

    // 用这个姓名字符串数组创建一个属性列表。
    array = CFArrayCreate( kCFAllocatorDefault,
                (const void **)names,
                kNumFamilyMembers,
                &kCFTypeArrayCallBacks );

    // 把这个 plist 转换成 XML 数据。
    xmlData = CFPropertyListCreateXMLData( kCFAllocatorDefault, array );

    // 清理 CF 类型。
    CFRelease( array );
    CFRelease( xmlData );
}
```

清单 3-4 展示了清单 3-3 中创建的 `xmlData` 如果打印到屏幕上会是什么样子。

__清单 3-4__  示例程序生成的 XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
        "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
    <string>Marge</string>
    <string>Homer</string>
    <string>Bart</string>
    <string>Lisa</string>
    <string>Maggie</string>
</array>
</plist>
```


你不能在 Core Foundation 属性列表中直接使用 C 的数值数据。Core Foundation 提供了 [CFNumberCreate](https://developer.apple.com/documentation/corefoundation/1542182-cfnumbercreate) 函数，用于把 C 数值转换成 CFNumber 对象——这是在属性列表中使用数字所必需的形式。

CFNumber 对象只是 C 数值的一层包装。Core Foundation 提供了创建 CFNumber、获取其值以及比较两个 CFNumber 对象的函数。要注意的是，CFNumber 对象在值方面是不可变的，但类型信息未必会被保留。你可以获取 CFNumber 对象的类型信息，但这是 CFNumber 对象用来存储你的值所采用的类型，_未必_与原始 C 数据的类型相同。

比较 CFNumber 对象时，转换和比较遵循的是人的直觉，而不是 C 的提升和比较规则。负零小于正零。正无穷大于除自身以外的一切，与自身比较则相等。负无穷小于除自身以外的一切，与自身比较则相等。与通常的做法不同，如果两个数都是 NaN，那么它们比较结果相等；如果只有其中一个是 NaN，那么当另一个数为负时 NaN 更大，当另一个数为正时 NaN 更小。

清单 3-5 展示了如何用一个 16 位整数创建 CFNumber 对象，然后获取该 CFNumber 对象的信息。

__清单 3-5__  用整数创建 CFNumber 对象

```c
Int16               sint16val = 276;
CFNumberRef         aCFNumber;
CFNumberType        type;
Int32               size;
Boolean             status;

// 用一个 16 位整数创建 CFNumber。
aCFNumber = CFNumberCreate(kCFAllocatorDefault,
                           kCFNumberSInt16Type,
                           &sint16val);

// 查出这个 CFNumber 实际使用的类型。
type = CFNumberGetType(aCFNumber);

// 现在查出它以字节为单位的大小。
size = CFNumberGetByteSize(aCFNumber);

// 从 CFNumber 中把值取回来。
status = CFNumberGetValue(aCFNumber,
                          kCFNumberSInt16Type,
                          &sint16val);
```

清单 3-6 创建了另一个 CFNumber 对象，并把它与清单 3-5 中创建的那个进行比较。

__清单 3-6__  比较两个 CFNumber 对象

```c
CFNumberRef         anotherCFNumber;
CFComparisonResult  result;

// 创建一个新的 CFNumber。
sint16val = 382;
anotherCFNumber = CFNumberCreate(kCFAllocatorDefault,
                        kCFNumberSInt16Type,
                        &sint16val);

// 比较两个 CFNumber 对象。
result = CFNumberCompare(aCFNumber, anotherCFNumber, NULL);

switch (result) {
    case kCFCompareLessThan:
        printf("aCFNumber is less than anotherCFNumber.\n");
        break;
    case kCFCompareEqualTo:
        printf("aCFNumber is equal to anotherCFNumber.\n");
        break;
    case kCFCompareGreaterThan:
        printf("aCFNumber is greater than anotherCFNumber.\n");
        break;
}
```

[下一页](Understanding%20XML%20Property%20Lists.md)[上一页](About%20Property%20Lists.md)

