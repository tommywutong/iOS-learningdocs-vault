---
title: Interactive Movies
apple_id: TP40000883
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-06-01'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/IQ_InteractiveMovies/preface/QT_Interactive_preface.html
archived_at: '2026-07-18T02:04:19.329558Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/QuickTime/IQ_InteractiveMovies/generalintro/1-General-Intro.html)

# Introduction to Interactive Movies

This book is a developer’s guide to building and developing interactive QuickTime movies with wired sprites and sprite animation, and is part of Apple’s Inside QuickTime: Technical Reference Library. It is intended primarily for content authors, Webmasters, and tool developers who need to understand the fundamentals of QuickTime interactivity and, specifically, how they can incorporate wired movies, sprites, sprite animation, and Flash into their own applications.

This book supersedes all existing documentation, including _Programming With Wired Movies and Sprite Animatio_n. It extends the content in those volumes and brings it up to date with the current release of QuickTime.

For information about building and developing interactive QuickTime movies with QuickTime VR, refer to the volume Interactive Movies: QuickTime VR.

The book is written as a companion volume to the QuickTime API Reference and supplements the latest documentation and updates to QuickTime that are available at: [http://developer.apple.com/documentation/Quicktime/QuickTime.html](https://developer.apple.com/documentation/Quicktime/QuickTime.html)

The book is divided into the following chapters:

- [Chapter 1, QuickTime Interactivity,](https://developer.apple.com/library/archive/documentation/QuickTime/IQ_InteractiveMovies/generalintro/1-General-Intro.html#//apple_ref/doc/uid/TP40000883-CH205-BCIJCJGJ) presents a general introduction to QuickTime interactivity with examples of movies that take advantage of QuickTime’s power and functionality to provide users with a rich media experience.
- [Chapter 2, QuickTime Sprites, Sprite Animation and Wired Movies,](https://developer.apple.com/library/archive/documentation/QuickTime/IQ_InteractiveMovies/introwiredsprites/2-Intro-Wired-Sprites.html#//apple_ref/doc/uid/TP40000883-CH206-BAJFCHFE) provides a conceptual overview of the QuickTime sprite, animation, and wired movie architecture, with each section laying down the fundamental building blocks.
- [Chapter 3, Sprite Media Handler,](https://developer.apple.com/library/archive/documentation/QuickTime/IQ_InteractiveMovies/spritemediahandler/3-Sprite-Media-Handler.html#//apple_ref/doc/uid/TP40000883-CH207-CJBEEIFB) describes the sprite media handler, a media handler you can use to add a sprite animation track to a QuickTime movie. The sprite media handler provides routines for manipulating the sprites and images in a sprite track.
- [Chapter 4, Authoring Wired Movies and Sprite Animations,](https://developer.apple.com/library/archive/documentation/QuickTime/IQ_InteractiveMovies/authoringwiredmovies/4-Authoring-Wired-Movies.html#//apple_ref/doc/uid/TP40000883-CH208-BCIDCFEG) describes how you can author wired movies and sprite animations using the sprite media handler.
- [Chapter 5, Using the Sprite Toolbox to Create Sprite Animations,](https://developer.apple.com/library/archive/documentation/QuickTime/IQ_InteractiveMovies/usingspriteanimation/5-Using-Sprite-Anim.html#//apple_ref/doc/uid/TP40000883-CH209-BBCFEAEI) discusses the sprite toolbox and how you can use it to add sprite-based animation to an application. The chapter is aimed at developers who are using the lower-level sprite toolbox APIs to create sprite animations in their applications, not in a QuickTime movie.
- [Chapter 6, Flash Media Handler,](https://developer.apple.com/library/archive/documentation/QuickTime/IQ_InteractiveMovies/flashmediahandler/6-Flash-Media-Handler.html#//apple_ref/doc/uid/TP40000883-CH210-CJBCBCCF) describes the Flash media handler, which was introduced in QuickTime 4. The Flash media handler allows a Macromedia Flash SWF 3.0 file to be treated as a track within a QuickTime movie. QuickTime 5 includes support for the interactive playback of SWF 4.0 files by extending the existing SWF importer, as well as the Flash media handler.
- [Chapter 7, Creating Advanced Interactive Movies,](https://developer.apple.com/library/archive/documentation/QuickTime/IQ_InteractiveMovies/advancedinteractive/7-Advanced-Interactive.html#//apple_ref/doc/uid/TP40000883-CH211-BCICIJJI) introduces you to some of the features that allow for the creation of more advanced, interactive movies.
- [Chapter 8, QuickTime Atoms and Atom Containers,](https://developer.apple.com/library/archive/documentation/QuickTime/IQ_InteractiveMovies/quicktimeatoms/8-QuickTime-Atoms.html#//apple_ref/doc/uid/TP40000883-CH212-BCICJDEI) introduces you to QuickTime atoms and atom containers, which QuickTime uses to store most of its data using specialized structures in memory. Movies themselves are atoms, as are tracks, media, and data samples.
- [Chapter 9, QuickTime and SMIL,](https://developer.apple.com/library/archive/documentation/QuickTime/IQ_InteractiveMovies/quicktimeandsmil/9-QuickTime%20and%20SMIL.html#//apple_ref/doc/uid/TP40000883-CH213-BBCDGADJ) introduces you to SMIL (pronounced “smile”), which stands for Synchronized Multimedia Integration Language. SMIL is a Web Consortium standard for describing multimedia presentations. QuickTime 4.1 and later can play SMIL presentations as if they were QuickTime movies.
- [Appendix A, QTWiredSprite.c Sample Code,](https://developer.apple.com/library/archive/documentation/QuickTime/IQ_InteractiveMovies/samplecodeappendix/Appendix-A-sample-code.html#//apple_ref/doc/uid/TP40000883-CH214-CJBJFHCE) presents sample code from `MakeActionSpriteMovie.c` that allows you to create a sample wired sprite movie containing one sprite track.

This book provides various conventions to present information. Words that require special treatment appear in specific fonts or font styles. Certain types of information use special fonts so that you can scan them quickly.

All code listings, reserved words, and the names of actual data structures, constants, fields, parameters, and functions are shown in Letter Gothic `(this is Letter Gothic)`.

Words that appear in boldface are key terms or concepts that are defined in the glossary.

There are several types of notes used in this book.

The functions described in this book are available using C interfaces. How you access them depends on the development environment you are using.

Code listings in this book are shown in ANSI C. They suggest methods of using various functions and illustrate techniques for accomplishing particular tasks. Although most code listings have been compiled and tested, Apple Computer Inc., does not intend for you to use these code samples in your application.

For any online updates to this book, check the QuickTime developers’ page on the World Wide Web at: [http://developer.apple.com/documentation/QuickTime/index.html](https://developer.apple.com/documentation/QuickTime/index.html)

For information about membership in Apple’s developer program, you should go to this URL: [http://developer.apple.com/membership](https://developer.apple.com/membership)

For Technical Support: [http://developer.apple.com/technicalsupport/index.html](https://developer.apple.com/technicalsupport/index.html)

For information on registering signatures, file types, and other technical information, contact

Macintosh Developer Technical Support Apple Computer, Inc. 1 Infinite Loop, M/S 303-2T Cupertino, CA 95014

[Next](https://developer.apple.com/library/archive/documentation/QuickTime/IQ_InteractiveMovies/generalintro/1-General-Intro.html)

