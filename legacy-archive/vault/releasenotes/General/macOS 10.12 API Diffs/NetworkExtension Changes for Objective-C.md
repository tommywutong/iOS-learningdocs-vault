---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/NetworkExtension.html
archived_at: '2026-07-18T02:50:41.463107Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# NetworkExtension Changes for Objective-C

### NetworkExtension

#### NEAppProxyFlow.h

Modified [NEFlowMetaData](https://developer.apple.com/documentation/networkextension/neflowmetadata)

|  | Protocols | Header |
| --- | --- | --- |
| From | -- | NetworkExtension/NEAppProxyFlow.h |
| To | NSCopying, NSSecureCoding | NetworkExtension/NEFlowMetaData.h |

Modified [NEFlowMetaData.sourceAppSigningIdentifier](https://developer.apple.com/documentation/networkextension/neflowmetadata/1406840-sourceappsigningidentifier)

|  | Header |
| --- | --- |
| From | NetworkExtension/NEAppProxyFlow.h |
| To | NetworkExtension/NEFlowMetaData.h |

Modified [NEFlowMetaData.sourceAppUniqueIdentifier](https://developer.apple.com/documentation/networkextension/neflowmetadata/1406448-sourceappuniqueidentifier)

|  | Header |
| --- | --- |
| From | NetworkExtension/NEAppProxyFlow.h |
| To | NetworkExtension/NEFlowMetaData.h |

#### NEFlowMetaData.h (Added)

Modified [NEFlowMetaData](https://developer.apple.com/documentation/networkextension/neflowmetadata)

|  | Protocols | Header |
| --- | --- | --- |
| From | -- | NetworkExtension/NEAppProxyFlow.h |
| To | NSCopying, NSSecureCoding | NetworkExtension/NEFlowMetaData.h |

Modified [NEFlowMetaData.sourceAppSigningIdentifier](https://developer.apple.com/documentation/networkextension/neflowmetadata/1406840-sourceappsigningidentifier)

|  | Header |
| --- | --- |
| From | NetworkExtension/NEAppProxyFlow.h |
| To | NetworkExtension/NEFlowMetaData.h |

Modified [NEFlowMetaData.sourceAppUniqueIdentifier](https://developer.apple.com/documentation/networkextension/neflowmetadata/1406448-sourceappuniqueidentifier)

|  | Header |
| --- | --- |
| From | NetworkExtension/NEAppProxyFlow.h |
| To | NetworkExtension/NEFlowMetaData.h |

#### NEPacket.h (Added)

Added [NEPacket](https://developer.apple.com/documentation/networkextension/nepacket)Added [NEPacket.data](https://developer.apple.com/documentation/networkextension/nepacket/2118333-data)Added [-[NEPacket initWithData:protocolFamily:]](https://developer.apple.com/documentation/networkextension/nepacket/2118334-initwithdata)Added [NEPacket.metadata](https://developer.apple.com/documentation/networkextension/nepacket/2118332-metadata)Added [NEPacket.protocolFamily](https://developer.apple.com/documentation/networkextension/nepacket/2118335-protocolfamily)

#### NEPacketTunnelFlow.h

Added [-[NEPacketTunnelFlow readPacketObjectsWithCompletionHandler:]](https://developer.apple.com/documentation/networkextension/nepackettunnelflow/2118343-readpacketobjectswithcompletionh)Added [-[NEPacketTunnelFlow writePacketObjects:]](https://developer.apple.com/documentation/networkextension/nepackettunnelflow/2118344-writepacketobjects)

#### NEProvider.h

Added [-[NEProvider displayMessage:completionHandler:]](https://developer.apple.com/documentation/networkextension/neprovider/1690502-displaymessage)

#### NEVPNConnection.h

Added [NEVPNConnection.manager](https://developer.apple.com/documentation/networkextension/nevpnconnection/1639571-manager)

#### NEVPNProtocolIKEv2.h

Removed NEVPNIKEv2DiffieHellmanGroup0Added [NEVPNIKEv2DiffieHellmanGroupInvalid](https://developer.apple.com/documentation/networkextension/nevpnikev2diffiehellmangroup/nevpnikev2diffiehellmangroupinvalid)

#### NWEndpoint.h

Modified [NWEndpoint](https://developer.apple.com/documentation/networkextension/nwendpoint)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCopying, NSSecureCoding |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
