---
title: 使用关联引用在 Objective-C 分类中模拟实例变量
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/05/faking-ivars-in-objc-categories-with-associative-references/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:77d0eb63a6ed5e00'
translated: true
---

> 原文：[Faking Instance Variables in Objective-C Categories With Associative References](https://oleb.net/blog/2011/05/faking-ivars-in-objc-categories-with-associative-references/)　·　Ole Begemann

# 使用关联引用在 Objective-C 分类中模拟实例变量

在 OS X 10.6 和 iOS 3.1 中，Apple 向 Objective-C 运行时添加了[关联引用（Associative References）](http://developer.apple.com/library/ios/#documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocAssociativeReferences.html)。从根本上说，这意味着每个对象都有一个可选的字典，你可以向其中添加任意键/值对。

这是一个很棒的特性，尤其是考虑到 Objective-C 长期以来就有一个可以向现有类添加*方法*的特性：[分类](http://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocCategories.html#//apple_ref/doc/uid/TP30001163-CH20-SW1)。然而，分类不允许你添加实例变量。利用关联引用，可以轻松地模拟 ivar。

在 Objective-C 运行时的 C API 中，你可以通过以下两个函数向对象添加键/值对并再次读取：

```
void objc_setAssociatedObject(id object, const void *key, id value, objc_AssociationPolicy policy)
id objc_getAssociatedObject(id object, const void *key)
```

如果我们将这些调用包装在属性的自定义 getter 和 setter 中，就可以使模拟的“ivar”实现对 API 使用者完全透明。

# 使用对象标记 UIView

举个例子，假设我们想为 `UIView` 添加一个能力，使其可以附加一个任意对象作为标记（`UIView` 现有的 `tag` 属性只接受整数，有时会比较受限）。我们的“对象标记”分类的接口可以这样写：

```
@interface UIView (ObjectTagAdditions)

@property (nonatomic, retain) id objectTag;

- (UIView *)viewWithObjectTag:(id)object;

@end
```

使用关联引用，该属性的实现非常直接：

```
#import <objc/runtime.h>

static char const * const ObjectTagKey = "ObjectTag";

@implementation UIView (ObjectTagAdditions)
@dynamic objectTag;

- (id)objectTag {
    return objc_getAssociatedObject(self, ObjectTagKey);
}

- (void)setObjectTag:(id)newObjectTag {
    objc_setAssociatedObject(self, ObjectTagKey, newObjectTag, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
}

...
```

通过指定 `OBJC_ASSOCIATION_RETAIN_NONATOMIC`，我们告诉运行时为我们 retain 该值。其他可能的值有 `OBJC_ASSOCIATION_ASSIGN`、`OBJC_ASSOCIATION_COPY_NONATOMIC`、`OBJC_ASSOCIATION_RETAIN`、`OBJC_ASSOCIATION_COPY`，分别对应我们熟悉的属性声明特性。

**更新于 2011 年 12 月 22 日：** 需要注意，关联的键是一个 void 指针 `void *key`，而不是字符串。这意味着在检索关联引用时，你必须向运行时传入完全相同的指针。如果你使用 C 字符串作为键，然后将该字符串复制到内存中的另一个位置，并尝试通过指向复制后字符串的指针来访问关联引用，将无法达到预期效果。

最后，这是递归方法 `-viewWithObjectTag:` 的代码：

```
- (UIView *)viewWithObjectTag:(id)object {
    // 如果 object 为 nil，则抛出异常
    if (object == nil) {
        [NSException raise:NSInternalInconsistencyException format:@"Argument to -viewWithObjectTag: must not be nil"];
    }

    // 递归搜索视图层级结构，查找指定的 objectTag
    if ([self.objectTag isEqual:object]) {
        return self;
    }
    for (UIView *subview in self.subviews) {
        UIView *resultView = [subview viewWithObjectTag:object];
        if (resultView != nil) {
            return resultView;
        }
    }
    return nil;
}
```

**更新于 2011 年 5 月 16 日：** Vadim Shpakovski [在 Twitter 上询问](https://twitter.com/vadimshpakovski/status/69894923800952832)，为什么当 `viewWithObjectTag:` 的参数为 `nil` 时，我选择生成一个异常而不是向调用者返回 `nil`。原因是返回 `nil` 会产生歧义，因为它意味着没有找到具有指定 `objectTag` 的视图。由于 `nil` 是 `objectTag` 的默认值，这种情况极不可能发生。

一个很好的替代方案是返回第一个 `objectTag` 确实为 `nil` 的视图，就像 `viewWithTag:` 所做的那样。我没有选择这样做，因为我猜想使用 `nil` 参数调用 `-viewWithObjectTag:` 更可能是程序员的错误，而非有意使用。不过，这只是个人偏好的问题。

---

**更新于 2011 年 12 月 22 日：** 改进了 `ObjectTagKey` 指针的声明，并在代码示例中添加了缺失的 `#import` 语句。
