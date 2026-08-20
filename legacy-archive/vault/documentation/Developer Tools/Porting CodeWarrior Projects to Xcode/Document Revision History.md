---
title: Porting CodeWarrior Projects to Xcode
apple_id: '20001708'
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2009-06-30'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/MovingProjectsToXcode/history/migration_rev_hist.html
archived_at: '2026-07-15T07:25:16.270069Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Porting CodeWarrior Projects to Xcode](Introduction%20to%20Porting%20CodeWarrior%20Projects%20to%20Xcode.md)


[Previous](Where%20to%20Go%20From%20Here.md)

# Document Revision History

This table describes the changes to _Porting CodeWarrior Projects to Xcode_.

| __Date__ | __Notes__ |
| 2009-06-30 | Made technical correction. |
|  | Fixed uninitialized-variable bug (`count`) in [Listing 5-2](Using%20PowerPlant%20in%20Universal%20Binaries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzsfvbecssijjfeqqq). |
| 2006-10-26 | Corrected errors. Changed title from "Moving CodeWarrior Projects to Xcode." |
|  | Updated [For Best Results When Importing](Importing%20a%20CodeWarrior%20Project%20Into%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ytclkdjbceqr2jijca) and [Known Issues With the Importer](Importing%20a%20CodeWarrior%20Project%20Into%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ytclkdjbceuq2bijfa) to note that CodeWarrior must be running when importing. |
| 2006-11-07 | Corrected errors. |
|  | Revised statement of pragma support in GCC. |
| 2006-09-05 | Corrected errors. |
|  | Fixed missing semicolon in [Listing 4-3](After%20Importing%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ytelkukbmferkgge3tk). |
|  | Updated [Known Issues With the Importer](Importing%20a%20CodeWarrior%20Project%20Into%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ytclkdjbceuq2bijfa) to reflect importer support for CW object targets. |
| 2006-05-23 | Made document-flow change. |
|  | Changed the order of the steps to update the PowerPlant source files in [Make Changes to PowerPlant](After%20Importing%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ytelkukbmferkgge3dm) to make them easier to follow. |
| 2005-11-09 | Updated for Xcode 2.2 and corrected errors. |
|  | Added [Using PowerPlant in Universal Binaries](Using%20PowerPlant%20in%20Universal%20Binaries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzsfvjvomi). |
|  | Updated [Exporting Symbols](Xcode%20From%20a%20CodeWarrior%20Perspective.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydslkcifbemqsijbda) to reflect support for importing `.exp` files in Xcode 2.2. |
|  | Corrected description in [C and C++ Libraries](Xcode%20From%20a%20CodeWarrior%20Perspective.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydslkcifbemrcci5aq) of options passed by Xcode to the compiler when changing filetype. |
|  | In [Working With Resources](Xcode%20From%20a%20CodeWarrior%20Perspective.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydslkcineusschivea), added links to additional information on resource files and build phases. |
|  | Added note, in [Known Issues With the Importer](Importing%20a%20CodeWarrior%20Project%20Into%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ytclkdjbceuq2bijfa), about the importer not supporting targets whose Project Type is Object. |
|  | Added note about including `ppcintrinsics.h` to use intrinsics in Xcode. |
|  | Fixed typos. |
| 2005-08-11 | Fixed typos and made minor editorial corrections. |
|  | Updated [Building Code](Xcode%20From%20a%20CodeWarrior%20Perspective.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydslkukbmferkggeztg) to reflect default Imported CodeWarrior Settings build configuration for imported projects. |
|  | Fixed typos. |
| 2005-06-06 | Updated for Xcode 2.1 and GCC 4.0. |
|  | Added section on [Build Configurations](Xcode%20From%20a%20CodeWarrior%20Perspective.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydslkukbmferkgge2tg); removed mention of build styles. |
|  | Updated description of Search field in [Some Special Features of Xcode](Xcode%20From%20a%20CodeWarrior%20Perspective.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydslkukbmferkgge2de) to include wildcard and regular expression searching. |
|  | Added descriptions of project window layouts and showing / hiding smart groups to [Customizing the Environment](Xcode%20From%20a%20CodeWarrior%20Perspective.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydslktk4yti). |
|  | Revised discussion of header files and search paths in [Header Files](Xcode%20From%20a%20CodeWarrior%20Perspective.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydslktk4ytg) to reflect Xcode 2.0 support for recursive search paths. |
|  | Updated build phase names throughout. |
|  | Added mention of breakpoint actions and watchpoints to [Debugging](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/MovingProjectsToXcode/migration_differences/migration_differences.html#//apple_ref/doc/uid/20001709-SW10). |
|  | Updated [The GCC Compiler](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/MovingProjectsToXcode/migration_differences/migration_differences.html#//apple_ref/doc/uid/20001709-SW5) for GCC 4.0; also added note about removal of GCC 3.1 and 2.95. |
|  | Noted that prebinding is no longer necessary if you are running on 10.3.4 or later in [Prebinding](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/MovingProjectsToXcode/migration_differences/migration_differences.html#//apple_ref/doc/uid/20001709-SW11). |
|  | Updated [C and C++ Libraries](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/MovingProjectsToXcode/migration_differences/migration_differences.html#//apple_ref/doc/uid/20001709-SW4) to reflect the switch to packaging the standard C++ library as a dynamic shared library. |
| 2005-04-29 | Fixed broken links. |
| 2005-01-11 | Corrected typos. |
|  | Fixed typos in [Listing 4-6](After%20Importing%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ytelkdjbceirsjijdq) and in [Migrate from MSL to System C and C++ Libraries](Preparing%20a%20CodeWarrior%20Project%20for%20Importing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ytalkukbmferkggeztk). |
|  | Updated for July 2004 Xcode Tools. |
|  | Updated screenshots. |
|  | Added information on using dead code stripping in Xcode to section [Dead Code Stripping](Xcode%20From%20a%20CodeWarrior%20Perspective.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydslkcifbegsscjjea). |
|  | Added a note about a Rez bug to section [Working With Resources](Xcode%20From%20a%20CodeWarrior%20Perspective.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrg4ydslkcineusschivea). |
|  | First public release. |

[Previous](Where%20to%20Go%20From%20Here.md)

