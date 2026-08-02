---
title: Core Video Programming Guide
apple_id: TP40001536
resource_type: Guide
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QuartzCore
published: '2007-04-03'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreVideo/CVProg_Tasks/CVProg_Tasks.html
archived_at: '2026-07-15T07:35:40.037986Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Video Programming Guide](Introduction%20to%20Core%20Video%20Programming%20Guide.md)


[Next](Glossary.md)[Previous](Core%20Video%20Concepts.md)

# Core Video Tasks

This chapter describes some common programming tasks used when processing Core Video. The examples in this chapter are written in Objective-C and use Cocoa, but Core Video can be used in a Carbon program as well.

In most cases, you will want to use the display link to access individual video frames. If your application is involved in generating the actual video frames (for example, if you’re writing a video compressor or creating animated images), you should consider using Core Video buffers to hold your frame data.

The most common Core Video task is to use the display link to obtain frames of uncompressed video. Your application is then free to manipulate them as it likes before sending the frames to the display.

For simplicity, assume that all the method calls in this section act on a `MyVideoView` object, which is subclassed from the `NSOpenGLView` class:

__Listing 2-1__  The MyVideoView interface

```objc
@interface MyVideoView : NSOpenGLView
{

    NSRecursiveLock         *lock;
    QTMovie                 *qtMovie;
    QTTime                  movieDuration;
    QTVisualContextRef      qtVisualContext;
    CVDisplayLinkRef        displayLink;
    CVImageBufferRef        currentFrame;
    CIFilter                *effectFilter;
    CIContext               *ciContext;

    NSDictionary            *fontAttributes;

    int                     frameCount;
    int                     frameRate;
    CVTimeStamp             frameCountTimeStamp;
    double                  timebaseRatio;
    BOOL                    needsReshape;
    id                      delegate;
}
…
@end
```

For more information about using the `NSOpenGLView` class, see the example project _Cocoa OpenGL_.

Setting up a display link involves the following steps:

- Create a display link thread.
- Bind the link to a specific display.
- Register a display output callback.
- Starting the display link thread.

The method `awakeFromNib` in Listing 2-2 shows how you might implement the display link.

__Listing 2-2__  Setting up a display link

```objc
- (void)awakeFromNib
{
    CVReturn            error = kCVReturnSuccess;
    CGDirectDisplayID   displayID = CGMainDisplayID();// 1

    error = CVDisplayLinkCreateWithCGDisplay(displayID, &displayLink);// 2
    if(error)
    {
        NSLog(@"DisplayLink created with error:%d", error);
        displayLink = NULL;
        return;
    }
    error = CVDisplayLinkSetOutputCallback(displayLink,// 3
                                 MyDisplayLinkCallback, self);

}
```

Here is how the code works:

1. Obtains the Core Graphics display ID for the display you want to associate with this display link. The Core Graphics function `CGMainDisplayID` simply returns the ID of the user’s main display (that is, the one containing the menu bar).
2. Creates a display link for the specified display. If desired, you can create a display link that can work with any of the currently active displays by calling `CVDisplayLinkCreateWithActiveCGDisplays` instead. You must then call `CVDisplayLinkSetCurrentCGDisplay` to designate a specific display for the display link.

   If the user moves the window containing the video to another monitor, you should update the display link appropriately. In Cocoa you can check the window position when you receive an NSWindowDidMoveNotification notification from a handler such as the following:

```objc
- (void)windowChangedScreen:(NSNotification*)inNotification
{
  NSWindow *window = [mainView window];
  CGDirectDisplayID displayID = (CGDirectDisplayID)[[[[window screen]
         deviceDescription] objectForKey:@"NSScreenNumber"] intValue];
  if((displayID != NULL) && (mainViewDisplayID != displayID))
  {
    CVDisplayLinkSetCurrentCGDisplay(displayLink, displayID);
    mainViewDisplayID = displayID;
  }
}
```

   In Carbon, you should call the Window Manager function `GetWindowGreatestAreaDevice` to obtain the `GDevice` structure for the window’s display. You can then store its device ID with the window and check to see if it has changed whenever your `kEventWindowBoundsChanged` handler gets called.
