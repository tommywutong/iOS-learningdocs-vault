---
title: 黑魔法__attribute__((cleanup)) · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2014/09/15/objc-attribute-cleanup/'
original_language: zh
published: 2014-09-15
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:335593245954765b'
translated: n/a
---

> 原文：[黑魔法__attribute__((cleanup)) · sunnyxx的技术博客](http://blog.sunnyxx.com/2014/09/15/objc-attribute-cleanup/)　·　sunnyxx (孙源)

# 黑魔法__attribute__((cleanup))

2014年9月15日

编译器属性`__attribute__`用于向编译器描述特殊的标识、检查或优化，几个常用的用法看[《mattt大神的文章》](http://nshipster.com/__attribute__/)就好。今天发现一个名为`cleanup`的黑魔法属性，简单介绍下。

---

## [#基本用法](#基本用法)基本用法

`__attribute__((cleanup(...)))`，用于修饰一个变量，**在它的作用域结束时可以自动执行一个指定的方法**，如：

```objc
// 指定一个cleanup方法，注意入参是所修饰变量的地址，类型要一样
// 对于指向objc对象的指针(id *)，如果不强制声明__strong默认是__autoreleasing，造成类型不匹配
static void stringCleanUp(__strong NSString **string) {
    NSLog(@"%@", *string);
}
// 在某个方法中：
{
    __strong NSString *string __attribute__((cleanup(stringCleanUp))) = @"sunnyxx";
} // 当运行到这个作用域结束时，自动调用stringCleanUp
```

所谓作用域结束，包括大括号结束、return、goto、break、exception等各种情况。  
当然，可以修饰的变量不止NSString，`自定义Class`或`基本类型`都是可以的：

```objc
// 自定义的Class
static void sarkCleanUp(__strong Sark **sark) {
    NSLog(@"%@", *sark);
}
__strong Sark *sark __attribute__((cleanup(sarkCleanUp))) = [Sark new];
// 基本类型
static void intCleanUp(NSInteger *integer) {
    NSLog(@"%d", *integer);
}
NSInteger integer __attribute__((cleanup(intCleanUp))) = 1;
```

假如一个作用域内有若干个cleanup的变量，他们的调用顺序是`先入后出`的栈式顺序；  
而且，cleanup是先于这个对象的`dealloc`调用的。

## [#进阶用法](#进阶用法)进阶用法

既然`__attribute__((cleanup(...)))`可以用来修饰变量，`block`当然也是其中之一，写一个block的cleanup函数非常有趣：

```objc
// void(^block)(void)的指针是void(^*block)(void)
static void blockCleanUp(__strong void(^*block)(void)) {
    (*block)();
}
```

于是在一个作用域里声明一个block：

```objc
{
   // 加了个`unused`的attribute用来消除`unused variable`的warning
    __strong void(^block)(void) __attribute__((cleanup(blockCleanUp), unused)) = ^{
        NSLog(@"I'm dying...");
    };
} // 这里输出"I'm dying..."
```

这里不得不提万能的`Reactive Cocoa`中神奇的`@onExit`方法，其实正是上面的写法，简单定义个宏：

```objc
#define onExit\
    __strong void(^block)(void) __attribute__((cleanup(blockCleanUp), unused)) = ^
```

用这个宏就能将一段写在前面的代码最后执行：

```objc
{
    onExit {
        NSLog(@"yo");
    };
} // Log "yo"
```

这样的写法可以将成对出现的代码写在一起，比如说一个lock：

```objc
NSRecursiveLock *aLock = [[NSRecursiveLock alloc] init];
[aLock lock];
// 这里
//     有
//        100多万行
[aLock unlock]; // 看到这儿的时候早忘了和哪个lock对应着了
```

用了`onExit`之后，代码更集中了：

```objc
NSRecursiveLock *aLock = [[NSRecursiveLock alloc] init];
[aLock lock];
onExit {
    [aLock unlock]; // 妈妈再也不用担心我忘写后半段了
};
// 这里
//    爱多少行
//           就多少行
```

还是那句老话：剩下的就全靠想象力了。
