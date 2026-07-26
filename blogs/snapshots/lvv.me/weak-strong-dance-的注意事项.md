---
title: weak-strong dance 的注意事项
source_url: 'https://lvv.me/posts/2022/08/13_weak_strong_dance/'
source_domain: lvv.me
source_group: single-site
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:2665340c028b6cce'
plan_ref: 第二周：weak、属性关键字与 Block / Day 5｜循环引用是 Day 4 所有权图的推论（对应 W2-14、W2-16）
plan_week: 第二周：weak、属性关键字与 Block
plan_day: Day 5｜循环引用是 Day 4 所有权图的推论（对应 W2-14、W2-16）
container: '//*[contains(@class,''markdown-body'')]'
container_source: guess
---

> 原文：[weak-strong dance 的注意事项](https://lvv.me/posts/2022/08/13_weak_strong_dance/)

在使用逃逸 Block 的时候，为了防止 self 被循环引用，一般使用以下方式：

```objectivec
- (void)foo {
    __weak typeof(self) wself = self;
    [self auth:^(NSString *token) {
        typeof(self) self = wself;
        if (!self) { return; }
    }];
}
```

在 Block 外部定义一个 `__weak` 类型的 `self` 引用，在 Block 内部使用同名的局部 `self` 变量，以上的技巧就叫做 `weak-strong dance` 。

在 Block 里对实例变量都要通过局部定义的变量 `self` 来访问，否则就会发生循环引用的情况：

```objectivec
- (void)foo {
    __weak typeof(self) wself = self;
    [self auth:^(NSString *token) {
        typeof(self) self = wself;
        if (!self) { return; }

        _token = token; // 这里会使用隐式 self->_token
    }];
}
```

在 Block 里直接使用实例变量 `_token` 会在编译期间把隐式 `self` 转换为使用真正的 `self` 而不是局部变量 `self`，就会导致循环引用。

所以在使用 `weak-strong dance` 技巧的时候，Block 块内的实例变量都要使用 `self->` 来访问。

## Swift 中的 weak-strong dance

作为 Objective-C 的继任者，Swift 在语言特性上就支持 weak-strong dance ，而且用起来简单多了：

```swift
func foo() {
    auth { [weak self] (token) in
        guard let self = self else {  return }

        self.token = token
    }
}
```

## 什么情况下不需要 weak-strong dance ？

只有逃逸闭包才需要 weak-strong dance，非逃逸闭包没有必要使用 weak-strong dance，因为非逃逸闭包是即时执行而且超出作用范围后就被释放了。

定义非逃逸闭包：

Objective-C 使用 `NS_NOESCAPE` 标识闭包类型，当然实际是否逃逸还是需要开发者来保证，声明只是让使用者知道它是非逃逸的：

```objectivec
void foo:(void (^NS_NOESCAPE)(void))block {
}
```

Swift 默认**非可选类型**的闭包都是**非逃逸闭包**，如果需要把一个非可选类型闭包声明为**逃逸闭包**，需要增加 `@escaping` 声明：

```swift
func foo(block: @escaping () -> Void) {
}
```
