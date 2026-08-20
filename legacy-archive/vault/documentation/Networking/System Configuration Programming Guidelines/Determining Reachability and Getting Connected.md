---
title: System Configuration Programming Guidelines
apple_id: TP40001065
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: SystemConfiguration
published: '2006-02-07'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/SystemConfigFrameworks/SC_ReachConnect/SC_ReachConnect.html
archived_at: '2026-07-15T08:18:27.020662Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [System Configuration Programming Guidelines](Introduction%20to%20System%20Configuration%20Programming%20Guidelines.md)


[Next](Document%20Revision%20History.md)[Previous](The%20System%20Configuration%20Schema.md)

# Determining Reachability and Getting Connected

This chapter describes the System Configuration reachability and connection APIs. You use the reachability API to determine if data destined for a remote host can leave the local machine. To start or stop a PPP connection, you use the connection API.

It is not necessary to have an in-depth understanding of the System Configuration architecture to determine reachability or start a PPP connection. The reachability and connection APIs provide a layer of abstraction that allows an application to make connections without worrying about the state of the network stack.

Many types of applications need to find out if a remote host is reachable or to start a PPP-based connection. For example, an application might need to check for software updates that are available from a remote server. In OS X version 10.3 and later, the System Configuration framework provides APIs to accomplish these tasks quickly and easily, without requiring a detailed knowledge of System Configuration architecture. In particular, the reachability and connection APIs do much of their work behind the scenes, so the application does not have to poll for status changes or watch specific keys in the dynamic store.

The System Configuration reachability API helps an application determine if a remote host is reachable. A remote host is considered reachable if a data packet sent to the host can leave the local computer, regardless of what ultimately happens to the packet. In other words, the reachability of a remote host does not guarantee that the host will receive the data.

In practice, when a remote host is deemed reachable, but the packets you send to it fail to arrive, the myriad possible reasons for the failure fall into two broad categories:

1. A part of the Internet connection over which you have no control is broken. For example, the remote host’s server is down.
2. A part of your local network infrastructure over which you might have control is broken. For example, your modem hasn’t dialed or your AirPort base station is turned off.

The reachability API cannot help you with problems in the first category. As long as data packets can leave the local machine, the remote host is considered reachable. What the reachability API can provide is help diagnosing some of the problems in the second category. If, for example, the modem is currently disconnected, the API can tell you this.

To further define the scope of the System Configuration reachability and connection APIs, this document uses the following phrases to distinguish between two different types of network connection:

- _Network transport connection_. This is a TCP-based connection you initiate using, for example, BSD sockets.
- _Network link connection_. This is a PPP-based connection you initiate by, for example, telling the modem to dial.

The reachability API helps you determine if a remote host is reachable by examining the status of the local network link connection. The connection API allows you to start a network link connection. After you successfully start a network link connection, you use different API (such as Core Foundation networking API) to establish a network transport connection.

Determining reachability and requesting a network link connection often go hand in hand. As an example, consider the running of an email application. The sequence of events might go like this:

1. The user launches the email application to check her email.
2. The email application uses the reachability API to find out if the POP server is reachable.
3. The reachability API tells the application that the POP server is reachable, but that a network link connection must first be made.
4. The email application asks the user if she wants to dial the modem and she clicks “OK”. (The application might skip this step if the user has set a preference that tells the modem to dial automatically when the email application is launched.)
5. The email application uses the connection API to start a PPP connection, which causes the modem to dial. At this point, the email application can return to its work.
6. The reachability API notifies the email application that the network link connection is up and the email application then uses a network transport connection to fetch the email.

After the email application delivers the email to the user, it might or might not cause the PPP connection to drop, depending on the user’s preferences. Either way, when the email application quits, the PPP connection is dropped and, if the email application held the last reference to the connection, the modem disconnects. For more information on connection references, see [Starting and Stopping a Connection](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrvfvbuqmrqgqwviucykjcummjrga).

