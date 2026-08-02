---
title: AppleScript Studio Programming Guide
apple_id: TP30000889
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2011-01-07'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/StudioBuildingApps/requirements/scriptStudio_requirements.html
archived_at: '2026-07-15T05:20:44.724719Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AppleScript Studio Programming Guide](Introduction%20to%20AppleScript%20Studio%20Programming%20Guide.md)


[Next](Mail%20Search%20Tutorial%2C%20Full%20Script%20Listing.md)[Previous](Mail%20Search%20Tutorial-%20Customize%20the%20Application.md)

# AppleScript Studio System Requirements and Version Information

This appendix describes the system requirements for developing and running AppleScript Studio applications and explains how to determine if AppleScript Studio is currently installed.

To build AppleScript Studio applications, you must install a version of the Mac OS X Developer Tools that includes AppleScript Studio. To run an AppleScript Studio application, the target machine must have the AppleScript Studio runtime required for the application. An AppleScript Studio runtime is available if `AppleScriptKit.framework` is present in `/System/Library/Frameworks`.

AppleScript Studio attempts to maintain the following:

- An application created and built with an older version of AppleScript Studio can run with a newer runtime.
- An application created and built with a newer version of AppleScript Studio can run with an older runtime, if it doesn’t use any features introduced after that runtime.

For example, an application built with AppleScript Studio version 1.1 that uses features added in version 1.1 requires the 1.1 runtime. However, a similar application that doesn’t use any features from AppleScript Studio 1.1 can run with the 1.0 runtime. And an application built with AppleScript Studio version 1.0 can run with any runtime, through version 1.3.

Table A-1 lists AppleScript Studio versions, the development environment they are part of, and the system software the corresponding runtime is installed with.

__Table A-1__  Availability for AppleScript Studio development environment and runtime

| AppleScript Studio Version | Distributed with development environment | Runtime installed with |
| 1.0 | December 2001 Developer Tools CD | Developer Tools CD (with AppleScript 1.8.2), or Mac OS X version 10.1.2 software update (with AppleScript 1.8.3 or later) |
| 1.1 | April 2002 Developer Tools CD | Developer Tools CD (with AppleScript 1.8.2 or later) |
| 1.2 | Mac OS X version 10.2 Developer Tools CD | Mac OS X version 10.2, and later (with AppleScript 1.9.0 or later) |
| 1.2.1 | December 2002 Developer Tools CD | Developer Tools CD (with AppleScript 1.9.1), or Mac OS X version 10.2.3 software update (with AppleScript 1.9.1 or later) |
| 1.3 | Mac OS X version 10.3 Xcode Tools | Mac OS X version 10.3, and later (with AppleScript 1.9.2 or later) |
| 1.4 | Mac OS X version 10.4 Xcode Tools | Mac OS X version 10.4, and later (with AppleScript 1.10 or later) |

For an example of how your application can determine whether the required version of AppleScript Studio is present, see the Examples section for the `will finish launching` event handler in the Application Suite in _AppleScript Studio Terminology Reference_.

Starting with the version of Interface Builder released with Mac OS X version 10.2, there is a Nib File Compatibility preference on the General pane of the Interface Builder Preferences window. You should select a nib-file preference that suits your compatibility goals, from the following choices (and restart Interface Builder for the changes to take affect):

- _Pre-10.2 format:_ applications will run with earlier versions of Mac OS X, but will not have access to new features (such as the circular progress indicator or the brushed-metal, textured window appearance)
- _10.2 and later format:_ provides access to all new features, but is not guaranteed to run in earlier versions of Mac OS X
- _Both Formats:_ provides access to new features but will also run in earlier versions of Mac OS X (though without the new features)

[Next](Mail%20Search%20Tutorial%2C%20Full%20Script%20Listing.md)[Previous](Mail%20Search%20Tutorial-%20Customize%20the%20Application.md)

