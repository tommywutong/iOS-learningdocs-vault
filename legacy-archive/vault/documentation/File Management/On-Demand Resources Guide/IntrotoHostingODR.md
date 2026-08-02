---
title: On-Demand Resources Guide
apple_id: TP40015083
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: Foundation
published: '2017-01-12'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/IntrotoHostingODR.html
archived_at: '2026-07-15T07:32:08.702691Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [On-Demand Resources Guide](index.md)



## Hosting Essentials

You can host on-demand resources for your app on any compliant web server. Apps distributed through the App Store can retrieve on-demand resources from your own web server during development and testing, but must use Apple's hosting when published on the App Store. Enterprise apps using in-house distribution can retrieve on-demand resources from your own web server during both development and distribution.

### Hosting On-Demand Resources

Host on-demand resources on any web server using the following steps:

- Configure your server security.
- Choose a URL for hosting the on-demand resources asset packs.
- Generate the asset packs.
- Add the asset packs to the server.
- Enable the app to use the hosted asset packs.

### Server Security Requirements

Hosting on-demand resources requires that a server comply with the Apple app transport security requirements. This includes having an SSL connection with a valid certificate signed by an appropriate authority. An app can be configured to reduce the security requirements. For more information, see the `NSAppTransportSecurity` key in the [Cocoa Keys](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251) chapter of the _[Information Property List Key Reference](../../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_.

> [!IMPORTANT]
> 

[Debugging On-Demand Resources](DebugTips.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2taobtfvbuqnrnknlte)

[Setting the Host in an App](EnablingHosting.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2taobtfvbuqmjyfvjvomi)
