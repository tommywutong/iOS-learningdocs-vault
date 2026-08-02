---
title: QuickTime Initialization Guide
apple_id: TP40001435
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/Conceptual/QT_InitializingQT/InitializingQT/InitializingQTfinal.html
archived_at: '2026-07-18T02:04:19.211175Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [QuickTime Initialization Guide](Introduction%20to%20QuickTime%20Initialization%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%20QuickTime%20Initialization%20Guide.md)

# Initializing QuickTime

QuickTime must be initialized before applications or components can make calls to the QuickTime Movie Toolbox.

If you are writing a threaded application, and intend to call QuickTime functions from multiple threads, you need to initialize QuickTime for each worker thread explicitly.

Windows applications must initialize the QuickTime Media Layer (QTML), prior to initializing QuickTime itself. This also serves to verify that QuickTime for Windows is installed.

As part of the initialization process, it is usually advisable to check the installed version of QuickTime to ensure that all required features are present on the user’s machine. This can also serve as a method to verify that QuickTime is installed prior to initializing it.

If your application runs on a Windows operating system, you need to verify that QuickTime is installed and initialize the QuickTime Media Layer (QTML). A single call to `InitializeQTML` does both. [Listing 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimzvfuzc2u2xge) shows the call to `InitializeQTML`.

__Listing 2-1__  Calling InitializeQTML

```

static void QuickTimeQTML (void)
{
  OSErr err;

    err = InitializeQTML(0L);
    CheckError (err, "InitializeQTML error" );
}
```

Use the `InitializeQTML` function to initialize QuickTime before calling any other QuickTime function. It is recommended that you call `InitializeQTML` at the very beginning of your program, in your `WinMain` function, before creating your main window.

`InitializeQTML` supports flags that allow you to specify how QuickTime should behave. For example, you can tell QuickTime to operate exclusively in full-screen mode, or to use the Windows Graphics Device Interface (GDI) for all drawing, rather than the DirectDraw or DCI services.

If QuickTime is not installed, the `InitializeQTML` function is not available and an error is returned.

If your application is distributed on a CD, you should include QuickTime installers on the disc and run the Windows installer if QuickTime is not present. (Including the installer requires a license from Apple, but there is currently no fee for such a license. To obtain a license, click the QuickTime link at [http://developer.apple.com/softwarelicensing/agreements/quicktime.html](https://developer.apple.com/softwarelicensing/agreements/quicktime.html) and follow the instructions there.) Alternatively, you may prompt the user to download QuickTime at [http://www.apple.com/quicktime/download/](http://www.apple.com/quicktime/download/).

If you are writing a routine that does not know whether `InitializeQTML` has already been called, call `InitializeQTML` at the beginning of the routine and `TerminateQTML` at the end.

It does no harm to call `InitializeQTML` more than once, as long as each call is nested with a matching call to `TerminateQTML`. If this function has already been called, subsequent calls do nothing except increment a counter. Calls to `TerminateQTML` just decrement the counter (if it is nonzero). Only the first nested call and the last nested call to `TerminateQTML` do any actual work, so there is no penalty for having multiple nested calls.

Once the QuickTime Media Layer has been initialized, Windows programmers should follow the same steps that Mac OS programmers follow to test the QuickTime version and initialize QuickTime itself.

Your application may want to check the version of QuickTime installed on the user’s system at runtime, to determine if all the needed features are supported. You should do this before initializing QuickTime.

To get the version of QuickTime installed on the user’s computer, call the `Gestalt` function (the necessary parts of which are included in QuickTime for Windows). The `Gestalt` function returns the QuickTime version if the appropriate selectors are passed in, as shown in [Listing 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimzvfuzc2u2xgq).

__Listing 2-2__  Getting the QuickTime version with Gestalt

```
{
    /* check the version of QuickTime installed */

    long version;
    OSErr result;

    result = Gestalt(gestaltQuickTime,&version);
    if ((result == noErr) && (version >= 0x05020000))
    {
        /* we have version 5.0.2 or later */
    }
}
```


Your application initializes a working QuickTime environment by calling `EnterMovies`.

```
    EnterMovies();
```

If you are writing a routine that does not know whether QuickTime has already been initialized, go ahead and call `EnterMovies`; repeated calls do no harm.

You do not need to balance calls to `EnterMovies` with calls to `ExitMovies`. Call `ExitMovies` only if you are done using QuickTime and want to free the resources as soon as possible without terminating your application. `ExitMovies` is called automatically when your application quits.

Windows users need to initialize QTML before calling `EnterMovies`, as shown in [Listing 2-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimzvfuzc2u2xgu).

__Listing 2-3__  Initializing QTML and QuickTime for Windows

```

static void InitQTMLandQuickTime (void)
{
  OSErr err;

    err = InitializeQTML(0L);
    CheckError (err, "InitializeQTML error" );
    EnterMovies();
}
```

`EnterMovies` initializes a single, non-reentrant QuickTime environment for your application.

If your application uses QuickTime on multiple threads simultaneously, call `EnterMoviesOnThread` from each thread that uses QuickTime to create a local QuickTime environment for that thread (requires QuickTime 6 or later).

For more information about threaded programming and QuickTime, see Technical Note TN2125, [Thread-safe programming in QuickTime.](https://developer.apple.com/technotes/tn/tn2125.html)

[Next](Document%20Revision%20History.md)[Previous](Introduction%20to%20QuickTime%20Initialization%20Guide.md)

