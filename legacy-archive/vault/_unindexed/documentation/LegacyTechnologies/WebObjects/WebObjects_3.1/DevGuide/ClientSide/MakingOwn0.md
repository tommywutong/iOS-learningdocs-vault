---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/ClientSide/MakingOwn0.html
archived_at: '2026-07-15T07:46:39.241415Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ClientSideComponents.mif.md)
[!Previous Section](Integrating4.md)

# Making Your Own Java Client-Side Components

If none of the applets in __next.wo.client.controls__ meets your needs, you can write your own applet and implement the associative behavior that is necessary to make the applet a WebObjects client-side component. You can also turn acquired applets into client-side components. The strategies you may adopt differ for applets for which you have source code and those for which you don't.

If you have the source code for an applet, you will probably want to modify it so that it implements the SimpleAssociationDestination interface. Applets that implement this interface can use the SimpleAssociation class (a subclass of Assocation) to mediate the exchange of state and action information with the AppletGroupController and thus with the server. You are not required to take this course with applets for which you have the source; if you wish, you can create a subclass of Association and implement the mandatory methods (see "[Creating a Subclass of Association](AssocSubclass.md)"). However, applets that implement SimpleAssociationDestination do not require an Association subclass tailored for them. Instead they can use the generic SimpleAssociation class.

[!Table of Contents](ClientSideComponents.mif.md)
[!Next Section](ImplementingSAD.md)
