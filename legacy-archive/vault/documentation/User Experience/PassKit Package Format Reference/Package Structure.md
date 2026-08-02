---
title: PassKit Package Format Reference
apple_id: TP40012026
resource_type: Guide
platform: watchOS|iOS
topic: User Experience
technology: PassKit
published: '2017-11-16'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Reference/PassKit_Bundle/Chapters/PackageStructure.html
archived_at: '2026-07-27T06:57:08.733463Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [PassKit Package Format Reference](About%20Pass%20Files.md)


[Previous](About%20Pass%20Files.md)

# Package Structure

Pass files are stored on disk as a zipped package with the `pkpass` file extension.

Localized resources are loaded using the standard bundle localization techniques, which are implemented by the [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) class. For more details, see _[Internationalization and Localization Guide](../../Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i)_.

The top level of the package contains the following files:

**`background.png`**
: The image displayed as the background of the front of the pass.

**`footer.png`**
: The image displayed on the front of the pass near the barcode.

**`icon.png`**
: The pass’s icon. This is displayed in notifications and in emails that have a pass attached, and on the lock screen.

When it is displayed, the icon gets a shine effect and rounded corners.

**`logo.png`**
: The image displayed on the front of the pass in the top left.

**`manifest.json`**
: A JSON dictionary. Each key is the path to a file (relative to the top level of the bundle) and the key’s value is the SHA-1 hash for that file. Every file in the bundle appears in the manifest, except for the manifest itself and the signature.

**`pass.json`**
: A JSON dictionary that defines the pass. Its contents are described in detail in [Top-Level Keys](https://developer.apple.com/library/archive/documentation/UserExperience/Reference/PassKit_Bundle/Chapters/TopLevel.html#//apple_ref/doc/uid/TP40012026-CH2-SW1).

**`signature`**
: A detached PKCS #7 signature of the `manifest.json` file.

**`strip.png`**
: The image displayed behind the primary fields on the front of the pass.

**`thumbnail.png`**
: An additional image displayed on the front of the pass. For example, on a membership card, the thumbnail could be used to a picture of the cardholder.

__Note:__ All of the pass’s images are loaded using standard [UIImage](https://developer.apple.com/documentation/uikit/uiimage) image-loading methods. This means, for example, the file name of the high-resolution version of the image ends with `@2x.png`.

[Previous](About%20Pass%20Files.md)
