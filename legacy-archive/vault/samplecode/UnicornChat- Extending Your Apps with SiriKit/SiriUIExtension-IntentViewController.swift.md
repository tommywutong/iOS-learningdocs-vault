---
title: 'UnicornChat: Extending Your Apps with SiriKit'
apple_id: TP40017332
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/UnicornChat/Listings/SiriUIExtension_IntentViewController_swift.html
archived_at: '2026-07-18T03:27:33.052471Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnicornChat: Extending Your Apps with SiriKit](UnicornChat-%20Extending%20Your%20Apps%20with%20SiriKit.md)


[Next](README.md.md)[Previous](SiriExtension-UCIntentsHandler.swift.md)

# SiriUIExtension/IntentViewController.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The view controller providing a user interface for the intent.
*/

import IntentsUI
import UnicornCore

class IntentViewController: UIViewController, INUIHostedViewControlling, INUIHostedViewSiriProviding {

    // MARK: INUIHostedViewControlling

    func configure(with interaction: INInteraction!, context: INUIHostedViewContext, completion: ((CGSize) -> Void)!) {
        var size: CGSize

        // Check if the interaction describes a SendMessageIntent.
        if interaction.representsSendMessageIntent {
            // If it is, let's set up a view controller.
            let chatViewController = UCChatViewController()
            chatViewController.messageContent = interaction.messageContent

            let contact = UCContact()
            contact.name = interaction.recipientName
            chatViewController.recipient = contact

            switch interaction.intentHandlingStatus {
                case .unspecified, .inProgress, .ready, .failure:
                    chatViewController.isSent = false

                case .success, .deferredToApplication:
                    chatViewController.isSent = true
            }

            present(chatViewController, animated: false, completion: nil)

            size = desiredSize
        }
        else {
            // Otherwise, we'll tell the host to draw us at zero size.
            size = CGSize.zero
        }

        completion(size)
    }

    var desiredSize: CGSize {
        return extensionContext!.hostedViewMaximumAllowedSize
    }

    var displaysMessage: Bool {
        return true
    }
}
```

[Next](README.md.md)[Previous](SiriExtension-UCIntentsHandler.swift.md)

