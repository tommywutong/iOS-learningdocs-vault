---
title: Performing Serial I/O
apple_id: DTS10000454
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2013-11-07'
source_url: https://developer.apple.com/library/archive/samplecode/SerialPortSample/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:23:40.375442Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Performing Serial I/O](Performing%20Serial%20I-O.md)


[Next](SerialPortSample-SerialPortSample.c.md)[Previous](Performing%20Serial%20I-O.md)

# ReadMe.txt

```
### SerialPortSample ###

================================================================================
DESCRIPTION:

Command line tool that demonstrates how to use IOKitLib to find all serial ports
on OS X. Also shows how to open write to, read from, and close a serial port.

Testing:

To have this sample find a specific device, define the macro MATCH_PATH with the
value of the callout device path in /dev, such as:

#define MATCH_PATH "/dev/cu.usbmodemfa131"

If MATCH_PATH is undefined, the sample will attempt to connect to the first 
serial device it finds.

================================================================================
BUILD REQUIREMENTS:

OS X 10.6 SDK or later

================================================================================
RUNTIME REQUIREMENTS:

OS X 10.6 or later

================================================================================
PACKING LIST:

SerialPortSample.c

================================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.5
    Verified compatibility with recent Xcode and OS X versions. Fixed bug with 
    MIN and TIME settings.

Version 1.4
    Updated to produce a universal binary. Added examples of setting arbitrary
    baud rates and the read timer latency. Use kIOMasterPortDefault instead of
    older IOMasterPort function.

Version 1.3
    Techniques shown are:
    - Finding a serial port
    - Opening and configuring the port
    - Sending an "AT" command to a modem attached to the port
    - Reading the "OK" response from the modem (if any)
    - Closing the port
```

[Next](SerialPortSample-SerialPortSample.c.md)[Previous](Performing%20Serial%20I-O.md)

