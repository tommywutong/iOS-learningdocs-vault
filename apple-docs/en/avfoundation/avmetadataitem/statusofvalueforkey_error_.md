---
title: 'statusOfValueForKey:error:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmetadataitem/statusofvalueforkey:error:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/statusofvalueforkey:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/statusofvalueforkey%3Aerror%3A.json'
content_hash: 'sha256:b75079e2da4a0aaa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# statusOfValueForKey:error:

<sub>Instance Method</sub>

Reports whether the value for a given key is immediately available without blocking.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (AVKeyValueStatus) statusOfValueForKey:(NSString *) key error:(NSError **) outError;
```

## Parameters

- `key` — The key whose status you want.

- `outError` — If the status of the value for the key is [AVKeyValueStatusFailed](../avkeyvaluestatus/failed.md), upon return contains an [NSError](../../foundation/nserror.md) object that describes the failure that occurred.

## Return Value

The current loading status of the value for `key`.

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
- [loadValuesAsynchronouslyForKeys:completionHandler:](loadvaluesasynchronouslyforkeys_completionhandler_.md) — Tells the object to load the values of any of the specified keys that aren’t already loaded.
