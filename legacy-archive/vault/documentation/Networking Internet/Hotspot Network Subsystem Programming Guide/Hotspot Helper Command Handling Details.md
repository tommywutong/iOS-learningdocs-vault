---
title: Hotspot Network Subsystem Programming Guide
apple_id: TP40016639
resource_type: Guide
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: NetworkExtension
published: '2015-12-03'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/Hotspot_Network_Subsystem_Guide/Contents/CommandHandlingDetails.html
archived_at: '2026-07-15T08:18:49.613882Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Hotspot Network Subsystem Programming Guide](About%20the%20Hotspot%20Network%20Subsystem.md)


[Next](Important%20Guidelines.md)[Previous](Hotspot%20Network%20Scan%20List%20Filtering.md)

# Hotspot Helper Command Handling Details

This chapter describes how the various commands should be handled by the Hotspot Helper. The terms _helper_ and _application_ are used interchangeably to refer to the application that is working as a Hotspot Helper.

The `kNEHotspotHelperCommandTypeFilterScanList` command is issued to all helpers when the Wi-Fi network list is presented to the user.

The helper uses the `networkList` property of the command w`NEHotspotHelperCommand` to retrieve the list of nearby Wi-Fi networks. Each Wi-Fi network is represented by a `NEHotspotNetwork` object. For any network that the helper can handle, it annotates the `NEHotspotNetwork` and adds it to a new list. When the list is complete, it creates an `NEHotspotHelperResponse` and annotates it using the `setNetworkList`: method. If the Hotspot Helper is unable to handle any of the nearby networks, it provides a response without invoking the `setNetworkList`: method.

The `kNEHotspotHelperCommandTypeEvaluate` command is issued as part of the authentication state machine. The application is expected to evaluate the current network and give an indication of its ability to handle the network. Properties of the current network are accessed via the network property of the `NEHotspotHelperCommand` object. The type of the network property is an `NEHotspotNetwork`. The `NEHotspotNetwork` provides access to various Wi-Fi properties, including SSID and BSSID.

The evaluation performed by the helper could be a simple table lookup, or it could involve sending network traffic to further examine the network. It is critical that the helper respond accurately and not claim networks that it does not recognize.

The helper has at most 45 seconds to perform the evaluation. As soon as one helper provides a response indicating that it handles the network with high confidence, the responses from all other helpers are ignored. The helpers that have not responded yet go back into the background. This is to ensure that there are no unnecessary delays getting onto the network.

The `kNEHotspotHelperCommandTypeAuthenticate` command is issued to the chosen helper that was deemed best in the __Evaluating__ state.

The helper is expected to perform whatever network operations are required to take the network out of captivity. The helper has 45 seconds to perform the authentication. If authentication is successful, the helper provides an `NEHotspotHelperResponse` that indicates `kNEHotspotHelperResultSuccess` and the state machine transitions to the __Authenticated__ state.

If the helper determines that the network is not one it can actually handle, it returns a result of `kNEHotspotHelperResultUnsupportedNetwork`. In this case, the state machine adds the helper to the exclude list and transitions back to the __Evaluating__ state.

If the helper encounters a fatal failure, it returns `kNEHotspotHelperResultFailure`. The Wi-Fi network is disassociated, and auto-join on that network is disabled. If the helper encountered a temporary failure, it returns `kNEHotspotHelperResultTemporaryFailure`. The Wi-Fi network is disassociated, but auto-join on the network is not disabled.

If the helper requires user input to continue, it creates a `UILocalNotification` to draw the user’s attention and returns `kNEHotspotHelperResultUIRequired`.

This table summarizes how the various result codes are interpreted:

