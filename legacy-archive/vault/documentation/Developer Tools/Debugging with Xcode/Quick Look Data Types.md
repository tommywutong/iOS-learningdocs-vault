---
title: Debugging with Xcode
apple_id: TP40015022
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/debugging_with_xcode/chapters/quick_look_data_types.html
archived_at: '2026-07-27T06:57:09.380048Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with Xcode](About%20Debugging%20with%20Xcode.md)


[Next](Appendix-%20The%20Static%20Analyzer.md)[Previous](Specialized%20Debugging%20Workflows.md)

# Quick Look Data Types

The Xcode debugger includes the variables Quick Look feature, a way to view the current state of object variables in your app by displaying their contents graphically in a pop-up display, either by clicking the Quick Look button in the debugger variables view or by pressing the Space bar with a variable selected.

（原归档配图获取待重试：`dwx-ql-qlbuttons_2x.png`）

Not all operating system object types can present quick looks, but many can. The following table lists common object types provided by the operating system that support Quick Look:

| Class Category | Object Type |
| --- | --- |
| Image classes | - `NSImage` - `UIImage` - `NSImageView` - `UIImageView` - `CIImage` - `NSBitmapImageRep` |
| Cursor class | - `NSCursor` |
| Color classes | - `NSColor` - `UIColor` |
| BezierPath classes | - `NSBezierPath` - `UIBezierPath` |
| Location classes | - `CLLocation` |
| View classes | - `NSView` - `UIView` |
| String class | - `NSString` |
| Attributed string class | - `NSAttributedString` |
| Data class | - `NSData` |
| URL class | - `NSURL` |
| SpriteKit classes | - `SKSpriteNode` - `SKShapeNode` - `SKTexture` - `SKTextureAtlas` |

You can always try the Quick Look feature if the object type isn’t in this list. If Quick Look isn’t available for the object type you’ve selected, Xcode shows the default Quick Look display for that object.

（原归档配图未能恢复：`dwx-ql-default_2x.png`）

You can extend Quick Look for use with custom object types by adding a rendering method to the object class. See _[Quick Look for Custom Types in the Xcode Debugger](../../IDEs/Quick%20Look%20for%20Custom%20Types%20in%20the%20Xcode%20Debugger/About%20Variables%20Quick%20Look%20for%20Custom%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dambr)_to learn how to implement Quick Look in your custom object classes.

[Next](Appendix-%20The%20Static%20Analyzer.md)[Previous](Specialized%20Debugging%20Workflows.md)
