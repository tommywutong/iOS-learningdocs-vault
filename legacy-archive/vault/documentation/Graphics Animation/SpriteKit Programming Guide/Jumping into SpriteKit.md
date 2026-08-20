---
title: SpriteKit Programming Guide
apple_id: TP40013043
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsAnimation/Conceptual/SpriteKit_PG/GettingStarted/GettingStarted.html
archived_at: '2026-07-15T07:35:15.965880Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [SpriteKit Programming Guide](About%20SpriteKit.md)


[Next](Working%20with%20Sprites.md)[Previous](About%20SpriteKit.md)

# Jumping into SpriteKit

The best way to learn SpriteKit is to see it in action. This example creates a pair of scenes and animates content in each. By working through this example, you will learn some of the fundamental techniques for working with SpriteKit content, including:

- Using scenes in a SpriteKit–based game.
- Organizing node trees to draw content.
- Using actions to animate scene content.
- Adding interactivity to a scene.
- Transitioning between scenes.
- Simulating physics inside a scene.

After you finish this project, you can use it to try out other SpriteKit concepts. Some suggestions can be found at the end of this example.

You should already be familiar with creating iOS apps before working through this project. For more information, see _[Start Developing iOS Apps Today (Retired)](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/RoadMapiOS-Legacy/index.html#//apple_ref/doc/uid/TP40011343)_. Most of the SpriteKit code in this example is the same on OS X.

This walkthrough requires Xcode 5.0. Create a new Xcode project for an iOS app using the Single View Application template.

Use the following values when creating your project:

- Product Name: `SpriteWalkthrough`
- Class Prefix: `Sprite`
- Devices: iPad

Add the SpriteKit framework to the project.

SpriteKit content is placed in a window, just like other visual content. SpriteKit content is rendered by the [SKView](https://developer.apple.com/documentation/spritekit/skview) class. The content that an [SKView](https://developer.apple.com/documentation/spritekit/skview) object renders is called a _scene_, which is an [SKScene](https://developer.apple.com/documentation/spritekit/skscene) object. Scenes participate in the [responder chain](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Responder.html#//apple_ref/doc/uid/TP40009071-CH1) and have other features that make them appropriate for games.

Because SpriteKit content is rendered by a view object, you can combine this view with other views in the view hierarchy. For example, you can use standard button controls and place them above your SpriteKit view. Or, you can add interactivity to sprites to implement your own buttons; the choice is up to you. Later in this example, you’ll see how to implement interactivity on the scene.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To configure the view controller to use SpriteKit

1. Open the storyboard for the project. It has a single view controller (`SpriteViewController`). Select the view controller’s view object and change its class to `SKView`.
2. Add an import line to the view controller’s implementation file.

```objc
#import <SpriteKit/SpriteKit.h>
```
3. Implement the view controller’s [viewDidLoad](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621495-viewdidload) method to configure the view.

```objc
- (void)viewDidLoad
{
    [super viewDidLoad];
    SKView *spriteView = (SKView *) self.view;
    spriteView.showsDrawCount = YES;
    spriteView.showsNodeCount = YES;
    spriteView.showsFPS = YES;
}
```

   The code turns on diagnostic information that describes how the scene renders the view. The most important piece of information is the frame rate (`spriteView.showsFPS`); you want your games to run at a constant frame rate whenever possible. The other lines show details on how many nodes were displayed in the view and how many drawing passes it took to render the content (fewer is better).

Next, add the first scene.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To create the Hello scene

1. Create a new class named `HelloScene` and make it a subclass of the [SKScene](https://developer.apple.com/documentation/spritekit/skscene) class.

   The header file created by Xcode has the following content:

```objc
#import <SpriteKit/SpriteKit.h>

@interface HelloScene : SKScene

@end
```

   You don’t need to change the header file.
2. Import the scene’s header file in your view controller’s implementation file.

```objc
#import "HelloScene.h"
```
3. Modify the view controller to create the scene and present the scene in the view.

```objc
- (void)viewWillAppear:(BOOL)animated
{
    HelloScene* hello = [[HelloScene alloc] initWithSize:CGSizeMake(768,1024)];
    SKView *spriteView = (SKView *) self.view;
    [spriteView presentScene: hello];
}
```
4. Build and run the project.

   The app should launch and display a screen that is blank except for the diagnostic information.

When designing a SpriteKit–based game, you design different scene classes for each major chunk of your game interface. For example, you might create a scene for the main menu and a separate scene for your gameplay. You’ll follow a similar design here. This first scene displays the traditional “Hello World” text.

Most often, you configure a scene’s content when it is first presented by the view. This is similar to the way view controllers load their views only when the `view` property is referenced. In this example, the code lives inside the [didMoveToView:](https://developer.apple.com/documentation/spritekit/skscene/1519607-didmove) method, which is called whenever the scene is presented in a view.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To display Hello World text in the scene

1. Add a new property to the scene’s implementation file to track whether the scene has created its content. Your implementation file should look like this:

```objc
#import "HelloScene.h"

@interface HelloScene ()
@property BOOL contentCreated;
@end

@implementation HelloScene

@end
```

   The property tracks information that doesn’t need to be exposed to clients, so, it is implemented in a private interface declaration inside of the implementation file.
2. Implement the scene’s [didMoveToView:](https://developer.apple.com/documentation/spritekit/skscene/1519607-didmove) method.

```objc
- (void)didMoveToView: (SKView *) view
{
    if (!self.contentCreated)
    {
        [self createSceneContents];
        self.contentCreated = YES;
    }
}
```

   The [didMoveToView:](https://developer.apple.com/documentation/spritekit/skscene/1519607-didmove) method is called whenever the scene is presented by a view, but in this case, the scene’s contents should only be configured the first time the scene is presented. So, this code uses the previously defined property (`contentCreated`) to track whether the scene’s contents have already been initialized.
3. Implement the scene’s `createSceneContents` method.

```objc
- (void)createSceneContents
{
    self.backgroundColor = [SKColor blueColor];
    self.scaleMode = SKSceneScaleModeAspectFit;
    [self addChild: [self newHelloNode]];
}
```

   A scene paints the view’s area with a background color before drawing its children. Note the use of the `SKColor` class to create the color object. In fact, `SKColor` is not a class; it is a macro that maps to [UIColor](https://developer.apple.com/documentation/uikit/uicolor) on iOS and [NSColor](https://developer.apple.com/documentation/appkit/nscolor) on OS X. It exists to make creating cross-platform code easier.

   A scene’s scale mode determines how the scene is scaled to fit in the view. In this example, the code scales the view so that you can see all of the scene’s content, using letterboxing if required.
4. Implement the scene’s `newHelloNode` method.

```objc
- (SKLabelNode *)newHelloNode
{
    SKLabelNode *helloNode = [SKLabelNode labelNodeWithFontNamed:@"Chalkduster"];
    helloNode.text = @"Hello, World!";
    helloNode.fontSize = 42;
    helloNode.position = CGPointMake(CGRectGetMidX(self.frame),CGRectGetMidY(self.frame));
    return helloNode;
}
```

   In SpriteKit, you never write code that explicitly executes drawing commands, as you would if you were using OpenGL ES or Quartz 2D. Instead, you add content by creating node objects and adding them to the scene. All drawing must be performed by the classes provided in SpriteKit. You can customize the behavior of those classes to produce many different graphical effects. However, by controlling all drawing, SpriteKit can apply many optimizations to how drawing is performed.
5. Build and run the project.

   You should see a blue screen with “Hello, World!” in it. You’ve now learned the basics for drawing SpriteKit content.

Static text is nice, but it might be more interesting if the text was animated. Most of the time, you move things around the scene by executing _actions_. Most actions in SpriteKit apply changes to a node. You create an action object to describe the changes you want, and then tell a node to run it. Then, when the scene is rendered, it executes the action, animating the changes over several frames until the action completes.

When the user touches inside the scene, the text animates and then fades away.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To animate the text

1. Add the following code to the `newHelloNode` method:

```
helloNode.name = @"helloNode";
```

   All nodes have a [name](https://developer.apple.com/documentation/spritekit/sknode/1483136-name) property that you can set to describe the node. You name a node when you want to be able to find it later or when you want to build behavior that is based on the node name. Later, you can search the tree for nodes that match the name.

   In this example, you give the label a name so that it can be discovered later. In an actual game, you might give the same name to any node that represents the same kind of content. For example, if your game represents each monster as a node, you might name the node `monster`.
2. Override the [touchesBegan:withEvent:](https://developer.apple.com/documentation/uikit/uiresponder/1621142-touchesbegan) method on the scene class. When the scene receives a touch event, it finds the node named `helloNode` and tells it to run a short animation.

   All node objects are subclasses of [UIResponder](https://developer.apple.com/documentation/uikit/uiresponder) on iOS and [NSResponder](https://developer.apple.com/documentation/appkit/nsresponder) on OS X. This means that you can create subclasses of node classes in SpriteKit to add interactivity to any node in the scene.

```objc
- (void)touchesBegan:(NSSet *) touches withEvent:(UIEvent *)event
{
    SKNode *helloNode = [self childNodeWithName:@"helloNode"];
    if (helloNode != nil)
    {
        helloNode.name = nil;
        SKAction *moveUp = [SKAction moveByX: 0 y: 100.0 duration: 0.5];
        SKAction *zoom = [SKAction scaleTo: 2.0 duration: 0.25];
        SKAction *pause = [SKAction waitForDuration: 0.5];
        SKAction *fadeAway = [SKAction fadeOutWithDuration: 0.25];
        SKAction *remove = [SKAction removeFromParent];
        SKAction *moveSequence = [SKAction sequence:@[moveUp, zoom, pause, fadeAway, remove]];
        [helloNode runAction: moveSequence];
    }
}
```

   To prevent the node from responding to repeated presses, the code clears the node’s name. Then, it builds action objects to perform various actions. After creating all of the actions, it creates a _sequence action_ that combines these actions together; when the sequence runs, it performs each of the child actions in order. Finally, the method tells the label node to execute the sequence.
3. Build and run the project.

   You should see the text as before. At the bottom of the screen, the node count should be `1`. Now, tap inside the view. You should see the text animate and fade away. After it fades away, the node count should change to `0`, because the node was removed from the parent.

SpriteKit makes it easy to transition between scenes. You can either keep scenes around persistently, or dispose of them when you transition between them. In this example, you create a second scene class to learn some other game behaviors. When the “Hello, World!” text disappears from the screen, the code creates a new scene and transitions to it. The Hello scene is discarded after the transition.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To create the Spaceship scene

1. Create a new class named `SpaceshipScene` and make it a subclass of the [SKScene](https://developer.apple.com/documentation/spritekit/skscene) class.
2. Implement code to initialize the spaceship scene’s contents. The code in the new scene’s implementation file is similar to the code you implemented for the `HelloScene` class.

```objc
#import "SpaceshipScene.h"

@interface SpaceshipScene ()
@property BOOL contentCreated;
@end

@implementation SpaceshipScene
- (void)didMoveToView:(SKView *)view
{
    if (!self.contentCreated)
    {
        [self createSceneContents];
        self.contentCreated = YES;
    }
}

- (void)createSceneContents
{
    self.backgroundColor = [SKColor blackColor];
    self.scaleMode = SKSceneScaleModeAspectFit;
}
@end
```
3. Import the `SpaceshipScene.h` header inside of the `HelloScene.m` file.

```objc
#import "SpaceshipScene.h"
```
4. In the `HelloScene` class’s [touchesBegan:withEvent:](https://developer.apple.com/documentation/uikit/uiresponder/1621142-touchesbegan) method, replace the call to [runAction:](https://developer.apple.com/documentation/spritekit/sknode/1483093-runaction) with a new call to [runAction:completion:](https://developer.apple.com/documentation/spritekit/sknode/1483103-runaction). Implement a completion handler to create and present a new scene.

```
[helloNode runAction: moveSequence completion:^{
    SKScene *spaceshipScene  = [[SpaceshipScene alloc] initWithSize:self.size];
    SKTransition *doors = [SKTransition doorsOpenVerticalWithDuration:0.5];
    [self.view presentScene:spaceshipScene transition:doors];
}];
```
5. Build and run the project.

   When you touch inside the scene, the text fades out and then the view transitions to the new scene. You should see a black screen.

The new scene doesn’t have any content yet, so you are going to add a spaceship to the scene. To build the spaceship, you need to use multiple [SKSpriteNode](https://developer.apple.com/documentation/spritekit/skspritenode) objects to create the spaceship and the lights on its surface. Each of the sprite nodes is going to execute actions.

Sprite nodes are the most common class used to create content in a SpriteKit app. They can either draw untextured or textured rectangles. In this example, you are going to use untextured objects. Later, these placeholders could be easily replaced with textured sprites without changing their behavior. In an actual game, you might need dozens or hundreds of nodes to create the visual content of your game. But, fundamentally, those sprites are going to use the same techniques as this simple example.

Although you could add all three sprites directly to the scene, that isn’t the SpriteKit way. The blinking lights are part of the spaceship! If the spaceship moves, the lights should move with it. The solution is to make the spaceship node their parent, in the same way that the scene is going to be the parent of the spaceship. The coordinates of the lights are going to be specified relative to the parent node’s position, which is at the center of the sprite image.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To add the spaceship

1. In `SpaceshipScene.m`, add code to the `createSceneContents` method to create the spaceship.

```
SKSpriteNode *spaceship = [self newSpaceship];
spaceship.position = CGPointMake(CGRectGetMidX(self.frame),                              CGRectGetMidY(self.frame)-150);
[self addChild:spaceship];
```
2. Implement the `newSpaceship` method.

```objc
- (SKSpriteNode *)newSpaceship
{
    SKSpriteNode *hull = [[SKSpriteNode alloc] initWithColor:[SKColor grayColor] size:CGSizeMake(64,32)];

    SKAction *hover = [SKAction sequence:@[
                          [SKAction waitForDuration:1.0],
                          [SKAction moveByX:100 y:50.0 duration:1.0],
                          [SKAction waitForDuration:1.0],
                          [SKAction moveByX:-100.0 y:-50 duration:1.0]]];
    [hull runAction: [SKAction repeatActionForever:hover]];

    return hull; }
```

   This method creates the spaceship’s hull and adds to it a short animation. Note that a new kind of action was introduced. A repeating action continuously repeats the action passed to it. In this case, the sequence repeats indefinitely.
3. Build and run the project.

   You should see a single rectangle for the spaceship’s hull.
4. Add code to the `newSpaceship` method to add the lights.

   Insert the following code after the line that creates the hull sprite.

```
SKSpriteNode *light1 = [self newLight];
light1.position = CGPointMake(-28.0, 6.0);
[hull addChild:light1];

SKSpriteNode *light2 = [self newLight];
light2.position = CGPointMake(28.0, 6.0);
[hull addChild:light2];
```

   When building complex nodes that have children, it is a good idea to isolate the code used to create the node behind a construction method or even a subclass. This makes it easier to change the sprite’s composition and behavior without requiring changes to clients that use the sprite.
5. Implement the `newLight` method.

```objc
- (SKSpriteNode *)newLight
{
    SKSpriteNode *light = [[SKSpriteNode alloc] initWithColor:[SKColor yellowColor] size:CGSizeMake(8,8)];

    SKAction *blink = [SKAction sequence:@[
                          [SKAction fadeOutWithDuration:0.25],
                          [SKAction fadeInWithDuration:0.25]]];
    SKAction *blinkForever = [SKAction repeatActionForever:blink];
    [light runAction: blinkForever];

    return light;
}
```
6. Build and run the project.

   You should see a pair of lights on the spaceship. When the spaceship moves, the lights move with it. All three nodes are continuously animated. You could add additional actions to move the lights around the ship; they would always move relative to the ship’s hull.

In an actual game, you usually need nodes to interact with each other. There are many ways to add behavior to sprites, so this example shows only one of them. You will add new nodes to the scene and use the physics subsystem to simulate their movement and implement collision effects.

SpriteKit provides a complete physics simulation which you can use to add automatic behaviors to nodes. That is, instead of executing actions on the nodes, physics is automatically simulated on the node, causing it to move. When it interacts with other nodes that are part of the physics system, collisions are automatically calculated and performed.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To add physics simulation to the Spaceship scene

1. Change the `newSpaceship` method to add a physics body to the spaceship.

```
hull.physicsBody = [SKPhysicsBody bodyWithRectangleOfSize:hull.size];
```
2. Build and run the project.

   The spaceship plummets through the bottom of the screen. This is because a gravitational force is applied to the spaceship’s physics body. Even though the move action is still running, physics effects are also applied to the spaceship.
3. Change the `newSpaceship` method to prevent the spaceship from being affected by physics interactions.

```
hull.physicsBody.dynamic = NO;
```

   When you run it now, the spaceship is no longer affected by gravity, so it runs as it did before. Later, making the physics body static also means that the spaceship’s velocity is unaffected by collisions.
4. Add code to the `createSceneContents` method to spawn rocks.

```
SKAction *makeRocks = [SKAction sequence: @[
    [SKAction performSelector:@selector(addRock) onTarget:self],
    [SKAction waitForDuration:0.10 withRange:0.15]
    ]];
[self runAction: [SKAction repeatActionForever:makeRocks]];
```

   The scene is _also_ a node, so it can run actions too. In this case, a custom action calls a method on the scene to create a rock. The sequence creates a rock, then waits for a random period of time. By repeating this action, the scene continuously spawns new rocks.
5. Implement the `addRock` method.

```objc
static inline CGFloat skRandf() {
    return rand() / (CGFloat) RAND_MAX;
}

static inline CGFloat skRand(CGFloat low, CGFloat high) {
    return skRandf() * (high - low) + low;
}

- (void)addRock
{
    SKSpriteNode *rock = [[SKSpriteNode alloc] initWithColor:[SKColor brownColor] size:CGSizeMake(8,8)];
    rock.position = CGPointMake(skRand(0, self.size.width), self.size.height-50);
    rock.name = @"rock";
    rock.physicsBody = [SKPhysicsBody bodyWithRectangleOfSize:rock.size];
    rock.physicsBody.usesPreciseCollisionDetection = YES;
    [self addChild:rock];
}
```
6. Build and run the project

   Rocks should now fall from the top of the scene. When a rock hits the ship, the rock bounces off the ship. No actions were added to move the rocks. Rocks fall and collide with the ship entirely due to the physics subsystem.

   The rocks are small and move quickly, so the code specifies precise collisions to ensure that all collisions are detected.

   If you let the app run for a while, the frame rate starts to drop, even though the node count remains very low. This is because the node code only shows the visible nodes in the scene. However, when rocks fall through the bottom of the scene, they continue to exist in the scene, which means that physics is still being simulated on them. Eventually there are so many nodes being processed that SpriteKit slows down.
7. Implement the [didSimulatePhysics](https://developer.apple.com/documentation/spritekit/skscene/1519965-didsimulatephysics) method in the scene, to remove rocks when they move offscreen.

```objc
-(void)didSimulatePhysics
{
    [self enumerateChildNodesWithName:@"rock" usingBlock:^(SKNode *node, BOOL *stop) {
        if (node.position.y < 0)
            [node removeFromParent];
    }];
}
```

   Each time the scene processes a frame, it runs actions and simulates physics. Your game can hook into this process to execute other custom code. Now, when the app processes a new frame of animation, it processes physics and then removes any rocks that moved off the bottom of the screen. When you run the app, the frame rate remains constant.

   Pre- and post-processing in a scene, combined with actions and physics, are the places you build your game’s behavior.

And that’s it—your first taste of SpriteKit! Everything else is a refinement of the basic techniques you’ve seen here.

Here are a few things you can try:

- Make an OS X version of this example. The code you wrote in the view controller is often implemented in an app delegate on OS X. You also need to change the responder code to use mouse events, rather than touch events. But the rest of the code should be the same.
- Use textured sprites to represent the ship and rocks. (Hint: [Working with Sprites](Working%20with%20Sprites.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbtfvbuqojnknltq))
- Try moving the spaceship in response to touch events. (Hint: [Adding Actions to Nodes](Adding%20Actions%20to%20Nodes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbtfvbuqmjrfvjvomi) and [Building Your Scene](Building%20Your%20Scene.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbtfvbuqmznknltc)).
- Add other behaviors when rocks collide with the ship. For example, make the rocks explode. (Hint: [Simulating Physics](Simulating%20Physics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbtfvbuqnrnknltc))
- Add sound effects. (Hint: Use a [playSoundFileNamed:waitForCompletion:](https://developer.apple.com/documentation/spritekit/skaction/1417664-playsoundfilenamed) action)
- Add additional graphical effects to the scene. (Hint: [Working with Sprites](Working%20with%20Sprites.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbtfvbuqojnknltq))

[Next](Working%20with%20Sprites.md)[Previous](About%20SpriteKit.md)

