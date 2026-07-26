---
title: 'loadValuesAsynchronously(forKeys:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avasynchronouskeyvalueloading/loadvaluesasynchronously(forkeys:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/loadvaluesasynchronously(forkeys:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronouskeyvalueloading/loadvaluesasynchronously%28forkeys%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:610c7df283196e06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousKeyValueLoading](../avasynchronouskeyvalueloading.md)

# loadValuesAsynchronously(forKeys:completionHandler:)

<sub>Instance Method</sub>

Tells the asset to load the values of all of the specified keys that aren’t already loaded.

> [!warning] Deprecated
> Use [load(_:isolation:)](<load(__isolation_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadValuesAsynchronously(forKeys keys: [String], completionHandler handler: (@Sendable () -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadValues(forKeys keys: [String]) async
```

## Parameters

- `keys` — An array of strings containing the keys to load. The keys are the property names of a class that adopts the protocol.

- `handler` — The closure the system calls when the load request completes.

## Discussion

Regardless of the number of keys specified, the system calls the completion handler only once per invocation of this method. The system calls this method:

- Synchronously if the asset already loaded the specified keys, or if an I/O error or other format-related error occurs immediately.
- Asynchronously when the values of the specified keys become loaded, if a loading error occurs at a later stage of processing, or you cancel loading. The system calls the closure on a background queue, so you should dispatch control back to the main queue before performing any user interface-related operations.

The completion states of the specified keys aren’t necessarily the same—some may return loaded, and others may have failed. Check the status of each key individually using the [- statusOfValueForKey:error:](<statusofvalue(forkey_error_).md>) method.

The following example shows how to use this method to load an asset’s [playable](../avasset/isplayable.md) key:

```objc
// Load the asset's "commonMetadata" key
[asset loadValuesAsynchronouslyForKeys:@[@"commonMetadata"] completionHandler:^{
    NSError *error = nil;
    AVKeyValueStatus status =
        [asset statusOfValueForKey:@"commonMetadata" error:&error];
    switch (status) {
        case AVKeyValueStatusLoaded:
            // The property successfully loaded. Continue processing.
             break;
        case AVKeyValueStatusFailed:
            // Examine the NSError pointer to determine the failure.
            break;
        case AVKeyValueStatusCancelled:
            // The asset canceled loading.
            break;
        default:
            // Handle all other cases.
            break;
    }
}];
```

## See Also

### Deprecated

- [Deprecated symbols](../avasynchronouskeyvalueloading-deprecated-symbols.md) — Review unsupported symbols and their replacements.
- [- statusOfValueForKey:error:](<statusofvalue(forkey_error_).md>) — Returns a status that indicates whether a property value is immediately available without blocking the calling thread. _(deprecated)_
- [AVKeyValueStatus](../avkeyvaluestatus.md) — Values that indicate the loaded status of a property. _(deprecated)_
