---
title: isProxy()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobjectprotocol/isproxy()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/isproxy()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/isproxy%28%29.json'
content_hash: 'sha256:ecaaeb46038ebee2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# isProxy()

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver does not descend from [NSObject](../nsobject-swift.class.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isProxy() -> Bool
```

## Return Value

[NO](../no.md) if the receiver really descends from [NSObject](../nsobject-swift.class.md), otherwise [YES](../yes.md).

## Discussion

This method is necessary because sending [- isKindOfClass:](<iskind(of_).md>) or [- isMemberOfClass:](<ismember(of_).md>) to an [NSProxy](../../foundation/nsproxy.md) object will test the object the proxy stands in for, not the proxy itself. Use this method to test if the receiver is a proxy (or a member of some other root class).
