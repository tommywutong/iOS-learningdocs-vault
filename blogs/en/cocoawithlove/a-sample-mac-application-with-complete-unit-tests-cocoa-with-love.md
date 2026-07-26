---
title: 'A sample Mac application with complete unit tests | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/12/sample-mac-application-with-complete.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:9aa21add006fa5f9'
translated: false
---

> 原文：[A sample Mac application with complete unit tests | Cocoa with Love](https://www.cocoawithlove.com/2009/12/sample-mac-application-with-complete.html)　·　Cocoa with Love (Matt Gallagher)

In this post, I present a complete Cocoa Mac application implemented with unit tests for all created code. I'll create the tests first and then only add the code required to make the tests pass, largely following a test-driven development (TDD) methodology.

Next week I'll show the configuration and implementation of this project as an iPhone application for the benefit of Cocoa Touch developers.

## Introduction

A few days ago, I spent some time searching for a Cocoa application with source code and full unit tests but I was only able to find Apple's trivial [iPhoneUnitTests sample project](http://developer.apple.com/IPhone/library/samplecode/iPhoneUnitTests/index.html).

With more than four years of official support (Apple added OCUnit to the Developer Tools in 2005) and a large number of articles and blog posts by Mac programmers endorsing unit testing and offering solutions to problems within unit testing, it is surprising to me that there are so few code examples showing Cocoa applications with full unit tests.

So I decided to re-implement one of my own projects ([the WhereIsMyMac application from an earlier post](https://www.cocoawithlove.com/2009/09/whereismymac-snow-leopard-corelocation.html)) with complete unit tests using a test-first approach — I'll create failing tests and only add code to the project to pass those failing tests.

I'll be cheating a bit relative to proper test-first development (since this is a re-implementation of an existing project, I already know what the final code should be) but I'll keep to the spirit of the process by only adding as much code as I need to make the tests pass.

I know people will want to see how this works on the iPhone but since this post is already large, I've deferred that implementation until next week.

## Xcode unit testing targets

There are two different ways of configuring Xcode for unit testing: logic test targets and application test targets.

- **Logic tests** — these are run in a executable that is separate from your application. The separate build can be easier to manage, faster to build and is easier to run objects in isolation since it avoids the application setup. However, you cannot test components which rely on the application (which is most user interface components). Generally, this type of test target is intended for libraries, frameworks and testing the back-end (model components of model-view-controller) of your application.

  Logic tests are easily run at build-time or from the command-line, which is helpful for continuous integration or automated test processes.
- **Application tests** — these tests let the application load first and are subsequently loaded into the existing application. This means that the full application environment is available to your tests. In many cases, controller tests and view tests need to be run as application tests since they are reliant on the full environment.

  Application tests allow your application to be tested in a more realistic environment, reducing the chance that environment or integration level issues will be missed. They are normally run as a separate step (not as part of the build) and therefore may be less convenient for tests that need to be run every time.

I'll focus exclusively on the second type of testing target, since it will allow full testing of the application.

It may seem strange to talk about "unit tests" which are supposed to be run in isolation but then talk about "Application tests" which provide the environment in which to run tests. The reality is that you can only isolate user-interface unit tests from your own code — there will always be some interaction (in hidden and not controllable ways) with the application framework code. Windows, views and controls simply won't work if there's no application around them.

## Mac project configuration

One of the best sources of information on configuring Xcode for Unit Tests is [Chris Hanson's series on unit testing](http://chanson.livejournal.com/119097.html). I'll follow many of the steps that he describes and further add OCMock integration to the procedure.

After you've created a blank project, use the "Project→New Target..." menu item to add a new "Cocoa→Unit Testing Bundle" Target to the project.

> **Note:** The testing target is a separate target. This means that you need to be careful of target membership. All application source files should be added to the application target only. Test code files should be added to the testing target only.

It'd be great if that's all that you needed but there's more.

First, drag your application's target onto the unit testing target to create a dependency (force the application to build before the unit tests).

Then edit the unit testing target's settings (Right click→Get Info) and set the "Build→Linking→Bundle Loader" for all configurations to:

```objc
$(CONFIGURATION_BUILD_DIR)/WhereIsMyMac.app/Contents/MacOS/WhereIsMyMac
```

where "WhereIsMyMac" is the name of the application you're unit testing. This will let the testing target link against the application (so you don't get linker errors when compiling).

Also set the "Build→Unit Testing→Test Host" to `$(BUNDLE_LOADER)` (this will give this property the same value as the above setting). This property lets the automated build-time script know to launch the application and inject the unit testing bundle into it to start the tests.

> **Logic tests note:** If you want to do logic tests instead of application tests, leave the Bundle Loader and Test Host fields empty and add all files you want to test to the test target (so the test target becomes a separate, self-contained target instead of linking against the main application).

Finally, [download a copy of OCMock](http://www.mulle-kybernetik.com/software/OCMock/), place the OCMock.framework in the same directory as your .xcodeproj file and set the "Build→Search Paths→Framework Search Paths" to:

- `"$(SDKROOT/Developer/Library/Frameworks"`
- `"$(SRCROOT)"`

Neither need to be recursive. The quotes are to handle potential spaces in your paths. The first search path will probably already exist in the settings but we add the second search path so that the OCUnit framework will be found in the project's directory.

The configuration so far will run all tests as a build step (the Cocoa Unit Testing target includes a Run Script build step that runs all the unit tests).

To allow debugging as well as build-time execution, add a new executable to the project ("Project→New Custom Executable...") with a path relative to the Build Product of:

```objc
WhereIsMyMac.app/Contents/MacOS/WhereIsMyMac
```

and in the custom application's settings (Right click→Get Info) on the Argument tab, set the arguments and environment variables as follows:

![](https://www.cocoawithlove.com/assets/objc-era/executable_settings.png)

Most of these settings configure the application to load our test bundle into itself when it runs. The `:$(SRCROOT)` at the end of fallback framework path is to allow the application to find the OCUnit framework in our project directory at runtime.

> **Separate executable**: since this test debugging executable is a separate executable, you will need to switch to the debugging executable for debugging tests and switch back when you want to run the application normally.

## AppDelegate Tests

### Startup integration

The application will start with the `WhereIsMyMacAppDelegate` and we'll use the the `WhereIsMyMacAppDelegate` to load the main window.

The first test is therefore to ensure that application's delegate is an instance of `WhereIsMyMacAppDelegate` on startup.

```objc
- (void)testAppDelegate
{
    id appDelegate = [[NSApplication sharedApplication] delegate];
    STAssertTrue([appDelegate isKindOfClass:[WhereIsMyMacAppDelegate class]],
        @"Cannot find the application delegate.");
}
```

This is a short and simple test but it isn't a unit test. It's actually an integration test (since it is testing the fully connected `+[NSApplication sharedApplication]` in place.

An ideal unit test would test the `NSApplication` in isolation and ensure that it creates and sets its delegate property correctly. This is infeasible since `NSApplication` can't be isolated so we simply accept the nature of the class and test the instance of `sharedApplication` that should be created on startup. Of course, unit testing `NSApplication` itself shouldn't be necessary but an integration test to ensure that the startup of the program leads correctly to the creation and setting of the `WhereIsMyMacAppDelegate` is still a good idea.

### applicationDidFinishLaunching:

The next test is to ensure that `applicationDidFinishLaunching:` on the delegate will:

1. create the `WhereIsMyMacWindowController` and set it on the delegate
2. load the `WhereIsMyMacWindowController`'s window
3. make the `WhereIsMyMacWindowController`'s window the main and key window

```objc
- (void)testApplicationDidFinishLaunching
{
    WhereIsMyMacAppDelegate *appDelegate =
        [[[WhereIsMyMacAppDelegate alloc] init] autorelease];

    id mockWindow = [OCMockObject mockForClass:[NSWindow class]];
    [[mockWindow expect] makeKeyAndOrderFront:appDelegate];

    mockWindowController = [OCMockObject mockForClass:[WhereIsMyMacWindowController class]];
    [[[mockWindowController expect] andReturn:mockWindow] window];
    NSUInteger preRetainCount = [mockWindowController retainCount];

    [appDelegate applicationDidFinishLaunching:nil];
    
    [mockWindowController verify];
    [mockWindow verify];
    
    NSUInteger postRetainCount = [mockWindowController retainCount];
    STAssertEquals(postRetainCount, preRetainCount + 1, @"Window controller not retained");

    id windowController;
    object_getInstanceVariable(appDelegate, "windowController", (void **)&windowController);
    STAssertEqualObjects(windowController, mockWindowController,
        @"windowController not set on appDelegate");

    object_setInstanceVariable(appDelegate, "windowController", nil);
    mockWindowController = nil;
}
```

This test is a near perfectly decoupled unit test of the `-[WhereIsMyMacAppDelegate applicationDidFinishLaunching:]` method. However, the approaches used to decouple it from the rest of the program probably make it tricky to understand.

The first two lines create a clean `WhereIsMyMacAppDelegate` to test.

The second two lines create a mock `NSWindow` that we use to check that the window is brought to the front by `makeKeyAndOrderFront:`. In conjunction with the later `[mockWindow verify]` this will test the 3rd requirement in the list above.

The next three lines create a `WhereIsMyMacWindowController` that will be swapped in place of any `WhereIsMyMacWindowController` that the `appDelegate` tries to create (more on how this works in the next paragraph). The `mockWindowController` is told to expect `window` to be invoked and when it does, will return the `mockWindow`. In conjunction with the `[mockWindowController verify]`, the retain count checks and the `STAssertEqualObjects` will verify the first two requirements in the list.

I mentioned that `mockWindowController` will be substituted in place of a real `WhereIsMyMacWindowController` any time the `appDelegate` tries to create a `WhereIsMyMacWindowController`. This works because `mockWindowController` is a global variable that affects the following category:

```objc
id mockWindowController = nil;

@implementation WhereIsMyMacWindowController (WhereIsMyMacAppDelegateTests)

- (id)init
{
    if (mockWindowController)
    {
        [self release];
        return mockWindowController;
    }
    
    return invokeSupersequent();
}

@end
```

This category overrides the `-[WhereIsMyMacWindowController init]` method to return the `mockWindowController` if it exists, otherwise the default behavior. The `invokeSupersequent()` comes from my old [Supersequent implementation](https://www.cocoawithlove.com/2008/03/supersequent-implementation.html) post (it's like invoking the `super` method but will invoke the current class' base or earlier category implementation, not just a genuine `super` method and is more flexible — though slower — than method swizzling).

Of course, we only want this override to return the mock object at specific times. This is why the `mockWindowController` must be explicitly set back to `nil` at the end of the method.

> **Notice that the category overrides init, not alloc:** technically, overriding `alloc` would prevent any method being invoked on `WhereIsMyMacWindowController` (making the test perfectly decoupled from other classes) however this would mean that we'd need to invoke `init` on the mock object and `OCClassMockObject` does not let you mock any methods that it implements for itself (this includes all of the `NSProxy` methods plus `initWithClass:` and `mockedClass`). So instead, we override `init` and make the acceptable tradeoff to allow `+[WhereIsMyMacWindowController alloc]` to be invoked.  
>   
> A related point is that `OCClassMockObject` can't mock `retain` or `release`. This is why manual checks on the `retainCount` are used instead of asking the mock object to expect a `retain`. If you expect `autorelease` to be used instead of `release`, you'd need to wrap the tested method invocation in an `NSAutoreleasePool` to flush the `autorelease` before testing the `retainCount`.

A final point about this test: it uses `object_getInstanceVariable` and `object_setInstanceVariable` to get the `windowController` from the `appDelegate` instead of the property accessor. The reason for this is that `object_getInstanceVariable` directly reads the value from the object without invoking any accessor methods that might have secondary effects. Some code presented elsewhere uses `valueForKey:` to achieve the same effect but the problem with this is that `valueForKey:` will use the `window` getter method if it exists — we want to directly test that the actual instance variable is set on the class without interference.

### applicationWillTerminate:

The final tests for the `WhereIsMyMacAppDelegate` are for the `applicationWillTerminate:` method. This method should close window and release it.

```objc
- (void)testApplicationWillTerminate
{
    WhereIsMyMacAppDelegate *appDelegate =
        [[[WhereIsMyMacAppDelegate alloc] init] autorelease];
    
    id mockWindowController = [OCMockObject mockForClass:[WhereIsMyMacWindowController class]];
    [mockWindowController retain];
    object_setInstanceVariable(appDelegate, "windowController", mockWindowController);
    
    NSUInteger preRetainCount = [mockWindowController retainCount];
    [[mockWindowController expect] close];

    [appDelegate applicationWillTerminate:nil];
    
    [mockWindowController verify];

    NSUInteger postRetainCount = [mockWindowController retainCount];
    STAssertEquals(postRetainCount, preRetainCount, @"Window controller not released");

    id windowController;
    object_getInstanceVariable(appDelegate, "windowController", (void **)&windowController);
    STAssertNil(windowController, @"Window controller property not set to nil");
}
```

After creating an `appDelegate` to test, this method creates a mock `WhereIsMyMacWindowController`, tells it to expect a `close` invocation, sets it as the `windowController` on the `appDelegate` to this new mock object, invokes `applicationWillTerminate:` on the `appDelegate`, verifies that the `close` method was invoked, ensures that the `retainCount` is decremented by one and that the `windowController` instance variable is set to `nil`.

That's three failing tests. One is more of an integration test than a unit test (since it relies on the `NSApplcation` operating in place) but the others are genuine isolated unit tests on the `WhereIsMyMacAppDelegate`. The implementation to pass these tests is less interesting but you can have a look at the sample project to see how I added code to pass these tests.

## Window Controller Tests

### loadWindow integration

As with the application delegate, the first test is an integration test. We need to test that the `loadWindow` method will load the required user interface elements from files in the bundle. This is similar to [Chris Hanson's "Trust by verify" approach](http://chanson.livejournal.com/148204.html) except that I test the loading of the window separately from the `windowDidLoad` and `window` methods.

```objc
- (void)testLoadWindow
{
    [windowController loadWindow];

    WebView *webView;
    object_getInstanceVariable(windowController, "webView", (void **)&webView);
    CLLocationManager *locationManager;
    object_getInstanceVariable(windowController, "locationManager", (void **)&locationManager);
    NSTextField *locationLabel;
    object_getInstanceVariable(windowController, "locationLabel", (void **)&locationLabel);
    NSTextField *accuracyLabel;
    object_getInstanceVariable(windowController, "accuracyLabel", (void **)&accuracyLabel);
    NSButton *openInBrowserButton;
    object_getInstanceVariable(windowController, "openInBrowserButton", (void **)&openInBrowserButton);
    
    STAssertTrue([windowController isWindowLoaded], @"Window failed to load");
    STAssertNotNil(webView, @"webView ivar not set on load");
    STAssertNotNil(locationLabel, @"locationLabel ivar not set on load");
    STAssertNotNil(accuracyLabel, @"accuracyLabel ivar not set on load");
    STAssertNotNil(openInBrowserButton, @"openInBrowserButton ivar not set on load");
    STAssertEqualObjects(windowController, [openInBrowserButton target],
        @"openInBrowserButton button doesn't target window controller");
    STAssertTrue([openInBrowserButton action] == @selector(openInDefaultBrowser:),
        @"openInBrowserButton button doesn't invoke openInDefaultBrowser:");
}
```

The `windowController` is a fixture that's allocated in the `setUp` method. The majority of this method then gets the instance variables from the `windowController` after the `loadWindow` method is invoked and tests that the required properties are all set.

We can now test the `windowDidLoad` method as a separate step to the `loadWindow`. The `windowDidLoad` should create a `CLLocationManager` object, set the window controller as the `delegate` and start location updates.

### windowDidLoad

```objc
- (void)testWindowDidLoad
{
    mockLocationManager = [OCMockObject mockForClass:[CLLocationManager class]];
    [[mockLocationManager expect] setDelegate:windowController];
    [[mockLocationManager expect] startUpdatingLocation];

    [windowController windowDidLoad];

    [mockLocationManager verify];
    
    object_setInstanceVariable(windowController, "locationManager", nil);
    mockLocationManager = nil;
}
```

This uses the same category override approach that was used in the `testApplicationDidFinishLaunching` method to swap in a mock `CLLocationManager` and ensure that the appropriate methods are invoked.

### locationManager:didUpdateToLocation:fromLocation:

Next step: verify that the correct Google Maps location is loaded in the `WebView`'s `mainFrame` when a given coordinate is passed to the `WhereIsMyMacWindowController` implementation of the `-[CLLocationManagerDelegate locationManager:didUpdateToLocation:fromLocation:]` method.

This test method is pretty big but the essence is that:

- The web view and its main frame are mocked.
- The main frame is told to expect specific a specific HTML string that's loaded from a pre-created file.
- The method is then passed the exact location that should trigger that HTML string.
- The mock web frame is then asked to verify that the expected HTML string was loaded.
- The window's labels are also tested to ensure they receive the correct values.

```objc
- (void)testUpdateToLocation
{
    NSString *htmlString =
        [NSString 
            stringWithContentsOfFile:
                [[NSBundle bundleWithIdentifier:@"com.yourcompany.UnitTests"]
                    pathForResource:@"WebPageTestContent" ofType:@"html"]
            encoding:NSUTF8StringEncoding
            error:NULL];
    id mockWebView = [OCMockObject mockForClass:[WebView class]];
    id mockWebFrame = [OCMockObject mockForClass:[WebFrame class]];
    [[[mockWebView stub] andReturn:mockWebFrame] mainFrame];
    [[mockWebFrame expect]
        loadHTMLString:htmlString
        baseURL:nil];
    object_setInstanceVariable(windowController, "webView", mockWebView);

    NSTextField *locationLabel = [[[NSTextField alloc] init] autorelease];
    NSTextField *accuracyLabel = [[[NSTextField alloc] init] autorelease];
    object_setInstanceVariable(windowController, "locationLabel", locationLabel);
    object_setInstanceVariable(windowController, "accuracyLabel", accuracyLabel);

    CLLocationCoordinate2D coord;
    coord.longitude = 144.96326388;
    coord.latitude = -37.80996889;
    CLLocation *location =
        [[[CLLocation alloc]
            initWithCoordinate:coord
            altitude:0
            horizontalAccuracy:kCLLocationAccuracyBest
            verticalAccuracy:kCLLocationAccuracyHundredMeters
            timestamp:[NSDate date]]
        autorelease];
    
    [windowController
        locationManager:nil
        didUpdateToLocation:location
        fromLocation:nil];
    [windowController
        locationManager:nil
        didUpdateToLocation:location
        fromLocation:location];
    
    [mockWebFrame verify];
    
    STAssertEqualObjects(
        ([locationLabel stringValue]),
        ([NSString stringWithFormat:@"%f, %f", coord.latitude, coord.longitude]),
        @"Location label not set.");
    STAssertEqualObjects(
        ([accuracyLabel stringValue]),
        ([NSString stringWithFormat:@"%f", kCLLocationAccuracyBest]),
        @"Location label not set.");
}
```

An interesting point to notice here is that the `WebPageTestContent` file is loaded from a bundle that isn't the `mainBundle`. This is because the test resides in the `UnitTests.octest` bundle, not the application's bundle (which is the "main" bundle).

### locationManager:didFailWithError: and openInDefaultBrowser:

I'll leave out the code for the `locationManager:didFailWithError:` test — it's largely the same as the previous test but with a different HTML string to load in the web view's main frame. You can see it in the downloaded project if you wish.

Similarly, `openInDefaultBrowser:` is just a URL, generated from the current location and sent to the shared `NSWorkspace` (which we mock through category overrides) so the test contains largely the same elements — so I'll omit the code for this test too. Again, check the downloaded project if you're interested.

### dealloc:

All that remains is to create tests for the `dealloc` method to ensure that the `locationManager` receives a `stopUpdatingLocation` and a `release` message.

```objc
- (void)testDealloc
{
    id mockLocationManager = [OCMockObject mockForClass:[CLLocationManager class]];
    NSUInteger preRetainCount = [mockLocationManager retainCount];
    [mockLocationManager retain];
    object_setInstanceVariable(windowController, "locationManager", mockLocationManager);
    
    [[mockLocationManager expect] stopUpdatingLocation];

    [windowController dealloc];
    
    [mockLocationManager verify];

    NSUInteger postRetainCount = [mockLocationManager retainCount];
    STAssertEquals(postRetainCount, preRetainCount, @"Location manager not released");
    
    windowController = nil;
}
```

Notice that we have to set `windowController` to `nil` at the end. This is because invoking `dealloc` on the `windowController` fixture has deallocated it and we need to ensure that the `tearDown` method doesn't try to invoke `release` on it.

Six failing tests for the `WhereIsMyMacWindowController`. You can look at the downloadable project to see the code added to pass these tests.

## Conclusion

> Download the complete [WhereIsMyMac-WithUnitTests.zip](https://www.cocoawithlove.com/assets/objc-era/WhereIsMyMac-WithUnitTests.zip) (139kb).  
>   
> **Warning:** Custom executables (like the _UnitTestWhereIsMyMac_ discussed in this post) are part of user data in the project file. If you make changes that you want to share with someone else, you will need to rename the _(your username).pbxuser_ file in the .xcodeproj bundle to _default.pbxuser_ (so that it applies to all users).  
>   
>  This project includes [OCMock.framework](http://www.mulle-kybernetik.com/software/OCMock/), which is Copyright (c) 2004-2009 by Mulle Kybernetik. OCMock is covered by its own license (contained in the _OCMock.framework/Versions/A/Resources/License.txt_ file).

In this post, I created a Mac project, created unit tests for all required functionality (plus two integration tests) and ultimately added code to make the project pass those tests. I've shown the configuration required for unit testing targets in Xcode and the implementation of the tests themselves, which show how to isolate units of a program (using mock objects and category overrides) for properly decoupled unit testing.

Unit tests for all created code does not mean that the project is "fully tested". There are lots of aspects associated with integration, runtime and memory behaviors, user events and the behaviors of the Cocoa frameworks that are not covered by these tests. Of course, this is the limit of "unit testing" for classes that operate in an application framework — to test these other aspects requires different kinds of tests.

Next week, I'll be presenting the same post developed for the iPhone. I apologize that this will result in two posts that almost the same but there are enough differences between the two that I couldn't squeeze both into a reasonable sized post. I also hope that by separating the posts, the result will be easier for dedicated Mac or iPhone programmers to follow.

Finally, a disclaimer: please don't consider the existence of this post as a recommendation that you should necessarily write your applications with full unit tests. It is important to look at the work involved and weigh the associated time costs and against your project's need for unit level validation. There are alternative approaches for maintaining code quality that have different associated costs and benefits which I hope to discuss and compare in a later post.
