---
title: ImproveYourImage
apple_id: DTS10000766
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2005-08-24'
source_url: https://developer.apple.com/library/archive/samplecode/ImproveYourImage/Introduction/Intro.html
archived_at: '2026-07-18T03:12:50.800704Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](MacShell-MacShell.c.md)

# ImproveYourImage

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0.1, 2005-08-24 Updated to produce a universal binary. No code changes were required. Added Draw CMYK, Draw using CGImage and Export from CGBitmapContext examples. |
| __Build Requirements:__ | Xcode 2.1 or greater, CodeWarrior 9.5 |
| __Runtime Requirements:__ | Mac OS X 10.4, or Mac OS X 10.3.9 with QuickTime 7.0 |

ImproveYourImage demonstrates the use of QuickTime Graphics Importers and Exporters. It includes twelve separate examples, each of which can be chosen from the "Examples" menu. Samples containing multiple steps "PAUSE" after each step, to continue, click the mouse button or slap the spacebar.
1) Draw Image - Uses Graphics Importers to simply draw a still image. Use Sample 1-Snowgum.jpg sample image.
2) Scale and Rotate - Uses Graphics Importers to import, draw, scale and rotate a still image. A fine use of QuadToQuadMatrix can be found here. Use Sample 1-Snowgum.jpg sample image.
3) Alpha Compositing - Uses Graphics Importers to demonstrate compositing with alpha graphics modes and images containing alpha channels. Use Sample 3a-Beach.jpg and Sample 3b-Penguin with shadow.png sample images.
4) Getting More Info - Demonstrates how to retrieve meta-data from image files using Graphics Importers - This example uses the Console.
5) Multiple Images - Uses Graphics Importers to display multiple layers stored in a Photoshop file. Use Sample 5-iMac in Australia.psd Image.
6) Images from URL - Demonstrates how to import an image from a URL DataRef.
7) Filtered Export - Shows how to add a filter to an imported image, draw it with the filter and export a new image with the filter applied.
8) Movies to Image - Importing and Exporting Image Sequences is demonstrated with this sample. Use the Clamation.mov supplied in the Sample 8-Movies <-> images folder.
9) Deep Images - Demonstrates QuickTime's support for deep pixmaps comparing a 48bit RGB image with a 24bit RGB image. Use Sample 9-48RGB vs 24RGB.tiff sample image.
10) Draw CMYK - Demonstrates how to draw an image that has been saved in the CMKY colorspace. Use Sample 10-CMYK.jpg sample image.
11) Draw using CGImage - Uses a Graphics Importer to retrieve as CGImage then uses Quartz to render the image into a Window.
12) Export from CGBitmapContext - First draws the image into a CGBitmapContext then uses the PNG Graphics Export component to save it to a file.

[Next](MacShell-MacShell.c.md)

