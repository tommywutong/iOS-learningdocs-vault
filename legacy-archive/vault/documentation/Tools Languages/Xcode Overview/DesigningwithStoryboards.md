---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/DesigningwithStoryboards.html
archived_at: '2026-07-27T06:57:08.002589Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](ConnectingObjectstoCode.md)[Previous](UsingInterfaceBuilder.md)

## Designing with Storyboards

You use a storyboard to graphically lay out the user’s path through your iOS, watchOS, or OS X app. Use Interface Builder to specify your user interface in terms of:

- Scenes
- Segues between scenes
- Controls used to trigger the segues

A __scene__ represents an onscreen content area. On iPhone and iPod touch, a screen generally contains a single scene. On iPad and Mac, a screen can be composed of more than one scene. A __segue__ represents the transition from one scene to the next scene, such as when one scene slides over another. You can also create segues between storyboards, enabling you to break up your interface into related scenes.

The screenshot shows a storyboard for a master-detail pattern in an iOS project. This storyboard contains three scenes and two segues. The leftmost scene represents a navigation controller, which manages user navigation between the master and detail scenes. When working from this template, add additional scenes as necessary by dragging view controllers from the Object library to the canvas and configuring the view controller with the Identity inspector (（原归档配图未能恢复：`IB_H_inspector_identity_button_2x.png`）). Drag objects from the Object library to lay out each scene. Configure the objects and the segues with the Attributes inspector (（原归档配图获取待重试：`IB_H_inspector_attributes_button_2x.png`）).

（原归档配图未能恢复：`interface_builder-storyboard_2x.png`）

Your master scene might, for example, contain a table listing multiple items. Each item in the master scene has a corresponding detail scene that provides additional information about the item. The navigation controller provides the Back button that returns the user to the master scene from all detail scenes.

（原归档配图获取待重试：`MasterDetailViews_2x.png`）

For more information about storyboards, see [Xcode Help](https://help.apple.com/xcode).

[Using Interface Builder](UsingInterfaceBuilder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnbsfvjvomi)

[Connecting Objects to Code](ConnectingObjectstoCode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnbufvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](ConnectingObjectstoCode.md)[Previous](UsingInterfaceBuilder.md)
