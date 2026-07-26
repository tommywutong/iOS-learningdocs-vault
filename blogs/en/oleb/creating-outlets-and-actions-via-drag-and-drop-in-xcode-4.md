---
title: Creating Outlets and Actions Via Drag and Drop in Xcode 4
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/06/creating-outlets-and-actions-via-drag-and-drop-in-xcode-4/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:59e6974ef6d42407'
translated: false
---

> 原文：[Creating Outlets and Actions Via Drag and Drop in Xcode 4](https://oleb.net/blog/2011/06/creating-outlets-and-actions-via-drag-and-drop-in-xcode-4/)　·　Ole Begemann

# Creating Outlets and Actions Via Drag and Drop in Xcode 4

One of the coolest new features in Xcode 4 is the ability to generate code for Interface Builder outlets and actions using drag and drop. What involved up to five separate manual code changes before can now be done with one drag and drop operation. Let’s see how it works in practice.

# Video: Creating Outlets and Actions via Drag and Drop

I recorded a short video to demonstrate the process (no sound):

<sub>[Download the video](https://oleb.net/media/xcode4-drag-and-drop.mp4) (H.264, 34 MB).</sub>

# Step by Step Guide

1. Open the .xib file that contains the view or control for which you want to create a new outlet or action.
2. Open the corresponding header file. You can either use Xcode’s Assistant Editor (Option + Command + Return) to display the .xib and .h files side by side or open the .h file in a separate window.
3. Pick the control in your user interface for which you want to create an outlet or action method. Hold down the Control key and drag (or right-click-and-drag) from the control in question over into your class `@interface`. Let the mouse button go when Xcode indicates a successful drag with a horizontal line.

  ![Dragging from Interface Builder directly into the code in Xcode 4](https://oleb.net/media/xcode4-creating-outlet-drag-and-drop-1.png)
4. In the window that pops up, choose whether you want to create an outlet or an action. Give it a name and optionally modify the other parameters. Click Connect when you’re finished.

  ![Popup window in Xcode 4 when creating an outlet via drag and drop](https://oleb.net/media/xcode4-creating-outlet-drag-and-drop-2.png)
5. If you chose to create an outlet, Xcode will declare a `@property` and a corresponding instance variable in your class’s interface.[1](#fn:1) If you check the implementation file, you will see that Xcode added not only the necessary `@synthesize` statement but also releases the ivar in your class’s `-dealloc` method. If the class is a `UIViewController`, Xcode is even smart enough to know about the memory management requirements and sets the outlet to `nil` in the controller’s `-viewDidUnload` method.

  Feel free to manually remove the ivar from your `@interface` as it is no longer required. The compiler can now generate an ivar for any synthesized property automatically.
6. If you chose to create an action, Xcode will declare a `-(IBAction)myAction:(id)sender;` method in your class’s interface and insert an empty method body at the bottom of your class’s `@implementation` section.

# Caveats

As easy as it is to create the connections, as cumbersome is it to undo them. If you recognize immediately after clicking the Connect button that you made a mistake, the Undo command can help. Undo works on a per-file basis in Xcode, so make sure to undo the changes in all three locations: the .h and .m files and the .xib file.

If you want to remove a connection at a later time, you have to delete the generated code manually. Do not forget to also remove the connection in the .xib file or your app will crash: control-click the control in question and click the x in front of the outlet or action that you want to delete.

1. I have not yet identified the system behind Xcode’s naming strategy for the instance variable. It seems that by default the ivar’s name is identical to the name of the property. If, however, there is an existing property whose corresponding ivar starts with an underscore, Xcode sometimes seems to pick up this popular naming scheme and henceforth generates ivars with leading underscores in this file (connecting them to their property via the `@synthesize xyz = _xyz;` statement). I have not been able to make this work reliably, though. [↩︎](#fnref:1)
