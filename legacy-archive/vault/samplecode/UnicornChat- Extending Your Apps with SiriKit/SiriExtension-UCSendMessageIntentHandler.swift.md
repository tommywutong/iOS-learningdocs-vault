---
title: 'UnicornChat: Extending Your Apps with SiriKit'
apple_id: TP40017332
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/UnicornChat/Listings/SiriExtension_UCSendMessageIntentHandler_swift.html
archived_at: '2026-07-18T03:27:32.939347Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnicornChat: Extending Your Apps with SiriKit](UnicornChat-%20Extending%20Your%20Apps%20with%20SiriKit.md)


[Next](SiriExtension-UCIntentsHandler.swift.md)[Previous](UnicornChat-%20Extending%20Your%20Apps%20with%20SiriKit.md)

# SiriExtension/UCSendMessageIntentHandler.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The handler class for INSendMessageIntent.
*/

import Foundation
import Intents
import UnicornCore

class UCSendMessageIntentHandler: NSObject, INSendMessageIntentHandling {

    // MARK: 1. Resolve
    func resolveRecipients(forSendMessage intent: INSendMessageIntent, with completion: @escaping ([INPersonResolutionResult]) -> Swift.Void) {

        if let recipients = intent.recipients {
            var resolutionResults = [INPersonResolutionResult]()

            for recipient in recipients {
                let matchingContacts = UCAddressBookManager().contacts(matchingName: recipient.displayName)

                switch matchingContacts.count {
                    case 2 ... Int.max:
                        // We need Siri's help to ask user to pick one from the matches.
                        let disambiguationOptions: [INPerson] = matchingContacts.map { contact in
                            return contact.inPerson()
                        }

                        resolutionResults += [.disambiguation(with: disambiguationOptions)]

                    case 1:
                        let recipientMatched = matchingContacts[0].inPerson()
                        resolutionResults += [.success(with: recipientMatched)]

                    case 0:
                        resolutionResults += [.unsupported()]

                    default:
                        break
                }
            }

            completion(resolutionResults)

        } else {
            // No recipients are provided. We need to prompt for a value.
            completion([INPersonResolutionResult.needsValue()])
        }
    }

    func resolveContent(forSendMessage intent: INSendMessageIntent, with completion: @escaping (INStringResolutionResult) -> Swift.Void) {
        if let text = intent.content, !text.isEmpty {
            completion(INStringResolutionResult.success(with: text))
        }
        else {
            completion(INStringResolutionResult.needsValue())
        }
    }

    // MARK: 2. Confirm
    func confirm(sendMessage intent: INSendMessageIntent, completion: @escaping (INSendMessageIntentResponse) -> Swift.Void) {

        if UCAccount.shared().hasValidAuthentication {
            completion(INSendMessageIntentResponse(code: .success, userActivity: nil))
        }
        else {
            // Creating our own user activity to include error information.
            let userActivity = NSUserActivity(activityType: String(describing: INSendMessageIntent.self))
            userActivity.userInfo = [NSString(string: "error"):NSString(string: "UserLoggedOut")]

            completion(INSendMessageIntentResponse(code: .failureRequiringAppLaunch, userActivity: userActivity))
        }
    }

    // MARK: 3. Handle
    func handle(sendMessage intent: INSendMessageIntent, completion: @escaping (INSendMessageIntentResponse) -> Swift.Void) {
        if intent.recipients != nil && intent.content != nil {
            // Send the message.
            let success = UCAccount.shared().sendMessage(intent.content, toRecipients: intent.recipients)
            completion(INSendMessageIntentResponse(code: success ? .success : .failure, userActivity: nil))
        }
        else {
            completion(INSendMessageIntentResponse(code: .failure, userActivity: nil))
        }
    }
}
```

[Next](SiriExtension-UCIntentsHandler.swift.md)[Previous](UnicornChat-%20Extending%20Your%20Apps%20with%20SiriKit.md)

