---
title: 'loadValuesAsynchronouslyForKeys:completionHandler:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmetadataitem/loadvaluesasynchronouslyforkeys:completionhandler:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/loadvaluesasynchronouslyforkeys:completionhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/loadvaluesasynchronouslyforkeys%3Acompletionhandler%3A.json'
content_hash: 'sha256:33a55909d1c6b2f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# loadValuesAsynchronouslyForKeys:completionHandler:

<sub>Instance Method</sub>

Tells the object to load the values of any of the specified keys that aren’t already loaded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) loadValuesAsynchronouslyForKeys:(NSArray<NSString *> *) keys completionHandler:(void (^)()) handler;
```

## Parameters

- `keys` — An array of [NSString](../../foundation/nsstring.md) objects, each of which represents one of the required keys.

- `handler` — The block to invoke when loading succeeds, fails, or is canceled.

## Discussion

For full discussion, see [AVAsynchronousKeyValueLoading](../avasynchronouskeyvalueloading.md).

## See Also

### Accessing values

- [value](value.md) — The value of the metadata item. _(deprecated)_
- [extraAttributes](extraattributes.md) — A dictionary of additional attributes for a metadata item. _(deprecated)_
- [stringValue](stringvalue.md) — The value of the metadata item as a string. _(deprecated)_
- [numberValue](numbervalue.md) — The value of the metadata item as a number. _(deprecated)_
- [dateValue](datevalue.md) — The value of the metadata item as a date. _(deprecated)_
- [dataValue](datavalue.md) — The value of the metadata item as a data value. _(deprecated)_
- [statusOfValueForKey:error:](statusofvalueforkey_error_.md) — Reports whether the value for a given key is immediately available without blocking.
