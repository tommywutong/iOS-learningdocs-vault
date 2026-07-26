---
title: 从YYModel源码中可以学到什么：前篇
source_url: 'https://blog.itlee.top/2017/12/21/YYModel%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90%E4%B8%80/'
source_domain: blog.itlee.top
source_group: single-site
original_language: zh
published: 2017-12-21
archived_at: 2026-07-27
content_hash: 'sha256:a046d1298355e227'
plan_ref: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 5｜用同一组问题读 YYModel，才有可比性（对应 W6-04）
plan_week: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天）
plan_day: Day 5｜用同一组问题读 YYModel，才有可比性（对应 W6-04）
container: '//*[contains(@class,''post-content'')]'
container_source: guess
---

> 原文：[从YYModel源码中可以学到什么：前篇](https://blog.itlee.top/2017/12/21/YYModel%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90%E4%B8%80/)

[移动端](https://blog.itlee.top/categories/%E7%A7%BB%E5%8A%A8%E7%AB%AF/)[iOS](https://blog.itlee.top/tags/iOS/)[YYModel](https://blog.itlee.top/tags/YYModel/)

# 从YYModel源码中可以学到什么：前篇

镇长2017-12-212023-11-02

![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

`YYModel`是一个高性能模型库。为了了解底层实现，笔者初步打算用两篇文章学习`YYModel`源码。本文是第一篇文章，初步分析`YYModel`整体架构及为使用者暴露出来的接口，相当于一个使用教程。第二篇文章从YYModel源码中可以学到什么：前篇一步步分析`YYModel`是如何转换成Model的。 接下来我们开始吧！

[`YYModel`](https://github.com/ibireme/YYModel)一个高性能模型框架。

作者在`Github`上给出的性能对比图(iphone 6 y：时间)

![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

`YYModel`：具体以下特点：高性能、自动类型转换、类型安全、非侵入性、轻量等。

关于如何使用`YYModel`查看文档和示例[【传送门】](https://github.com/ibireme/YYModel)。

本文主要任务，分析`YYModel`的整体架构，实现思路，涉及到的知识点。

版本：1.0.4

# 文件结构

![YYModel文件目录](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

`YYModel`，只有5个文件。接下我们会具体看这五个文件都做了什么工作。

- `YYModel.h`头文件，通过`#import`该文件使用库。
- `YYClassInfo.h` 根据名字应该能猜出，关于Class信息的文件。
- `NSObject + YYModel.h` 这个`NSObject`的一个`Category`。还定义了一些内部类。

![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## YYModel头文件

该文件只是一个头文件，代码很少。

```plaintext
#if __has_include(<YYModel/YYModel.h>)
FOUNDATION_EXPORT double YYModelVersionNumber;
FOUNDATION_EXPORT const unsigned char YYModelVersionString[];
#import <YYModel/NSObject+YYModel.h>
#import <YYModel/YYClassInfo.h>
#else
#import "NSObject+YYModel.h"
#import "YYClassInfo.h"
#endif
```

> 拓展：
> 
> 1. `FOUNDATION_EXPORT`是用来定义常量的，另外一个经常用到的`#define`定义常量。
> 
>   那么两者的区别？  
>    假设分别使用两者定义字符串常量，前者可以通过`==`来判断字符串是否相等，后者则需要使用`isEqualToString:`来判断。因为，前者比较的是字符串指针地址，后者比较每个字符，因此前者效率更高。
> 2. `__has_include()`
> 
>   ```plaintext
>   	#if __has_include(<UIKit/UIKit.h>)
>   	// 包含
>   #else
>      	// 不包含
>   #endif
>   ```
> 
>   判断`UIKit`库是否存在。

## YYClassInfo

在`YYClassInfo`文件中定义四个类，涉及到`Runtime`知识，请看这篇文章[博文](https://github.com/jesusLove/iOS-day-by-day)或者直接查看objc4源码

![YYClassInfo](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

- YYClassIvarInfo

  该类对应实例变量信息（ivars），包含：名称，偏移量，类型编码，类型；其中类型请查看[【官方文档Type Encodings】](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html)
- YYClassMethodInfo

  方法的信息类，包含，方法名称，SEL，IMP，参数类型编码，返回值类型编码等。
- YYClassPropertyInfo

  属性信息类，包含名称，类型，类型编码，ivar名称，类，协议列表，setter/getter等。
- YYClassInfo：类信息。

**拓展**

> **Ivar, Method, Property, SEL, IMP都是什么？**
> 
> 理解这些需要对`runtime`了解，上面给出了博文链接，这里简单复习一下。

```plaintext
typedef struct objc_method *Method; // 方法
typedef struct objc_ivar *Ivar; // 实例变量
typedef struct objc_category *Category; //分类
typedef struct objc_property *objc_property_t; // 属性

struct objc_class {
    Class isa
    Class super_class // 指向父类
    const char * name // 名称
    long version
    long info
    long instance_size
    struct objc_ivar_list * ivars // 实例变量表
    struct objc_method_list * * methodLists  //方法表
    struct objc_cache * cache
    struct objc_protocol_list * protocols //协议表

};
/* Use `Class` instead of `struct objc_class *` */
```

> `Ivar`指实例变量，存放在实例变量表中。`Method`方法，存放在方法表中。

接下再看一下`Objc_method`结构体

```plaintext
struct objc_method {
    SEL method_name
    char * method_types
    IMP method_imp
    }
```

> `SEL`指方法名称，`IMP`指方法实现。

## NSObject + YYModel

该文件定义三个分类和一个协议，以及两个内部类，下面是`.h`文件中提供的接口。

### NSObject分类

提供了一些`data`与`model`转换的方法。

```plaintext
// 根据接收到JSON创建一个实例，该方法是线程安全的。
// json对象可以是 NSDictionary，NSString，NSData.
+ (nullable instancetype)yy_modelWithJSON:(id)json;

// 字典转Model
+ (nullable instancetype)yy_modelWithDictionary:(NSDictionary *)dictionary;

// 通过json设置属性, 无效的数据会被忽略
- (BOOL)yy_modelSetWithJSON:(id)json;
- (BOOL)yy_modelSetWithDictionary:(NSDictionary *)dic;

// model转json对象（NSDictionary/NSArray）, NSData, NSString
- (nullable id)yy_modelToJSONObject;
- (nullable NSData *)yy_modelToJSONData;
- (nullable NSString *)yy_modelToJSONString;

#pragma mark - 其他快捷方法
// 拷贝（NSCoping协议）
- (nullable id)yy_modelCopy;

// 编码和解码(对应NSCoding协议的两个方法)
- (void)yy_modelEncodeWithCoder:(NSCoder *)aCoder;
- (id)yy_modelInitWithCoder:(NSCoder *)aDecoder;

// NSObject协议
// 哈希值
- (NSUInteger)yy_modelHash;
// 相等判断
- (BOOL)yy_modelIsEqual:(id)model;
// Debug描述
- (NSString *)yy_modelDescription;
```

> 以上NSObject分类中提供的接口，具体实现稍后学习。

```plaintext
// 直接添加以下代码即可自动完成
- (void)encodeWithCoder:(NSCoder *)aCoder { [self yy_modelEncodeWithCoder:aCoder]; }
- (id)initWithCoder:(NSCoder *)aDecoder { self = [super init]; return [self yy_modelInitWithCoder:aDecoder]; }
- (id)copyWithZone:(NSZone *)zone { return [self yy_modelCopy]; }
- (NSUInteger)hash { return [self yy_modelHash]; }
- (BOOL)isEqual:(id)object { return [self yy_modelIsEqual:object]; }
- (NSString *)description { return [self yy_modelDescription]; }
```

### NSArray分类

从json-array中创建一个数组, 其实也是遍历循环调用字典转Model。

```plaintext
+ (nullable NSArray *)yy_modelArrayWithClass:(Class)cls json:(id)json;
```

### NSDictionary分类

从json创建字典。

```plaintext
+ (nullable NSDictionary *)yy_modelDictionaryWithClass:(Class)cls json:(id)json;
```

### YYModel协议

`YYModel`协议，通过实现响应的方法，可以提供白名单，黑名单，自定义属性名称等功能。

```plaintext
// 自定义属性名称，可以将json中的名称映射到自定义的名称，可以解决冲突例如`id`。
+ (nullable NSDictionary<NSString *, id> *)modelCustomPropertyMapper;

// 如果属性是一个容器对象，例如NSArray/NSSet/NSDictonary,实现该方法可以返回一个映射字典（property -> class）
+ (nullable NSDictionary<NSString *, id> *)modelContainerPropertyGenericClass;

+ (nullable Class)modelCustomClassForDictionary:(NSDictionary *)dictionary;

// 白名单和黑名单（若实现，忽略黑名单，只处理白名单）
+ (nullable NSArray<NSString *> *)modelPropertyBlacklist;
+ (nullable NSArray<NSString *> *)modelPropertyWhitelist;

- (NSDictionary *)modelCustomWillTransformFromDictionary:(NSDictionary *)dic;

// 数据验证和自定义转换
// 当JSON转为Model完成后，会调用该方法。可以在该方法中进行校验工作，返回NO该Model被忽略，也可以完成一些转换工作。
- (BOOL)modelCustomTransformFromDictionary:(NSDictionary *)dic;
- (BOOL)modelCustomTransformToDictionary:(NSMutableDictionary *)dic;
```

> 拓展
> 
> 1. 在源码中会发现有一对`NS_ASSUME_NONNULL_BEGIN`和`NS_ASSUME_NONNULL_END`宏。
> 
>   在Swift中存在`Option`类型，可以使用`!`和`?`声明变量，但是在OC中没有这个特性。出现新的关键词用于OC转Swift时区分能否为空。
> 
> `nullable` && `nonnull`
> 
> `nullable`指对象可以为NULL。
> 
> `nonnull`指对象不可以为NULL。
> 
> 如果不遵循这一规则，编译器就会给出警告。
> 
> 为了简化书写，在`NS_ASSUME_NONNULL_BEGIN`和`NS_ASSUME_NONNULL_END`宏之间的代码，默认都是`nonnull`。所以我们只需指定哪些`nullable`的指针就可以了。  
>  [StackOverflow](https://stackoverflow.com/questions/37956272/ns-assume-nonnull-begin-macro)关于该宏的问题。

# 其他知识点

接下来补充一些知识点，或许对以后开发有帮助。

## `NS_OPTIONS` && `NS_ENUM`

这是两个简单方便的宏定义，从iOS6开始，他们取代了原来的`enum`。

例如：

```plaintext
typedef NS_ENUM(NSInteger, UITableViewCellStyle) {
    UITableViewCellStyleDefault,
    UITableViewCellStyleValue1,
    UITableViewCellStyleValue2,
    UITableViewCellStyleSubtitle
};
```

其中第一个元素存储类型。第二个参数是名字。

另外，`enum`也可以被定义为按位掩码。用简单的OR和AND数学运算既可实现一个整型值的编码。请看这篇文章[《NS_ OPTIONS && NS _ENUM - NShipster》](http://nshipster.cn/ns_enum-ns_options/)。

# 小结

本章主要整理`YYModel`整体框架以及开发者提供的接口，并没有涉及到内部实现。接下来的文章，我将会一步步分析源码实现。

# 参考

[Github - ibireme/YYModel](https://github.com/ibireme/YYModel)
