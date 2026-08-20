---
title: Specifying required OpenGL capabilities for the Mac App Store
apple_id: DTS40011181
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2012-02-22'
source_url: https://developer.apple.com/library/archive/qa/qa1748/_index.html
archived_at: '2026-07-18T02:34:32.718687Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1748

# Specifying required OpenGL capabilities for the Mac App Store

## Q:  How can I prevent customers who do not have the required OpenGL capabilities from purchasing my application from the Mac App Store?

A: When building an application on Mac OS X Lion 10.7 or later, you can specify OpenGL requirements when packaging it for the Mac App Store. This will insure that only customers who have the appropriate graphics hardware will be able to purchase your application.

It is achieved by specifying additional archiving requirements in a plist file. Select File > New > New File... from the Xcode menu, then choose the "Property List" template under the "Resource" category in the "Mac OS X" section, and follow the ensuing instructions to create a plist file. Add the `gl-renderer` key and an appropriate string value in the resulting plist to specify your application's OpenGL requirements.

The `gl-renderer` key specifies a predicate, against which each of the OpenGL hardware renderers will be checked. To successfully purchase and install the application, at least one of the renderers on the customer's machine must match the requirements of the predicate. Otherwise, the transaction will not go through, and the customer will be notified that he/she doesn't have the required graphics hardware to run the application. The following key paths are available for you to form the definition string:

- `version`, the supported OpenGL version as a double. You can use it to check if the required OpenGL version is available, for example: `version >= 3.2`
- `extensions`, an array of OpenGL extension strings supported. You can use it to check if a required OpenGL extension is available, for example: `'GL_ARB_texture_float' IN extensions`
- `limits.<gl-parameter>`, the integer value of the named GL parameter. Arbitrary GL parameters can be checked via the `limits` key, using the same symbolic name defined in the GL headers, for example: `limits.GL_MAX_TEXTURE_SIZE >= 1024`

If you want to check two or more conditions, you can use logical operators, `AND` and/or `OR`, as shown in the following listing:

__Listing 1__  Checking more than one condition

```
( version >= 2.0
    OR ( ( 'GL_ARB_texture_float' IN extensions OR 'GL_ATI_texture_float' IN extensions )
           AND 'GL_ARB_vertex_blend' IN extensions ) )
AND ( limits.GL_MAX_TEXTURE_SIZE >= 1024 AND limits.GL_MAX_TEXTURE_STACK_DEPTH > 8 )
```

Below are a couple simple real-world examples of the plist for your reference:

__Listing 2__  Plist with the `gl-renderer` key. The application will not allow purchasing on Macs that do not support GL_APPLE_float_pixels (e.g., the Intel GMA 950 and GMA X3100).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>gl-renderer</key>
    <string>( 'GL_APPLE_float_pixels' IN extensions )</string>
</dict>
</plist>
```


__Listing 3__  Plist with the `gl-renderer` key. The application will not allow purchasing on Macs that do not support GL_ARB_texture_rg (e.g., the Intel GMA 950, GMA X3100, and NVidia GeForce 7 series).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>gl-renderer</key>
    <string>( 'GL_ARB_texture_rg' IN extensions )</string>
</dict>
</plist>
```

When you have the plist file ready, in Xcode 4, you can provide it using the "Pre-install Requirements Property List" build setting. See Figure 1 for an example.

__Figure 1__  The Pre-install Requirements Property List build setting in Xcode 4

!!

Xcode 4 will automatically supply the plist to `productbuild` when you create the package from the Organizer and submit it to the Mac App Store.

Xcode 3 does not support using a production definition plist. If you choose to build your application with Xcode 3, you need to run the `productbuild` command directly for archiving your application and supply the plist via the `--product` option. See Listing 4 for an example.

__Listing 4__  The Xcode 3 way for supplying a production definition plist

```
productbuild \
    --component build/Release/Sample.app /Applications \
    --product product_definition.plist \
    Sample.pkg
```

See [OpenGL Capabilities Tables](https://developer.apple.com/graphicsimaging/opengl/capabilities/) for a complete listing of supported features by GPU class.

See man page of the productbuild command on Mac OS X Lion 10.7 or later for full details of the command.

See [Submitting to the Mac App Store](https://developer.apple.com/library/mac/#releasenotes/General/SubmittingToMacAppStore/_index.html) for more information on how to submit your application using Application Loader or within Xcode.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-02-22 | Added how to provide a production definition plist using the Pre-install Requirements Property List build setting in Xcode 4. |
| 2011-08-10 | New document that discusses how to specify required OpenGL capabilities for the Mac App Store so that only customers who have the appropriate graphics hardware will be able to purchase your application. |

