---
title: USBPrivateDataSample
apple_id: DTS10000456
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2006-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/USBPrivateDataSample/Listings/Read_Me_txt.html
archived_at: '2026-07-18T03:27:32.322702Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [USBPrivateDataSample](USBPrivateDataSample.md)


[Next](USBPrivateDataSample.c.md)[Previous](USBPrivateDataSample.md)

# Read Me.txt

```
Read Me for USBPrivateDataSample 1.2
------------------------------------
October 5, 2006

Demonstrates how to use IOKitLib and IOUSBLib to set up asynchronous callbacks when a USB device is attached to or removed from the system. It also shows how to associate arbitrary data with each device instance.


Sample Requirements
-------------------
This sample requires Mac OS X and Xcode 2.2.1 or later to build. The sample runs on Mac OS X 10.2 or later.


About the Sample
----------------
The sample uses the I/O Kit APIs to register for asynchronous notifications (callbacks) when a device with a given vendor and product ID has been plugged in. The notification structure has a refcon field where the sample stores a pointer to a block of memory where information about that device can be kept.

When a device arrives, another callback is registered that will be called when the device is removed.


Using the Sample
----------------
Usage:
USBPrivateDataSample [ vendorID [ productID ] ]

Simply build and run the sample. The desired vendor and product IDs can be specified as command line arguments. Output is sent to the console. 


Changes from Previous Versions
------------------------------
Updated to produce a universal binary. Modernized and incorporated bug fixes.


Feedback and Bug Reports
------------------------
Please send all feedback about this sample to 
<http://developer.apple.com/contact/feedback.html>.

Please submit any bug reports about this sample to
<http://developer.apple.com/bugreporter>. 
```

[Next](USBPrivateDataSample.c.md)[Previous](USBPrivateDataSample.md)

