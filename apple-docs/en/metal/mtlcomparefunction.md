---
title: MTLCompareFunction
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomparefunction
source_url: 'https://developer.apple.com/documentation/metal/mtlcomparefunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomparefunction.json'
content_hash: 'sha256:f78ca6984136fe38'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCompareFunction

<sub>Enumeration</sub>

Options used to specify how a sample compare operation should be performed on a depth texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLCompareFunction
```

## Overview

Whenever the comparison test passes, the incoming fragment is compared to the stored data at the specified location.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Compare function options

- [MTLCompareFunctionNever](mtlcomparefunction/never.md) — A new value never passes the comparison test.
- [MTLCompareFunctionLess](mtlcomparefunction/less.md) — A new value passes the comparison test if it is less than the existing value.
- [MTLCompareFunctionEqual](mtlcomparefunction/equal.md) — A new value passes the comparison test if it is equal to the existing value.
- [MTLCompareFunctionLessEqual](mtlcomparefunction/lessequal.md) — A new value passes the comparison test if it is less than or equal to the existing value.
- [MTLCompareFunctionGreater](mtlcomparefunction/greater.md) — A new value passes the comparison test if it is greater than the existing value.
- [MTLCompareFunctionNotEqual](mtlcomparefunction/notequal.md) — A new value passes the comparison test if it is not equal to the existing value.
- [MTLCompareFunctionGreaterEqual](mtlcomparefunction/greaterequal.md) — A new value passes the comparison test if it is greater than or equal to the existing value.
- [MTLCompareFunctionAlways](mtlcomparefunction/always.md) — A new value always passes the comparison test.

### Initializers

- [init(rawValue:)](<mtlcomparefunction/init(rawvalue_).md>)

## See Also

### Declaring the depth comparison mode

- [compareFunction](mtlsamplerdescriptor/comparefunction.md) — The sampler comparison function used when performing a sample compare operation on a depth texture.