| Authenticate result | Interpretation | Next state |
| --- | --- | --- |
| `kNEHotspotHelperResultSuccess` | Authentication successful; interface no longer captive; ready for general internet traffic. | __Authenticated__ |
| `kNEHotspotHelperResultUnsupportedNetwork` | Not actually a network handled by the helper. | __Evaluating__ |
| `kNEHotspotHelperResultTemporaryFailure` | A temporary error occurred; auto-join not changed. | __Failure__ |
| `kNEHotspotHelperResultUIRequired` | User interaction is required. | __PresentingUI__ |
| `kNEHotspotHelperResultFailure` (or any other result) | A fatal error occurred; auto-join disabled. | __Failure__ |

The `kNEHotspotHelperCommandTypePresentUI` command is issued after the chosen helper returns `kNEHotspotHelperResultUIRequired` in the __Authenticating__ state. The application has unlimited time to respond to this command. This command does not cause the application to run in the background.

After user interaction and authentication is complete, the helper provides a result of `kNEHotspotHelperResultSuccess` and the state machine transitions to the __Authenticated__ state.

If the helper determines that the network is not one it can actually handle, it returns a result of `kNEHotspotHelperResultUnsupportedNetwork`. This result causes the authentication state machine to add the helper to the exclude list and transition back to the __Evaluating__ state.

If the helper is not successful, it returns `kNEHotspotHelperResultFailure`.

The following table summarizes how the result values are interpreted:

| PresentUI result | Interpretation | Next state |
| --- | --- | --- |
| `kNEHotspotHelperResultSuccess` | Authentication successful; interface no longer captive; ready for general internet traffic. | __Authenticated__ |
| `kNEHotspotHelperResultUnsupportedNetwork` | Not actually a network handled by the helper. | __Evaluating__ |
| `kNEHotspotHelperResultTemporaryFailure` | A temporary error occurred; auto-join not changed. | __Failure__ |
| `kNEHotspotHelperResultFailure` (or any other result) | A fatal error occurred; auto-join disabled. | __Failure__ |

The `kNEHotspotHelperCommandTypeMaintain` command is issued to the chosen helper in two instances:

- Periodically (currently every 300 seconds), to give it an opportunity to redetect captivity while connected to the network.
- When rejoining a network that the chosen helper previously handled.

The helper has 45 seconds to send a response.

If the helper returns `kNEHotspotHelperResultSuccess`, the state machine transitions back to the __Authenticated__ state.

If the helper returns `kNEHotspotHelperResultAuthenticationRequired`, the state machine transitions back to the __Authenticating__ state to have the plug-in perform the authentication.

If the helper returns `kNEHotspotHelperResultFailure`, the state machine transitions back to the __Evaluating__ state.

The following table summarizes how the result values are interpreted:

| Maintain Result | Interpretation | Next State |
| --- | --- | --- |
| `kNEHotspotHelperResultSuccess` | Operation successful. | __Authenticated__ |
| `kNEHotspotHelperResultAuthenticationRequired` | Network requires authentication. | __Authenticating__ |
| `kNEHotspotHelperResultFailure` (or any other result) | An error occurred. | __Evaluating__ |

The `kNEHotspotHelperCommandTypeLogoff` command is issued to the chosen helper to initiate its logoff processing. Currently this command is provided to the helper after it invokes the `NEHotspotHelper` `logoff`: class method:

```
 (BOOL)logoff:(NEHotspotNetwork *)network;
```

The network object must correspond to the currently authenticated Wi-Fi network. The helper must also be the one that performed the authentication. If those conditions are not met, this function returns `FALSE`.

After the helper successfully invokes the `logoff`: method, the authentication state machine enters the __LoggingOff__ state and a command of type `kNEHotspotHelperCommandTypeLogoff` is passed to the helper’s handler block.

The helper has 45 seconds to respond to the command. Once the helper responds to the command, or 45 seconds have elapsed, the Wi-Fi network is disassociated and the authentication state machine enters the __Inactive__ state.

[Next](Important%20Guidelines.md)[Previous](Hotspot%20Network%20Scan%20List%20Filtering.md)

