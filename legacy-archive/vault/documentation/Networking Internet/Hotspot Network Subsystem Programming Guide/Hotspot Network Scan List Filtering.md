---
title: Hotspot Network Subsystem Programming Guide
apple_id: TP40016639
resource_type: Guide
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: NetworkExtension
published: '2015-12-03'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/Hotspot_Network_Subsystem_Guide/Contents/ScanListFiltering.html
archived_at: '2026-07-15T08:18:49.644421Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Hotspot Network Subsystem Programming Guide](About%20the%20Hotspot%20Network%20Subsystem.md)


[Next](Hotspot%20Helper%20Command%20Handling%20Details.md)[Previous](Authentication%20State%20Machine.md)

# Hotspot Network Scan List Filtering

An important function of the Hotpot Helper is to perform Wi-Fi scan list filtering. In the Wi-Fi pane in the Settings app, the user can browse the list of nearby Wi-Fi networks. A Wi-Fi network is annotated with the name of any Hotspot Helper that claims to handle that network. This name gives the user a visual cue that the network is one worth selecting over one that does not have an annotation.

The annotations are determined by the Wi-Fi scan list filtering process. The system asks each Hotpot Helper to provide feedback about the nearby Wi-Fi networks by issuing a [kNEHotspotHelperCommandTypeFilterScanList](Hotspot%20Helper%20Command%20Handling%20Details.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmmzzfvbuqnbnknlte) command containing a list of Wi-Fi networks. In its response, the Hotpot Helper specifies every network that it supports with any confidence.

[Next](Hotspot%20Helper%20Command%20Handling%20Details.md)[Previous](Authentication%20State%20Machine.md)

