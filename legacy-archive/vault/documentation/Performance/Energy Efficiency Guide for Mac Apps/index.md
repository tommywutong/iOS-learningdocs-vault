---
title: Energy Efficiency Guide for Mac Apps
apple_id: TP40013929
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/index.html
archived_at: '2026-07-18T01:50:31.596485Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)



## Energy Efficiency and the User Experience

All apps consume energy—whenever they update the user interface, perform networking operations, write to disk, or run code on the CPU. As users rely increasingly on battery power—and as apps proliferate—energy efficiency becomes integral to the user experience.

A great user experience requires:

![image: ../Art/long_battery_life_64w_2x.png](attachments/Art/long_battery_life_64w_2x.png)

__Great battery life.__ As energy efficiency goes down, so does battery life. Users want all-day battery life on their portable devices.

![image: ../Art/great_performance_64w_2x.png](attachments/Art/great_performance_64w_2x.png)

__Awesome speed.__ OS X is designed to provide great performance during complex operations—and to make your app fly.

![image: ../Art/responsiveness_64w_2x.png](attachments/Art/responsiveness_64w_2x.png)

__Responsiveness.__ Too many resources being consumed at once can result in a laggy interface that’s slow to respond to user input.

![image: ../Art/low_heat_64w_2x.png](attachments/Art/low_heat_64w_2x.png)

__Cool, quiet system.__ As more apps use more resources, the system works harder and faster, and the physical temperature of a device gradually rises. When this occurs, the system takes steps to cool down to a more acceptable level. On devices with fans, those fans may become active and audible to the user.

### OS X Energy-Saving Technologies

OS X employs advanced energy-saving technologies that help users get the most out of their Macs. These features help the system make smart decisions about how to utilize resources and run code as efficiently as possible.

### Centralized Task Scheduling and Grand Central Dispatch

Intensive background operations, such as software updates or file backups, may be unavoidable. Centralized Task Scheduling (CTS) and Grand Central Dispatch (GCD) APIs let you designate criteria that indicate when and how often a task should be deferred, how long it can be deferred, and under what circumstances. The system then makes an intelligent decision about when to perform the task based on the specified criteria.

### Quality of Service Levels

Tasks that affect the user, such as downloading and playing music, take priority over background and discretionary work. Quality of service class APIs allow you to assign distinct priority levels to the work your app performs, giving you fine grained control over task prioritization.

### Event-Based APIs and Services

Timers deliver events, or fire, at prescribed time intervals. If a timer fires when the system is idle, the CPU and numerous other systems are awakened from their low-power states. Yet many of these systems aren’t always needed to perform the work invoked by the timer. If the work can be performed when the system hardware is already running, the additional cost is not incurred and the CPU can remain idle longer. OS X provides services and APIs that efficiently deliver events without unnecessarily waking the CPU.

### App Nap

When your app isn’t busy performing user-initiated work, the system may put your app in App Nap. App Nap conserves energy by regulating your app’s CPU usage, I/O, and timers. As soon as the user resumes interacting with your app, OS X switches it back to full speed. Transitions are so seamless that the user thinks your app has been running at full speed all along. You can enhance App Nap by implementing notifications that tell your app when it becomes inactive, so it can immediately start reducing activity.

### Battery Menu, Activity Monitor, and Developer Tools

The Battery Status menu and Activity Monitor let you quickly identify apps that are using significant amounts of energy in OS X. Xcode, Instruments, and numerous command-line tools help you identify and address energy problems as you develop your app, rather than after those problems are encountered by users.

### Your Obligation as a Developer

Even small inefficiencies in apps add up across the system, significantly affecting battery life, performance, responsiveness, and temperature. As an app developer, you have an obligation to make sure your app runs as efficiently as possible. Use recommended APIs so the system can make smart decisions about how best to manage your app and the resources it uses. Whenever possible, avoid unnecessary updates to the user interface and I/O. Power-intensive operations should be under the user’s control. If a user initiates a large iMovie render, Automator batch job, Compressor conversion, or Xcode compile, for example, the user should not be surprised if the activity consumes power. Strive to make your app absolutely idle when it is not responding to user input.

By adhering to recommended guidelines, you can make big contributions to the overall energy efficiency of the platform and the satisfaction of your users.

[Fundamental Concepts](FundamentalConcepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqobnknltc)
