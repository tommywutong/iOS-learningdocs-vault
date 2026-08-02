---
title: Move off AudioUnitRemovePropertyListener and the Component Manager on Mac OS
  X 10.6 and greater
apple_id: DTS40009697
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2010-03-15'
source_url: https://developer.apple.com/library/archive/qa/qa1645/_index.html
archived_at: '2026-07-18T02:33:14.438860Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1645

# Move off AudioUnitRemovePropertyListener and the Component Manager on Mac OS X 10.6 and greater

## Q:  My application is still using AudioUnitRemovePropertyListener and the Component Manager when using Audio Units. For Mac OS X 10.6 what APIs should I move to?

A: My application is still using AudioUnitRemovePropertyListener and the Component Manager when using Audio Units. For Mac OS X 10.6 what APIs should I move to?

Traditionally, the Component Manager has been used for the registration, discovery and packaging of Audio Units. However, this may not always be the case and in order to provide an API that will be supported on Mac OS X 10.6, iPhone 2.0 and greater operating systems, applications using audio units should move from the old Component Manager APIs to the Audio Component APIs (located in `AudioUnitFramework/AudioComponent.h`) to find and open audio units.

When an application moves to using the Audio Component API on Mac OS X 10.6, it must also no longer call `AudioUnitRemovePropertyListener` (deprecated in Mac OS X 10.5) as it is not supported and will fail.

Applications should replace all calls to `AudioUnitRemovePropertyListener` with `AudioUnitRemovePropertyListenerWithUserData`. This updated API pairs with `AudioUnitAddPropertyListener` allowing applications to use the same `AudioUnitPropertyListenerProc` more than once.

When calling `AudioUnitRemovePropertyListenerWithUserData` the application should provide the same function pointer and user data provided when the listener was added with `AudioUnitAddPropertyListener`.

From `AudioUnitFramework/AUComponent.h` Mac OS X 10.6 SDK.


```
/*!     @function       AudioUnitAddPropertyListener     @abstract       registration call to receive notifications for when a property changes     @discussion     When an audio unit property value changes, a notification callback can be called by the                     audio unit to  inform interested parties that this event has occurred. The notification is                     defined by the tuple of inProc and inProcUserData as paired to the specified property ID,                     so the previously defined AudioUnitRemovePropertyListener is dperecated because it didn't                     allow for the provision of the inProcUserData to remove a given listener (so, you should                     use AudioUnitRemovePropertyListenerWithUserData).      @param          inUnit                     the audio unit     @param          inID                     the proeprty identifier     @param          inProc                     the proceedure to call when the property changes (on any scope or element)     @param          inProcUserData                     the user data to provide with the callback      @result         noErr, or various audio unit errors related to properties */ extern OSStatus AudioUnitAddPropertyListener(AudioUnit                     inUnit,                              AudioUnitPropertyID           inID,                              AudioUnitPropertyListenerProc inProc,                              void *                        inProcUserData)                              __OSX_AVAILABLE_STARTING(__MAC_10_0,__IPHONE_2_0);  /*!     @function       AudioUnitRemovePropertyListenerWithUserData     @abstract       remove a previously registered property listener     @discussion     Removes a previously registered property listener as specified by the inProc and                      inProcUser data as paired to the property identifier      @param          inUnit                     the audio unit     @param          inID                     the proeprty identifier     @param          inProc                     the proceedure previously registered     @param          inProcUserData                     the user data paired with the provided inProc      @result         noErr, or various audio unit errors related to properties */ extern OSStatus AudioUnitRemovePropertyListenerWithUserData(AudioUnit                     inUnit,                                             AudioUnitPropertyID           inID,                                             AudioUnitPropertyListenerProc inProc,                                             void *                        inProcUserData)                                             __OSX_AVAILABLE_STARTING(__MAC_10_5,__IPHONE_2_0);
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-03-15 | New document that reminds developers to move off the deprecated AudioUnitRemovePropertyListener API and to use the Audio Component APIs when finding and opening audio units. |

