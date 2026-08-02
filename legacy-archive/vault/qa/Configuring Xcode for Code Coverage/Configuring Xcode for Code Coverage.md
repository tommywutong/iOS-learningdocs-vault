---
title: Configuring Xcode for Code Coverage
apple_id: DTS10004232
resource_type: QA
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2014-03-12'
source_url: https://developer.apple.com/library/archive/qa/qa1514/_index.html
archived_at: '2026-07-18T02:31:55.333596Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1514

# Configuring Xcode for Code Coverage

## Q:  How can I configure my Xcode project to work with the GCOV code coverage tool?

A: Code Coverage allows you to identify what parts of your source code were executed during a test. Xcode supports code coverage testing with `GCOV` for iOS and OS X applications. When set up for GCOV use, Xcode generates .gcno files when compiling your app and .gcda data files when your app exits. The following steps show you how to set up your project in Xcode to generate these GCOV files.

1. Create a separate build configuration named `GCov_Build`.

   To keep your code coverage build separate from your Debug and Release, make a new build configuration named `GCov_Build` by duplicating Debug. See [Add a Build Configuration](https://developer.apple.com/library/ios/recipes/xcode_help-project_editor/Articles/BasingBuildConfigurationsonConfigurationFiles.html#//apple_ref/doc/uid/TP40010155-CH13-SW1) for more information about duplicating a build configuration.
2. Configure your application to work with `GCOV` at the project-level.

   Navigate to the Build Settings pane of your project, then update your settings for `GCov_Build` as follows:

   - Make sure that `Compiler for C/C++/Objective-C` is set to a version of `Apple LLVM Compiler`.
   - Make sure that `Generate Debug Symbols` is set to `YES`.
   - Set  `Generate Test Coverage Files` to `YES`.
   - Set  `Instrument Program Flow` to `YES`.

__Figure 1__  Build settings required for code coverage

!!

1. Compile your project to generate .gcno files.

   First set up your scheme to use `GCov_Build` when building and running your application as shown in Figure 2, then select Product > Build to compile your project. The compiler will create .gcno files in your build folder. Use the Projects organizer in Xcode to navigate to your application derived data's folder, then search within the Build/Intermediates directory for your .gcno files.

__Figure 2__  Set your scheme to use GCov_Build

!!

1. Run your application to generate .gcda files.

   Select Product > run to run your application. As your application runs, Xcode collects data about what parts of your code are used. It is important to give inputs to the application that will exercise the code you want to test. Xcode will write out the coverage data to .gcda files when your application exits.

   - OS X developers must use their application's Quit menu item to completely exit it.
   - iOS applications do not exit. Therefore, iOS developers should temporarily modify their application to force coverage data to be written out to .gcda files. Use any of the following methods to do so:

     - Set the `UIApplicationExitsOnSuspend` key to YES in your Info.plist file and send your running application to the background by pressing the home button.
     - Add a call to __gcov_flush() in your application to force the coverage data to be written out to .gcda files. For instance, you may want to insert a call to __gcov_flush() in `applicationDidEnterBackground:` as shown in Listing 1 to write out coverage information every time the home button is pressed.

       __Listing 1__  Using __gcov_flush() to force coverage data to be written out to .gcda files

```objc
#import "AppDelegate.h"
#include <stdio.h>

extern void __gcov_flush();
@implementation AppDelegate

- (void)applicationDidEnterBackground:(UIApplication *)application
{
  __gcov_flush();
}

…..
@end
```

1. Retrieve .gcda files.

   The .gcda files are usually placed in the same build directory containing your .gcno files. However, if your application is sandboxed, then you may not be able to write to this build directory. You can workaround this issue by using the `GCOV_PREFIX_STRIP` and `GCOV_PREFIX` environment variables to change the location of your .gcda files. `GCOV_PREFIX_STRIP` specifies the number of path components to be removed from the default build directory and `GCOV_PREFIX` specifies a path to substitute in their place.

   For instance, if your build directory is located at “/Users/Me/Library/Developer/Xcode/DerivedData/<application>/build” and you want to write it to your app's Documents directory, then first query the actual path of your app's sandbox, next assign this path to `GCOV_PREFIX` using the [setenv()](https://developer.apple.com/library/ios/documentation/System/Conceptual/ManPages_iPhoneOS/man3/setenv.3.html) function as follows:


```
NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
NSString *documentsDirectory = [paths objectAtIndex:0];
setenv("GCOV_PREFIX", [documentsDirectory cStringUsingEncoding:NSUTF8StringEncoding], 1);
```

   and finally set `GCOV_PREFIX_STRIP` to 7 to strip your app's full path as shown in Figure 3.

__Figure 3__  Setting GCOV_PREFIX_STRIP in Xcode

!!

After that the .gcda files are written to your app sandbox, copy them into the same directory containing your .gcno files. iOS developers should follow steps described in [Copying App Data from a Container on an iOS Device](https://developer.apple.com/library/ios/recipes/xcode_help-devices_organizer/articles/copy_app_data_from_sandbox.html#//apple_ref/doc/uid/TP40010392-CH14-SW1) to retrieve .gcda files from their devices. OS X developers should navigate to their app’s sandbox container (`~/Library/Containers/<bundle_id>`) on their Mac to retrieve these files.

__Figure 4__  Viewing .gcda files on an iOS device

!!

1. Use GCOV to view your results.

   Navigate to the directory containing both your .gcno and .gcda files in the Terminal application, then run the [gcov](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/gcov.1.html) tool on each source file for which you want to see the coverage data as seen in Listing 2.

   __Listing 2__  Running gcov on a source file

```shell
$ cd <path/to/directory with .gcda and .gcno files>
$ls
AppDelegate.d				MyApplication_dependency_info.dat	main.d
AppDelegate.dia				ViewController.d			main.dia
AppDelegate.gcda			ViewController.dia			main.gcda
AppDelegate.gcno			ViewController.gcda			main.gcno
AppDelegate.o				ViewController.gcno			main.o
MyApplication.LinkFileList		ViewController.o

$ xcrun gcov </path/to>/MyApplication/MyApplication/ViewController.m
File '</path/to>/MyApplication/MyApplication/ViewController.m'
Lines executed:69.23% of 13
</path/to>/MyApplication/MyApplication.m:creating 'ViewController.m.gcov'

$ cat ViewController.m.gcov
        -: 0:Source:</path/to>/MyApplication/MyApplication/ViewController.m
        -: 0:Graph:ViewController.gcno
        -: 0:Data:ViewController.gcda
        -: 0:Runs:0
        -: 0:Programs:0
        -: 1:
        -: 2:#import "ViewController.h"
        -: 3:
        -: 4:@interface ViewController ()
        1: 5:@property (strong) NSMutableArray *menuArray;
        -: 6:@end
        -: 7:
    #####: 8:@implementation ViewController
        -: 9:
        -: 10:
        1: 11:- (void)viewDidLoad
        -: 12:{
        1: 13: [super viewDidLoad];
        1: 14: [self loadData];
        1: 15:}
        -: 16:
        1: 17:-(void)loadData
        -: 18:{
        1: 19: NSString *plistPath = [[NSBundle mainBundle] pathForResource:@"Menu" ofType:@"plist"];
        1: 20: self.menuArray = [NSMutableArray arrayWithContentsOfFile:plistPath];
        -: 21:
        1: 22:}
        -: 23:
        -: 24:
    #####: 25:- (void)didReceiveMemoryWarning
        -: 26:{
    #####: 27: [super didReceiveMemoryWarning];
        -: 28: // Dispose of any resources that can be recreated.
    #####: 29:}
        -: 30:
        -: 31:@end
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-03-12 | Updated for Xcode 5. Was previously titled as "Using GCOV from Xcode." |
| 2007-02-23 | New document that illustrates how to set up Xcode for code coverage. |

