---
title: 'CFBridgingRetain(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/cfbridgingretain(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/cfbridgingretain(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/cfbridgingretain%28_%3A%29.json'
content_hash: 'sha256:8d5af16bd2cd7eb3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# CFBridgingRetain(_:)

<sub>Function</sub>

Casts an Objective-C pointer to a Core Foundation pointer and also transfers ownership to the caller.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBridgingRetain(_ X: Any?) -> CFTypeRef?
```

## Discussion

You use this function to cast an Objective-C object as Core Foundation-style object and take ownership of the object so that you can manage its lifetime. You are responsible for subsequently releasing the object, as illustrated in this example:

```objc
NSString *string = <#Get a string#>;
CFStringRef cfString = (CFStringRef)CFBridgingRetain(string);
// Use the CF string.
CFRelease(cfString);
```
