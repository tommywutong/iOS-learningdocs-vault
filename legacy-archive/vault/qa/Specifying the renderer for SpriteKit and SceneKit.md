---
title: Specifying the renderer for SpriteKit and SceneKit
apple_id: DTS40016604
resource_type: QA
platform: iOS|macOS
topic: Graphics & Animation
technology: null
published: '2015-10-08'
source_url: https://developer.apple.com/library/archive/qa/qa1904/_index.html
archived_at: '2026-07-27T06:57:05.415169Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1904

# Specifying the renderer for SpriteKit and SceneKit

## Q:  How can I specify the renderer for SpriteKit and SceneKit?

A: By default, SpriteKit and SceneKit render with Metal in iOS 9 and OS X El Capitan, however, there is a facility to use OpenGL.

__Important:__ For optimal performance, Metal rendering in SpriteKit and SceneKit is enabled by default. Setting __PrefersOpenGL__ rendering key is not recommended unless it is determined necessary for other reasons.

To do that:

1. Edit your app's Info.plist
2. Add the `PrefersOpenGL` key with a bool value of __YES__

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-10-08 | New document that explains how to fall back to the OpenGL renderer for SpriteKit and SceneKit. |
