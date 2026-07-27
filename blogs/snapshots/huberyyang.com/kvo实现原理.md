---
title: KVO实现原理
source_url: 'https://huberyyang.com/2018/04/13/KVO%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86/'
source_domain: huberyyang.com
source_group: single-site
original_language: zh
published: 2018-04-13
archived_at: 2026-07-27
content_hash: 'sha256:34f8110a22229756'
plan_ref: 第三周：Runtime 行为与 Cocoa 对象通信 / Day 5｜KVC 提供间接访问，KVO 在它的约定上插入通知（对应 W3-09）
plan_week: 第三周：Runtime 行为与 Cocoa 对象通信
plan_day: Day 5｜KVC 提供间接访问，KVO 在它的约定上插入通知（对应 W3-09）
container: //article
container_source: map
---

> 原文：[KVO实现原理](https://huberyyang.com/2018/04/13/KVO%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86/)

**KVO在Apple中的API文档如下：**

> Automatic key-value observing is implemented using a technique called isa-swizzling… When an observer is registered for an attribute of an object the isa pointer of the observed object is modified, pointing to an intermediate class rather than at the true class …

**KVO基本原理：**

1.KVO是基于runtime机制实现的

2.当某个类的属性对象第一次被观察时，系统就会在运行期动态地创建该类的一个派生类，在这个派生类中重写基类中任何被观察属性的setter 方法。派生类在被重写的setter方法内实现真正的通知机制

3.如果原类为Person，那么生成的派生类名为NSKVONotifying_Person

4.每个类对象中都有一个isa指针指向当前类，当一个类对象的第一次被观察，那么系统会偷偷将isa指针指向动态生成的派生类，从而在给被监控属性赋值时执行的是派生类的setter方法

5.键值观察通知依赖于NSObject 的两个方法: `willChangeValueForKey:` 和 `didChangevlueForKey:`；在一个被观察属性发生改变之前， `willChangeValueForKey:`一定会被调用，这就 会记录旧的值。而当改变发生后，`didChangeValueForKey:`会被调用，继而 `observeValueForKey:ofObject:change:context:` 也会被调用。

**KVO深入原理：**

1.Apple 使用了 isa 混写（isa-swizzling）来实现 KVO 。当观察对象A时，KVO机制动态创建一个新的名为：`NSKVONotifying_A`的新类，该类继承自对象A的本类，且KVO为`NSKVONotifying_A`重写观察属性的setter方法，setter方法会负责在调用原setter方法之前和之后，通知所有观察对象属性值的更改情况。

2.`NSKVONotifying_A`类剖析：在这个过程，被观察对象的 isa 指针从指向原来的A类，被KVO机制修改为指向系统新创建的子类 `NSKVONotifying_A`类，来实现当前类属性值改变的监听；

3.所以当我们从应用层面上看来，完全没有意识到有新的类出现，这是系统“隐瞒”了对KVO的底层实现过程，让我们误以为还是原来的类。但是此时如果我们创建一个新的名为`NSKVONotifying_A`的类()，就会发现系统运行到注册KVO的那段代码时程序就崩溃，因为系统在注册监听的时候动态创建了名为`NSKVONotifying_A`的中间类，并指向这个中间类了。

4.（isa 指针的作用：每个对象都有isa 指针，指向该对象的类，它告诉 Runtime 系统这个对象的类是什么。所以对象注册为观察者时，isa指针指向新子类，那么这个被观察的对象就神奇地变成新子类的对象（或实例）了。）因而在该对象上对 setter 的调用就会调用已重写的 setter，从而激活键值通知机制。

5.子类setter方法剖析：KVO的键值观察通知依赖于 NSObject 的两个方法:`willChangeValueForKey:`和 `didChangevlueForKey:`，在存取数值的前后分别调用2个方法： 被观察属性发生改变之前，`willChangeValueForKey:`被调用，通知系统该 `keyPath`的属性值即将变更；当改变发生后， `didChangeValueForKey: `被调用，通知系统该 `keyPath` 的属性值已经变更；之后，`observeValueForKey:ofObject:change:context:` 也会被调用。且重写观察属性的setter方法这种继承方式的注入是在运行时而不是编译时实现的。

![KVO原理图](https://raw.githubusercontent.com/HuberyYang/graphic/imgs/20180413/68ce11b3cb138fb1782413837315a1f6.png)

---

- [Previous  
   swift自定义Debug模式下print](https://huberyyang.com/2018/03/02/swift%E8%87%AA%E5%AE%9A%E4%B9%89Debug%E6%A8%A1%E5%BC%8F%E4%B8%8Bprint/)
- [Next  
   iOS bitcode 揭秘](https://huberyyang.com/2019/11/30/iOS-bitcode-%E6%8F%AD%E7%A7%98/)
