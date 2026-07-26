---
title: CTRunDelegateGetTypeID()
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctrundelegategettypeid()
source_url: 'https://developer.apple.com/documentation/coretext/ctrundelegategettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrundelegategettypeid%28%29.json'
content_hash: 'sha256:b9f4ff18a6901b97'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRunDelegateGetTypeID()

<sub>Function</sub>

Returns the type of CTRunDelegate objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTRunDelegateGetTypeID() -> CFTypeID
```

## Discussion

The return type is a Core Foundation type (CTType).

## See Also

### Getting Information About a Run Delegate

- [CTRunDelegateGetRefCon](<ctrundelegategetrefcon(__).md>) — Returns a run delegate’s “refCon” value.
