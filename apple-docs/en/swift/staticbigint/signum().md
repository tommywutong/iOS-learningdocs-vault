---
title: signum()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/staticbigint/signum()
source_url: 'https://developer.apple.com/documentation/swift/staticbigint/signum()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/staticbigint/signum%28%29.json'
content_hash: 'sha256:aa4ea8ae2ad43a11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StaticBigInt](../staticbigint.md)

# signum()

<sub>Instance Method</sub>

Indicates the value’s sign.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func signum() -> Int
```

## Return Value

`-1` if the value is less than zero, `0` if it is equal to zero, or `+1` if it is greater than zero.
