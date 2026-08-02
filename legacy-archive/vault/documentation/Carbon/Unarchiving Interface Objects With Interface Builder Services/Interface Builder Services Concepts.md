---
title: Unarchiving Interface Objects With Interface Builder Services
apple_id: TP30001005
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2004-02-17'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/UnarchivingIOwithIBS/ibs_concepts/IBSConcepts.html
archived_at: '2026-07-15T05:24:42.225924Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Unarchiving Interface Objects With Interface Builder Services](Introduction%20to%20Unarchiving%20Interface%20Objects%20With%20Interface%20Builder%20Services.md)


[Next](Interface%20Builder%20Services%20Tasks.md)[Previous](Introduction%20to%20Unarchiving%20Interface%20Objects%20With%20Interface%20Builder%20Services.md)

# Interface Builder Services Concepts

Interface Builder Services provides functions
that unarchive interface objects from _nib files_.
A nib file is an Interface Builder file; it contains a description
of one or more objects in a user interface. Before you use the functions
in Interface Builder Services, you may find it helpful to know a
bit more about Interface Builder, nib files, and strategies for
storing interface objects.

Interface Builder is an Apple development tool you can use
to build interfaces for your Carbon applications. It is a WYSIWYG
tool that lets you lay out user interfaces in a simple, intuitive
manner. You use it along with Project Builder, Apple’s main development
tool. Interface Builder and Project Builder are available on the
Mac OS X Developer CD.

You can find more information about using Interface Builder
in the online help provided with it.

A nib file contains the application’s interface-based resources.
It’s an Interface Builder file (the “ib” in “nib” stands
for Interface Builder) that contains descriptions of the interface elements
in your application. These descriptions use XML (extended markup
language), although you’ll never see, nor should you try to edit,
the XML in a nib file. A nib file can contain user-interface objects,
and references to any sounds, and images used in the interface.

A nib file can describe all or part of a user interface. Most
applications use two or more nib files, with one of them designated
as the main nib file. The main nib file contains the main menu and
any windows and panels you want to appear when your application
starts up. In addition to the main nib file, you can have one or
more nib files that you load whenever you need them. The additional
nib files are called _auxiliary nib files_. For
example, if your application is a word processor, you might have
an auxiliary nib file for a document window. Each time your user
creates a new document, you’d use Interface Builder Services to
unarchive a document window from the auxiliary nib file.

You can strategically store an application’s interface objects
in several nib files. When the application needs an interface object,
you can load the nib file which contains it. You’ll conserve memory
and improve program efficiency by following these guidelines:

- Store the
  main menu and perhaps a window in the main nib file. You should
  store a window in the main nib file only if the window always opens
  when the application starts up.
- Store each window or menu (such as an About window) that is
  likely to be used occasionally in a separate nib file. That way,
  you can call Interface Builder Services to load the window or menu
  only when a user requests it or when conditions warrant it.
- If your application uses a repeatable object, such as a word-processor
  document or a spreadsheet, store it in a document nib file. A _document
  nib file_ is an auxiliary nib file that’s used as a template
  for a document: it contains the user interface objects and other resources
  needed to make a document.

[Next](Interface%20Builder%20Services%20Tasks.md)[Previous](Introduction%20to%20Unarchiving%20Interface%20Objects%20With%20Interface%20Builder%20Services.md)

