---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.swing/Classes/EOImageView.html
archived_at: '2026-07-15T08:13:54.494896Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

# EOImageView

> **__Inherits from:__**
> : javax.swing.JComponent : java.awt.Container : java.awt.Component : Object

> **__Implements:__**
> : java.io.Serializable: java.awt.image.ImageObserver: java.awt.MenuContainer

> **__Package:__**
> : com.webobjects.eointerface.swing

---

## Class Description

---

The EOImageView class is used to display images (java.awt.Image objects) in Swing applications.

## Constants

---

EOImageView defines the following `int` constants to specify the scaling behavior of an EOImageView:

|  |  |
| --- | --- |
| __Constant__ | __Scaling Behavior__ |
| ScaleNone | No scaling |
| ScaleProportionally | Scales in proportion to the image size |
| ScaleToFit | Scales to fit the portion of the user interface the image view occupies |
| ScaleProportionallyIfTooLarge | Scales in proportion to the image size, but only if the image is too large to fit its portion of the user interface (the image view never scales the image to be larger) |

## Interfaces Implemented

---

> : java.io.Serializable:
>
> : java.awt.image.ImageObserver
>
> : [imageUpdate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zpnfwwcz3fkvygiylumu)
>
> :
>
> : java.awt.MenuContainer:

## Method Types

---

> **All methods**
>
> : [EOImageView](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zpivhus3lbm5svm2lfo4): [image](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zpnfwwcz3f): [imageScaling](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zpnfwwcz3fknrwc3djnztq): [paint](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zpobqws3tu): [scalingHints](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zponrwc3djnztuq2loorzq): [setBorder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zponsxiqtpojsgk4q): [setBounds](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zponsxiqtpovxgi4y): [setImage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zponsxislnmftwk): [setImageScaling](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zponsxislnmftwku3dmfwgs3th): [setScalingHints](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zponsxiu3dmfwgs3thjbuw45dt)

## Constructors

---

### EOImageView

`public EOImageView()`

Description forthcoming.

---

## Instance Methods

---

### image

`public java.awt.Image image()`

Returns the receiver's image.

---

### imageScaling

`public int imageScaling()`

Returns the type of scaling the receiver uses. The return value is one of:

- [ScaleNone](#apple-ijceisscjjbuk)
- [ScaleProportionally](#apple-ijceiscfjbceq)
- [ScaleToFit](#apple-ijceiskejjbeg)
- [ScaleProportionallyIfTooLarge](#apple-ijceiq2eirceo)

---

### imageUpdate

`public boolean imageUpdate( java.awt.Image image, int flags, int x, int y, int width, int height)`

See the method description for __imageUpdate__ in Sun's JComponent class documentation.

---

### paint

`public void paint(java.awt.Graphics aGraphics)`

See the method description for __setBorder__ in Sun's JComponent class documentation.

---

### scalingHints

`public int scalingHints()`

Returns the receiver's scaling hints-a constant identifying the algorithm the receiver uses to scale its image.

---

### setBorder

`public void setBorder(javax.swing.border.Border aBorder)`

See the method description for __setBorder__ in Sun's JComponent class documentation.

---

### setBounds

`public void setBounds( int x, int y, int width, int height)`

See the method description for __setBounds__ in Sun's Component class documentation.

---

### setImage

`public void setImage(java.awt.Image image)`

Sets the receiver's image to _image_ and repaints (only if _image_ is different from the receiver's old image).

---

### setImageScaling

`public void setImageScaling(int imageScaling)`

Sets the scaling behavior of the receiver; that is, identifies the circumstances under which the receiver scales. The _imageScaling_ argument should be one of the following constants (defined in EOImageView):

- [ScaleNone](#apple-ijceisscjjbuk)
- [ScaleProportionally](#apple-ijceiscfjbceq)
- [ScaleToFit](#apple-ijceiskejjbeg)
- [ScaleProportionallyIfTooLarge](#apple-ijceiq2eirceo)

The default scaling behavior is `ScaleProportionallyIfTooLarge`. For more information on these constants, see ["Constants" (page 22)](#apple-ijceisccifdui).

---

### setScalingHints

`public void setScalingHints(int scalingHints)`

Sets the algorithm the receiver uses to scale it's image.The _scalingHints_ argument should be one of the following constants (defined in java.awt.Image):

- `SCALE_DEFAULT`
- `SCALE_FAST`
- `SCALE_SMOOTH`
- `SCALE_REPLICATE`
- `SCALE_AREA_AVERAGING`

The default is `SCALE_SMOOTH`. For more information on the algorithms identified by these constants, see Sun's Image class documentation.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
