---
title: 'TCPTransports: Using Various Apple APIs to Run a TCP Connection'
apple_id: TP40017680
resource_type: Sample Code
platform: iOS
topic: null
technology: NetworkExtension
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/samplecode/TCPTransports/Listings/App_iOS_AppDelegate_swift.html
archived_at: '2026-07-18T03:25:59.781556Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCPTransports: Using Various Apple APIs to Run a TCP Connection](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)


[Next](App-iOS-ActiveConversation.swift.md)[Previous](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)

# App-iOS/AppDelegate.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Main app controller.
 */

import UIKit

@UIApplicationMain
class AppDelegate : UIResponder, UIApplicationDelegate, EndpointPicker.Delegate, ActiveConversation.Delegate {

    var window: UIWindow?

    /// This is the initial view, which allows the user to configure and start a
    /// connection.

    private var endpointPicker: EndpointPicker!

    func application(_ application: UIApplication, willFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = nil) -> Bool {
        self.endpointPicker = ((window?.rootViewController! as! UINavigationController).viewControllers[0] as! EndpointPicker)
        self.endpointPicker.endpoint = UserDefaults.standard.lastEndpoint
        self.endpointPicker.delegate = self
        return true
    }

    /// If there’s a conversation view on screen, this controller manages it.

    private var activeConversation: ActiveConversation? = nil

    func check(endpointPicker: EndpointPicker) -> String? {
        // Constructing the transport and then throwing it away is a bit of a
        // waste because it’s not actively toxic because transports don’t do
        // anything exciting until you call `start()`.  I could fix this by
        // caching the transport to be picked up by `prepareStartConnection(…)`,
        // but the reality is that this is not a big enough deal in this sample
        // to justify writing that code.
        do {
            _ = try ConversationTransport(endpoint: endpointPicker.endpoint)
            return nil
        } catch BSDSocketsTransport.Error.tlsNotSupported {
            return NSLocalizedString("_The_BSD_Sockets_transport_does_not_support_tls_", comment: "Body of alert view.")
        } catch BSDSocketsTransport.Error.numericAddressRequired {
            return NSLocalizedString("_The_BSD_Sockets_transport_requires_an_numeric_ip_address_", comment: "Body of alert view.")
        } catch NWTCPTransport.Error.nwTCPConnectionNotSupported {
            return NSLocalizedString("_The_NWTCPConnection_transport_is_not_supported_in_an_application_context_", comment: "Body of alert view.")
        } catch {
            return NSLocalizedString("_The_transport_youve_selected_doesnt_support_this_configuration_", comment: "Body of alert view.")
        }
    }

    func prepareStartConnection(segue: UIStoryboardSegue, endpointPicker: EndpointPicker) {
        precondition(self.activeConversation == nil)    // All is lost if we try to show a conversation while already showing one.

        // Get our connection info and persist it to user defaults.

        let endpoint = endpointPicker.endpoint
        UserDefaults.standard.lastEndpoint = endpoint

        // Create a transport from the connection info.  Note that this
        // shouldn’t throw because of the check in
        // `shouldPerformStartConnectionSegue(…)`, above.

        let conversationTransport = try! ConversationTransport(endpoint: endpointPicker.endpoint)

        // Get the destination view controller, combine it with the transport,
        // and create the active conversation.

        let conversationViewController = (segue.destination as! UINavigationController).viewControllers[0] as! ConversationViewController

        let activeConversation = ActiveConversation(viewController: conversationViewController, transport: conversationTransport)
        self.activeConversation = activeConversation
        activeConversation.delegate = self
        activeConversation.start()
    }

    func close(activeConversation: ActiveConversation) {
        self.endpointPicker.dismiss(animated: true) {
            assert(self.activeConversation != nil)          // I want to know about this in debug builds.
            if let activeConversation = self.activeConversation {
                activeConversation.stop()
                self.activeConversation = nil
            }
        }
    }
}

private extension UserDefaults {

    /// This property makes it easy to save and restore the user’s last chose endpoint.

    var lastEndpoint: Endpoint {
        get {
            guard let data = self.data(forKey: "lastEndpoint"),
                let result = try? PropertyListDecoder().decode(Endpoint.self, from: data)
                else {
                return Endpoint.empty
            }
            return result
        }
        set {
            guard let data = try? PropertyListEncoder().encode(newValue) else {
                assert(false)   // tell me in debug builds
                return
            }
            self.set(data, forKey: "lastEndpoint")
        }
    }
}
```

[Next](App-iOS-ActiveConversation.swift.md)[Previous](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)

