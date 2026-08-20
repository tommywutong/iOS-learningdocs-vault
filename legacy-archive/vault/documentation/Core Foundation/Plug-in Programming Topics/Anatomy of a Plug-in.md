---
title: Plug-in Programming Topics
apple_id: 10000128i
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2005-03-03'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPlugIns/Concepts/anatomy.html
archived_at: '2026-07-15T07:22:36.358233Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Plug-in Programming Topics](Introduction%20to%20Plug-ins.md)


[Next](Conceptual%20Building%20Blocks.md)[Previous](Plug-ins%20and%20Microsoft%E2%80%99s%20COM.md)

# Anatomy of a Plug-in

On disk, a CFPlugIn is laid out as a file package just like a CFBundle. What makes a CFPlugIn special is the addition of a few keys in the plug-in’s information property list. These keys are documented in [Plug-in Registration](Plug-in%20Registration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dclkdjjbeksscjbea) Because bundles and plug-ins share the same structure on disk, it is tempting—though incorrect—to think of a CFPlugIn as a CFBundle. At runtime, however, it is correct to say that a CFPlugIn _has_ a CFBundle.

CFPlugIns and CFBundles come in pairs. Every CFPlugIn has a CFBundle, but each CFBundle (an application or framework bundle for instance) does not necessarily correspond to a CFPlugIn. You should _never_ attempt to directly access a plug-in as a CFBundle. You should use the function `CFPlugInGetBundle` if you need to access a plug-in’s resources with the CFBundle API.

If your plug-in will be manually installed by users it is a good idea to define OS X style creator/type codes (and perhaps a filename extension as well, though this is not required) for your plug-ins so that they will display the appropriate icon in file system views.

[Next](Conceptual%20Building%20Blocks.md)[Previous](Plug-ins%20and%20Microsoft%E2%80%99s%20COM.md)

