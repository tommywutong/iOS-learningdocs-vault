---
title: Adding Complications to the Gallery
apple_id: TP40017258
resource_type: Release Note
platform: watchOS|iOS
topic: null
technology: WatchKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/WatchKit/AddingComplications/index.html
archived_at: '2026-07-18T02:59:12.881211Z'
---
> 导航：[总目录](../README.md) · [releasenotes](../_indexes/releasenotes.md)



# Adding Complications to the Gallery

> [!IMPORTANT]
> 

In watchOS 3 and later, users can configure multiple watch faces in the gallery area of the Apple Watch app on iPhone. To add your complication to the gallery, you must create a complication bundle that gives the user a preview of your complication. The complication bundle is stored in your iOS app bundle and used by the Apple Watch app to populate the gallery area. Each complication bundle includes localizable, static previews of the complications that you build using the ClockKit framework. Follow the steps below to create your complication bundle and add it to your iPhone app.

1. In your Complications controller code, implement [getLocalizableSampleTemplateForComplication:withHandler:](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource/1650686-getlocalizablesampletemplate). In your implementation, build the templates by using text or image provider calls. For example:

```
[CLKSimpleTextProvider localizableTextProviderWithStringsFileTextKey:@“AKey”]
```
2. Launch your app in Watch Simulator and make sure that your app is frontmost.
3. In Watch Simulator, choose File > Save Complication Bundle.

   Xcode generates a complication bundle and gives it the name that you enter. For example, `MyBundleName.ckcomplication`.
4. Add the generated complication bundle to your iPhone app.
5. In Xcode, launch your app on iPhone.

   When you launch the Apple Watch app and go to the gallery area, you should see an entry for your app.
