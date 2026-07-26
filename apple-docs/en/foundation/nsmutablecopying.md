---
title: NSMutableCopying
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutablecopying
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablecopying'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablecopying.json'
content_hash: 'sha256:0a16385d187a63eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMutableCopying

<sub>Protocol</sub>

A protocol that mutable objects adopt to provide functional copies of themselves.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSMutableCopying
```

## Overview

The [NSMutableCopying](nsmutablecopying.md) protocol declares a method for providing mutable copies of an object. Only classes that define an “immutable vs. mutable” distinction should adopt this protocol. Classes that don’t define such a distinction should adopt [NSCopying](nscopying.md) instead.

[NSMutableCopying](nsmutablecopying.md) declares one method, [- mutableCopyWithZone:](<nsmutablecopying/mutablecopy(with_).md>), but mutable copying is commonly invoked with the convenience method [mutableCopy()](<../objectivec/nsobject-swift.class/mutablecopy().md>). The [mutableCopy()](<../objectivec/nsobject-swift.class/mutablecopy().md>) method is defined for all NSObjects and simply invokes [- mutableCopyWithZone:](<nsmutablecopying/mutablecopy(with_).md>) with the default zone.

If a subclass inherits [NSMutableCopying](nsmutablecopying.md) from its superclass and declares additional instance variables, the subclass has to override [- mutableCopyWithZone:](<nsmutablecopying/mutablecopy(with_).md>) to properly handle its own instance variables, invoking the superclass’s implementation first.

## Relationships

- **Conforming Types**: [NSArray](nsarray.md), [NSAttributedString](nsattributedstring.md), [NSCharacterSet](nscharacterset.md), [NSCountedSet](nscountedset.md), [NSData](nsdata.md), [NSDictionary](nsdictionary.md), [NSIndexSet](nsindexset.md), [NSMutableArray](nsmutablearray.md), [NSMutableAttributedString](nsmutableattributedstring.md), [NSMutableCharacterSet](nsmutablecharacterset.md), [NSMutableData](nsmutabledata.md), [NSMutableDictionary](nsmutabledictionary.md), [NSMutableIndexSet](nsmutableindexset.md), [NSMutableOrderedSet](nsmutableorderedset.md), [NSMutableSet](nsmutableset.md), [NSMutableString](nsmutablestring.md), [NSMutableURLRequest](nsmutableurlrequest.md), [NSOrderedSet](nsorderedset.md), [NSPurgeableData](nspurgeabledata.md), [NSSet](nsset.md), [NSString](nsstring.md), [NSURLRequest](nsurlrequest.md)

## Topics

### Copying

- [- mutableCopyWithZone:](<nsmutablecopying/mutablecopy(with_).md>) — Returns a new instance that’s a mutable copy of the receiver.

## See Also

### Copying

- [NSCopying](nscopying.md) — A protocol that objects adopt to provide functional copies of themselves.
