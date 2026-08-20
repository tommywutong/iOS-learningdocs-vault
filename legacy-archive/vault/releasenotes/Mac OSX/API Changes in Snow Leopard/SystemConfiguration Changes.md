---
title: API Changes in Snow Leopard
apple_id: TP40007673
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/SnowLeopard_API_ReleaseNote/SystemConfiguration.html
archived_at: '2026-07-18T02:58:45.837736Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [API Changes in Snow Leopard](API%20Changes%20in%20Snow%20Leopard.md)


[ADC Home](https://developer.apple.com/) >
[Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) >
Release Notes >
OS X >
[API Changes in Snow Leopard Developer Preview](API%20Changes%20in%20Snow%20Leopard.md) >

# SystemConfiguration Changes

## SystemConfiguration

SCNetwork.hModified [SCNetworkInterfaceRefreshConfiguration()](https://developer.apple.com/documentation/systemconfiguration/1420192-scnetworkinterfacerefreshconfigu)

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

SCNetworkConfiguration.hAdded [kSCNetworkInterfaceTypeIPSec](https://developer.apple.com/documentation/systemconfiguration/kscnetworkinterfacetypeipsec)SCNetworkReachability.hAdded [SCNetworkReachabilityFlags](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags)Added [kSCNetworkReachabilityFlagsConnectionAutomatic](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514897-connectionautomatic)Added [kSCNetworkReachabilityFlagsConnectionRequired](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/kscnetworkreachabilityflagsconnectionrequired)Added [kSCNetworkReachabilityFlagsInterventionRequired](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514898-interventionrequired)Added [kSCNetworkReachabilityFlagsIsDirect](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514916-isdirect)Added [kSCNetworkReachabilityFlagsIsLocalAddress](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/1514896-islocaladdress)Added [kSCNetworkReachabilityFlagsIsWWAN](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/kscnetworkreachabilityflagsiswwan) (no architecture available)Added [kSCNetworkReachabilityFlagsReachable](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/kscnetworkreachabilityflagsreachable)Added [kSCNetworkReachabilityFlagsTransientConnection](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/kscnetworkreachabilityflagstransientconnection)Modified [SCNetworkReachabilityGetFlags()](https://developer.apple.com/documentation/systemconfiguration/1514924-scnetworkreachabilitygetflags)

|  | Declaration |
| --- | --- |
| Old | Boolean SCNetworkReachabilityGetFlags ( SCNetworkReachabilityRef target, SCNetworkConnectionFlags \*flags); |
| New | Boolean SCNetworkReachabilityGetFlags ( SCNetworkReachabilityRef target, SCNetworkReachabilityFlags \*flags); |

SCPreferences.hAdded [AuthorizationRef](https://developer.apple.com/documentation/security/authorizationref) (no architecture available)SCSchemaDefinitions.hAdded [kSCPropNetIPSecConnectTime](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecconnecttime)Added #def kSCPropNetIPSecConnectTimeAdded [kSCPropNetIPSecRemoteAddress](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecremoteaddress)Added #def kSCPropNetIPSecRemoteAddressAdded [kSCPropNetIPSecStatus](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecstatus)Added #def kSCPropNetIPSecStatusAdded #def kSCPropNetIPSecXAuthEnabledAdded [kSCPropNetIPSecXAuthEnabled](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecxauthenabled)Added [kSCPropNetIPSecXAuthName](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecxauthname)Added #def kSCPropNetIPSecXAuthNameAdded #def kSCPropNetIPSecXAuthPasswordAdded [kSCPropNetIPSecXAuthPassword](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecxauthpassword)Added [kSCPropNetIPSecXAuthPasswordEncryption](https://developer.apple.com/documentation/systemconfiguration/kscpropnetipsecxauthpasswordencryption)Added #def kSCPropNetIPSecXAuthPasswordEncryptionAdded #def kSCValNetIPSecAuthenticationMethodHybridAdded [kSCValNetIPSecAuthenticationMethodHybrid](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipsecauthenticationmethodhybrid)Added #def kSCValNetIPSecXAuthPasswordEncryptionKeychainAdded [kSCValNetIPSecXAuthPasswordEncryptionKeychain](https://developer.apple.com/documentation/systemconfiguration/kscvalnetipsecxauthpasswordencryptionkeychain)Added #def kSCValNetIPv4ConfigMethodIPSecAdded kSCValNetIPv4ConfigMethodIPSecAdded #def kSCValNetInterfaceTypeIPSecAdded [kSCValNetInterfaceTypeIPSec](https://developer.apple.com/documentation/systemconfiguration/kscvalnetinterfacetypeipsec)Modified kSCPropNetNetInfoBindingMethods

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified kSCValNetNetInfoBindingMethodsBroadcast

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified kSCPropNetNetInfoServerTags

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified [kSCPropUsersConsoleUserUID](https://developer.apple.com/documentation/systemconfiguration/kscpropusersconsoleuseruid)

|  | Deprecation |
| --- | --- |
| Old | 10.4 |
| New |  |

Modified kSCPropNetNetInfoServerAddresses

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified kSCPropNetNetInfoBroadcastServerTag

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified [kSCPropUsersConsoleUserName](https://developer.apple.com/documentation/systemconfiguration/kscpropusersconsoleusername)

|  | Deprecation |
| --- | --- |
| Old | 10.4 |
| New |  |

Modified kSCValNetNetInfoDefaultServerTag

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified kSCEntNetNetInfo

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified [kSCPropUsersConsoleUserGID](https://developer.apple.com/documentation/systemconfiguration/kscpropusersconsoleusergid)

|  | Deprecation |
| --- | --- |
| Old | 10.4 |
| New |  |

Modified kSCValNetNetInfoBindingMethodsManual

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified kSCValNetNetInfoBindingMethodsDHCP

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

SystemConfiguration.hAdded [kSCStatusConnectionNoService](https://developer.apple.com/documentation/systemconfiguration/kscstatusconnectionnoservice)

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
