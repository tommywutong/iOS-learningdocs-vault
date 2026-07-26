---
title: The App Launch Sequence on iOS
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/06/app-launch-sequence-ios/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:15f92b7b9e1174b8'
translated: false
---

> 原文：[The App Launch Sequence on iOS](https://oleb.net/blog/2011/06/app-launch-sequence-ios/)　·　Ole Begemann

# The App Launch Sequence on iOS

**Update February 9, 2012:** Apple made some changes to the app launch sequence in the default project templates in Xcode 4.2. For that reason, [I revisited this topic in a new article](https://oleb.net/blog/2012/02/app-launch-sequence-ios-revisited/). Please refer to the new post for up-to-date information.

I noticed that many beginning iOS developers see the launch process of an iOS app as a bit of a mystery. Somehow, someone sends our application delegate an `application:didFinishLaunchingWithOptions:` message, seemingly the first place where we have chance to inject code of our own. But how does our app get there?

# In the beginning was `main()`

The execution of every C program starts with a function called `main()`, and since Objective-C is a strict superset of C, the same must be true for an Objective-C program. If you create a new iOS project from one of the default templates, Xcode places this function in a separate file called `main.m` in the _Supporting Files_ group. Usually, you never have to look at that file but let’s do. This is the entire code of `main()`:

```
int main(int argc, char *argv[])
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    int retVal = UIApplicationMain(argc, argv, nil, nil);
    [pool release];
    return retVal;
}
```

The function’s arguments `argc` and `argv` contain info about the command-line arguments passed to the executable on launch. We can safely ignore them for this discussion. Let’s have a look at what the function does, which seems to be very litte:

1. call would fail).
2. . We will take a deeper look at it below.
3. It drains the autorelease pool it just created.
4. to its caller (which is the shell that launched the executable).

When an (Objective-)C program reaches the end of `main()`, it ends. So this looks like a very short program indeed. Nevertheless, this is how all iOS apps work, so the secret must be the `UIApplicationMain()` function. Should it ever return, our program would end immediately.

# `UIApplicationMain()`

Looking at the documentation for `UIApplicationMain()`, we find this:

> This function instantiates the application object from the principal class and and instantiates the delegate (if any) from the given class and sets the delegate for the application. It also sets up the main event loop, including the application’s run loop, and begins processing events. If the application’s `Info.plist` file specifies a main nib file to be loaded, by including the `NSMainNibFile` key and a valid nib file name for the value, this function loads that nib file.

> Despite the declared return type, this function never returns.

Let’s take this apart step by step:

![App Launch Sequence on iOS 4](https://oleb.net/media/ios-4-app-launch-flow.png)

<sub>Flowchart of the app launch sequence on iOS 4. Feel free to share this image under a [Creative Commons Attribution license](http://creativecommons.org/licenses/by/3.0/) (CC-BY).</sub>

1. First, the function creates the main application object (step 3 in the flowchart). If you specify `nil` as the third argument to `UIApplicationMain()` (the default), it will create an instance of `UIApplication` in this step. This is usually what you want. However, if you need to subclass `UIApplication` (for example, to override its event handling in `sendEvent:`), you have to pass a string with the name of your subclass to `UIApplicationMain()`.
2. The function then looks at its fourth argument. If it is non-nil, it interprets it as the name of the class for the application delegate, instantiates an object of this class and assigns it as the application object’s `delegate`. The default for the fourth argument is `nil`, though, which signifies that the app delegate will be created in the main NIB file.
3. Next, `UIApplicationMain()` loads and parses your app’s `Info.plist` (step 4). If it contains a key named “Main nib file base name” (`NSMainNibFile`), the function will also load the NIB file specified there (step 5).
4. By default, the main NIB file is called `MainWindow.nib`. It contains at least an object representing the application delegate, connected to the File’s Owner’s `delegate` outlet (step 6), and a `UIWindow` object that will be used as the app’s main window, connected to an outlet of the app delegate. If you used a view-controller-based app template, the NIB file will also contain your app’s root view controller and possibly one or more view child controllers.

  It is worth mentioning that this is the only step where the UIKit-based app templates (Window-based, View-based, Navigation-based, Tab-based, etc.) differ significantly from each other. If you started out with a view-based app and later want to introduce a navigation controller, there is no need to start a new project: simply replace the root view controller in the main NIB file and adjust one or two lines of code in the app delegate. I noticed that many newbies to the iOS platform struggle with this problem and assume a huge difference between the different project templates. There isn’t.
5. Now, `UIApplicationMain()` creates the application’s run loop that is used by the `UIApplication` instance to process events such as touches or network events (step 7). The run loop is basically an infinite loop that causes `UIApplicationMain()` to never return.
6. Before the application object processes the first event, it finally sends the well-known `application:didFinishLaunchingWithOptions:` message to its delegate, giving us the chance to do our own setup (step 8). The least we have to do here is put our main window on the screen by sending it a `makeKeyAndVisible` message.

# Entry points

You see, there is no magic here. Besides `application:didFinishLaunchingWithOptions:`, there are several more entry points for custom code during the launch sequence (none of which are usually needed):

- before

  is called.
- method of a custom

  subclass.
- or

  methods of our application delegate if it is created from a NIB file (the default).
- methods of our application delegate class or a custom

  subclass. Any class receives an

  message before it is sent its first message from within the program.

Note that this sequence only happens at the actual _launch_ of an app. If the app is already running and simply brought back from the background, none of this occurs.
