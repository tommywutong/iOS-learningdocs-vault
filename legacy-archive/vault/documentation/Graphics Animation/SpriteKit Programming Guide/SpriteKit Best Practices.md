---
title: SpriteKit Programming Guide
apple_id: TP40013043
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsAnimation/Conceptual/SpriteKit_PG/DesigningGameswithSpriteKit/DesigningGameswithSpriteKit.html
archived_at: '2026-07-15T07:35:15.954119Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [SpriteKit Programming Guide](About%20SpriteKit.md)


[Next](Document%20Revision%20History.md)[Previous](Simulating%20Physics.md)

# SpriteKit Best Practices

At this point, you already have a good idea of what SpriteKit can do and how it works. You know how to add nodes to scenes and perform actions on those nodes, and these tasks are the building blocks for creating gameplay. What you may be missing is the bigger picture. That is, you need an understanding of how to plan and develop games and tools using SpriteKit. To get the most out of SpriteKit, you need to know:

- How to organize your game into scenes and transitions
- When to subclass SpriteKit classes
- How to store your game’s data and art
- How to use build your own tools to create SpriteKit content and export that content for your game to use

SpriteKit provides more than just a graphics layer for your game; it also provides features that make it easy to integrate SpriteKit into your custom game tools. By integrating SpriteKit into your games tools, you can build your content in the tools and read it directly into your game engine. A data-driven design lets artists, game designers, and game programmers collaborate to build your game’s content.

Scenes are the fundamental building blocks for creating SpriteKit content. When you start a new game project, one of your tasks is to define which scenes are needed and when transitions occur between those scenes. Scenes usually represent modes of play or content that appears to the player. Usually, it is easy to see when you need a new scene; if your game needs to replace all of the content onscreen, use a transition to a new scene.

Designing your game’s scenes and the transitions between them is similar to the role of view controllers in a traditional iOS app. In an iOS app, content is implemented by view controllers. Each view controller creates a collection of views to draw that content. Initially, one view controller is presented by the window. Later, when the user interacts with the view controller’s views, it might trigger a transition to another view controller and its content. For example, selecting an item in a table view might bring up a detail view controller to display the contents of the selected item.

Scenes do not have a default behavior, like storyboards do in a traditional iOS app. Instead, you define and implement the behaviors for scenes. These behaviors include:

- When new scenes are created
- The contents of each scene
- When transitions occur between scenes
- The visual effect used to perform a transition
- How data is transferred from one scene to another

For example, you could implement a model similar to a segue, where a new scene is always instantiated on a transition. Or you could design your game engine to use scenes that it keeps around persistently. Each approach has its benefits:

- If a scene is instantiated every time a transition occurs, it is always created in a clean, known state. This means that you don’t have to worry about resetting any internal state of the scene, which can often have subtle bugs.
- If a scene is persistent, then you can transition back to the scene and have it be in the same state it was in when you left it. This design is useful in any kind of game where you need to quickly transition between multiple scenes of content.

Typically, a new scene is going to be developed in stages. At the start, you might be working with test apps and experimental ideas to understand how SpriteKit works. But later, as your game gets more sophisticated, your scenes need to adapt.

In test apps, and some simple games, all of your logic and code goes in the scene subclass. The scene manipulates the node tree and the contents of each node in the tree, running actions or changing other behaviors as necessary. The project is simple enough that all of the code can live in a single class.

The second stage of a project usually happens when the rendering or game logic starts getting longer or more complex. At this stage, you usually start breaking out specific behaviors and implementing them in other classes. For example, if your game includes the concept of a camera, you might create a `CameraNode` class to encapsulate the camera behavior. You might then create other node classes to encapsulate other behaviors. For example, you might create separate node classes to represent units in your game.

In the most sophisticated projects, artificial intelligence and other concepts become more important. In these designs, you may end up creating classes that work independently of SpriteKit. Objects of these classes perform work on behalf of the scene, but are not specifically tied to it. These classes are usually extracted from your SpriteKit subclasses when you realize that many of your methods are implementing game logic without really touching any SpriteKit content.

When SpriteKit renders a frame, it culls all of the nodes that are not visible on screen. In theory, this means you could simply keep all of your content to the scene, and let SpriteKit do all the work to manage it. For games with modest rendering requirements, this design would be adequate. But as your game gets larger and more sophisticated, you need to do more work to ensure good performance from SpriteKit.

Typically, a node needs to be part of the node tree because:

- It has a reasonably good chance of being rendered in the near future.
- The node runs actions that are required for accurate gameplay.
- The node has a physics body that is required for accurate gameplay.

