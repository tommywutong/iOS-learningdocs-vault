---
title: 'assetWriterInputGroupWithInputs:defaultInput:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinputgroup/assetwriterinputgroupwithinputs:defaultinput:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup/assetwriterinputgroupwithinputs:defaultinput:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputgroup/assetwriterinputgroupwithinputs%3Adefaultinput%3A.json'
content_hash: 'sha256:423eda1c0e8a896a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputGroup](../avassetwriterinputgroup.md)

# assetWriterInputGroupWithInputs:defaultInput:

<sub>Type Method</sub>

Returns a new group for the asset writer inputs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) assetWriterInputGroupWithInputs:(NSArray<AVAssetWriterInput *> *) inputs defaultInput:(AVAssetWriterInput *) defaultInput;
```

## Parameters

- `inputs` — The inputs with tracks to arrange into a mutually exclusive group.

- `defaultInput` — The group’s default input.

## Return Value

An asset writer input group.

## Discussion

When you add an input group to an asset writer, the system sets the default input’s [marksOutputTrackAsEnabled](../avassetwriterinput/marksoutputtrackasenabled.md) property value to [true](../../swift/true.md), and the value of the other inputs in the group to [false](../../swift/false.md).

## See Also

### Creating an input group

- [- initWithInputs:defaultInput:](<init(inputs_defaultinput_).md>) — Creates a group for the asset writer inputs.
