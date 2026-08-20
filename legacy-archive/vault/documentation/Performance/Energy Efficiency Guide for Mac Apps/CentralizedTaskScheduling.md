---
title: Energy Efficiency Guide for Mac Apps
apple_id: TP40013929
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/CentralizedTaskScheduling.html
archived_at: '2026-07-18T01:49:43.290352Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for Mac Apps](index.md)



## Defer Tasks with XPC Activity

The XPC Activity API is a C-level interface that can be used to request centralized scheduling of discretionary tasks in your app. XPC Activity is part of XPC (see _[activity.h Reference](https://developer.apple.com/documentation/xpc/activity.h)_ in _[XPC Services API Reference](https://developer.apple.com/documentation/xpc)_), a low-level interprocess communication mechanism in OS X.

Use the XPC Activity API to tell the system when you have work that can be deferred, how long it can be deferred, and whether it should be deferred until the computer is plugged into power.

Whenever possible, especially when your users are on battery power, defer execution of low priority discretionary tasks such as:

- Cleaning up temporary files
- Syncing data
- Indexing document content
- Checking for updated versions of your software (if your app is not distributed through the Mac App Store)
- Downloading updates (if your app is not distributed through the Mac App Store)

For detailed information about XPC Services, refer to _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_.

### XPC Activity Constants

To use the XPC Activity API, you register with XPC and provide a dictionary that specifies a set of activity properties. The following properties are especially useful for scheduling discretionary tasks:

- [XPC_ACTIVITY_ALLOW_BATTERY](https://developer.apple.com/documentation/xpc/xpc_activity_allow_battery). Boolean value indicating whether the activity should be allowed to run while the computer is on battery power.

  `XPC_ACTIVITY_ALLOW_BATTERY` defaults to `YES``true` for utility-level activities and `NO``false` for maintenance-level activities, but the constant can be overridden in either case.
- [XPC_ACTIVITY_DELAY](https://developer.apple.com/documentation/xpc/xpc_activity_delay). The number of seconds to delay before beginning the activity.
- [XPC_ACTIVITY_GRACE_PERIOD](https://developer.apple.com/documentation/xpc/xpc_activity_grace_period). The number of seconds to allow as a grace period before the scheduling of the activity becomes more aggressive.
- [XPC_ACTIVITY_REPEATING](https://developer.apple.com/documentation/xpc/xpc_activity_repeating). Boolean value indicating whether the activity should be automatically rescheduled after it completes.
- [XPC_ACTIVITY_INTERVAL](https://developer.apple.com/documentation/xpc/xpc_activity_interval). The number of seconds between repeating or delayed intervals.
- [XPC_ACTIVITY_PRIORITY_MAINTENANCE](https://developer.apple.com/documentation/xpc/xpc_activity_priority_maintenance). Maintenance-level priority. Maintenance priority is intended for user-invisible maintenance tasks such as garbage collection or optimization.
- [XPC_ACTIVITY_PRIORITY_UTILITY](https://developer.apple.com/documentation/xpc/xpc_activity_priority_utility). Utility-level priority. Utility priority is intended for user-visible tasks such as fetching data from the network, copying files, or importing data.

For a complete list of properties, see Global Constants in _[activity.h Reference](https://developer.apple.com/documentation/xpc/activity.h)_.

### Example of Simple XPC Activity Use

The code in Listing 14-1 defines and registers an XPC dictionary specifying a discretionary maintenance activity that can be delayed from 1 to 12 hours. Based on this dictionary, XPC runs the block of code that performs the activity in its own queue at an appropriate time that doesn’t interfere with the user’s battery life.

__Listing 14-1__Allowing a discretionary activity to be deferred for 12 hours

Objective-C

1. `// Create an empty XPC dictionary`
2. `xpc_object_t criteria = xpc_dictionary_create(NULL, NULL, 0);`
4. `// Tell XPC that this is a non-repeating activity`
5. `xpc_dictionary_set_bool(criteria, XPC_ACTIVITY_REPEATING, FALSE);`
7. `// The activity should start in 1 hour (3600 seconds)`
8. `xpc_dictionary_set_int64(criteria, XPC_ACTIVITY_DELAY, XPC_ACTIVITY_INTERVAL_1_HOUR);`
10. `// Allow XPC to defer the activity by as much as 12 hours`
11. `xpc_dictionary_set_int64(criteria, XPC_ACTIVITY_GRACE_PERIOD, 12 * XPC_ACTIVITY_INTERVAL_1_HOUR);`
13. `// Indicate that this is a user-invisible activity`
14. `xpc_dictionary_set_string(criteria,XPC_ACTIVITY_PRIORITY, XPC_ACTIVITY_PRIORITY_MAINTENANCE);`
16. `// Register the new XPC dictionary and pass it the handler block that performs the activity`
17. `xpc_activity_register("com.myapp.MySimpleActivity", criteria, ^(xpc_activity_t activity)`
18. `{`
19. `/* do background or deferred work here */`
20. `}`
21. `);`

Swift

1. `import XPC`
3. `// Create an empty XPC dictionary`
4. `var criteria = xpc_dictionary_create(nil, nil, 0)`
6. `// Tell XPC that this is a non-repeating activity`
7. `xpc_dictionary_set_bool(criteria, XPC_ACTIVITY_REPEATING, false)`
9. `// The activity should start in 1 hour (3600 seconds)`
10. `xpc_dictionary_set_int64(criteria, XPC_ACTIVITY_DELAY, XPC_ACTIVITY_INTERVAL_1_HOUR)`
12. `// Allow XPC to defer the activity by as much as 12 hours`
13. `xpc_dictionary_set_int64(criteria, XPC_ACTIVITY_GRACE_PERIOD, 12 * XPC_ACTIVITY_INTERVAL_1_HOUR)`
15. `// Indicate that this is a user-invisible activity`
16. `xpc_dictionary_set_string(criteria, XPC_ACTIVITY_PRIORITY, XPC_ACTIVITY_PRIORITY_MAINTENANCE)`
18. `// Register the new XPC dictionary and pass it the handler block that performs the activity`
19. `xpc_activity_register("com.myapp.MySimpleActivity", criteria) { (activity)`
20. `/* do background or deferred work here */`
21. `}`
22. `)`

### XPC Activity State

XPC activities also possess a state attribute, which allows them to keep running after the activity’s handler block has returned.

Your app can check the current activity state by calling [xpc_activity_get_state](https://developer.apple.com/documentation/xpc/1495816-xpc_activity_get_state), and it can set the current activity state by calling [xpc_activity_set_state](https://developer.apple.com/documentation/xpc/1495820-xpc_activity_set_state). XPC activities support the following states:

- [XPC_ACTIVITY_STATE_CHECK_IN](https://developer.apple.com/documentation/xpc/1495796-xpc_activity_state_t/xpc_activity_state_check_in). An optional state indicating that the activity has just completed a checkin with the system after `XPC_ACTIVITY_CHECK_IN` was provided as the criteria parameter to [xpc_activity_register](https://developer.apple.com/documentation/xpc/1495824-xpc_activity_register). The state gives the app an opportunity to inspect and modify the activity's criteria.
- [XPC_ACTIVITY_STATE_WAIT](https://developer.apple.com/documentation/xpc/1495796-xpc_activity_state_t/xpc_activity_state_wait). The activity is waiting for an opportunity to run. This value is never returned within the activity's handler block, as the block is invoked in response to `XPC_ACTIVITY_STATE_CHECK_IN` or `XPC_ACTIVITY_STATE_RUN`.
- [XPC_ACTIVITY_STATE_RUN](https://developer.apple.com/documentation/xpc/xpc_activity_state_run). The activity is eligible to run based on its criteria. Your app shouldn’t attempt to set this state, as it occurs automatically.
- [XPC_ACTIVITY_STATE_DEFER](https://developer.apple.com/documentation/xpc/xpc_activity_state_defer). The activity should be deferred (placed back into the `XPC_ACTIVITY_STATE_WAIT` state) until a time when its criteria are met again.
- [XPC_ACTIVITY_STATE_CONTINUE](https://developer.apple.com/documentation/xpc/1495796-xpc_activity_state_t/xpc_activity_state_continue). The activity will continue its operation beyond the return of its handler block. This state can be used to extend an activity to include asynchronous operations. The activity's handler block will not be invoked again until the state has been updated to either `XPC_ACTIVITY_STATE_DEFER` or, in the case of repeating activity, `XPC_ACTIVITY_STATE_DONE`.
- [XPC_ACTIVITY_STATE_DONE](https://developer.apple.com/documentation/xpc/xpc_activity_state_done). The activity has completed. For non-repeating activity, the resources associated with the activity will be automatically released upon return from the handler block. For repeating activity, timers present in the activity's criteria will be reset. Your app shouldn’t attempt to set this state, as it occurs automatically.

[Schedule Background Networking](SchedulingNetworkActivity.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmztfvjvomi)

[Observe Signs of Energy Leaks](SignsofEnergyLeaks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmrsfvjvomi)