In versions of OS X prior to 10.3, the System Configuration reachability API consisted of two functions. The functions, [SCNetworkCheckReachabilityByAddress](https://developer.apple.com/documentation/systemconfiguration/1420208-scnetworkcheckreachabilitybyaddr) and [SCNetworkCheckReachabilityByName](https://developer.apple.com/documentation/systemconfiguration/1420196-scnetworkcheckreachabilitybyname), supply information about the reachability of a remote host by providing a set of flags. The flags (defined in `SCNetwork.h`) indicate, for example, that the specified remote host could be reached using the current network configuration. Unfortunately, these functions encouraged polling because they did not support notifications.

In OS X version 10.3, the System Configuration framework introduced the SCNetworkReachability API which supports asynchronous notifications of changes in the connection to a remote host. You still get the same set of connection-status flags the previous reachability functions supplied to determine if a connection is required, but you no longer have to poll to find out if a connection attempt is successful.

Most functions in the new API rely on an `SCNetworkReachabilityRef` (defined in `SCNetworkReachability.h`) you use to identify the remote target. You create this reference for a specific address or hostname and use it to add the reference to your run loop and set up a callback function. You can use the information in the connection-status flags to request a network link connection and the new reachability API notifies you when the connection is established.

You can use the new reachability functions in your application to perform the following tasks:

- Create a reference for your target remote host you can use in other reachability functions.
- Add the target to your run loop.
- Provide a callback function that’s called when the reachability status of your target changes.
- Determine if the target is reachable.

The following sections describe how to use the SCNetworkReachability functions to perform these tasks. For a code example demonstrating how to use the SCNetworkReachability API, see _[SimpleReach](../../../samplecode/SimpleReach/SimpleReach.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmrtha)_.

The SCNetworkReachability API provides three functions that create a target reference you can use to monitor the reachability of a remote host:

- [SCNetworkReachabilityCreateWithAddress](https://developer.apple.com/documentation/systemconfiguration/1514895-scnetworkreachabilitycreatewitha)
- [SCNetworkReachabilityCreateWithAddressPair](https://developer.apple.com/documentation/systemconfiguration/1514908-scnetworkreachabilitycreatewitha)
- [SCNetworkReachabilityCreateWithName](https://developer.apple.com/documentation/systemconfiguration/1514904-scnetworkreachabilitycreatewithn)

If you are interested in the reachability of only the remote host, you can use either `SCNetworkReachabilityCreateWithAddress` or `SCNetworkReachabilityCreateWithName`. For `SCNetworkReachabilityCreateWithAddress`, you supply a remote host address in a `sockaddr` structure. For more information on the `sockaddr` structure, see the networking `man` page at [http://developer.apple.com/documentation/Darwin/Reference/ManPages/man4/netintro.4.html](https://developer.apple.com/documentation/Darwin/Reference/ManPages/man4/netintro.4.html). For `SCNetworkReachabilityCreateWithName`, you supply a remote host name, such as www.apple.com.

If you need to monitor possible changes to both the local and remote host addresses, you use the `SCNetworkReachabilityCreateWithAddressPair` function. This function returns a reference you can use to find out if:

- The address of your local host changes
- The remote address becomes unreachable
- The network route associated with the remote host changes

All three functions return an object of type `SCNetworkReachabilityRef` for the remote host, which you can use in any of the other SCNetworkReachability functions.

To ensure that your application receives notification when the reachability status of the target remote host changes, you add the target’s `SCNetworkReachabilityRef` to your application’s run loop. A run loop monitors sources of input to an application. When an input source becomes ready for processing (because some activity occurs), the run loop dispatches control to a callback function associated with the input source. For more information on run loops and modes, see _[Run Loops](../../Core%20Foundation/Run%20Loops/Introduction%20to%20Run%20Loops.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeztk2i)_.

For a network-aware application, the input source is the `SCNetworkReachabilityRef`, the activity is a change in the target’s connection status, and the callback function is one you provide. Thus, by using the reachability API to add your target to your application’s run loop and to provide a callback function (described in [Associating a Callback Function With the Target](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrvfvbuqmrqgqwuescbijceuq2d)), you ensure your application will be notified of changes in the target’s reachability.

To add an `SCNetworkReachabilityRef` to your application’s run loop, you use the [SCNetworkReachabilityScheduleWithRunLoop](https://developer.apple.com/documentation/systemconfiguration/1514894-scnetworkreachabilityschedulewit) function. You provide the `SCNetworkReachabilityRef`, a reference to your application’s run loop, and the mode in which the run loop should run, typically the default mode.

To remove an `SCNetworkReachabilityRef` from your application’s run loop, you use the [SCNetworkReachabilityUnscheduleFromRunLoop](https://developer.apple.com/documentation/systemconfiguration/1514899-scnetworkreachabilityunschedulef) function, which requires the same parameters as the `SCNetworkReachabilityScheduleWithRunLoop` function.

To make use of the notifications the reachability API provides, you should associate a callback function with the `SCNetworkReachabilityRef` representing the remote host you’re interested in. The callback function might display the change in the connection to the user or perform some other task.

To associate a callback function with your target, you first define a function of type `SCNetworkReachabilityCallBack` (this type is defined in `SCNetworkReachability.h`). To pass contextual information about the changes to your callback function, you define a structure of type [SCNetworkReachabilityContext](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycontext). You use the `info` argument to contain the context information (you can also specify NULL, if context information is unnecessary). Finally, you pass the callback function, the `SCNetworkReachabilityRef` representing the remote host, and the context to the [SCNetworkReachabilitySetCallback](https://developer.apple.com/documentation/systemconfiguration/1514903-scnetworkreachabilitysetcallback) function.

The SCNetworkReachability API provides the [SCNetworkReachabilityGetFlags](https://developer.apple.com/documentation/systemconfiguration/1514924-scnetworkreachabilitygetflags) function you can use to determine the reachability of a remote host. This function supplies the same connection-status flags the older reachability functions defined in `SCNetwork.h` supplied.

To use this function, you supply the `SCNetworkReachabilityRef` for your remote host and the address of the variable you declare to contain the flags. The flags you can receive are listed in Table 4-1.

__Table 4-1__  `SCNetworkConnectionFlags`

| Flag name | Meaning |
| `kSCNetworkFlagsTransientConnection` | The target is reachable through a transient connection (for example, PPP). |
| `kSCNetworkFlagsReachable` | The target is reachable using the current network configuration. |
| `kSCNetworkFlagsConnectionRequired` | The target is reachable using the current network configuration, but a connection must be established first. For example, a suitable dialup connection exists, but it is not active. |
| `kSCNetworkFlagsConnectionAutomatic` | The target is reachable using the current network configuration, but a connection must be established first. Further, any traffic directed to the target will automatically initiate the connection. |
| `kSCNetworkFlagsInterventionRequired` | The target is reachable using the current network configuration, but a connection must be established first. Further, some user action is required to establish connection (for example, providing a password). |
| `kSCNetworkFlagsIsLocalAddress` | The target is associated with a network interface on the current system. For example, the target address is one of the IP addresses assigned to the system. |
| `kSCNetworkFlagsIsDirect` | Network traffic to the target will not pass through a router because the destination address is on a network that’s directly connected to one of the local machine’s interfaces (for example, it’s on the same subnet as the local machine). |

In OS X version 10.3, the System Configuration framework introduced the SCNetworkConnection API. This API allows an application to control connection-oriented services already defined in the system. Currently, an application can control only PPP services with this API.

In addition to controlling an existing service, an application can use the SCNetworkConnection API to get information about the connection. The API provides connection-status information on two levels:

- High-level, generic information that describes the status of the network connection, such as connected or disconnected
- Detailed, PPP-specific information that describes the status of the PPP stack

These two levels of status information target different types of applications. A network-aware application might want to display whether or not a network link connection is live, but is probably uninterested in knowing if the PPP controller is currently configuring the link layer. A complex dialer application, on the other hand, might need to know exactly what the PPP controller is doing at each step of the connection process.

Although these functions are defined in the same header file, this chapter does not describe the PPP-specific connection-status functions in `SCNetworkConnection.h`. For more information on how to use these functions and how to use the System Configuration schema to interpret the results, see [The System Configuration Schema](The%20System%20Configuration%20Schema.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrvfvbuqmrqgmwugscejfeeiq2h). Instead, this chapter focuses on the remainder of the SCNetworkConnection API, describing how an application can use it to accomplish the following tasks:

- Create a reference representing the connection you can use with other connection functions.
- Add the connection reference to your application’s run loop.
- Start a connection.
- Get the status of a connection.
- Stop an existing connection.

For a code example demonstrating the use of the SCNetworkConnection API, see _[SimpleDial](../../../samplecode/SimpleDial/SimpleDial.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmrtg4)_.

The SCNetworkConnection API provides one function you can use to create a connection reference: `SCNetworkConnectionCreateWithServiceID`. To use this function, you supply a service ID and a callback function, along with a couple of other parameters, and you receive an object of type `SCNetworkConnectionRef`. You use this object to represent the connection in the other SCNetworkConnection functions.

Because you’ll be using the `SCNetworkConnectionRef` to refer to a specific PPP connection, you must supply a unique service ID to identify it. There are two ways to get this service ID. One way is to look in the dynamic store for available services and choose one. The second way is for your application to use the `SCNetworkConnectionCopyUserPreferences` function to get the default service ID (the one the Internet Connect application uses).

Although you can pass NULL for the callback function parameter, it is not recommended. If you don’t define a callback function, your application will not receive status-change notifications and will have to poll for updates.

To ensure your application gets notified of changes in a specific connection’s status, you can add the `SCNetworkConnectionRef` representing the connection to your application’s run loop. When the connection’s status changes, the `SCNetworkConnectionRef` alerts the run loop and the run loop passes control to the callback function you provide.

To add an `SCNetworkConnectionRef` to your application’s run loop, you use the `SCNetworkConnectionScheduleWithRunLoop` function. You provide the `SCNetworkConnectionRef`, a reference to your application’s run loop, and the mode in which the run loop should run (in most cases, the default mode). For more information on run loops and modes, see [Introduction to Run Loops](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFRunLoops/CFRunLoops.html#//apple_ref/doc/uid/10000135) in the [Core Foundation Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000421).

To remove the `SCNetworkConnectionRef` from your application’s run loop, you use the `SCNetworkConnectionUnscheduleFromRunLoop` function. Like the `SCNetworkConnectionScheduleWithRunLoop` function, this function expects the `SCNetworkConnectionRef`, a reference to your application’s run loop, and the run loop mode.

The SCNetworkConnection API provides two functions your application can use to control a connection using an `SCNetworkConnectionRef` object:

- `SCNetworkConnectionStart`
- `SCNetworkConnectionStop`

Both functions return immediately while the connection or disconnection process they initiate proceeds asynchronously. If you add the connection’s `SCNetworkConnectionRef` to your application’s run loop and provide a callback function, your application is notified when the status of the connection changes. Your application can then check the status to determine if the connection process is complete. If you don’t add the connection reference to the run loop, you will have to poll to discover the connection status, and this is not recommended.

By default, the `SCNetworkConnectionStart` function uses the user’s preferred connection settings to start the connection. You can, however, provide a dictionary of values to override some of these settings for the duration of the connection.

If you do provide a dictionary of additional settings be aware that:

- The dictionary must be in the correct format for a network service dictionary (described in [The NetworkServices Dictionary](The%20System%20Configuration%20Schema.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrvfvbuqmrqgmwugsceizbeiq2c)). If you do not follow this format precisely, the PPP controller may ignore the dictionary.
- The PPP controller merges the settings you provide with the user’s existing settings before the connection is established, ignoring any inappropriate values in your dictionary.

Starting and stopping a connection are implicitly arbitrated. This means that the interest other applications may have in a connection is taken into account before the connection is stopped. For example, application “B” can start a connection that has already been started by application “A”. Application “A” may choose to stop the connection but the system should not stop the connection until “B” is finished with it. Using the SCNetworkConnection functions, application “A” can call `SCNetworkConnectionStop` on the connection and the function will return success, but the connection will not stop until “B” calls `SCNetworkConnectionStop`. An application can also use the `linger` parameter (discussed below) to register interest.

The `SCNetworkConnectionStart` function allows an application to indicate an interest in a connection. In this way, an application can request that the existence of the connection be tied to actions the application takes. In the simplest case, an application might want a connection to start when the application calls `SCNetworkConnectionStart` and stop when any of the following events occur:

- The application quits.
- The application releases the `SCNetworkConnectionRef` representing the connection.
- The application calls `SCNetworkConnectionStop`.

To indicate interest in a connection, an application can use the `linger` parameter of the `SCNetworkConnectionStart` function. An application, such as an email client, that needs to get connected, perform its tasks, and get disconnected, sets the parameter to `FALSE`. This indicates that the connection should stop when the application quits or releases the connection reference. A PPP dialer application, on the other hand, might choose to set the parameter to `TRUE` so that the user has control over the modem. The `TRUE` value indicates the connection should _not_ stop when the application quits or releases the connection reference.

It’s important to note, however, that several concurrent applications might register interest in the same connection. When this is the case, the System Configuration framework keeps track of the references to the connection, stopping it when the last reference is released (or the last application holding a reference quits).

The `SCNetworkConnectionStop` function performs an arbitrated stop of the connection. In other words, it closes the connection if:

- There are no other interested applications currently running or holding references to the connection. If there are, the `SCNetworkConnectionStop` function returns success to the calling application, but the connection will persist until all interested applications terminate or release their references to the connection.
- An application calls `SCNetworkConnectionStop` and passes `TRUE` in the `forceDisconnect` parameter. This stops the connection regardless of the interest of other currently running applications. Most applications do not need to force a connection to stop in this way. A PPP dialer application, however, would probably choose to do this because it ensures that the connection stops when the user wants it to.

An application can use the `SCNetworkConnectionGetStatus` function to get the high-level status of the connection. You pass the `SCNetworkConnectionRef` representing the connection to the function and you receive one of the constants shown in [Introduction to System Configuration Programming Guidelines](Introduction%20to%20System%20Configuration%20Programming%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrvfvbuqmrqgewviucykjcummjqge).

__Table 4-2__  High-level connection status values

| Status | Meaning |
| `kSCNetworkConnectionInvalid` | The network connection refers to an invalid service. |
| `kSCNetworkConnectionDisconnected` | The network connection is disconnected. |
| `kSCNetworkConnectionConnecting` | The network connection is connecting. |
| `kSCNetworkConnectionConnected` | The network connection is connected. |
| `kSCNetworkConnectionDisconnecting` | The network connection is disconnecting. |

If your application needs to know more about the PPP connection, such as when the PPP controller is authenticating to the server, you should use the `SCNetworkConnectionCopyExtendedStatus` function. You pass the `SCNetworkConnectionRef` representing the connection to the function and you receive a dictionary that contains subdictionaries for each subcomponent of the service, such as PPP, IPv4, and Modem. The PPP connection status is represented by a constant defined in the SCNetworkConnection API. [Table 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrvfvbuqmrqgqwueqkci5cucq2d) shows the current set of constants. Note that additional status values might be defined in the future, so your application should be able to handle an unknown value.

__Table 4-3__  PPP connection status values

| Status | Meaning |
| `kSCNetworkConnectionPPPDisconnected` | PPP is disconnected. |
| `kSCNetworkConnectionPPPInitializing` | PPP is initializing. |
| `kSCNetworkConnectionPPPConnectingLink` | PPP is connecting the lower layer (as when, for example, the modem is dialing out). |
| `kSCNetworkConnectionPPPDialOnTraffic` | PPP is waiting for networking traffic to automatically establish the connection. |
| `kSCNetworkConnectionPPPNegotiatingLink` | The PPP lower layer is connected and PPP is negotiating the link layer (the LCP protocol). |
| `kSCNetworkConnectionPPPAuthenticating` | PPP is authenticating to the server (using PAP, CHAP, MSCHAP, or EAP protocol). |
| `kSCNetworkConnectionPPPWaitingForCallBack` | PPP is waiting for the server to call back. _Note_: this state is defined but will not occur because CallBack is not supported in OS X version 10.3. |
| `kSCNetworkConnectionPPPNetgotiatingNetwork` | PPP is authenticated and is now negotiating the networking layer (using IPCP or IPv6CP protocol). |
| `kSCNetworkConnectionPPPConnected` | PPP is fully connected for at least one networking layer. Additional networking protocols might still be negotiating. |
| kSCNetworkConnectionPPPTerminating | PPP networking and link protocols are terminating. |
| `kSCNetworkConnectionPPPDisconnectingLink` | PPP is disconnecting the lower connection layer (as when, for example, the modem is hanging up). |
| `kSCNetworkConnectionPPPHoldingLinkOff` | PPP is disconnected and maintaining the link temporarily “off”. |
| `kSCNetworkConnectionPPPSuspended` | PPP is suspended as the result of the “suspend” command as when, for example, a V92 Modem is “On Hold”. |
| `kSCNetworkConnectionPPPWaitingForRedial` | PPP found a busy server and is waiting for redial. |

For more information on why you might choose to use the `SCNetworkConnectionCopyExtendedStatus` function, see [Getting Detailed PPP Connection-Status Information](The%20System%20Configuration%20Schema.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrvfvbuqmrqgmwugscejbcegskf).

[Next](Document%20Revision%20History.md)[Previous](The%20System%20Configuration%20Schema.md)

