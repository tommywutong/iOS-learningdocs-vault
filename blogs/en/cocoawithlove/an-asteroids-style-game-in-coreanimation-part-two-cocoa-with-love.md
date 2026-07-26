---
title: 'An Asteroids-style game in CoreAnimation, Part Two. | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/02/asteroids-style-game-in-coreanimation_22.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:87514573c08e42f5'
translated: false
---

> 原文：[An Asteroids-style game in CoreAnimation, Part Two. | Cocoa with Love](https://www.cocoawithlove.com/2009/02/asteroids-style-game-in-coreanimation_22.html)　·　Cocoa with Love (Matt Gallagher)

How would you write an arcade-style 2D game in CoreAnimation? I'll show you how to write a resolution independent, high-speed, model-view-controller designed, Asteroids-style arcade game using CoreAnimation as the screen renderer. In this second of four parts, I'll create basic objects in the game and their corresponding CoreAnimation Layers on screen.

## We have a window

In the [previous post](https://www.cocoawithlove.com/2009/02/asteroids-style-game-in-coreanimation.html) I proposed an Asteroids-style game in CoreAnimation and explained the basic design of the Quartzeroids2 game

I showed the code to construct and scale the window. It has a blue gradient background and can switch between fullscreen and windowed modes.

Now, we need to put something in that window.

![](https://www.cocoawithlove.com/assets/objc-era/objectsonscreen.png)

Objects placed on screen in this part.

## Image Layers

Drawing in the window is done using CoreAnimation layers. If you looked closely at how the window background was drawn in Part One, you'll notice that it was a `CALayer`, drawn using a single image:

```objc
NSImage *image = [NSImage imageNamed:imageName];
[image
    drawInRect:NSRectFromCGRect([self bounds])
    fromRect:[image alignmentRect]
    operation:NSCompositeSourceOver
    fraction:1.0];
```

Since this single image is a PDF made from vector (not bitmapped) components, this means that the layer can be drawn at any resolution without aliasing effects from resizing. In fact, the background PDF isn't even the right aspect ratio and Cocoa happily reshapes it for us. The added processing time to render a PDF, relative to bitmap, doesn't really matter since CoreAnimation only renders the CALayer once, then reuses the existing texture.

## Game Objects and Layers

Placing a game-related object on screen will require two different components: the `GameObject` and the `GameObjectLayer`.

### GameObject

The `GameObject` is the version of the object as handled in the `GameData`. Since the game logic is responsible for deciding the size, positioning, speed, trajectory and in some cases the image and angle of rotation of the object, these properties will all be properties of the `GameObject`.

The `GameObject`s are held by the `GameData` object. It tracks all of the `GameObject`s in a dictionary, so all `GameObject`s can be accessed at any time by their unique key in the `GameData`'s `gameObjects` dictionary.

> The biggest quirk about how I decided to implement the
> 
> is that it is totally resolution independent. All coordinates and sizes are measured in units where
> 
> is the height of the game window. So the coordinates
> 
> ,
> 
> and
> 
> are the bottom-left corner, center and top-right corners of the screen respectively (
> 
> is the window aspect ratio: width of the window divided by the height).

With the `GameObject` being just a long list of Objective-C properties, most of the code in `GameObject` exists to set, modify or update those properties. The biggest common "update" that needs to be performed is to move the object according to its speed and trajectory and "wrap" the object if it goes off the edge of the screen:

```objc
- (BOOL)updateWithTimeInterval:(NSTimeInterval)timeInterval
{
    x += timeInterval * speed * cos(trajectory);
    y += timeInterval * speed * sin(trajectory);
    
    if (x > GAME_ASPECT + (0.5 + GAME_OBJECT_BOUNDARY_EXCESS) * width)
    {
        x = -0.5 * width;
    }
    else if (x < -(0.5 + GAME_OBJECT_BOUNDARY_EXCESS) * width)
    {
        x = GAME_ASPECT + 0.5 * width;
    }
    
    if (y > 1.0 + (0.5 + GAME_OBJECT_BOUNDARY_EXCESS) * height)
    {
        y = -0.5 * height;
    }
    else if (y < -(0.5 + GAME_OBJECT_BOUNDARY_EXCESS) * height)
    {
        y = 1.0 + 0.5 * height;
    }
    
    return NO;
}
```

This method returns "NO" to indicate that it was not deleted during the update. This won't be used until next week when we add more of the game logic.

The objects are allowed to exceed the edge of the bounds by `GAME_OBJECT_BOUNDARY_EXCESS`. This ensures that they don't feel like they disappeared with a tiny portion still onscreen.

### GameObjectLayer

The `GameObjectLayer` is a subclass of `ImageLayer`, using that class' code to render a single image to a `CALayer`. A `GameObjectLayer` contains a key that identifies its corresponding `GameObject` in the `GameData`. It observes the `GameData`'s `gameObjects` dictionary for changes on that key and when any of the observed `GameObject` properties change, the `GameObjectLayer` will update itself accordingly.

The result is that the only substantial work required in the `GameObjectLayer` is updating itself when a change in the `GameObject` is observed.

The `GameObjectLayer`'s `observeValueForKeyPath:ofObject:change:context:` method is smart enough to realize when the `GameObject` changes to `NSNull` (i.e. is deleted) and autodeletes.

```objc
- (void)update
{
    GameObject *gameObject = [[[GameData sharedGameData] gameObjects] objectForKey:gameObjectKey];
    double gameHeight = [[GameData sharedGameData] gameHeight];

    NSString *gameObjectImageName = gameObject.imageName;
    double x = gameObject.x * gameHeight;
    double y = gameObject.y * gameHeight;
    double width = gameObject.width * gameHeight;
    double height = gameObject.height * gameHeight;
    double angle = gameObject.angle;
    BOOL visible = gameObject.visible;

    self.imageName = gameObjectImageName;
    self.bounds = CGRectMake(0, 0, width, height);
    self.position = CGPointMake(x, y);
    self.transform = CATransform3DMakeRotation(angle, 0, 0, 1.0);
    self.hidden = !visible;
}
```

Notice that the `GameObjectLayer` is _not_ resolution independent, so the `GameObject` coordinates are multiplied through by the `gameHeight` to convert them to coordinates in the layer hierarchy.

### Controller code to bind them

The final element required to make `GameObject`s and `GameObjectLayer`s work together is controller code to construct the `GameObjectLayer` for each `GameObject` as it appears.

I chose to do this by making the `GameData` send a `GameObjectNewNotification` every time a new `GameObject` is added to the `gameObjects` dictionary. The GameController observes this notification with the following method:

```objc
- (void)createImageLayerForGameObject:(NSNotification *)notification
{
    NSString *gameObjectKey = [notification object];
    
    GameObjectLayer *newLayer =
        [[[GameObjectLayer alloc]
            initWithGameObjectKey:gameObjectKey]
        autorelease];

    [CATransaction begin];
    [CATransaction
        setValue:[NSNumber numberWithBool:YES]
        forKey:kCATransactionDisableActions];
    [backgroundLayer addSublayer:newLayer];
    [CATransaction commit];
}
```

Transactions are disabled so the layer doesn't fade in, it appears immediately.

## Letting the view reinterpret the data

If you ran the program with the above code, the asteroid would not look like the slightly soccerball texture shown in the screenshot at the top and it would not spin. The asteroid would be a smooth gradient circle. This is because the the asteroid shown in the screenshot is made of two components: the non-rotating "asteroid-back" which provides a consistent lightsource-like effect and the "asteroid-front" which is a spinning second layer on top of the back layer.

![](https://www.cocoawithlove.com/assets/objc-era/asteroid.png)

The `GameData` only contains the basic bounds information, which is mapped onto the "asteroid-back" by default. How can we add the second spinning layer for the purposes of display?

We could add the second layer as another object in the game but since I want this layer for the purposes of display (it has no real game-logic impact), I decided to handle it a different way.

After the `[CATransaction commit];` line in the previous code sample, I include the code:

```objc
if ([gameObjectKey rangeOfString:GAME_ASTEROID_KEY_BASE].location == 0)
{
    AsteroidFrontLayer *asteroidFrontLayer =
        [[[AsteroidFrontLayer alloc]
            initWithGameObjectKey:gameObjectKey]
        autorelease];
    
    [CATransaction begin];
    [CATransaction
        setValue:[NSNumber numberWithBool:YES]
        forKey:kCATransactionDisableActions];
    [backgroundLayer addSublayer:asteroidFrontLayer];
    [CATransaction commit];
}
```

So I look to see if the new `GameObject` is added to the `gameObjects` dictionary using a key that starts with `GAME_ASTEROID_KEY_BASE`. If it does, then I create a second layer that tracks the same underlying `GameObject`. This second layer is an `AsteroidFrontLayer` instead of the generic `GameObjectLayer`. This `AsteroidFrontLayer` class is a subclass of `GameObjectLayer` that overrides the `imageName` to be "asteroid-front" and applies a rotation to the layer on each update.

## Conclusion

> Quartzeroids2 Part 2 project
> 
> (225kB) which demonstrates the classes presented in this post.

The project for this part shows the `GameObject`, `GameObjectLayer` and `AsteroidFrontLayer` in a simple, non-interactive display. To show everything on screen, the `GameData` class contains a `newGame` method which constructs some sample objects and then starts a timer running to call the ` updateWithTimeInterval:` methods repeatedly.

Now that we can draw our objects on screen, Part 3 will add user-interaction and game logic.
