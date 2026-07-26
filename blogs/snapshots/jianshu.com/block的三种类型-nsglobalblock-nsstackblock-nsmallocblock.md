---
title: 'Block的三种类型:__NSGlobalBlock,__NSStackBlock,__NSMallocBlock'
source_url: 'https://www.jianshu.com/p/f0870fa95aac'
source_domain: jianshu.com
source_group: platform
original_language: zh
published: 2018-09-03
archived_at: 2026-07-27
content_hash: 'sha256:ffe9199df4bcce33'
plan_ref: 第二周：weak、属性关键字与 Block / Day 3｜先看 Block 是什么，再谈捕获（对应 W2-12、W2-13、W2-15）
plan_week: 第二周：weak、属性关键字与 Block
plan_day: Day 3｜先看 Block 是什么，再谈捕获（对应 W2-12、W2-13、W2-15）
container: //article
container_source: map
---

> 原文：[Block的三种类型:__NSGlobalBlock,__NSStackBlock,__NSMallocBlock](https://www.jianshu.com/p/f0870fa95aac)

我们在讲[block的本质](https://www.jianshu.com/p/e6759404f9cd)的时候已经知道了,block的本质就是一个 OC 对象,那么既然它是一个 OC 对象,它就会有类型,本文就将讲解`block`的三种类型.  
 我们在讲`block`的三种类型之前,先了解一下程序的内存分配情况,因为不同类型的`block`分配的内存也不同.

- .text段 : 也称代码段,我们写的代码都存放在这里
- .data区 : 也称数据区,一般存放全局变量, **__NSGlobalBlock存放在这里**
- 堆区 : 存放我们自己`alloc`出来的对象,动态分配内存,需要程序员自己申请内存,自己管理. **__NSMallocBlock存放在堆区**
- 栈区 : 一般存放局部变量,不需要程序员管理,系统自动分配,自动销毁,**__NSStackBlock存放在栈区**

  不同block的内存分配

##### 一: __NSGlobalBlock

- 结论:没有访问 auto变量 的block 就是 __NSGlobalBlock

```
int main(int argc, const char * argv[]) {
    @autoreleasepool {
        static int age = 10;
        void(^block)(void) = ^{
            NSLog(@"Hello, World! %d",age);
        };
        NSLog(@"%@",[block class]);
    }
    return 0;
}
控制台输出:__NSGlobalBlock__
```

这个很好理解,不过多解释

- 二: __NSStackBlock
- 结论:访问了auto变量 的block 就是 __NSStackBlock

```
int main(int argc, const char * argv[]) {
    @autoreleasepool {
        int age = 10;
        void(^block)(void) = ^{
            NSLog(@"Hello, World! %d",age);
        };
        NSLog(@"%@",[block class]);
    }
    return 0;
}
控制台输出:__NSMallocBlock__
```

怎么打印的是`__NSMallocBlock__`,刚才不是说访问了`auto变量`就是`__NSStackBlock`吗?  
 因为这里我们使用的是ARC,在ARC环境下,Xcode会默认帮我们做很多事情,我们在Build Settings中把ARC设置成MRC,再来打印一下:

```
2018-08-30 17:37:09.846365+0800 block的类型[4318:3463149] __NSStackBlock__
```

这次打印的就是`__NSStackBlock__`  
 ❓我们思考一下,`__NSStackBlock`在访问外部变量时,会有什么问题?

所以,为了避免出现这种情况,我们需要把`block`存储在堆上,`__NSMallocBlock`就闪亮登场了.

- 三: __NSMallocBlock
- 结论: 当一个`__NSStackBlock`调用了`copy`操作,返回的就是一个`__NSMallocBlock`

  __NSMallocBlock

❓思考:如果我们对`__NSGlobalBlock` 进行一次 `copy`操作,会发生什么变化呢?

__NSGlobalBlock copy后

##### ‼️注意

以上都是在MRC环境下,如果是在ARC环境下,编译器会根据情况自动将栈上的block复制到堆上,比如以下几种情况:

- block作为函数返回值时

  block作为返回值编译器会自动copy
- 将block赋值给__strong指针时

  被强指针引用的block会自动copy
- block作为Cocoa API方法名含有UsingBlock的方法参数时

  UsingBlock
- block作为GCD API的方法参数时

  GCD API的方法参数

**总结:**

- 1:一共有三种类型的Block.分为`__NSGlobalBlock`,`__NSStackBlock`,`__NSMallocBlock`.
- 2:没有访问 auto变量 的`block` 就是 `__NSGlobalBlock`  
   访问了auto变量 的`block` 就是 `__NSStackBlock`  
   当一个`__NSStackBlock`调用了copy操作,返回的就是一个`__NSMallocBlock`sing
- 3:在ARC环境下,编译器会自动把栈上的`block copy`到堆上
