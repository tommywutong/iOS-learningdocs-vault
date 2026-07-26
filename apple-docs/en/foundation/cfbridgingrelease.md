---
title: CFBridgingRelease
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/cfbridgingrelease
source_url: 'https://developer.apple.com/documentation/foundation/cfbridgingrelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/cfbridgingrelease.json'
content_hash: 'sha256:9fffa11508731088'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# CFBridgingRelease

<sub>Function</sub>

Moves a non-Objective-C pointer to Objective-C and also transfers ownership to ARC.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
static idCFBridgingRelease(CFTypeRef X);
```

## Discussion

You use this function to cast a Core Foundation-style object as an Objective-C object and transfer ownership of the object to ARC such that you don’t have to release the object, as illustrated in this example:

```objc
CFStringRef cfName = ABRecordCopyValue(person, kABPersonFirstNameProperty);
NSString *name = (NSString *)CFBridgingRelease(cfName);
```

## See Also

### Core Foundation ARC Integration

- [CFBridgingRetain](<cfbridgingretain(__).md>) — Casts an Objective-C pointer to a Core Foundation pointer and also transfers ownership to the caller.
