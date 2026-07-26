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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# browserAccessibilityImageDataSize

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSValue *) browserAccessibilityImageDataSize;
```

## Return Value

An NSValue wrapping a CGSize, or nil if this element does not represent an image.

## Discussion

Returns the native pixel dimensions of the image represented by this element.
