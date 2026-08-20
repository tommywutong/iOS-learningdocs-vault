---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_RideMaps_RideIntentUI_IntentViewController_swift.html
archived_at: '2026-07-18T03:13:01.891314Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-RideMaps-ListRideOptionsIntentExtension-IntentHandler.swift.md)[Previous](Projects-RideMaps-RequestRideIntentExtension-IntentHandler.swift.md)

# Projects/RideMaps/RideIntentUI/IntentViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    An object that implements the `INRidesharingDomainHandling` protocols to handle ridesharing tasks.
 */

import IntentsUI

// The intents whose interactions you wish to handle must be declared in the extension's Info.plist.

class IntentViewController: UIViewController, INUIHostedViewControlling {

    // MARK: - INUIHostedViewControlling

    // Prepare your view controller for the interaction to handle.
    func configure(with interaction: INInteraction!, context: INUIHostedViewContext, completion: ((CGSize) -> Void)!) {

        /*
         -configure can be called at any time. Most likely it could be called each time you send an update in get ride status live observation.

         Your non-ui extension and ui extension run in separate processes, so it is up to you how to synchronize data between the two. 

         It is recommended that you configure the view controller based only on the information in the interaction object to minimize data mismatch between the two extensions.

         The interaction object contains both an intent and response. Use the information on both of these objects to correctly configure the view controller.

         IMPORTANT: Any arbitrary data can be stored in the response's user activity's user info dictionary when you send a get ride status response back to Maps. It will be handed back to you here.

         The context will let you know whether this view controller will be shown inside Maps or Siri. If it is shown inside Maps, it is not necessary nor recommended to show an MKMapView.
         */

        if let completion = completion {
            completion(self.desiredSize)
        }
    }

    var desiredSize: CGSize {
        // NOTE: Maps does not respect desired size.
        return self.extensionContext!.hostedViewMaximumAllowedSize
    }

}
```

[Next](Projects-RideMaps-ListRideOptionsIntentExtension-IntentHandler.swift.md)[Previous](Projects-RideMaps-RequestRideIntentExtension-IntentHandler.swift.md)

