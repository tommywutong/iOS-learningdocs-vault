---
title: 'copyTaggedBufferGroupForHostTime:presentationTimeStamp:activeConfiguration:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.2+, iPadOS 17.2+, Mac Catalyst 17.2+, macOS 14.2+, tvOS 17.2+, visionOS 1.1+, watchOS 10.2+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayervideooutput/copytaggedbuffergroupforhosttime:presentationtimestamp:activeconfiguration:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayervideooutput/copytaggedbuffergroupforhosttime:presentationtimestamp:activeconfiguration:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayervideooutput/copytaggedbuffergroupforhosttime%3Apresentationtimestamp%3Aactiveconfiguration%3A.json'
content_hash: 'sha256:1a0963a0bc1fa1bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerVideoOutput](../avplayervideooutput.md)

# copyTaggedBufferGroupForHostTime:presentationTimeStamp:activeConfiguration:

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (CMTaggedBufferGroupRef) copyTaggedBufferGroupForHostTime:(CMTime) hostTime presentationTimeStamp:(CMTime *) presentationTimeStampOut activeConfiguration:(AVPlayerVideoOutputConfiguration **) activeConfigurationOut;
```

## See Also

### Accessing video data

- [Configuration](configuration.md) — An object that provides configuration information for the related player item.
