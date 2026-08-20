---
title: Using GLUT and OpenGL on OS X
apple_id: DTS40008046
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2013-04-02'
source_url: https://developer.apple.com/library/archive/qa/qa1613/_index.html
archived_at: '2026-07-18T02:32:42.243555Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1613

# Using GLUT and OpenGL on OS X

## Q:  How can I use GLUT on OS X?

A: GLUT is available on OS X through the GLUT framework. It is installed with every install of OS X. For more information about frameworks, please see [Introduction to Framework Programming Guide](https://developer.apple.com/documentation/MacOSX/Conceptual/BPFrameworks/Frameworks.html).

To use GLUT on OS X, you need to include the OpenGL and GLUT headers in a form of `#include <framework name/header name.h>`.

__Listing 1__  Include the OpenGL and GLUT headers

```c
#include <OpenGL/gl.h>
```
| ```
#include <OpenGL/glu.h> ``` |
```c
#include <GLUT/glut.h>
```

You also need to link your project to the OpenGL and GLUT frameworks. If you are using Xcode 4 to build your project, add the OpenGL and GLUT frameworks by following these steps:

- Select the target
- Click on the "Build Phases" tab
- Under "Link Binary With Libraries", click on the + sign
- Select `OpenGL.framework` and `GLUT.framework` and click "Add"

If you want to build your project from the command line or a make file, link the frameworks as shown in the following listing.

__Listing 2__  Build and link a GLUT program (glutapp) from the command line or a make file

```
cc -framework GLUT -framework OpenGL -framework Cocoa glutapp.c -o glutapp
```

For a GLUT sample that builds in Xcode, you may refer to [GLUTBasics](https://developer.apple.com/samplecode/GLUTBasics/index.html). This sample shows the use of standard callbacks and camera control. It is a good starter example to base your own projects on.

Cocoa-based NSOpenGL is recommended over GLUT for window creation on OS X. When you are ready to move from GLUT to NSOpenGL, please see the [Cocoa OpenGL](https://developer.apple.com/samplecode/CocoaGL/index.html) sample. This sample demonstrates how to setup windows for drawing and how to handle user events using NSOpenGL.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-04-02 | Update for Xcode 4. |
| 2008-10-13 | New document that states the required steps to add GLUT and OpenGL to an Xcode project. |

