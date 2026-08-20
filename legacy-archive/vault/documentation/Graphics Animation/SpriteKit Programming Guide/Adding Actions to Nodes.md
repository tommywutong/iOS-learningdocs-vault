---
title: SpriteKit Programming Guide
apple_id: TP40013043
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsAnimation/Conceptual/SpriteKit_PG/AddingActionstoSprites/AddingActionstoSprites.html
archived_at: '2026-07-15T07:35:13.550844Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [SpriteKit Programming Guide](About%20SpriteKit.md)


[Next](Building%20Your%20Scene.md)[Previous](Working%20with%20Sprites.md)

# Adding Actions to Nodes

Drawing sprites is useful, but a static image is a picture, not a game. To add gameplay, you need to be able to move sprites around the screen and perform other logic. The primary mechanism that SpriteKit uses to animate scenes is actions. Up to this point you’ve seen some part of the action subsystem. Now, it’s time to get a deeper appreciation for how actions are constructed and executed.

An action is an object that defines a change you want to make to the scene. In most cases, an action applies its changes to the node that is executing it. So, for example, if you want to move a sprite across the screen, you create a move action and tell the sprite node to run that action. SpriteKit automatically animates that sprite’s position until the action completes.

Every action is an opaque object that describes a change you want to make to the scene. All actions are implemented by the [SKAction](https://developer.apple.com/documentation/spritekit/skaction) class; there are no visible subclasses. Instead, actions of different types are instantiated using class methods. For example, here are the most common things you use actions to do:

- Changing a node’s position and orientation
- Changing a node’s size or scaling properties
- Changing a node’s visibility or making it translucent
- Changing a sprite node’s contents so that it animates through a series of textures
- Colorizing a sprite node
- Playing simple sounds
- Removing a node from the node tree
- Calling a block
- Invoking a selector on an object

After you create an action, its type cannot be changed, and you have a limited ability to change its properties. SpriteKit takes advantage of the immutable nature of actions to execute them very efficiently.

Actions can either be instantaneous or non-instantaneous:

- An instantaneous action starts and completes in a single frame of animation. For example, an action to remove a node from its parent is an instantaneous action because a node can’t be partially removed. Instead, when the action executes, the node is removed immediately.
- A non-instantaneous action has a duration over which it animates its effects. When executed, the action is processed in each frame of animation until the action completes.

The complete list of class methods used to create actions is described in _[SKAction Class Reference](https://developer.apple.com/documentation/spritekit/skaction)_, but you only need to go there when you are ready for a detailed look at how to configure specific actions.

An action is only executed after you tell a node to run it. The simplest way to run an action is to call the node’s [runAction:](https://developer.apple.com/documentation/spritekit/sknode/1483093-runaction) method. Listing 3-1 creates a new move action and then tells the node to execute it.

__Listing 3-1__  Running an action

```
SKAction *moveNodeUp = [SKAction moveByX:0.0 y:100.0 duration:1.0];
[rocketNode runAction: moveNodeUp];
```

A move action has a duration, so this action is processed by the scene over multiple frames of animation until the elapsed time exceeds the duration of the action. After the animation completes, the action is removed from the node.

You can run actions at any time. However, if you add actions to a node while the scene is processing actions, the new actions may not execute until the following frame. The steps a scene uses to process actions are described in more detail in [Advanced Scene Processing](Advanced%20Scene%20Processing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbtfvbuqnbnknltc).

A node can run multiple actions simultaneously, even if those actions were executed at different times. The scene keeps track of how far each action is from completing and computes the effect that the action has on the node. For example, if you run two actions that move the same node, both actions apply changes to every frame. If the move actions were in equal and opposite directions, the node would remain stationary.

Because action processing is tied to the scene, actions are processed only when the node is part of a presented scene’s node tree. You can take advantage of this feature by creating a node and assigning actions to it, but waiting until later to add the node to the scene. Later, when the node is added to the scene, it begins executing its actions immediately. This pattern is particularly useful because the actions that a node is running are copied and archived when the node is copied.

If a node is running any actions, its [hasActions](https://developer.apple.com/documentation/spritekit/sknode/1483081-hasactions) property returns `YES`.

To cancel actions that a node is running, call its [removeAllActions](https://developer.apple.com/documentation/spritekit/sknode/1483030-removeallactions) method. All actions are removed from the node immediately. If a removed action had a duration, any changes it already made to the node remain intact, but further changes are not executed.

The [runAction:completion:](https://developer.apple.com/documentation/spritekit/sknode/1483103-runaction) method is identical to the [runAction:](https://developer.apple.com/documentation/spritekit/sknode/1483093-runaction) method, but after the action completes, your block is called. This callback is only called if the action runs to completion. If the action is removed before it completes, the completion handler is never called.

Normally, you can’t see which actions a node is executing and if you want to remove actions, you must remove all of them. If you need to see whether a particular action is executing or remove a specific action, you must use _named actions_. A named action uses a unique key name to identify the action. You can start, remove, find, and replace named actions on a node.

Listing 3-2 is similar to [Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbtfvbuqmjrfvjvona), but now the action is identified with a key, `ignition`.

__Listing 3-2__  Running a named action

```
SKAction *moveNodeRight = [SKAction moveByX:100.0 y:0.0 duration:1.0];
[spaceship runAction: moveNodeRight withKey:@"ignition"];
```

The following key-based methods are available:

- [runAction:withKey:](https://developer.apple.com/documentation/spritekit/sknode/1483042-run) method to run the action. If an action with the same key is already executing, it is removed before the new action is added.
- [actionForKey:](https://developer.apple.com/documentation/spritekit/sknode/1483138-action) method to determine if an action with that key is already running.
- [removeActionForKey:](https://developer.apple.com/documentation/spritekit/sknode/1483076-removeactionforkey) method to remove the action.

Listing 3-3 shows how you might use a named action to control a sprite’s movement. When the user clicks inside the scene, the method is invoked. The code determines where the click occurred and then tells the sprite to run an action to move to that position. The duration is calculated ahead of time so that the sprite always appears to move at a fixed speed. Because this code uses the [runAction:withKey:](https://developer.apple.com/documentation/spritekit/sknode/1483042-run) method, if the sprite was already moving, the previous move is stopped mid-stream and the new action moves from the current position to the new position.

__Listing 3-3__  Moving a sprite to the most recent mouse-click position

```objc
- (void)mouseDown:(NSEvent *)theEvent
{
    CGPoint clickPoint = [theEvent locationInNode:self.playerNode.parent];
    CGPoint charPos = self.playerNode.position;
    CGFloat distance = sqrtf((clickPoint.x-charPos.x)*(clickPoint.x-charPos.x)+
                             (clickPoint.y-charPos.y)*(clickPoint.y-charPos.y));

    SKAction *moveToClick = [SKAction moveTo:clickPoint duration:distance/characterSpeed];
    [self.playerNode runAction:moveToClick withKey:@"moveToClick"];
}
```


SpriteKit provides many standard action types that change the properties of nodes in your scene. But actions show their real power when you combine them. By combining actions, you can create complex and expressive animations that are still executed by running a single action. A _compound action_ is as easy to work with as any of the basic action types. With that in mind, it is time to learn about sequences, groups, and repeating actions.

- A _sequence action_ (or _sequence_) has multiple child actions. Each action in the sequence begins after the previous action ends.
- A _group action_(or _group_) has multiple child actions. All actions stored in the group begin executing at the same time.
- A _repeating action_ has a single child action. When the child action completes, it is restarted.

A sequence is a set of actions that run consecutively. When a node runs a sequence, the actions are triggered in consecutive order. When one action completes, the next action starts immediately. When the last action in the sequence completes, the sequence action also completes.

Listing 3-4 shows that a sequence is created using an array of other actions.

__Listing 3-4__  Creating a sequence of actions

```
SKAction *moveUp = [SKAction moveByX:0 y:100.0 duration:1.0];
SKAction *zoom = [SKAction scaleTo:2.0 duration:0.25];
SKAction *wait = [SKAction waitForDuration: 0.5];
SKAction *fadeAway = [SKAction fadeOutWithDuration:0.25];
SKAction *removeNode = [SKAction removeFromParent];

SKAction *sequence = [SKAction sequence:@[moveUp, zoom, wait, fadeAway, removeNode]];
[node runAction: sequence];
```

There are a few things worth noting in this example:

- The `wait` action is a special action that is usually used only in sequences. This action simply waits for a period of time and then ends, without doing anything; you use them to control the timing of a sequence.
- The `removeNode` action is an instantaneous action, so it takes no time to execute. You can see that although this action is part of the sequence, it does not appear on the timeline in Figure 3-1. As an instantaneous action, it begins and completes immediately after the fade action completes. This action ends the sequence.

__Figure 3-1__  Move and zoom sequence timeline

!

A group action is a collection of actions that all start executing as soon as the group is executed. You use groups when you want actions to be synchronized. For example, the code in Listing 3-5 rotates and turns a sprite to give the illusion of a wheel rolling across the screen. Using a group (rather than running two separate actions) emphasizes that the two actions are closely related.

__Listing 3-5__  Using a group of actions to rotate a wheel

```
SKSpriteNode *wheel = (SKSpriteNode *)[self childNodeWithName:@"wheel"];
CGFloat circumference = wheel.size.height * M_PI;

SKAction *oneRevolution = [SKAction rotateByAngle:-M_PI*2 duration:2.0];
SKAction *moveRight = [SKAction moveByX:circumference y:0 duration:2.0];

SKAction *group = [SKAction group:@[oneRevolution, moveRight]]; [wheel runAction:group];
```

Although the actions in a group start at the same time, the group does not complete until the last action in the group has finished running. Listing 3-6 shows a more complex group that includes actions with different timing values. The sprite animates through its textures and moves down the screen for a period of two seconds. However, during the first second, the the sprite zooms in and changes from full transparency to a solid appearance. Figure 3-2 shows that the two actions that make the sprite appear finish halfway through the group’s animation. The group continues until the other two actions complete.

__Listing 3-6__  Creating a group of actions with different timing values

```
[sprite setScale: 0];
SKAction *animate = [SKAction animateWithTextures:textures timePerFrame:2.0/numberOfTextures];
SKAction *moveDown = [SKAction moveByX:0 y:-200 duration:2.0];
SKAction *scale = [SKAction scaleTo:1.0 duration:1.0];
SKAction *fadeIn = [SKAction fadeInWithDuration: 1.0];

SKAction *group = [SKAction group:@[animate, moveDown, scale, fadeIn]];
[sprite runAction:group];
```


__Figure 3-2__  Grouped actions start at the same time, but complete independently

!

A repeating action loops another action so that it repeats multiple times. When a repeating action is executed, it executes its contained action. Whenever the looped action completes, it is restarted by the repeating action. Listing 3-7 shows the creation methods used to create repeating actions. You can create an action that repeats an action a finite number of times or an action that repeats an action indefinitely.

__Listing 3-7__  Creating repeating actions

```
SKAction *fadeOut = [SKAction fadeOutWithDuration: 1];
SKAction *fadeIn = [SKAction fadeInWithDuration: 1];
SKAction *pulse = [SKAction sequence:@[fadeOut,fadeIn]];

SKAction *pulseThreeTimes = [SKAction repeatAction:pulse count:3];
SKAction *pulseForever = [SKAction repeatActionForever:pulse];
```

Figure 3-3 shows the timing arrangement for the `pulseThreeTimes` action. You can see that the sequence finishes, then repeats.

__Figure 3-3__  Timing for a repeating action

!

When you repeat a group, the entire group must finish before the group is restarted. Listing 3-8 creates a group that moves a sprite and animates its textures, but in this example the two actions have different durations. Figure 3-4 shows the timing diagram when the group is repeated. You can see that the texture animation runs to completion and then no animation occurs until the group repeats.

__Listing 3-8__  Repeating a group animation

```
SKAction *animate = [SKAction animateWithTextures:textures timePerFrame:1.0/numberOfImages];
SKAction *moveDown = [SKAction moveByX:0 y:-200 duration:2.0];

SKAction *group = [SKAction group:@[animate, moveDown]];
```


__Figure 3-4__  Timing for a repeated group

!

What you may have wanted was for each action to repeat at its own natural frequency. To do this, create a set of repeating actions and then group them together. Listing 3-9 shows how you would implement the timing shown in Figure 3-5.

__Listing 3-9__  Grouping a set of repeated actions

```
SKAction *animate = [SKAction animateWithTextures:textures timePerFrame:1.0/numberOfImages];
SKAction *moveDown = [SKAction moveByX:0 y:-200 duration:2.0];

SKAction *repeatAnimation = [SKAction repeatActionForever:animate];
SKAction *repeatMove = [SKAction repeatActionForever:moveDown];

SKAction *group = [SKAction group:@[repeatAnimation, repeatMove]];
```


__Figure 3-5__  Each action repeats at its natural interval

!

By default, an action with a duration applies its changes linearly over the duration you specified. However, you can adjust the timing of animations through a few properties:

- Normally, an animated action runs linearly. You can use an action’s [timingMode](https://developer.apple.com/documentation/spritekit/skaction/1417807-timingmode) property to choose a nonlinear timing mode for an animation. For example, you can have the action start quickly and then slow down over the remainder of the run.
- An action’s [speed](https://developer.apple.com/documentation/spritekit/skaction/1417718-speed) property changes the rate at which an animation plays. You can speed up or slow down an animation from its default timing.

  A speed value of `1.0` is the normal rate. If you set an action’s speed property to `2.0`, when the action is executed by a node, it plays twice as fast. To pause the action, set the value to `0`.

  If you adjust the speed of an action that contains other actions (such as a group, sequence, or repeating action), the rate is applied to the actions contained within. The enclosed actions are also affected by their own `speed` property.
- A node’s [speed](https://developer.apple.com/documentation/spritekit/sknode/1483036-speed) property has the same effect as the action’s [speed](https://developer.apple.com/documentation/spritekit/skaction/1417718-speed) property, but the rate is applied to _all_ actions processed by the node or by any of the node’s descendants in the scene tree.

SpriteKit determines the rate at which an animation applies by finding all of the rates that apply to the action and multiplying them.

Actions work best when you create them once and use them multiple times. Whenever possible, create actions early and save them in a location where they can be easily retrieved and executed.

Depending on the kind of action, any of the following locations might be useful:

- A node’s [userData](https://developer.apple.com/documentation/spritekit/sknode/1483121-userdata) property
- The parent node’s `userData` property, if dozens of nodes share the same actions and the same parent
- The scene’s `userData` property for actions shared by multiple nodes throughout the scene
- If subclassing, then on a property of the subclass

If you need designer or artist input on how a node’s properties are animated, consider moving the action creation code into your custom design tools. Then archive the action and load it in your game engine. For more information, see [SpriteKit Best Practices](SpriteKit%20Best%20Practices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbtfvbuqnznknltc).

Although actions are efficient, there is a cost to creating and executing them. If you are making changes to a node’s properties in every frame of animation and those changes need to be recomputed in each frame, you are better off making the changes to the node directly and not using actions to do so. For more information on where you might do this in your game, see [Advanced Scene Processing](Advanced%20Scene%20Processing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbtfvbuqnbnknltc).

Here are some things to try with actions:

- Try the different kinds of actions on your sprites. (Hint: _[SKAction Class Reference](https://developer.apple.com/documentation/spritekit/skaction)_)
- Create an action group that synchronizes moving a sprite onscreen with another animation. (Hint: [Groups Run Actions in Parallel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbtfvbuqmjrfvjvomjv))
- Use named actions to create cancelable actions. Connect those actions to your user interface code. (Hint: [Using Named Actions for Precise Control over Actions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbtfvbuqmjrfvjvony))
- Create a sequence that tells an interesting story. For example, consider creating an animated title screen to display when your game is launched. (Hint [Sequences Run Actions in Series](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbtfvbuqmjrfvjvomjr))

[Next](Building%20Your%20Scene.md)[Previous](Working%20with%20Sprites.md)

