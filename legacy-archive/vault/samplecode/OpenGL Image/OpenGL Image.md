---
title: OpenGL Image
apple_id: DTS10000538
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Image/Introduction/Intro.html
archived_at: '2026-07-18T03:18:10.964582Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# OpenGL Image

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Shows the high performance display of images using OpenGL Features. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon OpenGL SDK, and Universal Interfaces 3.3+ or DrawSprocket SDK |

OpenGL Image An example showing the high performance display of images using OpenGL Features - Support for all types of QuickTime still images - Multiple windows/images - Live rotation and dragging - Infinite zoom - Single or tiled textures to store images - Overlapped textures for correct image filtering and magnification - Driven by Carbon events - Selectable automatic rotation via Carbon timer - Selectable display of image information and stats - Selectable display of polygon grid - Selectable display of texel grid - Carbon nib application for both Mac OS X and Mac OS 9 - Bundled application for both Mac OS 9 and Mac OS X - Builds with CodeWarrior and Project Builder on Mac OS 9 and Mac OS X Version 1.0 6/27/2001 Version 1.0: Initial release This sample shows how to display images using OpenGL on Mac OS X and Mac OS 9. It uses QuickTime to load still images from any of the types support by the QuickTime Decompression Manager. It then uploads the images as OpenGL textures by either scaling the image to a power of 2 texture size or segmenting the image into multiple textures, which can be loaded separately. Additionally, the code shows how to create textures, which overlap each other to allow correct magnification filtering, resulting in smooth and correct image display. Techniques for handling multiple windows/images are shown, along with high performance live dragging and rotation. Images can infinitely zoomed in or out, using OpenGL to scale the image on the fly. An auto-rotation feature is implemented to show the integration of a Carbon timer in a multiple window real-time environment. Lastly, image/display information, polygon and texel grids can be displayed to show the techniques used to draw/composite the images. The Bundled Application: The application contained in the sample is a bundled application that will run on Mac OS X and Mac OS 9. If one opens the package they will see a alias to the Mac OS 9 application at the package top level. This must be maintained and should be recreated if removed (or application will not launch on Mac OS 9). At a lower level one will find a MacOS folder, with the Mac OS X application, and a MacOSClassic folder, with the Mac OS 9 application. The CodeWarrior project is set to automatically put the executable in the package. On the project Builder side, one must move the executable from inside the package created by Project Builder (in the build folder) to the package, at the top level of the sample, if changes are made on the Mac OS X side. Note, Project Builder will build and debug the application just fine but this will be the application in the build folder. Once building and debugging is complete move the executable to package at the top level of the sample. Interface Builder can be used to edit the nib files. The files that are in The Project Builder project are the ones in the English.lproj folder. Once these are updated they will automatically be used by Project builder for the Mac OS X package but this folder will need to moved manually to the resources folder in the package Contents for the package itself to be updated. This seems confusing but in reality is a very simple procedure allowing separate executables for Mac OS X and Mac OS 9. This can simplify your development process and allow your Mac OS X Carbon application to directly access all Mac OS X Mach-O based services. Note: Under CodeWarrior you will have to change the access path for the OpenGL SDK with valid a one for your local environment. Carbon SetupGL sample. aglString sample, Mac OS X and Project Builder or CWPro 6+; -or- MAc OS 9 and Carbon SDK 1.3.1+, Requirements: OpenGL SDK, and Universal Interfaces 3.3+ or DrawSprocket SDK Keywords: Carbon, OpenGL, Image, 2D, OpenGL Image, texture

[Next](main.c.md)

