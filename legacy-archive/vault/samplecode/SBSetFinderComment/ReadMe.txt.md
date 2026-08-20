---
title: SBSetFinderComment
apple_id: DTS10004535
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: ScriptingBridge
published: '2011-07-14'
source_url: https://developer.apple.com/library/archive/samplecode/SBSetFinderComment/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:22:27.033819Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SBSetFinderComment](SBSetFinderComment.md)


[Next](main.m.md)[Previous](SBSetFinderComment.md)

# ReadMe.txt

```objc
SBSetFinderComment
==================

ABOUT:

This file details the steps involved in putting together a project that uses Scripting Bridge to send Apple events to the Finder application for the purposes of setting and getting comments assigned to files and folders.  

1. Start with a new Cocoa application.

In this sample we're going to target the Finder application so we'll call our sample 'SBSetFinderComment'.  The techniques we are demonstrating in this sample can be used in any Cocoa Application.  We used a simple one window Cocoa application for this sample to keep it simple.  




2. Add a Scripting Bridge build rule to the project.

The first thing to do is to set up Xcode to automatically generate the Scripting Bridge source for the application you would like to target.  The following steps describe how you can do that:

(a) In the project navigator, choose the project file and select the "SBSetFinderComment" target.  

(b) With the "SBSetFinderComment" target selected, switch to the "Build Rules" tab.

(c) In the build rules tab, click on the + button at the bottom to add a new rule.

(d) Set up the new rule as follows:

    Process 'Source files with names matching:'   *.app

    using: 'Custom Script'

    set the script field to:

    sdef "$INPUT_FILE_PATH" | sdp -fh -o "$DERIVED_FILES_DIR" --basename "$INPUT_FILE_BASE" --bundleid `defaults read "$INPUT_FILE_PATH/Contents/Info" CFBundleIdentifier`

    click on the "+" icon below the 'with output files:' field, and then set the field to contain:

    $(DERIVED_FILES_DIR)/$(INPUT_FILE_BASE).h

    NOTE: if you're typing this rule in by hand, note that it should all be one one line, and it must be typed exactly as shown above.  If you have difficulty entering the above command, then copy and paste the command from the readme into the rule.

(e) All done.  Xcode is now set up to automatically generate Scripting Bridge source for any applications you add to your project.

NOTE: this rule uses the sdef and sdp command line tools.  To learn more about these tools, use the following commands in the Terminal window:
   man sdp
   man sdef




3. Select a target application.

To do this, drag and drop the application you would like to target into the project files group inside the project navigator.

You can drop the application among the source files you are using for your application.  Because of the build rule we added in step 2, Xcode will treat the Finder application as if it were one of the source files during the build.  

You should uncheck the 'Copy items into destination group's folder (if needed)' option so the application is not copied into your project directory.  In this sample we have selected 'Absolute Path' as the reference type so we can easily move the project around from machine to machine without invalidating the reference (so long as the Finder application is present in the System/Library/CoreServices folder,  Xcode will be able to find it).

In this case, we are adding the Finder to our project.  The Finder application is located in the /System/Library/CoreServices folder.




4. Add the target application to the Compile Sources.

After you have added the target application to your project, you must also add it to the main target's Compile Sources.  You can do that by adding the application to the 'Compile Sources' build phase under the main target.



5. Add the Scripting Bridge framework to your project.

In the Build Phases of the main target, expand the group titled "Link With Libraries".  Click the + button and select the ScriptingBridge.framework and click the Add button.




6. Add a minimum system version Info.plist key.

Since the ScriptingBridge.framework is necessary for this application to run and that framework is not present on previous system versions, you should add the following key/value pair to the Info.plist file for the application.  If someone tries to run this application on a system earlier than Mac OS X 10.5, then they will receive a notice from launch services letting them know that the application is meant to be run on a later version of Mac OS X.

    <key>LSMinimumSystemVersion</key>
    <string>10.5</string>



7. Build your project.

If you have followed the steps above, Xcode will generate the Scripting Bridge source for your project.  They will be put inside of your build folder in a place where the linker and compiler can find them.  

The build rule that we installed will create a .h and a .m file with the same name as the application.  For example, if you added Finder to your project, then the build rule will create Finder.h.  The files will be created inside of the build directory in the DerivedSources directory where the compiler can find them.

For the Debug build, the Finder.h file will be located in this sub folder of the build directory:
/build/Intermediates/SBSetFinderComment.build/Debug/SBSetFinderComment.build/DerivedSources/Finder.h

For the Release build, the Finder.h file will be located in this sub folder of the build directory:
/build/Intermediates/SBSetFinderComment.build/Release/SBSetFinderComment.build/DerivedSources/Finder.h

A convenient way for you to open and inspect these files is to use the 'Open Quickly' command in the file menu.  For most purposes, the .h file will contain most of the interesting information so to view that file you open the 'Finder.h' file.  

In some cases, depending on what frameworks are in your project, the 'Open Quickly' command may open the system's 'Finder.h' file that includes constants and definitions used by the file system and the Finder application.  If that happens for you, then you will need to navigate into the build folder to find the correct header file.




8. Add in the Finder's Scripting Bridge header.

In the file Controller.m, add '#import "Finder.h"' near the top of the file below '#import "Controller.h"'.  This will include all of the Scripting Bridge definitions for the Finder.

When you're done, the imports section should look like this:

    #import "Controller.h"
    #import "Finder.h"

In your own application, of course, you would import the Finder.h file in the file where you intend to call it from.  In this sample, we are using the Scripting Bridge interface inside of three methods in our Controller class so that is why we are importing it into Controller.m.




9. Roadmap - check out what the SBSetFinderComment sample is doing.

So, we've set up our sample and installed the basic parts.  Let's take a moment to look at the bigger picture so we can see where we're going and how Scripting Bridge fits into this sample.

In this sample we have have provided three methods that use Scripting Bridge to perform some commonly implemented tasks: (a) retrieving a file's Finder comment, (b) changing a file's Finder comment, and (c) revealing an item in the Finder.

We'll discuss each of these items in the sections below.




10. Retrieving a file's Finder Comment (aka, Spotlight Comment).

The method -finderCommentForFileURL:error: in the Controller class uses Scripting Bridge to retrieve the Finder Comment for an item referred to by the file url provided as a parameter.  As you can see, it's a very simple method:


- (NSString*) finderCommentForFileURL:(NSURL*) theFileURL error:(NSError**) error {
    NSString* result;

        /* retrieve the Finder application Scripting Bridge object. */
    FinderApplication* finder = [SBApplication applicationWithBundleIdentifier:@"com.apple.finder"];

    if ( finder == nil ) {
            /* A nil value here means the bundle id was not found or the applications does not have a 
             * scripting interface. */
        if ( error != NULL )
            *error = [NSError errorWithDomain:NSCocoaErrorDomain code:SBApplicationInstantiationError userInfo:
                        [NSDictionary dictionaryWithObject:@"Unable to create an instance of SBApplication." forKey:NSLocalizedDescriptionKey]];

        return nil;
    }

        /* retrieve a reference to our finder item asking for it by location */
    FinderItem * theItem = [[finder items] objectAtLocation: theFileURL];

        /* set the result.  */
    result = theItem.comment;

        /* Test for errors */
    if ( [finder lastError] != nil ) {
        if ( error != NULL )
                /* retrieve the error from the parent object */
            *error = [finder lastError];

    return NO;
    }

        /* return the comment (or nil on error). */
    return result;
}

Interesting items to note here are:

(a) after each call to a Scripting Bridge API that executes an Apple Event we test for errors and set the error argument to the last error reported by Scripting Bridge before returning nil. Alternatively, the SBApplication class allows you to set a delegate object that implements a -eventDidFail:withError: delegate method.

(b) we use the +applicationWithBundleIdentifier: SBApplication class method to create our Application object.  This will dynamically load the application object based on the dictionary inside of the application itself rather than building the application class from statically compiled information.

(c) the 'comment' property of the FinderItem is implemented as an Objective-C 2.0 property.  Most of the work involved with retrieving the comment including the Apple events required to retrieve the information happens inside of the property getter defined for this property.





12.  Changing a file's Finder Comment (aka, Spotlight Comment).

The method -changeFinderComment:forFileURL: in the Controller class uses Scripting Bridge to set the Finder Comment for an item referred to by the file url provided as a parameter.  As you can see, it is also a very simple method:


- (BOOL) changeFinderComment:(NSString*) comment forFileURL:(NSURL*) theFileURL error:(NSError**) error {

        /* retrieve the Finder application Scripting Bridge object. */
    FinderApplication* finder = [SBApplication applicationWithBundleIdentifier:@"com.apple.finder"];

    if ( finder == nil ) {
            /* A nil value here means the bundle id was not found or the applications does not have a 
             * scripting interface. */
        if ( error != NULL )
            *error = [NSError errorWithDomain:NSCocoaErrorDomain code:SBApplicationInstantiationError userInfo:
                        [NSDictionary dictionaryWithObject:@"Unable to create an instance of SBApplication." forKey:NSLocalizedDescriptionKey]];

        return NO;
    }

        /* retrieve a reference to our finder item asking for it by location */
    FinderItem * theItem = [[finder items] objectAtLocation: theFileURL];

        /* attempt to set the comment for the Finder item.  */
    theItem.comment = comment;

        /* Test for errors */
    if ( [finder lastError] != nil ) {
        if ( error != NULL )
                /* retrieve the error from the parent object */
            *error = [finder lastError];

        return NO;
    }

        /* return YES on success */
    return YES;
}


Interesting items to note here are:

(a) Again, after each call to a Scripting Bridge API that executes an Apple Event we test for errors and set the error argument to the last error reported by Scripting Bridge before returning nil. Alternatively, the SBApplication class allows you to set a delegate object that implements a -eventDidFail:withError: delegate method.

(b) we use the +applicationWithBundleIdentifier: SBApplication class method to create our Application object.  This will dynamically load the application object based on the dictionary inside of the application itself rather than building the application class from statically compiled information.

(c) the 'comment' property of the FinderItem is implemented as an Objective-C 2.0 property.  Most of the work involved with changing the comment including the Apple events required to set the comment to a new value inside of the property setter defined for this property.




14. Other details.

Much of the rest of the application code is there for housekeeping and managing the GUI.  Interesting parts worth mentioning are:

(a) We limit the size of Finder Comments to 750 Unicode characters in length.  Radar rdar://problem/4857955 states that Finder comments are limited to 750 Unicode characters.  This is the current recommendation at the time of this writing.

(b) we implement a -applicationDidBecomeActive: NSApplication delegate method to receive notifications whenever our application is switched into the forground.  We take this opportunity to refresh the comment field in case the comment was changed while our process was in the background.




15. Where to next?

Documentation for Scripting Bridge can be found in the Scripting Bridge Release Note.  To find the Scripting Bridge Release Note, select 'Documentation' from the Help Menu in Xcode, select "Release Notes" from the "Jump To:" menu in the top right of the document window, click on the "View the complete Release Notes List." link near the top left of the window and scroll down to the Scripting Bridge Release Note.

There are man pages available for the Scripting Bridge command line tools.  To access those pages, enter the following commands into the Terminal window:

   man sdp
   man sdef

There are two other Scripting Bridge samples available including ScriptingBridgeiCal and ScriptingBridgeFinder showing how to use Scripting Bridge together with the Apps named in their titles.



===========================================================================
BUILD REQUIREMENTS

Xcode 3.2, Mac OS X 10.6 Snow Leopard or later.

===========================================================================
RUNTIME REQUIREMENTS

Mac OS X 10.6 Snow Leopard or later.

===========================================================================
CHANGES FROM PREVIOUS VERSIONS

Version 1.1
- Updated error handling.
- Updated setup instructions in the ReadMe.
- Project updated for Xcode 4.
Version 1.0
- Initial Version

===========================================================================
Copyright (C) 2007-2011 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](SBSetFinderComment.md)

