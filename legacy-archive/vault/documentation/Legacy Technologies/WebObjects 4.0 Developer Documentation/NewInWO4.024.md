---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.024.html
archived_at: '2026-07-15T07:58:33.898063Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.023.md)

## WODirectAction Class

The main purpose of WODirectAction is to act as a repository for action methods. WODirectAction also defines these methods, which you can use in your actions:

|  WODirectAction |  |
|  Method |  Description |
|  initWithRequest: (Objective-C)  WODirectAction (Java) |  Subclasses must override to provide any additional initialization. |
|  request |  Returns the WORequest object that initiated the action. |
|  session |  Returns the current session. If there is no session, which is a possibility if the application is written entirely with direct actions, this method creates a new session before returning it. |
|  existingSession |  Attempts to restore and then return the session based upon the request. If the request didn't have a session ID or the session ID referred to a non-existent session, this method returns __nil__ (__null__ in Java). |
|  pageWithName: |  Creates and returns an instance of WOComponent with the specified name. |
|  takeFormValuesforKeyArray: |  Extracts input values from the request URL and assigns them to the WODirectAction instance using __takeValue:forKey:__. The argument is an NSArray of keys. |
|  takeFormValuesForKeys: (Objective-C only) |  Extracts input values from the request URL. The argument is a comma-separated list of NSStrings. |
|  takeFormValueArraysForKeyArray: |  Extracts input values from the request URL where the values are arrays. The argument is an NSArray of keys. |
|  takeFormValueArraysForKeys: (Objective-C only) |  Extracts input values from the request URL where the values are arrays. The argument is a comma-separated list of NSStrings. |
|  performActionNamed: |  Performs the action with the specified name and returns the result of that action. |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.025.md)
