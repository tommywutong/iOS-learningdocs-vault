---
title: Launch Services Programming Guide
apple_id: TP30000999
resource_type: Guide
platform: macOS
topic: Data Management
technology: ApplicationServices
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/LaunchServicesConcepts/LSCGlossary/LSCGlossary.html
archived_at: '2026-07-15T05:23:18.493270Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Launch Services Programming Guide](Introduction.md)


[Previous](Document%20Revision%20History.md)

# Glossary

- 
  __activate__

  To bring a running [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g) to the front of the screen, allowing the user to interact with it. Compare [launch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbiveuerkh).

- __active extension__

  A [filename extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjbeucqse)[claim](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfbuir2e)ed by at least one [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g) [register](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjjaumskc)ed with Launch Services. Compare [valid extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjffegrce).

- __application__

  An independently executable software program.

- __application bundle__

  A [bundle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjbceoskj) containing the executable code of an [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g) and its associated resources.

- __application file__

  A file containing the executable code of an [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g).

- __application package__

  An [application bundle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbi5degssc) presented to the user in the form of a [package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbindesqkb) whose contents are ordinarily inaccessible for browsing.

- __asynchronous launch__

  A [launch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbiveuerkh) operation in which control returns immediately to the calling program, without waiting for the launched [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g) to complete its [launch sequence](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbinaueq2k). Compare [synchronous launch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjffegssj).

- __binding information__

  The information maintained in the [Launch Services database](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbi5euqqkg) about the kinds of [document](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirduiqkh)s and [URL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbijdeurkc)s an [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g) is capable of [open](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirbuosci)ing.

- __binding preference__

  A preference set by the user specifying the [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g) in which to [open](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirbuosci) a given [document](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirduiqkh) or [URL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbijdeurkc).

- __binding rules__

  The rules used by Launch Services to determine an [item](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjbbuoskj)’s [default application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjjcucskd) according to the [binding information](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbivbegrkh) in the [Launch Services database](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbi5euqqkg).

- __bundle__

  A [directory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbijceuq2e) containing executable code and related resources, structured according to conventions defined by Core Foundation Bundle Services.

- __bundle identifier__

  A unique identifying string used to locate
  an [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g)’s [bundle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjbceoskj) at runtime.

- __bundle information property list__

  A collection of key-value pairs giving information about an [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g), stored in a file named `Info.plist` in its [application bundle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbi5degssc).

- __claim__

  Said of an [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g), to declare to Launch Services that it is capable of [open](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirbuosci)ing [document](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirduiqkh)s or [URL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbijdeurkc)s of a given type.

- __Core Foundation URL reference__

  A data object of type `CFURLRef` specifying a [URL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbijdeurkc).

- __creator signature__

  A four-character code associated with a file that identifies the [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g) that created it or that should be used to [open](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirbuosci) it.

- __default application__

  The [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g) selected by Launch Services, according to its own implicit [binding rules](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfceurcj), in which to [open](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirbuosci) a given [document](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirduiqkh) or [URL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbijdeurkc) in the absence of an explicit [binding preference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbincucskg) set by the user.

- __directory__

  A file-system object containing zero or more other named objects (files or other directories).

- __display name__

  A string used for displaying an [item](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjbbuoskj)’s name to the user, such as in the Finder or the Dock.

- __document__

  A unit or collection of data, contained in a file or [package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbindesqkb), that can be operated on by an [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g).

- __document file__

  A file containing a [document](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirduiqkh).

- __document package__

  A [package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbindesqkb) containing a [document](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirduiqkh) along with related resources.

- __document type__

  A family of [document file](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbireugskg)s characterized by a given [file type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbi5fegrcb), [creator signature](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbijfecssk), or [filename extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjbeucqse). Compare [URL type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbinfeor2i).

- __filename extension__

  A string of characters at the end of a filename, preceded by a period (`.`), that characterizes the nature of the file or the structure of its contents.

- __file-system reference__

  A data object of type `FSRef` designating a file residing on a local or remote file-system volume.

- __file type__

  A four-character code associated with a file that characterizes its nature or the structure of its contents.

- __folder__

  A [directory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbijceuq2e) presented to the user in such a way that its contents are accessible (subject to the appropriate permissions) for browsing. Compare [package](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbindesqkb).

- __item__

  Generically, an [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g), [document](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirduiqkh), or [URL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbijdeurkc) to be operated on by Launch Services.

- __item information record__

  A data structure of type `LSItemInfoRecord`, used by Launch Services to return information about an [item](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjbbuoskj).

