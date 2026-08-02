---
title: Energy Efficiency Guide for iOS Apps
apple_id: TP40015243
resource_type: Guide
platform: watchOS|iOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/index.html
archived_at: '2026-07-18T01:48:34.497313Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)



## Energy Efficiency and the User Experience

All apps consume energy—whenever they perform networking operations, update the user interface, or run code on the CPU. As users rely increasingly on battery power—and as apps proliferate—energy efficiency becomes integral to the user experience.

A great user experience requires:

![image: ../Art/long_battery_life_64w_2x.png](attachments/Art/long_battery_life_64w_2x.png)

__Great battery life.__ As energy efficiency goes down, so does battery life. Users expect all-day battery life on their iOS devices.

![image: ../Art/great_performance_64w_2x.png](attachments/Art/great_performance_64w_2x.png)

__Awesome speed.__ iOS is designed to provide great performance during complex operations—and to make your app fly.

![image: ../Art/responsiveness_64w_2x.png](attachments/Art/responsiveness_64w_2x.png)

__Responsiveness.__ Too many resources being consumed at once can result in a laggy interface that’s slow to respond to user input.

![image: ../Art/low_heat_64w_2x.png](attachments/Art/low_heat_64w_2x.png)

__Cool device.__ As more apps use more resources, the system works harder and faster, and the physical temperature of a device gradually rises. When this occurs, the system takes steps to cool down to a more acceptable level.

### iOS Energy-Saving Technologies

iOS employs advanced energy-saving technologies that help users get the most out of their devices. These features help the system make smart decisions about how to use resources and run code as efficiently as possible.

### Integrated Hardware and Software

iOS integrates with advanced hardware features such as a power efficient CPU, accelerated graphics, and wireless antennas. Hardware and software work together to deliver an optimized user experience that’s great for battery life.

### Intelligent App Management

iOS apps have a life cycle that’s managed by the system. When a user finishes interacting with an app, the app is placed into a background state, where activity is throttled and the app may be suspended. Apps generating high CPU usage for extended periods of time while running in the background may be terminated by the system, if necessary.

### Network Operation Deferral

APIs let you designate criteria that indicate when and how often a network operation should be deferred, how long it can be deferred, and under what circumstances. The system uses this information to defer the operation until an energy efficient time.

### Task Prioritization

Tasks that affect the user, such as downloading and playing music, take priority over background and discretionary work. Quality of service class APIs allow you to assign priority levels to the work your app performs, giving you fine-grained control over task prioritization.

### Developer Tools

Xcode and Instruments help you identify and address energy problems as you develop your app, rather than after those problems are encountered by users.

### Your Obligation as a Developer

Even small inefficiencies in apps add up, significantly affecting battery life, performance, and responsiveness. As an app developer, you have an obligation to make sure your app runs as efficiently as possible. Use recommended APIs so the system can make smart decisions about how best to manage your app and the resources it uses. Whenever possible, batch and reduce network operations, and avoid unnecessary updates to the user interface. Power-intensive operations should be under the user’s control. If a user is playing a graphics-heavy game, for example, the user should not be surprised if the activity consumes power. Strive to make your app absolutely idle when it is not responding to user input.

By adhering to recommended guidelines, you can make big contributions to the overall energy efficiency of the platform and the satisfaction of your users.

[Fundamental Concepts](FundamentalConcepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqnbnknltc)
