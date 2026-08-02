---
title: Audio Unit Resizing
apple_id: DTS10003212
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2004-03-23'
source_url: https://developer.apple.com/library/archive/qa/qa1343/_index.html
archived_at: '2026-07-18T02:30:25.514356Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1343

# Audio Unit Resizing

## Q:  How do Audio Unit plugins and Audio Unit hosts negotiate the resizing of the Audio Unit's UI? A: Some Audio Unit plugins may want to resize their UI within the hosting application. These changes can be based on the internal parameter state (and many other UI considerations) within each Audio Unit plugin.

A: A plugin should never resize its view's window, but instead resize the control it returns to the host when the plugin's view is first created. It is the host's responsibility to listen for changes to the bounds of that control, and then resize the view for the Audio Unit to fit within the confines of the application.

The Audio Unit's Carbon control is received by the host when the view is first created by using AudioUnitCarbonViewCreate . The host should create a listener for changes to the Audio Unit's view bounds by using AudioUnitCarbonViewSetEventListener with the event kEventControlBoundsChanged . Thus, when an Audio Unit needs to change its view size all it needs to do is resize the view's control. The host is setup to listen for changes to this control. When the kEventControlBoundsChanged event is received by the host, it can resize the Audio Unit window within the application.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-03-23 | New document that discusses the host's responsibilities when resizing Audio Units. |

