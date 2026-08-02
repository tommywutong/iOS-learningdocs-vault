---
title: Idling Movie Importers
apple_id: DTS10003421
resource_type: Technical Note
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-19'
source_url: https://developer.apple.com/library/archive/technotes/tn2111/_index.html
archived_at: '2026-07-26T19:53:51.011807Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2111

# Idling Movie Importers

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

This technical note discusses how to write an idling movie importer component. Idling movie importers differ from regular movie importers because they implement a special routine `MovieImportIdle` which is called periodically to process the movie data during the import operation.

[What is an Idling Movie Importer?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbsgewugsbrfvke4vcbi4yq)[Designating your Importer as an Idling Importer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbsgewugsbrfvke4vcbi4za)[MovieImportIdle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbsgewugsbrfvke4vcbi4ytg)[Notifying the Movie Controller that the Movie has changed](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbsgewugsbrfvke4vcbi4yti)[MovieImportSetIdleManager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbsgewugsbrfvke4vcbi4zq)[MovieImportDataRef/MovieImportFile/MovieImportHandle Special Considerations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbsgewugsbrfvke4vcbi42q)[MovieImportDataRef](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbsgewugsbrfvke4vcbi43a)[MovieImportGetLoadState](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbsgewugsbrfvke4vcbi44a)[Idling Importers & Movie Controllers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbsgewugsbrfvke4vcbi4yta)[Summary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbsgewugsbrfvke4vcbi4yte)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbsgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## What is an Idling Movie Importer?

