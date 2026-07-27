---
title: iOS 中 KVC 与 KVO 底层原理
source_url: 'https://blog.csdn.net/weixin_46818265/article/details/142442895'
source_domain: blog.csdn.net
source_group: platform
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:1478bfe54cd79c79'
plan_ref: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 8｜架构是前七天代码的职责重排（对应 W6-06、W6-07）
plan_week: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天）
plan_day: Day 8｜架构是前七天代码的职责重排（对应 W6-06、W6-07）
container: '//div[@id=''content_views'']'
container_source: map
---

> 原文：[iOS 中 KVC 与 KVO 底层原理](https://blog.csdn.net/weixin_46818265/article/details/142442895)

### KVC

本质：

```objc
[object setValue: forKey:];
```

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/77209b135706420da45d0c346a729d54.png)  
 `即使没有在.h 文件中有@property 的属性声明，setValue:forKey依然会按照上图流程执行代码`  
 `KVC 如果成功改变了成员变量，是一定可以被 KVO 监听到成员变量的前后改变的`  
 ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/462ff0c7662b4311a744bd10b1106f80.png)

### KVO

- runtime会生成中间类：NSKVONotifying_类名
- 修改原来实例isa指向  
   实例isa指向 NSKVONotifying_类名  
   NSKVONotifying_类名 的isa 指向 class
- 属性监听与改变

    - 直接修改成员值时，KVO是无能为力的  
      **kvo只能监听具有setProperty的属性**
    - runtime调用Fundation内部函数_NSSet数据类型(Int)ValueAndNotify。代码实现逻辑：

          1. 生成属性的set方法
          2. willChangeValueForKey:属性
          3. super set属性方法，修改 _属性 的值
          4. didChangeValueForKey:属性，此时调用监听器，通知外界属性改变。  
            `[observer observeValueForKeyPath…]`
- 应用场景

    - 给webView添加加载进图条  
       [self.wkWebView addObserver:self forKeyPath:@“estimatedProgress” options:NSKeyValueObservingOptionNew context:nil];
    - 给ScrollView底部添加公共视图  
       监听contentSize，在contentInset安全边距扩展视图
