---
title: KVO的实现原理
source_url: 'https://blog.csdn.net/zhoupengju/article/details/53129436'
source_domain: blog.csdn.net
source_group: platform
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:c363343047088ab5'
plan_ref: 第三周：Runtime 行为与 Cocoa 对象通信 / Day 5｜KVC 提供间接访问，KVO 在它的约定上插入通知（对应 W3-09）
plan_week: 第三周：Runtime 行为与 Cocoa 对象通信
plan_day: Day 5｜KVC 提供间接访问，KVO 在它的约定上插入通知（对应 W3-09）
container: '//div[@id=''content_views'']'
container_source: map
---

> 原文：[KVO的实现原理](https://blog.csdn.net/zhoupengju/article/details/53129436)

KVO：key-value observing 键值监听

未添加KVO监听的类， person.isa = PJPerson  
 给PJPerson添加KVO监听之后，RunTime会动态的添加一个类NSKVONotifying_PJPerson，这个类是PJPerson的子类 person.isa = NSKVONotifying_PJPerson

KVO的本质其实就是：利用runtime的动态属性给PJPerson添加一个子类，person通过isa指针找到这个子类的setAge类实现，这个setAge方法里面做了一些特殊的处理

1. 调用_NSSetIntValueAndNotify方法 (Foundation`_NSSetIntValueAndNotify) (通过[self.person1 methodForSelector:@selector(setAge:)] p (IMP)0x10816bcf2 就能获取到)
2. NSSetIntValueAndNotify的实现  
   2.1 [self willChangeValueForKey:@“age”];  
   2.2 [super setAge:age];  
   2.3 [self didChangeValueForKey:@“age”];  
   2.3.1 didChangeValueForKey的实现 通知监听器[observe observeValueForKeyPath:key ofObject:self change:0 context:nil]
3. 监听到属性的改变

-(void)setAge:(int)age {

```
// Foundation
_NSSetIntValueAndNotify();
```

}  
 object_getClass(self) 返回的才是真实的类

- (Class)class {  
   // 屏蔽内部实现， 隐藏了NSKVONotifying_PJPerson类的实现  
   }
- (void)dealloc {  
   // 做一些善后工作  
   }
- (BOOL)_isKVOA {  
   return YES;  
   }

利用RunTime打印类内部所有的方法

- (void)printMethodNamesOfClass:(Class)cls {

  unsigned int count;  
   NSMutableString *methodNames = [NSMutableString string];  
   Method *methodList = class_copyMethodList(cls, &count);  
   for (int i=0; i\<count; i++) {  
   Method method = methodList[i];

  ```
    NSString *methodName = NSStringFromSelector(method_getName(method));

    [methodNames appendString:methodName];
    [methodNames appendString:@", "];
  ```

  }

  free(methodList);

  NSLog(@"%@, %@", cls, methodNames);  
   }

KVO的本质是什么？  
 利用runtime的api动态的生成一个子类，并且让instance对象的isa指针指向它  
 当修改instance对象的属性时，会调用Foundation的`_NSSetIntValueAndNotify函数， 在_NSSetIntValueAndNotify函数内部  
 willChangeValueForKey:  
 调用父类原来的setter方法  
 didChangeValueForKey:  
 内部触发监听器（Oberser）的监听方法（observeValueForKeyPath:ofObject: change: context:）  
 KVO的本质其实就是改变了setAge方法的实现，能不能监听，其实就是看有没有setter方法  
 说到底就是修改了isa指针的指向，重写了setAge方法，替换了它的实现_NSSetIntValueAndNotify  
 重写class，dealloc方法

如何手动触发KVO  
 手动调用willChangeValueForKey和didChangeValueForKey

直接修改成员变量会触发KVO吗？  
 不会触发  
 切记，成员变量不是属性。  
 但可以手动的去触发它  
 [self.person1 willChangeValueForKey:@“age”];  
 self.person1-\>_age = 22;  
 [self.person1 didChangeValueForKey:@“age”];
