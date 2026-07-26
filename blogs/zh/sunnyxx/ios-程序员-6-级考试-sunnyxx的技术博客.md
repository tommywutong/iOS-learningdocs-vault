---
title: iOS 程序员 6 级考试 · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2014/03/06/ios_exam_0/'
original_language: zh
published: 2014-03-06
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:f45ddde5da2b747c'
translated: n/a
---

> 原文：[iOS 程序员 6 级考试 · sunnyxx的技术博客](http://blog.sunnyxx.com/2014/03/06/ios_exam_0/)　·　sunnyxx (孙源)

# iOS 程序员 6 级考试

2014年3月6日

## [#前言](#前言)前言

iOS 面试题看过来  
题目多来源于项目中遇到的错误和平时的误区，要是都能了如指掌，恭喜你，6级过了- -。  
考点大概是对 iOS 框架、objc 语言基础的理解，以看代码为主（那种“谈谈xxxx的理解的题就算了吧”）

不断总结中…

> It’s examing time…

---

## [#1-下面的代码分别输出什么？](#1-下面的代码分别输出什么？)1. 下面的代码分别输出什么？

```objc
@implementation Son : Father
- (id)init {
    self = [super init];
    if (self) {
        NSLog(@"%@", NSStringFromClass([self class]));
        NSLog(@"%@", NSStringFromClass([super class]));
    }
    return self;
}
@end
```

## [#2-下面的代码报错？警告？还是正常输出什么？](#2-下面的代码报错？警告？还是正常输出什么？)2. 下面的代码报错？警告？还是正常输出什么？

```objc
Father *father = [Father new];
BOOL b1 = [father responseToSelector:@selector(responseToSelector:)];
BOOL b2 = [Father responseToSelector:@selector(responseToSelector:)];
NSLog(@"%d, %d", b1, b2);
```

## [#3-请求很快就执行完成，但是completionBlock很久之后才设置，还能否执行呢？](#3-请求很快就执行完成，但是completionBlock很久之后才设置，还能否执行呢？)3. 请求很快就执行完成，但是completionBlock很久之后才设置，还能否执行呢？

```objc
...
// 当前在主线程

[request startAsync]; // 后台线程异步调用，完成后会在主线程调用completionBlock
sleep(100); // sleep主线程，使得下面的代码在后台线程完成后才能执行
[request setCompletionBlock:^{
    NSLog(@"Can I be printed?");
}];
...
```

## [#4-不使用IB时，下面这样做有问题么？](#4-不使用IB时，下面这样做有问题么？)4. 不使用IB时，下面这样做有问题么？

```objc
- (void)viewDidLoad {
  [super viewDidLoad];
  CGRect frame = CGRectMake(0, 0, self.view.bounds.size.width * 0.5, self.bounds.size.height * 0.5);
  UIView *view = [[UIView alloc] initWithFrame:frame];
  [self.view addSubview:view];
}
```

## [#5-下面代码输出什么？](#5-下面代码输出什么？)5. 下面代码输出什么？

```objc
- (void)viewDidLoad {
    [super viewDidLoad];

    NSLog(@"1");
    dispatch_sync(dispatch_get_main_queue(), ^{
        NSLog(@"2");
    });
    NSLog(@"3");
}
```

---

# [#答案和解答](#答案和解答)答案和解答

## [#请戳我，我是传送门](#请戳我，我是传送门)[请戳我，我是传送门](http://blog.sunnyxx.com/2014/03/06/ios_exam_0_key/)

原创文章，转载请注明源地址，[blog.sunnyxx.com](http://blog.sunnyxx.com)
