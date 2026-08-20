---
title: Quartz Composer MiniBooth
apple_id: DTS40009235
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2009-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/MiniBooth/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:14:59.537356Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Quartz Composer MiniBooth](Quartz%20Composer%20MiniBooth.md)


[Next](main.m.md)[Previous](Quartz%20Composer%20MiniBooth.md)

# ReadMe.txt

```
Copyright © 2007-2009 by Apple Inc.  All Rights Reserved.

Quartz Composer Application

MiniBooth                   A very simplified Photo Booth that shows how to combine 
                        the Composition Repository with the Composition Loader 
                        patch to apply image filtering on video output, and how 
                        to save the QCView contents as a PNG image file.

Sample Requirements             The project was created using the Xcode running under 
                        Mac OS X 10.6.x or later. The supplied Quartz Composer 
                        compositions were created using the Quartz Composer editor 
                        running under Mac OS X 10.6.x or later.

About the sample                In the sample, the user can select an image filter in the 
                        composition picker to generate videos with special effects. 
                        The supplied composition grabs the input video and output 
                        a sequence of images. The images are then processed with an 
                        image filter selected by the user to produce video with 
                        special effects. A QCCompositionPickerPanel is used to 
                        provide the image filters for the user to select. When a filter 
                        is selected, the application will receive a notification and 
                        it will pass the selected filter identifier as the new input 
                        parameter for the composition in the QCView. This filter is 
                        then applied to process the images.

Using the Sample                Open the project using the Xcode editor which can be found in 
                        /Developer/Applications. Build the project and run. Select the 
                        image filter from the composition picker to see the new results.

Installation                    n/a

Changes from Previous Versions  n/a

Feedback and Bug Reports            Please send all feedback about this sample to:
                        http://developer.apple.com/contact/feedback.html

                        Please submit any bug reports about this example to 
                        http://developer.apple.com/bugreport
```

[Next](main.m.md)[Previous](Quartz%20Composer%20MiniBooth.md)

