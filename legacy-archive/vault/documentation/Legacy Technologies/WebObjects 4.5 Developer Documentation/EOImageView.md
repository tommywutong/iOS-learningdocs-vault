---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOImageView.html
archived_at: '2026-07-15T08:11:44.841272Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOImageView

> **__Inherits
> from:__**
> : javax.swing.JComponent
> java.awt.Container :
> java.awt.Component ;
> Object

> **__Package:__**
> : com.apple.client.eointerface

---

## Class Description

---

The EOImageView class is used to display images
(java.awt.Image objects) in Java Client applications.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.yellow.eointerface package. |

## Constants

---

EOImageView defines the following `int` constants
to specify the scaling behavior of an EOImageView:

|  |  |
| --- | --- |
| __Constant__ | __Scaling Behavior__ |
| ScaleNone | No scaling |
| ScaleProportionally | Scales in proportion to the image size |
| ScaleToFit | Scales to fit the portion of the user interface the image view occupies |
| ScaleProportionallyIfTooLarge | Scales in proportion to the image size, but only if the image is too large to fit its portion of the user interface (the image view never scales the image to be larger) |

## Method Types

---

> **Accessing the image**
> : [image](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zpnfwwcz3f)
> : [setImage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zponsxislnmftwk)
>
> **Configuring scaling behavior**
> : [setImageScaling](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zponsxislnmftwku3dmfwgs3th)
> : [imageScaling](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zpnfwwcz3fknrwc3djnztq)
> : [setScalingHints](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zponsxiu3dmfwgs3thjbuw45dt)
> : [scalingHints](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zponrwc3djnztuq2loorzq)
>
> **Painting**
> : [imageUpdate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zpnfwwcz3fkvygiylumu)
> : [paint](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zpobqws3tu)
> : [setBorder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zponsxiqtpojsgk4q)
> : [setBounds](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfwwcz3fkzuwk5zponsxiqtpovxgi4y)

## Instance Methods

---

### image

`public java.awt.Image image()`

Returns the receiver's image.

---

### imageScaling

`public int imageScaling()`

Returns the type of scaling
the receiver uses. The return value is one of:

- [ScaleNone](#apple-ijceisscjjbuk)
- [ScaleProportionally](#apple-ijceiscfjbceq)
- [ScaleToFit](#apple-ijceiskejjbeg)
- [ScaleProportionallyIfTooLarge](#apple-ijceiq2eirceo)

---

### imageUpdate

`public boolean imageUpdate(
java.awt.Image  image,
int  flags,
int  x,
int  y,
int  width,
int  height)`

See the method description
for `imageUpdate` in Sun's JComponent class
documentation.

---

### paint

`public void paint(java.awt.Graphics  g)`

See the method description
for `setBorder` in Sun's JComponent class
documentation.

---

### scalingHints

`public int scalingHints()`

Returns the receiver's scaling
hints-a constant identifying the algorithm the receiver uses to
scale its image.

---

### setBorder

`public void setBorder(javax.swing.border.Border  border)`

See the method description
for `setBorder` in Sun's JComponent class
documentation.

---

### setBounds

`public void setBounds(
int  x,
int  y,
int  width,
int  height)`

See the method description
for `setBounds` in Sun's Component class
documentation.

---

### setImage

`public void setImage(java.awt.Image  image)`

Sets the receiver's image
to  _image_ and repaints (only if  _image_ is
different from the receiver's old image).

---

### setImageScaling

`public void setImageScaling(int  imageScaling)`

Sets the
scaling behavior of the receiver; that is, identifies the circumstances
under which the receiver scales. The  _imageScaling_ argument
should be one of the following constants (defined in EOImageView):

- [ScaleNone](#apple-ijceisscjjbuk)
- [ScaleProportionally](#apple-ijceiscfjbceq)
- [ScaleToFit](#apple-ijceiskejjbeg)
- [ScaleProportionallyIfTooLarge](#apple-ijceiq2eirceo)

The
default scaling behavior is `ScaleProportionallyIfTooLarge`.
For more information on these constants, see ["Constants"](#apple-ijceisccifdui).

---

### setScalingHints

`public void setScalingHints(int  scalingHints)`

Sets the algorithm the receiver
uses to scale it's image.The  _scalingHints_ argument
should be one of the following constants (defined in java.awt.Image):

- `SCALE_DEFAULT`
- `SCALE_FAST`
- `SCALE_SMOOTH`
- `SCALE_REPLICATE`
- `SCALE_AREA_AVERAGING`

The
default is `SCALE_SMOOTH`. For more
information on the algorithms identified by these constants, see Sun's
Image class documentation

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