As described in the [Movie Data Exchange Components](https://developer.apple.com/documentation/QuickTime/RM/ImportExport/DataExchange/index.html) documentation, movie import components import data from non-movie sources into QuickTime movies. For example, a CD audio track can be imported into a QuickTime movie. In general, this is accomplished by a single call to one of the importer's `MovieImportFile`, `MovieImportHandle` or `MovieImportDataRef` routines, at which time the importer component will download all the movie data, process it, then return the imported movie data to the calling program (see the [ElectricImage sample code](https://developer.apple.com/samplecode/ElectricImageComponent/ElectricImageComponent.html) for an example of an actual movie importer component).

Idling movie importer components differ from non-idling importer components in that they implement a special routine `MovieImportIdle` (see [MovieImportIdle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbsgewugsbrfvke4vcbi4ytg)) which is called periodically to allow the importer to process the movie data during the import operation. This means the import operation is usually not completed in a single call to one of the importer's `MovieImportFile`, `MovieImportHandle` or `MovieImportDataRef` routines. Instead, the importer's `MovieImportFile`, `MovieImportHandle` or `MovieImportDataRef` routine will return the value `movieImportResultNeedIdles` to indicate it needs to be idled (see [MovieImportDataRef](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbsgewugsbrfvke4vcbi43a)), after which the importer's `MovieImportIdle` routine is called periodically until processing of the movie data is complete.

Because they are called at periodic intervals, idling movie importers are given the opportunity to display the movie data as it is downloaded, similar to how fast-start movies are displayed, rather than after the data has been completely downloaded.

[Back to Top](#)

## Designating your Importer as an Idling Importer

You must identify your movie importer as an idling movie importer in order for your `MovieImportIdle` function to be called. You designate your movie importer as an idling importer by specifying the `canMovieImportWithIdle` component flag (see QuickTimeComponents.h) in the `componentFlags` field of your component's `ComponentDescription` structure:

__Listing 1__  `canMovieImportWithIdle` component flag.

```
canMovieImportWithIdle        = 1L << 20
```

[Back to Top](#)

## MovieImportIdle

Here's a description of the new `MovieImportIdle` function for idling importers. QuickTime will call this routine periodically to allow you to process the movie data for the movie import:

__Listing 2__  `MovieImportIdle`

```
MovieImportIdle

Call the movie data import component to handle periodic tasks.

ComponentResult MovieImportIdle ( // IV-2677
    MovieImportComponent    ci,                                 // IV-2677
    long                    inFlags,
    long                    *outFlags );

ci

A movie data import component instance. Your software obtains this reference
from OpenComponent or OpenDefaultComponent.

inFlags

Flags (see below) that specify control information governing the import operation.

outFlags

Flags (see below) that identify a field that is to receive status information about
the import operation. Your component sets the appropriate flags in this field
when the operation is complete.

Function Result: Returns noErr if there is no error.

inFlags Constants

Currently not used. Set to 0.

outFlags Constants

movieImportResultComplete

Indicates whether or not your component has completed importing the data. Set
this flag to 1 if your component is finished importing the data.

VERSION NOTES

Introduced in QuickTime 4.

PROGRAMMING INFO

C interface file: QuickTimeComponents.h
Availability:
    Non-Carbon CFM: in QuickTimeLib 4.0 and later
    CarbonLib: in CarbonLib 1.0.2 and later
    Mac OS X: in version 10.0 or later
    Windows: in qtmlClient.lib 4.0 and later
```

[Back to Top](#)

## Notifying the Movie Controller that the Movie has changed

After idling importers append newly processed media to a movie (usually via calls to `AddMediaSampleReferences64` and `InsertMediaIntoTrack`), they must notify the movie controller so the duration and state of the movie can be updated and all the media can become playable. This is accomplished by executing the wired action `kActionMovieChanged` for the movie with the `MovieExecuteWiredActions` function using code similar to the following:

__Listing 3__  Notify the movie controller that the movie has changed.

```
QTAtomContainer container;
Movie           theMovie;

// We must notify the movie controller that the movie has changed,
// so we'll send it the kActionMovieChanged wired action

if (QTNewAtomContainer(&container) == noErr)
{
    QTAtom anAction;
    OSType whichAction = EndianU32_NtoB(kActionMovieChanged);

    OSErr err = QTInsertChild(container, kParentAtomIsContainer,
                            kAction, 1, 0, 0, NULL, &anAction);
    if (err == noErr)
    {
        err = QTInsertChild(container, anAction, kWhichAction, 1, 0,
                                sizeof (whichAction), &whichAction, NULL);
    }

    if (err == noErr)
    {
        err = MovieExecuteWiredActions(theMovie, 0, container);
    }

    err = QTDisposeAtomContainer(container);
}
```

__Note:__ Do not execute this action more frequently than two or three times per second. Concurrent playback may become choppy if a movie's state is reset via this action too frequently.

Here's a description of the `MovieExecuteWiredActions` function:

__Listing 4__  `MovieExecuteWiredActions` function.

```
MovieExecuteWiredActions

Execute the specified wired actions for the movie

OSErr MovieExecuteWiredActions (
   Movie              theMovie,
   long               flags,
   QTAtomContainer    actions );

Parameter Descriptions

theMovie

A movie identifier. Your application obtains this identifier from such
functions as NewMovie, NewMovieFromFile, and NewMovieFromHandle.

flags

Flags (see below) that specify control information for the wired action
to be performed

actions

An atom container with the wired action(s) to execute

function result

You can access Movie Toolbox error returns through GetMoviesError and GetMoviesStickyError,
as well as in the function result. See Error Codes.

flags Constant

movieExecuteWiredActionDontExecute

Any wired action callback procedures shouldn't execute the actions,
but may want to look at them. The AddMovieExecuteWiredActionsProc
function lets you add a callback to a movie to execute wired actions.
The RemoveMovieExecuteWiredActionsProc lets you remove the callback.

Version Notes

Introduced in QuickTime 4.

Programming Info

C interface file: Movies.h
Carbon status: Supported

Related Java Methods

quicktime.std.movies.Movie.executeWiredActions()
```

[Back to Top](#)

## MovieImportSetIdleManager

QuickTime 6 introduces a number of new Idle Manager APIs. These are discussed in the [What's New in QuickTime 6](https://developer.apple.com/documentation/QuickTime/QT6WhatsNew/index.html) documentation. Among them is the `MovieImportSetIdleManager` API. Movie Importers written for QuickTime 6 may implement this function and tell the Idle Manager when they would like to be idled next. Refer to the documentation for additional information.

[Back to Top](#)

## MovieImportDataRef/MovieImportFile/MovieImportHandle Special Considerations

Movie Importer components may of course choose to implement the `MovieImportDataRef`, `MovieImportFile` and `MovieImportHandle` functions. Importers indicate support for these routines by specifying the appropriate flag (`canMovieImportDataReferences`, `canMovieImportFiles` and `canMovieImportHandles`) in the component's `componentFlags` field in the `ComponentDescription` structure.

Idling movie importers which support any of the above routines should return `movieImportResultNeedIdles` in the `outFlags` parameter to indicate they would like to have their `MovieImportIdle` routine called periodically to process the movie data, or return `movieImportResultComplete` to indicate the import is complete.

[Back to Top](#)

## MovieImportDataRef

Import components (in general) should implement `MovieImportDataRef` if they are able to accept a data reference (such as a handle) as the source for an import operation.

An import component indicates it supports `MovieImportDataRef` by specifying the `canMovieImportDataReferences` flag in the `componentFlags` field of their component's `ComponentDescription` structure.

Here's a description of the `MovieImportDataRef` function:

__Listing 5__  the `MovieImportDataRef` function.

```
MovieImportDataRef

Import movie data from a data reference.

ComponentResult MovieImportDataRef ( // IV-2677
    MovieImportComponent    ci,                           // IV-2677
    Handle                  dataRef,                      // IV-2683
    OSType                  dataRefType,                  // IV-2695
    Movie                   theMovie,                     // IV-2685
    Track                   targetTrack,                  // IV-2685
    Track                   *usedTrack,                   // IV-2685
    TimeValue               atTime,                       // IV-2697
    TimeValue               *addedDuration,               // IV-2697
    long                    inFlags,
    long                    *outFlags );

ci
A movie import component instance. Your software obtains this
reference from OpenComponent (II-1161) or OpenDefaultComponent (II-1163).

dataRef
The data reference to the data to be imported.

dataRefType
The type of data reference in the dataRef parameter.

theMovie
A movie identifier. Your application obtains this identifier from such
functions as NewMovie (II-1098), NewMovieFromFile (II-1110), and NewMovieFromHandle (II-1113).

targetTrack
The track that is to receive the imported data. This track identifier is supplied by the Movie Toolbox
and is valid only if the movieImportMustUseTrack flag in the inFlags parameter is set to 1.

usedTrack
A pointer to the track that received the imported data. Your component
returns this track identifier to the Movie Toolbox. Your component needs
to set this parameter only if you operate on a single track or if you
create a new track. If you modify more than one track, leave the field
referred to by this parameter unchanged.

atTime
The time corresponding to the location where your component is to place
the imported data. This time value is expressed in the movie's time
coordinate system.

addedDuration
A pointer to the duration of the data that your component added to
the movie. Your component must specify this value in the movie's
time coordinate system.

inFlags
Flags (see below) that control the behavior of this function.

outFlags
Flags (see below) that this function sets on return.

Function Result: See "Error Codes" (IV-2718). Returns noErr if there
is no error.

inFlags Constants

movieImportCreateTrack
Indicates that your component should create a new track to receive
the imported data. You must create a track whose type value corresponds
to the media type that you have specified in your component's
manufacturer code. You should return the track identifier of this new
track in the field referred to by the usedTrack parameter, unless you
create more than one track. If you create more than one track, be sure
to set the movieImportResultUsedMultipleTracks flag in the field referred
to by the outFlags parameter to 1. If the movieImportCreateTrack flag is
set to 1, then the movieImportMustUseTrack flag is set to 0.

movieImportMustUseTrack
Indicates that your component must use an existing track. That track is identified
by the targetTrack parameter. If you create more than one
track, be sure to set the movieImportResultUsedMultipleTracks flag in the
field referred to by the outFlags parameter to 1. If the
movieImportMustUseTrack flag is set to 1, then the movieImportCreateTrack
flag is set to 0. If both the movieImportCreateTrack and
movieImportMustUseTrack flags are set to 0, then you are free to use any existing
tracks in the movie or to create a new track (or tracks) as
needed.

movieImportInParallel
Indicates whether you are to perform an insert operation or a paste
operation. If this flag is set to 0, then you should insert the
imported data into the target track. If this flag is set to 1, then
you should add the imported data to the track, overwriting preexisting
open space currently in the track. Note that an application may use
MovieImportSetDuration (II-982) to control the amount of data you paste
into a movie. If the movieImportMustUseTrack flag is set to 1, then
you should use the track specified by the targetTrack parameter. If
this is not possible, return an appropriate Movie Toolbox result code.

movieImportWithIdle
Indicates you should perform the import operation as an idling importer. Set the
movieImportResultNeedIdles flag in the outFlags parameter to 1, and your
MovieImportIdle routine will get called periodically to process the movie data.

outFlags Constants

movieImportResultUsedMultipleTracks
Indicates that your component modified more than one track in the movie.
Set this flag to 1 if your component places imported data into more than
one track. In this case, you do not need to update the field referred to
by the usedTrack parameter.

movieImportResultNeedIdles
Indicates your component would like it's MovieImportIdle routine to be
called periodically to process the movie data.

movieImportResultComplete
Indicates your component is finished processing the movie data.

VERSION NOTES

Introduced in QuickTime 3 or earlier.

PROGRAMMING INFO

C interface file: QuickTimeComponents.h
Carbon status: Supported

RELATED JAVA METHODS

quicktime.std.movies.Track.fromMovieImporterDataRef(), quicktime.std.qtcomponents.MovieImporter.fromDataRef()
```

[Back to Top](#)

## MovieImportGetLoadState

Idling importers may choose to implement the movie importer `MovieImportGetLoadState` function. The `MovieImportGetLoadState` function returns a value that indicates the state of the asynchronous loading process for a movie.

Documentation for the asynchronous movie loading process (and the high-level function `GetMovieLoadState`) can be found in the [What's New in QuickTime 4.1](https://developer.apple.com/documentation/QuickTime/REF/QT41_HTML/QT41WhatsNew.html) pdf document. Additional load states can be found in the [What's New in QuickTime 5](https://developer.apple.com/documentation/QuickTime/WhatsNewQT5/index.html) pdf document.

Here's a brief description of the `MovieImportGetLoadState` function:

__Listing 6__  `MovieImportGetLoadState`.

```
Returns the asynchronous load state for a movie.

ComponentResult
MovieImportGetLoadState(
  MovieImportComponent   ci,
  long *                 importerLoadState)

ci
A movie import component instance.

importerLoadState
A pointer that is to receive the current load state for the movie.
Values for loading process are as follows:

kMovieLoadStateLoading
Indicates the importer is searching for the movie resource

kMovieLoadStatePlayable
Indicates the movie is fully formed, fast-start would work

kmovieLoadStatePlaythroughOK
Indicates that the download would complete before the playback
would complete. This value will be returned after the movie has
become playable

kMovieLoadStateComplete
Indicates all media data is available

Function Result: See "Error Codes" (IV-2718). Returns noErr if
there is no error.

DISCUSSION

Your component can implement this function if it supports
asynchronous movie loading over slow connections. Use it to
report the current load state of the movie.

VERSION NOTES

Availability:
     Non-Carbon CFM: in QuickTimeLib 4.1 and later
     CarbonLib: in CarbonLib 1.1 and later
     Mac OS X: in version 10.0 or later
     Windows: in qtmlClient.lib 4.1 and later

PROGRAMMING INFO

C interface file: QuickTimeComponents.h
Programming summary: "Importing Movie Data" (V-2910)
Carbon status: Supported
```

[Back to Top](#)

## Idling Importers & Movie Controllers

Idling importers may wish to supply a hint regarding the type of movie controller to use for the imported movie. For example, if the importer implements a still image format it might want to make sure the movie does not display any controller. This is accomplished by specifying the no-interface movie controller (also referred to as the none movie controller) as the desired movie controller for the movie. The no-interface movie controller operates just like the standard movie controller except that no controller bar is displayed and no keyboard events are passed to it.

When an application calls `NewMovieController` to attach a movie controller to a movie, `NewMovieController` first looks for a movie user data item of type `kUserDataMovieControllerType` and, if it finds one, tries to open an instance of a movie controller component having the subtype specified by that item's data. This occurs transparently to the application.

Importers can specify the suggested controller for the movie by calling the `SetUserDataItem` function, passing the desired controller type in the data parameter and `kUserDataMovieControllerType` for the udType parameter as follows:

__Listing 7__  Specifying the no-interface movie controller hint.

```
OSErr err;
OSType	noneType = FOUR_CHAR_CODE('none');

/* set the "none" controller for this movie */
err = SetUserDataItem(GetMovieUserData(theMovie), &noneType, sizeof(noneType),
                    kUserDataMovieControllerType, 1);
```

You should call `SetUserDataItem` in your importer's `MovieImportDataRef` routine to supply a movie controller hint for the movie.

[Back to Top](#)

## Summary

Idling movie importer components are just like regular movie import components except they implement a special routine `MovieImportIdle` which is called at periodic intervals to process the movie data. You designate a movie import component as an idling movie import component by specifying the `canMovieImportWithIdle` component flag (see QuickTimeComponents.h) in the `componentFlags` field of your component's `ComponentDescription` structure. Idling movie import components must implement the `MovieImportIdle` routine in order to get called periodically to process the movie data. Idling movie importers can also specify an appropriate movie controller hint for the movie by adding a `kUserDataMovieControllerType` user data item to the movie via the `SetUserDataItem` function.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-19 | Editorial |
| 2004-11-12 | New document that discusses how to write an idling movie importer component |

