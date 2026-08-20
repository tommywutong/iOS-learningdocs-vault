---
title: Available FireWire Isochronous Bandwidth
apple_id: DTS10003343
resource_type: QA
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2004-07-07'
source_url: https://developer.apple.com/library/archive/qa/qa1356/_index.html
archived_at: '2026-07-18T02:30:26.014748Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1356

# Available FireWire Isochronous Bandwidth

## Q:  Is there a way to find out the amount of isochronous bandwidth currently available on FireWire?

A: Is there a way to find out the amount of isochronous bandwidth currently available on FireWire?

Yes, but this information has dubious value (see Caveats, below).

You can find the current Isochronous Resource Manager (IRM) for the FireWire bus your device is on and read the IRM's `BANDWIDTH_AVAILABLE` register.

For example:

__Listing 1__  Read avaliable FireWire isoch bandwidth

```
IOReturn GetBandwidth( IOFireWireLibDeviceRef device, UInt32 * bandwidth ) {     OSStatus        error ;     UInt16      irmNodeID ;     UInt32      generation ;      // get current bus generation     error = (**device).GetBusGeneration( device, & generation ) ;      if ( !error )     {         // get ID of IRM         error = (**device).GetIRMNodeID( device, generation, & irmNodeID ) ;     }      if ( !error )     {         // build the FireWire address of the BANDWIDTH_AVAILABLE register         FWAddress address = { irmNodeID,                               kCSRRegisterSpaceBaseAddressHi,                                kCSRBandwidthAvailable } ;          UInt32 size = sizeof( *bandwidth ) ;          // read the BANDWIDTH_AVAILABLE register         error = (**device).Read( device,                                  0,                                  address,                                  bandwidth,                                  &size,                                  true,                                  generation ) ;     }      return( error ); }
```


It's possible for a bus reset to occur __at any time__. If `GetBandwidth` returns `kIOFireWireBusReset`, try calling it again.

If `GetBandwidth` returns `kIOReturnSuccess` and `*bandwidth` indicates sufficient bandwidth for your purpose, it's still possible for your request to allocate bandwidth to fail. This is because another device on the bus could allocate some (or all) of the available bandwidth __at any time__.

In other words the only way to be sure there is enough bandwidth is to have your request to allocate bandwidth succeed. This means that your isochronous channel setup routine must be prepared to deal gracefully with an error due to insufficient bandwidth, even if the above technique indicates enough bandwidth is available.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-07-07 | New document that discusses attempting to "pre-flight" an isochronous bandwidth allocation request by reading the currently available bandwidth. |

