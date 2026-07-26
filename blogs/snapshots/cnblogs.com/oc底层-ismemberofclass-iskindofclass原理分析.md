---
title: 【OC底层】isMemberOfClass、isKindOfClass原理分析
source_url: 'https://www.cnblogs.com/xgao/p/11277935.html'
source_domain: cnblogs.com
source_group: platform
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:ddbd3ac398cd69b5'
plan_ref: 第一周：对象、类与所有权的地基 / Day 3｜在结构图上推导类型判断，再看 Tagged Pointer（对应 W1-05、W1-06）
plan_week: 第一周：对象、类与所有权的地基
plan_day: Day 3｜在结构图上推导类型判断，再看 Tagged Pointer（对应 W1-05、W1-06）
container: '//div[@id=''cnblogs_post_body'']'
container_source: map
---

> 原文：[【OC底层】isMemberOfClass、isKindOfClass原理分析](https://www.cnblogs.com/xgao/p/11277935.html)

## isMemberOfClass

- 调用者必须是传入的类的实例对象才返回YES  
- 判断调用者是否是传入对象的实例，别弄反了，如 [s1 isMemberOfClass:p1] ，意思是s1是否是p1的实例对象  
- 不进行父类递归去查找判断

## **源码：**

```
+ (BOOL)isMemberOfClass:(Class)cls {
    return object_getClass((id)self) == cls;
}
- (BOOL)isMemberOfClass:(Class)cls {
    return [self class] == cls;
}
```

有两个方法，一个实例方法，一个类方法，两者区别：

- 实例方法：是根据实例对象取得类对象，再去判断  
 - 类方法：是根据对象取得元类对象，再去判断

## 实例代码：

```
XPerson* p1 = [[XPerson alloc]init];
XStudent* s1 = [[XStudent alloc]init];

// true (用s1的类对象和 [s1 class] 判断，肯定是一样的了)
NSLog(@"s1是否是s1 实例: %i",[s1 isMemberOfClass:[s1 class]]);
// true ([s1 class] 与 [XStudent class] 等同,一个类只会有一个类对象，一个元类对象，可以有多个实例对象)
NSLog(@"s1是否是XStudent 实例: %i",[s1 isMemberOfClass:[XStudent class]]);
// false (s1的类对象 != p1的类对象)
NSLog(@"s1是否是p1 实例: %i",[s1 isMemberOfClass:[p1 class]]);
// false (同上)
NSLog(@"s1是否是XPerson 实例: %i",[s1 isMemberOfClass:[XPerson class]]);

// false (XStudent元类对象 != XStudent类对象)（底层是获取XStudent的元类去比较）
NSLog(@"XStudent是否是XStudent 实例: %i",[XStudent isMemberOfClass:[XStudent class]]);
// true (XStudent元类对象 = XStudent元类对象)
NSLog(@"XStudent是否是XStudent元类 实例: %i",[XStudent isMemberOfClass:object_getClass([XStudent class])]);
// false (XStudent元类对象 != XPerson元类对象)
NSLog(@"XStudent是否是XPerson元类 实例: %i",[XStudent isMemberOfClass:objet_getClass([XPerson class])]);
```

## isKindOfClass

- 调用者是传入的类的实例对象，或者调用者是传入类的继承者链中的类的实例对象，则返回YES  
- 判断调用者是否是传入对象的子类，别弄反了  
- 去父类递归查找判断

## 源码：

```
+ (BOOL)isKindOfClass:(Class)cls {
    for (Class tcls = object_getClass((id)self); tcls; tcls = tcls->super_class) {
        if(tcls == cls) return YES;
    }
    return NO;
}
-（BOOL)isKindOfClass:(Class)cls {
    for(Class tcls = [self class]; tcls; tcls = tcls->super_class) {
        if(tcls == cls) return YES;
    }
    return NO;
}
```

## 实例代码：

```
XPerson* p1 = [[XPerson alloc]init];
XStudent* s1 = [[XStudent alloc]init];

// true (用s1的类对象、父类类对象、基类类对象([NSObject class]) 去和 p1的类对象比较，[p1 class]是s1的父类类对象)
NSLog(@"s1是否是p1 子类: %i",[s1 isKindOfClass:[p1 class]]);
// true (同上：[XPerson class] 与 [p1 class]是等同的)
NSLog(@"s1是否是XPerson 子类: %i",[s1 isKindOfClass:[XPerson class]]);
// true ([NSObject class]是s1的基类类对象)
NSLog(@"s1是否是NSObject 子类: %i",[s1 isKindOfClass:[NSObject class]]);

// false (用 XStudent的元类、父元类、基类(NSObject类对象) 去与 XPerson的对象比较)
NSLog(@"XStudent是否是XPerson 子类: %i",[XStudent isKindOfClass:[XPerson class]]);
// true (类方法需要传入 元类进去判断，里面会取 XStudent 元类去比较)
NSLog(@"XStudent是否是XPerson元类 子类: %i",[XStudent isKindOfClass:object_getClass([XPerson class])]);
// true (元类的最上层就是基元类)
NSLog(@"XStudent是否是NSObject元类 子类: %i",[XStudent isKindOfClass:object_getClass([NSObject class])]);
```
