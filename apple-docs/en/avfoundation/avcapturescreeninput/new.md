---
title: new
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.7+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturescreeninput/new
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/new'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturescreeninput/new.json'
content_hash: 'sha256:0764589f18b98cb0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureScreenInput](../avcapturescreeninput.md)

# new

<sub>Type Method</sub>

Creates a capture screen input that provides media data from the main screen.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) new;
```

## Discussion

Using this method is equivalent to calling [- initWithDisplayID:](<init(displayid_).md>) with the result of the [CGMainDisplayID()](<../../coregraphics/cgmaindisplayid().md>) function.

## See Also

### Initializing a capture screen input

- [- initWithDisplayID:](<init(displayid_).md>) — Initializes a capture screen input that provides media data from the specified display.
- [- init](<init().md>) — Initializes a capture screen input that provides media data from the main screen.