- __kind string__

  A string used (in the Finder’s Get Info window, for example) to characterize the general nature of an [item](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjbbuoskj), such as `Application`, `Folder`, `Alias`, `JPEG Picture`, `QuickTime Movie`, or `FrameMaker Document`.

- __launch__

  To start up an [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g) that was not previously running. Compare [activate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbiveemqkf).

- __launch options__

  A set of flags specifying the manner in which an [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g) is to be [open](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirbuosci)ed.

- __launch sequence__

  The sequence of operations performed by an [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g) immediately on being [launch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbiveuerkh)ed, indicated visually to the user by the application’s icon “bouncing” in the Dock.

- __Launch Services__

  A Mac app programming interface that enables a running program to [open](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirbuosci) other [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g)s, [document](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirduiqkh)s, or [URL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbijdeurkc)s in a way similar to the Finder or the Dock.

- __Launch Services database__

  The data structure in which Launch Services records information about available [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g)s and the kinds of [document](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirduiqkh)s or [URL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbijdeurkc)s they are capable of [open](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirbuosci)ing.

- __launch specification__

  A data structure of type `LSLaunchFSRefSpec` or `LSLaunchURLSpec`, used to specify to Launch Services the manner in which an [item](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjbbuoskj) or items are to be [open](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirbuosci)ed.

- __MIME__

  (Multipurpose Internet Mail Extension) A protocol used for adding attachments to email messages.

- __MIME type__

  A string designating the type of data in an attachment transmitted via [MIME](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbizcumssb), such as `text/plain`, `image/jpeg`, `audio/mp3`, or `video/quicktime`.

- __open__

  Generically, to [launch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbiveuerkh) or [activate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbiveemqkf) an [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g) or to present a [document](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirduiqkh) or [URL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbijdeurkc) for viewing or editing within an application.

- __package__

  A [directory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbijceuq2e) presented to the user so that it appears to be a single file, and whose contents are ordinarily inaccessible for browsing by the user. Compare [folder](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbizcekq2k).

- __preferred application__

  The [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g) selected by Launch Services in which to open a given [document](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirduiqkh) or [URL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbijdeurkc), either through an explicit [binding preference](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbincucskg) set by the user or, in the absence of such a user preference, by applying Launch Services’ own implicit [binding rules](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfceurcj) for determining the item’s [default application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjjcucskd).

- __reference constant__

  An arbitrary data item available for use by a program to convey information for its own purposes in an operation or data structure.

- __register__

  To make an [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g) known to Launch Services, copying its [binding information](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbivbegrkh) into the [Launch Services database](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbi5euqqkg) and making it available for opening [document](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirduiqkh)s and [URL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbijdeurkc)s.

- __role__

  A characterization (such as `Editor` or `Viewer`) of the kinds of operations an [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g) is capable of performing on [document](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirduiqkh)s or [URL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbijdeurkc)s of a given type.

- __role mask__

  A parameter specifying the [role](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbiveukskh) or roles that an [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g) should [claim](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfbuir2e) with respect to a given [item](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjbbuoskj) in order to be considered a candidate for [open](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbirbuosci)ing that item.

- __scheme__

  The component of a [uniform resource locator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjjeemskb) (URL) that identifies the type of resource it represents or the protocol to be used for accessing it, such as `http`, `ftp`, `mailto`, or `file`.

- __scheme-definition dictionary__

  A dictionary, specified in an [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g)’s [bundle information property list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjjfeqqsh), that declares a particular [URL type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbinfeor2i) that the application [claim](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfbuir2e)s to handle. Compare [type-definition dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjffemqsc).

- __synchronous launch__

  A [launch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbiveuerkh) operation in which control does not return to the calling program until the launched [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g) has completed its [launch sequence](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbinaueq2k). Compare [asynchronous launch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbircukrkf).

- __type-definition dictionary__

  A dictionary, specified in an [application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfeusq2g)’s [bundle information property list](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjjfeqqsh), that declares a particular [document type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbivcegrse) that the application [claim](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjfbuir2e)s to handle. Compare [scheme-definition dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjbdukqkb).

- __uniform resource locator__

  A string, in a standard format, designating a file, Web page, or other resource, typically (but not necessarily) to be accessed via the Internet. Often used loosely in the context of Launch Services to refer to the resource so designated.

- __URL__

  See [uniform resource locator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjjeemskb).

- __URL type__

  A family of [URL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbijdeurkc)s characterized by a given [scheme](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjjaukr2c) component. Compare [document type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbivcegrse).

- __valid extension__

  A [filename extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjbeucqse) that does not contain spaces, periods, or characters that are not supported by the underlying file system. Compare [active extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwugqsbjjduorsd).

[Previous](Document%20Revision%20History.md)

