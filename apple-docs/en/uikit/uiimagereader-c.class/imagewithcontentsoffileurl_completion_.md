---
title: 'imageWithContentsOfFileURL:completion:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimagereader-c.class/imagewithcontentsoffileurl:completion:'
source_url: 'https://developer.apple.com/documentation/uikit/uiimagereader-c.class/imagewithcontentsoffileurl:completion:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagereader-c.class/imagewithcontentsoffileurl%3Acompletion%3A.json'
content_hash: 'sha256:922d853526fa3536'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageReader](../uiimagereader-c.class.md)

# imageWithContentsOfFileURL:completion:

<sub>Instance Method</sub>

Asynchronously generate an image from the given file URL. If an image could not be generated, the completion will be called with nil.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) imageWithContentsOfFileURL:(NSURL *) url completion:(void (^)(UIImage *)) completion;
```
