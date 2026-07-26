---
title: Gesture Recognition on iOS With Attention to Detail
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/01/gesture-recognition-on-ios-with-attention-to-detail/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:e187b075018245cc'
translated: false
---

> 原文：[Gesture Recognition on iOS With Attention to Detail](https://oleb.net/blog/2012/01/gesture-recognition-on-ios-with-attention-to-detail/)　·　Ole Begemann

# Gesture Recognition on iOS With Attention to Detail

One of the things that sets the iPhone’s user interface apart from the competition is Apple’s incredible attention to detail. This attention does not only extend to every single pixel on the screen but, perhaps even more important, also to gesture recognition: the standard iOS controls do a lot of smart things in order to identify the gesture the user intended to make and to allow multiple gestures to be executed at the same time if appropriate.

For example, scroll views must distinguish between a simple tap and the beginning of a swipe gesture. Similarly, the built-in map view control allows pinching and scrolling in one simultaneous gesture (put two fingers on the screen and you can switch seamlessly between pinching and scrolling without having to “restart” the gesture).

# Half-assed Gesture Recognition Is Not Good Enough

We should set ourselves the same high standards for our own apps. In this article, I would like to show you an example where the half-assed implementation of gesture recognition seems to work well enough at first glance. But as the user continues to use the app, they quickly stumble upon little irritations, small annoyances in the user interface that they perhaps cannot even pinpoint but notice nevertheless. And while these irritations do not seem to be a big deal to many developers, I want to show you how getting rid of them can improve the user experience tremendously.

![The sample gesture recognition app](https://oleb.net/media/gesture-recognition-sample-app-screenshot.png)

<sub>The sample app: using the standard gestures, you can drag the image across the screen, make it bigger or smaller by pinching, and rotate it. A double tap resets the image to its original state.</sub>

For our example, imagine a simple app that lets the user play around with an image on screen. Using gestures, they can:

- Drag the image across the screen.
- Make it bigger or smaller.
- Rotate it.

In addition, a double tap should reset the image to its original position and size.

To implement this app we need to create four [gesture recognizers](http://developer.apple.com/library/IOs/#documentation/UIKit/Reference/UIGestureRecognizer_Class/Reference/Reference.html), one for each required gesture. The setup code for the app would look like this:

```
- (void)viewDidLoad
{
    [super viewDidLoad];

    self.imageView.userInteractionEnabled = YES;

    UIPanGestureRecognizer *panRecognizer = [[UIPanGestureRecognizer alloc] initWithTarget:self action:@selector(panDetected:)];
    [self.imageView addGestureRecognizer:panRecognizer];

    UIPinchGestureRecognizer *pinchRecognizer = [[UIPinchGestureRecognizer alloc] initWithTarget:self action:@selector(pinchDetected:)];
    [self.imageView addGestureRecognizer:pinchRecognizer];

    UIRotationGestureRecognizer *rotationRecognizer = [[UIRotationGestureRecognizer alloc] initWithTarget:self action:@selector(rotationDetected:)];
    [self.imageView addGestureRecognizer:rotationRecognizer];

    UITapGestureRecognizer *tapRecognizer = [[UITapGestureRecognizer alloc] initWithTarget:self action:@selector(tapDetected:)];
    tapRecognizer.numberOfTapsRequired = 2;
    [self.imageView addGestureRecognizer:tapRecognizer];
}
```

This is pretty straightforward code. Enable user interaction on our image view (which is disabled by default) and then create the gesture recognizers one by one and add them to the image view. The implementation of the gesture recognizer actions is equally simple:

```
- (void)panDetected:(UIPanGestureRecognizer *)panRecognizer
{
    CGPoint translation = [panRecognizer translationInView:self.view];
    CGPoint imageViewPosition = self.imageView.center;
    imageViewPosition.x += translation.x;
    imageViewPosition.y += translation.y;

    self.imageView.center = imageViewPosition;
    [panRecognizer setTranslation:CGPointZero inView:self.view];
}

- (void)pinchDetected:(UIPinchGestureRecognizer *)pinchRecognizer
{
    CGFloat scale = pinchRecognizer.scale;
    self.imageView.transform = CGAffineTransformScale(self.imageView.transform, scale, scale);
    pinchRecognizer.scale = 1.0;
}

- (void)rotationDetected:(UIRotationGestureRecognizer *)rotationRecognizer
{
    CGFloat angle = rotationRecognizer.rotation;
    self.imageView.transform = CGAffineTransformRotate(self.imageView.transform, angle);
    rotationRecognizer.rotation = 0.0;
}

- (void)tapDetected:(UITapGestureRecognizer *)tapRecognizer
{
    [UIView animateWithDuration:0.25 animations:^{
        self.imageView.center = CGPointMake(CGRectGetMidX(self.view.bounds), CGRectGetMidY(self.view.bounds));
        self.imageView.transform = CGAffineTransformIdentity;
    }];
}
```

[Download the code for the sample app at this stage](https://github.com/ole/GestureRecognition/zipball/plain-gestures).

# Works But Does Not Feel Great

Build and run this app, preferably on a device (testing the effectiveness of gestures on the simulator is not the best idea). If you are like me, using the app feels okay but not great. In fact, there are several problems with the gestures:

1. The gestures only work when all fingers are placed on the image view. This can get quite difficult when the target view is small, especially when two fingers are required as for pinching and rotating. It is possible for the user to make the image so small that it is almost impossible to recover from the situation.
2. None of the gestures work simultaneously with others. If I want to rotate the image but accidentally begin a pinch gesture, I have to release my fingers and start over. I cannot pinch, rotate and drag the image in one fluid motion.
3. There is no momentum at play here. All movements stop immediately when the user lifts their fingers off the screen.

We will solve points 1 and 2 in this post. I will cover the third issue in another article.

# Solving the UX Issues

The first problem is trivial to solve: rather than adding the gesture recognizers to the image view, we add them directly to its superview (the view controller’s view). That way, the user can use the entire screen for gestures. It does not matter whether two, one or no fingers hit the image view. Modify `viewDidLoad` to implement this change:

```
- (void)viewDidLoad
{
    [super viewDidLoad];

    UIPanGestureRecognizer *panRecognizer = [[UIPanGestureRecognizer alloc] initWithTarget:self action:@selector(panDetected:)];
    [self.view addGestureRecognizer:panRecognizer];

    UIPinchGestureRecognizer *pinchRecognizer = [[UIPinchGestureRecognizer alloc] initWithTarget:self action:@selector(pinchDetected:)];
    [self.view addGestureRecognizer:pinchRecognizer];

    UIRotationGestureRecognizer *rotationRecognizer = [[UIRotationGestureRecognizer alloc] initWithTarget:self action:@selector(rotationDetected:)];
    [self.view addGestureRecognizer:rotationRecognizer];

    UITapGestureRecognizer *tapRecognizer = [[UITapGestureRecognizer alloc] initWithTarget:self action:@selector(tapDetected:)];
    tapRecognizer.numberOfTapsRequired = 2;
    [self.view addGestureRecognizer:tapRecognizer];
}
```

For the second issue, we need to tell the gesture recognizers to work simultaneously. The default behavior of gesture recognizers is to block each other: only one gesture can be recognized at a time. Fortunately, that behavior is easy to modify. Every gesture recognizer will ask its delegate (if it has one) whether it should be allowed to recognize gestures simultaneously with any other gesture recognizer it comes in conflict with. By setting our view controller as the delegate of all our gesture recognizers and simply returning `YES` from the [`gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:`](http://developer.apple.com/library/IOs/documentation/UIKit/Reference/UIGestureRecognizerDelegate_Protocol/Reference/Reference.html#//apple_ref/occ/intfm/UIGestureRecognizerDelegate/gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:) delegate method, we can tell them to work together.

Don’t forget to add the [`UIGestureRecognizerDelegate`](http://developer.apple.com/library/IOs/#documentation/UIKit/Reference/UIGestureRecognizerDelegate_Protocol/Reference/Reference.html) protocol to our view controller’s interface declaration and extend the `viewDidLoad` method as follows:

```
- (void)viewDidLoad
{
	...

    panRecognizer.delegate = self;
    pinchRecognizer.delegate = self;
    rotationRecognizer.delegate = self;
    // We don't need a delegate for the tapRecognizer
}
```

And implement the delegate method:

```
- (BOOL)gestureRecognizer:(UIGestureRecognizer *)gestureRecognizer shouldRecognizeSimultaneouslyWithGestureRecognizer:(UIGestureRecognizer *)otherGestureRecognizer
{
    return YES;
}
```

[Download the code for the sample app at this stage](https://github.com/ole/GestureRecognition/zipball/improved-gestures).

Now try out the app again. With a few simple changes, the gestures feel much more fluid and natural. It is attention to detail like this that distinguishes the really good iOS apps from the mediocre one. As mentioned, stay tuned for a future post on how to handle momentum when working with gesture recognizers. [The code for the sample app is hosted on GitHub](https://github.com/ole/GestureRecognition).
