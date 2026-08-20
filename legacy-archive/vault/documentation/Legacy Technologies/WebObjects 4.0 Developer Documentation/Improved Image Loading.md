---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.036.html
archived_at: '2026-07-15T07:58:43.781025Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.035.md)

# Improved Image Loading

To make it easier to display images from a database, the following attributes have been added to WOActiveImage, WOImage, WOImageButton, WOFrame, WOBody, and WOEmbeddedObject.

|  Attribute |  Description |
|  data |  An NSData object containing the image or embedded object. |
|  mimeType |  The MIME type of the image to be put in the content-type header field. |
|  key |  The key under which the data is stored in an application-wide cache. If the key is already in the image cache table, then the value isn't computed again. This attribute is optional; the default is a random key, which means the data will be removed from the cache after access. |

```
```


Images are cached by the WOResourceManager object. The following are new methods on WOResourceManager that access the image cache:

|  WOResourceManager |  |
|  Method |  Description |
|  flushDataCache |  Removes all data from the image data cache. |
|  setData:forKey:mimeType:session: (Objective-C)  setData (Java) |  Adds image data of the specified type to the data cache with the specified key. |
|  removeDataForKey:session: (Objective-C)  removeDataForKey (Java) |  Removes the data for the specified key from the image data cache. The session argument is ignored. |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](New%20Methods.md)
