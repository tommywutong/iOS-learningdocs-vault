---
title: PCCardNetworkSample
apple_id: DTS10000258
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PCCardNetworkSample/Listings/ProjectDefines_h.html
archived_at: '2026-07-18T03:18:21.668322Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PCCardNetworkSample](PCCardNetworkSample.md)


[Next](Document%20Revision%20History.md)[Previous](PortScanner.r.md)

# ProjectDefines.h

```
/*
    File:       ProjectDefines.h

    Contains:   

    Written by: Rich Kubota 

    Copyright:  Copyright © 1998-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/16/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/

//----------------------------------------------------------------------

#define DEBUG           1
#define DEBUG1          0

//----------------------------------------------------------------------

// use the TupleDumper PPC utility which comes with the PC Card DDK to display the data
// associated with the following Tuples.  The following are used with the _IdentifyCard call
// to verify that the proper card is being supported.

// the following are found in the CISTPL_MANFID
// for the RATOC 5588 Ethernet card.

#define kManifID            0x0400
#define kManifInfo          0x0400

    // the following is the name of the driver and port scanner
    // they are used in the c an resource sources.
#define kDriverName                 "MyEnetDriver"
#define kDriverNameForCFRG          "OTModl$" kDriverName
#define kPortScannerName            "MyCustomPortScanner"
#define kPascalPortScannerName      "\p" kPortScannerName

#define kDescriptorProperty "driver-descriptor"
#define kPortConfigured     "port-configured"
#define kPortModule         "port-module"
#define kSocketNumber       "SocketNumber"

// The following defines are unique to the RATOC 5588 Ethernet card on which I designed
// this sample.  Change these values to match your card

// name string for the DriverDescriptor in the Enabler
#define kPluginNamePString  "\ppccard4,4"

// manufacturer ID tyo match from the CISTPL_MANFID
#define kManufacture        "PCMCIA LAN MBH10304  ES"

// product ID to match from the CISTPL_MANFID
#define kProduct            "  01"
```

[Next](Document%20Revision%20History.md)[Previous](PortScanner.r.md)