When a node does not meet any of these requirements, it is usually better to remove it from the tree, particularly if it has many children of its own. For example, emitter nodes often provide special effects without impacting gameplay at all, and they emit a large number of particles, which can be costly to render. If you had a large number of emitters in the scene, but offscreen, then the scene potentially may need to process hundreds or thousands of invisible nodes. Better to remove the emitter nodes until they are about to become visible.

Typically, the design of your culling algorithm is based on your gameplay. For example:

- In a racing game, the player is usually traveling around a track in a consistent direction. Because of this, you can usually predict what content is going to be visible in the near future and preload it. As the player advances through the race track, you can remove nodes the player can no longer see.
- In an adventure game, the player may be in a scrolling environment which permits movement in arbitrary directions. When the player moves through the world, you might be able to predict which terrain is nearby and which terrain is not. Then, only include the terrain for the local content.

When content is always going to be added and removed at once, consider using an interim node object to collect a set of content. The content can be quite complex, yet still be added to the scene with a single method call.

When you first design a SpriteKit game, it may seem like the scene class is doing a lot of the work. Part of the process of tuning your app is deciding whether the scene should perform a task or whether some other object in your game should do it. For example, you might consider moving work to another object when:

- The content or app logic is shared by multiple scenes.
- The content or app logic is particularly expensive to set up and only needs to be performed once.

For example, if your game uses the same textures for all its gameplay, you might create a special loading class that runs once at startup. You perform the work of loading the textures once, and then leave them in memory. If a scene object is deleted and recreated to restart gameplay, the textures do not need to be reloaded.

