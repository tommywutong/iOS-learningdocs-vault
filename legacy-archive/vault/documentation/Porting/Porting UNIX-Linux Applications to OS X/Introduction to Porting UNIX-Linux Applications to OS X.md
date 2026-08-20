---
title: Porting UNIX/Linux Applications to OS X
apple_id: TP30001003
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/documentation/Porting/Conceptual/PortingUnix/intro/intro.html
archived_at: '2026-07-18T01:50:47.670584Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Overview%20of%20OS%20X.md)

# Introduction to Porting UNIX/Linux Applications to OS X

The UNIX Porting Guide is a first stop for UNIX developers coming to OS X. This document helps guide developers in bringing applications written for UNIX-based operating systems to OS X. It provides the background needed to understand the operating system. It touches on some of the design decisions, and it provides a listing and discussion of some of the main areas that you should be concerned with in bringing UNIX applications to OS X. It also points out some of the advanced features of OS X not available in traditional UNIX applications that you can add to your ported applications.

This document also provides an entry point for other documentation on various subjects that may be of interest if you are porting an application from a UNIX environment to OS X.

This document is an overview, not a tutorial. In many regards it is a companion to the more extensive _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_, but with a bias toward the UNIX developer.

This document also does not cover porting shell scripts to OS X. For more information about shell scripts and OS X, you should read _[Shell Scripting Primer](../../Shell%20Scripting%20Primer/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denry)_.

The introduction of UNIX-like operating systems such as FreeBSD and Linux for personal computers was a great step in bringing the power and stability of UNIX to the mass market. Generally though, these projects were driven by power users and developers for their own use, without making design decisions that would make UNIX palatable to consumers. OS X, on the other hand, was designed from the beginning with end users in mind.

With this operating system, Apple builds its well-known strengths in simplicity and elegance of design on a UNIX-based foundation. Rather than reinventing what has already been done well, Apple is combining their strengths with the strengths brought about by many years of advancement by the UNIX community.

Any UNIX developers can benefit from reading this book.

- In-house corporate application developers
- Commercial UNIX developers
- Open source developers
- Open source porters
- Higher education faculty, staff, and students
- Science and research developers

If you’re a commercial UNIX developer, you are already familiar with other UNIX-based systems and may want to understand the differences between other systems and OS X. You might be interested in porting the GUI from an X11 environment into a native graphics environment using Carbon or Cocoa. You may also have special needs such as direct hardware access, exclusive file access guarantees, and so on.

If you’re a corporate in-house developer (developing applications for internal use), you probably want to port applications with minimal code divergence.

If you’re an open source developer, you might want information about how to incorporate new technologies into your software, and may be interested in GUI porting, depending on your level of interest. Alternately, you might be interested only in quickly porting code to a new platform with minimal changes so that you can easily get your changes back into the official code base. If so, you may be more likely to use compatibility shims than to use new APIs.

No matter what “flavor” of developer you are, this book will provide information that is helpful to you and provide pointers to additional documents that may be of interest.

This document is a first stop for UNIX developers coming to OS X. It contains many links to more extensive documentation. Specific details of implementation are covered here only in cases where it is not adequately covered in other places in the documentation set.

To use this document most effectively, first read [Overview of OS X](Overview%20of%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbyfvkfawcsivddcmbr) to find out the basics about the Mac and to get some of the high-level information you need to begin your port. If you already have an application that builds on other UNIX-based platforms, [Compiling Your Code in OS X](Compiling%20Your%20Code%20in%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjqfvkfawcsivddcmbr) will help you find out how to compile your code on OS X.

Most of your effort, however, should be spent towards making decisions concerning which, if any, graphical user interface to implement with your application. [Choosing a Graphical Environment for Your Application](Choosing%20a%20Graphical%20Environment%20for%20Your%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjrfvkfawcsivddcmbr) helps you with this.

If you want to refactor your application to take advantage of the rich feature set of OS X, see [Additional Features](Additional%20Features.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjwfvkfawcsivddcmbr) for examples of features available in OS X.

Once you have a complete application, read [Distributing Your Application](Distributing%20Your%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjvfvkfawcsivddcmbr) for information on getting your application to OS X users.

Developer documentation can be found at Apple’s developer website at [http://developer.apple.com/](https://developer.apple.com/). This site contains reference, conceptual, and tutorial material for the many facets of development on OS X. The OS X Developer Tools CD includes a snapshot of the developer documentation, which can be searched for and viewed in Xcode’s doc viewer. The `man` pages are also included with the OS X Developer Tools.

Apple Developer Connection (ADC) offers a variety of membership levels to help you in your development. These range from free memberships that give you access to developer software, to paid memberships that provide support incidents as well as the possibility of software seeds. More information on memberships is available at [http://developer.apple.com](https://developer.apple.com/programs/mac/).

Once a year in early Summer, Apple hosts the Worldwide Developers Conference (WWDC) in the San Francisco, California Bay area. This is an extremely valuable resource for developers trying to get an overall picture of OS X as well as specific implementation details of individual technologies. Information on WWDC is available on the ADC website.

Apple hosts an extensive array of public mailing lists. These are available for public subscription and searching at [http://lists.apple.com](http://lists.apple.com/). The _unix-porting_ list is highly recommended. The _darwin-dev_ and _darwinos-users_ lists also offer much help but less specific to the task of porting.

In addition to Apple’s own resources, many external resources exist, for example, O’Reilly’s Mac DevCenter, [http://www.oreillynet.com/mac/](http://www.oreillynet.com/mac/).

[Next](Overview%20of%20OS%20X.md)

