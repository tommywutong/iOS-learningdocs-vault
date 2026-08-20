---
title: Cellular Best Practices Guide
apple_id: TP40013998
resource_type: Guide
platform: iOS
topic: Performance
technology: null
published: '2014-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CellularBestPractices/BestPractices/BestPractices.html
archived_at: '2026-07-18T01:43:23.523027Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cellular Best Practices Guide](About%20Creating%20Efficient%20Cellular%20Apps.md)


[Next](Instruments%20Analysis%20Tool.md)[Previous](Cellular%20Processors-%20Interface%20to%20the%20Cellular%20Network.md)

# Best Practices for Developing Cellular Apps

Apple engineers analyzed the performance of many third-party apps, included streaming, gaming, messaging, and productivity apps. The analysis used more than 50 metrics, including:

- Control plane overhead
- Data consumption on the cellular interface
- Wi-Fi/cellular interface behavior
- Power consumption specific to cellular usage
- Background and active modes

The analysis, including experience with Apple’s own apps, resulted in several “best practices” for application development.

Limit app background activity either by bundling your requests or by making requests when another app has already initiated a connection (if that can be determined).

Background activity is not based on interactions with the user but rather on some other desired pattern of communication. Here are two examples.

The example in Figure 3-1 shows excessive, low-volume, background traffic because of a recurrent keepalive signal that runs even when the app is in the background, repeatedly initiating a new connection to transmit a very small amount of data. Although this kind of pinging is typically not a problem in Ethernet and Wi-Fi apps, repeated, independent connections, even with small amounts of data, can create large amounts of overhead with cellular connections.

__Figure 3-1__  A view of background “pings” that need to be eliminated

!

In this case, the background pings should be eliminated or bundled with other connections.

Figure 3-2 shows a problem with the advertising framework the app is using. In the background, separate from the app’s activity, the framework is downloading ads at irregular intervals. Although each download has very little data, each one requires new control plane connections.

__Figure 3-2__  A view of unbundled ads, resulting in high overhead

!

The ad delivery mechanism needs to be redesigned to avoid the overhead that comes from downloading the ads one at a time.

Both of the examples in the previous section take place in the background, when the user is not actively using the app. Even when the user is actively interacting with an app, it may attempt to communicate with separate, small chunks of data which can produce large overhead.

Figure 3-3 shows an app in active mode, where intermittent connections with very small amounts of data are creating high cellular control plane overhead. In this case, the app has been designed to show text on the user’s screen and when the user scrolls down, new text is requested. As the user scrolls down a few lines at a time, new data is downloaded in small chunks, with a new connection for each chunk.

Reorganizing the download process can make more efficient use of the connection overhead.

__Figure 3-3__  A view of excessive, low-volume, foreground traffic

!

Figure 3-4 shows a six-minute log of an app that is saving data to the cloud in real time. This example shows an app that is in active use. The user is repeatedly touching the screen and typing to select and edit the original input while composing text. Each time the user touches or types, the data is saved to the cloud, as if the user is not using an app on the device but is interacting with the cloud directly.

__Figure 3-4__  A view of an app saving data to the cloud in real time making numerous new connections

!!

Without any specific bundling of the data, every user interaction generates more cellular control plane overhead and additional data transfer. The lack of bundling thus impacts both the network overhead and the device's data plan.

Use power resources efficiently by monitoring user inputs to determine when an Auto-Lock override should be turned off.

The Auto-Lock feature on an iPhone sets the time that elapses before the iPhone automatically locks or turns off the display, if there is no user input. Typically, games attempt to override a device’s Auto-Lock functionality to provide what the game designers consider to be a better user experience. For example, a game may prevent the screen from going dark while the user is not taking any action. Generally, this is what the user wants—until the user sets the game down, walks away for half an hour, and returns to find a drained battery.

Figure 3-5 shows an example of a game that overrides the screen Auto-Lock functionality and keeps the screen on until the battery drains completely. A balance needs to be found between annoying the user unnecessarily and keeping the screen on without any checks for activity.

__Figure 3-5__  A game overriding the automatic dimming of the screen with disappointing results

!

Fortunately, this situation is easy to identify using the display brightness and sleep/wake instruments.