3. Sets the output callback for the display link. This is the function that the display link calls whenever it wants you to output a video frame. This example passes a reference to the instance using this method (that is, `self`), as user data. For example, if this method is part of the `MyVideoView` class, the user data is a reference to a `MyVideoView` instance.

When you are ready to start processing video frames, call `CVDisplayLinkStart` to activate the display link thread. This thread runs independent of your application process. You should stop the thread by calling `CVDisplayLinkStop` when your application quits or otherwise stops displaying video.

Before you can begin processing, you must set up your video source to provide frames. The video source can be anything that can supply uncompressed video data as OpenGL textures. For example, this source could be QuickTime, OpenGL, or your own proprietary video frame generator.

In each case, you need to create an OpenGL context to display the generated video. You pass this to your video source to indicate that this is where you want your video to be displayed.

Listing 2-3 shows a method that sets up a QuickTime movie to be your video source.

__Listing 2-3__  Initializing a QuickTime video source

```objc
- (id)initWithFilePath:(NSString*)theFilePath // 1
{
    self = [super init];

    OSStatus        theError = noErr;
    Boolean         active = TRUE;
    UInt32          trackCount = 0;
    OSType          theTrackType;
    Track           theTrack = NULL;
    Media           theMedia = NULL;

    QTNewMoviePropertyElement newMovieProperties[] = // 2
        {
        {kQTPropertyClass_DataLocation,
            kQTDataLocationPropertyID_CFStringNativePath,
            sizeof(theFilePath), &theFilePath, 0},
        {kQTPropertyClass_NewMovieProperty, kQTNewMoviePropertyID_Active,
            sizeof(active), &active, 0},
        {kQTPropertyClass_Context, kQTContextPropertyID_VisualContext,
            sizeof(qtVisualContext), &qtVisualContext, 0},
        };

    theError = QTOpenGLTextureContextCreate( NULL, NULL, // 3
        [[NSOpenGLView defaultPixelFormat]
         CGLPixelFormatObj], NULL, &qtVisualContext);

    if(qtVisualContext == NULL)
     {
        NSLog(@"QTVisualContext creation failed with error:%d", theError);
        return NULL;
    }

    theError = NewMovieFromProperties(
        sizeof(newMovieProperties) / sizeof(newMovieProperties[0]),// 4
        newMovieProperties, 0, NULL, &channelMovie);

    if(theError)
    {
        NSLog(@"NewMovieFromProperties failed with %d", theError);
        return NULL;
    }

    // setup the movie
    GoToBeginningOfMovie(channelMovie);// 5
    SetMovieRate(channelMovie, 1 << 16);
    SetTimeBaseFlags(GetMovieTimeBase(channelMovie), loopTimeBase);
    trackCount = GetMovieTrackCount(channelMovie);
    while(trackCount > 0)
    {
        theTrack = GetMovieIndTrack(channelMovie, trackCount);
        if(theTrack != NULL)
        {
            theMedia = GetTrackMedia(theTrack);
            if(theMedia != NULL)
            {
                GetMediaHandlerDescription(theMedia, &theTrackType, 0, 0);
                if(theTrackType != VideoMediaType)
                {
                    SetTrackEnabled(theTrack, false);
                }
            }
        }
        trackCount--;
    }

    return self;
}
```

Here is how the code works:

1. This method takes the file path of the QuickTime movie as its input parameter.
2. Sets up the movie properties array. These properties specify

   - the file path to the movie
   - whether or not the new movie should be active (yes, in this case)
   - the visual context to associate with this movie. The `qtVisualContext` variable is an instance variable of this method’s class.

   These properties are passed later to the `NewMovieFromProperties` function.
