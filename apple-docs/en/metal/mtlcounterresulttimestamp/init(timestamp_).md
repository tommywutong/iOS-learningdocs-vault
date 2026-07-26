---
title: 'init(timestamp:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcounterresulttimestamp/init(timestamp:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcounterresulttimestamp/init(timestamp:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcounterresulttimestamp/init%28timestamp%3A%29.json'
content_hash: 'sha256:a16111e561ce1419'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterResultTimestamp](../mtlcounterresulttimestamp.md)

# init(timestamp:)

<sub>Initializer</sub>

Creates a timestamp result from a value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(timestamp: UInt64)
```

## Parameters

- `timestamp` — A timestamp value from a counter sample buffer.

## Discussion

Metal creates [MTLCounterResultTimestamp](../mtlcounterresulttimestamp.md) instances for you when you resolve the counter set’s data (see [Converting a GPU’s counter data into a readable format](../converting-a-gpus-counter-data-into-a-readable-format.md)). There’s no reason for you to manually create one in your app.

## See Also

### Swift support

- [init()](<init().md>) — Creates a default timestamp result.
