---
title: AV Foundation iOS Machine Readable Code Detection FAQ
apple_id: DTS40013824
resource_type: Technical Note
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2013-10-04'
source_url: https://developer.apple.com/library/archive/technotes/tn2325/_index.html
archived_at: '2026-07-26T19:54:10.836222Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2325

# AV Foundation iOS Machine Readable Code Detection FAQ

Discusses frequently asked questions about AV Foundation iOS machine readable code detection.

[Why isn't my 1-Dimensional barcode being detected?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgobsgqwugsbrfvluqwk7jfju4x2ul5gvsxzrl5cestkfjzjust2oifgf6qsbkjbu6rcfl5bekskoi5puirkuivbvirkel4)[Why is my 1-Dimensional barcode not detected at all locations in the image?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgobsgqwugsbrfvluqwk7jfjv6tkzl4yv6rcjjvcu4u2jj5hectc7ijaveq2pircv6tspkrpuirkuivbvirkel5avix2bjrgf6tcpinaviskpjzjv6skol5keqrk7jfgucr2fl4)[Can AVCaptureMetadataOutput detect multiple 1-Dimensional barcodes in a frame?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgobsgqwugsbrfvbucts7iflegqkqkrkverknivkecrcbkrau6vkukbkvix2eivkekq2ul5gvktcujfieyrk7gfpuisknivhfgskpjzauyx2cifjegt2eivjv6skol5av6rssifgukxy)[Can AVCaptureMetadataOutput detect multiple 2-Dimensional barcodes in a frame?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgobsgqwugsbrfvbucts7iflegqkqkrkverknivkecrcbkrau6vkukbkvix2eivkekq2ul5gvktcujfieyrk7gjpuisknivhfgskpjzauyx2cifjegt2eivjv6skol5av6rssifgukxy)[Is UPC-A supported?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgobsgqwugsbrfvevgx2vkbbv6qk7knkvaucpkjkekrc7)[Are EAN-2 and EAN-5 supported?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgobsgqwugsbrfvaverk7ivau4xzsl5au4rc7ivau4xzvl5jvkucqj5jfirkel4)[How can I improve scanning results on very small or very dense codes?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgobsgqwugsbrfvee6v27inau4x2jl5eu2ucsj5lekx2tinau4tsjjzdv6usfknkuyvctl5hu4x2wivjfsx2tjvauytc7j5jf6vsfkjmv6rcfjzjukx2dj5ceku27)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgobsgqwvezlwnfzws33ojbuxg5dpoj4s2u2xge)

## Why isn't my 1-Dimensional barcode being detected?

First, check that the barcode is of a type supported by [AVMetadataMachineReadableCodeObject](https://developer.apple.com/documentation/avfoundation/avmetadatamachinereadablecodeobject).

Check that the barcode is in focus. Implementing tap-to-focus or repeatedly triggering auto-focus is recommended for best results on auto-focus enabled cameras. When using a fixed focus camera some codes might be too small to decode at the appropriate focus distance.

Check that the `AVCaptureSessionPreset` or `AVCaptureDeviceFormat` provides sufficient resolution for the density of barcode you're trying to scan.

[Back to Top](#)

## Why is my 1-Dimensional barcode not detected at all locations in the image?

2-dimensional barcode symbologies (Aztec, QR) have easily found marker patterns which allow them to be found efficiently anywhere in a digital image. 1-dimensional barcode symbologies (UPCE, Code39, Code93, Code128, EAN8, EAN13, PDF417\*) have no such patterns. This is because they were designed to be read by a laser scanner.

The `AVCaptureMetadataOutput` 1-dimensional barcode detectors behave in a manner consistent with this design. The detector samples the image using a limited set of scan lines. The `AVCaptureMetadataOutput` API can detect a barcode only when a decodable portion of the barcode intersects one of these lines.

The scanning pattern includes horizontal, vertical, near-horizontal, and near-vertical scan lines around the center of the `AVCaptureMetadataOutput` [rectOfInterest](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616291-rectofinterest) ("Center"). See Table 1. You may wish to provide hints to the user about where to place the barcode within the camera preview for best results.

In some circumstances, when fewer symbologies are enabled and on more powerful hardware, the set of scan lines is expanded to cover a larger portion of the region of interest ("Additional").

__Table 1__  Scanning pattern scan lines region of interest.

| Supported Device | Scan lines (only 1D codes enabled) | Scan lines (when 2D codes are also enabled) |
| iPhone 4 | Center | Center |
| iPhone 4S and later | Center + additional | Center |
| iPad (all) | Center + additional | Center |
| iPod Touch | Center + additional | Center |

\* PDF417 is a 2-dimensional symbology, but is treated by `AVCaptureMetadataOutput` as a (stacked) 1-dimensional code.

[Back to Top](#)

## Can AVCaptureMetadataOutput detect multiple 1-Dimensional barcodes in a frame?

No. Only a single 1-dimensional code will be returned with each call to `AVCaptureMetadataOutputObjectDelegate` [captureOutput:didOutputMetadataObjects:fromConnection:](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutputobjectsdelegate/1389481-captureoutput), and it will correspond to the center-most decodable barcode in the [rectOfInterest](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616291-rectofinterest).

[Back to Top](#)

## Can AVCaptureMetadataOutput detect multiple 2-Dimensional barcodes in a frame?

Yes. There is a limit of four barcodes per call to `AVCaptureMetadataOutputObjectDelegate` [captureOutput:didOutputMetadataObjects:fromConnection:](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutputobjectsdelegate/1389481-captureoutput) which will usually correspond to the center-most codes in the [rectOfInterest](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616291-rectofinterest).

[Back to Top](#)

## Is UPC-A supported?

Yes. UPC-A is a formal subset of EAN-13. A decoded UPC-A barcode is output as `AVMetadataObjectTypeEAN13Code` with a leading zero in the `stringValue`.

[Back to Top](#)

## Are EAN-2 and EAN-5 supported?

No.

[Back to Top](#)

## How can I improve scanning results on very small or very dense codes?

Code detectability depends on many factors, including: capture resolution, amount of light, complexity / density of the code being scanned, and distance from the lens.

1. Try using a higher resolution preset, but avoid using `AVCaptureSessionPresetPhoto` resolution — this can lead to longer exposure times and increased blur in low-light situations.

2. Try setting a `videoZoomFactor` between 1.0 and the `videoZoomFactorUpscaleThreshold`. This provides a higher resolution window on a smaller part of the image, which means there are more barcode pixels for the decoder to work with.

You should experiment with different camera resolutions and code densities to find the right combination that works for your particular application.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-10-04 | Fixed document links. |
| 2013-10-01 | New document that discusses frequently asked questions about AV Foundation iOS machine readable code detection |

