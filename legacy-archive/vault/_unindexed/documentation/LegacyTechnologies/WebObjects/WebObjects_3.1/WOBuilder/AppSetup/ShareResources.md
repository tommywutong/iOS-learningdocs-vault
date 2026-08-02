---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/AppSetup/ShareResources.html
archived_at: '2026-07-15T07:50:16.909618Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](AppSetup.book.md)
[!Previous Section](DeleteComponent.md)

Sharing Resources

# Sharing Resources

When you add a resource such as an image file to a component, the default behavior is to copy the file into the component's directory. The HTML that WebObjects Builder generates refers to the copy inside the component directory.

You may have resources that you want to share among several applications and several components. To set this up:

Create a directory under your HTTP server's document root.

Specify that directory's name in WebObjects Builder's Preferences panel.

WebObjects Builder already assumes that you have two directories under the document root: __Images__ and __Resources__. If they don't already exist, create these two directories. Use __Images__ to store image files (__.gif__, __.jpeg__, __.tiff__, and so on). Use __Resources__ to store all other files. You only need to add other directory names to the Preferences panel if you want to further organize your resources. For example, you might want to store all of the sound files in a separate directory named __Sounds__. In this case, you would create the __Sounds__ directory and then add it to the table in the Preferences panel.

If you drag a resource from one of the directories specified on the Preferences panel, WebObjects Builder assumes you want to share the resource and does not copy it into the component. If the Preferences panel lists extensions next to the directory, it only shares files with that extension.

For example, if you drag a __.gif__ file from the directory ___<DocumentRoot>___/Images to a component, that file is not copied into the component directory because the Preferences panel specifies that all __.gif__ files in ___<DocumentRoot>___/Images are shared resources. However, if there was a sound file in ___<DocumentRoot>___/Images and you dragged it to a component, the sound file _would_ be copied into the component because the Preferences panel does _not_ say that sound files in ___<DocumentRoot>___/Images are shared resources.

If you don't specify file extensions next to the directory name on the Preferences panel, any file in that directory is shared. For example, all files in the __Resources__ directory are shared, regardless of their type.

!

__Note:__ All of an application's components must reside in the application's directory. You cannot create a shared component directory under the document root. See "[Adding Existing Components](AddExistingComponent.md#apple-kjcumnztgazdg)" to learn how to share components.