Designing new games requires you to make subclasses of the [SKScene](https://developer.apple.com/documentation/spritekit/skscene) class. However, the other node classes in SpriteKit are also designed to be subclassed so that you can add custom behavior. For example, you might subclass the [SKSpriteNode](https://developer.apple.com/documentation/spritekit/skspritenode) class to add AI logic specific to your game. Or, you might subclass the [SKNode](https://developer.apple.com/documentation/spritekit/sknode) class to create a class that implements a particular drawing layer in your scene. And if you want to directly implement interactivity in a node, you must create a subclass.

When you design a new node class, there are implementation details specific to SpriteKit that are important to understand. But you also need to consider the role that the new class plays in your game and how objects of the class interact with other objects. You need to create well-defined class interfaces and calling conventions so that objects interoperate without subtle bugs slowing your development process.

Here are important guidelines to follow when creating your own subclasses:

- All of the standard node classes support the [NSCopying](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSCopying/Description.html#//apple_ref/occ/intf/NSCopying) and [NSCoding](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSCoding/Description.html#//apple_ref/occ/intf/NSCoding) protocols. If your subclass adds new properties or instance variables, then your subclass should also implement these behaviors. This support is essential if you plan to copy nodes within your game or use archiving to build your own game tools.
- Although nodes are similar to views, you cannot add new drawing behavior to a node class. You must work through the node’s existing methods and properties. This means either controlling a node’s own properties (such as changing a sprite’s texture) or adding additional nodes and controlling their behavior. In either case, you need to consider how your class is going to interact with other parts of your code. You may need to establish your own calling conventions to avoid subtle rendering bugs. For example, one common convention is to avoid adding children to a node object that creates and manages its own child nodes.
- In many cases, expect to add methods that can be called during the scene’s pre-processing and post-processing steps. Your scene coordinates these steps, but focused node subclasses perform the work.
- If you want to implement event handling in a node class, you must implement separate event-handling code for iOS and OS X. The [SKNode](https://developer.apple.com/documentation/spritekit/sknode) class inherits from [NSResponder](https://developer.apple.com/documentation/appkit/nsresponder) on OS X and [UIResponder](https://developer.apple.com/documentation/uikit/uiresponder) on iOS.
- In some game designs, you can rely on the fact that a particular combination of classes is always going to be used together in a specific scene. In other designs, you may want to create classes that can be used in multiple scenes. The more important reuse is to your design, the more time you should spend designing clean interfaces for objects to interact with each other. When two classes are dependent on each other, use [delegation](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) to break that dependency. Most often, you do this by defining a delegate on your node and a protocol for delegates to implement. Your scene (or another node, such as the node’s parent) implements this protocol. Your node class can then be reused in multiple scenes, without needing to know the scene’s class.
- Keep in mind that when a node class is being initialized, it is not yet in the scene, so its [parent](https://developer.apple.com/documentation/spritekit/sknode/1483080-parent) and [scene](https://developer.apple.com/documentation/spritekit/sknode/1483064-scene) properties are `nil`. You may need to defer some initialization work until after the node is added to the scene.

A large part of building a node tree is organizing the graphical content that needs to be drawn. What needs to be drawn first? What needs to be drawn last? How are these things rendered?

Consider the following advice when designing your node tree:

- Do not add the content nodes or physics bodies to the scene directly. Instead, add one or more [SKNode](https://developer.apple.com/documentation/spritekit/sknode) objects to the tree to represent different layers of content in your game and then work with those layer objects. You can then precisely control the contents of each layer. For example, you can rotate one layer of the content without rotating all of the scene’s content. It also becomes easier for you to remove or replace portions of your scene rendering with other code. For example, if game scores and other information is played in a heads-up display layer, then this layer can be removed when you want to take screenshots. In a very complex app, you might continue this pattern deeper into your node tree by adding children to a layer node.

  When you use layers to organize your content, consider how the layers interact with one another. Do they know anything about each other’s content? Does a higher-level layer need to know anything about how the lower layers are rendered in order to render its own content?
- Use clipping and effect nodes sparingly. Both are very powerful, but can be expensive, especially when nested together within the node tree.
- Whenever possible, nodes that are rendered together should use the same blend mode. If all of the children of a node use the same blend mode and texture atlas, then SpriteKit can usually draw these sprites in a single drawing pass. On the other hand, if the children are organized so that the drawing mode changes for each new sprite, then SpriteKit might perform as one drawing pass per sprite, which is quite inefficient.
- When designing emitter effects, use low particle birth rates whenever possible. Particles are not free; each particle adds rendering and drawing overhead.
- By default, sprites and other content are blended using an alpha blend mode. If the sprite’s content is opaque, such as for a background image, use the [SKBlendModeReplace](https://developer.apple.com/documentation/spritekit/skblendmode/replace) blend mode.
- Use game logic and art assets that match SpriteKit’s coordinate and rotation conventions. This means orienting artwork to the right. If you orient the artwork in some other direction, you need to convert angles between the conventions used by the art and the conventions used by SpriteKit. For example, if the artwork is oriented upward, then you add `PI/2` radians to the angle to convert from SpriteKit’s convention to your art’s convention and vice versa.
- Turn on the diagnostic messages in the [SKView](https://developer.apple.com/documentation/spritekit/skview) class. Use the frame rate as a general diagnostic for performance, and the node and drawing pass counts to further understand how the content was rendered. You can also use Instruments and its OpenGL diagnostic tools to find additional information about where your game is spending its time.
- Test your game on real hardware, and on devices with different characteristics. In many cases, the balance of CPU resources and GPU resources are different on each Mac or iOS device. Testing on multiple devices helps you to determine whether your game runs well on the majority of devices.

At any given time, your game manages a lot of data, including the positions of nodes in the scene. But it also includes static data such as:

- Art assets and required data to render that artwork correctly
- Level or puzzle layouts
- Data used to configure the gameplay (such as the speed of the monster and how much damage it does when it attacks)

Whenever possible, avoid embedding your game data directly in the game code. When the data changes, you are forced to recompile the game, which usually means that a programmer is involved in the design changes. Instead, keep data independent of the code, so that a game designer or artist can make changes directly to the data.

The best place to store game data depends on where that data is used within your game. For data not related to SpriteKit, a property list stored in your app bundle is a good solution. However, for SpriteKit data, you have another option. Because all SpriteKit classes support archiving, you can simply create archives of important SpriteKit objects and then include these archives in your game. For example, you might:

- Store a game level as an archive of a scene node. This archive includes the scene, all of its descendants in the node tree, and all of their connected physics bodies, joints, and actions.
- Store individual archives for specific preconfigured nodes, such a node for each monster. Then, when a new monster needs to be created, you load it from the archive.
- Store saved games as a scene archive.
- Build your own tools to create and edit archived content. Then, your game designers and artists can work within these tools to create game objects and archive them using a format that your game reads. Your game engine and your tools would share common classes.
- You could store SpriteKit data in a property list. Your game loads the property list and uses it to create game assets.

Here are a few guidelines for working with archives:

- Use the [userData](https://developer.apple.com/documentation/spritekit/sknode/1483121-userdata) property on nodes to store game-specific data, especially if you are not implementing your own subclasses.
- Avoid hardcoding references to specific nodes. Instead, give interesting nodes a unique [name](https://developer.apple.com/documentation/spritekit/sknode/1483136-name) property and search for them in the tree.
- Custom actions that call blocks cannot be archived. You need to create and add those actions within your game.
- Most node objects provide all the necessary properties to determine what they are and how they were configured. However, actions and physics bodies do not. This means that when developing your own game tools, you cannot simply archive actions and physics bodies and use these archives to store your tool data. Instead, the archives should only be the final output from your game tools.

[Next](Document%20Revision%20History.md)[Previous](Simulating%20Physics.md)

