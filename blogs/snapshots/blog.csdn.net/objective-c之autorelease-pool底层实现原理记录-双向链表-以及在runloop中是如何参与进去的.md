---
title: Objective-C之Autorelease Pool底层实现原理记录（双向链表）以及在Runloop中是如何参与进去的
source_url: 'https://blog.csdn.net/Deft_MKJing/article/details/82947706'
source_domain: blog.csdn.net
source_group: platform
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:74e6dd914a18f136'
plan_ref: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 3｜AutoreleasePool 放回事件循环中理解（对应 W4-01）
plan_week: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期
plan_day: Day 3｜AutoreleasePool 放回事件循环中理解（对应 W4-01）
container: '//div[@id=''content_views'']'
container_source: map
---

> 原文：[Objective-C之Autorelease Pool底层实现原理记录（双向链表）以及在Runloop中是如何参与进去的](https://blog.csdn.net/Deft_MKJing/article/details/82947706)

最近需要重新整理知识点备用，把一些重要的原理都搞了一遍

[NSDictionary和NSArray底层原理](https://blog.csdn.net/Deft_MKJing/article/details/82732833)

[HTTPS层引出OSI全部模型数据协议流转全过程](https://blog.csdn.net/Deft_MKJing/article/details/82868900)

[Xcode Command + R全过程以及启动优化](https://blog.csdn.net/Deft_MKJing/article/details/82929014)

## 前言

```objectivec
int main(int argc, char * argv[]) {
    @autoreleasepool {
        return UIApplicationMain(argc, argv, nil, NSStringFromClass([MTFAppDelegate class]));
    }
}
```

以上就是我们所看到的第一个自动释放池写法，按我之前的理解如下

1.自动释放池内部是由 AutoreleasePoolPage为节点的双向链表结构形成，AutoreleasePool本身没有任何形式的结构

2.当对象在autoreleasepool里面调用隐式执行autorelease的时候，会将对象加入上述以AutoreleasePoolPage为节点的双向链表中

3.每一个自动释放池初始化调用objc_autoreleasePoolPush（内部是会有一个哨兵对象作为标记，我的理解是一个自动释放池对应一个哨兵token），当objc_autoreleasePoolPop调用会根据传入的哨兵对象进行地址偏移，然后遍历出对象挨个执行release操作，知道遇到下一个哨兵或者stop为止

由于很早之前看到[雷纯峰](http://blog.leichunfeng.com/blog/2015/05/31/objective-c-autorelease-pool-implementation-principle/)和[德莱文大神](https://github.com/Draveness/analyze/blob/master/contents/objc/%E8%87%AA%E5%8A%A8%E9%87%8A%E6%94%BE%E6%B1%A0%E7%9A%84%E5%89%8D%E4%B8%96%E4%BB%8A%E7%94%9F.md)的文章，知道原理，但是一直没有系统记录下知识点，乘国庆有时间，又阅读了这两位大神的文章，特此记录下知识点，并加上些自己的理解，方便新手看懂和自己温故知新

## @autoreleasepool

根据我们看到的第一个main函数的自动释放池，可以看到**整个 iOS 的应用都是包含在一个自动释放池 block 中的**。

首先通过clang把OC代码转换成c++runtime代码

```
$ clang -rewrite-objc main.m
```

如下 也就是说`@autoreleasepool {}` 被转换为一个 `__AtAutoreleasePool` 结构体：

```
int main(int argc, const char * argv[]) {
    /* @autoreleasepool */ { __AtAutoreleasePool __autoreleasepool; 

        NSLog((NSString *)&__NSConstantStringImpl__var_folders_cz_5w_ql3y92hzcthzvjv84fcl80000gn_T_main_7919a8_mi_0);
    }
    return 0;
}
```

```
struct __AtAutoreleasePool {
  __AtAutoreleasePool() {atautoreleasepoolobj = objc_autoreleasePoolPush();}
  ~__AtAutoreleasePool() {objc_autoreleasePoolPop(atautoreleasepoolobj);}
  void * atautoreleasepoolobj;
};
```

最终转换出来实际上我们看到的main函数代码就是这样的

```
int main(int argc, const char * argv[]) {
    {
        void * atautoreleasepoolobj = objc_autoreleasePoolPush();
        
        // do whatever you want
        
        objc_autoreleasePoolPop(atautoreleasepoolobj);
    }
    return 0;
}
```

## AutoreleasePoolPage 的结构

上述展开的代码实际上就是如下PoolPage的操作

```
void *objc_autoreleasePoolPush(void) {
    return AutoreleasePoolPage::push();
}

void objc_autoreleasePoolPop(void *ctxt) {
    AutoreleasePoolPage::pop(ctxt);
}
```

**什么是AutoreleasePoolPage？**

其实AutoreleasePool没有单独的内存结构，而是通过AutoreleasePoolPage为节点的双向链表来实现。

- 每一个线程的 autoreleasepool 其实就是一个指针的堆栈；
- 每一个指针代表一个需要 release 的对象或者 POOL_SENTINEL（哨兵对象，代表一个 autoreleasepool 的边界）；
- 一个 pool token 就是这个 pool 所对应的 POOL_SENTINEL 的内存地址。当这个 pool 被 pop 的时候，所有内存地址在 pool token 之后的对象都会被 release ；
- 这个堆栈被划分成了一个以 page 为结点的双向链表。pages 会在必要的时候动态地增加或删除；
- Thread-local storage（线程局部存储）指向 hot page ，即最新添加的 autoreleased 对象所在的那个 page

空的poolpage如下

![](https://i-blog.csdnimg.cn/blog_migrate/5c83e84604357b4303f0d42e4aada14c.png)

> 1. `magic` 用来校验 AutoreleasePoolPage 的结构是否完整；
> 2. `next` 指向最新添加的 autoreleased 对象的下一个位置，初始化时指向 `begin()` ；
> 3. `thread` 指向当前线程；
> 4. `parent` 指向父结点，第一个结点的 parent 值为 `nil` ；双向链表上一个节点
> 5. `child` 指向子结点，最后一个结点的 child 值为 `nil` ；双向链表下一个节点
> 6. `depth` 代表深度，从 0 开始，往后递增 1；
> 7. `hiwat` 代表 high water mark 。
> 8. **每一个自动释放池都是由一系列的 `AutoreleasePoolPage` 组成的，并且每一个 `AutoreleasePoolPage` 的大小都是 `4096` 字节（16 进制 0x1000）**
> 
> 另外，当 `next == begin()` 时，表示 AutoreleasePoolPage 为空；当 `next == end()` 时，表示 AutoreleasePoolPage 已满。

其中有 56 bit 用于存储 `AutoreleasePoolPage` 的成员变量，剩下的 `0x100816038 ~ 0x100817000` 都是用来存储**加入到自动释放池中的对象**。

> `begin()` 和 `end()` 这两个类的实例方法帮助我们快速获取 `0x100816038 ~ 0x100817000` 这一范围的边界地址。

`next` 指向了下一个为空的内存地址，如果 `next` 指向的地址加入一个 `object`，也就是AutoreleasePool当中加入一个对象执行autorelease方法后，它就会如下图所示**移动到下一个为空的内存地址中**：

![](https://i-blog.csdnimg.cn/blog_migrate/e65316708fdeb794d27b6ef214a113eb.png)

## objc_autoreleasePoolPush (Push操作)

一些列的转换autoreleasePool的push方法转换为 AutoreleasePoolPage 的 push 函数，来看下它的作用和执行过程。**一个 push 操作其实就是创建一个新的 autoreleasepool ，对应 AutoreleasePoolPage 的具体实现就是往 AutoreleasePoolPage 中的 `next` 位置插入一个 POOL_SENTINEL ，并且返回插入的 POOL_SENTINEL 的内存地址。这个地址也就是我们前面提到的 pool token ，在执行 pop 操作的时候作为函数的入参。**

上面的AutoreleasePoolPage在这里会进入一个比较关键的方法 `autoreleaseFast`，并传入哨兵对象 `POOL_SENTINEL`：

```
static inline id *autoreleaseFast(id obj)
{
   AutoreleasePoolPage *page = hotPage();
   if (page && !page->full()) {
       return page->add(obj);
   } else if (page) {
       return autoreleaseFullPage(obj, page);
   } else {
       return autoreleaseNoPage(obj);
   }
}
```

上述方法分三种情况选择不同的代码执行：

- 有 `hotPage` 并且当前 `page` 不满

    - 调用 `page->add(obj)` 方法将对象添加至 `AutoreleasePoolPage` 的栈中
- 有 `hotPage` 并且当前 `page` 已满

    - 调用 `autoreleaseFullPage` 初始化一个新的页
    - 调用 `page->add(obj)` 方法将对象添加至 `AutoreleasePoolPage` 的栈中
- 无 `hotPage`

    - 调用 `autoreleaseNoPage` 创建一个 `hotPage`
    - 调用 `page->add(obj)` 方法将对象添加至 `AutoreleasePoolPage` 的栈中

最后的都会调用 `page->add(obj)` 将对象添加到自动释放池中。

> `hotPage` 可以理解为当前正在使用的 `AutoreleasePoolPage`。

## POOL_SENTINEL（哨兵对象）

这里很有必要先介绍下这个东西，正常情况下他就是nil的别名

```
#define POOL_SENTINEL nil
```

在每个自动释放池初始化调用 `objc_autoreleasePoolPush` 的时候，都会把一个 `POOL_SENTINEL` push 到自动释放池的栈顶，并且返回这个 `POOL_SENTINEL` 哨兵对象。

```
int main(int argc, const char * argv[]) {
    {
        void * atautoreleasepoolobj = objc_autoreleasePoolPush();
        
        // do whatever you want
        
        objc_autoreleasePoolPop(atautoreleasepoolobj);
    }
    return 0;
}
```

> 上面的 `atautoreleasepoolobj` 就是一个 `POOL_SENTINEL`。

理解：

当我们看到一个@autoreloeasepool{}的代码的时候，转换之后如上代码，可以理解为在双向链表结构的基础上，每个node节点就是poolpage对象，该对象有固定大小4096，前几个字节用于存储属性字段，后面从begin地址开始到end地址结束用来存储自动释放池里面的对象，就会在属性字段挨着的地址上出现一个哨兵标志POOL_SENTINEL，也就是nil标志自动释放池的出现，返回值地址用来标志对应的池子，后续pop的时候根据池子遍历对象挨个执行release操作

## autorelease 操作

AutoreleasePoolPage 的 `autorelease` 函数的实现对我们来说就比较容量理解了，它跟 push 操作的实现非常相似。**只不过 push 操作插入的是一个 POOL_SENTINEL ，而 autorelease 操作插入的是一个具体的 autoreleased 对象。**

```
static inline id autorelease(id obj)
{
    assert(obj);
    assert(!obj->isTaggedPointer());
    id *dest __unused = autoreleaseFast(obj);
    assert(!dest  ||  *dest == obj);
    return obj;
}
```

## objc_autoreleasePoolPop 方法

同理，前面提到的 `objc_autoreleasePoolPop` 函数本质上也是调用的 AutoreleasePoolPage 的 `pop` 函数。

pop 函数的入参就是 push 函数的返回值，也就是 POOL_SENTINEL 的内存地址，即 pool token 。当执行 pop 操作时，内存地址在 pool token 之后的所有 autoreleased 对象都会被 release 。直到 pool token 所在 page 的 `next` 指向 pool token 为止。

下面是某个线程的 autoreleasepool 堆栈的内存结构图，在这个 autoreleasepool 堆栈中总共有两个 POOL_SENTINEL ，即有两个 autoreleasepool 。该堆栈由三个 AutoreleasePoolPage 结点组成，第一个 AutoreleasePoolPage 结点为 `coldPage()` ，最后一个 AutoreleasePoolPage 结点为 `hotPage()` 。其中，前两个结点已经满了，最后一个结点中保存了最新添加的 autoreleased 对象 `objr3` 的内存地址。

![](https://i-blog.csdnimg.cn/blog_migrate/02ec06141c816bfa33ebca26967907fc.png)

如果执行pop（token），autoreleasepool对应的堆栈信息就会变成如下

![](https://i-blog.csdnimg.cn/blog_migrate/a092044110a9eab473e51261b9b9951d.png)

## 总结：

1.@autorelease展开来其实就是objc_autoreleasePoolPush和objc_autoreleasePoolPop，但是这两个函数也是封装的一个底层对象AutoreleasePoolPage，实际对应的是AutoreleasePoolPage::push和AutoreleasePoolPage::pop

2.autoreleasepool本身并没有内部结构，而是一种通过AutoreleasePoolPage为节点的双向链表结构

3.根据AutoreleasePoolPage双向链表的结构，可以看到当调用objc_autoreleasePoolPush的时候实际上除了初始化poolpage对象属性之外，还会插入一个**POOL_SENTINEL哨兵，**用来区分不同autoreleasepool之间包裹的对象。

4.当对象调用 `autorelease` 方法时，会将实际对象插入 `AutoreleasePoolPage` 的栈中，通过next指针移动。

5.autoreleasePoolPage的结构字段上面有介绍，其中每个双向链表的node节点也就是poolpage对象内存大小为4096，除了基础属性之外，外插一个**POOL_SENTINEL，**每出现一个@autorelease就会有一个哨兵，剩下的通过begin和end来标识是否存储满，满了就会重新创建一个poolpage来链接链表，按照这个套路，出现一个PoolPush就创建一个哨兵，出现一个对象的autorelease，就增加一个实际的对象，满了就创建新的链表节点这样衍生下去

6.AutoreleasePoolPage::pop那么当调用pop的时候，会传入需要drain的哨兵节点，遍历该内存地址上方所有对象，直到遇到对应的哨兵，然后释放栈中遍历到的对象，每删除一页就修正双向链表的指针，最后两张图很容易理解

7.ARC下，直接调用上面的方法，整个线程都被自动释放池双向链表管理，Push创建的时候插入哨兵对象，当我们在内部写代码的时候，会自动添加Autorelease，对象会加入到在哨兵节点之间，加入到next指针上，一个个往后移，满了4096就换下一个poolPage对象节点来存储，出了释放池，会调用pop，传入自动释放池的哨兵给pop，然后遍历哨兵内存地址之后的所有对象执行release，最后吧next指针移到目标哨兵

8.Runloop这里就不介绍了，可以翻看另外写的博客，App启动的时候会在主Runloop里面注册两个观察者和一个回调函数，

第一个Observe观察到entry即将进入loop的时候，会调用_objc_autoreleasePoolPush（）创建自动释放池，优先级最高，保证在所有回调方法之前。

第二个Observe观察到即将进入休眠或者退出的时候，当监听到Beforewaiting的时候，调用_objc_autoreleasePoolPop() 和 _objc_autoreleasePoolPush() 释放旧的创建新的，当监听到Exit的时候调用_objc_autoreleasePoolPop释放pool，这里的Observe优先级最低，发生在所有回调函数之后。
