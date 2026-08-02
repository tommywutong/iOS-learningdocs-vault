---
title: watchOS 2 Transition Guide
apple_id: TP40015234
resource_type: Guide
platform: watchOS
topic: General
technology: WatchKit
published: '2016-02-02'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/AppleWatch2TransitionGuide/LeverageSystemTechnologies.html
archived_at: '2026-07-15T07:33:19.259523Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [watchOS 2 Transition Guide](index.md)



## Available System Technologies

Extensions built specifically for watchOS 2 have access to various system frameworks and technologies.

### Networking

Support for network-based operations includes the following technologies:

- WatchKit extensions can access the network directly through an [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession) object. WatchKit extensions have full access to the [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession) capabilities, including the ability to download files in the background. For information on how to use this class, see _URL Loading System Programming Guide_.
- The Watch Connectivity framework supports bidirectional communication between your Watch app and iOS app. Use this framework to coordinate activities between the two apps. See [Communicating with Your Companion iOS App](UpdatetheAppCode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temzufvbuqnrnknlti).

### Additional Frameworks

Extensions built specifically for watchOS 2 have access to the following system frameworks:

- _[ClockKit Framework Reference](https://developer.apple.com/documentation/clockkit)_
- _[Contacts Framework Reference](https://developer.apple.com/documentation/contacts)_
- _[Core Data Framework Reference](https://developer.apple.com/documentation/coredata)_
- _[Core Foundation Framework Reference](https://developer.apple.com/documentation/corefoundation)_
- _Core Graphics Framework Reference_
- _[Core Location Framework Reference](https://developer.apple.com/documentation/corelocation)_
- _[Core Motion Framework Reference](https://developer.apple.com/documentation/coremotion)_
- _[Event Kit Framework Reference](https://developer.apple.com/documentation/eventkit)_
- _[Foundation Framework Reference](https://developer.apple.com/documentation/foundation)_
- _HealthKit Framework Reference_
- _[HomeKit Framework Reference](https://developer.apple.com/documentation/homekit)_
- _[Image I/O Reference Collection](https://developer.apple.com/documentation/imageio)_
- _[Map Kit Framework Reference](https://developer.apple.com/documentation/mapkit)_
- _[Mobile Core Services Framework Reference](https://developer.apple.com/documentation/mobilecoreservices)_
- _[PassKit Framework Reference](https://developer.apple.com/documentation/passkit)_
- _[Security Framework Reference](https://developer.apple.com/documentation/security)_
- _[Watch Connectivity Framework Reference](https://developer.apple.com/documentation/watchconnectivity)_
- _[WatchKit Framework Reference](https://developer.apple.com/documentation/watchkit)_

For detailed information about the interfaces supported by a particular framework, see the reference documentation for that framework.

[Scoping the Project](ScopingtheProject.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temzufvbuqmznknltc)

[Configure the Xcode Project](ConfiguretheXcodeProject.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temzufvbuqnjnknltc)