Honor device/user data plans with indications to user, especially when Wi-Fi is not available. Apps should not download or upload data for any purpose other than that needed for normal usage.

Figure 3-6 shows a very popular VoIP app that uses an ad hoc transport model, taking advantage of whatever connections are available. When it is open on a cellular device in background mode, the app’s flexible data transport model uses the cellular device as a router for other users’ data. Thus it is sending data that was never originated (intentionally or otherwise) by the user of the device and is eating into this user’s data plan. Worse, it initiates many new connections to do so, further increasing the overhead that consumes the user’s data allowance.

__Figure 3-6__  A VoIP app using your data plan to transport other users’ data

!!

Estimate of the number of connections that your app needs to function properly. When you see more connections than you expect, investigate to determine what is initiating those connections.

A video playback app can be a huge consumer of bandwidth if it makes no distinction between Wi-Fi and cellular connections.

In this example (Figure 3-7), a user began a video download while on a Wi-Fi connection. At some point, the device lost the Wi-Fi connection and transparently transitioned to a cellular connection, perhaps while the user walked from a building to a parking lot. The app gave the user no input and no choice of whether to continue the download under the new, potentially expensive, data channel.

__Figure 3-7__  Video playback downloading on Wi-Fi and unknowingly moving to cellular

!

Download data in as big a burst as possible for every connection, especially when using a cellular network.

The app in Figure 3-8 has all of its connections at the left side of the histogram. Because the app is creating few new connections, it might appear there is no problem with its download process. However, there is a repeating pattern in the download data: Large data spikes are alternating with periods of no data, approximately every ten seconds. Yet the app is not making new connections for these spikes.

__Figure 3-8__  An app's oscillating download pattern showing no new connections

!

This oscillating pattern is a more subtle overhead issue than simply creating new connections. Cellular traffic operates at different power and data levels within a single continuous connection. The choice of data rates is managed by the cellular network in negotiation with the mobile device. Even within a single connection, managing the transitions between low, medium, and high data rates requires communication overhead, as illustrated in Figure 3-9.

__Figure 3-9__  The communication overhead resulting from state transitions within a single connection

!

In Figure 3-10, an Apple internal analysis tool shows the actual Wideband Code Division Multiple Access (WCDMA) power and data states used by the device. They are oscillating along with the data bursts with short periods of high power and high data transfer between longer periods of medium power and little data. Although new connections are not being created, there is heavy communication overhead and wasted power with no data being transferred.

__Figure 3-10__  The data download rate affecting the power state, creating oscillation

!

In this app, an estimation of the data download rate determines the playback rate. Because a medium data rate predominates, the app specifies a lower playback quality, even though a higher playback quality could be easily supported.

This app determines how much to download based on the lower data rate. But because the block of data is sufficiently large to automatically put the device into high-power mode, the requested data packet completes quickly. This behavior leaves the processor and channel idle until the next packet comes due, scheduled according to the lower data rate.

The cellular processor runs at high or medium power over half of the time when no data is being transferred, thereby wasting resources and degrading the user experience.

Although the WCDMA state is not directly observable in Instruments, knowing about its state transition overhead may help you diagnose oscillating download problems like this and may help you to design apps that avoid this issue. If this app had a built-in understanding of the network’s power and data-rate transition criteria, it could transfer larger blocks of data at high power and deliberately go into low power between the blocks, conserving battery life while providing higher playback quality.

As an app developer, you need to be conscious of how data is being uploaded and downloaded by your app to avoid wasting network resources.

__Encoding and compression.__ Be aware of how much data is actually transmitted over the cellular interface per byte generated by the app. A single byte of data can have as much as 1500 bytes of overhead.

__Cache utilization.__ Use the cache efficiently to avoid unnecessary downloading of same data over and over again.

__Data request patterns.__ Look for patterns in how data is requested. Perhaps all the images of a webpage can be downloaded in one connection instead of making multiple connections.

Each of these aspects of data usage impacts the network through changes in the device’s state and through the generation of control plane traffic.

[Next](Instruments%20Analysis%20Tool.md)[Previous](Cellular%20Processors-%20Interface%20to%20the%20Cellular%20Network.md)