3. Creates an OpenGL texture context. This is the abstract destination into which OpenGL textures are drawn. The QuickTime function `QTOpenGLTextureContextCreate` requires you to pass in a CGLContext and a CGLPixelFormat object. In Cocoa, you can obtain these from the NSOpenGLContext and NSOpenGLPixelFormat objects created when you initialize OpenGL. In Carbon, you can obtain the underlying context and pixel format from the AGLContext and AGLPixelFormat objects using the AGL functions `aglGetCGLContext` and `aglGetCGLPixelFormat`.)

   This context, stored in the instance variable `qtVisualContext` is passed to `NewMovieFromProperties` to be the visual context into which QuickTime will draw its movies.
4. Creates the movie. The QuickTime function `NewMovieFromProperties`, available in OS X v10.4 and later, or QuickTime 7.0 and later, is the preferred way to instantiate movies.

   If you are using Cocoa, you can call the QTKit method `movieFromFile` instead.

   If for some reason you want to set or change the visual context after creating the movie, you can call the QuickTime function `SetMovieVisualContext`.
5. Performs various initializations on the movie. This section is mostly boilerplate code to start the movie at the beginning, at the normal frame rate, and in a continuous loop. The code also loops through the available tracks and turns off any non-video tracks.

When the display link is running, it periodically calls back to your application each time you should prepare a frame. Your callback function should obtain a frame from the designated video source as an OpenGL texture, and then output it to the screen.

If you are using object-oriented programming, you will probably want your callback to invoke a method, as shown in Listing 2-4 and Listing 2-5.

__Listing 2-4__  Invoking a method from your callback

```
CVReturn MyDisplayLinkCallback (
    CVDisplayLinkRef displayLink,
    const CVTimeStamp *inNow,
    const CVTimeStamp *inOutputTime,
    CVOptionFlags flagsIn,
    CVOptionFlags *flagsOut,
    void *displayLinkContext)
{
 CVReturn error =
        [(MyVideoView*) displayLinkContext displayFrame:inOutputTime];
 return error;
}
```

The callback function simply invokes the `displayFrame` method implemented in the `MyVideoView` class. An instance of this class is passed to your callback in the `displayLinkContext` parameter. (The `MyVideoView` class that displays your frames should be a subclass of `NSOpenGLView`, as shown in [Listing 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmzwfvbuqmrqgmwueqkcjfbusqsb).)

__Listing 2-5__  Implementing the displayFrame method

```objc
- (CVReturn)displayFrame:(const CVTimeStamp *)timeStamp
{
    CVReturn rv = kCVReturnError;
    NSAutoreleasePool *pool;

    pool = [[NSAutoreleasePool alloc] init];
    if([self getFrameForTime:timeStamp])
    {
        [self drawRect:NSZeroRect];
        rv = kCVReturnSuccess;
    }
    else
    {
       rv = kCVReturnError;
    }
    [pool release];
    return rv;
}
```

You obtain the frame for the specified time as an OpenGL texture. Listing 2-6 shows how you might implement the `getFrameForTime` method if you were obtaining your video frames from QuickTime. This example assumes that the method is part of a custom `MyVideoView` class.

__Listing 2-6__  Obtaining frames from QuickTime

```objc
- (BOOL)getFrameForTime:(const CVTimeStamp*)syncTimeStamp
{
    CVOpenGLTextureRef      newTextureRef = NULL;

    QTVisualContextTask(qtVisualContext);// 1
    if(QTVisualContextIsNewImageAvailable(qtVisualContext, syncTimeStamp))// 2
    {
        QTVisualContextCopyImageForTime(qtVisualContext, NULL, syncTimeStamp,// 3
                 &newTextureRef);

        CVOpenGLTextureRelease(currentFrame);// 4
        currentFrame = newTextureRef;

        CVOpenGLTextureGetCleanTexCoords (// 5
                    currentFrame, lowerLeft, lowerRight, upperRight, upperLeft);
        return YES; // we got a frame from QT
    }
    else
    {
        //NSLog(@"No Frame ready");
    }
    return NO;  // no frame available
}
```

