---
title: AVBNetworkBrowser
apple_id: DTS40014220
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioVideoBridging
published: '2014-03-20'
source_url: https://developer.apple.com/library/archive/samplecode/sc1827/Listings/ReadMe_txt.html
archived_at: '2026-07-26T19:54:13.765057Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVBNetworkBrowser](AVBNetworkBrowser.md)


[Next](AVBNetworkBrowser-ANBAppDelegate.h.md)[Previous](AVBNetworkBrowser.md)

# ReadMe.txt

```
### AVBNetworkBrowser ###

====================================================================================

DESCRIPTION:

This project provides an example of using the AudioVideoBridging framework to discover IEEE Std. 1722.1™-2013 (AVDECC) based Entities on the network and to read information from them.

====================================================================================

The main files are as follows:

ANBAppDelegate.m/.h
The app delegate which handles discovering the network interface controller, tracking the interface objects created for them and gluing the back end updates to the UI updates.

ANBWindowController.m/.h
The window controller which handles the linking the back end updates into the windows view hierarchy via a view based NSTableView and the Cocoa Bindings of the detail view.

ANBEUI64Transformer.m/.h
The NSValueTransformer subclass which handles converting the EUI-64 values to and from a hex string representation.

ANBAVDECCEntity.m/.h
This class maintains the state and information of the AVDECC based Entity. It uses AVDECC AECP AEM commands to read descriptors and other information from the Entity and AVDECC AECP Address Access commands to read the contents of memory objects from the Entity.

ANBInterface.m/.h
A wrapper class around the AVBInterface (AVBEthernetInterface) object which tracks the ANBAVDECCEntity objects for the interface and provides the IOKit matching for re-establishing the discovery delegate and restarting the discovery for the interface’s AVB17221EntityDiscovery object.
```

[Next](AVBNetworkBrowser-ANBAppDelegate.h.md)[Previous](AVBNetworkBrowser.md)

