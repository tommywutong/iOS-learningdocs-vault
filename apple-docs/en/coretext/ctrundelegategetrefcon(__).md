---
title: 'CTRunDelegateGetRefCon(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctrundelegategetrefcon(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctrundelegategetrefcon(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrundelegategetrefcon%28_%3A%29.json'
content_hash: 'sha256:575baa688955b12d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunDelegateGetRefCon(_:)

<sub>Function</sub>

Returns a run delegate’s “refCon” value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTRunDelegateGetRefCon(_ runDelegate: CTRunDelegate) -> UnsafeMutableRawPointer
```

## Parameters

- `runDelegate` — The run delegate object being queried.

## Return Value

A constant value associated with the run delegate as an identifier.

## Discussion

The run delegate object was created with the returned “refCon” value.

## See Also

### Getting Information About a Run Delegate

- [CTRunDelegateGetTypeID](<ctrundelegategettypeid().md>) — Returns the type of CTRunDelegate objects.
