---
title: HomeKit Developer Guide
apple_id: TP40015050
resource_type: Guide
platform: watchOS|iOS
topic: null
technology: HomeKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/HomeKitDeveloperGuide/CreatingActionSetsandScenes/CreatingActionSetsandScenes.html
archived_at: '2026-07-27T06:57:09.470811Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HomeKit Developer Guide](Introduction%20to%20HomeKit.md)


[Next](Managing%20Users.md)[Previous](Testing%20Your%20HomeKit%20App.md)

# Creating Action Sets and Triggers

An action set ([HMActionSet](https://developer.apple.com/documentation/homekit/hmactionset)) and a trigger ([HMTimerTrigger](https://developer.apple.com/documentation/homekit/hmtimertrigger)) allow you to control many accessories at once. For example, an action set might execute a set of actions ([HMAction](https://developer.apple.com/documentation/homekit/hmaction)) just before the user goes to bed. A write action writes a value to a characteristic. The actions in an action set execute in an undefined order. A trigger executes an action set at a given date and can repeat. Action sets have unique names within a home and are recognized by Siri.

（原归档配图获取待重试：`actionsets_2x.png`）

## Creating Write Actions

Write actions write the values of characteristics of a service and are added to action sets. The [HMAction](https://developer.apple.com/documentation/homekit/hmaction) class is an abstract superclass for the [HMCharacteristicWriteAction](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction) concrete subclass. An action has an associated characteristic object, so you access a service object and its characteristics, as described in [Accessing Services and Characteristics](Accessing%20Services%20and%20Characteristics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tanjqfvbuqnrnknltc), to create an associated [HMCharacteristicWriteAction](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction) object.

To create a write action, use the [initWithCharacteristic:targetValue:](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction/1621976-initwithcharacteristic) initialization method in the [HMCharacteristicWriteAction](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction) class.

```
HMCharacteristicWriteAction *action = [[HMCharacteristicWriteAction alloc] initWithCharacteristic:characteristic targetValue:value];
```

In your code, replace the `value` parameter with the value you want to write, depending on the possible values for the characteristic, and replace `characteristic` with the [HMCharacteristic](https://developer.apple.com/documentation/homekit/hmcharacteristic) object that represents the characteristic you want to change.

## Creating and Executing Action Sets

An action set is a collection of actions that are executed together; for example, a nighttime action set might include actions to turn off lights, turn the temperature down, and lock doors.

To create an action set, use the [addActionSetWithName:completionHandler:](https://developer.apple.com/documentation/homekit/hmhome/1620231-addactionsetwithname) asynchronous method.

```
[self.home addActionSetWithName:@"NightTime" completionHandler:^(HMActionSet *actionSet, NSError *error) {
    if (error == nil) {
        // Successfully added an action set
    } else {
        // Unable to add an action set
    }
}];
```

To add an action to an action set, use the [addAction:completionHandler:](https://developer.apple.com/documentation/homekit/hmactionset/1616798-addaction) asynchronous method.

```
[actionSet addAction:action completionHandler:^(NSError *error) {
    if (error == nil) {
        // Successfully added an action to an action set
    } else {
        // Unable to add an action to an action set
    }
}];
```

To remove an action, use the [removeAction:completionHandler:](https://developer.apple.com/documentation/homekit/hmactionset/1616787-removeaction) method.

To execute an action set, use the [executeActionSet:completionHandler:](https://developer.apple.com/documentation/homekit/hmhome/1620256-executeactionset) method in the [HMHome](https://developer.apple.com/documentation/homekit/hmhome) class. For example, the user wants to control all holiday lights. You create one action set for turning all holiday lights on and another action set for turning all holiday lights off. To turn the holiday lights on, send the [executeActionSet:completionHandler:](https://developer.apple.com/documentation/homekit/hmhome/1620256-executeactionset) message to the home object passing the “holiday lights on” action set.

## Creating and Enabling Timer Triggers

Triggers execute one or more action sets. iOS manages and executes triggers for you in the background. The [HMTrigger](https://developer.apple.com/documentation/homekit/hmtrigger) class is an abstract superclass for the [HMTimerTrigger](https://developer.apple.com/documentation/homekit/hmtimertrigger) concrete subclass. When you create a timer trigger, you specify the fire date and optional recurrence information. Creating and enabling a timer trigger is a multistep process.

__To create and enable a timer trigger__

1. Create a timer trigger.

   ```
   self.trigger = [[HMTimerTrigger alloc] initWithName:name
         fireDate:fireDate
         timeZone:nil
         recurrence:nil
         recurrenceCalendar:nil];
   ```

   The fire date must be in the future, and the seconds value must be zero. If you specify a recurrence, the minimum interval is five minutes and the maximum interval is five weeks. To specify a recurrence using the [NSDateComponents](https://developer.apple.com/documentation/foundation/nsdatecomponents) and [NSCalendar](https://developer.apple.com/documentation/foundation/nscalendar) parameters, read _[Date and Time Programming Guide](../../Cocoa/Date%20and%20Time%20Programming%20Guide/About%20Dates%20and%20Times.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazts2i)_.
2. Add action sets to the trigger.

   Use the [HMTrigger](https://developer.apple.com/documentation/homekit/hmtrigger) superclass method, [addActionSet:completionHandler:](https://developer.apple.com/documentation/homekit/hmtrigger/1620716-addactionset), to add an action set to a trigger.
3. Add the trigger to a home.

   Use the [addTrigger:completionHandler:](https://developer.apple.com/documentation/homekit/hmhome/1620271-addtrigger) method in the `HMHome` class to add a trigger to a home.
4. Enable the trigger.

   Newly created trigger objects are disabled by default. Use the [enable:completionHandler:](https://developer.apple.com/documentation/homekit/hmtrigger/1620714-enable) method to enable a trigger.

An enabled timer trigger will execute its action sets at the next fire date.

[Next](Managing%20Users.md)[Previous](Testing%20Your%20HomeKit%20App.md)
