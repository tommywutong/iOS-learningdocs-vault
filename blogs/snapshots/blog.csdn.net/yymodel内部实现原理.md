---
title: YYModel内部实现原理
source_url: 'https://blog.csdn.net/Lu_Ca/article/details/114532423'
source_domain: blog.csdn.net
source_group: platform
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:7d4cc9656b93607c'
plan_ref: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 5｜用同一组问题读 YYModel，才有可比性（对应 W6-04）
plan_week: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天）
plan_day: Day 5｜用同一组问题读 YYModel，才有可比性（对应 W6-04）
container: '//div[@id=''content_views'']'
container_source: map
---

> 原文：[YYModel内部实现原理](https://blog.csdn.net/Lu_Ca/article/details/114532423)

YYModel作为开发过程中模型转换框架，为JSON与数据模型之间的相互转换，提供了高性能的解决方案。

之前一直听别人说，YYModel内部实现是KVC进行的属性赋值。也认为是合理的，但是今天查看源码发现，里边其实并不是采用的setValue：forKey：的方式进行赋值的。而是采用了objc_msgSend方法调用了属性的setter方法进行赋值的。以后，跟别人说YYModel里可别再说是KVC了，一看就没有看过源码。下边粘一句赋值源码

```
case YYEncodingTypeNSMutableString: {
                    if ([value isKindOfClass:[NSString class]]) {
                        if (meta->_nsType == YYEncodingTypeNSString) {
                            ((void (*)(id, SEL, id))(void *) objc_msgSend)((id)model, meta->_setter, value);
                        } else {
                            ((void (*)(id, SEL, id))(void *) objc_msgSend)((id)model, meta->_setter, ((NSString *)value).mutableCopy);
                        }
                    } 
```

里边清楚的写着((**void** (*)(**id**, **SEL**, **id**))(**void** *) objc_msgSend)((**id**)model, meta-\>_setter, value);

接下来我写一下我看到的模型与数据之间进行转换的大概流程。

### Json转Model

我们通常通过调用方法yy_modelWithJson进行转化操作。其实这个函数里边主要实现了下边四步：

1、是先将json序列化为可用的字典，然后调用yy_modelWithDictionary方法

2、yy_modelWithDictionary对Json类型确定，通过类对象创建对象的实例，并通过yy_modelSetWithDictionary进行赋值

3、在yy_modelSetWithDictionary方法中，通过modelSetValueForProperty方法赋值。

4、modelSetValueForProperty里对属性数据类型判断，然后分别通过调用的消息发送的objc_msgSend的方式，再调用setter方法进行赋值。

### Model转Json

通常我们调用yy_modelToJSONString方法进行转换操作。而这个函数的实现过程大致是这样的：

1、通过调用yy_modelToJSONData返回的data，然后通过[[NSString alloc] initWithData:jsonData encoding:NSUTF8StringEncoding]生成的json字符串

2、yy_modelToJSONData方法里调用yy_modelToJSONObject方法返回一个id类型的对象，然后通过[NSJSONSerialization dataWithJSONObject:jsonObject options:0 error:**NULL**]生成第一步需要的NSData。

3、yy_modelToJSONObject中调用ModelToJSONObjectRecursive方法。

4、然后ModelToJSONObjectRecursive主要是对对象进行预处理，转成有效的json对象。

#### ModelToJSONObjectRecursive方法过程

- ModelToJSONObjectRecursive方法对于能直接转json的属性之间返回。
- 对于集合类的属性如字典、数组等进行内部判断通过递归调用ModelToJsonObjectRecursive方法的方式不断查看每个元素是否可以直接转json。如果可以直接返回集合类，如果不可以，创建一个新的集合，遍历之前的每个元素，将里边的元素转成NSString、NSNumber，然后解析完成后添加到集合类。
- 自定义类对象，使用NSDictionary对象来重新组装，通过objc_msgSend调用getter的方法取值，然后逐一转成有效的json对象。

⚠️：以上都是个人通过查看源码个人结论，如果有错误的地方欢迎指正，共勉
