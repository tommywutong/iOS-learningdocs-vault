---
title: PCCardNetworkSample
apple_id: DTS10000258
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PCCardNetworkSample/Introduction/Intro.html
archived_at: '2026-07-18T03:18:20.629997Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](dlpiether.h.md)

# PCCardNetworkSample

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-07-22 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

Code sample which demonstrates a Ethernet driver, PC Card Enabler, and Open Transport Port Scanner for an Ethernet PC Card. Specifically, the sample is targeted for network PC Cards other than Ethernet so that they can properly register themselves with Open Transport The code sample provides a MetroWerks Code Warrior project file which includes a sample Ethernet driver, a PC Card Enabler and a Port Scanner. The Enabler is designed to handle port registration of the network card in conjunction with the provided port scanner. The sample code demonstrates techniques to 1. register a driver name so that the default PC Card port scanner registers a custom driver name to use instead of the auto generated name based on the device, and 2. how to keep the default scanner from registering the network card as an Ethernet device. The sample project was created with MetroWerks CodeWarrior 4.0 with the Universal Interfaces and Libraries v3.2, and the Open Transport 2.0.1 DDK To use the sample, a PowerBook 2400, 3400, or G3 series is required. The sample was tested with SSW 8.5 and OT 2.0.1 and may work with SSW 7.6.1 and OT 1.1.2. The sample ethernet driver only supports a single PC Card. The sample could be rewritten to support multiple Ethernet PC Cards. The purpose of the sample was to demonstrate port registration for non-Ethernet network PC Cards. The sample does not demonstrate the loading of support additional port scanners which the card may require, such as for ATM MiddleWare. Requirmements: Open Transport 1.1.2 or greater, PowerBook 2400, 3400, G3, or G3 Series or newer. Keywords: PC Card, Network Driver, Open Transport Module, Token Ring, ATM, Enabler, Port Scanner

[Next](dlpiether.h.md)

