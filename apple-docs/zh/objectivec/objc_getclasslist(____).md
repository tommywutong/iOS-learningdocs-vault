---
title: 'objc_getClassList(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_getclasslist(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_getclasslist(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_getclasslist%28_%3A_%3A%29.json'
content_hash: 'sha256:12bc2999ce64899f'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_getClassList(_:_:)

<sub>函数</sub>

Obtains the list of registered class definitions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_getClassList(_ buffer: AutoreleasingUnsafeMutablePointer<AnyClass>?, _ bufferCount: Int32) -> Int32
```

## 参数

- `buffer` — `Class` 值数组。输出时，每个 `Class` 值指向一个类定义，数量不超过 `bufferCount` 与已注册类总数中的较小者。可传入 `NULL` 以仅获取已注册类定义的总数，而不实际检索任何类定义。

- `bufferCount` — 整数值。传入你在 `buffer` 中已分配空间的指针数量。返回时，此函数仅填充该数量的元素。若该数量小于已注册类的数量，则此函数返回已注册类的任意子集。

## 返回值

表示已注册类总数的整数值。

## 讨论

Objective-C 运行时库会自动注册源代码中定义的所有类。你可以在运行时创建类定义，并通过 `objc_addClass` 函数注册它们。

以下代码示例演示如何使用此函数检索当前进程中已向 Objective-C 运行时注册的所有类定义。

```objc
int numClasses;
Class * classes = NULL;
 
classes = NULL;
numClasses = objc_getClassList(NULL, 0);
 
if (numClasses > 0 )
{
    classes = malloc(sizeof(Class) * numClasses);
    numClasses = objc_getClassList(classes, numClasses);
    free(classes);
}
```

### 特殊注意事项

不能假定从此函数获得的类对象一定继承自 [NSObject](nsobject-swift.class.md)，因此在未先检测方法是否已实现的情况下，不能安全地在这些类上调用任何方法。

## 另请参阅

### 获取类定义

- [objc_copyClassList](<objc_copyclasslist(__).md>) — 创建并返回一个指向所有已注册类定义的指针列表。
- [objc_lookUpClass](<objc_lookupclass(__).md>) — 返回指定类的类定义。
- [objc_getClass](<objc_getclass(__).md>) — 返回指定类的类定义。
- [objc_getRequiredClass](<objc_getrequiredclass(__).md>) — 返回指定类的类定义。
- [objc_getMetaClass](<objc_getmetaclass(__).md>) — 返回指定类的元类定义。
