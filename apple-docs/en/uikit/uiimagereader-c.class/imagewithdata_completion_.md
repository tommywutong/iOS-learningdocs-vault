---
title: 'imageWithData:completion:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimagereader-c.class/imagewithdata:completion:'
source_url: 'https://developer.apple.com/documentation/uikit/uiimagereader-c.class/imagewithdata:completion:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagereader-c.class/imagewithdata%3Acompletion%3A.json'
content_hash: 'sha256:cb72540167268f22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageReader](../uiimagereader-c.class.md)

# imageWithData:completion:

<sub>Instance Method</sub>

Asynchronously generate an image from the given data. If an image could not be generated, the completion will be called with nil.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) imageWithData:(NSData *) data completion:(void (^)(UIImage *)) completion;
```