Here is how the code works:

1. Gives time to the context, allowing it to perform any required housekeeping. You should call this function before obtaining each frame.
2. Checks to see if a new frame is available for the given time. The requested time, as passed to your callback by the display link, represents not the current time, but the time in the future when the frame will be displayed.
3. If a frame is available, obtain it as an OpenGL texture. The QuickTime function `QTVisualContextCopyImageForTime` lets you obtain a frame from QuickTime as any Core Video image buffer type.
4. Releases the current texture (stored in the instance variable `currentFrame`) and sets the newly acquired texture to replace it. You should release your OpenGL textures when you are through using them to minimize the likelihood of filling up video memory.
5. Obtains the coordinates of the clean aperture for the texture. In most cases, these are the texture bounds needed for rendering.

After you have acquired the frame from your video source, it is up to you to decide what to do with it. The frame is given to you as an OpenGL texture, so you can manipulate it with any OpenGL calls. Listing 2-7 shows how you could set up OpenGL to draw into the view bounds by overriding the standard NSView `drawRect` method.

__Listing 2-7__  Displaying OpenGL in a rectangle

```objc
- (void)drawRect:(NSRect)theRect
{
    [lock lock];    // 1
    NSRect      frame = [self frame];
    NSRect      bounds = [self bounds];

    [[self openGLContext] makeCurrentContext];// 2
    if(needsReshape)// 3
    {
        GLfloat     minX, minY, maxX, maxY;

        minX = NSMinX(bounds);
        minY = NSMinY(bounds);
        maxX = NSMaxX(bounds);
        maxY = NSMaxY(bounds);

        [self update];

        if(NSIsEmptyRect([self visibleRect])) // 4
        {
            glViewport(0, 0, 1, 1);
        } else {
            glViewport(0, 0,  frame.size.width ,frame.size.height);
        }
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        glOrtho(minX, maxX, minY, maxY, -1.0, 1.0);

        needsReshape = NO;
    }

    glClearColor(0.0, 0.0, 0.0, 0.0);
    glClear(GL_COLOR_BUFFER_BIT);

    if(!currentFrame)// 5
        [self updateCurrentFrame];
    [self renderCurrentFrame];      // 6
    glFlush();// 7
    [lock unlock];// 8
}
```

Here is how the code works:

1. Locks the current thread. OpenGL is not thread-safe, so you must make sure that only one thread can make OpenGL calls at any given time.
2. Sets OpenGL to render into this object’s context.
3. If the drawing rectangle has been resized, then take steps to update the size of the OpenGL context.
4. Maps the OpenGL context to the new bounds of the view, if the view is visible. If not, then map the context to be effectively invisible.
5. Obtains the current frame again if it does not already exist. This situation can occur if the `drawRect` method is invoked in response to a view resize.
6. Draws the current frame into the OpenGL context. `renderCurrentFrame` is the method that holds your custom frame code.
7. Flushes the drawing to the OpenGL renderer. The frame is then automatically displayed onscreen at the appropriate time.
8. Unlocks the thread after completing all OpenGL calls.

The `renderCurrentFrame` method contains the custom processing your application wants to apply to the frame. Listing 2-8 shows a simple example of how you can implement this method. This example uses Core Image to draw the frame into the OpenGL context.

__Listing 2-8__  Drawing a frame

```objc
- (void)renderCurrentFrame
{
    NSRect      frame = [self frame];

    if(currentFrame)
    {
        CGRect      imageRect;
        CIImage     *inputImage;

        inputImage = [CIImage imageWithCVImageBuffer:currentFrame];// 1

        imageRect = [inputImage extent];// 2
        [ciContext drawImage:inputImage // 3
                atPoint:CGPointMake(
                (int)((frame.size.width - imageRect.size.width) * 0.5),
                (int)((frame.size.height - imageRect.size.height) * 0.5))
                fromRect:imageRect];

    }
    QTVisualContextTask(qtVisualContext);// 4
}
```

