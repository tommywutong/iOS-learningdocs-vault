---
title: HID Class Device Interface Guide
apple_id: TP40000970
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/HID/samples/samples.html
archived_at: '2026-07-15T07:31:12.731217Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HID Class Device Interface Guide](Introduction%20to%20Working%20With%20HID%20Class%20Device%20Interfaces.md)


[Next](Document%20Revision%20History.md)[Previous](Working%20With%20Legacy%20HID%20Class%20Device%20Interfaces.md)

# Complete Code Samples

The code samples elsewhere in this document are intended to introduce concepts. Thus, this document does not include all the necessary code to build a working tool on its own.

The code samples in this chapter are complete samples that you can run and use as a basis for experimentation.

The following sample code projects show how to use the HID Manager interfaces added in OS X v10.5:

- _[HID Explorer](../../../samplecode/HID%20Explorer/HID%20Explorer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbugm)_—A Cocoa application that demonstrates how to use the HID Manager APIs while providing a useful tool for exploring the HID devices attached to your computer.
- _[HID Config Save](../../../samplecode/HID%20Config%20Save/HID%20Config%20Save.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbugi)_—A Carbon application that demonstrates how to save and restore element configuration information and shows how to use the configured inputs in a game environment.
- _[HID Calibrator](../../../samplecode/HID%20Calibrator/HID%20Calibrator.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydonrugu)_—A Carbon application that demonstrates the HID Manager APIs..
- _[HID LED test tool](../../../samplecode/HID%20LED%20test%20tool/HID%20LED%20test%20tool.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoobxha)_—A command-line tool that demonstrates how to iterate HID devices and manipulate their LEDs.

The code samples in this section are designed for older versions of OS X (prior to version 10.5). For version 10.5 and later, these APIs are deprecated. You should use the APIs shown in [Accessing a HID Device](Accessing%20a%20HID%20Device.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzqfvbuqmrrgqwvgvzs) for new code written for OS X v10.5 and later.

The Companion Files disk image contains a complete, buildable version of the example in [Legacy HID Access Overview](Legacy%20HID%20Access%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzqfvbuqmrrgewugskiizeucske) and [Working With Legacy HID Class Device Interfaces](Working%20With%20Legacy%20HID%20Class%20Device%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcmbvfvkfaoi).

In addition, a second example tool, HIDTestTool, is included. This tool provides additional sample code that may be useful when working with various HID devices.

If you are viewing this document on the web, the disk image can be downloaded by clicking the "Companion Files” link at the top of the table of contents. If you are viewing this document as a PDF file, or if you are viewing it from a local installation, you must first go to the online version of this document at [http://developer.apple.com/documentation/DeviceDrivers/Conceptual/HID/index.html](https://developer.apple.com/documentation/DeviceDrivers/Conceptual/HID/index.html).

In addition to these examples, the _[HID Manager Basics](../../../samplecode/HID%20Manager%20Basics/HID%20Manager%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbugq)_, _[HID Utilities Source](../../../samplecode/HID%20Utilities%20Source/HID%20Utilities%20Source.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbugu)_, and _[UniversalHIDModuleTest](../../../samplecode/UniversalHIDModuleTest/UniversalHIDModuleTest.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydambwgi)_ sample code projects use these legacy APIs.

[Next](Document%20Revision%20History.md)[Previous](Working%20With%20Legacy%20HID%20Class%20Device%20Interfaces.md)

