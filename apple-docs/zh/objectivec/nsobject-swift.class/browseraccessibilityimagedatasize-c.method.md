---
title: browserAccessibilityImageDataSize
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, macOS, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/browseraccessibilityimagedatasize-c.method
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/browseraccessibilityimagedatasize-c.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/browseraccessibilityimagedatasize-c.method.json'
content_hash: 'sha256:d6893ebd87c898a4'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# browserAccessibilityImageDataSize

<sub>实例方法</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSValue *) browserAccessibilityImageDataSize;
```

## 返回值

包装 CGSize 的 NSValue；如果此元素不表示图像，则为 nil。

## 讨论

返回此元素所表示图像的原生像素尺寸。
