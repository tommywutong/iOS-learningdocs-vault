---
title: Using SKCloudServiceController to determine your device's music library capabilities
apple_id: DTS40017392
resource_type: QA
platform: iOS
topic: null
technology: StoreKit
published: '2016-07-05'
source_url: https://developer.apple.com/library/archive/qa/qa1929/_index.html
archived_at: '2026-07-18T02:37:10.645117Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1929

# Using SKCloudServiceController to determine your device's music library capabilities

## Q:  Calling requestCapabilities(completionHandler:) always returns the None capability. How do I determine my device's current music library capabilities?

A: Calling [requestCapabilities(completionHandler:)](https://developer.apple.com/reference/storekit/skcloudservicecontroller/1620610-requestcapabilitieswithcompletio) may return the `None` capability for any of the following reasons:

- You are not logged into Apple Music on your device.
- Your app hasn't requested access to the music library on the device yet. Use [SKCloudServiceController's requestAuthorization:](https://developer.apple.com/reference/storekit/skcloudservicecontroller/1620609-requestauthorization) to request access to it as demonstrated in Listing 1.

  __Listing 1__  Asking for permission to access the music library on the device.

```swift
func requestMusicLibraryAccess()
{
   SKCloudServiceController.requestAuthorization({
      (status: SKCloudServiceAuthorizationStatus) in
          switch(status)
          {
             case .Authorized: print("Access granted.")
             case .Denied, .Restricted: print("Access denied or restricted.")
             case .NotDetermined: print("Access cannot be determined.")
          }
      })
}
```
- Your app does not have permission to access the music library on the device. Use [SKCloudServiceController's authorizationStatus](https://developer.apple.com/reference/storekit/skcloudservicecontroller/1620631-authorizationstatus?language=objc) to determine your app's authorization status as illustrated in Listing 2.

  __Listing 2__  Checking the app's authorization status for the music library on the device .

```swift
func checkMusicLibraryAuthorizationStatus()
{
   switch SKCloudServiceController.authorizationStatus()
   {
      case .Authorized: print("Access granted.")
      case .NotDetermined: requestAuthorization()
      case .Denied, .Restricted: print("Access denied or restricted.")
   }
}
```
- You are probably not using the returned `capabilities` parameter of [requestCapabilities(completionHandler:)](https://developer.apple.com/reference/storekit/skcloudservicecontroller/1620610-requestcapabilitieswithcompletio) appropriately. You should be checking `capabilities` for the features that you are interested in.

  To determine whether the device supports playback of Apple Music catalog tracks, check whether `capabilities` includes `SKCloudServiceCapability.MusicCatalogPlayback` as shown in Listing 3.

  __Listing 3__  Determining whether the device allows playback of Apple Music catalog tracks.

```
let controller = SKCloudServiceController()
controller.requestCapabilitiesWithCompletionHandler({
     (capabilities: SKCloudServiceCapability, error: NSError?) in
     if capabilities.contains(SKCloudServiceCapability.MusicCatalogPlayback)
     {
         print("The device allows playback of Apple Music catalog tracks.")
     }
})
```

  To determine whether the device allows tracks to be added to the user’s music library, check whether `capabilities` includes `SKCloudServiceCapability.AddToCloudMusicLibrary` as shown in Listing 4.

  __Listing 4__  Determining whether the device allows tracks to be added to the user’s music library.

```
let controller = SKCloudServiceController()
controller.requestCapabilitiesWithCompletionHandler({
   (capabilities: SKCloudServiceCapability, error: NSError?) in
     if capabilities.contains(SKCloudServiceCapability.AddToCloudMusicLibrary)
     {
         print("The device allows tracks to be added to the user’s music library.")
     }
})
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-07-05 | New document that describes how to determine your device's music library capabilities using SKCloudServiceController. |

