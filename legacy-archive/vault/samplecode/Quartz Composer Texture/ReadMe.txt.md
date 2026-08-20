---
title: Quartz Composer Texture
apple_id: DTS40009211
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2009-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/Texture/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:26:43.647888Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Quartz Composer Texture](Quartz%20Composer%20Texture.md)


[Next](main.m.md)[Previous](Quartz%20Composer%20Texture.md)

# ReadMe.txt

```
Copyright © 2007-2009 by Apple Inc.  All Rights Reserved.

Quartz Composer Application

Texture                     An application that shows how to use the QCRenderer API to 
                        render a Quartz composition into an OpenGL pBuffer, then 
                        create a texture from it, and use the texture into another 
                        OpenGL scene.

Sample Requirements             The project was created using the Xcode running under Mac OS 
                        X 10.6.x or later.

About the sample                This sample asks the user to select a Quartz Composer 
                        composition for rendering. The application uses two 
                        rendering contexts. One context has the screen as the 
                        rendering target, the other has a pbuffer as the rendering 
                        target. Every time the rendering is triggered, a QCRenderer 
                        with the selected composition renders the image result into 
                        the pixel buffer. The image is then used as a texture in the 
                        first context in an OpenGL quad.

Using the Sample                Open the project using the Xcode editor which can be found 
                        in /Developer/Applications. Build the project and run.

Installation                    n/a

Changes from Previous Versions          n/a

Feedback and Bug Reports            Please send all feedback about this sample to:
                        http://developer.apple.com/contact/feedback.html

                        Please submit any bug reports about this example to 
                        http://developer.apple.com/bugreport
```

[Next](main.m.md)[Previous](Quartz%20Composer%20Texture.md)

