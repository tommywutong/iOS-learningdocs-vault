---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.045.html
archived_at: '2026-07-15T07:58:49.510060Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.044.md)

### WOIFrame Component

The WOIFrame component inserts an IFRAME tag into your page. This tag is a container to create an in-line or floating frame: a frame in which the contents of another HTML document can be seen. The difference between an IFRAME and a normal frame is that the floating frame can be seen inside a document and is treated as a part of the document. This means that when you scroll through the page the frame will scroll with it. IFRAME tags are supported by Microsoft's Internet Explorer browser.
WOIFrame has three special _mutually-exclusive_ attributes, all of which are identical to WOFrame:

|  WOIFrame |  |
|  Attribute |  Description |
|  src |  External source that will supply the content for this frame. |
|  pageName |  Name of a WebObjects component that will supply the content for this frame. |
|  value |  Method that will supply the content for this frame. |

```
```


The WOIFrame component's remaining attributes are simply passed through to the IFRAME:

|  WOIFrame |  |
|  Attribute |  Description |
|  frameborder |  Specifies whether or not a border should be displayed for the frame. |
|  height |  Specify the height of the frame to the browser, either as a number of pixels or as a percentage of the current screen height. |
|  marginheight |  An optional attribute that controls the vertical margins for the frame (margins are specified in pixels). |
|  marginwidth |  An optional attribute that controls the horizontal margins for the frame (margins are specified in pixels). |
|  name |  An optional argument that assigns a name to a frame so it can be targeted by links in other documents or, more commonly, from other frames in the same document. |
|  scrolling |  Specifies whether or not the frame should have a scrollbar. Optional. |
|  width |  Specifies the height of the frame to the browser, either as a number of pixels or as a percentage of the current screen height. |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.046.md)
