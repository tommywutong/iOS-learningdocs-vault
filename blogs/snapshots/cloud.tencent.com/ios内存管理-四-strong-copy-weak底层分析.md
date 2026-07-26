---
title: 'iOS内存管理（四）-strong&copy&weak底层分析'
source_url: 'https://cloud.tencent.com/developer/article/2303898'
source_domain: cloud.tencent.com
source_group: platform
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:8806912cfb380bca'
plan_ref: 第二周：weak、属性关键字与 Block / Day 1｜先把属性翻译成所有权关系（对应 W2-07、W2-08、W2-09）
plan_week: 第二周：weak、属性关键字与 Block
plan_day: Day 1｜先把属性翻译成所有权关系（对应 W2-07、W2-08、W2-09）
container: '//div[contains(@class,''rno-markdown'')]'
container_source: map
---

> 原文：[iOS内存管理（四）-strong&copy&weak底层分析](https://cloud.tencent.com/developer/article/2303898)

## 常见关键字

- 内存管理有关的关键字：weak，assign，strong，retain，copy
- 线程安全有关的的关键字：nonatomic，atomic
- 访问权限有关的的关键字：readonly，readwrite（只读，可读写）
- 修饰变量的关键字：const，static，extern

## strong & copy & weak 底层分析

在LGPerson中我们定义了两个两个属性，分别用copy和strong修饰

![image](https://developer.qcloudimg.com/http-save/6658895/b3b1c5bce2179a9d462005415ecdd9b4.jpg)

image

##### objc_setProperty

- 如果是atomic & copy修饰，name为objc_setProperty_atomic_copy
- 如果是atomic 且没有copy修饰，name为 objc_setProperty_atomic
- 如果是nonatomic & copy 修饰，name为 objc_setProperty_nonatomic_copy
- 其余组合，统一为name = objc_setProperty_nonatomic

![image](https://developer.qcloudimg.com/http-save/6658895/2c7b180e92afa72f5e111bf4f6d385a7.png)

image

##### objc_storeStrong

代码语言：txt

复制

```txt
void
objc_storeStrong(id *location, id obj)
{
    id prev = *location;
    if (obj == prev) {
        return;
    }
    objc_retain(obj);//retain新值
    *location = obj;
    objc_release(prev);//release旧值
}
```

分析：

- obj新值引用计时器加1
- 当前的指针指向新值，更新指针
- 旧值引用计数器减1

##### 总结：

- copy和strong修饰的属性在底层编译的不一致，主要还是llvm中对其进行了不同的处理的结果。copy的赋值是通过objc_setProperty，而strong的赋值时通过self + 内存平移（即将指针通过平移移至name所在的位置，然后赋值），然后还原成 strong类型
- strong & copy 在底层调用objc_storeStrong，本质是新值retain，旧值release
- weak 在底层调用objc_initWeak

## 常见问题：