Here is how the code works:

1. Creates a Core Image image from the current frame. The Core Image method `ImageWithCVImageBuffer` creates the image from any image buffer type (that is, a pixel buffer, OpenGL buffer, or OpenGL texture).
2. Obtains the bounding rectangle for the image.
3. Draws the image into a Core Image context. The Core Image method `drawImage:atPoint:fromRect` draws the frame in the specified visual context at a specified location.

   Before drawing, you must have created a Core Image context that references the same drawing space as the OpenGL context. Doing so allows you to draw into the space using Core Image APIs and then display it using OpenGL. For example, you could add the following code to [Listing 2-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmzwfvbuqmrqgmwugscbijauiski) after creating your OpenGL context :

```
/* Create CGColorSpaceRef */
CGColorSpaceRef colorSpace = CGColorSpaceCreateDeviceRGB();

/* Create CIContext */
ciContext = [[CIContext contextWithCGLContext:
                (CGLContextObj)[[self openGLContext] CGLContextObj]
                pixelFormat:(CGLPixelFormatObj)
                [[self pixelFormat] CGLPixelFormatObj]
                options:[NSDictionary dictionaryWithObjectsAndKeys:
                (id)colorSpace,kCIContextOutputColorSpace,
                (id)colorSpace,kCIContextWorkingColorSpace,nil]] retain];
CGColorSpaceRelease(colorSpace);
```

   See _[Core Image Programming Guide](../Core%20Image%20Programming%20Guide/About%20Core%20Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobv)_ for more information about creating Core Image contexts.
4. Gives time to the visual context to perform any required housekeeping. You should call `QTVisualContextTask` once each time through your drawing method.

If you want to apply filtering effects to your video, it is often simpler to apply a Core Image filter to them rather than try to implement your own image processing. To do so, you need to obtain your frame as a Core Image image.

You can load a Core Image filter using the Core Image CIFIlter method `filterWithName`:

```
effectFilter = [[CIFilter filterWithName:@"CILineScreen"] retain];
[effectFilter setDefaults];
```

This example loads the standard Core Image line screen filter, but you should use whatever is appropriate for your application.

After you have loaded the filter, you process your image with it in your drawing method. Listing 2-9 shows how you could apply a Core Image filter. This listing is identical to [Listing 2-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmzwfvbuqmrqgmwueqkci5ducr2e) except that it filters the input image before drawing it into the Core Image context.

__Listing 2-9__  Applying a Core Image filter to an image

```objc
- (void)renderCurrentFrameWithFilter
{
    NSRect      frame = [self frame];

    if(currentFrame)
    {
        CGRect      imageRect;
        CIImage     *inputImage, *outputImage;

        inputImage = [CIImage imageWithCVImageBuffer:currentFrame];

        imageRect = [inputImage extent];
        [effectFilter setValue:inputImage forKey:@"inputImage"];// 1
        [[[NSGraphicsContext currentContext] CIContext]// 2
            drawImage:[effectFilter valueForKey:@"outputImage"]
            atPoint:CGPointMake((int)
                ((frame.size.width - imageRect.size.width) * 0.5),
                (int)((frame.size.height - imageRect.size.height) * 0.5))
            fromRect:imageRect];

    }
    QTVisualContextTask(qtVisualContext);
}
```

Here is how the code works:

1. Sets the CIImage filter to apply to the frame.
2. Draws the image with the specified filter.

Keep in mind that the Core Image image is immutable; each time you obtain a frame, you must create a new image.

For more details about creating and using Core Image filters, see _[Core Image Programming Guide](../Core%20Image%20Programming%20Guide/About%20Core%20Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobv)_.

[Next](Glossary.md)[Previous](Core%20Video%20Concepts.md)

