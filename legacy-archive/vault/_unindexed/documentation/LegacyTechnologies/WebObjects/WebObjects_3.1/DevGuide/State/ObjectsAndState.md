---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/ObjectsAndState.html
archived_at: '2026-07-15T07:47:46.895862Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](WhenStore.md)

# Objects and State

WebObjects defines three classes that manage state in an application---WOApplication, WOSession, and WOComponent. (Note: In Java these classes are known as WebApplication, WebSession, and Component.) An application object handles state associated with the application as a whole, session objects handle state associated with a particular user session within the application, and component objects handle state associated with a particular page or component within a session:

!

__Figure 1.__  Application, Sessions, and Components

Keep in mind as you read about these classes and about their participation in the request-response loop that the behaviors described are the default ones. Since these classes are public, you are free to change or augment their behaviors either by overriding their methods in scripts, by adding methods through categories, or by creating and using subclasses in their place.

[!Table of Contents](ManagingState.book.md)
[!Next Section](AppObjAndState.md)
