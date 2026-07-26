---
title: beginConfiguration()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/beginconfiguration()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/beginconfiguration()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/beginconfiguration%28%29.json'
content_hash: 'sha256:0c739e56c9326f4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# beginConfiguration()

<sub>Instance Method</sub>

Marks the beginning of changes to a running capture session’s configuration to perform in a single atomic update.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func beginConfiguration()
```

## Discussion

Call this method and [- commitConfiguration](<commitconfiguration().md>) to batch multiple configuration operations on a running session into an atomic update.

After you call this method, you can add or remove outputs, alter the [sessionPreset](sessionpreset.md), or configure individual capture input or output properties. The session configuration doesn’t change until you invoke [- commitConfiguration](<commitconfiguration().md>), at which the system updates all settings. You can nest [- beginConfiguration](<beginconfiguration().md>) and [- commitConfiguration](<commitconfiguration().md>) pairs, and the system applies the changes when you call the outermost commit.

## See Also

### Configuring a session

- [- commitConfiguration](<commitconfiguration().md>) — Commits one or more changes to a running capture session’s configuration in a single atomic update.
