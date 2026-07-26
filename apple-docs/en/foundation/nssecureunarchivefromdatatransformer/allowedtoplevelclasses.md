---
title: allowedTopLevelClasses
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nssecureunarchivefromdatatransformer/allowedtoplevelclasses
source_url: 'https://developer.apple.com/documentation/foundation/nssecureunarchivefromdatatransformer/allowedtoplevelclasses'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssecureunarchivefromdatatransformer/allowedtoplevelclasses.json'
content_hash: 'sha256:5ee96a91cf50066f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSecureUnarchiveFromDataTransformer](../nssecureunarchivefromdatatransformer.md)

# allowedTopLevelClasses

<sub>Type Property</sub>

A list of allowed classes the top-level object in an archive must conform to, for encoding and decoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var allowedTopLevelClasses: [AnyClass] { get }
```

## Discussion

This property contains the value of [+ transformedValueClass](<../valuetransformer/transformedvalueclass().md>) if that value isn’t `nil`. Otherwise, it holds a list of the top level classes that it decodes, which includes [NSArray](../nsarray.md), [NSDictionary](../nsdictionary.md), [NSSet](../nsset.md), [NSString](../nsstring.md), [NSNumber](../nsnumber.md), [NSDate](../nsdate.md), [NSData](../nsdata.md), [NSURL](../nsurl.md), [NSUUID](../nsuuid.md), and [NSNull](../nsnull.md).

Override this property in subclasses to provide an expanded or different set of allowed transformation classes.
