---
title: 'resolveInstanceMethod(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/resolveinstancemethod(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/resolveinstancemethod(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/resolveinstancemethod%28_%3A%29.json'
content_hash: 'sha256:e2aca049fa024731'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# resolveInstanceMethod(_:)

<sub>类型方法</sub>

为实例方法的给定选择器动态提供实现。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func resolveInstanceMethod(_ sel: Selector!) -> Bool
```

## 参数

- `sel` — 要解析的选择器的名称。

## 返回值

若找到该方法并将其添加到接收者则为 [YES](../yes.md)，否则为 [NO](../no.md)。

## 讨论

此方法和 [+ resolveClassMethod:](<resolveclassmethod(__).md>) 允许你动态地为给定选择器提供实现。

Objective-C 方法只是至少接受两个参数——`self` 和 `_cmd`——的 C 函数。使用 [class_addMethod](<../class_addmethod(________).md>) 函数，你可以将函数作为方法添加到类中。给定以下函数：

```objc
void dynamicMethodIMP(id self, SEL _cmd)
{
    // implementation ....
}
```

你可以使用 `resolveInstanceMethod:` 动态地将其作为方法（称为 `resolveThisMethodDynamically`）添加到类中，如下所示：

```objc
+ (BOOL) resolveInstanceMethod:(SEL)aSEL
{
    if (aSEL == @selector(resolveThisMethodDynamically))
    {
          class_addMethod([self class], aSEL, (IMP) dynamicMethodIMP, "v@:");
          return YES;
    }
    return [super resolveInstanceMethod:aSel];
}
```

### 特殊注意事项

在调用 Objective-C 转发机制之前会调用此方法。若调用 [- respondsToSelector:](<../nsobjectprotocol/responds(to_).md>) 或 [+ instancesRespondToSelector:](<instancesrespond(to_).md>)，动态方法解析器会首先有机会为给定选择器提供 `IMP`。

## 另请参阅

### 动态解析方法

- [+ resolveClassMethod:](<resolveclassmethod(__).md>) — 为类方法的给定选择器动态提供实现。
