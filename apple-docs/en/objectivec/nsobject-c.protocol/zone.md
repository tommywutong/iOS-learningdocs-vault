---
title: zone
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-c.protocol/zone
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-c.protocol/zone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-c.protocol/zone.json'
content_hash: 'sha256:ddf6b7cb1646dbec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# zone

<sub>Instance Method</sub>

Zones are deprecated and ignored by most classes that have it as a parameter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (struct _NSZone *) zone;
```

## Return Value

A pointer to the zone from which the receiver was allocated.

## See Also

### Obsolete Methods

- [retain](retain.md) — Increments the receiver’s reference count.
- [release](release.md) — Decrements the receiver’s reference count.
- [autorelease](autorelease.md) — Decrements the receiver’s retain count at the end of the current autorelease pool block.
- [retainCount](retaincount.md) — Do not use this method.
