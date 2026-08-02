---
title: On-Demand Resources Guide
apple_id: TP40015083
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: Foundation
published: '2017-01-12'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/EnablingHosting.html
archived_at: '2026-07-15T07:32:03.775630Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [On-Demand Resources Guide](index.md)



## Setting the Host in an App

You set the host used to store on-demand resources for an app in the build settings for a target. Each target can have a different host.

### Configuring a Target

The Asset Pack Manifest URL Prefix build setting for a target is a string specifying the location where the asset packs are stored. The value is either:

- __The empty string.__ The app uses the default host for accessing on-demand resources: the App Store for distributed apps, Xcode or Xcode Server for apps in development, or TestFlight for apps distributed for testing.
- __A hosted asset-packs URL.__ The app requests on-demand resources from the server at the path specified by the URL.

### Specifying a Hosted Asset-Packs URL

The hosting URL for an asset pack resolves to the path where the asset pack is stored. The URL ends with a forward slash (/). The general form is:

`<protocol>://<path-to-asset-packs>/`

For example, if the asset pack is hosted on the HTTPS server `www.mytags.com` in the directory `/appcontent/tagme/tags/`, the URL is `https://www.mytags.com/appcontent/tagme/tags/`.

### Setting the Host for a Target

__To add a hosted asset-packs URL to a target__

1. In the project navigator, select the project file.
2. In the project editor, select the target.
3. Select the Build Settings pane.
4. Show the Assets category.

   > [!TIP]
   > 
5. Set the value of the Asset Pack Manifest URL Prefix setting to the URL for the hosted asset packs.

[Hosting Essentials](IntrotoHostingODR.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2taobtfvbuqmjxfvjvomi)

[Generating Hosted Asset Packs](GeneratingHostedContent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2taobtfvbuqmjzfvjvomi)
