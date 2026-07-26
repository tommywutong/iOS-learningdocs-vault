---
title: activityImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivity/activityimage
source_url: 'https://developer.apple.com/documentation/uikit/uiactivity/activityimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivity/activityimage.json'
content_hash: 'sha256:1e85d067ee3e44a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivity](../uiactivity.md)

# activityImage

<sub>Instance Property</sub>

An image that identifies the service to the user.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var activityImage: UIImage? { get }
```

## Discussion

The default value is `nil`. Subclasses must override this property to return a valid image object that can be presented to the user. The [UIActivityViewController](../uiactivityviewcontroller.md) object uses this image to generate a button for your service in its UI.

The alpha channel of the image is used as a mask to generate the final image that’s presented to the user. Any color data in the image itself is ignored. Opaque pixels have a gradient applied to them, and this gradient is then laid on top of a standard background. Thus, a completely opaque image would yield a gradient-filled rectangle.

For iPhone and iPod touch, images on iOS 7 should be 60 by 60 points; on earlier versions of iOS, you should use images no larger than 43 by 43 points. For iPad, images on iOS 7 should be 76 by 76 points; on earlier versions of iOS, you should use images no larger than 60 by 60 points. On a device with Retina display, the number of pixels is doubled in each direction.

## See Also

### Getting the activity information

- [activityCategory](activitycategory.md) — The category of the activity, which may be used to group activities in the UI.
- [Category](category.md) — An enumeration that defines categories of activities.
- [activityType](activitytype-swift.property.md) — The type of service being provided.
- [ActivityType](activitytype-swift.struct.md) — A structure that describes the types of activities for which the system has built-in support.
- [activityTitle](activitytitle.md) — A user-readable string that describes the service.
