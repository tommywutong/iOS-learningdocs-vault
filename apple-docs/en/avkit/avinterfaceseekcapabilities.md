---
title: AVInterfaceSeekCapabilities
framework: AVKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinterfaceseekcapabilities
source_url: 'https://developer.apple.com/documentation/avkit/avinterfaceseekcapabilities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfaceseekcapabilities.json'
content_hash: 'sha256:b73de6b023b4bf6e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVInterfaceSeekCapabilities

<sub>Enumeration</sub>

Describes navigation capabilities of the media source.

<sub>tvOS, visionOS</sub>

```objc
enum AVInterfaceSeekCapabilities : NSUInteger;
```

## Overview

This option set defines timeline navigation operations. Different content types and sources may have varying levels of navigation support based on technical limitations, licensing restrictions, or content type.

## Topics

### Enumeration Cases

- [AVInterfaceSeekCapabilitiesNone](avinterfaceseekcapabilities/avinterfaceseekcapabilitiesnone.md) — The source does not support any scanning or seeking operations.
- [AVInterfaceSeekCapabilitiesScanBackward](avinterfaceseekcapabilities/avinterfaceseekcapabilitiesscanbackward.md) — The source supports backward scanning at accelerated rates for rewind operations. Enables rapid reverse progression through content at speeds greater than normal playback.
- [AVInterfaceSeekCapabilitiesScanForward](avinterfaceseekcapabilities/avinterfaceseekcapabilitiesscanforward.md) — The source supports forward scanning at accelerated rates for fast-forward operations. Enables rapid progression through content at speeds greater than normal playback.
- [AVInterfaceSeekCapabilitiesSeek](avinterfaceseekcapabilities/avinterfaceseekcapabilitiesseek.md) — The source supports seeking to specific time positions for precise navigation. Enables jumping directly to any arbitrary point within the seekable time ranges.
